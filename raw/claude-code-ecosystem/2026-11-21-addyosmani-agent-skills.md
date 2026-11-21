# Agent Skills

> Source: https://github.com/addyosmani/agent-skills
> Collected: 2026-11-21
> Published: Unknown

Title: GitHub - addyosmani/agent-skills: Production-grade engineering skills for AI coding agents.

URL Source: http://github.com/addyosmani/agent-skills

Final URL: https://github.com/addyosmani/agent-skills

Markdown Content:
**Production-grade engineering skills for AI coding agents.**

Skills encode the workflows, quality gates, and best practices that senior engineers use when building software. These ones are packaged so AI agents follow them consistently across every phase of development.

[![Image 1: addyosmani%2Fagent-skills | Trendshift](https://camo.githubusercontent.com/5dc6e429424932795b82fa89fa3e85ff9f25c761cd92182a6862cae6554d8a2e/68747470733a2f2f7472656e6473686966742e696f2f6170692f62616467652f7265706f7369746f726965732f3235323030)](https://trendshift.io/repositories/25200)

[![Image 2: Addy's Agent Skills](https://camo.githubusercontent.com/5183c88c0c465e42b11e52276ceb439ba1ada7008e8d7ba9ef52870a36f67fd3/68747470733a2f2f616464796f736d616e692e636f6d2f6173736574732f696d616765732f61646479732d6167656e742d736b696c6c732e6a7067)](https://camo.githubusercontent.com/5183c88c0c465e42b11e52276ceb439ba1ada7008e8d7ba9ef52870a36f67fd3/68747470733a2f2f616464796f736d616e692e636f6d2f6173736574732f696d616765732f61646479732d6167656e742d736b696c6c732e6a7067)

```
DEFINE          PLAN           BUILD          VERIFY         REVIEW          SHIP
 ┌──────┐      ┌──────┐      ┌──────┐      ┌──────┐      ┌──────┐      ┌──────┐
 │ Idea │ ───▶ │ Spec │ ───▶ │ Code │ ───▶ │ Test │ ───▶ │  QA  │ ───▶ │  Go  │
 │Refine│      │  PRD │      │ Impl │      │Debug │      │ Gate │      │ Live │
 └──────┘      └──────┘      └──────┘      └──────┘      └──────┘      └──────┘
  /spec          /plan          /build        /test         /review       /ship
```

* * *

## Commands

[](https://github.com/addyosmani/agent-skills#commands)
10 slash commands that map to the development lifecycle. Each one activates the right skills automatically.

| What you're doing | Command | Key principle |
| --- | --- | --- |
| Define what to build | `/spec` | Spec before code |
| Plan how to build it | `/plan` | Small, atomic tasks |
| Build incrementally | `/build` | One slice at a time |
| Prove it works | `/test` | Tests are proof |
| Set the quality bar | `/constraints` | Decide it once, enforce it everywhere |
| Review before merge | `/review` | Improve code health |
| Audit web performance | `/webperf` | Measure before you optimize |
| Audit accessibility | `/a11y` | Automation is a smoke test; manual verification completes the audit |
| Simplify the code | `/code-simplify` | Clarity over cleverness |
| Ship to production | `/ship` | Faster is safer |

In Claude Code these install as plugin commands. Where a built-in command has the same name, as `/review` does, use the namespaced form: `/agent-skills:review`.

Want fewer manual steps once the spec exists? **`/build auto`** generates the plan and implements every task in a single approved pass — you approve the plan once, then it runs autonomously. It removes the human stepping _between_ tasks, not the verification: every task is still test-driven and committed individually, and it pauses on failures or risky steps.

Skills also activate automatically based on what you're doing — designing an API triggers `api-and-interface-design`, building UI triggers `frontend-ui-engineering`, and so on.

* * *

## Quick Start

[](https://github.com/addyosmani/agent-skills#quick-start)
**Fastest path — any agent, one command.** The open [skills CLI](https://github.com/vercel-labs/skills) installs into 70+ agents (Claude Code, Cursor, Codex, Copilot, Cline, and more):

npx skills add addyosmani/agent-skills            # install all 26 skills
npx skills add addyosmani/agent-skills --list     # browse before installing

Or grab individual skills:

npx skills add addyosmani/agent-skills --skill code-review-and-quality   # five-axis review before merge
npx skills add addyosmani/agent-skills --skill interview-me              # requirements interrogation, one question at a time
npx skills add addyosmani/agent-skills --skill test-driven-development   # red-green-refactor, enforced

> **Installing one skill?** A per-skill `npx` install copies only `skills/<name>/`, not the repo-level `references/` directory. The skill still works, but paths to supplementary shared checklists are unavailable. Use a whole-repo integration, clone the repository, or copy the needed checklist into a `references/` directory inside the installed skill. This portability gap is tracked in [#361](https://github.com/addyosmani/agent-skills/issues/361).

Prefer a native integration? Pick your tool below.

**Claude Code (recommended)**
**Marketplace install:**

```
/plugin marketplace add addyosmani/agent-skills
/plugin install agent-skills@addy-agent-skills
```

> **SSH errors?** The marketplace clones repos via SSH. If you don't have SSH keys set up on GitHub, either [add your SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) or use the full HTTPS URL to force HTTPS cloning during the marketplace-add step:
> 
> 
> 
> /plugin marketplace add https://github.com/addyosmani/agent-skills.git
> /plugin install agent-skills@addy-agent-skills
> 
> 
> If `/plugin install` still fails with `git@github.com: Permission denied (publickey)` on Windows or macOS, the recommended workaround is to configure Git once to rewrite GitHub SSH URLs to HTTPS for subprocess clones:
> 
> 
> 
> git config --global url."https://github.com/".insteadOf git@github.com:

**Local / development:**

git clone https://github.com/addyosmani/agent-skills.git
claude --plugin-dir /path/to/agent-skills

**Cursor**
Put workflow skills under `.cursor/skills/` (sync from `agent-skills/skills/`) and short policies in `.cursor/rules/*.mdc` — do not paste full skills into rules. Both directories live in your project; this repo does not ship a `.cursor/` folder. See [docs/cursor-setup.md](https://github.com/addyosmani/agent-skills/blob/main/docs/cursor-setup.md).

**Antigravity CLI**
Install as a native plugin for skills and subagents. In affected Antigravity CLI releases, legacy command TOMLs are reported as converted but their wrapper commands are not discoverable; invoke the underlying namespaced skills directly. See [docs/antigravity-setup.md](https://github.com/addyosmani/agent-skills/blob/main/docs/antigravity-setup.md#lifecycle-workflows-and-command-compatibility).

**Install from the repo:**

agy plugin install https://github.com/addyosmani/agent-skills.git

**Install from a local clone:**

git clone https://github.com/addyosmani/agent-skills.git
agy plugin install ./agent-skills

**Gemini CLI**
Install as native skills for auto-discovery, or add to `GEMINI.md` for persistent context. See [docs/gemini-cli-setup.md](https://github.com/addyosmani/agent-skills/blob/main/docs/gemini-cli-setup.md).

**Install from the repo:**

gemini skills install https://github.com/addyosmani/agent-skills.git --path skills

**Install from a local clone:**

gemini skills install ./agent-skills/skills/

**Windsurf**
Add skill contents to your Windsurf rules configuration. See [docs/windsurf-setup.md](https://github.com/addyosmani/agent-skills/blob/main/docs/windsurf-setup.md).

**OpenCode**
Copy skills to `.opencode/skills/` (or `~/.config/opencode/skills/`), add a project-local `AGENTS.md`, and use the built-in `skill` tool for agent-driven execution. Optional slash commands can be added under `.opencode/commands/`.

See [docs/opencode-setup.md](https://github.com/addyosmani/agent-skills/blob/main/docs/opencode-setup.md).

**GitHub Copilot**
Use agent definitions from `agents/` as Copilot personas and skill content in `.github/copilot-instructions.md`. The lifecycle slash commands (`/spec`, `/plan`, `/build`, `/test`, `/review`, `/ship`) are Claude Code commands and do not appear in Copilot; invoke the skills by name (`/spec-driven-development`, …) instead. See [docs/copilot-setup.md](https://github.com/addyosmani/agent-skills/blob/main/docs/copilot-setup.md).

Using the standalone `copilot` CLI? Install it as a plugin — see [docs/copilot-cli-setup.md](https://github.com/addyosmani/agent-skills/blob/main/docs/copilot-cli-setup.md).

**Kiro IDE & CLI** Skills for Kiro reside under ".kiro/skills/" and can be stored under Project or Global level. Kiro also supports Agents.md. See Kiro docs at [https://kiro.dev/docs/skills/](https://kiro.dev/docs/skills/)

**Codex**
Install as a native Codex plugin (Codex CLI v0.122+):

codex plugin marketplace add addyosmani/agent-skills
codex plugin add agent-skills@agent-skills

The first command registers the marketplace; the second installs the plugin. Codex reads the root `skills/` directory directly through `.codex-plugin/plugin.json`. Once installed, invoke skills in chat using `@` (e.g., `@spec-driven-development`). See [docs/codex-setup.md](https://github.com/addyosmani/agent-skills/blob/main/docs/codex-setup.md) for local installation and troubleshooting.

**Command Code**
Install natively with the built-in `cmd skills` command. Command Code clones the repo, discovers every `SKILL.md`, and installs into `.commandcode/skills/`:

cmd skills add addyosmani/agent-skills            # pick skills to install (project)
cmd skills add addyosmani/agent-skills --global   # install for all projects (~/.commandcode/skills/)
cmd skills add addyosmani/agent-skills -s spec-driven-development  # install a specific skill

Installed skills show up in the TUI slash menu, e.g. `/spec-driven-development`. See [docs/commandcode-setup.md](https://github.com/addyosmani/agent-skills/blob/main/docs/commandcode-setup.md).

**Other Agents**
Skills are plain Markdown - they work with any agent that accepts system prompts or instruction files. See [docs/getting-started.md](https://github.com/addyosmani/agent-skills/blob/main/docs/getting-started.md). Hosts that install the pack but aren't listed above are in [docs/other-hosts.md](https://github.com/addyosmani/agent-skills/blob/main/docs/other-hosts.md).

* * *

## Adoption

[](https://github.com/addyosmani/agent-skills#adoption)
Already installed? How you roll the pack out depends on your codebase. The **[Adoption Guide](https://github.com/addyosmani/agent-skills/blob/main/docs/adoption-guide.md)** covers two paths: the full lifecycle from day one for a greenfield project, or an incremental, verification-first rollout for an established codebase.

* * *

## All 26 Skills

[](https://github.com/addyosmani/agent-skills#all-26-skills)
The commands above are entry points. The pack includes 26 skills total — 25 lifecycle skills plus the `using-agent-skills` meta-skill. Each skill is a structured workflow with steps, verification gates, and anti-rationalization tables. You can also reference any skill directly.

### Meta - Discover which skill applies

[](https://github.com/addyosmani/agent-skills#meta---discover-which-skill-applies)
| Skill | What It Does | Use When |
| --- | --- | --- |
| [using-agent-skills](https://github.com/addyosmani/agent-skills/blob/main/skills/using-agent-skills/SKILL.md) | Maps incoming work to the right skill workflow and defines shared operating rules | Starting a session or deciding which skill applies |

### Define - Clarify what to build

[](https://github.com/addyosmani/agent-skills#define---clarify-what-to-build)
| Skill | What It Does | Use When |
| --- | --- | --- |
| [interview-me](https://github.com/addyosmani/agent-skills/blob/main/skills/interview-me/SKILL.md) | One-question-at-a-time interview that extracts what the user actually wants instead of what they think they should want, until ~95% confidence | The ask is underspecified, or the user invokes "interview me" / "grill me" |
| [idea-refine](https://github.com/addyosmani/agent-skills/blob/main/skills/idea-refine/SKILL.md) | Structured divergent/convergent thinking to turn vague ideas into concrete proposals | You have a rough concept that needs exploration |
| [spec-driven-development](https://github.com/addyosmani/agent-skills/blob/main/skills/spec-driven-development/SKILL.md) | Write a PRD covering objectives, commands, structure, code style, testing, and boundaries before any code | Starting a new project, feature, or significant change |
| [constraint-driven-development](https://github.com/addyosmani/agent-skills/blob/main/skills/constraint-driven-development/SKILL.md) | Interviews you for a quality bar with sane default thresholds, writes CONSTRAINTS.md, places each check by cost, and catches agents silencing checks or skipping tests to get green | No standards are written down, or an agent is producing more than anyone reads |

### Plan - Break it down

[](https://github.com/addyosmani/agent-skills#plan---break-it-down)
| Skill | What It Does | Use When |
| --- | --- | --- |
| [planning-and-task-breakdown](https://github.com/addyosmani/agent-skills/blob/main/skills/planning-and-task-breakdown/SKILL.md) | Decompose specs into small, verifiable tasks with acceptance criteria and dependency ordering | You have a spec and need implementable units |

### Build - Write the code

[](https://github.com/addyosmani/agent-skills#build---write-the-code)
| Skill | What It Does | Use When |
| --- | --- | --- |
| [incremental-implementation](https://github.com/addyosmani/agent-skills/blob/main/skills/incremental-implementation/SKILL.md) | Thin vertical slices - implement, test, verify, commit. Feature flags, safe defaults, rollback-friendly changes | Any change touching more than one file |
| [test-driven-development](https://github.com/addyosmani/agent-skills/blob/main/skills/test-driven-development/SKILL.md) | Red-Green-Refactor, test pyramid (80/15/5), test sizes, DAMP over DRY, Beyonce Rule, browser testing | Implementing logic, fixing bugs, or changing behavior |
| [context-engineering](https://github.com/addyosmani/agent-skills/blob/main/skills/context-engineering/SKILL.md) | Feed agents the right information at the right time - rules files, context packing, MCP integrations | Starting a session, switching tasks, or when output quality drops |
| [source-driven-development](https://github.com/addyosmani/agent-skills/blob/main/skills/source-driven-development/SKILL.md) | Ground every framework decision in official documentation - verify, cite sources, flag what's unverified | You want authoritative, source-cited code for any framework or library |
| [doubt-driven-development](https://github.com/addyosmani/agent-skills/blob/main/skills/doubt-driven-development/SKILL.md) | Adversarial fresh-context review of every non-trivial decision in-flight - CLAIM → EXTRACT → DOUBT → RECONCILE → STOP, with optional user-authorized cross-model escalation | Stakes are high (production, security, irreversible), working in unfamiliar code, or a confident output is cheaper to verify now than to debug later |
| [frontend-ui-engineering](https://github.com/addyosmani/agent-skills/blob/main/skills/frontend-ui-engineering/SKILL.md) | Component architecture, design systems, state management, responsive design, WCAG 2.1 AA accessibility | Building or modifying user-facing interfaces |
| [api-and-interface-design](https://github.com/addyosmani/agent-skills/blob/main/skills/api-and-interface-design/SKILL.md) | Contract-first design, Hyrum's Law, One-Version Rule, error semantics, boundary validation | Designing APIs, module boundaries, or public interfaces |

### Verify - Prove it works

[](https://github.com/addyosmani/agent-skills#verify---prove-it-works)
| Skill | What It Does | Use When |
| --- | --- | --- |
| [browser-testing-with-devtools](https://github.com/addyosmani/agent-skills/blob/main/skills/browser-testing-with-devtools/SKILL.md) | Chrome DevTools MCP for live runtime data - DOM inspection, console logs, network traces, performance profiling | Building or debugging anything that runs in a browser |
| [debugging-and-error-recovery](https://github.com/addyosmani/agent-skills/blob/main/skills/debugging-and-error-recovery/SKILL.md) | Five-step triage: reproduce, localize, reduce, fix, guard. Stop-the-line rule, safe fallbacks | Tests fail, builds break, or behavior is unexpected |

### Review - Quality gates before merge

[](https://github.com/addyosmani/agent-skills#review---quality-gates-before-merge)
| Skill | What It Does | Use When |
| --- | --- | --- |
| [code-review-and-quality](https://github.com/addyosmani/agent-skills/blob/main/skills/code-review-and-quality/SKILL.md) | Five-axis review, change sizing (~100 lines), severity labels (Nit/Optional/FYI), review speed norms, splitting strategies | Before merging any change |
| [code-simplification](https://github.com/addyosmani/agent-skills/blob/main/skills/code-simplification/SKILL.md) | Chesterton's Fence, Rule of 500, reduce complexity while preserving exact behavior | Code works but is harder to read or maintain than it should be |
| [security-and-hardening](https://github.com/addyosmani/agent-skills/blob/main/skills/security-and-hardening/SKILL.md) | OWASP Top 10 prevention, auth patterns, secrets management, dependency auditing, three-tier boundary system | Handling user input, auth, data storage, or external integrations |
| [performance-optimization](https://github.com/addyosmani/agent-skills/blob/main/skills/performance-optimization/SKILL.md) | Measure-first approach - Core Web Vitals targets, profiling workflows, bundle analysis, anti-pattern detection | Performance requirements exist or you suspect regressions |
| [accessibility-engineering](https://github.com/addyosmani/agent-skills/blob/main/skills/accessibility-engineering/SKILL.md) | Audit an existing interface for WCAG 2.2 AA conformance and remediate the violations found - axe-core and pa11y commands, keyboard and screen reader testing, severity triage | Auditing a page or component for accessibility before shipping |

### Ship - Deploy with confidence

[](https://github.com/addyosmani/agent-skills#ship---deploy-with-confidence)
| Skill | What It Does | Use When |
| --- | --- | --- |
| [git-workflow-and-versioning](https://github.com/addyosmani/agent-skills/blob/main/skills/git-workflow-and-versioning/SKILL.md) | Trunk-based development, atomic commits, change sizing (~100 lines), the commit-as-save-point pattern | Making any code change (always) |
| [ci-cd-and-automation](https://github.com/addyosmani/agent-skills/blob/main/skills/ci-cd-and-automation/SKILL.md) | Shift Left, Faster is Safer, feature flags, quality gate pipelines, failure feedback loops | Setting up or modifying build and deploy pipelines |
| [deprecation-and-migration](https://github.com/addyosmani/agent-skills/blob/main/skills/deprecation-and-migration/SKILL.md) | Code-as-liability mindset, compulsory vs advisory deprecation, migration patterns, zombie code removal | Removing old systems, migrating users, or sunsetting features |
| [documentation-and-adrs](https://github.com/addyosmani/agent-skills/blob/main/skills/documentation-and-adrs/SKILL.md) | Architecture Decision Records, API docs, inline documentation standards - document the _why_ | Making architectural decisions, changing APIs, or shipping features |
| [observability-and-instrumentation](https://github.com/addyosmani/agent-skills/blob/main/skills/observability-and-instrumentation/SKILL.md) | Structured logging, RED metrics, OpenTelemetry tracing, symptom-based alerting - instrument as you build | Adding telemetry, or shipping anything that runs in production |
| [shipping-and-launch](https://github.com/addyosmani/agent-skills/blob/main/skills/shipping-and-launch/SKILL.md) | Pre-launch checklists, feature flag lifecycle, staged rollouts, rollback procedures, monitoring setup | Preparing to deploy to production |

* * *

## Agent Personas

[](https://github.com/addyosmani/agent-skills#agent-personas)
Pre-configured specialist personas for targeted reviews:

| Agent | Role | Perspective |
| --- | --- | --- |
| [code-reviewer](https://github.com/addyosmani/agent-skills/blob/main/agents/code-reviewer.md) | Senior Staff Engineer | Five-axis code review with "would a staff engineer approve this?" standard |
| [test-engineer](https://github.com/addyosmani/agent-skills/blob/main/agents/test-engineer.md) | QA Specialist | Test strategy, coverage analysis, and the Prove-It pattern |
| [security-auditor](https://github.com/addyosmani/agent-skills/blob/main/agents/security-auditor.md) | Security Engineer | Vulnerability detection, threat modeling, OWASP assessment |
| [web-performance-auditor](https://github.com/addyosmani/agent-skills/blob/main/agents/web-performance-auditor.md) | Web Performance Engineer | Core Web Vitals audit with Quick/Deep modes and a metric-honesty rule; run it via `/webperf` |
| [accessibility-auditor](https://github.com/addyosmani/agent-skills/blob/main/agents/accessibility-auditor.md) | Accessibility Engineer | WCAG 2.2 AA audit with a scorecard and findings ranked by real user impact; run it via `/a11y` |

See [docs/agents.md](https://github.com/addyosmani/agent-skills/blob/main/docs/agents.md) for the decision matrix, orchestration rules, and how personas compose with skills and slash commands.

* * *

## Reference Checklists

[](https://github.com/addyosmani/agent-skills#reference-checklists)
Quick-reference material that skills pull in when needed:

| Reference | Covers |
| --- | --- |
| [definition-of-done.md](https://github.com/addyosmani/agent-skills/blob/main/references/definition-of-done.md) | Project-wide standing bar every change clears, contrasted with per-task acceptance criteria |
| [testing-patterns.md](https://github.com/addyosmani/agent-skills/blob/main/references/testing-patterns.md) | Test structure, naming, mocking, React/API/E2E examples, anti-patterns (JavaScript/TypeScript) |
| [security-checklist.md](https://github.com/addyosmani/agent-skills/blob/main/references/security-checklist.md) | Pre-commit checks, auth, input validation, headers, CORS, OWASP Top 10 |
| [performance-checklist.md](https://github.com/addyosmani/agent-skills/blob/main/references/performance-checklist.md) | Core Web Vitals targets, frontend/backend checklists, measurement commands |
| [accessibility-checklist.md](https://github.com/addyosmani/agent-skills/blob/main/references/accessibility-checklist.md) | Keyboard nav, screen readers, visual design, ARIA, testing tools |
| [observability-checklist.md](https://github.com/addyosmani/agent-skills/blob/main/references/observability-checklist.md) | On-call questions, structured logging, RED/USE metrics, tracing, symptom-based alerting, pre-launch gate |
| [orchestration-patterns.md](https://github.com/addyosmani/agent-skills/blob/main/references/orchestration-patterns.md) | Endorsed multi-persona orchestration patterns, anti-patterns, and the "personas don't invoke personas" rule |

* * *

## How Skills Work

[](https://github.com/addyosmani/agent-skills#how-skills-work)
Every skill follows a consistent anatomy:

```
┌─────────────────────────────────────────────────┐
│  SKILL.md                                       │
│                                                 │
│  ┌─ Frontmatter ─────────────────────────────┐  │
│  │ name: lowercase-hyphen-name               │  │
│  │ description: Guides agents through [task].│  │
│  │              Use when…                    │  │
│  └───────────────────────────────────────────┘  │                                                                                                
│  Overview         → What this skill does        │
│  When to Use      → Triggering conditions       │
│  Process          → Step-by-step workflow       │
│  Rationalizations → Excuses + rebuttals         │
│  Red Flags        → Signs something's wrong     │
│  Verification     → Evidence requirements       │
└─────────────────────────────────────────────────┘
```

**Key design choices:**

*   **Process, not prose.** Skills are workflows agents follow, not reference docs they read. Each has steps, checkpoints, and exit criteria.
*   **Anti-rationalization.** Every skill includes a table of common excuses agents use to skip steps (e.g., "I'll add tests later") with documented counter-arguments.
*   **Verification is non-negotiable.** Every skill ends with evidence requirements - tests passing, build output, runtime data. "Seems right" is never sufficient.
*   **Progressive disclosure.** The `SKILL.md` is the entry point. Supporting references load only when needed, keeping token usage minimal.

* * *

## Project Structure

[](https://github.com/addyosmani/agent-skills#project-structure)
The portable core stays in shared directories. Host-specific paths are native discovery conventions, not branding aliases; renaming or merging them would break the tools that scan those exact locations.

| Layer / consumer | Repository paths | Purpose |
| --- | --- | --- |
| Shared workflow core | `skills/` (26 skills) | Portable `SKILL.md` workflows used by every integration |
| Shared review material | `agents/` (5 personas), `references/` (7 checklists) | Specialist reviewers and pack-level checklists carried by whole-repo installs |
| Claude Code adapter | `.claude/commands/` (10 commands), `.claude-plugin/`, `hooks/` | Slash-command wrappers, marketplace metadata, and lifecycle hooks |
| Gemini CLI adapter | `.gemini/commands/` (10 commands) | Gemini-native TOML command wrappers |
| Antigravity CLI adapter | `commands/` (10 commands), `plugin.json` | Legacy TOML wrappers and the root plugin manifest; see the [known wrapper limitation](https://github.com/addyosmani/agent-skills/blob/main/docs/antigravity-setup.md#lifecycle-workflows-and-command-compatibility) |
| Codex adapter | `.codex-plugin/`, `.agents/plugins/` | Codex plugin metadata and marketplace registration; Codex consumes `skills/` directly |
| GitHub Copilot CLI adapter | `plugin.json` | Root plugin metadata; Copilot CLI discovers `skills/` by convention and does not register the lifecycle wrappers |
| Contributor tooling | `scripts/` (13 scripts), `evals/` (26 case files), `.github/workflows/` | Validation, routing evals, and CI |
| Documentation | `docs/` | Universal guidance and per-tool setup guides |

Tools without a checked-in adapter directory install or copy the shared `skills/` core into their own native location. The [Quick Start](https://github.com/addyosmani/agent-skills#quick-start) links the setup guide for each supported host.

* * *

## Why Agent Skills?

[](https://github.com/addyosmani/agent-skills#why-agent-skills)
AI coding agents default to the shortest path - which often means skipping specs, tests, security reviews, and the practices that make software reliable. Agent Skills gives agents structured workflows that enforce the same discipline senior engineers bring to production code.

Each skill encodes hard-won engineering judgment: _when_ to write a spec, _what_ to test, _how_ to review, and _when_ to ship. These aren't generic prompts - they're the kind of opinionated, process-driven workflows that separate production-quality work from prototype-quality work.

Skills bake in best practices from Google's engineering culture — including concepts from [Software Engineering at Google](https://abseil.io/resources/swe-book) and Google's [engineering practices guide](https://google.github.io/eng-practices/). You'll find Hyrum's Law in API design, the Beyonce Rule and test pyramid in testing, change sizing and review speed norms in code review, Chesterton's Fence in simplification, trunk-based development in git workflow, Shift Left and feature flags in CI/CD, and a dedicated deprecation skill treating code as a liability. These aren't abstract principles — they're embedded directly into the step-by-step workflows agents follow.

* * *

## How it compares

[](https://github.com/addyosmani/agent-skills#how-it-compares)
Wondering how this stacks up against [Superpowers](https://github.com/obra/superpowers) or [Matt Pocock's skills](https://github.com/mattpocock/skills)? See **[docs/comparison.md](https://github.com/addyosmani/agent-skills/blob/main/docs/comparison.md)** for an honest, side-by-side look at how the three are shaped differently and when to reach for each — including a link to a controlled [head-to-head experiment](https://www.linkedin.com/pulse/superpowers-vs-agent-skills-faster-shipping-safer-reasoning-om-mishra-dzakf/).

* * *

## Contributing

[](https://github.com/addyosmani/agent-skills#contributing)
Skills should be **specific** (actionable steps, not vague advice), **verifiable** (clear exit criteria with evidence requirements), **battle-tested** (based on real workflows), and **minimal** (only what's needed to guide the agent).

See [docs/skill-anatomy.md](https://github.com/addyosmani/agent-skills/blob/main/docs/skill-anatomy.md) for the format specification, [CONTRIBUTING.md](https://github.com/addyosmani/agent-skills/blob/main/CONTRIBUTING.md) for guidelines, and [docs/advanced-per-agent-configuration.md](https://github.com/addyosmani/agent-skills/blob/main/docs/advanced-per-agent-configuration.md) for applying model routing, tool restrictions, and other per-agent runtime controls without breaking the portable `SKILL.md` frontmatter.

* * *

## Team

[](https://github.com/addyosmani/agent-skills#team)
agent-skills is built and maintained by:

|  | Name | GitHub | Role |
| --- | --- | --- | --- |
| [![Image 3: Addy Osmani](https://github.com/addyosmani.png?size=120)](https://github.com/addyosmani.png?size=120) | **Addy Osmani** | [@addyosmani](https://github.com/addyosmani) | Creator |
| [![Image 4: Federico Bartoli](https://github.com/federicobartoli.png?size=120)](https://github.com/federicobartoli.png?size=120) | **Federico Bartoli** | [@federicobartoli](https://github.com/federicobartoli) | Collaborator |
| [![Image 5: Joan León](https://github.com/nucliweb.png?size=120)](https://github.com/nucliweb.png?size=120) | **Joan León** | [@nucliweb](https://github.com/nucliweb) | Collaborator |

* * *

## License

[](https://github.com/addyosmani/agent-skills#license)
MIT - use these skills in your projects, teams, and tools.
