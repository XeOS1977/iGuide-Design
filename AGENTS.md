# iGuide Design

A digital design company delivering customer projects for corporate branding
and digital assets, including websites and apps.

## Change workflow

Use a dedicated branch and draft pull request for each change.
Before editing files, confirm that the branch has an open pull request.
Check repository status and fetch remote changes before starting; preserve user work.
Keep changes within the pull request's scope; never push directly to `main`.
For a new branch, use a planning-only commit to open the draft pull request
before editing implementation files. This planning file is the sole pre-PR
file-edit exception. Review the complete diff and run appropriate checks before
committing and pushing changes to the pull request branch.

## Agent skills

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
