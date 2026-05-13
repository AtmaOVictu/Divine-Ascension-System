export type UiLanguage = "sl" | "en";

type UiText = {
  brand: {
    title: string;
    subtitle: string;
  };
  navigation: {
    library: string;
    dictionary: string;
    writingDesk: string;
    book: string;
    conceptGraph: string;
  };
  navigationHints: {
    library: string;
    dictionary: string;
    writingDesk: string;
    book: string;
    conceptGraph: string;
  };
  hero: {
    title: string;
    description: string;
    activeProject: string;
    activeConcept: string;
    draftStatus: string;
    defaultProject: string;
  };
  projectSwitcher: {
    activeProject: string;
    noProject: string;
    renameProject: string;
    saveProjectName: string;
    cancel: string;
    loaded: string;
    switchProject: string;
    rename: string;
    confirmDelete: string;
    delete: string;
    newProject: string;
    newProjectPlaceholder: string;
    createProject: string;
    exportProject: string;
    importProject: string;
    projectTransfer: string;
    success: string;
    error: string;
    warning: string;
    info: string;
  };
  sidebar: {
    axiomTitle: string;
  };
  conceptDesk: {
    title: string;
    flow: string;
    inputLabel: string;
    inputPlaceholder: string;
    analyze: string;
    semanticReport: string;
    relatedConcepts: string;
    connotations: string;
    antinomies: string;
    chapterProposal: string;
    notEnoughForChapter: string;
    canonCandidates: string;
    noCanonCandidates: string;
    excerptsWithSource: string;
    emptyConcept: string;
  };
  writingDesk: {
    title: string;
    description: string;
    chapterTitle: string;
    chapterBody: string;
    addExcerpt: string;
    linkConcept: string;
    saveVersion: string;
    linkedExcerpts: string;
  };
  book: {
    title: string;
    description: string;
    compareVersions: string;
    compareVersionsNextStep: string;
    linkedExcerptsCount: string;
  };
  graph: {
    title: string;
    description: string;
    ariaLabel: string;
  };
  transfer: {
    exportUnavailableProject: string;
    exportPackageFailed: string;
    exportSuccess: (projectName: string) => string;
    exportBrowserFailed: string;
    importInvalidJson: string;
    importInvalidPackageType: string;
    importUnsupportedVersion: string;
    importInvalidProject: string;
    importInvalidWorkspace: string;
    importInvalidExportedAt: string;
    importInvalidPackage: string;
    importProjectCreateFailed: string;
    importWorkspacePersistFailed: string;
    importActivationFailed: string;
    importSuccess: (projectName: string) => string;
    importReadFailed: string;
  };
  statusLabels: Record<string, string>;
  sourceKindLabels: Record<string, string>;
};

export const uiText: Record<UiLanguage, UiText> = {
  sl: {
    brand: {
      title: "JEWIK KNJIŽNICA",
      subtitle: "Namenska lokalna knjižnica za pisanje, pomen, konotacije, poglavja, različice in kanon.",
    },
    navigation: {
      library: "Knjižnica",
      dictionary: "SLOVAR",
      writingDesk: "Pisalna miza",
      book: "Knjiga",
      conceptGraph: "Mreža pojma",
    },
    navigationHints: {
      library: "viri in izseki",
      dictionary: "pojem in konotacije",
      writingDesk: "poglavja in različica",
      book: "knjiga in struktura",
      conceptGraph: "mreža povezav",
    },
    hero: {
      title: "Prva stabilna delovna površina",
      description: "Ta različica ostaja brskalniško varna React/Vite plast brez posegov v Tauri, z ločenim podatkovnim jedrom in semenskimi podatki za \"Beseda je Ne\".",
      activeProject: "Aktivni projekt",
      activeConcept: "Pojem v delu",
      draftStatus: "Stanje zapisa",
      defaultProject: "Privzeti projekt",
    },
    projectSwitcher: {
      activeProject: "Aktivni projekt",
      noProject: "Brez projekta",
      renameProject: "Novo ime projekta",
      saveProjectName: "Shrani ime",
      cancel: "Prekliči",
      loaded: "Naložen",
      switchProject: "Preklopi",
      rename: "Preimenuj",
      confirmDelete: "Potrdi izbris",
      delete: "Izbriši",
      newProject: "Nov projekt",
      newProjectPlaceholder: "Vnesi ime projekta",
      createProject: "Ustvari projekt",
      exportProject: "Izvozi projekt",
      importProject: "Uvozi projekt",
      projectTransfer: "Prenos projekta",
      success: "uspeh",
      error: "napaka",
      warning: "opozorilo",
      info: "info",
    },
    sidebar: {
      axiomTitle: "Glavni aksiom",
    },
    conceptDesk: {
      title: "SLOVAR",
      flow: "Pojem -> izsek -> povezava -> konotacija -> antinomija -> poglavje.",
      inputLabel: "Vnesi pojem ...",
      inputPlaceholder: "npr. ne",
      analyze: "Analiziraj",
      semanticReport: "Semantično poročilo",
      relatedConcepts: "Povezani pojmi",
      connotations: "Konotacije",
      antinomies: "Antinomije",
      chapterProposal: "Predlog poglavja",
      notEnoughForChapter: "Za ta pojem še ni dovolj gradiva za poglavje.",
      canonCandidates: "Kandidati za kanon",
      noCanonCandidates: "Brez izsekov ni kandidatov za kanon.",
      excerptsWithSource: "Izseki z izvorom",
      emptyConcept: "prazen",
    },
    writingDesk: {
      title: "Pisalna miza",
      description: "Lokalni osnutek ostaja v React state/localStorage, brez pisanja v datoteke.",
      chapterTitle: "Naslov poglavja",
      chapterBody: "Besedilo poglavja",
      addExcerpt: "Dodaj izsek",
      linkConcept: "Poveži pojem",
      saveVersion: "Shrani različico",
      linkedExcerpts: "Povezani izseki",
    },
    book: {
      title: "Knjiga",
      description: "Struktura knjige, poglavja, statusi in različice.",
      compareVersions: "Primerjaj različice",
      compareVersionsNextStep: "Primerjava različic bo naslednji najmanjši funkcionalni korak.",
      linkedExcerptsCount: "povezanih izsekov",
    },
    graph: {
      title: "Mreža pojma",
      description: "Vizualni prikaz osnovne pojmovne mreže okoli pojma ne.",
      ariaLabel: "Mreža pojma ne",
    },
    transfer: {
      exportUnavailableProject: "Aktivnega projekta ni mogoče izvoziti.",
      exportPackageFailed: "Paket projekta ni bilo mogoče pripraviti za izvoz.",
      exportSuccess: (projectName) => `Projekt \"${projectName}\" je izvožen kot ProjectPackage JSON.`,
      exportBrowserFailed: "Izvoz projekta ni uspel v trenutnem brskalniškem okolju.",
      importInvalidJson: "Izbrana datoteka ni veljaven JSON paket projekta.",
      importInvalidPackageType: "Izbrana datoteka ni veljaven JEWIK paket projekta.",
      importUnsupportedVersion: "Paket projekta uporablja nepodprto verzijo.",
      importInvalidProject: "Paket projekta nima veljavnega imena projekta.",
      importInvalidWorkspace: "Paket projekta nima veljavnega workspace stanja.",
      importInvalidExportedAt: "Paket projekta nima veljavnega časa izvoza.",
      importInvalidPackage: "Paket projekta je napačno oblikovan.",
      importProjectCreateFailed: "Novega projekta ni bilo mogoče varno ustvariti.",
      importWorkspacePersistFailed: "Uvoženega workspace stanja ni bilo mogoče varno zapisati.",
      importActivationFailed: "Uvoženega projekta ni bilo mogoče varno aktivirati.",
      importSuccess: (projectName) => `Projekt \"${projectName}\" je uspešno uvožen.`,
      importReadFailed: "Datoteke projekta ni bilo mogoče prebrati ali uvoziti.",
    },
    statusLabels: {
      NEW: "NOVO",
      INDEXED: "INDEKSIRANO",
      USED: "UPORABLJENO",
      PARKED: "ODLOŽENO",
      RELEVANT: "POMEMBNO",
      REJECTED: "ZAVRNJENO",
      CANON_CANDIDATE: "KANDIDAT ZA KANON",
      IDEA: "ZASNOVA",
      DRAFT: "OSNUTEK",
      REVIEW: "PREGLED",
      CANON: "KANON",
      RAW: "SUROVO",
      CLEAN: "ČISTOPIS",
      BOOK: "KNJIŽNO",
      SYSTEM: "SISTEMSKO",
      READER: "BRALNO",
      shranjeno: "SHRANJENO",
      nespremenjeno: "NESPREMENJENO",
      osnutek: "OSNUTEK",
    },
    sourceKindLabels: {
      markdown: "Markdown",
      txt: "TXT",
      docx: "DOCX",
      pdf: "PDF",
      unknown: "Neznano",
    },
  },
  en: {
    brand: {
      title: "JEWIK LIBRARY",
      subtitle: "Purpose-built local library for writing, meaning, connotations, chapters, variants, and canon.",
    },
    navigation: {
      library: "Library",
      dictionary: "DICTIONARY",
      writingDesk: "Writing Desk",
      book: "Book",
      conceptGraph: "Concept Graph",
    },
    navigationHints: {
      library: "sources and excerpts",
      dictionary: "concept and connotations",
      writingDesk: "chapters and variant",
      book: "book and structure",
      conceptGraph: "network of relations",
    },
    hero: {
      title: "First Stable Workspace",
      description: "This version remains a browser-safe React/Vite layer without Tauri changes, with a separate data core and seed data for \"Beseda je Ne\".",
      activeProject: "Active project",
      activeConcept: "Working concept",
      draftStatus: "Draft status",
      defaultProject: "Default project",
    },
    projectSwitcher: {
      activeProject: "Active project",
      noProject: "No project",
      renameProject: "New project name",
      saveProjectName: "Save name",
      cancel: "Cancel",
      loaded: "Loaded",
      switchProject: "Switch",
      rename: "Rename",
      confirmDelete: "Confirm delete",
      delete: "Delete",
      newProject: "New project",
      newProjectPlaceholder: "Enter project name",
      createProject: "Create project",
      exportProject: "Export project",
      importProject: "Import project",
      projectTransfer: "Project transfer",
      success: "success",
      error: "error",
      warning: "warning",
      info: "info",
    },
    sidebar: {
      axiomTitle: "Core axiom",
    },
    conceptDesk: {
      title: "DICTIONARY",
      flow: "Concept -> excerpt -> relation -> connotation -> antinomy -> chapter.",
      inputLabel: "Enter concept ...",
      inputPlaceholder: "e.g. ne",
      analyze: "Analyze",
      semanticReport: "Semantic report",
      relatedConcepts: "Related concepts",
      connotations: "Connotations",
      antinomies: "Antinomies",
      chapterProposal: "Chapter proposal",
      notEnoughForChapter: "There is not enough material yet for a chapter.",
      canonCandidates: "Canon candidates",
      noCanonCandidates: "Without excerpts there are no canon candidates.",
      excerptsWithSource: "Excerpts with source",
      emptyConcept: "empty",
    },
    writingDesk: {
      title: "Writing Desk",
      description: "The local draft remains in React state/localStorage, without writing to files.",
      chapterTitle: "Chapter title",
      chapterBody: "Chapter text",
      addExcerpt: "Add excerpt",
      linkConcept: "Link concept",
      saveVersion: "Save variant",
      linkedExcerpts: "Linked excerpts",
    },
    book: {
      title: "Book",
      description: "Book structure, chapters, statuses, and variants.",
      compareVersions: "Compare variants",
      compareVersionsNextStep: "Variant comparison is the next smallest functional step.",
      linkedExcerptsCount: "linked excerpts",
    },
    graph: {
      title: "Concept Graph",
      description: "Visual sketch of the base concept network around ne.",
      ariaLabel: "Concept graph for ne",
    },
    transfer: {
      exportUnavailableProject: "The active project cannot be exported.",
      exportPackageFailed: "The project package could not be prepared for export.",
      exportSuccess: (projectName) => `Project \"${projectName}\" was exported as ProjectPackage JSON.`,
      exportBrowserFailed: "Project export failed in the current browser environment.",
      importInvalidJson: "The selected file is not valid project package JSON.",
      importInvalidPackageType: "The selected file is not a valid JEWIK project package.",
      importUnsupportedVersion: "The project package version is not supported.",
      importInvalidProject: "The project package does not contain a valid project name.",
      importInvalidWorkspace: "The project package does not contain a valid workspace state.",
      importInvalidExportedAt: "The project package does not contain a valid export time.",
      importInvalidPackage: "The project package is malformed.",
      importProjectCreateFailed: "The new project could not be created safely.",
      importWorkspacePersistFailed: "The imported workspace state could not be written safely.",
      importActivationFailed: "The imported project could not be activated safely.",
      importSuccess: (projectName) => `Project \"${projectName}\" was imported successfully.`,
      importReadFailed: "The project file could not be read or imported.",
    },
    statusLabels: {
      NEW: "NEW",
      INDEXED: "INDEXED",
      USED: "USED",
      PARKED: "PARKED",
      RELEVANT: "RELEVANT",
      REJECTED: "REJECTED",
      CANON_CANDIDATE: "CANON CANDIDATE",
      IDEA: "IDEA",
      DRAFT: "DRAFT",
      REVIEW: "REVIEW",
      CANON: "CANON",
      RAW: "RAW",
      CLEAN: "CLEAN",
      BOOK: "BOOK",
      SYSTEM: "SYSTEM",
      READER: "READER",
      shranjeno: "SAVED",
      nespremenjeno: "UNCHANGED",
      osnutek: "DRAFT",
    },
    sourceKindLabels: {
      markdown: "Markdown",
      txt: "TXT",
      docx: "DOCX",
      pdf: "PDF",
      unknown: "Unknown",
    },
  },
};

export function getUiText(language: UiLanguage = "sl"): UiText {
  return uiText[language];
}
