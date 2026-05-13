import { createEmptyState } from "../domain/sampleData";
import type {
  CounterAngle,
  DefinitionRef,
  DocumentSource,
  EvidenceRef,
  SimulationCase,
  SimulationStep,
  StudioState,
  TruthUnit,
  UnitLink,
} from "../domain/types";
import { createId, stamp } from "../domain/types";

export const STORAGE_KEY = "jewik-truthbase-studio:v1";
export const TRUTHBASE_IMPORT_CONTRACT = "truthbase_import.v1";
export const IMPORT_METADATA_STORAGE_KEY = "jewik-truthbase-studio:import-metadata:v1";
export const PROJECT_REGISTRY_STORAGE_KEY = "jewik-truthbase-studio:projects:v1";
export const PROJECT_STATE_STORAGE_KEY_PREFIX = "jewik-truthbase-studio:project-state:v1:";

const DEFAULT_PROJECT_NAME = "Default project";

export type StudioProject = {
  id: string;
  name: string;
  createdAt: string;
  updatedAt: string;
};

export type StudioProjectRegistry = {
  version: 1;
  activeProjectId: string;
  projects: StudioProject[];
};

export type ImportSourceMetadata = {
  layer: string | null;
  generator: string | null;
  adapter: string | null;
  inputArtifact: string | null;
  mode: string | null;
  manualCanonGate: string | null;
};

export type ImportMetadata =
  | { importKind: "direct" }
  | {
      importKind: "envelope";
      contract: string;
      generatedAt: string | null;
      source: ImportSourceMetadata | null;
    };

// Helper: type-safe object check
function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null;
}

function readOptionalString(record: Record<string, unknown>, key: string): string | null {
  return typeof record[key] === "string" ? record[key] : null;
}

function getLocalStorage(): Storage | null {
  if (typeof window === "undefined") {
    return null;
  }

  return window.localStorage;
}

function createProjectRecord(name = DEFAULT_PROJECT_NAME): StudioProject {
  const now = stamp();

  return {
    id: createId("project"),
    name,
    createdAt: now,
    updatedAt: now,
  };
}

function buildProjectRegistry(
  projects: StudioProject[],
  activeProjectId: string,
): StudioProjectRegistry {
  return {
    version: 1,
    activeProjectId,
    projects,
  };
}

function getProjectStateStorageKey(projectId: string): string {
  return `${PROJECT_STATE_STORAGE_KEY_PREFIX}${projectId}`;
}

function isValidStudioProject(value: unknown): value is StudioProject {
  if (!isRecord(value)) {
    return false;
  }

  return (
    typeof value.id === "string" &&
    typeof value.name === "string" &&
    typeof value.createdAt === "string" &&
    typeof value.updatedAt === "string"
  );
}

function isValidProjectRegistry(value: unknown): value is StudioProjectRegistry {
  if (!isRecord(value)) {
    return false;
  }

  return (
    value.version === 1 &&
    typeof value.activeProjectId === "string" &&
    Array.isArray(value.projects) &&
    value.projects.every(isValidStudioProject)
  );
}

function looksLikeStudioStateRecord(value: Record<string, unknown>): boolean {
  return [
    "documents",
    "truthUnits",
    "evidenceRefs",
    "definitions",
    "counterAngles",
    "links",
    "simulationCases",
  ].some((key) => Array.isArray(value[key]));
}

function extractImportSourceMetadata(value: unknown): ImportSourceMetadata | null {
  if (!isRecord(value)) {
    return null;
  }

  return {
    layer: readOptionalString(value, "layer"),
    generator: readOptionalString(value, "generator"),
    adapter: readOptionalString(value, "adapter"),
    inputArtifact: readOptionalString(value, "inputArtifact"),
    mode: readOptionalString(value, "mode"),
    manualCanonGate: readOptionalString(value, "manualCanonGate"),
  };
}

function extractImportPayload(value: unknown): unknown {
  if (!isRecord(value)) {
    return value;
  }

  if (value.contract === TRUTHBASE_IMPORT_CONTRACT && isRecord(value.state)) {
    return value.state;
  }

  return value;
}

function isImportSourceMetadata(value: unknown): value is ImportSourceMetadata {
  if (!isRecord(value)) {
    return false;
  }

  return (
    (typeof value.layer === "string" || value.layer === null) &&
    (typeof value.generator === "string" || value.generator === null) &&
    (typeof value.adapter === "string" || value.adapter === null) &&
    (typeof value.inputArtifact === "string" || value.inputArtifact === null) &&
    (typeof value.mode === "string" || value.mode === null) &&
    (typeof value.manualCanonGate === "string" || value.manualCanonGate === null)
  );
}

function isImportMetadata(value: unknown): value is ImportMetadata {
  if (!isRecord(value) || typeof value.importKind !== "string") {
    return false;
  }

  if (value.importKind === "direct") {
    return true;
  }

  if (value.importKind !== "envelope") {
    return false;
  }

  return (
    typeof value.contract === "string" &&
    (typeof value.generatedAt === "string" || value.generatedAt === null) &&
    (value.source === null || isImportSourceMetadata(value.source))
  );
}

export function extractImportMetadata(value: unknown): ImportMetadata | null {
  if (!isRecord(value)) {
    return null;
  }

  if (value.contract === TRUTHBASE_IMPORT_CONTRACT && isRecord(value.state)) {
    return {
      importKind: "envelope",
      contract: TRUTHBASE_IMPORT_CONTRACT,
      generatedAt: readOptionalString(value, "generatedAt"),
      source: extractImportSourceMetadata(value.source),
    };
  }

  if (looksLikeStudioStateRecord(value)) {
    return { importKind: "direct" };
  }

  return null;
}

// Helper: validate string array contents
function isStringArray(value: unknown): value is string[] {
  return Array.isArray(value) && value.every((item) => typeof item === "string");
}

// Helper: validate SimulationStep element shape
function isValidSimulationStep(item: unknown): item is SimulationStep {
  if (!isRecord(item)) return false;
  return (
    typeof item.status === "string" &&
    typeof item.note === "string"
  );
}

// Field validators for element-shape filtering
function isValidDocumentSource(item: unknown): item is DocumentSource {
  if (!isRecord(item)) return false;
  return (
    typeof item.id === "string" &&
    typeof item.title === "string" &&
    typeof item.content === "string" &&
    typeof item.createdAt === "string" &&
    typeof item.updatedAt === "string"
  );
}

function isValidTruthUnit(item: unknown): item is TruthUnit {
  if (!isRecord(item)) return false;
  return (
    typeof item.id === "string" &&
    typeof item.documentId === "string" &&
    typeof item.type === "string" &&
    typeof item.status === "string" &&
    typeof item.consentStatus === "string" &&
    typeof item.title === "string" &&
    typeof item.claim === "string" &&
    isStringArray(item.keyDefinitions) &&
    isStringArray(item.evidenceFromDocument) &&
    typeof item.counterAngle === "string" &&
    isStringArray(item.proposedLinks) &&
    typeof item.notes === "string" &&
    typeof item.createdAt === "string" &&
    typeof item.updatedAt === "string"
  );
}

function isValidEvidenceRef(item: unknown): item is EvidenceRef {
  if (!isRecord(item)) return false;
  return (
    typeof item.id === "string" &&
    typeof item.truthUnitId === "string" &&
    typeof item.quote === "string" &&
    (item.sourceLocation === undefined || typeof item.sourceLocation === "string") &&
    typeof item.confidence === "number" &&
    Number.isFinite(item.confidence) &&
    item.confidence >= 0 &&
    item.confidence <= 1
  );
}

function isValidDefinitionRef(item: unknown): item is DefinitionRef {
  if (!isRecord(item)) return false;
  return (
    typeof item.id === "string" &&
    typeof item.term === "string" &&
    typeof item.definition === "string" &&
    typeof item.scope === "string" &&
    isStringArray(item.linkedUnitIds)
  );
}

function isValidCounterAngle(item: unknown): item is CounterAngle {
  if (!isRecord(item)) return false;
  return (
    typeof item.id === "string" &&
    typeof item.truthUnitId === "string" &&
    typeof item.description === "string" &&
    typeof item.severity === "string"
  );
}

function isValidUnitLink(item: unknown): item is UnitLink {
  if (!isRecord(item)) return false;
  return (
    typeof item.id === "string" &&
    typeof item.fromUnitId === "string" &&
    typeof item.toUnitId === "string" &&
    typeof item.relationType === "string" &&
    typeof item.note === "string"
  );
}

function isValidSimulationCase(item: unknown): item is SimulationCase {
  if (!isRecord(item)) return false;
  return (
    typeof item.id === "string" &&
    typeof item.title === "string" &&
    typeof item.description === "string" &&
    isStringArray(item.involvedUnitIds) &&
    (Array.isArray(item.steps) && item.steps.every(isValidSimulationStep))
  );
}

// Reference validation helpers
function extractIds(array: Array<{ id: string }>): Set<string> {
  return new Set(array.map((item) => item.id));
}

function filterByDocumentId(
  truthUnits: TruthUnit[],
  validDocIds: Set<string>
): TruthUnit[] {
  return truthUnits.filter((unit) => validDocIds.has(unit.documentId));
}

function filterByTruthUnitId<T extends { truthUnitId: string }>(
  items: T[],
  validUnitIds: Set<string>
): T[] {
  return items.filter((item) => validUnitIds.has(item.truthUnitId));
}

function filterUnitLinks(
  links: UnitLink[],
  validUnitIds: Set<string>
): UnitLink[] {
  return links.filter(
    (link) =>
      validUnitIds.has(link.fromUnitId) && validUnitIds.has(link.toUnitId)
  );
}

function normalizeIdArray(
  idArray: string[],
  validIdSet: Set<string>
): string[] {
  return idArray.filter((id) => validIdSet.has(id));
}

// Deduplication: keep first item per id, drop later duplicates
function dedupeById<T extends { id: string }>(items: T[]): T[] {
  const seen = new Set<string>();
  const result: T[] = [];
  for (const item of items) {
    if (!seen.has(item.id)) {
      seen.add(item.id);
      result.push(item);
    }
  }
  return result;
}

export function sanitizeState(raw: unknown): StudioState {
  const empty = createEmptyState();
  const payload = extractImportPayload(raw);

  if (!payload || typeof payload !== "object") {
    return empty;
  }

  const candidate = payload as Partial<StudioState>;

  // STEP 1: Filter documents by shape, then deduplicate by id
  const validDocumentsWithDupes = Array.isArray(candidate.documents)
    ? (candidate.documents as unknown[]).filter(isValidDocumentSource)
    : empty.documents;
  const validDocuments = dedupeById(validDocumentsWithDupes);
  const documentIds = extractIds(validDocuments);

  // STEP 2: Filter truthUnits by shape, by documentId reference, then deduplicate by id
  const validTruthUnitsWithRefs = Array.isArray(candidate.truthUnits)
    ? (candidate.truthUnits as unknown[]).filter(isValidTruthUnit)
    : empty.truthUnits;
  const validTruthUnitsFiltered = filterByDocumentId(validTruthUnitsWithRefs, documentIds);
  const validTruthUnits = dedupeById(validTruthUnitsFiltered);
  const unitIds = extractIds(validTruthUnits);

  // STEP 3: Filter evidenceRefs by shape, by truthUnitId reference, then deduplicate by id
  const validEvidenceRefsWithShape = Array.isArray(candidate.evidenceRefs)
    ? (candidate.evidenceRefs as unknown[]).filter(isValidEvidenceRef)
    : empty.evidenceRefs;
  const validEvidenceRefsFiltered = filterByTruthUnitId(validEvidenceRefsWithShape, unitIds);
  const evidenceRefs = dedupeById(validEvidenceRefsFiltered);

  // STEP 4: Filter counterAngles by shape, by truthUnitId reference, then deduplicate by id
  const validCounterAnglesWithShape = Array.isArray(candidate.counterAngles)
    ? (candidate.counterAngles as unknown[]).filter(isValidCounterAngle)
    : empty.counterAngles;
  const validCounterAnglesFiltered = filterByTruthUnitId(validCounterAnglesWithShape, unitIds);
  const counterAngles = dedupeById(validCounterAnglesFiltered);

  // STEP 5: Filter unitLinks by shape, by fromUnitId/toUnitId references, then deduplicate by id
  const validLinksWithShape = Array.isArray(candidate.links)
    ? (candidate.links as unknown[]).filter(isValidUnitLink)
    : empty.links;
  const validLinksFiltered = filterUnitLinks(validLinksWithShape, unitIds);
  const links = dedupeById(validLinksFiltered);

  // STEP 6: Filter definitions by shape, normalize linkedUnitIds array, then deduplicate by id
  const validDefinitionsWithShape = Array.isArray(candidate.definitions)
    ? (candidate.definitions as unknown[]).filter(isValidDefinitionRef)
    : empty.definitions;
  const validDefinitionsNormalized = validDefinitionsWithShape.map((def) => ({
    ...def,
    linkedUnitIds: normalizeIdArray(def.linkedUnitIds, unitIds),
  }));
  const definitions = dedupeById(validDefinitionsNormalized);

  // STEP 7: Filter simulationCases by shape, normalize involvedUnitIds array, then deduplicate by id
  const validSimulationCasesWithShape = Array.isArray(candidate.simulationCases)
    ? (candidate.simulationCases as unknown[]).filter(isValidSimulationCase)
    : empty.simulationCases;
  const validSimulationCasesNormalized = validSimulationCasesWithShape.map((caseItem) => ({
    ...caseItem,
    involvedUnitIds: normalizeIdArray(caseItem.involvedUnitIds, unitIds),
  }));
  const simulationCases = dedupeById(validSimulationCasesNormalized);

  return {
    documents: validDocuments,
    truthUnits: validTruthUnits,
    evidenceRefs,
    definitions,
    counterAngles,
    links,
    simulationCases,
  };
}

function readLegacyStateFromStorage(storage: Storage): StudioState | null {
  const raw = storage.getItem(STORAGE_KEY);

  if (!raw) {
    return null;
  }

  try {
    return sanitizeState(JSON.parse(raw));
  } catch {
    return null;
  }
}

function readProjectStateFromStorage(storage: Storage, projectId: string): StudioState {
  const raw = storage.getItem(getProjectStateStorageKey(projectId));

  if (!raw) {
    return createEmptyState();
  }

  try {
    return sanitizeState(JSON.parse(raw));
  } catch {
    return createEmptyState();
  }
}

function writeProjectStateToStorage(storage: Storage, projectId: string, state: StudioState): void {
  storage.setItem(getProjectStateStorageKey(projectId), JSON.stringify(sanitizeState(state)));
}

function writeLegacyActiveState(storage: Storage, state: StudioState): void {
  storage.setItem(STORAGE_KEY, JSON.stringify(sanitizeState(state)));
}

function persistProjectRegistry(storage: Storage, registry: StudioProjectRegistry): void {
  storage.setItem(PROJECT_REGISTRY_STORAGE_KEY, JSON.stringify(registry));
}

function createDefaultProjectRegistry(
  storage: Storage,
  initialState: StudioState | null = null,
): StudioProjectRegistry {
  const project = createProjectRecord(DEFAULT_PROJECT_NAME);
  const state = initialState ?? readLegacyStateFromStorage(storage) ?? createEmptyState();
  const registry = buildProjectRegistry([project], project.id);

  persistProjectRegistry(storage, registry);
  writeProjectStateToStorage(storage, project.id, state);
  writeLegacyActiveState(storage, state);

  return registry;
}

function ensureProjectRegistry(storage: Storage): StudioProjectRegistry {
  const raw = storage.getItem(PROJECT_REGISTRY_STORAGE_KEY);

  if (!raw) {
    return createDefaultProjectRegistry(storage);
  }

  try {
    const parsed = JSON.parse(raw) as unknown;
    if (!isValidProjectRegistry(parsed)) {
      return createDefaultProjectRegistry(storage);
    }

    const projects = dedupeById(parsed.projects);
    if (projects.length === 0) {
      return createDefaultProjectRegistry(storage);
    }

    const activeProject =
      projects.find((project) => project.id === parsed.activeProjectId) ?? projects[0]!;
    const registry = buildProjectRegistry(projects, activeProject.id);
    persistProjectRegistry(storage, registry);
    return registry;
  } catch {
    return createDefaultProjectRegistry(storage);
  }
}

export function readProjectRegistry(): StudioProjectRegistry {
  const storage = getLocalStorage();

  if (!storage) {
    const project = createProjectRecord(DEFAULT_PROJECT_NAME);
    return buildProjectRegistry([project], project.id);
  }

  return ensureProjectRegistry(storage);
}

export function readProjectState(projectId: string): StudioState {
  const storage = getLocalStorage();

  if (!storage) {
    return createEmptyState();
  }

  const registry = ensureProjectRegistry(storage);
  if (!registry.projects.some((project) => project.id === projectId)) {
    return createEmptyState();
  }

  return readProjectStateFromStorage(storage, projectId);
}

export function readState(): StudioState {
  const storage = getLocalStorage();

  if (!storage) {
    return createEmptyState();
  }

  const registry = ensureProjectRegistry(storage);
  const state = readProjectStateFromStorage(storage, registry.activeProjectId);
  writeLegacyActiveState(storage, state);
  return state;
}

export function writeProjectState(projectId: string, state: StudioState): void {
  const storage = getLocalStorage();

  if (!storage) {
    return;
  }

  const registry = ensureProjectRegistry(storage);
  if (!registry.projects.some((project) => project.id === projectId)) {
    return;
  }

  const sanitized = sanitizeState(state);
  writeProjectStateToStorage(storage, projectId, sanitized);

  if (registry.activeProjectId === projectId) {
    writeLegacyActiveState(storage, sanitized);
  }
}

export function writeState(state: StudioState): void {
  const storage = getLocalStorage();

  if (!storage) {
    return;
  }

  const registry = ensureProjectRegistry(storage);
  const sanitized = sanitizeState(state);
  writeProjectStateToStorage(storage, registry.activeProjectId, sanitized);
  writeLegacyActiveState(storage, sanitized);
}

export function createProject(
  name = DEFAULT_PROJECT_NAME,
  initialState: StudioState = createEmptyState(),
): StudioProject {
  const project = createProjectRecord(name.trim() || DEFAULT_PROJECT_NAME);
  const storage = getLocalStorage();

  if (!storage) {
    return project;
  }

  const registry = ensureProjectRegistry(storage);
  const nextRegistry = buildProjectRegistry(
    [...registry.projects, project],
    registry.activeProjectId,
  );

  persistProjectRegistry(storage, nextRegistry);
  writeProjectStateToStorage(storage, project.id, initialState);

  return project;
}

export function renameProject(projectId: string, nextName: string): void {
  const storage = getLocalStorage();
  const trimmedName = nextName.trim();

  if (!storage || !trimmedName) {
    return;
  }

  const registry = ensureProjectRegistry(storage);
  const nextProjects = registry.projects.map((project) =>
    project.id === projectId
      ? {
          ...project,
          name: trimmedName,
          updatedAt: stamp(),
        }
      : project,
  );

  persistProjectRegistry(
    storage,
    buildProjectRegistry(nextProjects, registry.activeProjectId),
  );
}

export function setActiveProjectId(projectId: string): void {
  const storage = getLocalStorage();

  if (!storage) {
    return;
  }

  const registry = ensureProjectRegistry(storage);
  if (!registry.projects.some((project) => project.id === projectId)) {
    return;
  }

  persistProjectRegistry(storage, buildProjectRegistry(registry.projects, projectId));
  writeLegacyActiveState(storage, readProjectStateFromStorage(storage, projectId));
}

export function deleteProject(projectId: string): void {
  const storage = getLocalStorage();

  if (!storage) {
    return;
  }

  const registry = ensureProjectRegistry(storage);
  const remainingProjects = registry.projects.filter((project) => project.id !== projectId);
  storage.removeItem(getProjectStateStorageKey(projectId));

  if (remainingProjects.length === 0) {
    createDefaultProjectRegistry(storage);
    return;
  }

  const nextActiveProjectId =
    registry.activeProjectId === projectId ? remainingProjects[0]!.id : registry.activeProjectId;
  const nextRegistry = buildProjectRegistry(remainingProjects, nextActiveProjectId);

  persistProjectRegistry(storage, nextRegistry);

  if (registry.activeProjectId === projectId) {
    writeLegacyActiveState(
      storage,
      readProjectStateFromStorage(storage, nextActiveProjectId),
    );
  }
}

export function readImportMetadata(): ImportMetadata | null {
  const storage = getLocalStorage();

  if (!storage) {
    return null;
  }

  const raw = storage.getItem(IMPORT_METADATA_STORAGE_KEY);
  if (!raw) {
    return null;
  }

  try {
    const parsed = JSON.parse(raw) as unknown;
    return isImportMetadata(parsed) ? parsed : null;
  } catch {
    return null;
  }
}

export function writeImportMetadata(metadata: ImportMetadata | null): void {
  const storage = getLocalStorage();

  if (!storage) {
    return;
  }

  if (metadata === null) {
    storage.removeItem(IMPORT_METADATA_STORAGE_KEY);
    return;
  }

  storage.setItem(IMPORT_METADATA_STORAGE_KEY, JSON.stringify(metadata));
}
