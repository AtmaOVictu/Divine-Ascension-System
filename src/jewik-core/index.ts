export type EntryType = "ORDINARY_WORD" | "INTERNAL_OPERATOR";

export type DictionaryLayerKind =
  | "OFFICIAL"
  | "COMMUNITY"
  | "DERIVED"
  | "UNAVAILABLE";

export type ProofStatus = "DRAFT" | "UNDER_REVIEW" | "PROVEN";

export type EvidenceItem = {
  id: string;
  text: string;
  source: string;
  createdAt: string;
};

export type DictionaryLayer = {
  kind: DictionaryLayerKind;
  meaning: string;
  notes: string;
};

export type JewikCut = {
  expression: string;
  notes: string;
};

export type VersionHistoryItem = {
  id: string;
  at: string;
  event: string;
};

export type LexiconEntry = {
  id: string;
  term: string;
  type: EntryType;
  dictionaryLayer: DictionaryLayer;
  segmentation: string;
  phoneticNotes: string;
  operatorMapping: string;
  antinomies: string[];
  jewikCut: JewikCut;
  evidence: EvidenceItem[];
  proofStatus: ProofStatus;
  proofNotes: string;
  versionHistory: VersionHistoryItem[];
  exportText: string;
  createdAt: string;
  updatedAt: string;
};

export type WorkbenchState = {
  entries: LexiconEntry[];
};

export type ValidationIssue = {
  code:
    | "MISSING_TERM"
    | "MISSING_DICTIONARY_MEANING"
    | "MISSING_CUT"
    | "MISSING_OPERATOR_MAPPING"
    | "PROVEN_REQUIRES_EVIDENCE"
    | "PROVEN_REQUIRES_DICTIONARY_LAYER";
  severity: "error" | "warning";
  message: string;
};

export type ValidationResult = {
  issues: ValidationIssue[];
  canMarkProven: boolean;
  isValid: boolean;
};

export type ProofTransitionResult = {
  entry: LexiconEntry;
  changed: boolean;
  blocked: boolean;
  message: string;
};

export const entryTypeOptions: EntryType[] = [
  "ORDINARY_WORD",
  "INTERNAL_OPERATOR",
];

export const dictionaryLayerKindOptions: DictionaryLayerKind[] = [
  "OFFICIAL",
  "COMMUNITY",
  "DERIVED",
  "UNAVAILABLE",
];

export const proofStatusOptions: ProofStatus[] = [
  "DRAFT",
  "UNDER_REVIEW",
  "PROVEN",
];

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null;
}

function readString(
  record: Record<string, unknown>,
  key: string,
  fallback = "",
): string {
  return typeof record[key] === "string" ? record[key] : fallback;
}

function normalizeList(values: string[]): string[] {
  return values
    .map((value) => value.trim())
    .filter((value, index, collection) => value.length > 0 && collection.indexOf(value) === index);
}

function normalizeEvidenceItem(value: unknown): EvidenceItem | null {
  if (!isRecord(value)) {
    return null;
  }

  const text = readString(value, "text").trim();
  if (!text) {
    return null;
  }

  return {
    id: readString(value, "id", createId("evidence")),
    text,
    source: readString(value, "source"),
    createdAt: readString(value, "createdAt", stamp()),
  };
}

function normalizeVersionHistoryItem(value: unknown): VersionHistoryItem | null {
  if (!isRecord(value)) {
    return null;
  }

  const event = readString(value, "event").trim();
  if (!event) {
    return null;
  }

  return {
    id: readString(value, "id", createId("history")),
    at: readString(value, "at", stamp()),
    event,
  };
}

function normalizeEntryType(value: unknown): EntryType {
  return value === "INTERNAL_OPERATOR" ? "INTERNAL_OPERATOR" : "ORDINARY_WORD";
}

function normalizeDictionaryLayerKind(value: unknown): DictionaryLayerKind {
  return dictionaryLayerKindOptions.includes(value as DictionaryLayerKind)
    ? (value as DictionaryLayerKind)
    : "OFFICIAL";
}

function normalizeProofStatus(value: unknown): ProofStatus {
  return proofStatusOptions.includes(value as ProofStatus)
    ? (value as ProofStatus)
    : "DRAFT";
}

function serializeEvidenceLines(entry: LexiconEntry): string {
  if (entry.evidence.length === 0) {
    return "No evidence.";
  }

  return entry.evidence
    .map((item, index) => {
      const source = item.source.trim() ? ` (${item.source.trim()})` : "";
      return `${index + 1}. ${item.text}${source}`;
    })
    .join("\n");
}

function serializeHistoryLines(entry: LexiconEntry): string {
  if (entry.versionHistory.length === 0) {
    return "No version history.";
  }

  return entry.versionHistory
    .map((item) => `${item.at} :: ${item.event}`)
    .join("\n");
}

function buildCardText(entry: LexiconEntry): string {
  const antinomies = entry.antinomies.length > 0 ? entry.antinomies.join(" | ") : "none";

  return [
    `TERM: ${entry.term || "(empty term)"}`,
    `TYPE: ${entry.type}`,
    `LAYER: ${entry.dictionaryLayer.kind}`,
    `MEANING: ${entry.dictionaryLayer.meaning || "(empty meaning)"}`,
    `CUT: ${entry.jewikCut.expression || "(empty cut)"}`,
    `PROOF: ${entry.proofStatus}`,
    `EVIDENCE COUNT: ${entry.evidence.length}`,
    `OPERATOR MAP: ${entry.operatorMapping || "(empty mapping)"}`,
    `ANTINOMIES: ${antinomies}`,
  ].join("\n");
}

function createHistoryItem(event: string, at = stamp()): VersionHistoryItem {
  return {
    id: createId("history"),
    at,
    event,
  };
}

function appendHistoryIfMissing(
  entry: LexiconEntry,
  event: string,
  at = stamp(),
): LexiconEntry {
  const lastEvent = entry.versionHistory[entry.versionHistory.length - 1]?.event;
  if (lastEvent === event) {
    return entry;
  }

  return {
    ...entry,
    versionHistory: [...entry.versionHistory, createHistoryItem(event, at)],
  };
}

type ProofBlockingReason =
  | "missing-evidence"
  | "unavailable-dictionary-layer"
  | "missing-dictionary-meaning";

function getProofPrerequisites(entry: LexiconEntry): {
  hasEvidence: boolean;
  hasDictionaryLayer: boolean;
  hasDictionaryMeaning: boolean;
} {
  return {
    hasEvidence: entry.evidence.length > 0,
    hasDictionaryLayer: entry.dictionaryLayer.kind !== "UNAVAILABLE",
    hasDictionaryMeaning: entry.dictionaryLayer.meaning.trim().length > 0,
  };
}

function getProofBlockingReason(entry: LexiconEntry): ProofBlockingReason | null {
  const { hasEvidence, hasDictionaryLayer, hasDictionaryMeaning } = getProofPrerequisites(entry);

  if (!hasEvidence) {
    return "missing-evidence";
  }

  if (!hasDictionaryLayer) {
    return "unavailable-dictionary-layer";
  }

  if (!hasDictionaryMeaning) {
    return "missing-dictionary-meaning";
  }

  return null;
}

function stabilizeEntry(
  entry: LexiconEntry,
  touch: boolean,
  proofContractContext: "sanitize" | "remove-evidence" | "general" | null = null,
): LexiconEntry {
  const synced = syncEntry(entry, touch);
  const blockingReason =
    synced.proofStatus === "PROVEN" ? getProofBlockingReason(synced) : null;

  if (blockingReason === null) {
    return synced;
  }

  let proofContractEvent = "Proof status downgraded to UNDER_REVIEW because PROVEN requires evidence.";

  if (blockingReason === "missing-evidence") {
    proofContractEvent =
      proofContractContext === "sanitize"
        ? "Sanitizer downgraded PROVEN to UNDER_REVIEW because evidence was empty."
        : proofContractContext === "remove-evidence"
          ? "Proof status downgraded to UNDER_REVIEW because evidence was removed."
          : "Proof status downgraded to UNDER_REVIEW because PROVEN requires evidence.";
  } else if (blockingReason === "unavailable-dictionary-layer") {
    proofContractEvent =
      proofContractContext === "sanitize"
        ? "Sanitizer downgraded PROVEN to UNDER_REVIEW because dictionary layer was UNAVAILABLE."
        : "Proof status downgraded to UNDER_REVIEW because dictionary layer was UNAVAILABLE.";
  } else if (blockingReason === "missing-dictionary-meaning") {
    proofContractEvent =
      proofContractContext === "sanitize"
        ? "Sanitizer downgraded PROVEN to UNDER_REVIEW because dictionary meaning was empty."
        : "Proof status downgraded to UNDER_REVIEW because dictionary meaning was empty.";
  }

  return syncEntry(
    appendHistoryIfMissing(
      {
        ...synced,
        proofStatus: "UNDER_REVIEW",
      },
      proofContractEvent,
    ),
    false,
  );
}

function syncEntry(entry: LexiconEntry, touch: boolean): LexiconEntry {
  const next: LexiconEntry = {
    ...entry,
    term: entry.term.trimStart(),
    type: normalizeEntryType(entry.type),
    segmentation: entry.segmentation.trim(),
    phoneticNotes: entry.phoneticNotes.trim(),
    operatorMapping: entry.operatorMapping.trim(),
    antinomies: normalizeList(entry.antinomies),
    proofStatus: normalizeProofStatus(entry.proofStatus),
    proofNotes: entry.proofNotes.trim(),
    dictionaryLayer: {
      kind: normalizeDictionaryLayerKind(entry.dictionaryLayer.kind),
      meaning: entry.dictionaryLayer.meaning.trim(),
      notes: entry.dictionaryLayer.notes.trim(),
    },
    jewikCut: {
      expression: entry.jewikCut.expression.trim(),
      notes: entry.jewikCut.notes.trim(),
    },
    evidence: entry.evidence
      .map((item) => normalizeEvidenceItem(item))
      .filter((item): item is EvidenceItem => item !== null),
    versionHistory: entry.versionHistory
      .map((item) => normalizeVersionHistoryItem(item))
      .filter((item): item is VersionHistoryItem => item !== null),
    exportText: "",
    updatedAt: touch ? stamp() : entry.updatedAt,
  };

  next.exportText = buildCardText(next);
  return next;
}

export function stamp(): string {
  return new Date().toISOString();
}

export function createId(prefix: string): string {
  const randomPart =
    typeof crypto !== "undefined" && typeof crypto.randomUUID === "function"
      ? crypto.randomUUID()
      : `${Date.now()}-${Math.round(Math.random() * 100000)}`;

  return `${prefix}-${randomPart}`;
}

export function formatDate(value: string): string {
  return new Intl.DateTimeFormat("sl-SI", {
    dateStyle: "medium",
    timeStyle: "short",
  }).format(new Date(value));
}

export function createBlankEntry(): LexiconEntry {
  const now = stamp();
  const entry: LexiconEntry = {
    id: createId("entry"),
    term: "",
    type: "ORDINARY_WORD",
    dictionaryLayer: {
      kind: "OFFICIAL",
      meaning: "",
      notes: "",
    },
    segmentation: "",
    phoneticNotes: "",
    operatorMapping: "",
    antinomies: [],
    jewikCut: {
      expression: "",
      notes: "",
    },
    evidence: [],
    proofStatus: "DRAFT",
    proofNotes: "",
    versionHistory: [
      {
        id: createId("history"),
        at: now,
        event: "Entry created.",
      },
    ],
    exportText: "",
    createdAt: now,
    updatedAt: now,
  };

  return stabilizeEntry(entry, false);
}

export function createSampleEntry(): LexiconEntry {
  const now = stamp();
  const entry: LexiconEntry = {
    id: "entry-beseda",
    term: "beseda",
    type: "ORDINARY_WORD",
    dictionaryLayer: {
      kind: "OFFICIAL",
      meaning: "A word is a unit of meaning that can also act inside a frame.",
      notes: "Phase 1 keeps the layer explicit and separate.",
    },
    segmentation: "be-se-da",
    phoneticNotes: "Stress on the second syllable in this working note.",
    operatorMapping: "WORD_ACT",
    antinomies: ["description vs action", "sound vs meaning"],
    jewikCut: {
      expression: "beseda -> pomen -> dejanje",
      notes: "The cut separates raw sound, stable meaning, and enacted effect.",
    },
    evidence: [
      {
        id: "evidence-beseda-1",
        text: "Working source note: a word can describe and also trigger action.",
        source: "Phase 1 sample",
        createdAt: now,
      },
    ],
    proofStatus: "UNDER_REVIEW",
    proofNotes: "Not canon. Evidence exists, so PROVEN can be attempted.",
    versionHistory: [
      {
        id: "history-beseda-1",
        at: now,
        event: "Sample entry seeded for Phase 1.",
      },
    ],
    exportText: "",
    createdAt: now,
    updatedAt: now,
  };

  return stabilizeEntry(entry, false);
}

export function createInitialWorkbenchState(): WorkbenchState {
  return {
    entries: [createSampleEntry()],
  };
}

export function sanitizeWorkbenchState(raw: unknown): WorkbenchState {
  if (!isRecord(raw) || !Array.isArray(raw.entries)) {
    return { entries: [] };
  }

  const entries = raw.entries
    .map((value) => {
      if (!isRecord(value)) {
        return null;
      }

      const dictionaryLayer = isRecord(value.dictionaryLayer)
        ? value.dictionaryLayer
        : {};
      const jewikCut = isRecord(value.jewikCut) ? value.jewikCut : {};
      const evidence = Array.isArray(value.evidence) ? value.evidence : [];
      const history = Array.isArray(value.versionHistory)
        ? value.versionHistory
        : [];
      const antinomies = Array.isArray(value.antinomies)
        ? value.antinomies.filter((item): item is string => typeof item === "string")
        : [];

      const candidate: LexiconEntry = {
        id: readString(value, "id", createId("entry")),
        term: readString(value, "term"),
        type: normalizeEntryType(value.type),
        dictionaryLayer: {
          kind: normalizeDictionaryLayerKind(dictionaryLayer.kind),
          meaning: readString(dictionaryLayer, "meaning"),
          notes: readString(dictionaryLayer, "notes"),
        },
        segmentation: readString(value, "segmentation"),
        phoneticNotes: readString(value, "phoneticNotes"),
        operatorMapping: readString(value, "operatorMapping"),
        antinomies,
        jewikCut: {
          expression: readString(jewikCut, "expression"),
          notes: readString(jewikCut, "notes"),
        },
        evidence,
        proofStatus: normalizeProofStatus(value.proofStatus),
        proofNotes: readString(value, "proofNotes"),
        versionHistory: history,
        exportText: readString(value, "exportText"),
        createdAt: readString(value, "createdAt", stamp()),
        updatedAt: readString(value, "updatedAt", stamp()),
      };

      return stabilizeEntry(candidate, false, "sanitize");
    })
    .filter((entry): entry is LexiconEntry => entry !== null);

  return { entries };
}

export function refreshEntry(entry: LexiconEntry): LexiconEntry {
  return stabilizeEntry(entry, true, "general");
}

export function recordEntryEvent(entry: LexiconEntry, event: string): LexiconEntry {
  return stabilizeEntry(
    appendHistoryIfMissing(entry, event),
    true,
    "general",
  );
}

export function addEvidence(
  entry: LexiconEntry,
  payload: { text: string; source: string },
): LexiconEntry {
  const text = payload.text.trim();
  if (!text) {
    return entry;
  }

  const next = stabilizeEntry(
    {
      ...entry,
      evidence: [
        ...entry.evidence,
        {
          id: createId("evidence"),
          text,
          source: payload.source.trim(),
          createdAt: stamp(),
        },
      ],
    },
    true,
  );

  return recordEntryEvent(next, "Evidence added.");
}

export function removeEvidence(entry: LexiconEntry, evidenceId: string): LexiconEntry {
  const nextEvidence = entry.evidence.filter((item) => item.id !== evidenceId);
  if (nextEvidence.length === entry.evidence.length) {
    return entry;
  }

  const next = stabilizeEntry(
    {
      ...entry,
      evidence: nextEvidence,
    },
    true,
    "remove-evidence",
  );

  return recordEntryEvent(next, "Evidence removed.");
}

export function validateEntry(entry: LexiconEntry): ValidationResult {
  const issues: ValidationIssue[] = [];
  const { hasEvidence, hasDictionaryLayer, hasDictionaryMeaning } = getProofPrerequisites(entry);
  const requiresProofReadyDictionary = hasEvidence || entry.proofStatus === "PROVEN";

  if (!entry.term.trim()) {
    issues.push({
      code: "MISSING_TERM",
      severity: "error",
      message: "Term is required.",
    });
  }

  if (
    entry.dictionaryLayer.kind !== "UNAVAILABLE" &&
    !hasDictionaryMeaning
  ) {
    issues.push({
      code: "MISSING_DICTIONARY_MEANING",
      severity: "error",
      message: "Dictionary meaning is required unless the layer is UNAVAILABLE.",
    });
  }

  if (
    requiresProofReadyDictionary &&
    (!hasDictionaryLayer || !hasDictionaryMeaning)
  ) {
    issues.push({
      code: "PROVEN_REQUIRES_DICTIONARY_LAYER",
      severity: "error",
      message: "PROVEN requires an available dictionary layer with non-empty meaning.",
    });
  }

  if (entry.type === "INTERNAL_OPERATOR" && !entry.operatorMapping.trim()) {
    issues.push({
      code: "MISSING_OPERATOR_MAPPING",
      severity: "error",
      message: "Internal operators require an explicit JEWIK operator mapping.",
    });
  }

  if (!entry.jewikCut.expression.trim()) {
    issues.push({
      code: "MISSING_CUT",
      severity: "warning",
      message: "JEWIK cut is still empty.",
    });
  }

  if (entry.proofStatus === "PROVEN" && !hasEvidence) {
    issues.push({
      code: "PROVEN_REQUIRES_EVIDENCE",
      severity: "error",
      message: "PROVEN requires at least one evidence item.",
    });
  }

  return {
    issues,
    canMarkProven: hasEvidence && hasDictionaryLayer && hasDictionaryMeaning,
    isValid: issues.every((issue) => issue.severity !== "error"),
  };
}

export function setProofStatus(
  entry: LexiconEntry,
  nextStatus: ProofStatus,
): ProofTransitionResult {
  if (nextStatus === "PROVEN") {
    const blockingReason = getProofBlockingReason(entry);

    if (blockingReason === "missing-evidence") {
      return {
        entry: recordEntryEvent(entry, "Blocked PROVEN attempt without evidence."),
        changed: false,
        blocked: true,
        message: "Blocked: PROVEN requires evidence.",
      };
    }

    if (blockingReason === "unavailable-dictionary-layer") {
      return {
        entry: recordEntryEvent(
          entry,
          "Blocked PROVEN attempt because dictionary layer was UNAVAILABLE.",
        ),
        changed: false,
        blocked: true,
        message: "Blocked: PROVEN requires an available dictionary layer.",
      };
    }

    if (blockingReason === "missing-dictionary-meaning") {
      return {
        entry: recordEntryEvent(
          entry,
          "Blocked PROVEN attempt because dictionary meaning was empty.",
        ),
        changed: false,
        blocked: true,
        message: "Blocked: PROVEN requires dictionary meaning.",
      };
    }
  }

  const next = recordEntryEvent(
    stabilizeEntry(
      {
        ...entry,
        proofStatus: nextStatus,
      },
      true,
      "general",
    ),
    `Proof status set to ${nextStatus}.`,
  );

  return {
    entry: next,
    changed: nextStatus !== entry.proofStatus,
    blocked: false,
    message: `Proof status is now ${nextStatus}.`,
  };
}

export function buildCardTextExport(entry: LexiconEntry): string {
  return stabilizeEntry(entry, false, "general").exportText;
}

export function buildMarkdownExport(entry: LexiconEntry): string {
  const current = stabilizeEntry(entry, false, "general");
  const antinomies =
    current.antinomies.length > 0
      ? current.antinomies.map((item) => `- ${item}`).join("\n")
      : "- none";

  return [
    `# ${current.term || "(empty term)"}`,
    "",
    `- type: ${current.type}`,
    `- proofStatus: ${current.proofStatus}`,
    `- evidenceCount: ${current.evidence.length}`,
    `- dictionaryLayer: ${current.dictionaryLayer.kind}`,
    `- segmentation: ${current.segmentation || "(empty)"}`,
    `- operatorMapping: ${current.operatorMapping || "(empty)"}`,
    "",
    "## Dictionary Meaning",
    current.dictionaryLayer.meaning || "(empty)",
    "",
    "## Dictionary Layer Notes",
    current.dictionaryLayer.notes || "(empty)",
    "",
    "## Phonetic Notes",
    current.phoneticNotes || "(empty)",
    "",
    "## JEWIK Cut",
    current.jewikCut.expression || "(empty)",
    "",
    "## Cut Notes",
    current.jewikCut.notes || "(empty)",
    "",
    "## Antinomies",
    antinomies,
    "",
    "## Evidence",
    serializeEvidenceLines(current),
    "",
    "## Proof Notes",
    current.proofNotes || "(empty)",
    "",
    "## Version History",
    serializeHistoryLines(current),
  ].join("\n");
}

export function buildJsonExport(entry: LexiconEntry): string {
  return JSON.stringify(stabilizeEntry(entry, false, "general"), null, 2);
}
