# REPLAY / BACKUP PROTOKOL — JEWIK KNJIŽNICA

## 1. Namen protokola

Ta protokol določa ročni postopek, po katerem uporabnik preveri, ali projekt v aplikaciji JEWIK KNJIŽNICA ostaja stabilen skozi osvežitev strani, preklop med projekti, izvoz, uvoz in obnovo.

Protokol se izvede:

- pred resnejšim dnevnim delom,
- po pomembnejših spremembah v project storage ali import/export toku,
- pred uporabo starejših ali tujih paketov,
- pred ročnim arhiviranjem pomembnih projektov.

Protokol obstaja zato, da potrdi:

- da projekt ostane vezan na svoj delovni prostor,
- da izvoz ustvari varnostno kopijo zunaj aplikacije,
- da uvoz vedno ustvari nov projekt in ne prepiše obstoječega,
- da neveljaven paket ne poškoduje stanja aplikacije.

## 2. Stopnje varnosti uporabe

- Razvojna uporaba:
  primerna za lokalno preverjanje funkcij, proofa in builda.
- Dnevno delo z ročnim backupom:
  primerno po Fazi B.2 in tem protokolu B.3, če uporabnik pred in po večjih spremembah izvozi projekt.
- Resna knjižnična uporaba po podatkovnem modelu:
  primerna šele po uvedbi KNJIŽNICA podatkovnega jedra za SLOVAR, vire, izseke, fragmente in povezave.
- Prihodnja namizna uporaba:
  primerna šele po desktop/local file storage fazi, ko bo aplikacija vezana na lokalne datoteke ali lokalno bazo.

## 3. Predpogoji

Pred ročnim replay testom zaženi:

```bash
corepack pnpm proof
corepack pnpm build
corepack pnpm dev
```

Nato:

- odpri aplikacijo v browserju,
- preveri, da je prikazan slovenski UI JEWIK KNJIŽNICA,
- preveri, da sta gumba `Izvozi projekt` in `Uvozi projekt` dosegljiva v levem sidebarju.

## 4. Osnovni replay test

Koraki:

1. Odpri aplikacijo.
2. Ustvari projekt A.
3. V projekt A vpiši prepoznavno vsebino.
4. Osveži stran.
5. Preveri, da projekt A in njegova vsebina ostaneta naložena.
6. Ustvari projekt B.
7. V projekt B vpiši drugačno vsebino.
8. Preklopi iz projekta B nazaj na projekt A.
9. Preveri, da se vsebina projekta A pravilno obnovi.
10. Preklopi nazaj na projekt B.
11. Preveri, da se vsebini projektov A in B ne pomešata.

Kaj ta test potrdi:

- project-scoped workspace persistence deluje,
- refresh ne izgubi aktivnega projekta,
- preklop med projekti ne zamenja vsebine med delovnimi prostori.

## 5. Export replay test

Koraki:

1. Izberi projekt A.
2. Klikni `Izvozi projekt`.
3. Shrani JSON datoteko na disk.
4. Preveri, da export ne spremeni aktivnega projekta.
5. Preveri, da export ne spremeni vsebine projekta.
6. Preveri, da je bila ustvarjena JSON datoteka s smiselno obliko imena, na primer:
   `jewik-project-ime-projekta.json`

Kaj ta test potrdi:

- izvoz deluje kot read-only tok,
- ProjectPackage JSON nastane zunaj aplikacije,
- izvoz ne spremeni delovnega stanja projekta.

## 6. Import replay test

Koraki:

1. Preklopi na projekt B.
2. Klikni `Uvozi projekt`.
3. Izberi JSON datoteko, ki je bila izvožena iz projekta A.
4. Preveri, da po uvozu nastane nov projekt.
5. Preveri, da novi projekt vsebuje vsebino projekta A.
6. Preveri, da projekt B ni prepisan.
7. Preveri, da aktivni projekt po uspešnem uvozu postane uvoženi projekt.
8. Če ime projekta že obstaja, preveri, da se uporabi varen suffix, na primer:
   `Ime (import)` ali `Ime (import 2)`.

Kaj ta test potrdi:

- uvoz ne prepisuje obstoječega projekta,
- ProjectPackage JSON se pravilno pretvori v nov projekt,
- podvojeno ime ne poškoduje registryja.

## 7. Invalid import replay test

Koraki:

1. Pripravi neveljaven JSON.
2. Klikni `Uvozi projekt`.
3. Izberi neveljaven JSON.
4. Preveri, da aplikacija pokaže slovensko napako.
5. Preveri, da `activeProjectId` ostane isti kot pred neuspelim uvozom.
6. Preveri, da workspace vsebina ostane ista.
7. Preveri, da project registry ni poškodovan.
8. Osveži stran in preveri, da stanje ostane stabilno.

Kaj ta test potrdi:

- poškodovan ali napačen paket je varno zavrnjen,
- neuspešen uvoz ne spremeni aktivnega projekta,
- neuspešen uvoz ne spremeni vsebine delovnega prostora.

## 8. Dnevna backup disciplina

Priporočena disciplina:

- pred večjim pisanjem izvozi projekt,
- po večjem pisanju izvozi projekt,
- po pomembnem preimenovanju izvozi projekt,
- pred uvozom starega ali tujega paketa izvozi trenutni projekt,
- pred daljšim eksperimentom v SLOVARJU ali pisalnem toku izvozi projekt,
- izvoze hrani zunaj aplikacije v namenski backup mapi.

Minimalno pravilo za dnevno delo:

Po Fazi B.2 in po potrjenem B.3 replay protokolu je aplikacija primerna za dnevno delo z ročnim export backupom.

## 9. Predlagana struktura backup mape

Primer:

```text
JEWIK_BACKUP/
  2026-05-13/
    projekt-ime__pred-pisanjem.json
    projekt-ime__po-pisanju.json
    projekt-ime__po-importu.json
```

Priporočilo:

- uporabi ločeno zunanjo mapo,
- izvoze zloži po datumih,
- v ime datoteke vključi trenutek ali namen izvoza,
- pomembnih JSON paketov ne hrani samo v `Downloads`.

## 10. Pravilo dovoljenja za uporabo

- Do B.2:
  aplikacija je primerna predvsem za testiranje.
- Po B.2 + B.3:
  aplikacija je primerna za dnevno delo z ročnim export backupom.
- Po KNJIŽNICA DATA MODEL:
  aplikacija bo primerna za resnejšo knjižnično uporabo.
- Po desktop/local file storage:
  aplikacija bo primerna kot namizno delovno orodje.
- Po version/archive logu:
  aplikacija bo primerna kot dolgoročni arhivski sistem.

## 11. Kaj protokol ne zagotavlja

- Ne zagotavlja še namizne lokalne datotečne shrambe.
- Ne zagotavlja še SQLite ali drugega lokalnega backend-a.
- Ne zagotavlja še avtomatskega cloud synca.
- Ne nadomešča zunanjega backupa.
- Ne pomeni, da je `localStorage` že končni arhiv.
- Ne pomeni, da je KNJIŽNICA podatkovno jedro že zaključeno.

## 12. Kratek acceptance checklist

- PASS/HOLD: proof zelen
- PASS/HOLD: build zelen
- PASS/HOLD: projekt A preživi refresh
- PASS/HOLD: projekt B ima ločeno vsebino
- PASS/HOLD: export deluje
- PASS/HOLD: import ustvari nov projekt
- PASS/HOLD: invalid import ne spremeni stanja
- PASS/HOLD: backup JSON je shranjen zunaj aplikacije
