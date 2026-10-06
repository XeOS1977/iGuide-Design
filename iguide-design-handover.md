# iGuide Design — session handover

## Purpose and scope

The user is establishing a digital design company that completes customer
projects for corporate branding and digital assets, including websites and apps.
The first requested deliverable was deployment of Matt Pocock's engineering
skills and UI UX Pro Max. The session completed that prerequisite setup,
verified skill discovery after a restart, and updated the Git workflow following
the user's revised preference.

This document records the decision history, practical rationale, verified facts,
and continuation context. Existing implementation and configuration are linked
rather than reproduced. No company website or customer application has yet been
implemented, and no visual identity, framework, or deployment platform has been
chosen.

## Current state

- Repository: <https://github.com/XeOS1977/iGuide-Design>.
- Workspace: `D:\AI\iGuide_Design` (Windows, PowerShell 5.1).
- Active branch: `main`.
- Local `HEAD` and `origin/main` both verified at
  `50a4203a79ceff802f2a852fb2fa8dffea65e7a6`.
- Working tree was clean after the final push.
- All repository setup changes are on local and remote `main`.
- PR #1 was already merged when the agent checked it during the workflow change:
  <https://github.com/XeOS1977/iGuide-Design/pull/1>.
- Matt Pocock skills are installed globally on this machine; UI UX Pro Max and
  its installer-bundled companion skills are committed in the repository.
- The user reported restarting OpenCode, and the agent verified the local UI UX
  Pro Max skill could then be loaded through the Skill tool.

## User requests and decisions, in order

### 1. Install the prerequisite skill sets

The user described the company and requested Matt Pocock skills plus “UI/UX Max
pro.” The agent identified the latter as **UI UX Pro Max** from the official
`nextlevelbuilder/ui-ux-pro-max-skill` repository.

Inspection found an empty local Git repository with no remote and no commits.
The Matt Pocock suite was already installed globally under
`~/.config/opencode/skills/` and exposed in the agent's skill catalogue. Rather
than duplicate that installation, the agent configured the project conventions
the suite expects.

Relevant sources:

- <https://github.com/mattpocock/skills>
- <https://github.com/nextlevelbuilder/ui-ux-pro-max-skill>

### 2. Choose issue tracking, labels, and agent instructions

The setup skill required confirmation of project conventions. Local Markdown
tracking was initially recommended because no remote existed. The user chose
GitHub instead and supplied `XeOS1977/iGuide-Design`.

The user approved:

- GitHub Issues as the authoritative tracker for specs and tickets.
- Default triage labels: `needs-triage`, `needs-info`, `ready-for-agent`,
  `ready-for-human`, and `wontfix`.
- `AGENTS.md` as the instruction file rather than `CLAUDE.md`.
- A single-context domain layout: root `CONTEXT.md` and `docs/adr/` when domain
  terminology or architectural decisions are actually resolved.

The single-context choice fit the empty, non-monorepo project. Domain documents
were not invented merely to satisfy a directory convention; the consumer rules
instruct agents to proceed silently when those artifacts are absent.

See the authoritative files:

- `AGENTS.md`
- `docs/agents/issue-tracker.md`
- `docs/agents/triage-labels.md`
- `docs/agents/domain.md`

### 3. Initially require a PR before implementation edits

While identifying the GitHub repository, the user requested a pull request every
time before changing files, to avoid drift.

Both local and GitHub repositories had no commits. GitHub needs a base branch
and a differing branch to create a PR. The agent explained this constraint and
proposed a bootstrap exception: an initial README commit on `main`, followed by
a planning-only commit on a setup branch to enable a draft PR. The user approved
the configuration draft, bootstrap, commits, and pushes.

The agent then:

1. Initialized `main` with the company README and configured `origin`.
2. Created `chore/design-skills-setup`.
3. Committed the approved plan at `docs/plans/design-skills-setup.md`.
4. Opened draft PR #1 before installation and project configuration edits.
5. Committed and pushed the setup to that PR branch.

The original workflow used a planning-only file exception for each new PR,
because a branch with no changes cannot open a useful GitHub PR. This workflow
is historical and was later explicitly revoked by the user.

### 4. Install UI UX Pro Max locally

The official documentation recommends its CLI to produce the assistant-specific
file structure. The agent ran:

```powershell
npx --yes ui-ux-pro-max-cli@latest init --ai opencode
```

The package version reported during setup was **2.15.0**. A pinned reproduction
command is recorded in `docs/agents/skills-setup.md`.

The resulting installation includes:

- `ui-ux-pro-max`
- `brand`
- `design`
- `design-system`
- `banner-design`
- `slides`
- `ui-styling`

These companion skills came from the installer and were retained because their
branding and design functions align with the stated company services. They do
not mean that every optional asset-generation integration was configured or
tested. The core UI UX Pro Max skill has local searchable datasets and Python
scripts; its search engine uses the standard library without third-party Python
packages.

The agent added Python cache exclusions in `.gitignore`, so running searches
does not create tracked Python bytecode artifacts.

### 5. Create GitHub triage labels

The GitHub repository already had `wontfix`. The agent created the other four
approved canonical labels and retained the existing label. Issue publication and
triage operations are documented in `docs/agents/issue-tracker.md`.

The setting **“PRs as a request surface: no”** concerns whether external PRs are
treated as incoming triage requests. It is distinct from the repository's own
change workflow and was not changed when the user's PR-first rule changed.

### 6. Verify the installation and the restart

Available runtime versions at setup:

- Node.js: `v24.19.0`
- npm: `11.17.0`
- Python: `3.12.10`

The agent successfully ran:

```powershell
python .opencode/skills/ui-ux-pro-max/scripts/search.py "digital design agency" --design-system -p "iGuide Design"
python .opencode/skills/ui-ux-pro-max/scripts/search.py "visible keyboard focus" --domain ux
```

Both returned results. The generated design-system output was an installation
smoke check, not an approved brand direction, and was not persisted as the
company's design system.

The user subsequently said, in Dutch, that OpenCode had been restarted and asked
for verification. The agent successfully loaded `ui-ux-pro-max` with the Skill
tool from the project installation and repeated a focused UX search with one
result. The global Matt Pocock skill catalogue was also visible. This verified
post-restart discoverability and core search behavior; it was not a full test of
every engineering or companion design skill.

Git status was clean and PR #1 was still open as a draft at that verification.

### 7. Revoke the PR requirement and put everything on main

The user's later instruction was:

> Vergeet mijn opdracht om PR's te doen en zorg ervoor dat alles in de main branch staat

Meaning: forget the previous PR instruction and ensure everything is on `main`.
This explicitly supersedes the initial PR-first preference.

After fetching, the agent found that PR #1 was already merged on GitHub and
remote `main` was ahead of local `main`. The agent did not need to merge the PR
itself. It switched to `main` and pulled with `--ff-only`.

It then updated:

- `AGENTS.md`: work directly on `main`; PRs are optional, not required. Preserve
  user work, fetch remote changes before starting, review the complete diff, and
  run appropriate checks before committing and pushing when requested.
- `docs/plans/design-skills-setup.md`: explicitly mark the PR-first setup plan as
  historical and point to `AGENTS.md` for the current workflow.

Rationale: preserve an accurate setup history without allowing a historical plan
to reintroduce a rule the user had revoked.

The user asked for this handover and then asked whether the instruction was
complete while the workflow edit was still unpushed. The agent accurately stated
that it was not yet fully finished, then reviewed the diff, ran `git diff
--check`, committed the two documentation changes, and pushed directly to
`main`. Local and remote commit IDs now match, and the working tree is clean.

## Commit history and references

Implementation details and file contents are available in the commits rather
than duplicated here:

| Commit | Purpose |
| --- | --- |
| `edf8fd8` | Initial company README; approved empty-repository bootstrap |
| `0d499d3` | Planning-only setup commit enabling the first draft PR |
| `a886728` | Engineering conventions and local design skill installation |
| `43431da` | Merge of PR #1 into main, discovered during the later fetch |
| `50a4203` | Remove mandatory PR workflow and document direct-main work |

Repository artifacts:

- `README.md`: company description.
- `AGENTS.md`: current agent instructions and skill context pointers.
- `docs/agents/*.md`: tracker, domain, labels, and installation conventions.
- `docs/plans/design-skills-setup.md`: historical approved setup scope.
- `.opencode/skills/`: committed UI UX Pro Max and companion skill assets.
- `.gitignore`: Python cache exclusions.

## Verification boundaries and portability

- Documentation diff checks passed for the agent-authored files.
- The complete vendor whitespace check reported trailing whitespace in the
  installer-bundled `ui-ux-pro-max/scripts/design_system.py`. Those files were
  retained as installed, and the finding was recorded in PR #1.
- No full upstream test suite or UI application test suite was run. Verification
  focused on installation, skill discovery, and working search commands.
- The Matt Pocock suite is global, so cloning this repository on another machine
  does not install it. Follow the source project's installation guidance there.
- UI UX Pro Max and companions are local and versioned in the repository.
- Skills/configuration changes require restarting OpenCode for discovery; the
  user has already done so for the installed skills.
- No credentials or tokens are included in this handover.

## Current decisions and unresolved product choices

Settled:

- Company scope: customer corporate branding and digital asset design.
- GitHub Issues for project specifications and tickets.
- Default triage labels.
- `AGENTS.md` for project agent instructions.
- Single-context domain-documentation convention.
- UI UX Pro Max for interface design, implementation, and review.
- Direct work on `main`; no mandatory PR process.

Not yet decided:

- Company positioning, target customers, brand identity, and content.
- Website/app feature scope and customer project workflow.
- Framework, hosting, deployment, and application architecture.

These are future planning topics, not blockers to the completed skills setup.

## Suggested skills for the next agent

Call the Skill tool according to the next actual task:

- `ui-ux-pro-max`: website/app design, implementation, or interface review.
- `brand` or `design`: company brand identity and related visual deliverables.
- `grill-me` or `grill-with-docs`: when the user wants to sharpen requirements
  through an interview; the latter can record domain terminology and ADRs.
- `to-spec` / `to-tickets`: publish agreed requirements or implementation tickets
  to the configured GitHub Issues tracker.
- `implement`: implement an agreed specification or ticket set.
- `domain-modeling`: resolve terminology or architectural domain decisions.
- `writing-for-agents`: edit agent-facing project documentation.
- `customize-opencode`: only when changing OpenCode configuration or skills.

Read `AGENTS.md` and the relevant linked conventions before continuing. Fetch
and inspect repository status first. The latest direct-main preference takes
precedence over historical PR-first records.

## Handover location

This handover was saved outside the repository to the approved OS temporary
directory, as instructed by the handoff skill:

`C:\Users\Paul\AppData\Local\Temp\opencode\iguide-design-handover.md`
