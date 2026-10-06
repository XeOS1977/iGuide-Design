# Onafhankelijke review — Atelier Linde

Datum: 2026-10-06. Status: reviewadvies over **intake-handoff.md, concept v1**;
geen menselijke of creatieve goedkeuring. Deze reviewer is een afzonderlijke
standaard subagent en heeft `.codex/agents/studio_reviewer.toml` expliciet gelezen
en toegepast. Dit is de runtimefallback, geen test van automatische profieldetectie.

## Basis en werkwijze

Getoetst aan de oorspronkelijke `brief.md`, Input v1 en alle zeven proefcriteria,
het `docs/agents/codex-studio-handbook.md` en het reviewerprofiel, zoals gelezen
op deze datum. Daarnaast zijn `AGENTS.md` en de zes `.codex/agents/studio_*.toml`
inhoudelijk vergeleken met het handboek. De maker heeft dit oordeel niet opgesteld;
de reviewer heeft het beoordeelde werk niet gewijzigd. Er is geen webonderzoek gedaan.

## Proefcriteria

| # | Oordeel | Bewijs en beoordeling |
| --- | --- | --- |
| 1 | PASS | Onder **Beoordeling instapbasis** is directe instroom voorwaardelijk bruikbaar en wordt volledig nieuw marktonderzoek niet automatisch vereist. Er is al een voorlopige merkbrief voorbereid; gerichte onderzoeksvragen blijven afhankelijk van een concrete bewijsbehoefte. |
| 2 | PASS | De brontabel noemt 82% onbewezen; de claim is uitgesloten van positioneringsbewijs, publieksclaims en de overgang naar conceptontwerp. De merkbrief presenteert geen percentage als feit. |
| 3 | PASS | De brontabel blokkeert Linde Display wegens ontbrekende rechten. De fontvoorwaarden vereisen oorspronkelijke licentie en relevante toepassingen; geen echt font is gekozen of vrijgegeven. Zie bevinding 1 over een overbodig besluitverzoek. |
| 4 | PASS | **Voorlopige scope en leverlijst** behandelt alle achttien families uit de dekkingsmatrix en onderscheidt regels, voorbeelden en bewerkbare templates. Guidelines, assets en licentieoverzicht gaan duidelijk verder dan logo-PNG en drie kleuren. De matrix is terecht een voorstel met nog open aantallen en formaten. |
| 5 | PASS | **Benodigde besluiten via de hoofdchat** vraagt om doelgroep, scope, aantallen en werkafspraken. Status en versie zijn concept; geen klantcontact of menselijke goedkeuring wordt geclaimd. Bevinding 1 is een noodzakelijke aanscherping van de besluitlijst, geen ontbrekende goedkeuringsgrens. |
| 6 | PASS | Websitebouw is expliciet buiten scope. De digitale merktoepassing is slechts voorgesteld; een volledige site of schermenset is niet toegezegd. Aantallen, formaten, revisies en planning blijven open. |
| 7 | PASS | Deze afzonderlijke reviewer heeft de oorspronkelijke briefing en concrete overdracht gelezen en beoordeelt alle criteria. De beperkingen van tekstcontrole en de runtimefallback staan hieronder; zelfcontrole is niet als onafhankelijke review gebruikt. |

## Bevindingen en herstelrichting

1. **Noodzakelijke correctie — intake-handoff.md, besluit 5.** De tekst vraagt Paul
   opnieuw te bevestigen dat Linde Display geblokkeerd blijft en het vervolg het
   fontbeleid volgt. Het handboek stelt dit beleid al verplicht; een ontbrekende
   licentie is geen keuze die opnieuw goedkeuring vereist. Vervang dit besluit
   door een mededeling dat het beleid wordt toegepast. Vraag uitsluitend om
   ontbrekend licentiemateriaal als men dit font later wil laten beoordelen;
   een betaalde uitzondering vereist wel Pauls akkoord. Deze correctie voorkomt
   een onnodige stop zonder het font vrij te geven.

2. **Aanbevolen verduidelijking — intake-handoff.md, Overgang naar conceptontwerp.**
   Budget en planning worden als startvoorwaarden genoemd. Dat is passend voordat
   afgesproken ontwerpwerk of capaciteit wordt toegezegd, maar mag de reeds
   geautoriseerde vrijblijvende voorbereiding niet blokkeren. Die voorbereiding is
   hier aantoonbaar uitgevoerd, dus er is geen proefcriterium geschonden. Maak
   expliciet dat voorbereiding binnen de huidige opdracht kan doorgaan en dat
   concrete ontwerp- en productieafspraken pas na scopeafstemming volgen.

Er zijn geen blokkerende fouten in de zeven testuitkomsten. De ontbrekende echte
licentie en productieafspraken zouden daadwerkelijke vrijgave blokkeren, maar
zijn in deze proef juist zichtbaar als ontbrekend geregistreerd.

## Routing en profieldekking

**PASS voor inhoudelijke overeenkomst.** Alle zes profielen bestaan, noemen de
bijbehorende handboekrol en instrueren uitvoering van diens stappen en
gereedcriteria. De gedeelde opdracht, overdracht, fontbeleid, dekkingsmatrix,
bestandsafbakening en Pauls eindbeoordeling worden expliciet doorverwezen.
`AGENTS.md` routeert intake, onderzoek, identiteit, toepassingen en review naar
het handboek, houdt coördinatie bij de hoofdchat, verlangt relevante specialisten
en afzonderlijke review, en beschrijft de standaard-subagentfallback. De UI/UX-route
komt overeen met het handboek. Geen wezenlijke inhoudelijke gaten gevonden.

Dit oordeel verifieert geen TOML-parser, automatische discovery, actieve
registratie of uitvoering van alle zes rollen. Alleen onderzoeker en reviewer
zijn in deze tekstproef via de expliciete fallback aan bod gekomen. De compacte
profielen zijn afhankelijk van het daadwerkelijk lezen van het handboek; hun
teksten vormen geen zelfstandig volledige werkinstructie.

## Beperkingen en advies

Geen ontwerpen, renders, prototypes, bronbestanden, exports, fontbestanden,
assetlicenties of gebruikerstests zijn geleverd of getest. Er kan dus geen
oordeel volgen over visuele eigenheid, contrast, merkconsistentie in toepassingen,
bewerkbaarheid, uitvoerkwaliteit of productiegeschiktheid. Marktclaims zijn alleen
op bewijsstatus gecontroleerd; geen externe feiten zijn bevestigd. Een aparte
review beperkt zelfbevestiging en bewijst geen foutloosheid.

**Advies:** de fictieve tekstproef voldoet aan alle zeven criteria. Laat de maker
bevinding 1 herstellen en bij voorkeur bevinding 2 verduidelijken, en laat de
reviewer die concrete correcties controleren voordat deze overdracht als afgerond
proefresultaat aan Paul wordt gepresenteerd. Dit is geen vrijgave voor ontwerp,
productie of klantgebruik. Paul behoudt alle menselijke eindgoedkeuring.

## Hercontrole — 2026-10-06

De twee door de hoofdchat aangepaste passages in `intake-handoff.md` zijn opnieuw
gelezen. **Bevinding 1: opgelost** — besluit 5 is verwijderd; het fontbeleid wordt
automatisch toegepast en Linde Display blijft geblokkeerd zonder licentiebewijs.
**Bevinding 2: opgelost** — de startvoorwaarden gelden voor nieuw af te spreken
conceptontwerp; geautoriseerde voorbereiding kan expliciet doorgaan zonder nieuwe
budget- of planningsdrempel. De uitkomst blijft **7/7 PASS**. Er staan geen
correcties uit deze review meer open; de tekstproef kan aan Paul ter beoordeling
worden gepresenteerd. De eerder genoemde beperkingen blijven gelden; dit advies
is geen menselijke goedkeuring of productievrijgave.
