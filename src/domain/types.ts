export type TruthType =
  | "AKSIOM_APD"
  | "DEFINICIJA"
  | "UNIVERZALNO_TESTABILNA_RESNICA"
  | "EMPIRIČNA_TRDITEV"
  | "RELACIJSKA_RESNICA"
  | "OSEBNA_RESNICA"
  | "SIMBOLNA_RESNICA"
  | "KONTRADIKCIJA"
  | "METODA";

export type TruthStatus =
  | "CANDIDATE"
  | "TESTABLE"
  | "NEEDS_DEFINITION"
  | "NEEDS_EVIDENCE"
  | "CONFLICT"
  | "READY_FOR_MY_CONSENT"
  | "CANON";

export type ConsentStatus = "EMPTY" | "DA" | "NE" | "POPRAVI" | "KANON";

export type RelationType =
  | "SUPPORTS"
  | "CONTRADICTS"
  | "DEFINES"
  | "REFINES"
  | "TESTS"
  | "SYMBOLICALLY_LINKED";

export type DocumentSource = {
  id: string;
  title: string;
  filename?: string;
  content: string;
  createdAt: string;
  updatedAt: string;
};

export type TruthUnit = {
  id: string;
  documentId: string;
  type: TruthType;
  status: TruthStatus;
  consentStatus: ConsentStatus;
  title: string;
  claim: string;
  keyDefinitions: string[];
  evidenceFromDocument: string[];
  counterAngle: string;
  proposedLinks: string[];
  notes: string;
  createdAt: string;
  updatedAt: string;
};

export type EvidenceRef = {
  id: string;
  truthUnitId: string;
  quote: string;
  sourceLocation?: string;
  confidence: number;
};

export type DefinitionRef = {
  id: string;
  term: string;
  definition: string;
  scope: string;
  linkedUnitIds: string[];
};

export type CounterAngle = {
  id: string;
  truthUnitId: string;
  description: string;
  severity: "nizka" | "srednja" | "visoka";
};

export type UnitLink = {
  id: string;
  fromUnitId: string;
  toUnitId: string;
  relationType: RelationType;
  note: string;
};

export type SimulationStep = {
  status: TruthStatus;
  note: string;
};

export type SimulationCase = {
  id: string;
  title: string;
  description: string;
  involvedUnitIds: string[];
  steps: SimulationStep[];
};

export type StudioState = {
  documents: DocumentSource[];
  truthUnits: TruthUnit[];
  evidenceRefs: EvidenceRef[];
  definitions: DefinitionRef[];
  counterAngles: CounterAngle[];
  links: UnitLink[];
  simulationCases: SimulationCase[];
};

export type ViewId =
  | "library"
  | "truthUnits"
  | "consent"
  | "ontograph"
  | "simulation"
  | "exchange";

export type ViewLabel = {
  id: ViewId;
  label: string;
  hint: string;
};

export const truthTypeOptions: TruthType[] = [
  "AKSIOM_APD",
  "DEFINICIJA",
  "UNIVERZALNO_TESTABILNA_RESNICA",
  "EMPIRIČNA_TRDITEV",
  "RELACIJSKA_RESNICA",
  "OSEBNA_RESNICA",
  "SIMBOLNA_RESNICA",
  "KONTRADIKCIJA",
  "METODA",
];

export const truthStatusOptions: TruthStatus[] = [
  "CANDIDATE",
  "TESTABLE",
  "NEEDS_DEFINITION",
  "NEEDS_EVIDENCE",
  "CONFLICT",
  "READY_FOR_MY_CONSENT",
  "CANON",
];

export const consentOptions: ConsentStatus[] = ["EMPTY", "DA", "NE", "POPRAVI", "KANON"];

export const relationTypeLabels: Record<RelationType, string> = {
  SUPPORTS: "podpira",
  CONTRADICTS: "nasprotuje",
  DEFINES: "definira",
  REFINES: "izostri",
  TESTS: "testira",
  SYMBOLICALLY_LINKED: "simbolno poveže",
};

export const viewLabels: ViewLabel[] = [
  { id: "library", label: "Library", hint: "dokumenti in vhodi" },
  { id: "truthUnits", label: "Truth Units", hint: "delovna tabela enot" },
  { id: "consent", label: "Consent", hint: "moje soglasje in kanon" },
  { id: "ontograph", label: "Ontograph", hint: "jasen seznam relacij" },
  { id: "simulation", label: "Simulation Lab", hint: "prehod kandidat -> kanon" },
  { id: "exchange", label: "Export / Import", hint: "lokalni JSON tok" },
];

export const simulationPath: TruthStatus[] = [
  "CANDIDATE",
  "NEEDS_DEFINITION",
  "TESTABLE",
  "READY_FOR_MY_CONSENT",
  "CANON",
];

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
