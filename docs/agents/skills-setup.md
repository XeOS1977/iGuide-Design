# Installed skills

## Matt Pocock engineering skills

The suite is installed globally at `~/.config/opencode/skills/` on the setup
machine. Project conventions are configured through `AGENTS.md` and the
issue-tracker, triage-labels, and domain documents in this directory.

Source: <https://github.com/mattpocock/skills>.
On another machine, install the suite for OpenCode before using these workflows;
the global skill files are not vendored in this repository.

## UI UX Pro Max

Installed locally using `ui-ux-pro-max-cli` version **2.15.0**:

```powershell
npx --yes ui-ux-pro-max-cli@2.15.0 init --ai opencode
```

Source: <https://github.com/nextlevelbuilder/ui-ux-pro-max-skill>.
The installer includes companion skills for brand, design, design-system,
banner-design, slides, and ui-styling under `.opencode/skills/`.

Python 3 is required for the local search engine; no Python packages are needed.
Verified on Windows with Python 3.12.10:

```powershell
python .opencode/skills/ui-ux-pro-max/scripts/search.py "digital design agency" --design-system -p "iGuide Design"
python .opencode/skills/ui-ux-pro-max/scripts/search.py "visible keyboard focus" --domain ux
```

Both commands returned results successfully. These are installation smoke checks;
their output does not establish the company's visual identity.

Quit and restart OpenCode after installing or updating skills so discovery reloads.
Edit `docs/agents/*.md` directly to update project conventions.
