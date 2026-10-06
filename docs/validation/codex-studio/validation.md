# Validatie Codex-studio — 2026-10-06

## Inrichting

- Zes projectprofielen in .codex/agents/, met name, description en developer_instructions.
- AGENTS.md koppelt studiowerk aan het handboek en expliciete specialistdelegatie.
- Hoofdchat coördineert en Paul behoudt klantcontact en creatieve eindbeoordeling.
- Geen globale configuratie, modelkeuze of permissies gewijzigd.

## Technische controles

- Python 3.12 tomllib parseert alle zes profielen; verplichte velden, unieke namen,
  bestandsnamen en verwijzingen gecontroleerd: geslaagd.
- UTF-8 en trailing-whitespacecontrole op nieuwe en gewijzigde bestanden: geslaagd.
- git diff --check voor bestaande gewijzigde bestanden: geslaagd.
- Codex Doctor 0.160.1 met --strict-config: configuratie geladen, 0 fail.
  Omgevingswaarschuwingen: Defender, geen Dev Drive, optionele MCP-instellingen,
  TERM=dumb en threadinventaris. Geen wijzigingen aan die onderwerpen uitgevoerd.

## Gedragstest

Briefing: brief.md. Synthetische intake: intake-handoff.md. Afzonderlijke review:
review.md. De onderzoeker en reviewer hebben hun TOML-profiel expliciet gelezen;
de huidige toolinterface biedt geen selector voor nieuw aangemaakte named agents.
Dit is de gedocumenteerde fallback, geen bewijs van automatische profieldetectie.

De proef toetst directe instroom, ontbrekend bronbewijs, fontbeleid, volledige
scopeafbakening en overdracht. Zie review.md voor de afzonderlijke uitkomsten.

## Grenzen

De proef is tekstueel. Geen echt marktonderzoek, visueel merkontwerp, fontlicentie,
bewerkbaar ontwerpbestand, PDF-export of gebruikersflow is geproduceerd of getest.
De andere vier rollen zijn structureel gecontroleerd, niet afzonderlijk uitgevoerd.
De expliciete fallback is hier uitgevoerd. Automatische ontdekking is inmiddels
ook bevestigd, zie de aanvullende afronding hieronder.

De inrichting is lokaal opgeslagen. Commit en push zijn niet uitgevoerd.

## Afronding en projectisolatie

Een verse Codex exec-sessie (0.160.1, ephemeral, read-only) is gevraagd uitsluitend
de in runtimecontext/tooldefinities zichtbare agenttypes te noemen, zonder tools of
bestandslezingen. Alle zes studio-profielen zijn teruggegeven. Dit bevestigt
automatische ontdekking in de verse CLI-sessie; de bestaande desktopchat blijft
de expliciete fallback gebruiken zolang diens toolinterface geen selector biedt.
De debug prompt-input-uitvoer alleen bevatte de namen niet en was onvoldoende
als detectietest. Er zijn geen globale instellingen gewijzigd.

De projectstarter is getest met twee afzonderlijke synthetische opdrachten in
een tijdelijke map. Input van project A verscheen niet in B; zes profielen en de
UI/UX-skill werden gekopieerd. Bestaande bestemmingen werden geweigerd met behoud
van hun inhoud; ongeldige IDs en bestemmingen in de bureaurepository eveneens.
De aanvullende review vond dat geneste bestemmingen binnen andere projecten of
Git-checkouts moesten worden geweigerd; daarvoor is een oudermapcontrole toegevoegd.

Vijf blijvende regressietests in scripts/test_new_project.py slagen: gescheiden
projecten, bestaande inhoud behouden, geneste klantopdracht weigeren, Git-oudermap
weigeren (inclusief .git-bestand), en bureaumap/ongeldig ID weigeren. De reviewer
heeft de oudermapcorrectie opnieuw beoordeeld en de bevinding gesloten.

Tests valideren werkmaporganisatie, geen harde leesrechtenisolatie tussen klanten.
Opleverregels en versiegebonden goedkeuring staan in docs/agents/project-workflow.md.
