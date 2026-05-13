export type SourceStatus = "NEW" | "INDEXED" | "USED" | "PARKED";
export type SourceKind = "markdown" | "txt" | "docx" | "pdf" | "unknown";
export type ExcerptStatus =
  | "NEW"
  | "RELEVANT"
  | "PARKED"
  | "REJECTED"
  | "CANON_CANDIDATE";
export type ChapterStatus = "IDEA" | "DRAFT" | "REVIEW" | "CANON" | "PARKED";
export type VariantKind = "RAW" | "CLEAN" | "BOOK" | "SYSTEM" | "READER" | "CANON";
export type DictionaryEntryStatus = "DRAFT" | "REVIEW" | "CANON" | "PARKED";
export type FragmentStatus = "DRAFT" | "REVIEW" | "CANON" | "PARKED";

export type BookSource = {
  id: string;
  title: string;
  kind: SourceKind;
  status: SourceStatus;
  path: string;
  note: string;
  excerptIds: string[];
};

export type SourceExcerpt = {
  id: string;
  sourceId: string;
  sourceTitle: string;
  locator: string;
  text: string;
  status: ExcerptStatus;
  note: string;
  conceptHints: string[];
};

export type ConceptNode = {
  id: string;
  term: string;
  normalizedTerm: string;
  aliases: string[];
  draftDefinition: string;
};

export type ConnotationLink = {
  id: string;
  concept: string;
  target: string;
  note: string;
};

export type AntinomyLink = {
  id: string;
  concept: string;
  opposite: string;
  note: string;
};

export type ChapterCandidate = {
  id: string;
  title: string;
  status: ChapterStatus;
  summary: string;
  supportingExcerptIds: string[];
  relatedConcepts: string[];
};

export type CanonCandidate = {
  id: string;
  concept: string;
  excerptId: string;
  sourceId: string;
  reason: string;
};

export type DictionaryEntry = {
  id: string;
  term: string;
  meaning: string;
  status: DictionaryEntryStatus;
  sourceExcerptIds: string[];
  fragmentIds: string[];
  createdAt: string;
  updatedAt: string;
};

export type ConceptReport = {
  concept: string;
  normalizedConcept: string;
  definition: string;
  relatedConcepts: string[];
  exactMatches: SourceExcerpt[];
  aliasMatches: SourceExcerpt[];
  connotations: ConnotationLink[];
  antinomies: AntinomyLink[];
  chapterCandidates: ChapterCandidate[];
  canonCandidates: CanonCandidate[];
};

export type ChapterDraft = {
  id: string;
  bookId: string;
  title: string;
  status: ChapterStatus;
  text: string;
  linkedExcerptIds: string[];
  linkedConcepts: string[];
  variants: VariantKind[];
  currentVariant: VariantKind;
  updatedAt: string;
};

export type LibraryFragment = {
  id: string;
  title: string;
  body: string;
  conceptIds: string[];
  sourceExcerptIds: string[];
  chapterId?: string;
  status: FragmentStatus;
  createdAt: string;
  updatedAt: string;
};

export type BookProject = {
  id: string;
  title: string;
  summary: string;
  chapterIds: string[];
  availableVariants: VariantKind[];
  canonLabel: string;
};

export type LibraryCoreState = {
  dictionaryEntries: DictionaryEntry[];
  sources: BookSource[];
  excerpts: SourceExcerpt[];
  fragments: LibraryFragment[];
  chapters: ChapterDraft[];
  books: BookProject[];
};
