import {
  addEvidence,
  buildCardTextExport,
  buildJsonExport,
  buildMarkdownExport,
  createBlankEntry,
  createInitialWorkbenchState,
  recordEntryEvent,
  removeEvidence,
  sanitizeWorkbenchState,
  setProofStatus,
  validateEntry,
} from "../jewik-core";
import { createEmptyState, createSampleState } from "../domain/sampleData";
import conceptAliases from "../jewik-book-engine/conceptAliases";
import {
  buildConceptReport,
  findAliasMatches,
  normalizeConcept,
} from "../jewik-book-engine/conceptReport";
import {
  createProjectPackage,
  isProjectPackage,
  parseProjectPackage,
  PROJECT_PACKAGE_TYPE,
  PROJECT_PACKAGE_VERSION,
  readWorkspaceFromProjectPackage,
  serializeProjectPackage,
} from "../jewik-book-engine/projectPackage";
import { seedExcerpts } from "../jewik-book-engine/seedData";
import { createDefaultProjectWorkspace } from "../jewik-book-engine/storage";
import {
  createProject,
  deleteProject,
  PROJECT_REGISTRY_STORAGE_KEY,
  readProjectRegistry,
  readProjectState,
  readState as readStudioState,
  renameProject,
  setActiveProjectId,
  STORAGE_KEY,
  writeProjectState,
  writeState as writeStudioState,
} from "../store/localStore";

const assert = {
  equal<T>(actual: T, expected: T, message: string): void {
    if (actual !== expected) {
      throw new Error(`${message} Expected: ${String(expected)}. Actual: ${String(actual)}.`);
    }
  },
  ok(value: unknown, message: string): void {
    if (!value) {
      throw new Error(message);
    }
  },
};

function createStorageMock(seed: Record<string, string> = {}): Storage {
  const values = new Map<string, string>(Object.entries(seed));

  return {
    get length() {
      return values.size;
    },
    clear() {
      values.clear();
    },
    getItem(key: string) {
      return values.has(key) ? values.get(key)! : null;
    },
    key(index: number) {
      return [...values.keys()][index] ?? null;
    },
    removeItem(key: string) {
      values.delete(key);
    },
    setItem(key: string, value: string) {
      values.set(key, value);
    },
  };
}

function setWindowMock(localStorage: Storage): PropertyDescriptor | undefined {
  const previousDescriptor = Object.getOwnPropertyDescriptor(globalThis, "window");

  Object.defineProperty(globalThis, "window", {
    value: { localStorage },
    configurable: true,
    writable: true,
  });

  return previousDescriptor;
}

function restoreWindow(previousDescriptor: PropertyDescriptor | undefined): void {
  if (previousDescriptor) {
    Object.defineProperty(globalThis, "window", previousDescriptor);
    return;
  }

  delete (globalThis as { window?: unknown }).window;
}

function main(): void {
  const initial = createInitialWorkbenchState();
  assert.equal(initial.entries.length, 1, "Phase 1 seed must expose one sample entry.");

  const sample = initial.entries[0];
  assert.ok(sample, "Sample entry must exist.");
  assert.equal(sample.term, "beseda", "Sample entry term must remain stable.");
  assert.equal(sample.proofStatus, "UNDER_REVIEW", "Sample entry must start under review.");
  assert.equal(sample.evidence.length, 1, "Sample entry must include one evidence item.");

  const blank = createBlankEntry();
  const blankValidation = validateEntry(blank);
  assert.equal(blankValidation.canMarkProven, false, "Blank entry must not allow PROVEN.");
  assert.ok(
    blankValidation.issues.some((issue) => issue.code === "MISSING_TERM"),
    "Blank entry must require a term.",
  );

  const blockedProof = setProofStatus(blank, "PROVEN");
  assert.equal(blockedProof.blocked, true, "PROVEN without evidence must be blocked.");
  assert.equal(blockedProof.entry.proofStatus, "DRAFT", "Blocked proof must preserve prior status.");
  assert.ok(
    blockedProof.entry.versionHistory.some((item) =>
      item.event.includes("Blocked PROVEN attempt without evidence."),
    ),
    "Blocked proof attempt must be recorded in version history.",
  );

  const evidenced = addEvidence(blank, {
    text: "Operational note: the entry now has supporting evidence.",
    source: "proofCheck",
  });
  assert.equal(evidenced.evidence.length, 1, "Evidence must be appended.");

  const proven = setProofStatus(
    {
      ...evidenced,
      dictionaryLayer: {
        ...evidenced.dictionaryLayer,
        meaning: "Operational working meaning for proof transition.",
      },
    },
    "PROVEN",
  );
  assert.equal(proven.blocked, false, "PROVEN with evidence must succeed.");
  assert.equal(proven.entry.proofStatus, "PROVEN", "Proof status must become PROVEN.");

  const provenWithTwoEvidence = addEvidence(proven.entry, {
    text: "Secondary evidence item for partial removal invariant.",
    source: "proofCheck",
  });
  assert.equal(
    provenWithTwoEvidence.proofStatus,
    "PROVEN",
    "Adding more evidence must keep a PROVEN entry in PROVEN state.",
  );
  assert.equal(
    provenWithTwoEvidence.evidence.length,
    2,
    "Partial removal invariant requires two evidence items before one is removed.",
  );

  const stillProvenAfterPartialEvidenceRemoval = removeEvidence(
    provenWithTwoEvidence,
    provenWithTwoEvidence.evidence[0]!.id,
  );
  assert.equal(
    stillProvenAfterPartialEvidenceRemoval.proofStatus,
    "PROVEN",
    "Removing one of multiple evidence items must not downgrade PROVEN.",
  );
  assert.equal(
    stillProvenAfterPartialEvidenceRemoval.evidence.length,
    1,
    "Removing one of two evidence items must leave one evidence item behind.",
  );

  const downgradedAfterEvidenceRemoval = removeEvidence(proven.entry, proven.entry.evidence[0]!.id);
  assert.equal(
    downgradedAfterEvidenceRemoval.proofStatus,
    "UNDER_REVIEW",
    "Removing the last evidence item must downgrade PROVEN to UNDER_REVIEW.",
  );
  assert.ok(
    downgradedAfterEvidenceRemoval.versionHistory.some((item: { event: string }) =>
      item.event.includes("Proof status downgraded to UNDER_REVIEW because evidence was removed."),
    ),
    "Evidence removal downgrade must be written into version history.",
  );

  const provenValidation = validateEntry(proven.entry);
  assert.equal(provenValidation.isValid, false, "PROVEN blank entry must still fail other required fields.");
  assert.ok(
    !provenValidation.issues.some((issue) => issue.code === "PROVEN_REQUIRES_EVIDENCE"),
    "Evidence must satisfy the PROVEN rule.",
  );

  const recorded = recordEntryEvent(proven.entry, "Manual export test.");
  assert.equal(
    recorded.versionHistory[recorded.versionHistory.length - 1]?.event,
    "Manual export test.",
    "Version history must be append-only.",
  );
  const recordedJsonText = buildJsonExport(recorded);
  const recordedJson = JSON.parse(recordedJsonText) as {
    versionHistory?: Array<{ event?: string }>;
  };
  const recordedJsonHistory = recordedJson.versionHistory ?? [];
  assert.equal(
    recordedJsonHistory[recordedJsonHistory.length - 1]?.event,
    "Manual export test.",
    "JSON export must preserve appended version history events.",
  );
  const recordedMarkdown = buildMarkdownExport(recorded);
  assert.ok(
    recordedMarkdown.includes("Manual export test."),
    "Markdown export must preserve appended version history event text.",
  );

  const markdown = buildMarkdownExport(sample);
  assert.ok(markdown.includes("# beseda"), "Markdown export must include the term heading.");
  assert.ok(markdown.includes("## Evidence"), "Markdown export must include the evidence section.");

  const cardText = buildCardTextExport(sample);
  assert.ok(cardText.includes("TERM: beseda"), "Card export must include the term.");
  assert.ok(cardText.includes("PROOF: UNDER_REVIEW"), "Card export must include proof status.");
  assert.ok(cardText.includes("EVIDENCE COUNT: 1"), "Card export must include evidence count.");

  const jsonText = buildJsonExport(sample);
  const parsedJson = JSON.parse(jsonText) as {
    term?: string;
    exportText?: string;
    proofStatus?: string;
    evidence?: Array<unknown>;
  };
  assert.equal(parsedJson.term, "beseda", "JSON export must preserve the term.");
  assert.ok(parsedJson.exportText, "JSON export must preserve derived export text.");
  const roundtripState = sanitizeWorkbenchState({ entries: [parsedJson] });
  assert.equal(roundtripState.entries.length, 1, "Valid JSON export roundtrip must keep one entry.");
  assert.equal(roundtripState.entries[0]?.term, "beseda", "Roundtrip must preserve the sample term.");
  assert.equal(
    roundtripState.entries[0]?.proofStatus,
    "UNDER_REVIEW",
    "Roundtrip must preserve the sample proof status.",
  );
  assert.equal(
    roundtripState.entries[0]?.evidence.length,
    1,
    "Roundtrip must preserve the sample evidence count.",
  );
  assert.equal(
    validateEntry(roundtripState.entries[0]!).isValid,
    true,
    "Valid JSON export roundtrip must remain valid after sanitize.",
  );

  const sanitized = sanitizeWorkbenchState({
    entries: [
      {
        term: "rez",
        type: "INTERNAL_OPERATOR",
        dictionaryLayer: {
          kind: "DERIVED",
          meaning: "A cut that separates a frame.",
          notes: "",
        },
        segmentation: "rez",
        phoneticNotes: "",
        operatorMapping: "CUT",
        antinomies: ["inside vs outside"],
        jewikCut: {
          expression: "inside -> cut -> outside",
          notes: "",
        },
        evidence: [],
        proofStatus: "DRAFT",
        proofNotes: "",
        versionHistory: [],
      },
    ],
  });
  assert.equal(sanitized.entries.length, 1, "Sanitizer must keep one valid entry.");
  assert.equal(sanitized.entries[0]?.term, "rez", "Sanitizer must preserve provided term.");
  assert.ok(sanitized.entries[0]?.exportText, "Sanitizer must derive export text.");
  assert.equal(
    validateEntry(sanitized.entries[0]!).isValid,
    true,
    "Internal operator with mapping must remain valid.",
  );

  const invalidOperator = sanitizeWorkbenchState({
    entries: [
      {
        term: "rez",
        type: "INTERNAL_OPERATOR",
        dictionaryLayer: {
          kind: "DERIVED",
          meaning: "A cut that separates a frame.",
          notes: "",
        },
        segmentation: "rez",
        phoneticNotes: "",
        operatorMapping: "",
        antinomies: [],
        jewikCut: {
          expression: "inside -> cut -> outside",
          notes: "",
        },
        evidence: [],
        proofStatus: "DRAFT",
        proofNotes: "",
        versionHistory: [],
      },
    ],
  });
  assert.ok(
    validateEntry(invalidOperator.entries[0]!).issues.some((issue) => issue.code === "MISSING_OPERATOR_MAPPING"),
    "Internal operators without mapping must fail validation.",
  );

  const invalidOperatorJsonText = buildJsonExport(invalidOperator.entries[0]!);
  const invalidOperatorJson = JSON.parse(invalidOperatorJsonText) as {
    type?: string;
    operatorMapping?: string;
  };
  assert.equal(
    invalidOperatorJson.type,
    "INTERNAL_OPERATOR",
    "JSON export must preserve INTERNAL_OPERATOR type for invalid operator entries.",
  );
  assert.equal(
    invalidOperatorJson.operatorMapping,
    "",
    "JSON export must preserve empty operatorMapping for invalid operator entries.",
  );

  const sanitizedInvalidProven = sanitizeWorkbenchState({
    entries: [
      {
        id: "entry-invalid-proven",
        term: "dokaz",
        type: "ORDINARY_WORD",
        dictionaryLayer: {
          kind: "OFFICIAL",
          meaning: "Working term",
          notes: "",
        },
        segmentation: "do-kaz",
        phoneticNotes: "",
        operatorMapping: "",
        antinomies: [],
        jewikCut: {
          expression: "claim -> check",
          notes: "",
        },
        evidence: [],
        proofStatus: "PROVEN",
        proofNotes: "",
        versionHistory: [],
      },
    ],
  });
  assert.equal(
    sanitizedInvalidProven.entries[0]?.proofStatus,
    "UNDER_REVIEW",
    "Sanitizer must downgrade imported PROVEN entries without evidence.",
  );
  assert.ok(
    sanitizedInvalidProven.entries[0]?.versionHistory.some((item) =>
      item.event.includes("Sanitizer downgraded PROVEN to UNDER_REVIEW because evidence was empty."),
    ),
    "Sanitizer downgrade must leave a history trace.",
  );

  const fakeProvenExport = buildMarkdownExport({
    ...blank,
    proofStatus: "PROVEN",
  });
  assert.ok(
    fakeProvenExport.includes("- proofStatus: UNDER_REVIEW"),
    "Export must not print fake PROVEN when evidence is missing.",
  );
  assert.ok(
    fakeProvenExport.includes("- evidenceCount: 0"),
    "Markdown export must show evidence count explicitly.",
  );

  const fakeProvenJsonText = buildJsonExport({
    ...blank,
    proofStatus: "PROVEN",
  });
  const fakeProvenJson = JSON.parse(fakeProvenJsonText) as {
    proofStatus?: string;
    evidence?: Array<unknown>;
  };
  assert.equal(
    fakeProvenJson.proofStatus,
    "UNDER_REVIEW",
    "JSON export must not preserve fake PROVEN when evidence is missing.",
  );
  assert.equal(
    fakeProvenJson.evidence?.length,
    0,
    "JSON export must preserve zero evidence count for fake PROVEN input.",
  );

  const sanitizedEmpty = sanitizeWorkbenchState({});
  assert.equal(sanitizedEmpty.entries.length, 0, "Sanitizer must fall back to empty state on invalid input.");

  // PHASE A: Tests for NO_DICTIONARY_LAYER → NO_PROVEN law
  // These tests are expected to FAIL until src/jewik-core/index.ts is patched.
  // LAW: PROVEN requires all three: evidence.length > 0, dictionaryLayer.kind !== "UNAVAILABLE", dictionaryLayer.meaning.trim().length > 0

  // Test 1: Entry with evidence but empty dictionary meaning must NOT be allowed PROVEN
  const entryWithEvidenceButEmptyDictionary = createBlankEntry();
  entryWithEvidenceButEmptyDictionary.term = "test-term";
  entryWithEvidenceButEmptyDictionary.dictionaryLayer = {
    kind: "OFFICIAL",
    meaning: "",
    notes: "",
  };
  entryWithEvidenceButEmptyDictionary.evidence = [
    {
      id: "e1",
      text: "Test evidence",
      source: "proofCheck",
      createdAt: new Date().toISOString(),
    },
  ];
  const blockedEmptyMeaning = setProofStatus(entryWithEvidenceButEmptyDictionary, "PROVEN");
  assert.equal(
    blockedEmptyMeaning.blocked,
    true,
    "PROVEN with evidence but empty dictionary meaning must be blocked.",
  );

  // Test 2: Entry with evidence but dictionaryLayer.kind === "UNAVAILABLE" must NOT be allowed PROVEN
  const entryWithUnavailableDictionary = createBlankEntry();
  entryWithUnavailableDictionary.term = "test-term-2";
  entryWithUnavailableDictionary.dictionaryLayer = {
    kind: "UNAVAILABLE",
    meaning: "Some meaning",
    notes: "",
  };
  entryWithUnavailableDictionary.evidence = [
    {
      id: "e2",
      text: "Test evidence",
      source: "proofCheck",
      createdAt: new Date().toISOString(),
    },
  ];
  const blockedUnavailableDictionary = setProofStatus(entryWithUnavailableDictionary, "PROVEN");
  assert.equal(
    blockedUnavailableDictionary.blocked,
    true,
    "PROVEN with UNAVAILABLE dictionary layer must be blocked.",
  );

  // Test 3: validateEntry() must report PROVEN_REQUIRES_DICTIONARY_LAYER
  const validationWithEmptyMeaning = validateEntry(entryWithEvidenceButEmptyDictionary);
  assert.ok(
    validationWithEmptyMeaning.issues.some((issue) => issue.code === "PROVEN_REQUIRES_DICTIONARY_LAYER"),
    "Validation must report PROVEN_REQUIRES_DICTIONARY_LAYER for empty dictionary meaning.",
  );
  const validationWithUnavailable = validateEntry(entryWithUnavailableDictionary);
  assert.ok(
    validationWithUnavailable.issues.some((issue) => issue.code === "PROVEN_REQUIRES_DICTIONARY_LAYER"),
    "Validation must report PROVEN_REQUIRES_DICTIONARY_LAYER for UNAVAILABLE dictionary layer.",
  );

  // Test 4: validateEntry().canMarkProven must be false unless all conditions are met
  const validationCanMarkProvenEmpty = validateEntry(entryWithEvidenceButEmptyDictionary);
  assert.equal(
    validationCanMarkProvenEmpty.canMarkProven,
    false,
    "canMarkProven must be false for empty dictionary meaning.",
  );
  const validationCanMarkProvenUnavailable = validateEntry(entryWithUnavailableDictionary);
  assert.equal(
    validationCanMarkProvenUnavailable.canMarkProven,
    false,
    "canMarkProven must be false for UNAVAILABLE dictionary layer.",
  );

  // Test 5: stabilizeEntry() must downgrade PROVEN → UNDER_REVIEW when dictionary layer is invalid
  const fakeProvenWithEmptyMeaning = {
    ...entryWithEvidenceButEmptyDictionary,
    proofStatus: "PROVEN" as const,
  };
  const stabilizedFromInvalidDict = sanitizeWorkbenchState({
    entries: [fakeProvenWithEmptyMeaning],
  });
  assert.equal(
    stabilizedFromInvalidDict.entries[0]?.proofStatus,
    "UNDER_REVIEW",
    "Sanitizer must downgrade PROVEN to UNDER_REVIEW when dictionary layer is invalid (empty meaning).",
  );
  const fakeProvenWithUnavailable = {
    ...entryWithUnavailableDictionary,
    proofStatus: "PROVEN" as const,
  };
  const stabilizedFromUnavailable = sanitizeWorkbenchState({
    entries: [fakeProvenWithUnavailable],
  });
  assert.equal(
    stabilizedFromUnavailable.entries[0]?.proofStatus,
    "UNDER_REVIEW",
    "Sanitizer must downgrade PROVEN to UNDER_REVIEW when dictionary layer is UNAVAILABLE.",
  );

  // JEWIK Book Engine pure function checks
  assert.equal(normalizeConcept(" NE "), "ne", "normalizeConcept must trim and lowercase.");

  const aliasMatches = findAliasMatches("ne", conceptAliases, seedExcerpts);
  assert.ok(
    aliasMatches.some((excerpt) => excerpt.id === "excerpt-cut-sign"),
    'findAliasMatches("ne") must find an alias-driven excerpt.',
  );

  const conceptReport = buildConceptReport("ne", seedExcerpts, conceptAliases);
  assert.ok(conceptReport.exactMatches.length > 0, "buildConceptReport must expose exact matches.");
  assert.ok(conceptReport.aliasMatches.length > 0, "buildConceptReport must expose alias matches.");
  assert.ok(conceptReport.connotations.length > 0, "buildConceptReport must expose connotations.");
  assert.ok(conceptReport.antinomies.length > 0, "buildConceptReport must expose antinomies.");
  assert.ok(
    conceptReport.chapterCandidates.length > 0,
    "buildConceptReport must expose chapter candidates when matches exist.",
  );

  const noExcerptReport = buildConceptReport("ne", [], conceptAliases);
  assert.equal(
    noExcerptReport.canonCandidates.length,
    0,
    "Canon candidates must not be created when no excerpts exist.",
  );

  const sampleStudioState = createSampleState();
  const emptyStudioState = createEmptyState();
  const originalWindowDescriptor = Object.getOwnPropertyDescriptor(globalThis, "window");

  try {
    const emptyStorage = createStorageMock();
    setWindowMock(emptyStorage);

    const defaultRegistry = readProjectRegistry();
    assert.equal(defaultRegistry.projects.length, 1, "Default project must be created if none exists.");
    assert.equal(
      defaultRegistry.activeProjectId,
      defaultRegistry.projects[0]?.id,
      "Default project must become active.",
    );
    assert.equal(
      readStudioState().documents.length,
      0,
      "Default active project must start from an empty state when no legacy state exists.",
    );

    writeStudioState(sampleStudioState);
    const secondProject = createProject("Second project", emptyStudioState);
    setActiveProjectId(secondProject.id);
    assert.equal(
      readProjectRegistry().activeProjectId,
      secondProject.id,
      "Active project id must be stored after switching.",
    );
    assert.equal(
      readStudioState().documents.length,
      0,
      "Each newly created project must keep its own separate empty state.",
    );

    const secondProjectState = createSampleState();
    secondProjectState.documents[0]!.title = "Second project sample";
    writeProjectState(secondProject.id, secondProjectState);
    assert.equal(
      readProjectState(secondProject.id).documents[0]?.title,
      "Second project sample",
      "Project-specific state writes must persist to the addressed project.",
    );

    setActiveProjectId(defaultRegistry.activeProjectId);
    assert.equal(
      readStudioState().documents[0]?.title,
      sampleStudioState.documents[0]?.title,
      "Switching back must restore the original project's saved state.",
    );

    setActiveProjectId(secondProject.id);
    assert.equal(
      readStudioState().documents[0]?.title,
      "Second project sample",
      "Switching active project must change the loaded active state.",
    );

    renameProject(secondProject.id, "Renamed project");
    assert.equal(
      readProjectRegistry().projects.find((project) => project.id === secondProject.id)?.name,
      "Renamed project",
      "Renaming a project must update project metadata.",
    );

    deleteProject(secondProject.id);
    assert.ok(
      !readProjectRegistry().projects.some((project) => project.id === secondProject.id),
      "Deleting a project must remove it from the registry.",
    );

    const legacyStorage = createStorageMock({
      [STORAGE_KEY]: JSON.stringify(sampleStudioState),
    });
    setWindowMock(legacyStorage);
    const migratedRegistry = readProjectRegistry();
    assert.equal(
      migratedRegistry.projects.length,
      1,
      "Legacy single-state storage must migrate into one default project.",
    );
    assert.equal(
      readStudioState().documents[0]?.title,
      sampleStudioState.documents[0]?.title,
      "Migrated default project must preserve the legacy state payload.",
    );

    const corruptedRegistryStorage = createStorageMock({
      [PROJECT_REGISTRY_STORAGE_KEY]: "{broken-json",
      [STORAGE_KEY]: JSON.stringify(sampleStudioState),
    });
    setWindowMock(corruptedRegistryStorage);
    const recoveredRegistry = readProjectRegistry();
    assert.equal(
      recoveredRegistry.projects.length,
      1,
      "Corrupted project registry must recover safely to one default project.",
    );
    assert.equal(
      readStudioState().documents[0]?.title,
      sampleStudioState.documents[0]?.title,
      "Registry recovery must still preserve the legacy fallback state when available.",
    );

    const packageWorkspace = createDefaultProjectWorkspace(false);
    const projectPackage = createProjectPackage(
      {
        id: "project-package-proof",
        name: "Project Package Proof",
      },
      packageWorkspace,
      "2026-05-13T12:00:00.000Z",
    );
    assert.ok(projectPackage, "createProjectPackage must create a valid package for valid inputs.");
    assert.equal(
      projectPackage?.packageVersion,
      PROJECT_PACKAGE_VERSION,
      "createProjectPackage must set packageVersion 1.",
    );
    assert.equal(
      projectPackage?.packageType,
      PROJECT_PACKAGE_TYPE,
      "createProjectPackage must set the canonical packageType.",
    );
    assert.ok(
      isProjectPackage(projectPackage),
      "isProjectPackage must accept a valid package object.",
    );

    const serializedPackage = serializeProjectPackage(projectPackage!);
    const parsedPackage = parseProjectPackage(serializedPackage);
    assert.equal(parsedPackage.ok, true, "serialize + parse roundtrip must succeed.");

    if (!parsedPackage.ok) {
      throw new Error(parsedPackage.message);
    }

    const roundtripWorkspace = readWorkspaceFromProjectPackage(parsedPackage.value);
    assert.ok(
      roundtripWorkspace,
      "Valid ProjectPackage must yield a readable workspace snapshot.",
    );
    assert.equal(
      roundtripWorkspace?.activeConcept,
      packageWorkspace.activeConcept,
      "Workspace roundtrip must preserve activeConcept.",
    );
    assert.equal(
      roundtripWorkspace?.chapterDraft.title,
      packageWorkspace.chapterDraft.title,
      "Workspace roundtrip must preserve draft title.",
    );

    const invalidJsonPackage = parseProjectPackage("{broken-json");
    assert.equal(invalidJsonPackage.ok, false, "Corrupted JSON must be rejected safely.");
    if (!invalidJsonPackage.ok) {
      assert.equal(
        invalidJsonPackage.code,
        "INVALID_JSON",
        "Corrupted JSON must report INVALID_JSON.",
      );
    }

    const wrongTypePackage = parseProjectPackage(
      JSON.stringify({
        ...projectPackage,
        packageType: "wrong.package-type",
      }),
    );
    assert.equal(wrongTypePackage.ok, false, "Wrong packageType must be rejected.");
    if (!wrongTypePackage.ok) {
      assert.equal(
        wrongTypePackage.code,
        "INVALID_PACKAGE_TYPE",
        "Wrong packageType must report INVALID_PACKAGE_TYPE.",
      );
    }

    const wrongVersionPackage = parseProjectPackage(
      JSON.stringify({
        ...projectPackage,
        packageVersion: 2,
      }),
    );
    assert.equal(wrongVersionPackage.ok, false, "Unsupported packageVersion must be rejected.");
    if (!wrongVersionPackage.ok) {
      assert.equal(
        wrongVersionPackage.code,
        "UNSUPPORTED_PACKAGE_VERSION",
        "Unsupported packageVersion must report UNSUPPORTED_PACKAGE_VERSION.",
      );
    }

    const missingProjectNamePackage = parseProjectPackage(
      JSON.stringify({
        ...projectPackage,
        project: {
          ...projectPackage?.project,
          name: "",
        },
      }),
    );
    assert.equal(missingProjectNamePackage.ok, false, "Missing project.name must be rejected.");
    if (!missingProjectNamePackage.ok) {
      assert.equal(
        missingProjectNamePackage.code,
        "INVALID_PROJECT",
        "Missing project.name must report INVALID_PROJECT.",
      );
    }

    const missingWorkspacePackage = parseProjectPackage(
      JSON.stringify({
        ...projectPackage,
        workspace: {
          draft: "invalid",
          lastConcept: null,
        },
      }),
    );
    assert.equal(
      missingWorkspacePackage.ok,
      false,
      "Missing or malformed workspace must be rejected.",
    );
    if (!missingWorkspacePackage.ok) {
      assert.equal(
        missingWorkspacePackage.code,
        "INVALID_WORKSPACE",
        "Malformed workspace must report INVALID_WORKSPACE.",
      );
    }

    assert.equal(
      readWorkspaceFromProjectPackage({
        ...projectPackage,
        workspace: {
          draft: "invalid",
        },
      }),
      null,
      "readWorkspaceFromProjectPackage must reject malformed workspace payloads.",
    );
  } finally {
    restoreWindow(originalWindowDescriptor);
  }

  console.log("PROOF PASS");
  console.log(
    JSON.stringify(
      {
        sampleEntries: initial.entries.length,
        sampleTerm: sample.term,
        blankIssues: blankValidation.issues.map((issue) => issue.code),
        provenStatus: proven.entry.proofStatus,
      },
      null,
      2,
    ),
  );
}

main();
