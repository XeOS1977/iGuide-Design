# Issue tracker: GitHub

Track issues and specs in `XeOS1977/iGuide-Design` using the `gh` CLI.
The `origin` remote identifies the repository; specify
`--repo XeOS1977/iGuide-Design` when no remote is configured.

## Operations

- Publish a spec or ticket: `gh issue create --title "..." --body "..."`.
- Read a ticket: `gh issue view <number> --comments`.
- List work: `gh issue list --state open --json number,title,body,labels,assignees`.
- Comment: `gh issue comment <number> --body "..."`.
- Apply or remove labels: `gh issue edit <number> --add-label "..."`
  or `--remove-label "..."`.
- Close: `gh issue close <number> --comment "..."`.

## Pull requests as a triage surface

**PRs as a request surface: no.** This flag controls external PR triage;
the change workflow is defined in `AGENTS.md`.

## Wayfinding and dependencies

Use a single issue labelled `wayfinder:map` for the map and GitHub sub-issues
for child tickets. Label children `wayfinder:<type>` (`research`, `prototype`,
`grilling`, or `task`). If sub-issues are unavailable, use a task list in the
map and a `Part of #<map>` line in each child.

Use GitHub's native issue dependencies for blocking edges. Obtain the blocker's
database ID with `gh api repos/XeOS1977/iGuide-Design/issues/<number> --jq .id`,
then add it with
`gh api --method POST repos/XeOS1977/iGuide-Design/issues/<child>/dependencies/blocked_by -F issue_id=<blocker-id>`.
If dependencies are unavailable, record `Blocked by: #<number>` in the child.

For the frontier, select the first open child in map order with no open blockers
and no assignee. Claim with `gh issue edit <number> --add-assignee @me`.
Resolve by commenting with the answer, closing the child, and adding its gist
and link to the map's Decisions-so-far section.
