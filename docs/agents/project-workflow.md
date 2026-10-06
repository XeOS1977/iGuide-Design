# Afzonderlijke klantopdrachten in Codex

## Start en scheiding

De bureaurepository bevat werkwijze, profielen, tools en synthetische tests.
Maak iedere nieuwe klantopdracht als zelfstandige map buiten deze repository.
Gebruik één project-ID per opdracht, bijvoorbeeld 2026-001-linde-merkidentiteit.
Een afzonderlijk verkocht vervolgtraject krijgt een nieuw ID, ook bij dezelfde klant.
Leg bij de intake de gekozen scope vast; één opdracht mag meerdere modules omvatten.

Maak vanuit de bureaurepository de map met scripts/new_project.py. Geef een nieuwe
bestemming, project-ID, klant en opdracht op. De starter weigert bestaande mappen
en bestemmingen binnen de bureaurepository, een bestaande klantopdracht of een
Git-checkout. Gebruik bij voorkeur:
D:/AI/iGUIDE-Projects/<project-ID>/.

Voeg de nieuwe map daarna toe als apart project in Codex en start daar de hoofdchat.
Een aparte chat binnen de bureaumap scheidt bestanden niet. Agents werken alleen
in hun toegewezen projectmap. Deze werkinstructie is geen technische toegangsmuur:
controleer de feitelijke sessierechten wanneer harde klantisolatie nodig is.

## Mappen

| Map | Inhoud |
| --- | --- |
| 00-project | Briefingaanvullingen, besluiten, goedkeuringen en versie van de bureau-inrichting. |
| 01-input | Ontvangen klantmateriaal, herkomst, licenties en overgenomen merkbaseline. |
| 02-research | Onderzoek, bronnen en strategische merkbrief. |
| 03-brand | Guidelines, merkassets, fonts en dekkingsmatrix in bewerking. |
| 04-design | Werkbestanden, prototypes en templates per uiting. |
| 05-review | Bevindingen en hercontroles gekoppeld aan concrete bestanden/versies. |
| 06-delivery | Uitsluitend afzonderlijke opleverpakketten met versienummer. |
| 07-archive | Vervangen concepten en gesloten werkversies. |

PROJECT.md identificeert klant, opdracht, scope, status, tracker en remote.
De starter kopieert het handboek, deze instructie, de zes profielen en de UI/UX-skill.
studio-baseline.json legt hashes van de gekopieerde bureau-inrichting vast.
Dit is een vaste kopie: latere bureauwijzigingen veranderen lopende opdrachten niet.
Werk die alleen bewust bij en registreer gevolgen en nieuw versiebewijs.

## Voortbouwen op eerder merkwerk

Neem uitsluitend expliciet aangewezen, goedgekeurde bestanden uit een eerdere
oplevering over naar 01-input. Registreer bronproject, release, herkomst en rechten.
Lees geen andere klantmappen als algemene context. Een wijziging van een oudere
merkidentiteit gebeurt in de nieuwe opdracht en krijgt een eigen release;
pas nooit stilzwijgend een vorige oplevering aan.

## Review en vrijgave

1. Controleer deliverables tegen PROJECT.md en, waar relevant, de dekkingsmatrix.
2. Laat een aparte reviewer de concrete resultaatversie beoordelen.
3. Leg Pauls akkoord op die versie vast in 00-project/approvals.md.
4. Maak een nieuwe map 06-delivery/v001 (of het volgende vrije versienummer).
5. Neem alleen overeengekomen bestanden op, plus LEESMIJ, bestandsindex,
   licenties, versiegegevens, gebruiksinstructies en bekende beperkingen.
6. Controleer het pakket opnieuw op volledigheid, leesbaarheid en klantvreemde
   of interne inhoud. Elke wijziging na akkoord vraagt beoordeling van die wijziging.
7. Paul verzorgt verzending. Registreer wat wanneer is opgeleverd. Behoud de versie.

Ruwe input, interne reviews, offertes, agentconfiguratie en andere klantinformatie
gaan alleen mee als dat specifiek is afgesproken. ZIP nooit de gehele projectmap.

## Versiebeheer en GitHub

De starter initialiseert of publiceert geen repository. Leg opslag/back-up en een
eventuele eigen private remote vast voordat klantwerk afhankelijk wordt van Git.
Een private repository en .gitignore vervangen geen controle van de inhoud.
Gebruik de bureaurepository niet als standaardtracker voor vertrouwelijke klantdata.
Stel per opdracht de toegestane tracker vast; tot die tijd blijven concepten lokaal.

## Voorbeeld startopdracht aan Codex

"Start een afzonderlijk project voor klant Linde, opdracht merkidentiteit,
project-ID 2026-001-linde-merkidentiteit. Gebruik de projectstarter."

Als de map buiten de huidige schrijfgrenzen ligt, doorloop de normale
toestemmingsprocedure. Voeg geen andere klantmappen aan de sessie toe.
