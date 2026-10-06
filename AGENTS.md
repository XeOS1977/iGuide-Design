# iGuide Design

A digital design company delivering customer projects for corporate branding
and digital assets, including websites and apps.

## Change workflow

Work directly on `main`; pull requests are optional, not required.
Check repository status and fetch remote changes before starting; preserve user work.
Review the complete diff and run appropriate checks before committing and
pushing changes to `main` when requested.

## Agent skills

### Codex studio workflow

Codex is the primary environment. For client intake, research, brand identity,
brand applications, or studio quality reviews, read
`docs/agents/codex-studio-handbook.md` before execution.
The main chat coordinates; delegate scoped specialist work to subagents using
the project profiles in `.codex/agents/`. Use only relevant roles and request a
separate quality review before presenting a deliverable for Paul's approval.
If named profiles are unavailable in the current session, pass the matching
profile instructions and handbook to a standard subagent explicitly.
Paul owns client contact and creative final approval.
For a new client assignment or delivery, read `docs/agents/project-workflow.md`.
Create client work in a separate project directory using `scripts/new_project.py`;
this repository holds studio tooling, not client production files.

### Issue tracker

Use GitHub Issues in `XeOS1977/iGuide-Design` when publishing or reading specs,
tickets, or triage work. See `docs/agents/issue-tracker.md`.

### Triage labels

Use the five default triage labels when classifying issues.
See `docs/agents/triage-labels.md`.

### Domain docs

Before exploring the codebase, follow the single-context consumer rules in
`docs/agents/domain.md`: root `CONTEXT.md` and `docs/adr/`.

### UI/UX

For website and app interface design, implementation, or review, load
`ui-ux-pro-max` from `.opencode/skills/ui-ux-pro-max/SKILL.md`.
