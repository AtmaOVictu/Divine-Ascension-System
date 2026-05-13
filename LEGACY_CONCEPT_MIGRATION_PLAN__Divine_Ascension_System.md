# LEGACY_CONCEPT_MIGRATION_PLAN__Divine_Ascension_System

## STATUS
- Selektivni konceptni plan
- Vir: LEGACY_IMPORT__Divine_Ascension_System.md
- Migracija kode: NE
- Namen: prevod starih konceptov v JEWIK jezik

## SAMOSTOJEČE JEDRO
Stari sistem ne prinaša kode za prenos, ampak zgodnje koncepte, ki jih je treba prevesti v JEWIK: stanja, sled, prag, resnica. Vrednost je v prevodu, ne v kopiranju.

## KONCEPTNI PREVOD

### Ego / Jaz / Enotnost
- Izvorni pomen v Divine-Ascension-System:
  tri osnovna stanja razreda `Agent`, po katerih se subjekt premika glede na napetost in čustveno intenziteto.
- JEWIK prevod:
  zgodnji predhodnik stanj ali položajev smisla, ne pa neposreden RES model ali JEWIK statusni sistem.
- Kaj se sme uporabiti:
  kot arhivska sled, da je sistem že zgodaj mislil stanje subjekta kot prehodno in ne statično.
- Kaj se ne sme prenesti:
  imena stanj kot neposredni enum za JEWIK podatkovno jedro ali proof plast.
- Prihodnja faza:
  Faza C.1 — podatkovno jedro KNJIŽNICE, samo kot ozadje pri opredelitvi pojmovnih ali interpretativnih plasti.

### history
- Izvorni pomen v Divine-Ascension-System:
  preprost seznam preteklih stanj v objektu `Agent`.
- JEWIK prevod:
  zgodnji predhodnik arhivske sledi, časovne sledi ali zapisane spremembe stanja.
- Kaj se sme uporabiti:
  kot koncept, da pomembna sprememba pusti sled.
- Kaj se ne sme prenesti:
  isti objektni vzorec `history = [state]` kot implementacijski mehanizem za JEWIK arhiv.
- Prihodnja faza:
  arhivska sled in version log, ko bo KNJIŽNICA dobila resno časovno in dokazno plast.

### transition thresholds
- Izvorni pomen v Divine-Ascension-System:
  pragova `tension > 0.7` ali `emotion > 0.5`, ki sprožita prehod stanja.
- JEWIK prevod:
  zgodnji predhodnik minimalne validacijske ali proof/check logike, kjer se status spremeni šele ob jasnem pogoju.
- Kaj se sme uporabiti:
  ideja, da mora prehod imeti determinističen, preverljiv prag.
- Kaj se ne sme prenesti:
  konkretna numerična praga, `tension`, `emotion` ali ista metafizika prehoda.
- Prihodnja faza:
  proof/check logika za statuse, kjer bo pomembno, da prehod ne temelji na megli, ampak na pogojih.

### “Kaj je resnica?”
- Izvorni pomen v Divine-Ascension-System:
  hardcode-ano vprašanje v `dialogue.py`, prek katerega sistem pokaže različne odgovore glede na stanje.
- JEWIK prevod:
  zgodnji motiv truth/proof osi in vprašanja, kako pojem, zapis ali stanje artikulira resnico.
- Kaj se sme uporabiti:
  kot rodoslovni motiv in dokumentacijska os za poznejše razločevanje med trditvijo, pomenom, dokazom in razlago.
- Kaj se ne sme prenesti:
  isti dialog kot JEWIK domenska logika ali kot UI besedilo.
- Prihodnja faza:
  SLOVAR, proof in razlagalna dokumentacija, ne pa trenutni runtime model.

### Agent
- Izvorni pomen v Divine-Ascension-System:
  en sam razred, ki nosi stanje, napetost, čustvo, zgodovino in odgovor.
- JEWIK prevod:
  arhivski signal, da je bil zgodnji sistem mišljen kot nosilec stanj in prehodov, ne pa kot uporaben razred za današnji projekt.
- Kaj se sme uporabiti:
  samo kot zgodovinski znak, da se je sistem najprej organiziral okoli “nosilca stanja”.
- Kaj se ne sme prenesti:
  `Agent` kot implementacijski razred, osrednja domena ali nova os sedanjega projekta.
- Prihodnja faza:
  nobena neposredna implementacijska faza; ostaja arhivski pojem, dokler agentna pomoč ne dobi ločenega, jasno omejenega pomena.

## NEPRENOSLJIVO
- `divine_agents/agent.py` kot koda
- `divine_agents/dialogue.py` kot domenska logika
- stari YAML workflowi
- prazen notebook
- Divine Ascension framing kot operativni model

## UPORABNO ZA PRIHODNJE FAZE
- Dokumentacija:
  opis zgodnje ontološke osi, vprašanja resnice in ideje, da prehod pušča sled.
- Podatkovni model:
  samo kot opozorilo, da bo treba ločiti stanje, sled, dokaz in razlago; ne kot vir za shemo.
- Proof/check logika:
  navdih za majhne deterministične teste prehoda, brez prenosa starih pragov ali izrazov.
- Arhivska sled:
  ideja, da pomembna sprememba ostane zapisana.
- UI tekst / razlaga:
  samo kot ozadje za kasnejšo razlago pojmov, ne kot neposredni copy ali naslovje.

## IMPLEMENTACIJSKA MEJA
Ta dokument ne uvaja nobene nove entitete, nobene nove sheme, nobene nove funkcije in nobenega UI elementa.

## NEXT STEP
Faza C.1 — podatkovno jedro KNJIŽNICE.

Utemeljitev:
Konceptni prevod je smiseln šele, če dobi ciljno podatkovno jedro, kamor se lahko kasneje vežejo SLOVAR, viri, izseki in fragmente. Faza B.3 je že zaključena kot operativni backup protokol, zato bi bila ponovitev manj smiselna od naslednjega strukturnega koraka. Stari legacy koncepti nimajo vrednosti brez jasnega cilja v modelu. Zato je naslednji pravi korak opredelitev prvih nosilnih entitet KNJIŽNICE.
