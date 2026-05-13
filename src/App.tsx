import { useEffect, useState } from "react";

import { ProjectSwitcher } from "./components/ProjectSwitcher";
import conceptAliases from "./jewik-book-engine/conceptAliases";
import { buildConceptReport, normalizeConcept } from "./jewik-book-engine/conceptReport";
import {
  createProjectPackage,
  parseProjectPackage,
  readWorkspaceFromProjectPackage,
  serializeProjectPackage,
  type ProjectPackageParseResult,
} from "./jewik-book-engine/projectPackage";
import {
  seedBookProjects,
  seedChapterDrafts,
  seedExcerpts,
  seedSources,
} from "./jewik-book-engine/seedData";
import {
  createDefaultLibraryCoreState,
  createDefaultProjectWorkspace,
  type ProjectWorkspaceSnapshot,
  readProjectWorkspace,
  removeProjectWorkspace,
  saveDraftToLocalStorage,
  saveLastConceptToLocalStorage,
  writeProjectWorkspace,
} from "./jewik-book-engine/storage";
import {
  createProject,
  deleteProject,
  readProjectRegistry,
  renameProject,
  setActiveProjectId,
  type StudioProjectRegistry,
} from "./store/localStore";
import type {
  BookProject,
  ChapterDraft,
  ChapterStatus,
  DictionaryEntry,
  ExcerptStatus,
  LibraryCoreState,
  SourceExcerpt,
  VariantKind,
} from "./jewik-book-engine/types";
import { getUiText } from "./uiText";

type ViewId = "library" | "concept" | "writing" | "book" | "graph";
type DraftState = ProjectWorkspaceSnapshot["draftState"];
type ProjectTransferTone = "accent" | "good" | "warn" | "danger";
type ProjectTransferState = {
  message: string;
  tone: ProjectTransferTone;
};
const text = getUiText();

const graphNodes = [
  { id: "ne", label: "ne", x: 300, y: 170, accent: true },
  { id: "nic", label: "nič", x: 110, y: 80 },
  { id: "meja", label: "meja", x: 160, y: 275 },
  { id: "locitev", label: "ločitev", x: 290, y: 40 },
  { id: "odsotnost", label: "odsotnost", x: 480, y: 70 },
  { id: "da", label: "da", x: 520, y: 260 },
  { id: "o", label: "O", x: 360, y: 310 },
  { id: "razpoka", label: "razpoka", x: 80, y: 190 },
] as const;

const graphEdges = [
  ["ne", "nic"],
  ["ne", "meja"],
  ["ne", "locitev"],
  ["ne", "odsotnost"],
  ["ne", "da"],
  ["ne", "o"],
  ["ne", "razpoka"],
] as const;

const navigationItems: Array<{ id: ViewId; label: string; hint: string }> = [
  { id: "library", label: text.navigation.library, hint: text.navigationHints.library },
  { id: "concept", label: text.navigation.dictionary, hint: text.navigationHints.dictionary },
  { id: "writing", label: text.navigation.writingDesk, hint: text.navigationHints.writingDesk },
  { id: "book", label: text.navigation.book, hint: text.navigationHints.book },
  { id: "graph", label: text.navigation.conceptGraph, hint: text.navigationHints.conceptGraph },
];

function displayProjectName(name: string): string {
  return name.trim() === "Default project" ? text.hero.defaultProject : name;
}

function injectStyles(): void {
  if (typeof document === "undefined") {
    return;
  }

  if (document.getElementById("jewik-book-engine-style")) {
    return;
  }

  const style = document.createElement("style");
  style.id = "jewik-book-engine-style";
  style.textContent = `
    :root {
      color-scheme: dark;
      --bg: #0b0b14;
      --panel: rgba(18, 17, 31, 0.9);
      --panel-strong: rgba(29, 27, 46, 0.95);
      --panel-soft: rgba(45, 33, 78, 0.38);
      --line: rgba(152, 127, 255, 0.18);
      --line-strong: rgba(190, 164, 255, 0.38);
      --text: #efeaff;
      --muted: #b8aecf;
      --accent: #9b6dff;
      --accent-strong: #c9b1ff;
      --good: #74d6a6;
      --warn: #f4c36b;
      --danger: #f28ca8;
      --shadow: 0 28px 60px rgba(0, 0, 0, 0.35);
      font-family: "Segoe UI", "Helvetica Neue", sans-serif;
      background:
        radial-gradient(circle at top left, rgba(155, 109, 255, 0.26), transparent 26rem),
        radial-gradient(circle at bottom right, rgba(79, 47, 138, 0.34), transparent 28rem),
        linear-gradient(180deg, #090911 0%, #0f1020 100%);
      color: var(--text);
    }

    * {
      box-sizing: border-box;
    }

    body {
      margin: 0;
      min-height: 100vh;
      background: transparent;
      color: var(--text);
    }

    button,
    input,
    textarea {
      font: inherit;
    }

    button {
      cursor: pointer;
      border: 1px solid var(--line);
      border-radius: 14px;
      padding: 0.72rem 0.96rem;
      color: var(--text);
      background: rgba(255, 255, 255, 0.04);
      transition: transform 140ms ease, border-color 140ms ease, background 140ms ease;
    }

    button:hover {
      transform: translateY(-1px);
      border-color: var(--line-strong);
      background: rgba(255, 255, 255, 0.08);
    }

    button.primary {
      border-color: transparent;
      background: linear-gradient(135deg, var(--accent) 0%, #6a39dd 100%);
    }

    button.secondary {
      background: rgba(155, 109, 255, 0.14);
    }

    input,
    textarea {
      width: 100%;
      border: 1px solid var(--line);
      border-radius: 14px;
      padding: 0.82rem 0.9rem;
      background: rgba(10, 10, 18, 0.78);
      color: var(--text);
    }

    textarea {
      min-height: 240px;
      resize: vertical;
    }

    .app-shell {
      display: grid;
      grid-template-columns: 280px minmax(0, 1fr);
      min-height: 100vh;
    }

    .sidebar {
      position: sticky;
      top: 0;
      height: 100vh;
      padding: 1.25rem;
      border-right: 1px solid var(--line);
      background: rgba(9, 10, 20, 0.78);
      backdrop-filter: blur(18px);
      overflow: auto;
    }

    .workspace {
      padding: 1.25rem;
      display: grid;
      gap: 1rem;
    }

    .panel {
      border: 1px solid var(--line);
      border-radius: 24px;
      padding: 1.15rem;
      background: var(--panel);
      box-shadow: var(--shadow);
    }

    .panel.soft {
      background: var(--panel-soft);
    }

    .brand {
      padding-bottom: 1rem;
      margin-bottom: 1rem;
      border-bottom: 1px solid var(--line);
    }

    .brand h1,
    .workspace h2,
    .workspace h3 {
      margin: 0;
      font-family: Georgia, "Times New Roman", serif;
      letter-spacing: -0.04em;
    }

    .brand h1 {
      font-size: 2rem;
      line-height: 0.94;
      margin-bottom: 0.55rem;
    }

    .muted {
      color: var(--muted);
    }

    .nav {
      display: grid;
      gap: 0.55rem;
    }

    .nav button {
      text-align: left;
      border-radius: 18px;
      padding: 0.95rem;
    }

    .nav button.active {
      background: rgba(155, 109, 255, 0.18);
      border-color: rgba(201, 177, 255, 0.42);
    }

    .hint {
      display: block;
      margin-top: 0.25rem;
      font-size: 0.84rem;
      color: var(--muted);
    }

    .hero {
      display: grid;
      gap: 0.95rem;
      grid-template-columns: minmax(0, 1.3fr) minmax(260px, 0.7fr);
    }

    .grid {
      display: grid;
      gap: 1rem;
    }

    .grid.two {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .grid.library {
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    }

    .row {
      display: flex;
      flex-wrap: wrap;
      gap: 0.65rem;
      align-items: center;
      justify-content: space-between;
    }

    .stack {
      display: grid;
      gap: 0.8rem;
    }

    .metric {
      border: 1px solid var(--line);
      border-radius: 18px;
      padding: 0.95rem;
      background: rgba(255, 255, 255, 0.03);
    }

    .metric strong {
      display: block;
      font-size: 1.7rem;
      margin-top: 0.2rem;
    }

    .badge-row {
      display: flex;
      flex-wrap: wrap;
      gap: 0.45rem;
    }

    .badge {
      display: inline-flex;
      align-items: center;
      border: 1px solid var(--line);
      border-radius: 999px;
      padding: 0.28rem 0.62rem;
      font-size: 0.8rem;
      color: var(--muted);
      background: rgba(255, 255, 255, 0.04);
    }

    .badge.good {
      color: var(--good);
      border-color: rgba(116, 214, 166, 0.28);
      background: rgba(116, 214, 166, 0.12);
    }

    .badge.warn {
      color: var(--warn);
      border-color: rgba(244, 195, 107, 0.28);
      background: rgba(244, 195, 107, 0.12);
    }

    .badge.danger {
      color: var(--danger);
      border-color: rgba(242, 140, 168, 0.3);
      background: rgba(242, 140, 168, 0.12);
    }

    .badge.accent {
      color: var(--accent-strong);
      border-color: rgba(201, 177, 255, 0.3);
      background: rgba(155, 109, 255, 0.14);
    }

    .card-list {
      display: grid;
      gap: 0.8rem;
    }

    .card {
      border: 1px solid var(--line);
      border-radius: 20px;
      padding: 0.95rem;
      background: rgba(255, 255, 255, 0.03);
    }

    .card h3 {
      margin-bottom: 0.45rem;
      font-size: 1.1rem;
    }

    .field label {
      display: block;
      margin-bottom: 0.45rem;
      font-size: 0.84rem;
      color: var(--muted);
    }

    .excerpt-actions {
      display: flex;
      flex-wrap: wrap;
      gap: 0.45rem;
      margin-top: 0.75rem;
    }

    .excerpt-actions button {
      padding: 0.46rem 0.74rem;
      border-radius: 999px;
      font-size: 0.84rem;
    }

    .editor-layout {
      display: grid;
      gap: 1rem;
      grid-template-columns: minmax(0, 1.2fr) 320px;
    }

    .book-card {
      display: grid;
      gap: 0.9rem;
    }

    .book-summary {
      display: grid;
      gap: 0.55rem;
    }

    .chapter-list {
      display: grid;
      gap: 0.7rem;
    }

    .graph-wrap {
      overflow: auto;
    }

    .graph {
      width: 100%;
      min-width: 620px;
      height: 360px;
      border: 1px solid var(--line);
      border-radius: 24px;
      background:
        radial-gradient(circle at center, rgba(155, 109, 255, 0.12), transparent 45%),
        rgba(255, 255, 255, 0.02);
    }

    .graph line {
      stroke: rgba(201, 177, 255, 0.46);
      stroke-width: 2;
    }

    .graph circle {
      fill: rgba(20, 18, 33, 0.96);
      stroke: rgba(201, 177, 255, 0.56);
      stroke-width: 2;
    }

    .graph circle.accent {
      fill: rgba(155, 109, 255, 0.26);
      stroke: rgba(233, 224, 255, 0.82);
      stroke-width: 3;
    }

    .graph text {
      fill: var(--text);
      font-size: 14px;
      text-anchor: middle;
      dominant-baseline: middle;
    }

    .pill-note {
      padding: 0.8rem 0.95rem;
      border: 1px dashed var(--line-strong);
      border-radius: 18px;
      color: var(--muted);
      background: rgba(255, 255, 255, 0.03);
    }

    @media (max-width: 1120px) {
      .app-shell {
        grid-template-columns: 1fr;
      }

      .sidebar {
        position: static;
        height: auto;
      }

      .hero,
      .grid.two,
      .editor-layout {
        grid-template-columns: 1fr;
      }
    }
  `;
  document.head.appendChild(style);
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

function cloneLibraryCore(libraryCore: LibraryCoreState): LibraryCoreState {
  return {
    dictionaryEntries: libraryCore.dictionaryEntries.map((entry) => ({
      ...entry,
      sourceExcerptIds: [...entry.sourceExcerptIds],
      fragmentIds: [...entry.fragmentIds],
    })),
    sources: libraryCore.sources.map((source) => ({
      ...source,
      excerptIds: [...source.excerptIds],
    })),
    excerpts: cloneExcerpts(libraryCore.excerpts),
    fragments: libraryCore.fragments.map((fragment) => ({
      ...fragment,
      conceptIds: [...fragment.conceptIds],
      sourceExcerptIds: [...fragment.sourceExcerptIds],
    })),
    chapters: libraryCore.chapters.map((chapter) => cloneDraft(chapter)),
    books: libraryCore.books.map((book) => ({
      ...book,
      chapterIds: [...book.chapterIds],
      availableVariants: [...book.availableVariants],
    })),
  };
}

function getWorkspaceLibraryCore(workspace: ProjectWorkspaceSnapshot): LibraryCoreState {
  return cloneLibraryCore(
    workspace.libraryCore ?? createDefaultLibraryCoreState(workspace.chapterDraft, workspace.excerpts),
  );
}

function stamp(): string {
  return new Date().toISOString();
}

function toneForStatus(value: string): "accent" | "good" | "warn" | "danger" {
  if (["USED", "RELEVANT", "CANON_CANDIDATE", "CANON", "BOOK"].includes(value)) {
    return "good";
  }

  if (["NEW", "IDEA", "RAW", "SYSTEM", "READER", "CLEAN"].includes(value)) {
    return "accent";
  }

  if (["INDEXED", "DRAFT", "REVIEW", "PARKED"].includes(value)) {
    return "warn";
  }

  return "danger";
}

function findChapterById(chapterId: string): ChapterDraft | undefined {
  return seedChapterDrafts.find((chapter) => chapter.id === chapterId);
}

function sanitizeProjectFileSegment(name: string): string {
  return name
    .trim()
    .toLowerCase()
    .replace(/[^a-z0-9]+/gi, "-")
    .replace(/^-+|-+$/g, "")
    .replace(/-{2,}/g, "-") || "project";
}

function buildProjectExportFileName(projectName: string): string {
  return `jewik-project-${sanitizeProjectFileSegment(projectName)}.json`;
}

function resolveImportedProjectName(
  baseName: string,
  existingProjects: Array<{ name: string }>,
): string {
  const trimmedBaseName = baseName.trim();
  const takenNames = new Set(existingProjects.map((project) => project.name));

  if (!takenNames.has(trimmedBaseName)) {
    return trimmedBaseName;
  }

  const firstImportName = `${trimmedBaseName} (import)`;
  if (!takenNames.has(firstImportName)) {
    return firstImportName;
  }

  let suffix = 2;
  while (takenNames.has(`${trimmedBaseName} (import ${suffix})`)) {
    suffix += 1;
  }

  return `${trimmedBaseName} (import ${suffix})`;
}

function getProjectPackageErrorMessage(result: ProjectPackageParseResult): string {
  if (result.ok) {
    return "";
  }

  switch (result.code) {
    case "INVALID_JSON":
      return text.transfer.importInvalidJson;
    case "INVALID_PACKAGE_TYPE":
      return text.transfer.importInvalidPackageType;
    case "UNSUPPORTED_PACKAGE_VERSION":
      return text.transfer.importUnsupportedVersion;
    case "INVALID_PROJECT":
      return text.transfer.importInvalidProject;
    case "INVALID_WORKSPACE":
      return text.transfer.importInvalidWorkspace;
    case "INVALID_EXPORTED_AT":
      return text.transfer.importInvalidExportedAt;
    default:
      return text.transfer.importInvalidPackage;
  }
}

function downloadTextFile(fileName: string, text: string): void {
  if (typeof window === "undefined" || typeof document === "undefined") {
    throw new Error("Download is not available in the current environment.");
  }

  const blob = new Blob([text], { type: "application/json;charset=utf-8" });
  const objectUrl = window.URL.createObjectURL(blob);
  const anchor = document.createElement("a");

  anchor.href = objectUrl;
  anchor.download = fileName;
  document.body.appendChild(anchor);
  anchor.click();
  anchor.remove();
  window.URL.revokeObjectURL(objectUrl);
}

function workspacesMatch(
  left: ProjectWorkspaceSnapshot,
  right: ProjectWorkspaceSnapshot,
): boolean {
  return JSON.stringify(left) === JSON.stringify(right);
}

function feedbackLabelForTone(tone: ProjectTransferTone): string {
  switch (tone) {
    case "good":
      return text.projectSwitcher.success;
    case "warn":
      return text.projectSwitcher.warning;
    case "danger":
      return text.projectSwitcher.error;
    default:
      return text.projectSwitcher.info;
  }
}

function countAllMatches(excerpts: SourceExcerpt[], concept: string): number {
  return buildConceptReport(concept, excerpts, conceptAliases).exactMatches.length +
    buildConceptReport(concept, excerpts, conceptAliases).aliasMatches.length;
}

function labelForStatus(value: string): string {
  return text.statusLabels[value] ?? value;
}

function labelForSourceKind(value: string): string {
  return text.sourceKindLabels[value] ?? value;
}

function Badge({ value, toneValue }: { value: string; toneValue?: string }) {
  return <span className={`badge ${toneForStatus(toneValue ?? value)}`}>{value}</span>;
}

function ExcerptCard({
  excerpt,
  onStatusChange,
}: {
  excerpt: SourceExcerpt;
  onStatusChange: (excerptId: string, status: ExcerptStatus) => void;
}) {
  return (
    <article className="card">
      <div className="row">
        <strong>{excerpt.sourceTitle}</strong>
        <Badge value={labelForStatus(excerpt.status)} toneValue={excerpt.status} />
      </div>
      <p>{excerpt.text}</p>
      <div className="badge-row">
        <span className="badge">{excerpt.locator}</span>
        {excerpt.conceptHints.map((hint) => (
          <span key={`${excerpt.id}-${hint}`} className="badge">
            {hint}
          </span>
        ))}
      </div>
      <p className="muted">{excerpt.note}</p>
      <div className="excerpt-actions">
        <button onClick={() => onStatusChange(excerpt.id, "RELEVANT")}>relevantno</button>
        <button onClick={() => onStatusChange(excerpt.id, "PARKED")}>parkirano</button>
        <button onClick={() => onStatusChange(excerpt.id, "REJECTED")}>zavrnjeno</button>
        <button onClick={() => onStatusChange(excerpt.id, "CANON_CANDIDATE")}>kandidat za kanon</button>
      </div>
    </article>
  );
}

export function App() {
  const initialProjectRegistry = readProjectRegistry();
  const initialWorkspace = readProjectWorkspace(initialProjectRegistry.activeProjectId, true);

  const [activeView, setActiveView] = useState<ViewId>("library");
  const [projectRegistry, setProjectRegistry] = useState<StudioProjectRegistry>(initialProjectRegistry);
  const [activeProjectId, setActiveProjectIdState] = useState(initialProjectRegistry.activeProjectId);
  const [excerpts, setExcerpts] = useState<SourceExcerpt[]>(initialWorkspace.excerpts);
  const [conceptInput, setConceptInput] = useState(initialWorkspace.conceptInput);
  const [activeConcept, setActiveConcept] = useState(initialWorkspace.activeConcept);
  const [chapterDraft, setChapterDraft] = useState<ChapterDraft>(initialWorkspace.chapterDraft);
  const [libraryCore, setLibraryCore] = useState<LibraryCoreState>(getWorkspaceLibraryCore(initialWorkspace));
  const [draftState, setDraftState] = useState<DraftState>(initialWorkspace.draftState);
  const [lastSavedSnapshot, setLastSavedSnapshot] = useState(initialWorkspace.lastSavedSnapshot);
  const [bookMessage, setBookMessage] = useState(initialWorkspace.bookMessage);
  const [projectTransferState, setProjectTransferState] = useState<ProjectTransferState | null>(null);
  const [dictionaryTerm, setDictionaryTerm] = useState("");
  const [dictionaryMeaning, setDictionaryMeaning] = useState("");
  const [dictionaryEntryState, setDictionaryEntryState] = useState<ProjectTransferState | null>(null);

  useEffect(() => {
    injectStyles();
  }, []);

  useEffect(() => {
    if (typeof document !== "undefined") {
      document.title = text.brand.title;
    }
  }, []);

  useEffect(() => {
    writeProjectWorkspace(
      activeProjectId,
      {
        activeConcept,
        bookMessage,
        chapterDraft,
        conceptInput,
        draftState,
        excerpts,
        libraryCore,
        lastSavedSnapshot,
      },
      true,
    );
  }, [
    activeConcept,
    activeProjectId,
    bookMessage,
    chapterDraft,
    conceptInput,
    draftState,
    excerpts,
    libraryCore,
    lastSavedSnapshot,
  ]);

  const report = buildConceptReport(activeConcept, excerpts, conceptAliases);
  const reportMatches = [...report.exactMatches, ...report.aliasMatches];
  const dictionaryEntries = libraryCore.dictionaryEntries;
  const linkedExcerpts = chapterDraft.linkedExcerptIds
    .map((excerptId) => excerpts.find((excerpt) => excerpt.id === excerptId))
    .filter((excerpt): excerpt is SourceExcerpt => Boolean(excerpt));
  const activeProject =
    projectRegistry.projects.find((project) => project.id === activeProjectId) ?? null;
  const visibleProjects = projectRegistry.projects.map((project) => ({
    ...project,
    name: displayProjectName(project.name),
  }));
  const activeProjectName = activeProject ? displayProjectName(activeProject.name) : text.hero.defaultProject;

  function getCurrentWorkspace(): ProjectWorkspaceSnapshot {
    return {
      activeConcept,
      bookMessage,
      chapterDraft,
      conceptInput,
      draftState,
      excerpts,
      libraryCore,
      lastSavedSnapshot,
    };
  }

  function applyWorkspace(workspace: ProjectWorkspaceSnapshot): void {
    setExcerpts(cloneExcerpts(workspace.excerpts));
    setConceptInput(workspace.conceptInput);
    setActiveConcept(workspace.activeConcept);
    setChapterDraft(cloneDraft(workspace.chapterDraft));
    setLibraryCore(getWorkspaceLibraryCore(workspace));
    setDraftState(workspace.draftState);
    setLastSavedSnapshot(workspace.lastSavedSnapshot);
    setBookMessage(workspace.bookMessage);
    setDictionaryTerm("");
    setDictionaryMeaning("");
    setDictionaryEntryState(null);
  }

  function refreshProjectRegistry(): StudioProjectRegistry {
    const nextRegistry = readProjectRegistry();
    setProjectRegistry(nextRegistry);
    return nextRegistry;
  }

  function rollbackImportedProject(
    importedProjectId: string,
    previousActiveProjectId: string,
    previousWorkspace: ProjectWorkspaceSnapshot,
  ): void {
    deleteProject(importedProjectId);
    removeProjectWorkspace(importedProjectId);
    setActiveProjectId(previousActiveProjectId);

    const rollbackRegistry = refreshProjectRegistry();
    setActiveProjectIdState(rollbackRegistry.activeProjectId);
    applyWorkspace(previousWorkspace);
  }

  function handleSwitchProject(projectId: string): void {
    if (projectId === activeProjectId) {
      return;
    }

    writeProjectWorkspace(activeProjectId, getCurrentWorkspace(), true);
    setActiveProjectId(projectId);

    const nextRegistry = refreshProjectRegistry();
    setActiveProjectIdState(nextRegistry.activeProjectId);
    applyWorkspace(readProjectWorkspace(nextRegistry.activeProjectId));
  }

  function handleCreateProject(name: string): void {
    writeProjectWorkspace(activeProjectId, getCurrentWorkspace(), true);
    const createdProject = createProject(name);
    const nextWorkspace = createDefaultProjectWorkspace(false);

    writeProjectWorkspace(createdProject.id, nextWorkspace);
    setActiveProjectId(createdProject.id);

    const nextRegistry = refreshProjectRegistry();
    setActiveProjectIdState(nextRegistry.activeProjectId);
    applyWorkspace(nextWorkspace);
  }

  function handleRenameProject(projectId: string, nextName: string): void {
    if (!nextName.trim()) {
      return;
    }

    renameProject(projectId, nextName);
    refreshProjectRegistry();
  }

  function handleDeleteProject(projectId: string): void {
    const deletingActiveProject = projectId === activeProjectId;

    if (deletingActiveProject) {
      writeProjectWorkspace(activeProjectId, getCurrentWorkspace(), true);
    }

    deleteProject(projectId);
    removeProjectWorkspace(projectId);

    const nextRegistry = refreshProjectRegistry();
    setActiveProjectIdState(nextRegistry.activeProjectId);

    if (deletingActiveProject) {
      applyWorkspace(readProjectWorkspace(nextRegistry.activeProjectId));
    }
  }

  function handleExportProject(): void {
    if (!activeProject) {
      setProjectTransferState({
        tone: "danger",
        message: text.transfer.exportUnavailableProject,
      });
      return;
    }

    const projectPackage = createProjectPackage(
      {
        id: activeProject.id,
        name: activeProject.name,
      },
      getCurrentWorkspace(),
    );

    if (!projectPackage) {
      setProjectTransferState({
        tone: "danger",
        message: text.transfer.exportPackageFailed,
      });
      return;
    }

    try {
      downloadTextFile(
        buildProjectExportFileName(activeProject.name),
        serializeProjectPackage(projectPackage),
      );
      setProjectTransferState({
        tone: "good",
        message: text.transfer.exportSuccess(activeProject.name),
      });
    } catch {
      setProjectTransferState({
        tone: "danger",
        message: text.transfer.exportBrowserFailed,
      });
    }
  }

  async function handleImportProject(file: File): Promise<void> {
    const previousActiveProjectId = activeProjectId;
    const previousWorkspace = getCurrentWorkspace();

    let importedProjectId: string | null = null;

    try {
      const jsonText = await file.text();
      const parsedPackage = parseProjectPackage(jsonText);

      if (!parsedPackage.ok) {
        setProjectTransferState({
          tone: "danger",
          message: getProjectPackageErrorMessage(parsedPackage),
        });
        return;
      }

      const importedWorkspace = readWorkspaceFromProjectPackage(parsedPackage.value);
      if (!importedWorkspace) {
        setProjectTransferState({
          tone: "danger",
          message: text.transfer.importInvalidWorkspace,
        });
        return;
      }

      const importedProjectName = resolveImportedProjectName(
        parsedPackage.value.project.name,
        projectRegistry.projects,
      );
      const createdProject = createProject(importedProjectName);
      importedProjectId = createdProject.id;

      const createdRegistry = refreshProjectRegistry();
      if (!createdRegistry.projects.some((project) => project.id === createdProject.id)) {
        importedProjectId = null;
        setProjectTransferState({
          tone: "danger",
          message: text.transfer.importProjectCreateFailed,
        });
        return;
      }

      writeProjectWorkspace(createdProject.id, importedWorkspace);
      const persistedImportedWorkspace = readProjectWorkspace(createdProject.id);
      if (!workspacesMatch(persistedImportedWorkspace, importedWorkspace)) {
        rollbackImportedProject(createdProject.id, previousActiveProjectId, previousWorkspace);
        importedProjectId = null;
        setProjectTransferState({
          tone: "danger",
          message: text.transfer.importWorkspacePersistFailed,
        });
        return;
      }

      setActiveProjectId(createdProject.id);
      const nextRegistry = refreshProjectRegistry();
      if (nextRegistry.activeProjectId !== createdProject.id) {
        rollbackImportedProject(createdProject.id, previousActiveProjectId, previousWorkspace);
        importedProjectId = null;
        setProjectTransferState({
          tone: "danger",
          message: text.transfer.importActivationFailed,
        });
        return;
      }

      setActiveProjectIdState(nextRegistry.activeProjectId);
      applyWorkspace(importedWorkspace);
      setProjectTransferState({
        tone: "good",
        message: text.transfer.importSuccess(importedProjectName),
      });
    } catch {
      if (importedProjectId) {
        rollbackImportedProject(importedProjectId, previousActiveProjectId, previousWorkspace);
      }

      setProjectTransferState({
        tone: "danger",
        message: text.transfer.importReadFailed,
      });
    }
  }

  function handleAnalyze(): void {
    const nextConcept = conceptInput.trim() || "ne";
    setActiveConcept(nextConcept);
    saveLastConceptToLocalStorage(nextConcept);
  }

  function handleAddDictionaryEntry(): void {
    const nextTerm = dictionaryTerm.trim();
    const nextMeaning = dictionaryMeaning.trim();

    if (!nextTerm) {
      setDictionaryEntryState({
        tone: "warn",
        message: text.conceptDesk.entryTermRequired,
      });
      return;
    }

    if (!nextMeaning) {
      setDictionaryEntryState({
        tone: "warn",
        message: text.conceptDesk.entryMeaningRequired,
      });
      return;
    }

    const timestamp = stamp();
    const nextEntry: DictionaryEntry = {
      id: `dictionary-${sanitizeProjectFileSegment(nextTerm)}-${Date.now().toString(36)}`,
      term: nextTerm,
      meaning: nextMeaning,
      status: "DRAFT",
      sourceExcerptIds: [],
      fragmentIds: [],
      createdAt: timestamp,
      updatedAt: timestamp,
    };

    setLibraryCore((current) => ({
      ...current,
      dictionaryEntries: [nextEntry, ...current.dictionaryEntries],
    }));
    setDictionaryTerm("");
    setDictionaryMeaning("");
    setDictionaryEntryState({
      tone: "good",
      message: text.conceptDesk.entryCreated(nextTerm),
    });
  }

  function handleExcerptStatusChange(excerptId: string, status: ExcerptStatus): void {
    setExcerpts((current) =>
      current.map((excerpt) => (excerpt.id === excerptId ? { ...excerpt, status } : excerpt)),
    );
  }

  function updateDraft(nextDraft: ChapterDraft): void {
    setChapterDraft(nextDraft);
    const snapshot = JSON.stringify(nextDraft);
    setDraftState(snapshot === lastSavedSnapshot ? "nespremenjeno" : "osnutek");
  }

  function handleDraftTitleChange(title: string): void {
    updateDraft({
      ...chapterDraft,
      title,
      updatedAt: stamp(),
    });
  }

  function handleDraftTextChange(text: string): void {
    updateDraft({
      ...chapterDraft,
      text,
      updatedAt: stamp(),
    });
  }

  function handleAddExcerpt(): void {
    const nextExcerpt = reportMatches.find(
      (excerpt) => !chapterDraft.linkedExcerptIds.includes(excerpt.id),
    );

    if (!nextExcerpt) {
      return;
    }

    updateDraft({
      ...chapterDraft,
      linkedExcerptIds: [...chapterDraft.linkedExcerptIds, nextExcerpt.id],
      updatedAt: stamp(),
    });
  }

  function handleLinkConcept(): void {
    const normalized = normalizeConcept(activeConcept);
    if (!normalized || chapterDraft.linkedConcepts.includes(normalized)) {
      return;
    }

    updateDraft({
      ...chapterDraft,
      linkedConcepts: [...chapterDraft.linkedConcepts, normalized],
      updatedAt: stamp(),
    });
  }

  function handleSaveVersion(): void {
    const nextDraft = {
      ...chapterDraft,
      updatedAt: stamp(),
      currentVariant: ("RAW" satisfies VariantKind),
    };
    saveDraftToLocalStorage(nextDraft);
    setChapterDraft(nextDraft);
    const snapshot = JSON.stringify(nextDraft);
    setLastSavedSnapshot(snapshot);
    setDraftState("shranjeno");
  }

  function renderLibraryView() {
    return (
      <section className="grid library">
        {seedSources.map((source) => (
          <article key={source.id} className="panel">
            <div className="row">
              <h3>{source.title}</h3>
              <Badge value={labelForStatus(source.status)} toneValue={source.status} />
            </div>
            <p className="muted">{source.note}</p>
            <div className="badge-row">
              <span className="badge">{labelForSourceKind(source.kind)}</span>
              <span className="badge">{source.path}</span>
              <span className="badge">{source.excerptIds.length} izsekov</span>
            </div>
          </article>
        ))}
      </section>
    );
  }

  function renderConceptDeskView() {
    return (
      <div className="grid">
        <section className="panel">
          <div className="row">
            <div>
              <h2>{text.conceptDesk.title}</h2>
              <p className="muted">
                {text.conceptDesk.flow}
              </p>
            </div>
            <Badge value={report.normalizedConcept || text.conceptDesk.emptyConcept} />
          </div>
          <div className="grid two">
            <div className="field">
              <label htmlFor="concept-input">{text.conceptDesk.inputLabel}</label>
              <input
                id="concept-input"
                value={conceptInput}
                onChange={(event) => setConceptInput(event.target.value)}
                placeholder={text.conceptDesk.inputPlaceholder}
              />
            </div>
            <div className="field">
              <label>&nbsp;</label>
              <button className="primary" onClick={handleAnalyze}>
                {text.conceptDesk.analyze}
              </button>
            </div>
          </div>
        </section>

        <section className="grid two">
          <article className="panel soft">
            <div className="row">
              <div>
                <h3>{text.conceptDesk.newEntryTitle}</h3>
                <p className="muted">{text.conceptDesk.newEntryDescription}</p>
              </div>
              <Badge value={`${dictionaryEntries.length}`} />
            </div>
            <div className="stack" style={{ marginTop: "1rem" }}>
              <div className="field">
                <label htmlFor="dictionary-term">{text.conceptDesk.entryTermLabel}</label>
                <input
                  id="dictionary-term"
                  value={dictionaryTerm}
                  onChange={(event) => setDictionaryTerm(event.target.value)}
                  placeholder={text.conceptDesk.entryTermPlaceholder}
                />
              </div>
              <div className="field">
                <label htmlFor="dictionary-meaning">{text.conceptDesk.entryMeaningLabel}</label>
                <textarea
                  id="dictionary-meaning"
                  value={dictionaryMeaning}
                  onChange={(event) => setDictionaryMeaning(event.target.value)}
                  placeholder={text.conceptDesk.entryMeaningPlaceholder}
                />
              </div>
              <div className="row">
                <button className="primary" onClick={handleAddDictionaryEntry}>
                  {text.conceptDesk.addEntry}
                </button>
              </div>
              {dictionaryEntryState ? (
                <div className="badge-row">
                  <Badge
                    value={feedbackLabelForTone(dictionaryEntryState.tone)}
                    toneValue={dictionaryEntryState.tone}
                  />
                  <span className="muted">{dictionaryEntryState.message}</span>
                </div>
              ) : null}
            </div>
          </article>

          <article className="panel">
            <div className="row">
              <div>
                <h3>{text.conceptDesk.dictionaryEntriesTitle}</h3>
                <p className="muted">{text.conceptDesk.dictionaryEntriesDescription}</p>
              </div>
              <Badge value={`${dictionaryEntries.length}`} />
            </div>
            {dictionaryEntries.length > 0 ? (
              <div className="card-list" style={{ marginTop: "0.8rem" }}>
                {dictionaryEntries.map((entry) => (
                  <div key={entry.id} className="card">
                    <div className="row">
                      <strong>{entry.term}</strong>
                      <Badge value={labelForStatus(entry.status)} toneValue={entry.status} />
                    </div>
                    <p>{entry.meaning}</p>
                    <div className="badge-row">
                      <span className="badge">
                        {entry.sourceExcerptIds.length} {text.conceptDesk.entrySourceLinks}
                      </span>
                      <span className="badge">
                        {entry.fragmentIds.length} {text.conceptDesk.entryFragmentLinks}
                      </span>
                    </div>
                  </div>
                ))}
              </div>
            ) : (
              <p className="pill-note" style={{ marginTop: "0.8rem" }}>
                {text.conceptDesk.noDictionaryEntries}
              </p>
            )}
          </article>

          <article className="panel">
            <h3>{text.conceptDesk.semanticReport}</h3>
            <p>{report.definition}</p>
            <div className="stack">
              <div>
                <strong>{text.conceptDesk.relatedConcepts}</strong>
                <div className="badge-row" style={{ marginTop: "0.55rem" }}>
                  {report.relatedConcepts.map((item) => (
                    <span key={item} className="badge accent">
                      {item}
                    </span>
                  ))}
                </div>
              </div>
              <div>
                <strong>{text.conceptDesk.connotations}</strong>
                <div className="card-list" style={{ marginTop: "0.7rem" }}>
                  {report.connotations.map((item) => (
                    <div key={item.id} className="card">
                      <strong>{item.target}</strong>
                      <p className="muted">{item.note}</p>
                    </div>
                  ))}
                </div>
              </div>
              <div>
                <strong>{text.conceptDesk.antinomies}</strong>
                <div className="card-list" style={{ marginTop: "0.7rem" }}>
                  {report.antinomies.map((item) => (
                    <div key={item.id} className="card">
                      <strong>{item.opposite}</strong>
                      <p className="muted">{item.note}</p>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          </article>

          <article className="panel">
            <h3>{text.conceptDesk.chapterProposal}</h3>
            {report.chapterCandidates.length > 0 ? (
              <div className="card-list">
                {report.chapterCandidates.map((candidate) => (
                  <div key={candidate.id} className="card">
                    <div className="row">
                      <strong>{candidate.title}</strong>
                      <Badge value={labelForStatus(candidate.status)} toneValue={candidate.status} />
                    </div>
                    <p>{candidate.summary}</p>
                    <div className="badge-row">
                      {candidate.relatedConcepts.map((item) => (
                        <span key={`${candidate.id}-${item}`} className="badge">
                          {item}
                        </span>
                      ))}
                    </div>
                  </div>
                ))}
              </div>
            ) : (
              <p className="pill-note">{text.conceptDesk.notEnoughForChapter}</p>
            )}

            <h3 style={{ marginTop: "1rem" }}>{text.conceptDesk.canonCandidates}</h3>
            {report.canonCandidates.length > 0 ? (
              <div className="card-list">
                {report.canonCandidates.map((candidate) => (
                  <div key={candidate.id} className="card">
                    <strong>{candidate.concept}</strong>
                    <p className="muted">{candidate.reason}</p>
                  </div>
                ))}
              </div>
            ) : (
              <p className="pill-note">{text.conceptDesk.noCanonCandidates}</p>
            )}
          </article>
        </section>

        <section className="panel">
          <h3>{text.conceptDesk.excerptsWithSource}</h3>
          <div className="card-list" style={{ marginTop: "0.8rem" }}>
            {reportMatches.map((excerpt) => (
              <ExcerptCard
                key={excerpt.id}
                excerpt={excerpt}
                onStatusChange={handleExcerptStatusChange}
              />
            ))}
          </div>
        </section>
      </div>
    );
  }

  function renderWritingDeskView() {
    return (
      <section className="editor-layout">
        <article className="panel">
          <div className="row">
            <div>
              <h2>{text.writingDesk.title}</h2>
              <p className="muted">{text.writingDesk.description}</p>
            </div>
            <div className="badge-row">
              <Badge value={labelForStatus(chapterDraft.status)} toneValue={chapterDraft.status} />
              <Badge value={labelForStatus(draftState)} />
            </div>
          </div>
          <div className="stack" style={{ marginTop: "1rem" }}>
            <div className="field">
              <label htmlFor="chapter-title">{text.writingDesk.chapterTitle}</label>
              <input
                id="chapter-title"
                value={chapterDraft.title}
                onChange={(event) => handleDraftTitleChange(event.target.value)}
              />
            </div>
            <div className="field">
              <label htmlFor="chapter-body">{text.writingDesk.chapterBody}</label>
              <textarea
                id="chapter-body"
                value={chapterDraft.text}
                onChange={(event) => handleDraftTextChange(event.target.value)}
              />
            </div>
            <div className="row">
              <button onClick={handleAddExcerpt}>{text.writingDesk.addExcerpt}</button>
              <button onClick={handleLinkConcept}>{text.writingDesk.linkConcept}</button>
              <button className="primary" onClick={handleSaveVersion}>
                {text.writingDesk.saveVersion}
              </button>
            </div>
            <div className="badge-row">
              {chapterDraft.linkedConcepts.map((item) => (
                <span key={item} className="badge accent">
                  {item}
                </span>
              ))}
              {chapterDraft.variants.map((variant) => (
                <span key={variant} className="badge">
                  {labelForStatus(variant)}
                </span>
              ))}
            </div>
          </div>
        </article>

        <aside className="panel soft">
          <h3>{text.writingDesk.linkedExcerpts}</h3>
          <div className="card-list" style={{ marginTop: "0.8rem" }}>
            {linkedExcerpts.map((excerpt) => (
              <div key={excerpt.id} className="card">
                <div className="row">
                  <strong>{excerpt.sourceTitle}</strong>
                  <Badge value={labelForStatus(excerpt.status)} toneValue={excerpt.status} />
                </div>
                <p>{excerpt.text}</p>
                <p className="muted">{excerpt.locator}</p>
              </div>
            ))}
          </div>
        </aside>
      </section>
    );
  }

  function renderBookDeskView() {
    return (
      <div className="grid">
        <section className="panel">
          <div className="row">
            <div>
              <h2>{text.book.title}</h2>
              <p className="muted">{text.book.description}</p>
            </div>
            <button className="secondary" onClick={() => setBookMessage(text.book.compareVersionsNextStep)}>
              {text.book.compareVersions}
            </button>
          </div>
          <p className="pill-note" style={{ marginTop: "0.9rem" }}>
            {bookMessage}
          </p>
        </section>

        <section className="grid two">
          {seedBookProjects.map((project: BookProject) => (
            <article key={project.id} className="panel book-card">
              <div className="book-summary">
                <div className="row">
                  <h3>{project.title}</h3>
                  <span className="badge accent">{project.canonLabel}</span>
                </div>
                <p className="muted">{project.summary}</p>
                <div className="badge-row">
                  {project.availableVariants.map((variant) => (
                    <span key={`${project.id}-${variant}`} className="badge">
                      {labelForStatus(variant)}
                    </span>
                  ))}
                </div>
              </div>
              <div className="chapter-list">
                {project.chapterIds.map((chapterId) => {
                  const chapter = findChapterById(chapterId);
                  if (!chapter) {
                    return null;
                  }

                  return (
                    <div key={chapter.id} className="card">
                    <div className="row">
                      <strong>{chapter.title}</strong>
                      <Badge value={labelForStatus(chapter.status)} toneValue={chapter.status} />
                    </div>
                      <p className="muted">{chapter.linkedExcerptIds.length} {text.book.linkedExcerptsCount}</p>
                      <div className="badge-row">
                        {chapter.variants.map((variant) => (
                          <span key={`${chapter.id}-${variant}`} className="badge">
                            {labelForStatus(variant)}
                          </span>
                        ))}
                      </div>
                    </div>
                  );
                })}
              </div>
            </article>
          ))}
        </section>
      </div>
    );
  }

  function renderGraphView() {
    return (
      <section className="panel">
        <div className="row">
          <div>
            <h2>{text.graph.title}</h2>
            <p className="muted">{text.graph.description}</p>
          </div>
          <Badge value="ne" />
        </div>
        <div className="graph-wrap" style={{ marginTop: "0.9rem" }}>
          <svg className="graph" viewBox="0 0 600 340" role="img" aria-label={text.graph.ariaLabel}>
            {graphEdges.map(([fromId, toId]) => {
              const from = graphNodes.find((node) => node.id === fromId)!;
              const to = graphNodes.find((node) => node.id === toId)!;
              return <line key={`${fromId}-${toId}`} x1={from.x} y1={from.y} x2={to.x} y2={to.y} />;
            })}
            {graphNodes.map((node) => (
              <g key={node.id}>
                <circle
                  cx={node.x}
                  cy={node.y}
                  r={node.accent ? 34 : 28}
                  className={node.accent ? "accent" : undefined}
                />
                <text x={node.x} y={node.y}>
                  {node.label}
                </text>
              </g>
            ))}
          </svg>
        </div>
      </section>
    );
  }

  function renderActiveView() {
    switch (activeView) {
      case "library":
        return renderLibraryView();
      case "concept":
        return renderConceptDeskView();
      case "writing":
        return renderWritingDeskView();
      case "book":
        return renderBookDeskView();
      case "graph":
        return renderGraphView();
      default:
        return null;
    }
  }

  return (
    <div className="app-shell">
      <aside className="sidebar">
        <div className="brand">
          <h1>{text.brand.title}</h1>
          <p className="muted">
            {text.brand.subtitle}
          </p>
        </div>

        <ProjectSwitcher
          activeProjectId={activeProjectId}
          onCreate={handleCreateProject}
          onDelete={handleDeleteProject}
          onExport={handleExportProject}
          onImportFile={handleImportProject}
          onRename={handleRenameProject}
          onSwitch={handleSwitchProject}
          projectTransferMessage={projectTransferState?.message ?? null}
          projectTransferTone={projectTransferState?.tone ?? "accent"}
          projects={visibleProjects}
        />

        <section className="panel soft">
          <div className="stack">
            <div>
              <strong>{text.sidebar.axiomTitle}</strong>
              <p className="muted">
                pojem -&gt; izsek -&gt; povezava -&gt; konotacija -&gt; antinomija -&gt; poglavje -&gt; različica -&gt; kanon
              </p>
            </div>
            <div className="badge-row">
              <span className="badge accent">{seedSources.length} virov</span>
              <span className="badge accent">{excerpts.length} izsekov</span>
              <span className="badge accent">{countAllMatches(excerpts, activeConcept)} zadetkov</span>
            </div>
          </div>
        </section>

        <nav className="nav" style={{ marginTop: "1rem" }}>
          {navigationItems.map((item) => (
            <button
              key={item.id}
              className={item.id === activeView ? "active" : undefined}
              onClick={() => setActiveView(item.id)}
            >
              {item.label}
              <span className="hint">{item.hint}</span>
            </button>
          ))}
        </nav>
      </aside>

      <main className="workspace">
        <section className="hero">
          <article className="panel">
            <h2>{text.hero.title}</h2>
            <p className="muted">
              {text.hero.description}
            </p>
            <p className="muted" style={{ marginTop: "0.7rem", marginBottom: 0 }}>
              {text.hero.activeProject}: <strong>{activeProjectName}</strong>
            </p>
          </article>
          <article className="panel soft">
            <div className="grid two">
              <div className="metric">
                <span className="muted">{text.hero.activeConcept}</span>
                <strong>{report.normalizedConcept || "ne"}</strong>
              </div>
              <div className="metric">
                <span className="muted">{text.hero.draftStatus}</span>
                <strong>{labelForStatus(draftState)}</strong>
              </div>
            </div>
          </article>
        </section>

        {renderActiveView()}
      </main>
    </div>
  );
}
