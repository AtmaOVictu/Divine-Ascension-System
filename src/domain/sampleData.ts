import type { StudioState } from "./types";
import { stamp } from "./types";

export function createEmptyState(): StudioState {
  return {
    documents: [],
    truthUnits: [],
    evidenceRefs: [],
    definitions: [],
    counterAngles: [],
    links: [],
    simulationCases: [],
  };
}

export function createSampleState(): StudioState {
  const now = stamp();
  const documentId = "doc-truthbase-root";
  const unitIds = {
    wordAct: "unit-word-act",
    definitionNeed: "unit-definition-need",
    gravity: "unit-gravity",
    personalTruth: "unit-personal-truth",
    contradiction: "unit-contradiction",
  };

  return {
    documents: [
      {
        id: documentId,
        title: "JEWIK delovni zapis o resnici, definiciji in soglasju",
        filename: "jewik-delovni-zapis.txt",
        content:
          "Beseda ni samo opis, ampak dejanje. Resnica potrebuje definicijo uporabljenih besed, sicer test ni čist. Gravitacija je univerzalno testabilna trditev znotraj določenega modela. Osebna resnica je veljavna kot izkušnja, vendar ne nujno kot univerzalna trditev. Kontradikcija ni nujno napaka; lahko je signal razlike med okviri.",
        createdAt: now,
        updatedAt: now,
      },
    ],
    truthUnits: [
      {
        id: unitIds.wordAct,
        documentId,
        type: "AKSIOM_APD",
        status: "CANDIDATE",
        consentStatus: "EMPTY",
        title: "Beseda kot dejanje",
        claim: "Beseda ni samo opis, ampak dejanje.",
        keyDefinitions: ["beseda", "dejanje"],
        evidenceFromDocument: [
          "Iz dokumenta izhaja, da izjava o besedi govori o učinku in ne le o opisu.",
        ],
        counterAngle:
          "Če izjava nima jasnega konteksta ali naslovnika, je lahko njena dejanska moč omejena.",
        proposedLinks: [
          "Poveži z definicijo pojma resnica, ker brez natančnih pojmov aksiom ostane odprt.",
        ],
        notes: "Za kanonizacijo je smiselno ločiti performativni govor od opisa stanja.",
        createdAt: now,
        updatedAt: now,
      },
      {
        id: unitIds.definitionNeed,
        documentId,
        type: "DEFINICIJA",
        status: "NEEDS_DEFINITION",
        consentStatus: "POPRAVI",
        title: "Definicija pred testom",
        claim: "Resnica potrebuje definicijo uporabljenih besed.",
        keyDefinitions: ["resnica", "definicija"],
        evidenceFromDocument: [
          "Dokument izrecno poveže čistost testa z natančnostjo pojmov.",
        ],
        counterAngle:
          "V nekaterih praksah delovni konsenz zadostuje tudi brez popolne definicijske zaprtosti.",
        proposedLinks: [
          "Poveži z gravitacijo kot primerom, kjer model določa pomen trditve.",
        ],
        notes: "Potrebna je omejitev obsega: katere besede so obvezne za definicijo in katere ne.",
        createdAt: now,
        updatedAt: now,
      },
      {
        id: unitIds.gravity,
        documentId,
        type: "UNIVERZALNO_TESTABILNA_RESNICA",
        status: "TESTABLE",
        consentStatus: "DA",
        title: "Gravitacija znotraj modela",
        claim: "Gravitacija je univerzalno testabilna trditev znotraj določenega modela.",
        keyDefinitions: ["gravitacija", "model"],
        evidenceFromDocument: [
          "Formulacija izrecno zameji testabilnost z modelom in s tem prepreči absolutizacijo.",
        ],
        counterAngle:
          "Če se model zamenja, se lahko spremeni tudi interpretacija meritev in napovedi.",
        proposedLinks: [
          "Poveži z metodo testiranja in z definicijo resnice kot modelno vezane trditve.",
        ],
        notes: "Dober primer ločevanja med dokazno potjo in metafizično absolutnostjo.",
        createdAt: now,
        updatedAt: now,
      },
      {
        id: unitIds.personalTruth,
        documentId,
        type: "OSEBNA_RESNICA",
        status: "CANDIDATE",
        consentStatus: "EMPTY",
        title: "Osebna resnica kot izkušnja",
        claim:
          "Osebna resnica je veljavna kot izkušnja, vendar ne nujno kot univerzalna trditev.",
        keyDefinitions: ["osebna resnica", "izkušnja", "univerzalna trditev"],
        evidenceFromDocument: [
          "Dokument loči veljavnost osebne izkušnje od veljavnosti univerzalne izjave.",
        ],
        counterAngle:
          "Nekatere osebne izkušnje lahko postanejo empirične hipoteze, če so operacionalizirane.",
        proposedLinks: [
          "Poveži s kontradikcijo, ker različni okviri lahko proizvedejo različne osebne resnice.",
        ],
        notes: "Treba je paziti, da osebne resnice ne degradiramo v nepomembnost.",
        createdAt: now,
        updatedAt: now,
      },
      {
        id: unitIds.contradiction,
        documentId,
        type: "KONTRADIKCIJA",
        status: "READY_FOR_MY_CONSENT",
        consentStatus: "EMPTY",
        title: "Kontradikcija kot signal okvirja",
        claim:
          "Kontradikcija ni nujno napaka; lahko je signal razlike med okviri.",
        keyDefinitions: ["kontradikcija", "okvir"],
        evidenceFromDocument: [
          "Besedilo kontradikcijo preusmeri iz napake v diagnostični signal.",
        ],
        counterAngle:
          "V formalnih sistemih je kontradikcija še vedno lahko kritična napaka, če uniči doslednost sklepanja.",
        proposedLinks: [
          "Poveži z osebno resnico in z definicijo, ker se spor pogosto začne v različnih okvirih pomena.",
        ],
        notes: "To je kandidat za osebni kanon, ko uporabnik presodi meje uporabe.",
        createdAt: now,
        updatedAt: now,
      },
    ],
    evidenceRefs: [
      {
        id: "evidence-word-act",
        truthUnitId: unitIds.wordAct,
        quote: "Beseda ni samo opis, ampak dejanje.",
        sourceLocation: "odstavek 1",
        confidence: 0.88,
      },
      {
        id: "evidence-definition-need",
        truthUnitId: unitIds.definitionNeed,
        quote: "Resnica potrebuje definicijo uporabljenih besed, sicer test ni čist.",
        sourceLocation: "odstavek 1",
        confidence: 0.91,
      },
      {
        id: "evidence-gravity",
        truthUnitId: unitIds.gravity,
        quote: "Gravitacija je univerzalno testabilna trditev znotraj določenega modela.",
        sourceLocation: "odstavek 1",
        confidence: 0.93,
      },
      {
        id: "evidence-personal-truth",
        truthUnitId: unitIds.personalTruth,
        quote:
          "Osebna resnica je veljavna kot izkušnja, vendar ne nujno kot univerzalna trditev.",
        sourceLocation: "odstavek 1",
        confidence: 0.86,
      },
      {
        id: "evidence-contradiction",
        truthUnitId: unitIds.contradiction,
        quote:
          "Kontradikcija ni nujno napaka; lahko je signal razlike med okviri.",
        sourceLocation: "odstavek 1",
        confidence: 0.89,
      },
    ],
    definitions: [
      {
        id: "definition-beseda",
        term: "beseda",
        definition: "Nosilec pomena, ki lahko poleg opisa izvede tudi odnos ali odločitev.",
        scope: "jezikovno dejanje",
        linkedUnitIds: [unitIds.wordAct],
      },
      {
        id: "definition-resnica",
        term: "resnica",
        definition:
          "Trditev ali okvir, ki ga uporabnik lahko preverja, popravlja, zavrne ali kanonizira.",
        scope: "delovni studio",
        linkedUnitIds: [unitIds.definitionNeed, unitIds.gravity, unitIds.personalTruth],
      },
      {
        id: "definition-definicija",
        term: "definicija",
        definition: "Dogovor o pomenu izraza z jasno mejo uporabe.",
        scope: "pojmovni nivo",
        linkedUnitIds: [unitIds.definitionNeed],
      },
      {
        id: "definition-gravitacija",
        term: "gravitacija",
        definition: "Primer modelno testabilne trditve, kjer meritev potrebuje okvir razlage.",
        scope: "empirični model",
        linkedUnitIds: [unitIds.gravity],
      },
      {
        id: "definition-okvir",
        term: "okvir",
        definition: "Sistem predpostavk, znotraj katerega dobijo izrazi in meritve pomen.",
        scope: "meta raven",
        linkedUnitIds: [unitIds.contradiction, unitIds.personalTruth],
      },
    ],
    counterAngles: [
      {
        id: "counter-word-act",
        truthUnitId: unitIds.wordAct,
        description:
          "Performativnost besede je odvisna od moči govorca, konteksta in sprejema pri naslovniku.",
        severity: "srednja",
      },
      {
        id: "counter-gravity",
        truthUnitId: unitIds.gravity,
        description:
          "Univerzalnost v praksi pomeni ponovljivost znotraj modela, ne absolutne metafizične popolnosti.",
        severity: "nizka",
      },
      {
        id: "counter-contradiction",
        truthUnitId: unitIds.contradiction,
        description:
          "Če kontradikcije ne omejimo z okvirjem, lahko razbije sklepanje namesto da ga razjasni.",
        severity: "visoka",
      },
    ],
    links: [
      {
        id: "link-definition-word",
        fromUnitId: unitIds.definitionNeed,
        toUnitId: unitIds.wordAct,
        relationType: "DEFINES",
        note: "Definicija besed določa, kako beremo aksiom o besedi kot dejanju.",
      },
      {
        id: "link-gravity-definition",
        fromUnitId: unitIds.gravity,
        toUnitId: unitIds.definitionNeed,
        relationType: "TESTS",
        note: "Model gravitacije je primer, kjer definicije pogojujejo testabilnost.",
      },
      {
        id: "link-personal-contradiction",
        fromUnitId: unitIds.personalTruth,
        toUnitId: unitIds.contradiction,
        relationType: "SUPPORTS",
        note: "Različne osebne izkušnje lahko pojasnijo izvor kontradikcije med okviri.",
      },
      {
        id: "link-contradiction-definition",
        fromUnitId: unitIds.contradiction,
        toUnitId: unitIds.definitionNeed,
        relationType: "REFINES",
        note: "Ko se okviri ločijo, postane definicijski spor viden in popravljiv.",
      },
      {
        id: "link-word-personal",
        fromUnitId: unitIds.wordAct,
        toUnitId: unitIds.personalTruth,
        relationType: "SYMBOLICALLY_LINKED",
        note: "Beseda kot dejanje vpliva na to, kako posameznik artikulira lastno resnico.",
      },
    ],
    simulationCases: [
      {
        id: "simulation-candidate-to-canon",
        title: "Prehod od kandidata do kanona",
        description:
          "Simulacija pokaže, kako ista trditev prehaja skozi definicijsko in dokazno disciplino, preden jo uporabnik kanonizira.",
        involvedUnitIds: [unitIds.wordAct, unitIds.definitionNeed, unitIds.contradiction],
        steps: [
          {
            status: "CANDIDATE",
            note: "Trditev je vnesena iz dokumenta kot kandidat in še nima osebnega soglasja.",
          },
          {
            status: "NEEDS_DEFINITION",
            note: "Pojmi se razčistijo, da uporabnik razume natančen obseg besed.",
          },
          {
            status: "TESTABLE",
            note: "Preveri se, kaj v trditvi je testabilno in kaj ostane simbolna ali osebna raven.",
          },
          {
            status: "READY_FOR_MY_CONSENT",
            note: "Dokazna pot in proti-kot sta dovolj jasna, da sledi osebna presoja.",
          },
          {
            status: "CANON",
            note: "Kanon nastane šele, ko ga uporabnik izrecno potrdi, ne avtomatsko.",
          },
        ],
      },
    ],
  };
}
