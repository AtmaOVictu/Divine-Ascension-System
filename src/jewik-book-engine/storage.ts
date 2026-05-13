import {
  seedBookProjects,
  seedChapterDrafts,
  seedConceptNodes,
  seedExcerpts,
  seedSources,
} from "./seedData";
import type {
  BookProject,
  BookSource,
  ChapterDraft,
  DictionaryEntry,
  LibraryCoreState,
  LibraryFragment,
  SourceExcerpt,
} from "./types";

const DRAFT_STORAGE_KEY = "jewik-book-engine:draft:v1";
const LAST_CONCEPT_STORAGE_KEY = "jewik-book-engine:last-concept:v1";
const PROJECT_WORKSPACE_STORAGE_KEY_PREFIX = "jewik-book-engine:project-workspace:v1:";
const DEFAULT_BOOK_MESSAGE = "Primerjava verzij je v tej fazi placeholder.";
const DEFAULT_LIBRARY_TIMESTAMP = seedChapterDrafts[0]?.updatedAt ?? "2026-05-12T12:00:00.000Z";

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
  libraryCore?: LibraryCoreState;
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

function cloneSources(sources: BookSource[]): BookSource[] {
  return sources.map((source) => ({
    ...source,
    excerptIds: [...source.excerptIds],
  }));
}

function cloneBooks(books: BookProject[]): BookProject[] {
  return books.map((book) => ({
    ...book,
    chapterIds: [...book.chapterIds],
    availableVariants: [...book.availableVariants],
  }));
}

function cloneDictionaryEntries(entries: DictionaryEntry[]): DictionaryEntry[] {
  return entries.map((entry) => ({
    ...entry,
    sourceExcerptIds: [...entry.sourceExcerptIds],
    fragmentIds: [...entry.fragmentIds],
  }));
}

function cloneFragments(fragments: LibraryFragment[]): LibraryFragment[] {
  return fragments.map((fragment) => ({
    ...fragment,
    conceptIds: [...fragment.conceptIds],
    sourceExcerptIds: [...fragment.sourceExcerptIds],
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

function isBookSource(value: unknown): value is BookSource {
  if (!isRecord(value)) {
    return false;
  }

  return (
    typeof value.id === "string" &&
    typeof value.title === "string" &&
    typeof value.kind === "string" &&
    typeof value.status === "string" &&
    typeof value.path === "string" &&
    typeof value.note === "string" &&
    isStringArray(value.excerptIds)
  );
}

function isBookProject(value: unknown): value is BookProject {
  if (!isRecord(value)) {
    return false;
  }

  return (
    typeof value.id === "string" &&
    typeof value.title === "string" &&
    typeof value.summary === "string" &&
    isStringArray(value.chapterIds) &&
    isStringArray(value.availableVariants) &&
    typeof value.canonLabel === "string"
  );
}

function isDictionaryEntryStatus(value: unknown): value is DictionaryEntry["status"] {
  return value === "DRAFT" || value === "REVIEW" || value === "CANON" || value === "PARKED";
}

function isFragmentStatus(value: unknown): value is LibraryFragment["status"] {
  return value === "DRAFT" || value === "REVIEW" || value === "CANON" || value === "PARKED";
}

function isDictionaryEntry(value: unknown): value is DictionaryEntry {
  if (!isRecord(value)) {
    return false;
  }

  return (
    typeof value.id === "string" &&
    typeof value.term === "string" &&
    typeof value.meaning === "string" &&
    isDictionaryEntryStatus(value.status) &&
    isStringArray(value.sourceExcerptIds) &&
    isStringArray(value.fragmentIds) &&
    typeof value.createdAt === "string" &&
    typeof value.updatedAt === "string"
  );
}

function isLibraryFragment(value: unknown): value is LibraryFragment {
  if (!isRecord(value)) {
    return false;
  }

  return (
    typeof value.id === "string" &&
    typeof value.title === "string" &&
    typeof value.body === "string" &&
    isStringArray(value.conceptIds) &&
    isStringArray(value.sourceExcerptIds) &&
    (value.chapterId === undefined || typeof value.chapterId === "string") &&
    isFragmentStatus(value.status) &&
    typeof value.createdAt === "string" &&
    typeof value.updatedAt === "string"
  );
}

function isLibraryCoreState(value: unknown): value is LibraryCoreState {
  if (!isRecord(value)) {
    return false;
  }

  return (
    Array.isArray(value.dictionaryEntries) &&
    value.dictionaryEntries.every(isDictionaryEntry) &&
    Array.isArray(value.sources) &&
    value.sources.every(isBookSource) &&
    Array.isArray(value.excerpts) &&
    value.excerpts.every(isSourceExcerpt) &&
    Array.isArray(value.fragments) &&
    value.fragments.every(isLibraryFragment) &&
    Array.isArray(value.chapters) &&
    value.chapters.every(isChapterDraft) &&
    Array.isArray(value.books) &&
    value.books.every(isBookProject)
  );
}

type ProjectWorkspaceSnapshotInput = Omit<ProjectWorkspaceSnapshot, "libraryCore"> & {
  libraryCore?: unknown;
};

function isProjectWorkspaceSnapshotBase(value: unknown): value is ProjectWorkspaceSnapshotInput {
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

function normalizeTerm(value: string): string {
  return value.trim().toLowerCase();
}

function mergeChapterDraftIntoChapters(
  chapters: ChapterDraft[],
  chapterDraft: ChapterDraft,
): ChapterDraft[] {
  const nextDraft = cloneDraft(chapterDraft);
  const existingIndex = chapters.findIndex((chapter) => chapter.id === nextDraft.id);

  if (existingIndex === -1) {
    return [...chapters, nextDraft];
  }

  return chapters.map((chapter, index) => (index === existingIndex ? nextDraft : cloneDraft(chapter)));
}

function createDefaultDictionaryEntries(excerpts: SourceExcerpt[]): DictionaryEntry[] {
  return seedConceptNodes.map((node) => {
    const sourceExcerptIds = excerpts
      .filter((excerpt) => {
        const normalizedHints = excerpt.conceptHints.map(normalizeTerm);
        return (
          normalizedHints.includes(node.normalizedTerm) ||
          normalizedHints.includes(normalizeTerm(node.term)) ||
          node.aliases.some((alias) => normalizedHints.includes(normalizeTerm(alias)))
        );
      })
      .map((excerpt) => excerpt.id);

    return {
      id: `dictionary-${node.id}`,
      term: node.term,
      meaning: node.draftDefinition,
      status: "DRAFT",
      sourceExcerptIds,
      fragmentIds: [],
      createdAt: DEFAULT_LIBRARY_TIMESTAMP,
      updatedAt: DEFAULT_LIBRARY_TIMESTAMP,
    };
  });
}

export function createDefaultLibraryCoreState(
  chapterDraft: ChapterDraft = cloneDraft(seedChapterDrafts[0]!),
  excerpts: SourceExcerpt[] = cloneExcerpts(seedExcerpts),
): LibraryCoreState {
  return {
    dictionaryEntries: createDefaultDictionaryEntries(excerpts),
    sources: cloneSources(seedSources),
    excerpts: cloneExcerpts(excerpts),
    fragments: [],
    chapters: mergeChapterDraftIntoChapters(
      seedChapterDrafts.map((chapter) => cloneDraft(chapter)),
      chapterDraft,
    ),
    books: cloneBooks(seedBookProjects),
  };
}

function cloneLibraryCoreState(libraryCore: LibraryCoreState): LibraryCoreState {
  return {
    dictionaryEntries: cloneDictionaryEntries(libraryCore.dictionaryEntries),
    sources: cloneSources(libraryCore.sources),
    excerpts: cloneExcerpts(libraryCore.excerpts),
    fragments: cloneFragments(libraryCore.fragments),
    chapters: libraryCore.chapters.map((chapter) => cloneDraft(chapter)),
    books: cloneBooks(libraryCore.books),
  };
}

export function normalizeProjectWorkspaceSnapshot(
  snapshot: ProjectWorkspaceSnapshotInput,
): ProjectWorkspaceSnapshot {
  const chapterDraft = cloneDraft(snapshot.chapterDraft);
  const excerpts = cloneExcerpts(snapshot.excerpts);
  const nextLibraryCore = isLibraryCoreState(snapshot.libraryCore)
    ? (() => {
        const clonedCore = cloneLibraryCoreState(snapshot.libraryCore);

        return {
          ...clonedCore,
          excerpts: cloneExcerpts(excerpts),
          chapters: mergeChapterDraftIntoChapters(clonedCore.chapters, chapterDraft),
        };
      })()
    : createDefaultLibraryCoreState(chapterDraft, excerpts);

  return {
    ...snapshot,
    chapterDraft,
    excerpts,
    libraryCore: nextLibraryCore,
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
  const nextExcerpts = cloneExcerpts(seedExcerpts);

  return {
    activeConcept: fallbackConcept,
    bookMessage: DEFAULT_BOOK_MESSAGE,
    chapterDraft: nextDraft,
    conceptInput: fallbackConcept,
    draftState: fallbackDraft ? "shranjeno" : "nespremenjeno",
    excerpts: nextExcerpts,
    libraryCore: createDefaultLibraryCoreState(nextDraft, nextExcerpts),
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
    if (!isProjectWorkspaceSnapshotBase(parsed)) {
      return createDefaultProjectWorkspace(useLegacyFallback);
    }

    return normalizeProjectWorkspaceSnapshot(parsed);
  } catch {
    return createDefaultProjectWorkspace(useLegacyFallback);
  }
}

export function writeProjectWorkspace(
  projectId: string,
  snapshot: ProjectWorkspaceSnapshot,
  syncLegacy = false,
): void {
  const storage = getSafeStorage();
  const existingRaw = storage.getItem(getProjectWorkspaceKey(projectId));
  let existingLibraryCore: LibraryCoreState | undefined;

  if (existingRaw) {
    try {
      const parsed = JSON.parse(existingRaw) as unknown;
      if (isProjectWorkspaceSnapshotBase(parsed)) {
        existingLibraryCore = normalizeProjectWorkspaceSnapshot(parsed).libraryCore;
      }
    } catch {
      existingLibraryCore = undefined;
    }
  }

  const nextSnapshot = normalizeProjectWorkspaceSnapshot({
    ...snapshot,
    libraryCore: snapshot.libraryCore ?? existingLibraryCore,
  });

  storage.setItem(getProjectWorkspaceKey(projectId), JSON.stringify(nextSnapshot));

  if (syncLegacy) {
    saveDraftToLocalStorage(nextSnapshot.chapterDraft);
    saveLastConceptToLocalStorage(nextSnapshot.activeConcept || nextSnapshot.conceptInput || "ne");
  }
}

export function removeProjectWorkspace(projectId: string): void {
  getSafeStorage().removeItem(getProjectWorkspaceKey(projectId));
}
