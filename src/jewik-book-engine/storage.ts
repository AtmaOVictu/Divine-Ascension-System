import { seedChapterDrafts, seedExcerpts } from "./seedData";
import type { ChapterDraft, SourceExcerpt } from "./types";

const DRAFT_STORAGE_KEY = "jewik-book-engine:draft:v1";
const LAST_CONCEPT_STORAGE_KEY = "jewik-book-engine:last-concept:v1";
const PROJECT_WORKSPACE_STORAGE_KEY_PREFIX = "jewik-book-engine:project-workspace:v1:";
const DEFAULT_BOOK_MESSAGE = "Primerjava verzij je v tej fazi placeholder.";

const memoryFallback = new Map<string, string>();

type StorageLike = {
  getItem(key: string): string | null;
  removeItem(key: string): void;
  setItem(key: string, value: string): void;
};

export type ProjectWorkspaceSnapshot = {
  activeConcept: string;
  bookMessage: string;
  chapterDraft: ChapterDraft;
  conceptInput: string;
  draftState: "shranjeno" | "nespremenjeno" | "osnutek";
  excerpts: SourceExcerpt[];
  lastSavedSnapshot: string;
};

function createMemoryStorage(): StorageLike {
  return {
    getItem(key) {
      return memoryFallback.has(key) ? memoryFallback.get(key)! : null;
    },
    removeItem(key) {
      memoryFallback.delete(key);
    },
    setItem(key, value) {
      memoryFallback.set(key, value);
    },
  };
}

function getSafeStorage(): StorageLike {
  if (typeof window === "undefined" || !("localStorage" in window)) {
    return createMemoryStorage();
  }

  try {
    const probeKey = "__jewik_book_engine_probe__";
    window.localStorage.setItem(probeKey, "1");
    window.localStorage.removeItem(probeKey);
    return window.localStorage;
  } catch {
    return createMemoryStorage();
  }
}

function isStringArray(value: unknown): value is string[] {
  return Array.isArray(value) && value.every((item) => typeof item === "string");
}

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null;
}

function isChapterDraft(value: unknown): value is ChapterDraft {
  if (typeof value !== "object" || value === null) {
    return false;
  }

  const candidate = value as Record<string, unknown>;

  return (
    typeof candidate.id === "string" &&
    typeof candidate.bookId === "string" &&
    typeof candidate.title === "string" &&
    typeof candidate.status === "string" &&
    typeof candidate.text === "string" &&
    isStringArray(candidate.linkedExcerptIds) &&
    isStringArray(candidate.linkedConcepts) &&
    isStringArray(candidate.variants) &&
    typeof candidate.currentVariant === "string" &&
    typeof candidate.updatedAt === "string"
  );
}

function cloneDraft(draft: ChapterDraft): ChapterDraft {
  return {
    ...draft,
    linkedExcerptIds: [...draft.linkedExcerptIds],
    linkedConcepts: [...draft.linkedConcepts],
    variants: [...draft.variants],
  };
}

function cloneExcerpts(excerpts: SourceExcerpt[]): SourceExcerpt[] {
  return excerpts.map((excerpt) => ({
    ...excerpt,
    conceptHints: [...excerpt.conceptHints],
  }));
}

function isSourceExcerpt(value: unknown): value is SourceExcerpt {
  if (!isRecord(value)) {
    return false;
  }

  return (
    typeof value.id === "string" &&
    typeof value.sourceId === "string" &&
    typeof value.sourceTitle === "string" &&
    typeof value.locator === "string" &&
    typeof value.text === "string" &&
    typeof value.status === "string" &&
    typeof value.note === "string" &&
    isStringArray(value.conceptHints)
  );
}

function isProjectWorkspaceSnapshot(value: unknown): value is ProjectWorkspaceSnapshot {
  if (!isRecord(value)) {
    return false;
  }

  return (
    typeof value.activeConcept === "string" &&
    typeof value.bookMessage === "string" &&
    typeof value.conceptInput === "string" &&
    typeof value.draftState === "string" &&
    typeof value.lastSavedSnapshot === "string" &&
    Array.isArray(value.excerpts) &&
    value.excerpts.every(isSourceExcerpt) &&
    isChapterDraft(value.chapterDraft)
  );
}

function cloneProjectWorkspaceSnapshot(
  snapshot: ProjectWorkspaceSnapshot,
): ProjectWorkspaceSnapshot {
  return {
    ...snapshot,
    chapterDraft: cloneDraft(snapshot.chapterDraft),
    excerpts: cloneExcerpts(snapshot.excerpts),
  };
}

export function saveDraftToLocalStorage(draft: ChapterDraft): void {
  getSafeStorage().setItem(DRAFT_STORAGE_KEY, JSON.stringify(draft));
}

export function loadDraftFromLocalStorage(): ChapterDraft | null {
  const raw = getSafeStorage().getItem(DRAFT_STORAGE_KEY);
  if (!raw) {
    return null;
  }

  try {
    const parsed = JSON.parse(raw) as unknown;
    return isChapterDraft(parsed) ? parsed : null;
  } catch {
    return null;
  }
}

export function saveLastConceptToLocalStorage(concept: string): void {
  getSafeStorage().setItem(LAST_CONCEPT_STORAGE_KEY, concept);
}

export function loadLastConceptFromLocalStorage(): string {
  return getSafeStorage().getItem(LAST_CONCEPT_STORAGE_KEY) ?? "";
}

export function getProjectWorkspaceKey(projectId: string): string {
  return `${PROJECT_WORKSPACE_STORAGE_KEY_PREFIX}${projectId}`;
}

export function createDefaultProjectWorkspace(useLegacyFallback = false): ProjectWorkspaceSnapshot {
  const fallbackConcept = useLegacyFallback ? loadLastConceptFromLocalStorage() || "ne" : "ne";
  const fallbackDraft = useLegacyFallback ? loadDraftFromLocalStorage() : null;
  const nextDraft = fallbackDraft ? cloneDraft(fallbackDraft) : cloneDraft(seedChapterDrafts[0]!);

  return {
    activeConcept: fallbackConcept,
    bookMessage: DEFAULT_BOOK_MESSAGE,
    chapterDraft: nextDraft,
    conceptInput: fallbackConcept,
    draftState: fallbackDraft ? "shranjeno" : "nespremenjeno",
    excerpts: cloneExcerpts(seedExcerpts),
    lastSavedSnapshot: JSON.stringify(nextDraft),
  };
}

export function readProjectWorkspace(
  projectId: string,
  useLegacyFallback = false,
): ProjectWorkspaceSnapshot {
  const raw = getSafeStorage().getItem(getProjectWorkspaceKey(projectId));

  if (!raw) {
    return createDefaultProjectWorkspace(useLegacyFallback);
  }

  try {
    const parsed = JSON.parse(raw) as unknown;
    if (!isProjectWorkspaceSnapshot(parsed)) {
      return createDefaultProjectWorkspace(useLegacyFallback);
    }

    return cloneProjectWorkspaceSnapshot(parsed);
  } catch {
    return createDefaultProjectWorkspace(useLegacyFallback);
  }
}

export function writeProjectWorkspace(
  projectId: string,
  snapshot: ProjectWorkspaceSnapshot,
  syncLegacy = false,
): void {
  const nextSnapshot = cloneProjectWorkspaceSnapshot(snapshot);
  const storage = getSafeStorage();

  storage.setItem(getProjectWorkspaceKey(projectId), JSON.stringify(nextSnapshot));

  if (syncLegacy) {
    saveDraftToLocalStorage(nextSnapshot.chapterDraft);
    saveLastConceptToLocalStorage(nextSnapshot.activeConcept || nextSnapshot.conceptInput || "ne");
  }
}

export function removeProjectWorkspace(projectId: string): void {
  getSafeStorage().removeItem(getProjectWorkspaceKey(projectId));
}
