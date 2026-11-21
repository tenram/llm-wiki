# netresearch/github-project-skill — README and documentation

> Source: https://github.com/netresearch/github-project-skill
> Collected: 2026-11-15
> Published: Unknown



--- FILE: AGENTS.md ---

<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->
<!-- SPDX-FileCopyrightText: Netresearch DTT GmbH -->

# GitHub Project Skill

<!-- Index file — detail lives in docs/ and skills/. Keep under 100 lines. -->

## Repo Structure

- `skills/github-project/` — Skill definition (SKILL.md), checkpoints, evals
- `skills/github-project/references/` — Detailed reference docs (merge strategy, sub-issues, branch migration, etc.)
- `skills/github-project/assets/` — Templates (auto-merge workflows, PR templates, CODEOWNERS, etc.)
- `skills/github-project/scripts/` — `verify-github-project.sh` verification script, `init-branch-protection.sh` branch protection bootstrap
- `tests/` — Behavioural tests for the scripts (run by `.github/workflows/tests.yml`)
- `.github/workflows/` — CI (lint, tests, security, release, auto-merge-deps)
- `.claude-plugin/` — Plugin manifest for Claude Code marketplace
- `Build/` — Build scripts and git hooks
- `docs/` — Architecture and execution plans

## Scope

This skill covers **GitHub platform configuration only**:

- Branch protection rules and GitHub Rulesets
- CODEOWNERS configuration
- GitHub Issues, Discussions, Projects, sub-issues
- Dependabot/Renovate auto-merge (including merge queue GraphQL)
- PR review thread resolution (GraphQL API)
- Repository settings and release configuration
- Master-to-main branch migration

**Delegated to other skills:**

- CI/CD pipelines: `go-development`, `php-modernization`, `typo3-testing`
- Security scanning (CodeQL, gosec): `security-audit`
- SLSA, SBOMs, supply chain: `enterprise-readiness`
- Git branching, conventional commits: `git-workflow`

## Commands

```bash
# Lint (CI uses reusable workflow from skill-repo-skill)
# No local lint target — validation runs in GitHub Actions

# Verify a target repo's GitHub project setup
./skills/github-project/scripts/verify-github-project.sh /path/to/repo

# Check plugin version consistency
./Build/Scripts/check-plugin-version.sh

# Run the behavioural tests (offline; see README "Tests")
bash tests/verify-github-project.sh
bash tests/init-branch-protection.sh
bash tests/check-plugin-version.sh
bash tests/checkpoint-gh-37.sh
```

## Key Patterns

- Auto-merge has three variants: branch-protection (`--auto`), merge-queue (GraphQL `enqueuePullRequest`), direct (no protection)
- PR thread resolution requires GraphQL API — `gh` CLI does not support it
- Rulesets `allowed_merge_methods` must match repo-level merge settings
- Sub-issues use GraphQL `addSubIssue` mutation (up to 8 levels, 100 per parent)

## References

- `skills/github-project/references/auto-merge-guide.md` — Auto-merge setup patterns
- `skills/github-project/references/merge-strategy.md` — Merge method alignment
- `skills/github-project/references/sub-issues.md` — Sub-issues GraphQL API
- `skills/github-project/references/branch-migration.md` — Master to main migration
- `skills/github-project/references/repo-retirement.md` — Retiring a repository (consumers, Packagist abandon, archive)
- `skills/github-project/references/repository-structure.md` — Standard repo layout
- `skills/github-project/references/dependency-management.md` — Dependabot/Renovate config
- `skills/github-project/references/gh-cli-reference.md` — GitHub CLI patterns
- `skills/github-project/references/actionlint-guide.md` — Workflow linting
- `skills/github-project/references/pr-commit-cleanup.md` — PR commit hygiene
- `skills/github-project/references/reusable-workflow-security.md` — Workflow security
- `skills/github-project/references/security-config.md` — Security configuration
- `skills/github-project/references/org-security-settings.md` — Org-level security
- `skills/github-project/references/tag-validation.md` — Tag validation
- `skills/github-project/references/release-labeling.md` — Release label automation
- `skills/github-project/references/repo-setup-guide.md` — Repository setup guide
- `docs/ARCHITECTURE.md` — Architecture overview
- `docs/SECURITY-ASSURANCE.md` — Security assurance case: threats, trust boundaries, limits



--- FILE: README.md ---

---
# SPDX-License-Identifier: CC-BY-SA-4.0
# SPDX-FileCopyrightText: Netresearch DTT GmbH
name: github-project
description: "GitHub repository setup and platform-specific features. This skill should be used when creating new GitHub repositories, configuring branch protection rules, setting up GitHub Issues/Discussions/Projects, creating sub-issues and issue hierarchies, managing PR review workflows, configuring Dependabot/Renovate auto-merge, setting up merge queues with GraphQL enqueuePullRequest mutations, or checking GitHub project configuration. Focuses on GitHub platform features, not CI/CD pipelines or language-specific tooling. By Netresearch."
---

# GitHub Project Skill

GitHub platform configuration and repository management patterns. This skill focuses exclusively on **GitHub-specific features**.

> **New repo? Run this BEFORE the first PR:**
> `bash skills/github-project/scripts/init-branch-protection.sh OWNER/REPO`
> Applies `required_conversation_resolution: true` + 1-approver baseline so the
> "abort merge if unresolved threads" rule is structurally enforced, not just
> documented. See `skills/github-project/SKILL.md` → *Required First Step
> After `gh repo create`* for the full flow (baseline, required checks, merge queue).

## 🔌 Compatibility

This is an **Agent Skill** following the [open standard](https://agentskills.io) originally developed by Anthropic and released for cross-platform use.

**Supported Platforms:**
- ✅ Claude Code (Anthropic)
- ✅ Cursor
- ✅ GitHub Copilot
- ✅ Other skills-compatible AI agents

> Skills are portable packages of procedural knowledge that work across any AI agent supporting the Agent Skills specification.


## Scope Boundaries

**This Skill Covers:**
- Branch protection rules and PR workflows
- CODEOWNERS configuration
- GitHub Issues, Discussions, Projects
- Sub-issues and issue hierarchies (parent/child relationships)
- Dependabot/Renovate auto-merge
- GitHub Releases configuration
- Repository collaboration features

**Delegate to Other Skills:**
- CI/CD pipelines → `go-development`, `php-modernization`, `typo3-testing`
- Security scanning (CodeQL, gosec) → `security-audit`
- SLSA, SBOMs, supply chain → `enterprise-readiness`
- Git branching strategies, conventional commits → `git-workflow`

## Triggers

**Setup & Configuration:**
- Creating a new GitHub repository
- "Check my GitHub project setup"
- "Configure branch protection"
- "Set up GitHub Issues/Discussions"
- "How do I require PR reviews?"
- "Auto-merge Dependabot PRs"
- "Configure CODEOWNERS"

**Sub-Issues & Issue Hierarchies:**
- "Create sub-issues"
- "Add child issues to parent"
- "Link issues as parent/child"
- "Break down issue into sub-tasks"
- "Set up issue hierarchy"
- "Convert checklist to sub-issues"

**Troubleshooting (PR Merge Blocked):**
- "PR can't be merged" / "merge is blocked"
- "unresolved conversations" / "unresolved comments"
- "required reviews not met"
- "CODEOWNERS review required"
- "status checks failed" (for branch protection context)
- `gh pr merge` returns error

**Troubleshooting (Auto-Merge Failures):**
- "auto-merge not working" / "Dependabot PR not merging"
- "Merge method squash merging is not allowed"
- "Merge method merge commit is not allowed"
- "required status check not found"
- "status check name mismatch"
- PRs stuck with auto-merge enabled
- "Protected branch rules not configured" (--auto requires branch protection)
- Merge queue not processing PRs

**Troubleshooting (Ruleset Conflicts):**
- "Rebase is not an allowed merge method"
- "Squash is not an allowed merge method"
- "Merge commit is not an allowed merge method"
- Ruleset merge method mismatch warning on PR

**Merge Queue Configuration:**
- "set up merge queue"
- "enqueuePullRequest"
- "auto-merge with merge queue"
- "GraphQL merge queue mutation"

**Branch Migration:**
- "rename master to main"
- "change default branch"
- "migrate from master"
- "prevent master branch"
- "block master from being created"

## Installation

### Marketplace (Recommended)

Add the [Netresearch marketplace](https://github.com/netresearch/claude-code-marketplace) once, then browse and install skills:

```bash
# Claude Code
/plugin marketplace add netresearch/claude-code-marketplace
/plugin install github-project@netresearch-claude-code-marketplace
```

### Without a marketplace

Since Claude Code 2.1.157 a plugin directory under your personal skills directory loads on its own:

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/netresearch/github-project-skill.git \
  ~/.claude/skills/github-project
```

It loads as `github-project@skills-dir` on the next session. Update with `git -C ~/.claude/skills/github-project pull` and start a new session; remove it by deleting the directory. This route has no `claude plugin update`.

### npx ([skills.sh](https://skills.sh))

Install with any [Agent Skills](https://agentskills.io)-compatible agent:

```bash
npx skills add https://github.com/netresearch/github-project-skill --skill github-project
```

### Download Release

Download the [latest release](https://github.com/netresearch/github-project-skill/releases/latest) and extract to your agent's skills directory.

### Git Clone

```bash
git clone https://github.com/netresearch/github-project-skill.git
```

### Composer (PHP Projects)

```bash
composer require netresearch/github-project-skill
```

Requires [netresearch/composer-agent-skill-plugin](https://github.com/netresearch/composer-agent-skill-plugin).

### npm (Node Projects)

```bash
npm install --save-dev \
  @netresearch/agent-skill-coordinator \
  github:netresearch/github-project-skill
```

Requires [@netresearch/agent-skill-coordinator](https://github.com/netresearch/node-agent-skill-coordinator), which discovers the skill in `node_modules` and registers it in `AGENTS.md` via a `postinstall` hook. For pnpm, also allowlist the coordinator's postinstall:

```json
{
  "pnpm": {
    "onlyBuiltDependencies": ["@netresearch/agent-skill-coordinator"]
  }
}
```

## Workflows

### New Repository Setup

To set up a new GitHub repository:

1. Create essential files: README.md, LICENSE, SECURITY.md
2. Configure `.github/` directory structure (see `references/repository-structure.md`)
3. Set up branch protection on `main` branch
4. Configure CODEOWNERS for automatic reviewer assignment
5. Create issue and PR templates
6. Enable Dependabot or Renovate for dependency updates
7. Configure auto-merge workflow for dependency PRs
8. Set up release notes configuration

Run verification: `./scripts/verify-github-project.sh /path/to/repo`

### Branch Configuration

**Required branch settings:**

| Setting | Value | Rationale |
|---------|-------|-----------|
| Default branch name | `main` | Industry standard |
| Default branch protected | ✅ | Prevent direct pushes |
| Allowed merge method | **Merge commits only** | Preserve complete history |
| Delete branch on merge | ✅ | Keep repo clean |

To configure via GitHub CLI:

```bash
# Ensure default branch is named "main"
gh api repos/{owner}/{repo} --jq '.default_branch'

# Configure merge settings (merge commits only, delete on merge)
gh repo edit --enable-merge-commit --disable-rebase-merge --disable-squash-merge --delete-branch-on-merge
```

**Note:** If you prefer rebase merging for linear history, use `--enable-rebase-merge --disable-merge-commit` instead. Ensure consistency with any GitHub Rulesets (see [Rulesets Configuration](#github-rulesets-configuration)).

### Repository Settings

**Complete repository settings:**

| Setting | Value | Rationale |
|---------|-------|-----------|
| Allow merge commits | ✅ | With PR title and description |
| Allow squash merging | ❌ | Preserve commit granularity |
| Allow rebase merging | ❌ | Use merge queue instead |
| Automatically delete head branches | ✅ | Keep repo clean |
| Allow auto-merge | ✅ | Enable merge queue integration |
| Always suggest updating PR branches | ✅ | Keep PRs up-to-date with base |
| Discussions | ✅ | Community Q&A |
| Wikis | ❌ | Use docs folder instead |

**Configure via CLI:**

```bash
# Configure all repository settings
gh repo edit \
  --enable-merge-commit \
  --disable-squash-merge \
  --disable-rebase-merge \
  --delete-branch-on-merge \
  --enable-auto-merge \
  --enable-discussions \
  --disable-wiki

# Set merge commit message format (PR title and description)
gh api repos/{owner}/{repo} \
  --method PATCH \
  -f merge_commit_title=PR_TITLE \
  -f merge_commit_message=PR_BODY

# Enable "always suggest updating PR branches"
gh api repos/{owner}/{repo} \
  --method PATCH \
  -F allow_update_branch=true
```

**Important:** Do NOT enable `required_linear_history` when using merge commits. Linear history requires fast-forward merges only (no merge commits). If you see "not authorized to push" errors, check if `required_linear_history` is enabled and disable it.

### Renaming "master" to "main"

For complete migration steps from `master` to `main` as default branch, see `references/branch-migration.md`.

Quick start:
```bash
git branch -m master main
git push -u origin main
gh repo edit --default-branch main
git push origin --delete master
```

### Branch Protection Configuration

To configure branch protection via GitHub CLI:

```bash
# View current protection
gh api repos/{owner}/{repo}/branches/main/protection

# Set branch protection
gh api repos/{owner}/{repo}/branches/main/protection \
  --method PUT \
  -f required_status_checks='{"strict":true,"contexts":["test","lint"]}' \
  -f enforce_admins=true \
  -f required_pull_request_reviews='{"required_approving_review_count":1,"dismiss_stale_reviews":true,"require_code_owner_reviews":true}' \
  -f restrictions=null \
  -f required_conversation_resolution=true
```

**Recommended Settings:**
| Setting | Value | Purpose |
|---------|-------|---------|
| Require pull request | ✅ | Enforce code review |
| Required approvals | 1+ | Based on team size |
| Dismiss stale reviews | ✅ | Re-review after changes |
| Require CODEOWNERS review | ✅ | Domain expert review |
| Require conversation resolution | ✅ | All comments addressed |
| Do not allow force pushes | ✅ | Protect history |
| Allow merge commits | ✅ | Preserve complete history |
| Disable rebase merge | ✅ | Avoid linear-only restriction |
| Disable squash merge | ✅ | Preserve commit granularity |
| Delete branch on merge | ✅ | Auto-cleanup merged branches |

### GitHub Rulesets Configuration

GitHub Rulesets provide repository rules that can override or conflict with repository-level settings. **Critical:** The `pull_request` rule in rulesets has its own `allowed_merge_methods` setting that must match repository settings.

**View existing rulesets:**
```bash
# List all rulesets
gh api repos/{owner}/{repo}/rulesets

# Get specific ruleset details
gh api repos/{owner}/{repo}/rulesets/{ruleset_id}
```

**Common Issue: "Rebase is not an allowed merge method" Warning**

This warning appears on PRs when there's a mismatch between:
1. **Repository settings** (`allow_rebase_merge: false`)
2. **Ruleset settings** (`allowed_merge_methods` includes `"rebase"`)

**Diagnosis:**
```bash
# Check repository merge settings
gh api repos/{owner}/{repo} --jq '{allow_merge_commit, allow_rebase_merge, allow_squash_merge}'

# Check ruleset merge settings
gh api repos/{owner}/{repo}/rulesets/{ruleset_id} --jq '.rules[] | select(.type == "pull_request") | .parameters.allowed_merge_methods'

# Check merge queue settings
gh api repos/{owner}/{repo}/rulesets/{ruleset_id} --jq '.rules[] | select(.type == "merge_queue") | .parameters.merge_method'
```

**Fix: Update ruleset to match repository settings**

A PUT replaces every field it sends as a whole: a `rules` array holding only the two changed rules deletes all other rules of the ruleset, and GitHub rejects a `pull_request` or `merge_queue` rule that does not carry all of its required parameters. Read the ruleset, change the two fields, and send the full `rules` array back. The REST reference marks no top-level field of the PUT as required; that a field left out (`bypass_actors`, `conditions`) is kept is not tested here, so read the ruleset back.

For merge commits only:
```bash
gh api repos/{owner}/{repo}/rulesets/{ruleset_id} --jq '{rules: [.rules[]
    | if .type == "pull_request" then .parameters.allowed_merge_methods = ["merge"]
      elif .type == "merge_queue" then .parameters.merge_method = "MERGE"
      else . end
    | if .parameters == null then del(.parameters) else . end]}' \
  | gh api repos/{owner}/{repo}/rulesets/{ruleset_id} -X PUT --input -
# Read it back: the same rules and bypass actors as before, with the two fields changed
gh api repos/{owner}/{repo}/rulesets/{ruleset_id} --jq '{bypass_actors, conditions, rules}'
```

**Ruleset merge method alignment:**

| Repository Setting | Ruleset `allowed_merge_methods` | Ruleset `merge_queue.merge_method` |
|-------------------|--------------------------------|-----------------------------------|
| `allow_merge_commit: true` only | `["merge"]` | `"MERGE"` |
| `allow_rebase_merge: true` only | `["rebase"]` | `"REBASE"` |
| `allow_squash_merge: true` only | `["squash"]` | `"SQUASH"` |

### PR Comment Resolution Workflow

To enforce PR comment resolution:

1. Enable "Require conversation resolution" in branch protection
2. During review:
   - Reviewers leave line-specific comments
   - Author responds to each comment
   - Author clicks "Resolve conversation" after addressing
3. PR cannot merge until all conversations are resolved
4. Options for each thread:
   - "Resolve conversation" → Mark as addressed
   - Reply with explanation → Then resolve
   - "Won't fix" with reason → Then resolve

### Programmatic Review Thread Resolution (CRITICAL)

**IMPORTANT**: "Addressing" review comments means BOTH:
1. Fixing the code
2. **LITERALLY resolving** the thread via GitHub GraphQL API

The `gh` CLI does not support resolving review threads directly. Use GraphQL API.

**Step 1: Get unresolved review threads**
```bash
gh api graphql -f query='{
  repository(owner: "OWNER", name: "REPO") {
    pullRequest(number: NUMBER) {
      reviewThreads(first: 50) {
        nodes {
          id
          isResolved
          path
          line
          comments(first: 1) {
            nodes { body }
          }
        }
      }
    }
  }
}'
```

**Step 2: Resolve each thread by ID**
```bash
gh api graphql -f query='mutation {
  resolveReviewThread(input: {threadId: "PRRT_xxxxxxxxxxxx"}) {
    thread { isResolved }
  }
}'
```

**Step 3: Verify all threads resolved**
```bash
gh api graphql -f query='{
  repository(owner: "OWNER", name: "REPO") {
    pullRequest(number: NUMBER) {
      reviewThreads(first: 50) {
        nodes { id isResolved }
      }
    }
  }
}' | jq '.data.repository.pullRequest.reviewThreads.nodes | map(select(.isResolved == false))'
```

**PR Completion Checklist**:
- [ ] Code changes pushed and CI passing
- [ ] All review threads LITERALLY resolved via GraphQL API
- [ ] PR title and description updated to reflect final changes
- [ ] Added to merge queue or auto-merge enabled

### CODEOWNERS Setup

To configure automatic reviewer assignment:

1. Create `.github/CODEOWNERS`
2. Define ownership patterns (last matching pattern wins):

```
# Default owners for everything
* @org/maintainers

# Directory ownership
/src/auth/ @org/security-team
/docs/ @org/docs-team

# File pattern ownership
*.sql @org/dba-team
/.github/ @org/maintainers
```

3. Enable "Require review from CODEOWNERS" in branch protection

### Dependency Auto-Merge Setup

To configure automatic merging of dependency updates:

1. Configure Dependabot or Renovate (see `references/dependency-management.md`)
2. Create auto-merge workflow using appropriate template (see decision matrix below)
3. Workflow auto-approves and merges minor/patch updates
4. Major updates require manual review

**Auto-Merge Decision Matrix:**

| Repository Configuration | Template | Merge Method |
|--------------------------|----------|--------------|
| Merge queue enabled | `auto-merge-queue.yml.template` | GraphQL `enqueuePullRequest` |
| Branch protection (no queue) | `auto-merge.yml.template` | `gh pr merge --auto` |
| No branch protection | `auto-merge-direct.yml.template` | `gh pr merge --rebase` (direct) |

### Merge Queue Auto-Merge Setup

For repositories with merge queues enabled, the `--auto` flag and direct merge commands don't work. Use the GraphQL `enqueuePullRequest` mutation instead.

**Key points:**
- The `mergeMethod` parameter is NOT valid for `enqueuePullRequest` - merge method is set by queue configuration
- Use `github.event.pull_request.node_id` to get the PR's GraphQL node ID
- The mutation adds the PR to the queue; actual merge happens when queue processes it

```yaml
# .github/workflows/auto-merge-deps.yml
name: Auto-merge dependency PRs
on:
  pull_request_target:
    types: [opened, synchronize, reopened]

permissions:
  contents: write
  pull-requests: write

jobs:
  auto-merge:
    runs-on: ubuntu-latest
    if: github.actor == 'dependabot[bot]' || github.actor == 'renovate[bot]'
    steps:
      - name: Approve PR
        env:
          PR_URL: ${{ github.event.pull_request.html_url }}
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: gh pr review --approve "$PR_URL"

      - name: Add to merge queue
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          PR_NODE_ID: ${{ github.event.pull_request.node_id }}
        run: |
          gh api graphql -f query='
            mutation($pullRequestId: ID!) {
              enqueuePullRequest(input: {pullRequestId: $pullRequestId}) {
                mergeQueueEntry { id }
              }
            }' -f pullRequestId="$PR_NODE_ID"
```

### Direct Auto-Merge Setup (No Branch Protection)

For repositories without branch protection rules, the `--auto` flag fails with "Protected branch rules not configured". Use direct merge instead:

```yaml
# .github/workflows/auto-merge-deps.yml
- name: Merge PR
  env:
    PR_URL: ${{ github.event.pull_request.html_url }}
    GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
  run: gh pr merge --rebase "$PR_URL"
```

### Troubleshooting: Auto-Merge Failures

When auto-merge is enabled but PRs aren't merging automatically:

**Step 1: Check repo merge settings vs workflow merge method**
```bash
# View current merge method settings
gh api repos/{owner}/{repo} --jq '{
  allow_squash_merge,
  allow_merge_commit,
  allow_rebase_merge,
  delete_branch_on_merge
}'
```

**Step 2: Identify merge method mismatch**

| Workflow Uses | Repo Setting Required | Error Message |
|---------------|----------------------|---------------|
| `gh pr merge --squash` | `allow_squash_merge: true` | "Merge method squash merging is not allowed" |
| `gh pr merge --merge` | `allow_merge_commit: true` | "Merge method merge commit is not allowed" |
| `gh pr merge --rebase` | `allow_rebase_merge: true` | "Merge method rebase is not allowed" |

**Step 3: Fix merge method alignment**

Either update workflow to match repo settings (`gh pr merge --rebase`) or update repo:
```bash
gh api repos/{owner}/{repo} --method PATCH -f allow_rebase_merge=true
```

**Step 4: Validate required status checks**

Status check names must **exactly match** what workflows produce:
```bash
# Compare expected vs actual check names
gh api repos/{owner}/{repo}/branches/main/protection/required_status_checks --jq '.contexts[]'
gh pr checks <number> --json name --jq '.[].name'
```

**Common status check name mismatches:**

| Expected | Actual | Issue |
|----------|--------|-------|
| `Analyze (javascript-typescript)` | `Analyze (javascript)` | Language detection |
| `build` | `Build / build` | Workflow name prefix |
| `test` | `test (ubuntu-latest, 18)` | Matrix parameters |

**Step 5: Fix and re-trigger**
```bash
# Update branch protection check names
gh api repos/{owner}/{repo}/branches/main/protection/required_status_checks \
  --method PATCH -f strict=true --input - <<< '{"contexts":["actual-check-name"]}'

# Re-trigger stuck PRs
gh pr update-branch <number> --rebase
```

**Auto-merge compatibility checklist:**

| Check | Command | Expected |
|-------|---------|----------|
| Merge method alignment | `gh api repos/{owner}/{repo} --jq '.allow_rebase_merge'` | Matches workflow flag |
| Status checks pass | `gh pr checks <number>` | All green |
| Status check names match | Compare `gh pr checks` vs branch protection | Exact match |
| Reviews complete | `gh pr view <number> --json reviewDecision` | `APPROVED` |
| No merge conflicts | `gh pr view <number> --json mergeable` | `MERGEABLE` |
| Auto-merge enabled | `gh pr view <number> --json autoMergeRequest` | Not null |

### GitHub Discussions Setup

To enable Discussions:

1. Go to **Settings → Features → Discussions**
2. Create categories:
   - 📣 Announcements (maintainers only)
   - 💬 General
   - 💡 Ideas
   - 🙏 Q&A (Question/Answer format)
3. Add Discussions link to issue template chooser

**Use Discussions for:** Questions, ideas, announcements
**Use Issues for:** Bug reports, confirmed features, actionable tasks

### GitHub Releases Configuration

To configure automatic release notes:

1. Create `.github/release.yml`:

```yaml
changelog:
  exclude:
    authors: [dependabot, renovate]
  categories:
    - title: 🚀 Features
      labels: [enhancement]
    - title: 🐛 Bug Fixes
      labels: [bug]
    - title: 📚 Documentation
      labels: [documentation]
```

2. Create releases via CLI:

```bash
gh release create v1.0.0 --generate-notes
```

### Sub-Issues Configuration

GitHub's sub-issues feature enables parent-child relationships between issues (up to 8 levels, 100 sub-issues per parent). For complete GraphQL API reference, see `references/sub-issues.md`.

**Important:** The `gh` CLI does not support sub-issues directly. Use GraphQL API.

Quick reference:
```bash
# Get issue node ID
gh api graphql -f query='{repository(owner:"OWNER",name:"REPO"){issue(number:123){id}}}'

# Add sub-issue (requires node IDs)
gh api graphql -f query='mutation{addSubIssue(input:{issueId:"PARENT_ID",subIssueId:"CHILD_ID"}){issue{number}subIssue{number}}}'

# List sub-issues
gh api graphql -f query='{repository(owner:"OWNER",name:"REPO"){issue(number:123){subIssues(first:50){nodes{number title state}}}}}'
```

### Troubleshooting: PR Merge Blocked

When a PR cannot be merged, diagnose the cause:

**Step 1: Check PR status**
```bash
# View PR details including merge state
gh pr view <number> --json mergeable,mergeStateStatus,reviewDecision,statusCheckRollup

# Check for blocking issues
gh pr checks <number>
```

**Step 2: Identify the blocker**

| Symptom | Cause | Resolution |
|---------|-------|------------|
| `BLOCKED` mergeStateStatus | Unresolved conversations | Resolve all review threads |
| `REVIEW_REQUIRED` reviewDecision | Missing approvals | Request reviews from required reviewers |
| `CHANGES_REQUESTED` reviewDecision | Changes requested | Address feedback, request re-review |
| Failed checks in `statusCheckRollup` | CI/CD failures | Fix failing tests/lints |
| `CODEOWNERS review required` | Missing code owner approval | Get approval from designated owners |

**Step 3: Resolution actions**
```bash
# For unresolved conversations: view and resolve threads
gh pr view <number> --comments

# For missing reviews: request specific reviewers
gh pr edit <number> --add-reviewer username

# For CODEOWNERS blocking: check which files need review
gh pr view <number> --json files
```

**Common `gh pr merge` errors:**

| Error Message | Meaning | Fix |
|---------------|---------|-----|
| `Pull request is not mergeable` | Branch protection blocking | Run diagnosis steps above |
| `Required status check "X" is expected` | CI not run or pending | Wait for CI or trigger manually |
| `At least 1 approving review is required` | No approvals yet | Request and obtain review |
| `Changes were made after the most recent approval` | Stale approval | Request re-review |
| `Protected branch rules not configured` | `--auto` requires branch protection | Use direct merge or enable branch protection |
| `InputObject 'EnqueuePullRequestInput' doesn't accept argument 'mergeMethod'` | Invalid GraphQL parameter | Remove `mergeMethod` from mutation - it's set by queue config |

## Quick CLI Reference

```bash
# Repository
gh repo view
gh repo edit --enable-discussions

# Issues
gh issue list
gh issue create
gh issue edit 123 --add-label "priority: high"

# Pull requests
gh pr list
gh pr create
gh pr review --approve
gh pr merge --squash

# Releases
gh release create v1.0.0 --generate-notes

# Labels
gh label create "name" --color "hex" --description "desc"

# Projects
gh project create --title "Project Name"
```

## Resources

| Resource | Purpose |
|----------|---------|
| `references/repository-structure.md` | Standard files and directory layout |
| `references/dependency-management.md` | Dependabot/Renovate and auto-merge patterns |
| `references/sub-issues.md` | GitHub sub-issues GraphQL API |
| `references/branch-migration.md` | Master to main migration guide |
| `assets/auto-merge.yml.template` | Auto-merge with branch protection (--auto flag) |
| `assets/auto-merge-queue.yml.template` | Auto-merge with merge queue (GraphQL mutation) |
| `assets/auto-merge-direct.yml.template` | Auto-merge without branch protection |
| `scripts/verify-github-project.sh` | Verification script for project setup |

## Related Skills

This skill focuses on GitHub platform configuration. For complete project setup:

| Skill | Purpose |
|-------|---------|
| `go-development` | Go code patterns, Makefile interface, testing, linting |
| `enterprise-readiness` | OpenSSF Scorecard, SLSA provenance, signed releases, CI workflow templates |
| `git-workflow` | Git branching strategies, conventional commits |
| `security-audit` | Deep security audits (OWASP, CVE analysis) |

### Skill Coordination

```
github-project (this skill)
├── Repository configuration
├── Branch protection / rulesets
├── Dependabot/Renovate auto-merge
└── Coordinates with:
    ├── go-development → CI workflow content (test, lint, build)
    └── enterprise-readiness → Security workflows (Scorecard, CodeQL, SLSA)
```

## Tests

The behavioural tests live in `tests/` and run offline; they need bash, git, jq, python3 and the usual coreutils, grep and sed:

```bash
bash tests/verify-github-project.sh    # skills/github-project/scripts/verify-github-project.sh
bash tests/init-branch-protection.sh   # skills/github-project/scripts/init-branch-protection.sh
bash tests/check-plugin-version.sh     # Build/Scripts/check-plugin-version.sh and Build/hooks/pre-push
bash tests/checkpoint-gh-37.sh         # checkpoint GH-37 in skills/github-project/checkpoints.yaml
```

- `tests/verify-github-project.sh` runs the verifier against fixture directories; only the dotted-name fixture has a github.com `origin`, and the three remote fixtures run with a stub `gh` on `PATH`, so no fixture reaches the network. The stub checks that a non-GitHub remote and a host that merely contains `github.com` trigger no call and that a github.com remote whose name contains a dot is queried with its slug. It checks the exit codes, that all 12 sections run, and individual pass and failure lines, including the default-branch check in a git repository.
- `tests/init-branch-protection.sh` puts a stub `gh` first on `PATH` that answers from prepared responses and records every request and request body. It checks each exit code documented in the script header, the body sent with `PUT` (with and without `--solo`), that nothing is written over protection the script could not read, that drift is reported and not corrected, both `--from-current-checks` paths (with `strict` false under a merge queue), and `--merge-queue`: the ruleset body and its read-back, the strict PATCH, the `allow_auto_merge` PATCH and its read-back, the no-op on an existing standard queue, and each refusal, including a required `Analyze (…)` context under CodeQL default setup (allowed without default setup and as a workflow-prefixed `codeql / Analyze (…)`) and `"app_id": -1` for unpinned contexts in the printed PATCH.
- `tests/check-plugin-version.sh` builds throwaway git repositories and checks that a semver tag at `HEAD` must match the version in `.claude-plugin/plugin.json`, and that the pre-push hook passes the result on.
- `tests/checkpoint-gh-37.sh` reads GH-37's script out of `checkpoints.yaml` and runs it in fixture directories: the org preset as `github>` or `local>` (with `:preset` or `#ref`, in JSON, JSONC or JSON5) and a repository without a Renovate config pass; `config:recommended` alone, the preset only in a comment, a `description` or `ignorePresets`, a look-alike repository name, a missing `extends`, and a preset in a later config file than the one Renovate reads fail.

Each check prints `ok` or `FAIL`; a `FAIL` line names the expectation that was not met and is followed by the script's output. A test file exits 1 when any check failed. In CI, the Skill Tests workflow (`.github/workflows/tests.yml`) runs every `tests/**/*.sh` on each pull request and on pushes to `main`, and fails when the repository ships scripts under `skills/*/scripts/` but no test ran.

The skill's Markdown and templates are not executed here; Skill Validation and Eval Validation check their structure and the eval definitions in `skills/github-project/evals/evals.json`. A pull request that adds or changes behaviour in a script adds or updates a check in `tests/` that fails without the change.

## Governance and policies

This repository follows the Netresearch organisation policies:

- [Governance](https://github.com/netresearch/.github/blob/main/GOVERNANCE.md): ownership, roles, how decisions are made and disputes resolved, and continuity.
- [Roadmap](https://github.com/netresearch/.github/blob/main/ROADMAP.md): planned and explicitly excluded work for the coming year.
- [Handling of dependency and code analysis findings](https://github.com/netresearch/.github/blob/main/SECURITY.md#handling-of-dependency-and-code-analysis-findings): thresholds, deadlines and the exception process for dependency (SCA) and static analysis (SAST) findings.
- [Secret management](https://github.com/netresearch/.github/blob/main/SECURITY.md#secret-management): how CI and release credentials are stored, accessed and rotated.
- [Access roster](https://github.com/netresearch/.github/blob/main/docs/access-roster.md): who holds administrative access to this repository and the organisation.

The security assurance case for this skill (threat model, trust boundaries, countermeasures and limits) is in [docs/SECURITY-ASSURANCE.md](docs/SECURITY-ASSURANCE.md).

Checks that run on pull requests in this repository:

- Every pull request: Skill Validation (`lint.yml`: skill structure, markdownlint, yamllint, actionlint, JSON syntax, ShellCheck, ruff, checkpoint schema), Eval Validation (`eval-validate.yml`) and Skill Tests (`tests.yml`).
- Pull requests to `main`: `security.yml` with Betterleaks (secret scanning), zizmor (workflow static analysis), dependency review, Composer Audit and Opengrep SAST (both behind a preflight event-gate job), and CodeQL for `actions`; Harness Verification (`harness-verify.yml`) and Template Drift (`check-template-drift.yml`). The organisation's security policy sets when dependency review and Opengrep fail: see [dependencies](https://github.com/netresearch/.github/blob/main/SECURITY.md#dependencies-software-composition-analysis) and [static analysis (SAST)](https://github.com/netresearch/.github/blob/main/SECURITY.md#static-analysis-sast).
- Also on every pull request: Labeler (`labeler.yml`), the DCO sign-off check, SonarCloud Code Analysis and the CodeRabbit review status (GitHub Apps) and, for dependency-update pull requests, auto-merge (`auto-merge-deps.yml`).

## License

This project uses split licensing:

- **Code** (scripts, workflows, configs): [MIT](LICENSE-MIT)
- **Content** (skill definitions, documentation, references): [CC-BY-SA-4.0](LICENSE-CC-BY-SA-4.0)

See the individual license files for full terms.

---

**Made with ❤️ for Open Source by [Netresearch](https://www.netresearch.de/)**

## Verification

To check GitHub project configuration:

```bash
./skills/github-project/scripts/verify-github-project.sh /path/to/repository
```

Checks: documentation files, CODEOWNERS, dependency management, issue/PR templates, auto-merge workflow, release configuration.



--- FILE: docs/ARCHITECTURE.md ---

<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->
<!-- SPDX-FileCopyrightText: Netresearch DTT GmbH -->

# Architecture Overview

## Purpose

The github-project-skill is an Agent Skill package that provides GitHub platform configuration knowledge to AI agents (Claude Code, Cursor, GitHub Copilot, and other skills-compatible agents).

## Skill Structure

```
skills/github-project/
├── SKILL.md              # Skill entry point — loaded by agents at activation
├── checkpoints.yaml      # Verification checkpoints for skill validation
├── evals/evals.json      # Evaluation test cases
├── references/           # Deep-dive reference documents (linked from SKILL.md/README)
├── assets/               # Workflow and config templates (*.template files)
└── scripts/              # verify-github-project.sh — checks a repo's GH config
```

## How It Works

1. **Agent activation**: An AI agent loads `SKILL.md` when GitHub project configuration tasks are detected (PR merge issues, branch protection, auto-merge, etc.).
2. **Knowledge delivery**: SKILL.md contains quick diagnostics and decision trees. For deeper topics, it references files in `references/`.
3. **Templates**: The `assets/` directory provides copy-paste workflow templates (auto-merge variants, PR quality gates, issue templates, etc.).
4. **Verification**: `scripts/verify-github-project.sh` audits a target repository against recommended GitHub project standards.

## Distribution Channels

- **Composer**: `netresearch/github-project-skill` via `composer.json` (requires `composer-agent-skill-plugin`)
- **npm**: `github:netresearch/github-project-skill` via `package.json` (requires `@netresearch/agent-skill-coordinator`, which discovers the skill in `node_modules` and registers it in `AGENTS.md` via a `postinstall` hook)
- **Claude Code plugin**: `.claude-plugin/plugin.json` for marketplace distribution
- **npx / skills.sh**: Direct install via `npx skills add`
- **Git clone / release download**: Manual installation

When making changes to release or distribution logic, all five channels must be considered. The npm channel ships from a `package.json` allowlist (`files: ["skills/github-project/", "LICENSE-MIT", "LICENSE-CC-BY-SA-4.0", "README.md"]`) — anything outside that allowlist is invisible to npm consumers.

## Key Design Decisions

- **Platform-only scope**: This skill handles GitHub platform features. CI/CD content, language tooling, and security scanning are delegated to dedicated skills.
- **Three auto-merge patterns**: Merge queue (GraphQL), branch protection (`--auto`), and direct merge each have separate templates because they require fundamentally different GitHub API interactions.
- **GraphQL for thread resolution**: GitHub REST API and `gh` CLI lack PR review thread resolution support, so the skill teaches GraphQL mutations.
- **Split licensing**: Code (MIT) and content (CC-BY-SA-4.0) are licensed separately to allow flexible reuse.



--- FILE: docs/SECURITY-ASSURANCE.md ---

<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->
<!-- SPDX-FileCopyrightText: Netresearch DTT GmbH -->

# Security assurance case — github-project-skill

This document states what a user can expect from this repository in terms of security, and argues why that expectation holds. Every claim names the file that implements it. Reporting a vulnerability: see the [security policy](https://github.com/netresearch/.github/blob/main/SECURITY.md). Components: [ARCHITECTURE.md](ARCHITECTURE.md).

## What the repository ships

| Part | Files | Runs where |
| --- | --- | --- |
| Skill instructions for an AI agent | `skills/github-project/SKILL.md`, `skills/github-project/references/*.md` | Read by the agent as instructions; not executed. The agent may run the `gh` and `git` commands they describe against the user's repositories. |
| Templates | `skills/github-project/assets/*.template` | Copied by the user or the agent into the user's repository; they run there as that repository's workflows and configuration. |
| Scripts | `skills/github-project/scripts/init-branch-protection.sh`, `skills/github-project/scripts/verify-github-project.sh` | On the user's machine, with the user's `gh` authentication. |
| Checkpoints | `skills/github-project/checkpoints.yaml` | Only when an assessment tool runs its `command` and `script` patterns in a user's project. |
| Repository checks | `Build/Scripts/check-plugin-version.sh`, `Build/hooks/pre-push`, `scripts/verify-harness.sh`, `tests/*.sh` | In this repository's CI and on contributors' machines. |

The repository ships no server component and no container image. It stores nothing and handles no user accounts or credentials of its own; the scripts use whatever token `gh` is authenticated with.

## Security requirements

1. `init-branch-protection.sh` changes branch protection only in the ways its header documents, and never overwrites protection it could not read.
2. `verify-github-project.sh` and the checkpoints only read: they change no file in the assessed project and send no write request to GitHub.
3. The skill content and templates recommend GitHub settings and workflows that do not hand pull request code a write token or secrets, and that require review before merge.
4. Nothing committed to this repository contains a secret.
5. A release carries the version that `.claude-plugin/plugin.json` states, and its archives can be verified against the build that produced them.

## Actors and trust boundaries

- **Skill user and agent.** The agent reads `SKILL.md` and the references and runs `gh`/`git` commands with the user's GitHub authentication. What it runs is decided by the agent and the user, not by this repository. `allowed-tools` in `SKILL.md` only pre-approves `gh`, `git`, `grep`, `Read` and `Write`; it does not take any tool away from the agent.
- **GitHub API.** Both scripts talk to GitHub only through `gh api`. Responses are treated as data: `init-branch-protection.sh` parses them with `jq` and builds request bodies with `jq --argjson` and `jq -R`, not by string concatenation.
- **Assessed repository.** `verify-github-project.sh` reads files in the directory it is given and, when the checkout's `origin` points at github.com, reads that repository's settings through the API. `checkpoints.yaml` patterns run in the assessed project's working directory with the privileges of whoever starts the assessment tool.
- **Contributors.** Changes reach `main` through pull requests, checked by the workflows in `.github/workflows/`. `.envrc` (used by direnv) sets `core.hooksPath` to `Build/hooks`, so a contributor who allows it runs the repository's `pre-push` hook.
- **CI.** Workflows run on GitHub-hosted runners with `permissions: {}` at the top level and grant each job only the scopes its called reusable workflow needs (`.github/workflows/*.yml`). The two `pull_request_target` workflows (`auto-merge-deps.yml`, `labeler.yml`) only call reusables that merge or label and do not check out pull request code; `auto-merge-deps.yml` passes two named secrets instead of `secrets: inherit`.

## Threats and countermeasures

| Threat | Countermeasure | Evidence |
| --- | --- | --- |
| A malformed or hostile `<owner>/<repo>` argument reaches the API path or the shell (CWE-20, CWE-78) | The slug must match `^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$`, the mode must be one of four fixed values; every variable is quoted | `init-branch-protection.sh` (argument parsing); `tests/init-branch-protection.sh` ("slug with shell metacharacters exits 2") |
| Existing branch protection is replaced by the template after a failed read, clearing required status checks | Only GitHub's explicit "Branch not protected" answer leads to a PUT; any other read error, or a successful answer without a `url` field, exits 3 without writing | `init-branch-protection.sh` (lines after "Check whether protection already exists"); `tests/init-branch-protection.sh` ("unreadable protection is not overwritten", "unexpected protection response is not overwritten") |
| An administrator's deliberate protection settings are silently reverted | On existing protection the script compares the fields the template sets, prints each difference and exits 1 without writing | `init-branch-protection.sh` (`check_field`); `tests/init-branch-protection.sh` ("drift is not corrected") |
| Adding required status checks drops other protection settings | `--from-current-checks` PATCHes only the `required_status_checks` subresource when it exists, and otherwise re-sends every field of the current protection | `init-branch-protection.sh` (`--from-current-checks` mode); `tests/init-branch-protection.sh` ("approval count is carried over", "enforce_admins is carried over") |
| Enabling the merge queue rewrites an existing ruleset, or leaves a queue no entry can pass | `--merge-queue` only creates a new ruleset and never PUTs an existing one; it reads the rules and protection first and exits without writing on an unreadable state (3), a drifted queue or a ruleset requiring up-to-date branches (1), or a required context that never reports on `merge_group` (6), including `Analyze (…)` under CodeQL default setup, or a `code_scanning` rule for CodeQL under default setup, which blocks every fork pull request (6); the created ruleset and the `allow_auto_merge` it sets are read back | `init-branch-protection.sh` (`--merge-queue` mode); `tests/init-branch-protection.sh` ("a drifted queue is not corrected", "a required app context gets no write", "a required default-setup Analyze context gets no write", "a ruleset read back without the queue exits 1", "a drifted queue does not get auto-merge allowed either", "allow_auto_merge read back as false exits 1") |
| A failed check is made a required status check, or checks are taken from an incomplete run | Only check-runs with conclusion `success` are used; a combined status other than `success` is reported as a warning | `init-branch-protection.sh`; `tests/init-branch-protection.sh` ("only successful check-runs, deduplicated, are required") |
| An audit reports a result that does not reflect the repository | `verify-github-project.sh` runs every section and fails when a required item is missing; the GitHub API part is skipped, and says so, when there is no github.com remote | `verify-github-project.sh`; `tests/verify-github-project.sh` |
| Pull request code runs with a write token or secrets in a user's repository (CWE-829) | The auto-merge and auto-approve templates use `pull_request_target` without checking out pull request code, gate on `github.event.pull_request.user.login`, and set explicit `permissions`; `pr-quality.yml.template` states that a checkout must not be added | `assets/auto-merge*.yml.template`, `assets/pr-quality.yml.template` |
| Merges bypass review or leave review threads unresolved | The branch protection template requires one approval and conversation resolution and forbids force pushes and deletions; checkpoints GH-30 and GH-31 read the protection back | `assets/branch-protection.json.template`, `checkpoints.yaml` |
| A reusable workflow or action is changed underneath its callers, or receives more secrets than it needs | The references explain SHA pinning of third-party actions and composite-action refs, transitive action risks, and passing named secrets instead of `secrets: inherit`; checkpoint GH-34 flags unpinned composite-action refs | `references/reusable-workflow-security.md`, `references/reusable-workflow-pitfalls.md`, `checkpoints.yaml` (GH-34) |
| A checkpoint modifies the assessed project | Every checkpoint is a file-existence, content or regex check, a `gh api` GET, or a shell/Python body that only reads files and exits with a status; none writes a file or sends a write request | `checkpoints.yaml` |
| A release is tagged with a version that disagrees with `plugin.json` | The pre-push hook runs `check-plugin-version.sh`, which fails when a semver tag at `HEAD` differs from `.claude-plugin/plugin.json` | `Build/hooks/pre-push`, `Build/Scripts/check-plugin-version.sh`; `tests/check-plugin-version.sh` |
| A released archive is tampered with | The release workflow publishes a Cosign-signed `SHA256SUMS.txt` and build-provenance attestations for the archives | `.github/workflows/release.yml` (calls the skill-repo-skill release reusable) |
| A secret is committed | Betterleaks scans every push to `main` and every pull request to `main` | `.github/workflows/security.yml` |
| A vulnerable or malicious dependency is added | Dependency review checks the dependencies a pull request adds or changes against known vulnerabilities; Composer Audit checks the Composer dependencies against known advisories; Renovate proposes updates, including pre-commit hook revisions | `.github/workflows/security.yml`, `renovate.json` |
| Insecure code or workflow patterns | Opengrep scans the code for insecure patterns; zizmor analyses the workflows; ShellCheck runs on every `*.sh` file in Skill Validation | `.github/workflows/security.yml`, `.github/workflows/lint.yml` |
| A failing step continues with partial state | `init-branch-protection.sh`, `check-plugin-version.sh` and `verify-harness.sh` run with `set -euo pipefail`; `verify-github-project.sh` runs with `set -e` and counts results without commands that can fail | the scripts named |

Which of these checks must pass before a pull request can merge is set in the branch protection of `main`, not in this repository.

## Secure design principles applied

- **Least privilege:** the scripts send only the requests their mode needs; `verify-github-project.sh` sends none that write. Workflows here and in the templates start from explicit `permissions`.
- **Fail-safe defaults:** `init-branch-protection.sh` writes only when it has positively established the current state, and treats every other outcome as an error (exit codes 1 to 6 in its header).
- **Complete mediation of input:** arguments are validated before the first API call; API data enters request bodies through `jq`, never through the shell.
- **Economy of mechanism:** the scripts need bash, `gh`, `jq` and `git` and nothing else.

## What a user cannot expect

- The skill gives guidance; it does not enforce it. The agent runs `gh` with the user's token, and a token with admin rights can change any setting the references describe. Review what an agent proposes to run.
- `init-branch-protection.sh` writes branch protection with the user's token; it is not a dry run. Its baseline leaves `enforce_admins` off, so administrators can still bypass the protection until they enable it.
- The templates are examples to adapt. Some reference third-party actions by version tag (for example `step-security/harden-runner@v2`) rather than by commit SHA.
- `verify-github-project.sh` checks the presence of files and settings, not their content in depth, and reads the settings of whatever repository the checkout's `origin` points at.
- The checkpoints run shell commands in the assessed project when an assessment tool executes them; run them only in projects you trust. The LLM review checkpoints are judgements by a model and can miss issues.
- Security fixes follow the supported-versions rules of the organisation's security policy; older releases may not receive them.



--- FILE: skills/github-project/SKILL.md ---

---
# SPDX-License-Identifier: CC-BY-SA-4.0
# SPDX-FileCopyrightText: Netresearch DTT GmbH
name: github-project
description: "Use when bootstrapping a repo (apply branch protection before first PR), PRs won't merge or BLOCKED, AI reviewer pushback, auto-merge fails for Dependabot/Renovate, branch protection or rulesets, CI fails, authoring or consuming reusable workflows, editing a repo's own .github/workflows, harden-runner, or CODEOWNERS/PR templates."
license: "(MIT AND CC-BY-SA-4.0). See LICENSE-MIT and LICENSE-CC-BY-SA-4.0"
compatibility: "Requires gh CLI, git."
metadata:
  author: Netresearch DTT GmbH
  version: "2.22.2"
  repository: https://github.com/netresearch/github-project-skill
allowed-tools: Bash(gh:*) Bash(git:*) Bash(grep:*) Read Write
---

# GitHub Project Skill

## When to Use

- **Post `gh repo create` + push, before first PR** — REQUIRED: `scripts/init-branch-protection.sh OWNER/REPO`
- **First issue/PR into a foreign repo** — `references/upstream-contributions.md` BEFORE filing
- Adding a workflow job — pitfall #6
- PR won't merge / threads
- Auto-merge fails (Dependabot/Renovate)
- Solo auto-approve
- Branch protection, rulesets
- GHA failures
- Signed-commit merge
- CodeQL
- Scorecard
- CODEOWNERS, templates, labels
- Fork PR merge base

## Quick Diagnostics

### PR Won't Merge

```bash
gh pr view PR --repo OWNER/REPO \
  --json mergeStateStatus,reviewDecision,mergeable,reviewThreads
```

### Solo Maintainer: Stuck on REVIEW_REQUIRED

First preserve the documented review contract (`references/review-policy-contract.md`). For an authorized solo-maintainer setup, either `assets/pr-quality.yml.template` (auto-approve, approvals >= 1) or `scripts/init-branch-protection.sh OWNER/REPO --solo` (approvals 0, conversation resolution kept) — `references/auto-merge-guide.md` compares both.

### Auto-merge Setup

Requires `allow_auto_merge`, `pull_request_target`, bot detection, `gh pr merge --auto` (`references/auto-merge-guide.md`).

### Auto-merge Not Working

```bash
gh pr view PR --repo OWNER/REPO --json autoMergeRequest --jq .autoMergeRequest
```

Bypass actors: `references/security-config.md`.

### GitHub Actions Failing

```bash
gh run list --repo OWNER/REPO --limit 5
gh run view RUN_ID --repo OWNER/REPO --log-failed
gh run rerun RUN_ID --repo OWNER/REPO
```

**"CI failed on main" can be a fork PR.** A run's branch is the head branch, so a fork PR from a branch named `main` shows up as `main` in notifications and in `gh run list --branch main`. Its `pull_requests` array is empty. Before treating your `main` as red, read `event` and `head_repository`: `pull_request` from another repository is that PR's failure.

```bash
gh api repos/OWNER/REPO/actions/runs/RUN_ID \
  --jq '{event, head_branch, head_repo: .head_repository.full_name}'
```

### Security Quick Checks

```bash
gh api repos/OWNER/REPO/rules/branches/main
gh api repos/OWNER/REPO/branches/main/protection \
  --jq '{rcr: .required_conversation_resolution.enabled, admins: .enforce_admins.enabled}'
gh api repos/OWNER/REPO/code-scanning/default-setup --jq '.state'
gh pr view PR --repo OWNER/REPO --json reviewThreads --jq '.reviewThreads'
```

### Merge Strategy Issues

`references/auto-merge-guide.md`: signed-commit rebase, workflow-file PRs, Copilot race.

### Calling Organisation Reusables

**Rule:** `uses: netresearch/<repo>/.github/workflows/<name>.yml@main`. Never a commit hash, also not `@<sha> # main`; third-party actions stay SHA-pinned. A CodeQL `actions/unpinned-tag`, zizmor or SonarCloud finding on such a line is dismissed as won't fix, never fixed by pinning. Why: `references/reusable-workflow-security.md`.

## Running Scripts

```bash
scripts/init-branch-protection.sh OWNER/REPO              # baseline
scripts/init-branch-protection.sh OWNER/REPO --from-current-checks   # after first CI
scripts/init-branch-protection.sh OWNER/REPO --merge-queue    # then: org-standard queue
scripts/verify-github-project.sh /path/to/repository      # local-checkout audit
```

## No editorializing

State what a change does, not how good it is.

## References

| Topic | Reference |
|-------|-----------|
| Repo bootstrap | `references/repo-bootstrap.md` |
| Repository file layout | `references/repository-structure.md` |
| Branch migration | `references/branch-migration.md` |
| Repository retirement, Packagist abandon | `references/repo-retirement.md` |
| Dependabot/Renovate | `references/dependency-management.md` |
| Auto-approve + auto-merge | `references/auto-merge-guide.md` |
| Merge strategy | `references/merge-strategy.md` |
| Sub-issues | `references/sub-issues.md` |
| Release labeling | `references/release-labeling.md` |
| gh CLI commands | `references/gh-cli-reference.md` |
| Polyglot CI checklists | `references/repo-setup-guide.md` |
| Scorecard, CodeQL, security | `references/security-config.md` |
| Qualified human approvals, actual base, stacked PR guard | `references/review-policy-contract.md` |
| actionlint | `references/actionlint-guide.md` |
| Actions upgrades, Node-runtime wave | `references/actions-upgrade-guide.md` |
| Workflow bash pitfalls | `references/workflow-bash-patterns.md` |
| Runner capacity, concurrency groups (schedule vs push) | `references/ci-runner-capacity.md`, `scripts/collect-runner-capacity.py` |
| No editorializing | `references/no-editorializing.md` |
| Fork merge base | `references/pr-commit-cleanup.md` |
| Multi-repo batch ops | `references/multi-repo-operations.md` |
| Private copy of a public repo (mirror push) | `references/multi-repo-operations.md` |
| Cross-repo references, code permalinks | `references/cross-repo-references.md` |
| Foreign-repo contributions | `references/upstream-contributions.md` |
| Reusable workflow security | `references/reusable-workflow-security.md` |
| Reusable workflow pitfalls | `references/reusable-workflow-pitfalls.md` |
| Org security settings | `references/org-security-settings.md` |
| Tag validation | `references/tag-validation.md` |
| AI reviewer pushback | `references/ai-reviewer-pushback.md` |
| Agentic workflows | `references/agentic-workflows.md` |
| Pages + data collectors | `references/pages-and-collector-workflows.md` |

---

> Contributing: https://github.com/netresearch/github-project-skill



--- FILE: skills/github-project/references/actionlint-guide.md ---

<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->
<!-- SPDX-FileCopyrightText: Netresearch DTT GmbH -->

# actionlint - GitHub Actions Workflow Linter

Static analysis tool for GitHub Actions workflow files. Catches syntax errors, type mismatches, deprecated features, and security issues before pushing to CI.

**Repository:** https://github.com/rhysd/actionlint

## Installation

```bash
# Go install
go install github.com/rhysd/actionlint/cmd/actionlint@latest

# Homebrew
brew install actionlint

# Download binary (Linux)
curl -sL https://github.com/rhysd/actionlint/releases/latest/download/actionlint_linux_amd64.tar.gz | tar xz -C /usr/local/bin actionlint

# Docker
docker run --rm -v "$(pwd):/repo" -w /repo rhysd/actionlint:latest
```

## Command-Line Usage

```bash
# Lint all workflows in .github/workflows/
actionlint

# Lint a specific file
actionlint .github/workflows/ci.yml

# Colored output (auto-detects terminal)
actionlint -color

# JSON output (for CI pipelines and editors)
actionlint -format '{{json .}}'

# SARIF output (for GitHub Code Scanning)
actionlint -format sarif > actionlint.sarif

# Verbose output (shows checked files)
actionlint -verbose

# Ignore specific rules
actionlint -ignore 'SC2086'           # Ignore shellcheck rule
actionlint -ignore 'label "self-hosted"'  # Ignore runner label warning

# Specify shellcheck binary path
actionlint -shellcheck /usr/local/bin/shellcheck

# Disable shellcheck integration
actionlint -shellcheck=

# Disable pyflakes integration
actionlint -pyflakes=

# Stdin mode (pipe workflow content)
cat .github/workflows/ci.yml | actionlint -stdin-filename ci.yml -
```

## Flag Reference

| Flag | Description |
|------|-------------|
| `-color` | Force colored output |
| `-no-color` | Disable colored output |
| `-format <template>` | Custom output format (Go template) |
| `-ignore <pattern>` | Regex pattern for errors to ignore (repeatable) |
| `-shellcheck <path>` | Path to shellcheck binary (empty to disable) |
| `-pyflakes <path>` | Path to pyflakes binary (empty to disable) |
| `-stdin-filename <name>` | Filename for stdin input |
| `-verbose` | Show verbose output |
| `-debug` | Show debug output |
| `-oneline` | One-line compact output |
| `-config-file <path>` | Path to configuration file |

## Configuration File

Create `.github/actionlint.yaml` in the repository root (auto-detected):

```yaml
# .github/actionlint.yaml

# Define custom runner labels your org uses
self-hosted-runner:
  labels:
    - linux-large
    - ubuntu-24.04-16core
    - arm64

# Patterns of errors to ignore (regex)
ignore:
  # Ignore shellcheck SC2086 (double quote to prevent globbing)
  - 'SC2086'
  # Ignore specific expression warnings
  - 'label "self-hosted" is unknown'

# Configure paths (available since actionlint 1.7+)
paths:
  shellcheck: /usr/local/bin/shellcheck
  pyflakes: ""  # disable pyflakes
```

### Configuration for Common Project Types

**TYPO3 Extension:**
```yaml
self-hosted-runner:
  labels: []
ignore:
  - 'SC2086'  # phpunit commands often need unquoted vars
```

**Go Project:**
```yaml
self-hosted-runner:
  labels: []
ignore: []
```

**Monorepo with Custom Runners:**
```yaml
self-hosted-runner:
  labels:
    - linux-large
    - gpu-runner
    - arm64-builder
ignore:
  - 'label "linux-large" is unknown'
```

## Common Error Codes and Fixes

### Expression Syntax Errors

```
Error: unexpected token "}" while parsing
```
**Cause:** Malformed `${{ }}` expression.
**Fix:** Check for unbalanced braces, missing operators, or invalid function calls.

```yaml
# Bad
if: ${{ github.event_name == 'push' && }}

# Good
if: ${{ github.event_name == 'push' }}
```

### Undefined Action Inputs/Outputs

```
Error: input "node-versions" is not defined in action "actions/setup-node@v4"
```
**Cause:** Typo in action input name.
**Fix:** Check the action's `action.yml` for correct input names.

```yaml
# Bad
- uses: actions/setup-node@v4
  with:
    node-versions: '22'  # wrong: plural

# Good
- uses: actions/setup-node@v4
  with:
    node-version: '22'   # correct: singular
```

**Local actions always, remote actions only if actionlint knows them.** A local action (`uses: ./.github/actions/foo`) is read from the repository, so its `with:` block is fully checked — a bogus input reports `input "bogus_input" is not defined in action "local" defined at "./.github/actions/local"` and exits 1. A remote action is checked against a bundled metadata set of popular actions (`actions/*`, `docker/*` and similar); for a remote action outside that set the `with:` block is unchecked, and an input the action does not declare is accepted silently.

Measured, 2026-09-07, TYPO3-Documentation/t3docs-ci-deploy: a step passed `script:` to `appleboy/scp-action`, which has no such input. The action tarred its empty `source` and failed on every invocation for six months; `actionlint` on that file exits 0. So a green actionlint says nothing about an unknown remote action's `with:` block — read the pinned metadata file when a step is not doing what its inputs say (GitHub accepts both spellings, so try `action.yml` and fall back to `action.yaml`):

```bash
for f in action.yml action.yaml; do
  gh api "repos/<owner>/<action>/contents/$f?ref=<sha>" --jq .content 2>/dev/null | base64 -d && break
done
```

What it *does* check on every file is expression syntax. That part is worth trusting: breaking one quote in `${{ toJSON(format('{0}', x)) }}` reports `unexpected EOF while lexing end of string literal [expression]` and exits 1.

### YAML Type Errors

```
Error: "permissions" section should be mapping
```
**Cause:** Wrong YAML structure for permissions block.
**Fix:** Use mapping syntax, not sequence.

```yaml
# Bad
permissions:
  - contents: read

# Good
permissions:
  contents: read
```

### Deprecated Action Versions

```
Error: the runner of "ubuntu-18.04" is no longer supported
```
**Cause:** Using a deprecated runner image.
**Fix:** Update to a supported runner version.

```yaml
# Bad
runs-on: ubuntu-18.04

# Good
runs-on: ubuntu-24.04
```

### Missing Permissions Declarations

actionlint checks that workflow-level or job-level `permissions` are set when using `GITHUB_TOKEN`. This aligns with the principle of least privilege.

```yaml
# Add explicit permissions
permissions:
  contents: read
  pull-requests: write
```

### ShellCheck Issues in run: Blocks

```
Error: shellcheck reported issue in this script: SC2086
```
**Cause:** ShellCheck found an issue in a `run:` block. actionlint embeds shellcheck analysis for bash/sh scripts.
**Fix:** Follow the shellcheck recommendation, or ignore with inline directive.

```yaml
# Fix: quote the variable
- run: echo "$MY_VAR"

# Or ignore inline (not recommended)
- run: |
    # shellcheck disable=SC2086
    echo $MY_VAR
```

### Context/Object Property Access

```
Error: property "conclusion" is not defined in object type "steps"
```
**Cause:** Accessing a step output without using the step ID.
**Fix:** Use `steps.<step-id>.outputs.<name>` or `steps.<step-id>.conclusion`.

```yaml
steps:
  - id: build
    run: echo "done"
  - if: steps.build.conclusion == 'success'
    run: echo "Build succeeded"
```

## ShellCheck Integration

actionlint embeds [ShellCheck](https://www.shellcheck.net/) to analyze shell scripts in `run:` blocks. This provides:

- Variable quoting warnings (SC2086)
- Unused variable detection (SC2034)
- Command injection risks (SC2091)
- Bash-specific syntax issues

**How it works:**
1. actionlint extracts `run:` block content
2. Detects shell type from `shell:` key (defaults to `bash`)
3. Runs shellcheck on the extracted script
4. Maps errors back to workflow file line numbers

**Controlling shellcheck rules:**

```yaml
# Per-block: use shellcheck directives
- run: |
    # shellcheck disable=SC2086,SC2034
    echo $UNQUOTED_VAR

# Globally: ignore in actionlint config
# .github/actionlint.yaml
ignore:
  - 'SC2086'

# Disable shellcheck entirely
# Run: actionlint -shellcheck=
```

**Common shellcheck rules in workflows:**

| Rule | Description | Fix |
|------|-------------|-----|
| SC2086 | Double quote to prevent globbing | `"$VAR"` instead of `$VAR` |
| SC2034 | Variable appears unused | Remove or export the variable |
| SC2046 | Quote to prevent word splitting | `"$(command)"` instead of `$(command)` |
| SC2129 | Use `>> file` grouped, not repeated | Group multiple appends |
| SC2155 | Declare and assign separately | `local var; var=$(cmd)` |

## Pre-commit Hook Integration

### Using pre-commit framework

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/rhysd/actionlint
    rev: v1.7.11  # check for latest version
    hooks:
      - id: actionlint
```

### Manual git hook

```bash
#!/usr/bin/env bash
# .git/hooks/pre-commit

# Check if any workflow files are staged
WORKFLOW_FILES=$(git diff --cached --name-only --diff-filter=ACM | grep -E '\.github/workflows/.*\.ya?ml$')

if [ -n "$WORKFLOW_FILES" ]; then
    echo "Running actionlint on modified workflows..."
    echo "$WORKFLOW_FILES" | xargs actionlint
    if [ $? -ne 0 ]; then
        echo "actionlint failed. Fix errors before committing."
        exit 1
    fi
fi
```

## CI Integration Patterns

### Direct Run in CI

```yaml
name: Lint Workflows
on:
  pull_request:
    paths:
      - '.github/workflows/**'

jobs:
  actionlint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7
      - name: Install actionlint
        run: |
          curl -sL https://github.com/rhysd/actionlint/releases/latest/download/actionlint_linux_amd64.tar.gz \
            | tar xz -C /usr/local/bin actionlint
      - name: Run actionlint
        run: actionlint -color
```

### With reviewdog (Inline PR Comments)

```yaml
name: Lint Workflows
on:
  pull_request:
    paths:
      - '.github/workflows/**'

permissions:
  contents: read
  pull-requests: write

jobs:
  actionlint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7
      - uses: reviewdog/action-actionlint@v1
        with:
          fail_level: error
          reporter: github-pr-review  # inline comments on PR
```

**Important:** Always set `fail_level: error` with reviewdog. Without it, actionlint warnings appear as annotations but do not fail the check, allowing broken workflows to be merged.

### SARIF Upload (GitHub Code Scanning)

```yaml
name: Lint Workflows
on:
  push:
    branches: [main]
  pull_request:
    paths:
      - '.github/workflows/**'

permissions:
  contents: read
  security-events: write

jobs:
  actionlint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7
      - name: Install actionlint
        run: |
          curl -sL https://github.com/rhysd/actionlint/releases/latest/download/actionlint_linux_amd64.tar.gz \
            | tar xz -C /usr/local/bin actionlint
      - name: Run actionlint (SARIF)
        run: actionlint -format sarif > actionlint.sarif
        continue-on-error: true
      - uses: github/codeql-action/upload-sarif@v3
        with:
          sarif_file: actionlint.sarif
```

### Combined with Other Linters

```yaml
name: CI Quality
on: [pull_request]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7

      # Lint workflows
      - name: actionlint
        run: |
          curl -sL https://github.com/rhysd/actionlint/releases/latest/download/actionlint_linux_amd64.tar.gz \
            | tar xz -C /usr/local/bin actionlint
          actionlint -color

      # Lint Dockerfiles
      - uses: hadolint/hadolint-action@v3.1.0
        with:
          dockerfile: Dockerfile

      # Lint shell scripts
      - name: shellcheck
        run: shellcheck scripts/*.sh
```

## Editor Integration

- **VS Code:** Install [actionlint extension](https://marketplace.visualstudio.com/items?itemName=arahata.linter-actionlint) for real-time feedback
- **Vim/Neovim:** Use with ALE or null-ls for inline diagnostics
- **JetBrains:** Configure as external tool with file watcher on `*.yml` in `.github/workflows/`

## Troubleshooting

### "shellcheck is not installed"
actionlint optionally uses shellcheck. Install it or disable with `actionlint -shellcheck=`.

### False positives on reusable workflows
Reusable workflow inputs/outputs may not be fully validated. Use `-ignore` for known false positives.

### Custom actions not recognized
actionlint cannot resolve local actions (`./`) or private actions at lint time. Ignore with:
```yaml
# .github/actionlint.yaml
ignore:
  - 'could not read action'
```

### Large matrix expressions
Complex matrix expressions with `fromJSON()` may cause type-check warnings. These are usually safe to ignore:
```yaml
ignore:
  - 'fromJSON'
```

### yamllint `empty-lines` rejects trailing blank lines

Unrelated to actionlint itself, but bites right next to it in CI: if you run `yamllint` in the same lane, its default `empty-lines` rule rejects a file that ends with more than one newline. Workflow files end with exactly one newline.

Generators that use `echo "$CONTENT" > file.yml` frequently add a trailing blank; prefer:

```bash
printf '%s\n' "$CONTENT" > file.yml
```

Verify after writing:

```bash
# Bytes at end of file — should be `0a` (one newline), not `0a0a`.
tail -c 2 file.yml | xxd -p
```

### `docker://IMAGE@sha256:DIGEST` fails workflow startup

Also unrelated to actionlint's own checks (it does not flag this), but a sharp adjacent gotcha when SHA-pinning tools in a gate: a `uses:` step referencing a Docker image by **digest** fails the entire run at startup with `startup_failure` — no job even begins:

```yaml
# ✗ startup_failure — digest form is NOT accepted for docker:// refs
- uses: docker://rhysd/actionlint@sha256:b1934e...

# ✓ tag form is accepted
- uses: docker://rhysd/actionlint:1.7.12
```

`docker://` action refs take `image:tag` only. To get digest-level reproducibility, don't use `docker://` — download the release binary and verify its checksum in a `run:` step (fails closed on mismatch):

```bash
curl -sSfL -o actionlint.tar.gz \
  "https://github.com/rhysd/actionlint/releases/download/v1.7.12/actionlint_1.7.12_linux_amd64.tar.gz"
echo "<sha256>  actionlint.tar.gz" | sha256sum -c -
tar xzf actionlint.tar.gz actionlint
```



--- FILE: skills/github-project/references/actions-upgrade-guide.md ---

<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->
<!-- SPDX-FileCopyrightText: Netresearch DTT GmbH -->

# GitHub Actions Upgrade Guide

Read this when bumping SHA-pinned actions across majors — a Renovate major PR,
or a manual sweep after a security advisory. It covers the one systemic change
driving most current majors (the Node-runtime wave), the upgrade procedure for
SHA pins, and the verified breaking changes per common action.

Version facts and dates below were verified against the actions' release notes
and the GitHub changelog on **2026-08-26**. Versions age; the procedure does
not. Re-resolve current versions at upgrade time instead of trusting any table,
this one included.

## The Node-runtime wave (2025–2026)

GitHub is removing the Node 20 action runtime
([changelog, 2025-09-19](https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/),
dates since revised):

- Since **2026-06-16**, runners execute `runs.using: node20` actions on Node 24
  by default.
- On **2026-09-23**, Node 20 is removed from the runner. Actions still
  declaring `node20` and incompatible with Node 24 break outright.
- Opt in early per workflow with `FORCE_JAVASCRIPT_ACTIONS_TO_NODE24=true`.

Nearly every 2026 major of the common actions is this same change wearing the
action's own version number: the action moves to `runs.using: node24`, which
**requires Actions Runner ≥ 2.327.1**. On GitHub-hosted runners that floor is
long met — just bump. On **self-hosted runners, update the runner first**, or
every bumped action fails at startup. Node 24 itself does not support
macOS ≤ 13.4 or ARM32 self-hosted runners.

Many of the same majors also migrated to ESM. That is transparent to callers —
it only matters when you maintain a fork of the action.

## Upgrade procedure for SHA-pinned actions

Pinning conventions (`uses: owner/action@SHA # vX.Y.Z`, batch tooling) live in
[`security-config.md`](./security-config.md) and
[`org-security-settings.md`](./org-security-settings.md). For the bump itself:

1. **Resolve the real current major from the tag list, never from a
   "latest release" endpoint** — point releases for old majors land later and
   take the latest-release slot (observed 2026-08-26: `actions/download-artifact`
   answered `v3.1.0-node20` as latest release while the current major was v8).

   ```bash
   gh api "repos/OWNER/ACTION/releases?per_page=15" --jq '.[].tag_name' | sort -Vr | head -5
   ```

2. **Read the release notes of every major you cross**, not only the target:

   ```bash
   gh api repos/OWNER/ACTION/releases/tags/vX.0.0 --jq .body
   ```

3. **Resolve tag → SHA and keep the comment in sync** — the comment is what
   humans and Renovate read; a stale comment is worse than none:

   ```bash
   gh api repos/OWNER/ACTION/commits/vX.Y.Z --jq .sha
   ```

4. **Verify**: `actionlint` on the changed workflows
   ([`actionlint-guide.md`](./actionlint-guide.md)), zizmor where wired, and
   watch the first run on a PR — a runtime floor violation only surfaces at
   execution.

Renovate bumps SHA and comment together on its own; a major still needs step 2
before approving the PR.

## Breaking changes by action

Verified from release notes, 2026-08-26. "Runner ≥ 2.327.1" is shorthand for
the Node 24 runtime change described above.

| Action | Current | Major | What changes |
|---|---|---|---|
| `actions/checkout` | v7.0.1 | v6 | Credentials persisted to a separate file instead of `.git/config` ([#2286](https://github.com/actions/checkout/pull/2286)) — anything reading the token out of `.git/config` stops finding it |
| | | v7 | Checkout of a fork PR head is **blocked for `pull_request_target` and `workflow_run` events** ([#2454](https://github.com/actions/checkout/pull/2454)); workflows that deliberately check out fork code on those triggers must be restructured. ESM |
| `actions/cache` | v5.1.0 | v5 | Node 24, runner ≥ 2.327.1 |
| `actions/download-artifact` | v8.0.1 | v5 | **Breaking path behavior** for single-artifact downloads by ID ([#416](https://github.com/actions/download-artifact/pull/416)) |
| | | v6–v7 | Node 24 (v7 makes it the default runtime), runner ≥ 2.327.1 |
| | | v8 | ESM; **hash mismatches now error by default** (overridable per release notes) |
| `actions/upload-artifact` | v7.0.1 | v6 | Node 24 default, runner ≥ 2.327.1 |
| | | v7 | ESM; new `archive: false` uploads a single file unzipped (`name` input ignored in that mode) |
| `actions/setup-node` | v7.0.0 | v7 | ESM; adds `cache-primary-key`/`cache-matched-key` outputs — no caller-facing break found in the notes |
| `ramsey/composer-install` | 4.0.0 | v4 | Internal `actions/cache` v5 → runner ≥ 2.327.1 (breaking for self-hosted only) |
| `docker/setup-buildx-action` | v4.3.0 | v4 | Node 24, runner ≥ 2.327.1; **removes deprecated inputs/outputs** ([#464](https://github.com/docker/setup-buildx-action/pull/464)); ESM |
| `docker/login-action` | v4.6.0 | v4 | Node 24, runner ≥ 2.327.1; ESM |
| `step-security/harden-runner` | v2.21.0 | — | Still on the v2 line, no major crossed |

The absence of a row is not evidence of a painless upgrade — it means the
action was not checked on 2026-08-26. Run step 2 of the procedure.



--- FILE: skills/github-project/references/agentic-workflows.md ---

<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->
<!-- SPDX-FileCopyrightText: Netresearch DTT GmbH -->

# Agentic Workflows Reference

Authoring AI-agent workflows that run on GitHub Actions: `gh-aw` for compiling Markdown specs into hardened Actions YAML, and `gh-aw-firewall` (`awf`) for sandboxing the agent process inside the runner.

## When to use

- Building issue-triage bots, PR-review agents, doc-update agents, scheduled maintenance bots that run as GitHub Actions workflows.
- Hardening an existing agent workflow (permissions narrowing, SHA pinning, output filtering, tool allowlists) without hand-rolling the boilerplate.
- Adding egress control and credential isolation to an agent that calls external LLM/MCP endpoints.

## When NOT to use

- Non-agent CI workflows (lint, test, release). Use the standard patterns in `repo-setup-guide.md` and `reusable-workflow-security.md` instead.
- One-off `gh` scripts run by a maintainer locally — `gh-aw` targets workflows committed to a repo.

## `gh-aw` — GitHub Agentic Workflows

`gh` CLI extension that compiles a natural-language Markdown spec into a hardened GitHub Actions workflow YAML. Each spec is a single Markdown file with YAML front-matter (trigger, permissions, engine, tools) plus a body that describes what the agent should do in prose.

Source: https://github.com/github/gh-aw

### Install

```bash
gh extension install github/gh-aw
```

### What the compiler enforces

- **SHA-pinned `uses:`** for the agent-runtime actions it injects — no `@main`, no floating tags.
- **Narrowed `permissions:`** at the job level, derived from the front-matter declaration. Default is read-only; write scopes are opt-in per workflow.
- **Input sanitisation** for untrusted fields (issue body, PR title, comment body) that are interpolated into the agent prompt — these are passed via env vars, not `${{ }}` expansion in `run:` blocks. See `workflow-bash-patterns.md` for the underlying injection class.
- **Sanitised-output gating** for any step that uses agent output to perform a write (create comment, push branch, file issue). Agent output is filtered before it reaches the GitHub API call.
- **Tool allowlists** for the MCP servers and `gh`/`bash` surfaces the agent is permitted to call. Anything outside the allowlist is refused at runtime.
- **Engine pluggability** — Claude, GitHub Models, and others can be swapped via front-matter without rewriting the workflow.

### Minimal spec shape

```markdown
---
on:
  issues:
    types: [opened]
permissions:
  issues: write
  contents: read
engine: claude
tools:
  github:
    allowed: [add_issue_comment, get_issue]
---

# Triage Bot

Read the issue body and add one of the labels: bug, feature, question.
Post a one-sentence comment explaining the choice.
```

Saved as `.github/aw/triage-bot.md`, `gh aw compile` turns this into a fully-formed `.github/workflows/triage-bot.yml` with the hardening above baked in. Treat the compiled YAML as generated output — edit the Markdown, recompile, commit both.

### Relationship to the rest of the skill

- Compiled workflows still need org-level SHA pinning (`org-security-settings.md`) and supply-chain auditing of any non-default action they pull in (`reusable-workflow-security.md`).
- For reusable-workflow consumers, the gh-aw output is the "workflow" — apply `reusable-workflow-pitfalls.md` to the surrounding wiring.

## `gh-aw-firewall` — Agent egress firewall (`awf`)

Binary that wraps the compiled agent workflow in a Docker sandbox with a Squid proxy enforcing a domain allowlist, plus an optional API-proxy sidecar that holds the LLM credentials so the agent process itself never sees them.

Source: https://github.com/github/gh-aw-firewall

### Components

| Component | Role |
|-----------|------|
| Squid proxy | Enforces an outbound domain allowlist. All agent egress goes through it. |
| Agent container | The compiled `gh-aw` workflow runs here, network-restricted to the proxy. |
| API-proxy sidecar (optional) | Holds the Anthropic/OpenAI/GitHub Models API key; injects auth headers; agent only sees the proxy endpoint, never the secret. |

### When to layer `awf` on top of `gh-aw`

- Agent calls third-party LLM/MCP endpoints and you want the API key out of the agent process's environment (defence against prompt-injection-driven exfiltration).
- You want a hard, declarative allowlist of domains the agent may reach — not a `harden-runner` post-hoc audit.
- The workflow ingests untrusted content (issue bodies, PR diffs from forks, web fetches) and the agent has any write permission.

### When you DON'T need `awf`

- Agent only uses `GITHUB_TOKEN` via the `gh` CLI inside the same repo and makes no external calls. `gh-aw`'s permission narrowing is sufficient.
- Workflow is on a private repo with no fork PR triggers and you trust all input authors.

## `awf` vs `step-security/harden-runner`

They are **not mutually exclusive** and solve adjacent problems:

| | `harden-runner` | `awf` |
|---|---|---|
| Scope | The GitHub Actions runner VM | The agent process inside the workflow |
| Mechanism | eBPF egress monitoring + allowlist on the runner | Squid proxy + Docker network isolation around the agent container |
| Credential isolation | No — secrets in env are visible to all steps | Yes (with API-proxy sidecar) — LLM key never reaches agent |
| Detection vs prevention | Both, configurable | Prevention (proxy refuses non-allowlisted egress) |
| Applies to | Any workflow | Agent workflows specifically |

A defence-in-depth setup uses both: `harden-runner` at the runner level (covers all steps including `actions/checkout`, `setup-*`, etc.) and `awf` around the agent container (adds credential isolation and a narrower allowlist scoped to LLM/MCP endpoints).

## Audit checklist for an agentic workflow

Before merging a new agent workflow:

- [ ] Spec is committed alongside the generated YAML; CI regenerates and diffs to detect drift.
- [ ] Front-matter `permissions:` is the minimum needed — no `write-all`, no `secrets: inherit`.
- [ ] Tool allowlist is explicit — no wildcard MCP servers or `bash` with unrestricted command set.
- [ ] Untrusted input fields go through env-var passing, not direct prompt interpolation (gh-aw does this by default — verify in compiled YAML).
- [ ] If the agent has any write scope and ingests fork-PR content: `awf` is enabled or the trigger excludes untrusted authors.
- [ ] LLM credentials are stored as repository or environment secrets, never in workflow files; with `awf`, they live in the API-proxy sidecar and are not exposed to the agent step.
- [ ] Agent workflow has `concurrency:` scoped to the triggering issue/PR (not a static repo-wide group) so concurrent issues/PRs don't serialise unnecessarily — e.g. `group: ${{ github.workflow }}-${{ github.event.issue.number || github.event.pull_request.number || github.sha }}`.

## Related

- `reusable-workflow-security.md` — supply-chain trust + SHA pinning that applies to any action the compiled workflow references.
- `workflow-bash-patterns.md` — the injection class that gh-aw's input-sanitisation flow defends against.
- `security-config.md` — `harden-runner` setup at the runner level.
- `org-security-settings.md` — org-wide `sha_pinning_required` setting that `gh-aw` output already complies with.



--- FILE: skills/github-project/references/ai-reviewer-pushback.md ---

<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->
<!-- SPDX-FileCopyrightText: Netresearch DTT GmbH -->

# AI Reviewer Pushback Patterns

How to evaluate, respond to, and resolve review comments from automated AI reviewers (GitHub Copilot, gemini-code-assist, CodeRabbit, Sourcery, Codium / PR-Agent, etc.) without either rubber-stamping wrong advice or ignoring valid feedback.

## When to use

- An AI reviewer left comments on a PR and you need to decide which to apply.
- A reviewer flagged a "high priority" issue that contradicts your local verification.
- You're being asked to change config, code, or APIs based on AI-generated suggestions.

## The core problem

AI code reviewers produce a mix of:

1. **Genuinely useful catches** — typos, missing null checks, leaked secrets, unused imports, accessibility issues, the kind of thing a careful reviewer would also notice.
2. **Stylistic preferences** — usually low-stakes, often defensible either way.
3. **Plausible-sounding but factually wrong claims** — invented API names, deprecated patterns presented as current, version-status claims that lag reality.

Categories 1 and 2 are easy. Category 3 is the dangerous one: an AI reviewer states with full confidence that "the field is named X" or "this version is not yet released," and a hurried maintainer applies the change to clear the review. The fix breaks the build, regresses security, or introduces a real bug.

## Common failure modes to watch for

### Field-name / API-name hallucination

The reviewer asserts that a config key, function, or type is named X. The name doesn't exist in current docs (or never existed at all).

**Real examples seen in the wild:**

- gemini-code-assist suggested `ignoredBuilds:` for pnpm 11. Pnpm 11 has no `ignoredBuilds` setting — the legacy field was named `ignoredBuiltDependencies` (deprecated 10.26, removed in 11), and the modern equivalent is `allowBuilds: { pkg: false }`.
- Suggesting `secrets: inherit` "for simplicity" in reusable workflows — actively dangerous, exposes the entire org-secret namespace.
- Recommending TYPO3 v11 ViewHelper namespaces in v13/v14 code.

**Tell:** the suggestion always sounds confident, often quotes a documentation-shaped block, and doesn't link to the docs.

### Stale knowledge of release status

The reviewer claims a current release "is not out yet," recommends an outdated minimum version, or asserts a feature "doesn't exist" when it has shipped. Training cutoffs are months to years behind, and bots rarely declare their knowledge boundary.

**Illustrative shapes** (specific versions cited here will go stale — treat as examples of the pattern, not authoritative current state):

- "Language X version N is not released yet" — when it is. Verify against the language's release page.
- "Use Node N as the maximum supported version" — when a newer LTS is current.
- "Framework F version N has not been released" — when an N.x release is already in production.
- "Tool T version vN does not exist; T is on major vN-1" — when major vN shipped after the bot's cutoff. The reply often predicts a concrete consequence ("the download will 404 and the install will silently fail") and hands you a downgrade to paste. The prediction is testable: fetch the URL and run the tool.

**Tell:** version assertions without a release-date check, or recommendations that pull constraints downward from what your CI matrix is already running. A dependency- or tooling-upgrade PR is where this lands hardest — the bot's stale snapshot is, by definition, the state the PR is moving away from, so it reads every upgrade as an error.

**Refuting it takes three commands** — the registry's own answer, the artifact's reachability, and the tool reporting its own version:

```bash
gh api repos/OWNER/TOOL/releases/latest --jq .tag_name           # what is actually latest
curl -sIL -o /dev/null -w '%{http_code}\n' "$URL_THE_BOT_SAYS_404s"   # the predicted 404
tool --version                                                   # the binary's own answer
```

Quote all three in the reply. A version claim refuted by the tool printing its own version number is not arguable, and it converts the thread from opinion-vs-opinion into a closed question.

### Pattern advice frozen at a past major

The reviewer suggests a deprecated pattern that was current in their training data: jQuery for vanilla DOM tasks, Vue 2 Options API in a Vue 3 codebase, deprecated GitHub Actions inputs (`fail_on_error` instead of `fail_level`), CKEditor 4 plugin shapes used in a CKEditor 5 codebase.

**Tell:** the advice contradicts code patterns already in the same file or neighbouring files.

### Inverting a security control

The reviewer recommends weakening a control "to fix the failing build." The build is failing because the control is correctly enforcing a new default; the right fix is configuration, not weakening.

**Real examples:**

- "Set `strict-peer-dependencies=false`" when the underlying issue is a missing peer.
- "Set `engine-strict=false`" when engines is correctly rejecting an unsupported version.
- "Disable harden-runner" when an egress is being legitimately blocked.

**Tell:** the suggested change makes the symptom go away by removing the check that produced the symptom.

### Runtime / language-semantics claims

The reviewer asserts how the language runtime behaves — an exception it "will" throw, a coercion, an evaluation order — and the assertion is simply wrong.

**Real example:**

- Copilot claimed a **user-defined** method that declares **fewer** parameters than a caller passes "will throw `ArgumentCountError`." For user-defined functions/methods PHP only throws on too-few *required* arguments — **extra positional arguments are silently ignored** (verified: `function f($a){} f(1,2,3)` returns normally, no error). The one exception is *internal* functions: since PHP 8.0 those do throw `ArgumentCountError` on extra arguments (`strlen("a","b")`). The method here was user-defined, so the code was correct — and the passing functional tests proved it. (A second reviewer on this very PR then asserted the opposite — that user-defined methods *do* throw on extra args — which a one-line `php -r` disproves; a nice illustration that two bots can confidently contradict each other, and the runtime is the arbiter.)

**Tell:** the claim is about runtime behavior that a green test already exercises. Don't restructure code to satisfy a semantics claim your test suite already disproves — the test run is the authority (see step 2). Reproduce it in a one-off snippet if you're unsure, rather than trusting the assertion.

## The pushback workflow

When you suspect a reviewer comment is wrong, follow this sequence **before** changing any code:

### 1. Verify against primary sources

Open the official docs for the library/tool the reviewer is talking about. Look for:

- The exact field/API name they suggested. Is it in the current docs? Was it ever in the docs?
- The version they reference. Is that the current major? Was the feature/deprecation they mention introduced/removed in a release that has already shipped?
- The release-status claim. Cross-check against the project's release page or registry.

If you have a documentation lookup tool available (e.g. the [Context7](https://github.com/upstash/context7) MCP server, which fetches current library docs on demand), use it. Otherwise fetch the docs URL directly. Treat AI training-data as a stale snapshot.

### 2. Check empirical evidence already on the PR

If the reviewer is claiming "this won't work" but **CI is green**, that's strong evidence the configuration does work. Note:

- The specific check name (e.g. `build-and-push`).
- The conclusion (`SUCCESS`).
- The pnpm/node/php/library version the runner used (often visible in the install-step log).

A green CI run on a non-trivial check is empirical evidence that overrides a confident textual assertion. Cite it.

### 3. Read the bot's "why"

Some bots include a rationale block. If the rationale references behavior from a deprecated version, an old release line, or a feature that was removed, that's diagnostic. Quote it back when you reply.

### 4. Decide

Three legitimate outcomes:

1. **Apply the change.** The reviewer is right. Make the change in a follow-up commit and reply linking the commit SHA.
2. **Push back.** The reviewer is wrong. Reply on the thread with citations and resolve. Do NOT change the code.
3. **Compromise.** The reviewer has a point but the suggested implementation is wrong. Reply explaining the alternative, link the commit that does the right thing.

### 5. Reply directly to the thread

Always reply to the review-comment thread, not as a top-level PR comment. The reply preserves context and lets future readers follow the disagreement.

```bash
# Find thread IDs
gh api graphql -f query='query {
  repository(owner: "OWNER", name: "REPO") {
    pullRequest(number: NUMBER) {
      reviewThreads(first: 50) {
        nodes {
          id
          isResolved
          comments(first: 1) {
            nodes { databaseId author { login } body }
          }
        }
      }
    }
  }
}' --jq '.data.repository.pullRequest.reviewThreads.nodes[] |
  {id, isResolved,
   author: .comments.nodes[0]?.author?.login,
   snippet: (.comments.nodes[0]?.body // "")[0:100]}'

# Reply to a thread
gh api graphql \
  -f query='mutation($body: String!, $tid: ID!) {
    addPullRequestReviewThreadReply(input: {body: $body, pullRequestReviewThreadId: $tid}) {
      comment { url }
    }
  }' \
  -f tid="PRRT_xxx" \
  -f body="See pnpm 10.26 release notes (https://...) — the field is named allowBuilds and takes a map, not an array."
```

### 6. Resolve the thread

After replying, resolve. Don't leave threads open as a passive-aggressive disagreement marker — it makes the PR look unsettled to future reviewers and can block merges on repos that require thread resolution.

```bash
gh api graphql \
  -f query='mutation($tid: ID!) {
    resolveReviewThread(input: {threadId: $tid}) {
      thread { isResolved }
    }
  }' \
  -f tid="PRRT_xxx"
```

## Reply template — pushback with evidence

A good pushback reply has four parts:

1. **State the disagreement** in one sentence.
2. **Cite the primary source** (link, with relevant quote).
3. **Cite empirical evidence** (CI run, test result, doc URL).
4. **State what you are doing** (leaving as-is / applying alt fix / etc.).

Example:

> Thanks, but this suggestion is incorrect on both points and I am leaving the config as-is.
>
> **1. The field is `allowBuilds` and it is a map.** [pnpm 10.26 release notes](https://pnpm.io/blog/releases/10.26) define it as a map of package matchers to booleans, supporting per-version pinning (`nx@21.6.4: true`).
>
> **2. `ignoredBuilds` is not a pnpm setting.** The legacy field was `ignoredBuiltDependencies`, also removed in pnpm 11.
>
> **3. Verified empirically.** The `build-and-push` CI check is green on this PR with the current config (pnpm v11.0.9), no `ERR_PNPM_IGNORED_BUILDS` warning.

This pattern works for any bot reviewer. Three citations + a clear decision.

## Reply template — partial agreement

When the reviewer raised a real concern but suggested a wrong fix:

> Good catch on the underlying issue — fixed in [<commit-sha>](<commit-url>).
>
> Going with `<alternative>` rather than `<bot-suggestion>` because <one-sentence reason with link>.

## Anti-patterns

- **Silently making the change to clear the review.** Future maintainers can't tell whether the change was correct or compliance-driven.
- **Top-level "thanks, addressed in commit X" comments.** Lose the diff context. Always reply on the thread.
- **"Disagree, see commit history."** Not a reply. Cite docs and CI evidence.
- **Leaving the thread unresolved with no reply.** Reads as ignoring the bot. Reply, then resolve.
- **Marking a thread resolved without replying when you applied the change.** Drops the rationale; future readers see a closed thread with no record of the decision.

## When the finding is about scope, not content — CodeRabbit guideline files

A recurring class of CodeRabbit finding is not wrong about the rule, only about
where the rule applies: a PHP rule quoted at a Markdown-only diff, a frontend
convention raised on a CI file. The cause is configuration, not the reviewer.
`knowledge_base.code_guidelines` supplies a guideline document — `AGENTS.md`,
`CLAUDE.md` and friends are in the defaults — to reviews of **every** path, so a
rule reading "in every file" is evaluated against every file.

Two settings sound interchangeable and are not:

| Setting | What it does | What it cannot do |
|---|---|---|
| `knowledge_base.code_guidelines.filePatterns[]` | selects **which files are read** as guidelines; an entry may carry `applyTo` to scope **where they apply** | — |
| `reviews.path_instructions[]` | **adds** guidance for a glob | subtract a repository-wide guideline document |

So the fix for a mis-scoped rule is `applyTo`, not `path_instructions`:

```yaml
knowledge_base:
  code_guidelines:
    enabled: true
    filePatterns:
      - "**/AGENTS.md"                 # repo-wide: plain string
      - files: "docs/php-rules.md"     # scoped: object form
        applyTo: "**/*.php"
```

Three traps, each of which cost a wrong turn:

- **`applyTo` is absent from the prose documentation.** It exists only in the
  [published schema](https://storage.googleapis.com/coderabbit_public_assets/schema.v2.json).
  Reading the docs page and concluding "nothing can scope a guideline document"
  is the wrong answer, confidently reached.
- **The object form requires both `files` and `applyTo`.** An entry with `files`
  alone is schema-invalid, so a document you want unscoped must be written as a
  plain string.
- **`filePatterns` is declared `default: []` with the default set documented in
  prose only**, which does not say whether an explicit list extends or replaces
  it. List the repo-wide document explicitly and the question stops mattering.

Validate the result against the schema, not merely as well-formed YAML —
`jsonschema` against `schema.v2.json` catches the `files`-without-`applyTo` case
that a YAML parser accepts happily.

## Per-bot quirks

Behavior is bot-specific and changes; treat as starting hints, verify against current behavior:

| Bot | Note |
|-----|------|
| `gemini-code-assist[bot]` | Often confidently invents config field names; **frequently behind on tool/package versions and releases** — treat every version assertion as unverified (see [Stale knowledge of release status](#stale-knowledge-of-release-status)), especially when it asks you to pin *downward*; severity badges (`high`/`medium`) are not always correlated with actual severity |
| `copilot-pull-request-reviewer[bot]` | Tends toward verbose summaries; reviews almost never come back as `APPROVED` (state is `COMMENTED`); see `auto-merge-guide.md` for the auto-merge race condition |
| `coderabbitai[bot]` | Higher signal but verbose; prone to repeating the same nit across many threads — resolving in batches is reasonable |
| `sourcery-ai[bot]` | Stylistic / refactor focus; advice quality drops on non-mainstream language constructs |

## Related

- `auto-merge-guide.md` — Copilot-as-reviewer race condition that blocks PRs without leaving an actionable review
- `merge-strategy.md` — for repos that require all threads resolved before merge



--- FILE: skills/github-project/references/auto-merge-guide.md ---

<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->
<!-- SPDX-FileCopyrightText: Netresearch DTT GmbH -->

# Auto-merge & Auto-approve Guide

Auto-merge for dependency bots and auto-approve for solo maintainers.

These setups apply only after the project's documented review contract has
been established. They must not replace required qualified human reviews with
automated approval or reduce an existing reviewer count. Inspect enforcement on
the actual PR base, including temporary stacked branches:
[review-policy-contract.md](review-policy-contract.md).

## Solo Maintainer: Choose One of Two Setups

GitHub does not let an author approve their own pull request. A repository with one maintainer therefore needs either an automated approver or no required approval; `required_approving_review_count: 1` without `pr-quality.yml` leaves an admin bypass as the only way to merge.

| Setup | Branch protection | Needs | Trade-off |
|-------|-------------------|-------|-----------|
| **A — auto-approve** | `required_approving_review_count: 1` | `pr-quality.yml` on the default branch (template below); `can_approve_pull_request_reviews=true` | Keeps the OpenSSF Scorecard Code-Review point and an approval record per PR; the bootstrap PR adding the workflow needs a manual approval |
| **B — no required approval** | `required_approving_review_count: 0`, `required_conversation_resolution: true`, required status checks | nothing extra; bootstrap with `init-branch-protection.sh OWNER/REPO --solo` | Unresolved threads, failing checks, force pushes and deletions still block; Scorecard's Code-Review check scores lower |

Measured 2026-09-14 across eight netresearch repositories: data-tools-skill, jira-skill, git-workflow-skill, maint, timetracker and retro-skill use B; ofelia and ldap-manager use A (issue #191). Pick A where Scorecard matters or several people review; pick B for single-maintainer skill and tooling repositories.

### Setup A: Auto-approve via `pr-quality.yml`

Keep `required_approving_review_count >= 1` and use a `pr-quality.yml` workflow that auto-approves PRs from repo collaborators.

**How it works:** The workflow checks the PR author's repository permission. If they have `write` or `admin` access, it approves the PR automatically via `github-actions[bot]`, satisfying the review requirement without manual intervention.

**Use the template:** `assets/pr-quality.yml.template` → `.github/workflows/pr-quality.yml`

**Branch protection settings:**

```bash
gh api repos/OWNER/REPO/branches/main/protection/required_pull_request_reviews -X PATCH \
  --input - << 'EOF'
{
  "required_approving_review_count": 1,
  "dismiss_stale_reviews_on_push": true,
  "require_code_owner_reviews": false
}
EOF
```

**Who gets auto-approved:**

| PR author | Approved by | Auto-merged by |
|-----------|-------------|----------------|
| Repo collaborator (write/admin) | `pr-quality.yml` | Manual merge or auto-merge rule |
| Dependabot / Renovate / release-please | `auto-merge-deps.yml` | `auto-merge-deps.yml` (via `--auto`) |
| External contributor | Manual review required | Manual merge |

> **Bootstrap note:** When first adding `pr-quality.yml`, the PR that introduces it must be approved manually (the workflow isn't on the base branch yet). All subsequent PRs auto-approve.

## Troubleshooting Quick Reference

| Symptom | Cause | Fix |
|---------|-------|-----|
| PR BLOCKED, checks pass | Check names don't match | Update branch protection to use exact names (e.g., `job (variant)` not `job`) |
| PR BLOCKED, `reviewDecision: REVIEW_REQUIRED` | `require_code_owner_reviews: true` | Obtain the required qualified code owner approval; change requirements only under an authorized policy change |
| PR BLOCKED, unresolved threads | `required_conversation_resolution: true` | Resolve all review threads before merging |
| PR has pending reviewers | Requested reviewers haven't responded | Wait for all requested reviewers to submit their review |
| Renovate PR not using bypass | Workflow racing with Renovate | Only approve in workflow; let Renovate enable auto-merge via `platformAutomerge` |
| CI can't push to main | Branch protection blocks direct push | Use Renovate `lockFileMaintenance` instead |
| Workflow not triggering | Rapid merges skip push events | Add `workflow_dispatch` trigger, run manually |
| "Merge method X not allowed" | Wrong merge strategy | Use auto-detection (see below) or check `gh api repos/O/R --jq '{merge: .allow_merge_commit, squash: .allow_squash_merge, rebase: .allow_rebase_merge}'` |
| "Rebase merges cannot be automatically signed" | Signed commits + rebase | Allow merge commits (`allow_merge_commit`) and merge with `--merge` (reusable: `merge-strategy: merge`); GitHub signs merge and squash commits, never rebased ones |
| Renovate PR `CLEAN` for weeks, never merges | Signed commits + rebase-only: GitHub drops the armed auto-merge without an error | `gh api --paginate repos/O/R/issues/N/timeline --jq '.[].event' \| grep -c auto_merge_disabled`; fix as in the row above |
| Bot PR approved after a human push | Job checks only `user.login` | Require `user.login` AND `github.actor` (see dependency-management.md) |
| Third-party gitleaks scan fails on bot PRs | Legacy `gitleaks-action@v2` needs a license secret Dependabot cannot read | Call `netresearch/.github/.github/workflows/betterleaks.yml@main` (betterleaks, no license); tune `.gitleaks.toml` for false positives |
| Old PRs not auto-merging | Opened before workflow existed | Comment `@dependabot rebase` / `@renovate rebase` to trigger `synchronize` |
| Can't merge workflow file PRs | `GITHUB_TOKEN` lacks `workflows` scope | Merge manually; use workflow check in `auto-merge-direct.yml` template |
| Auto-approve skipped, PR stuck `REVIEW_REQUIRED` or blank `reviewDecision` | Auto-approve raced with Copilot reviewer | Re-run the auto-approve workflow after Copilot finishes; long-term fix is adding `pull_request_review` trigger — see [Auto-Approve Race Condition with Copilot Reviewer](#auto-approve-race-condition-with-copilot-reviewer) |

## Auto-Approve Race Condition with Copilot Reviewer

**This section is the canonical home for the "PR stuck BLOCKED despite green CI + explicit approval" gotcha.** Project-level `CLAUDE.md` entries should cross-reference this file rather than restating the details.

When using a solo-maintainer auto-approve workflow alongside GitHub Copilot as a reviewer, a race condition can leave PRs stuck blocked even though every gate appears satisfied:

1. New push triggers both the auto-approve workflow and Copilot review
2. Auto-approve runs first, sees Copilot as a pending reviewer, skips approval silently
3. Stale review dismissal (`dismiss_stale_reviews_on_push: true`) clears any previous approvals from the push
4. Copilot finishes reviewing with state `COMMENTED` (not `APPROVED`) — Copilot almost never actively approves
5. No approval exists anywhere; PR stays `BLOCKED`

**Symptoms** — `gh pr view N --json mergeStateStatus,reviewDecision` returns one of:

- `{"mergeStateStatus":"BLOCKED", "reviewDecision":"REVIEW_REQUIRED"}` (classic case)
- `{"mergeStateStatus":"BLOCKED", "reviewDecision":""}` (no review decision computed yet — seen when Copilot is mid-review and the repo has `required_approving_review_count >= 1`)

In both cases: all CI status checks are `SUCCESS`, there are no `CHANGES_REQUESTED` reviews, no unresolved review threads, and the auto-approve job reports `success` in `gh run list`. The approval simply never happened.

### Diagnosis

Confirm the silent-skip is the cause before re-running anything:

```bash
# 1. Find the latest auto-approve run for THIS PR's head commit and its job id.
#    Scoping by head_sha prevents picking up runs from other PRs/branches.
HEAD_SHA=$(gh pr view PR_NUMBER --repo OWNER/REPO --json headRefOid --jq .headRefOid)
RUN_ID=$(gh api "repos/OWNER/REPO/actions/runs?head_sha=$HEAD_SHA&per_page=20" \
  --jq '[.workflow_runs[] | select(.name == "PR Quality Gates")] | .[0].id')
JOB_ID=$(gh api "repos/OWNER/REPO/actions/runs/$RUN_ID/jobs" \
  --jq '.jobs[] | select(.name | test("Auto-[Aa]pprove")) | .id' | head -1)

# 2. Inspect the job log for the skip marker. Use `gh run view --log` — the
#    raw /logs API returns a zip archive that won't grep cleanly.
gh run view --log --job="$JOB_ID" --repo OWNER/REPO \
  | grep -iE "skip|copilot|pending reviewer|requested_reviewers"
```

If the log contains a line like "Skipping approval: pending reviewers" or shows `requested_reviewers` containing `copilot-pull-request-reviewer[bot]`, the race condition is confirmed.

Also useful — current reviewer state:

```bash
gh api repos/OWNER/REPO/pulls/PR_NUMBER \
  --jq '{requested_reviewers: [.requested_reviewers[]?.login], requested_teams: [.requested_teams[]?.slug]}'
```

An empty `requested_reviewers` after Copilot's review has landed confirms Copilot is no longer blocking — so a rerun will now succeed.

### Fix — re-run the workflow

```bash
# Scope the lookup to THIS PR's head commit — filtering only by workflow name
# can return runs from other PRs/branches.
HEAD_SHA=$(gh pr view PR_NUMBER --repo OWNER/REPO --json headRefOid --jq .headRefOid)
RUN_ID=$(gh api "repos/OWNER/REPO/actions/runs?head_sha=$HEAD_SHA&per_page=20" \
  --jq '[.workflow_runs[] | select(.name == "PR Quality Gates")] | .[0].id')

# Re-run it
gh api repos/OWNER/REPO/actions/runs/$RUN_ID/rerun -X POST
```

Wait ~2 minutes, then re-check `gh pr view N --json mergeStateStatus,reviewDecision`. Expected result: `{"mergeStateStatus":"CLEAN", "reviewDecision":"APPROVED"}`.

> **Why the rerun works:** `gh run rerun` on the latest run re-reads the current reviewer list. By that point Copilot has submitted its review, so it's no longer in `requested_reviewers` and auto-approve proceeds. See also [CI Re-runs Replay the Same Commit](#ci-re-runs-replay-the-same-commit) — use the LATEST run id (not an older failed one) so the rerun executes against current HEAD.

### Prevention

Pick one of these patterns when authoring or updating a `pr-quality.yml` / auto-approve workflow. See [`../assets/pr-quality.yml.template`](../assets/pr-quality.yml.template) for the baseline.

**Option A — also trigger on review submission (simplest):**

```yaml
on:
    pull_request_target:
        types: [opened, synchronize, reopened]
    pull_request_review:
        types: [submitted, dismissed]
```

When Copilot submits its review, the workflow re-fires and now sees an empty `requested_reviewers` list. This is the lowest-effort fix and works for most solo-maintainer setups.

**Option B — poll with retry inside the approval step (race-free, slower):**

Before approving, poll `requested_reviewers` until it's empty or a timeout elapses. Typical timeout: 5 minutes. Use this when Copilot reviews are slow or when missed-approval events are expensive (e.g. repos with tight merge SLOs).

**Option C — wait for Copilot explicitly:**

Gate the approval step on `github.event.review.user.login == 'copilot-pull-request-reviewer[bot]' && github.event.review.state != 'changes_requested'` in a `pull_request_review`-triggered job. Race-free but fires only after Copilot posts — not useful when Copilot isn't actually assigned to the PR.

**Do NOT** "fix" this race by dropping `required_approving_review_count` to `0` on a Setup A repository — that silently switches it to Setup B, losing the OpenSSF Scorecard Code-Review point and the approval record. Switching to B is a deliberate choice (see [Solo Maintainer: Choose One of Two Setups](#solo-maintainer-choose-one-of-two-setups)), not a race workaround.

## Post-Merge Review Sweep

**Symptom:** you admin-merge a PR that was CLEAN, then hours/days later `gh api graphql` shows unresolved review threads on it. The reviewer posted comments AFTER the merge landed.

**Why this happens:**

1. Admin-merging bypasses the "all threads resolved" check that a normal merge would enforce. A Copilot / human review that was still being authored at merge time lands afterwards.
2. Automated reviewers (GitHub Copilot, Advanced Security code-scanning, gosec/semgrep via reviewdog) often post on the final commit AFTER CI finishes — which can be after the merge.
3. In a batch workflow (e.g. closing out a multi-repo rollout), you move on to the next PR before the previous one settles.

**Consequences:** legitimate review findings go unanswered. If the finding was substantive (correctness bug, dead code, doc drift) it silently ships.

**Sweep process — run at the end of any batched-merge session:**

```bash
# List every PR you merged + check unresolved threads on each.
prs=(
  "owner/repo1#123"
  "owner/repo2#456"
  ...
)
for pr in "${prs[@]}"; do
  R="${pr%#*}"; N="${pr#*#}"
  OWNER="${R%/*}"; NAME="${R#*/}"
  u=$(gh api graphql -f query="{
    repository(owner: \"$OWNER\", name: \"$NAME\") {
      pullRequest(number: $N) {
        reviewThreads(first: 100) { nodes { isResolved } }
      }
    }
  }" | jq '[.data.repository.pullRequest.reviewThreads.nodes[]
            | select(.isResolved == false)] | length')
  [ "$u" -gt 0 ] && echo "UNRESOLVED: $pr ($u)"
done
```

`reviewThreads(first: 100)` covers GitHub's per-page maximum. Paginate with `pageInfo { hasNextPage endCursor }` + `after:` for PRs that might exceed 100 threads (long-running PRs on hot files).

For each unresolved thread:

1. Read the initial comment body via `reviewThreads(first: 100) { nodes { id isResolved comments(first: 1) { nodes { author { login } body } } } }`. Bump `comments(first:)` or paginate if you need follow-up replies on the same thread rather than just the initiating comment.
2. If valid → open a follow-up PR that addresses it, referencing the PR + thread by URL in the commit message.
3. Reply on the thread using the GraphQL mutations in [`gh-cli-reference.md`](./gh-cli-reference.md): `addPullRequestReviewThreadReply` + `resolveReviewThread`.
4. If not valid (false positive, design-intent) → reply with the reasoning (cite evidence — tested behavior, design docs, etc.) then resolve.

**Don't silently dismiss review threads.** Even for false positives, leave a reply explaining why so the next person who opens the PR sees the decision.

**Re-sweep after follow-up PRs merge.** Copilot often reviews the follow-up PR itself and posts new threads. The sweep isn't one-shot — run it again until the count hits zero across all touched PRs.

### Wait for Copilot Before Merging (prevents the cascade)

Copilot's review is **asynchronous**: it usually lands 1–3 min after the PR opens, sometimes longer on a busy day. If you enable `--auto --merge` the instant CI passes, you merge *before* Copilot has reviewed — and the review lands on an already-merged PR, which then needs a follow-up PR to address. Copilot reviews that follow-up too, so the same race repeats. A single round of non-trivial review can easily cascade to 5–6 follow-up PRs.

**Prevention — poll for Copilot before enabling auto-merge:**

```bash
# Wait up to 5 min for Copilot's review to appear. If it never does
# (skill-only docs PRs, repos without Copilot review enabled), the loop
# exits on timeout and you proceed.
for _ in $(seq 1 30); do
  reviewed=$(gh pr view "$PR" --repo "$REPO" --json reviews --jq '
    [.reviews[] | select(.author.login == "copilot-pull-request-reviewer")] | length')
  [ "$reviewed" -ge 1 ] && break
  sleep 10
done

# Now address any unresolved threads, THEN enable auto-merge.
gh pr merge "$PR" --repo "$REPO" --auto --merge
```

**Or enforce via branch protection:** add `copilot-pull-request-reviewer` as a required reviewer so branch protection blocks merge until the review exists. GitHub's UI for this is under *Settings → Branches → Branch protection rules → Require review from Code Owners / specific reviewers*; for rulesets, set `required_pull_request_reviews.required_approving_review_count >= 1` with `dismiss_stale_reviews_on_push: true`. Note that *requested* isn't the same as *approved* — see [merge-strategy.md](./merge-strategy.md) on blocking on pending reviews.

**If you still cascade**, expect it: budget 2–3 sweep rounds mentally rather than claiming "done" after the first merge. The Copilot-review → fix → merge → Copilot-reviews-the-fix loop is the norm on non-trivial text changes, not the exception.

### Validate Copilot Suggestions Before Applying

Copilot occasionally suggests syntactically invalid or semantically wrong code. Recent examples from this fleet:

- **`?:` ternary** in a GitHub Actions expression — not supported; GHA expressions use `&&` / `||` chains
- **`inputs.make_latest`** in a workflow that triggers on both `push.tags` and `workflow_dispatch` — the `inputs` context is undefined on `push` events and raises *"Unrecognized named-value: 'inputs'"*; use `github.event.inputs.*` for safety across events

Treat suggestions as reviewer *input*, not ground truth. Read the code, verify against docs (see [workflow-bash-patterns.md](./workflow-bash-patterns.md) for the GHA expression specifics), and apply in the form that's actually correct. Reply with your adjusted reasoning on the thread rather than silently applying a broken suggestion and having to patch it two sweeps later.

## CI Annotations — Always Check Before Declaring a PR Clean

CI checks can report `success` at the status-run level while still emitting **warning annotations** (typical for actionlint / shellcheck via reviewdog, CodeQL deprecation notices, YAML-lint). These annotations don't show up in `gh pr checks` or in the PR summary page — they only appear on the job's detail page or on the Files-Changed tab. Declaring a PR "clean" based on `gh pr checks` alone leaves real findings un-addressed.

**Check explicitly:**

```bash
# Annotations on a specific check run:
gh api repos/OWNER/REPO/check-runs/CHECK_RUN_ID/annotations --jq \
  '.[] | {message, annotation_level, path, start_line}'

# All check runs for a commit that have any annotations:
gh api "repos/OWNER/REPO/commits/SHA/check-runs" --jq \
  '.check_runs[] | select(.output.annotations_count > 0) |
   {name, annotations: .output.annotations_count}'
```

**Make warnings blocking.** reviewdog-based linters default to posting warnings that don't fail the workflow. Configure them to fail:

```yaml
- uses: reviewdog/action-actionlint@v1   # or -shellcheck, -yamllint, etc.
  with:
    fail_level: error
```

`fail_level: error` is the modern input; the deprecated `fail_on_error` + `level` combination still works but is going away. When a new reviewdog-based linter is added, grep the caller for `fail_level:` and set it to `error` up front — otherwise real findings silently accumulate.

## CI Re-runs Replay the Same Commit

`gh run rerun <run-id>` **re-executes the ORIGINAL commit SHA**, not `HEAD`. If you push a fix and re-run a failed old workflow, the rerun still fails against the pre-fix code.

**Right way:** push the fix, then either wait for the automatic run triggered by the push, or re-run the LATEST run:

```bash
# Latest run ID for a workflow on a branch:
gh api "repos/OWNER/REPO/actions/runs?per_page=5" --jq \
  '.workflow_runs[] | select(.name == "CI") | {id, head_sha: .head_sha[:7]}' \
  | head -1

gh api repos/OWNER/REPO/actions/runs/RUN_ID/rerun -X POST
```

## `mergeStateStatus: BLOCKED` — Check Required vs Non-Required Checks First

`BLOCKED` does **not** mean a check failed — most often it means required checks are still **pending**. Before diagnosing a PR as blocked by a specific tool, compare the failing check against the branch's *required* set. A red **non-required** check never blocks merge.

Real case (2026-07-18): two bump PRs showed `mergeStateStatus: BLOCKED` with `copilot-pull-request-reviewer` at `conclusion: failure` — the failure body was *"Copilot was unable to review this pull request because the user who requested the review has reached their quota limit."* That check was **not** in `required_status_checks`, so both PRs auto-merged the moment the required set (Skill Validation, composer-audit, gitleaks, DCO, …) went green. Reporting them as "Copilot-blocked" was wrong.

This holds even when a `copilot_code_review` rule is active on the branch — that rule requests a review, it does not gate the merge. See "A quota-limited Copilot review does not block the merge" in `merge-strategy.md`.

```bash
# The required set (the ONLY checks that can BLOCK) comes from two sources that
# no single endpoint merges — read both, on the PR's base branch:
BASE=$(gh pr view PR --repo OWNER/REPO --json baseRefName --jq .baseRefName)
# rulesets (repository and organisation):
gh api --paginate "repos/OWNER/REPO/rules/branches/$BASE?per_page=100" \
  --jq '.[] | select(.type=="required_status_checks") | .parameters.required_status_checks[].context'
# classic branch protection — classify a check as advisory only once this read
# succeeded or reported "Branch not protected":
if gh api "repos/OWNER/REPO/branches/$BASE/protection" > prot.json 2> prot.err; then
  jq -r '.required_status_checks.contexts[]?' prot.json
elif grep -q "Branch not protected" prot.err; then
  echo "no classic branch protection"
else
  cat prot.err; echo "classic protection NOT read — the required set is incomplete"
fi

# A failing check in NEITHER list is advisory — it does not gate merge.
# BLOCKED + all required checks green/pending → wait, don't intervene.
```

Corollary: a quota-exhausted Copilot review returns `conclusion: failure`, not `neutral` — treat "failure" on an advisory reviewer check as noise, not a code problem. Never reach for `--admin` to "unblock" it.

### BLOCKED with every visible gate satisfied

When the required checks are green, no thread is open and `reviewDecision` is `APPROVED`, but `mergeStateStatus` stays `BLOCKED`, the cause is not yet known. Report it that way — "cause unknown, ruled out: …" — followed by what is left as candidates. A candidate is not a cause: name something as the cause only after a comparison with a PR whose gate opened under the same rules shows a difference.

Read the PR page first. Its merge box lists a required check it still waits for as "Expected — Waiting for status to be reported", and that line can name a gate the API evidence below shows as satisfied. No API returns that list — GraphQL has no `mergeRequirements` field on `PullRequest` — so a script can only report "cause unknown" here; ask the person who can see the page, or open it.

Branch protection comes from two sources, and each endpoint reads only one of them: `rules/branches/<base>` returns the rules of every ruleset (repository and organisation) and none of the classic branch protection; `branches/<base>/protection` returns the classic protection and none of the rulesets. On netresearch/git-workflow-skill the classic protection holds eight required contexts that `rules/branches/main` does not list. Before collecting anything, read the head SHA and the state again a few minutes later: `mergeStateStatus` can lag behind the condition that set it (see "When every gate checks out, re-query before diagnosing further" in `merge-strategy.md`). If a second read on the same SHA still says `BLOCKED`, collect the evidence in this order:

```bash
# The PR's base branch and head SHA, used by every step below:
read -r BASE SHA < <(gh pr view PR --repo OWNER/REPO --json baseRefName,headRefOid --jq '"\(.baseRefName) \(.headRefOid)"')

# 1a. Rules from all rulesets on the base branch:
gh api --paginate "repos/OWNER/REPO/rules/branches/$BASE?per_page=100" \
  | jq -c '.[] | {type, ruleset_id, parameters}'

# 1b. Classic branch protection on the same branch. On an error gh prints the
#     error body to stdout, and jq would turn it into an all-null object that
#     looks like "nothing set" — so branch on the exit status and on stderr:
#     "Branch not protected (HTTP 404)" means there is none; any other error,
#     including "Not Found (HTTP 404)" for a caller without admin rights, means
#     the protection was not read.
if gh api "repos/OWNER/REPO/branches/$BASE/protection" > prot.json 2> prot.err; then
  jq '{
    reviews: (.required_pull_request_reviews // null | if . then del(.url, .bypass_pull_request_allowances) else . end),
    checks: .required_status_checks,
    conversation_resolution: .required_conversation_resolution.enabled,
    signatures: .required_signatures.enabled,
    enforce_admins: .enforce_admins.enabled}' prot.json
elif grep -q "Branch not protected" prot.err; then
  echo "no classic branch protection"
else
  cat prot.err; echo "classic protection NOT read"
fi

# 2. If either source sets a strict policy (strict_required_status_checks_policy
#    in a ruleset, required_status_checks.strict in classic protection), the head
#    must contain the base. Compare by SHA, which also works for a fork PR, whose
#    branch does not exist in the base repository:
gh api "repos/OWNER/REPO/compare/$BASE...$SHA" --jq '{behind_by, ahead_by}'

# 3. Every run on the head, including superseded ones, with the app that reported it
#    (a required context can name an integration_id; a run from another app does not count):
gh api --paginate "repos/OWNER/REPO/commits/$SHA/check-runs?per_page=100&filter=all" \
  --jq '.check_runs[] | "\(.name) \(.status)/\(.conclusion) app=\(.app.id)"'

# 4. Check suites on the head — a dynamic run (the Copilot review) appears here
#    but not in the GraphQL statusCheckRollup:
gh api --paginate "repos/OWNER/REPO/commits/$SHA/check-suites?per_page=100" \
  --jq '.check_suites[] | "\(.id) \(.app.slug) \(.status)/\(.conclusion)"'
```

`gh api repos/OWNER/REPO/rulesets` and `rules/branches/<base>` answer different questions: the first lists the rulesets defined on the repository, the second the ruleset rules that apply to the branch. Read the second, plus the classic protection, for a merge question.

A `pull_request` rule can carry parameters the review decision does not reflect, such as `require_extra_approval_for_unattributed_changes`. List such a parameter as a candidate that the API does not let you evaluate, never as the cause. Real case (2026-09-24, netresearch/t3x-nr-image-optimize#201): every required context from both sources was satisfied (success, or skipped for `scorecard`) and reported by the required app, the head was not behind, no thread was open, the review decision was `APPROVED` and both commits carried valid signatures, yet the PR stayed `BLOCKED` on every read at the same head over several hours, so the re-query did not clear it. A failed Copilot review suite (quota) sat outside the rollup; `merge-strategy.md` rules a quota-limited Copilot review out as a merge blocker, which leaves that parameter as the only named candidate. The operator reported the parameter as the cause ("needs a second approval"), which nothing had shown. The GitHub page meanwhile showed a required check as "Expected — waiting" that the API reported as successful.

On #201 the page and the API disagreed about that check: `security / Composer Audit` had a successful run on the head with a byte-identical name from the required app (`integration_id` 15368), and `isRequired: true` with `SUCCESS` in the rollup. Re-running the job added a second successful run and changed nothing.

What cleared it was closing and reopening the pull request: `BLOCKED` became `CLEAN` on the same head SHA, and the PR merged. That is a workaround, not a diagnosis. The reopen changed two things at once — the Composer Audit check reported again, and the auto-approve workflow ran again and posted a second `APPROVED` review — so either the stale "Expected" check or the second approval under `require_extra_approval_for_unattributed_changes` may have been the gate. The cause stays undetermined.

When a PR is stuck like this, in order:

1. Close and reopen the pull request. It sends the `pull_request` and `pull_request_target` events with the activity type `reopened`, so every workflow whose `types:` include it — the default types do — runs again on the same head; neither the code nor the history changes. Not every check run comes back on the head. On #201 the Codecov and SonarQube Cloud apps reported again; DCO and the dynamic Copilot review did not; the workflow jobs for CodeQL, Opengrep, betterleaks and zizmor ran again and uploaded new results, and the SonarQube Cloud app uploaded a new SonarCloud analysis, but GitHub Advanced Security created no new check run for `CodeQL`, `Opengrep OSS`, `SonarCloud`, `betterleaks` or `zizmor` on the head, whose earlier runs had already succeeded. Whether a reopen creates a required check that is missing entirely was not observed. The workflows that run again include approve and review workflows — on #201 the auto-approve job posted a second approval — and in a repository that requests Copilot or another review on these events, a reopen can put a review in flight that must finish before merging (see "Never merge while a review is announced or in flight" in `merge-strategy.md`). The existing approval was not dismissed on #201.
2. Only if that does not help, push a new commit. It triggers every workflow that runs on the `synchronize` activity of `pull_request` or `pull_request_target`, or on `push` (branch and path filters still apply), and it dismisses earlier approvals where `dismiss_stale_reviews_on_push` (ruleset) or `dismiss_stale_reviews` (classic protection) is set.

## Migrating Inline Jobs to Reusable Workflows Renames Every Required Check

A called workflow reports its checks as `<caller job name> / <inner job name>`,
so converting an inline job to `uses:` changes the context name even when the
job keeps its id. On a repository with required status checks the old context
then never reports again, and a required context that never reports blocks
merges forever — the PR sits at `BLOCKED` with every visible check green.

Three consequences, all of which bit a single `render-guides` migration:

- **The ruleset has to change in the same step.** Reproducing the old names is
  not possible: the ` / ` segment is always inserted, so an inline
  `Tests (8.2)` becomes at best `Tests / Tests (PHP 8.2)`.
- **No ordering keeps the gate closed.** Switching the ruleset first blocks
  every other open PR, whose checks still report the old names; merging first
  blocks the queue. The workable sequence is to drop the required contexts for
  the merge window and set the new ones immediately afterwards — a short,
  deliberate window without a gate, not something to discover mid-merge.
- **Steps promoted out of a required job become ungated.** Commands that ran as
  *steps inside* a required check are implicitly required. Split into their own
  called jobs they are separate checks and gate nothing unless the ruleset lists
  them. In the case above `composer normalize --dry-run`, `make test-docs` and
  `make test-rendertest` would have gone from required to optional as a side
  effect of a change whose subject was action-version hygiene.

Read the new names from a real run rather than predicting them — the inner job
name is defined in the called workflow, which may sit in another repository, and
it can carry its own matrix suffix:

```bash
gh api "repos/{owner}/{repo}/commits/<head-sha>/check-runs" --paginate \
  --jq '.check_runs[] | "\(.conclusion // .status)\t\(.name)"' | sort
```

Suffix matching belongs to *discovery*, not to configuration. Use it to find the
check run a reusable produced, then put its complete `.name` into the ruleset —
a required context is compared for equality, so `Tests (PHP 8.2)` as a required
context matches nothing and leaves the check pending forever. The rule against
`==` applies to your own filtering code (`gh pr checks` output, self-gating
workflows), where the caller prefix is not yours to know.

## Merge Queue Behavior and Pitfalls

### Sequential Processing

GitHub's merge queue processes PRs **one at a time**:

- Full CI runs for each PR before it merges
- Force-pushing a queued PR re-triggers CI from scratch and resets its position
- When the preceding PR merges, queued PRs behind it are effectively **rebased behind** — they must be rebased on the new `main`, force-pushed, and re-queued

### Force Push + Stale Review Dismissal Interaction

Rebasing before re-queuing triggers stale review dismissal, which cascades into an auto-approve requirement:

1. You force-push the rebased branch
2. `dismiss_stale_reviews_on_push: true` clears the previous approval
3. Auto-approve workflow must re-run to create a fresh approval
4. **Old review threads survive force push** — threads created against now-obsolete commits are still tracked by GitHub's conversation resolution requirement and still block merge

Explicitly resolve stale threads via GraphQL before re-queuing:

```bash
# Find thread IDs
gh api repos/OWNER/REPO/pulls/NUMBER/comments --jq '.[] | {id, node_id, body}'

# Resolve each thread
gh api graphql -f query='mutation { resolveReviewThread(input: {threadId: "PRRT_xxx"}) { thread { isResolved } } }'
```

### Multi-PR Workflow Pattern

When landing multiple dependent PRs, expect the dependent PRs to need rebasing after each merge:

```
1. Queue PR1 and PR2 (PR2 depends on PR1)
2. PR1 merges
3. PR2 is now behind — must be rebased:
   git fetch origin
   git rebase origin/main
   git push --force-with-lease
4. Force push dismisses approval → wait for auto-approve to re-run (or re-trigger it)
5. Resolve any stale review threads from old commits
6. Re-queue PR2:
   gh pr merge NUMBER --merge --auto
```

**Checklist before re-queuing after rebase:**

| Step | Command |
|------|---------|
| Rebase on latest main | `git rebase origin/main && git push --force-with-lease` |
| Trigger auto-approve | Wait for `pr-quality.yml` to run, or re-run it manually |
| Resolve stale threads | GraphQL `resolveReviewThread` for each stale thread |
| Re-enable auto-merge | `gh pr merge NUMBER --merge --auto` |

### Troubleshooting Merge Queue Issues

| Symptom | Cause | Fix |
|---------|-------|-----|
| PR exits queue after force push | CI reset on new push | Expected — wait for CI to pass again |
| PR stuck after preceding PR merged | PR is now behind `main` | Rebase, force push, re-queue |
| `REVIEW_REQUIRED` after rebase | Stale review dismissal cleared approval | Re-run auto-approve workflow |
| Unresolved threads block merge | Old threads survive rebase | Resolve via GraphQL `resolveReviewThread` |
| Armed (`autoMergeRequest` set) but never enters the queue | First `--auto` armed auto-merge without enqueuing — checks are green, no threads, yet `mergeQueue.entries` is empty and the PR just sits | Re-issue `gh pr merge NUMBER --auto`; it reports "already queued to merge" and the entry then shows `AWAITING_CHECKS`. Confirm with the [`mergeQueue.entries` GraphQL query](#verifying-a-pr-actually-merged-enqueue--merged) — do not assume arming enqueued it |

### Verifying a PR Actually Merged (enqueue ≠ merged)

On a merge-queue repo, `gh pr merge … --merge` (or `--auto`) only **enqueues** the PR —
the command returns success immediately and the PR is **still open**. Don't report
"merged" off the exit code; the queue runs its own CI first and merges later (minutes,
if the queue runs the full matrix). It can also silently stall.

The queue runs CI on a synthetic branch named `gh-readonly-queue/<base>/pr-<N>-<sha>`.
To find that CI and confirm the PR lands:

```bash
# Is it queued, and at what position?
gh api graphql -f query='query($owner:String!,$repo:String!){
  repository(owner:$owner,name:$repo){
    mergeQueue { entries(first:10){ nodes{ position state pullRequest{ number } } } } } }' \
  -f owner=OWNER -f repo=REPO \
  --jq '.data.repository.mergeQueue?.entries?.nodes[]? // empty'

# Watch the queue's own CI (note the merge_group event, not pull_request)
gh run list --repo OWNER/REPO --event merge_group --limit 5 \
  --json status,conclusion,headBranch,name \
  --jq '.[] | select(.headBranch|test("pr-<N>-")) | "\(.status)/\(.conclusion // "-") \(.name)"'

# Confirm it actually merged (state MERGED + branch gone)
gh pr view <N> --repo OWNER/REPO --json state,mergedAt,mergeCommit \
  --jq '{state, mergedAt, mergeCommit: (.mergeCommit?.oid // "none")}'
```

Poll `state == "MERGED"` (or a `merge_group` run concluding `failure`) before declaring
done — green checks on the PR head are necessary but not sufficient once a queue is in
play.

## Signed Commits and Merge Strategy Compatibility

GitHub can only auto-sign **merge commits** and **squash merges**. It **cannot** auto-sign rebased commits. If branch protection requires signed commits and the workflow uses `--rebase`, merges fail with:

> `Base branch requires signed commits. Rebase merges cannot be automatically signed by GitHub.`

### Auto-detect Merge Strategy

Instead of hardcoding `--merge`, `--squash`, or `--rebase`, auto-detect from repo settings:

```bash
STRATEGY=$(gh api "repos/${{ github.repository }}" --jq '
  if .allow_squash_merge then "--squash"
  elif .allow_merge_commit then "--merge"
  elif .allow_rebase_merge then "--rebase"
  else "--squash" end')
gh pr merge --auto $STRATEGY "$PR_URL"
```

**Priority order:** squash > merge > rebase. Squash is preferred because:
1. Works with signed commit requirements (GitHub can sign squash merges)
2. Clean history for single-commit dependency PRs
3. Most universally compatible

### Enabling Squash Merge on Repos

If a repo only allows rebase merges and requires signed commits, enable squash:

```bash
gh api repos/OWNER/REPO -X PATCH -f allow_squash_merge=true
```

## Workflow File Changes Cannot Be Auto-merged

PRs that modify `.github/workflows/` files cannot be merged by `GITHUB_TOKEN` — it lacks the `workflows` permission scope. This commonly affects Dependabot/Renovate PRs that update GitHub Actions versions.

**Detection:** The `auto-merge-deps.yml` workflow should check for workflow file changes before attempting merge:

```bash
WORKFLOW_FILES=$(gh pr diff "$PR_URL" --name-only | grep -E '^\.github/workflows/' || true)
if [ -n "$WORKFLOW_FILES" ]; then
  echo "PR modifies workflow files — requires manual merge"
fi
```

**Resolution:** Merge manually using a local clone with SSH authentication:

```bash
# For repos without branch protection (direct push allowed):
git clone --depth=5 git@github.com:OWNER/REPO.git /tmp/REPO
cd /tmp/REPO
BRANCH=$(gh pr view NUMBER --repo OWNER/REPO --json headRefName --jq '.headRefName')
git fetch origin "$BRANCH"
git merge --no-ff -S --signoff "origin/$BRANCH" -m "Merge pull request #NUMBER from OWNER/$BRANCH"
git push origin MAIN_BRANCH
```

**For repos with multiple workflow PRs:** Merge sequentially — each subsequent PR may need rebasing after the previous one merges since they typically touch the same workflow files.

## Batch Auto-merge for Multiple PRs

When enabling auto-merge across many repos/PRs at once:

```bash
gh pr merge NUMBER --repo OWNER/REPO --auto --merge
```

**Limitations discovered:**
- "Pull request Auto merge is not allowed for this repository" means the repository setting `allow_auto_merge` is `false` (measured 2026-10-21/22 in six netresearch repositories, merge-queue ones included). Check it with `gh api repos/OWNER/REPO --jq .allow_auto_merge` and enable it with `gh api -X PATCH repos/OWNER/REPO -F allow_auto_merge=true`; `init-branch-protection.sh --merge-queue` does this for a queue repository. A timing cause (a second PR rejected while the first is pending) was reported earlier but has not been measured.
- Repos where you lack admin/maintainer access will fail with permission errors

## Archived Repos — Handle Dependabot/Renovate PRs with Care

Archived repositories still receive Dependabot/Renovate PRs, but you cannot
merge them or enable auto-merge — writes are blocked, and auto-merge fails with a
permission error. Don't fight it:

1. **Unarchive** the repo.
2. **Close** the PR (or merge it, if the update is genuinely wanted).
3. **Re-archive** the repo.

Before any batch auto-merge sweep across an org, filter archived repos out first
so they don't generate noise:

```bash
# gh filters archived repos out server-side:
gh repo list ORG --no-archived --json name --jq '.[].name'
```

Never enable auto-merge on an archived repo — it errors and leaves the PR in a
confusing half-state.

## Recommended Renovate Config for Auto-merge

```json
{
  "extends": ["config:recommended"],
  "automergeType": "pr",
  "platformAutomerge": true,
  "lockFileMaintenance": {
    "enabled": true,
    "schedule": ["before 6am on monday"]
  },
  "packageRules": [
    {
      "matchUpdateTypes": ["patch", "minor", "pin", "digest"],
      "automerge": true
    }
  ]
}
```

**Key settings:**
- `platformAutomerge: true` - Renovate enables auto-merge (uses bypass permissions)
- `lockFileMaintenance` - Handles lock file updates via PR (not direct push)

**The `renovate/stability-days` check (produced by the `minimumReleaseAge` config option, formerly `stabilityDays`) keeps an armed PR `UNSTABLE` on purpose.** A Renovate PR with auto-merge armed, every real check green, and only `renovate/stability-days` PENDING is not stuck — the pending status *is* the supply-chain delay, and Renovate completes the merge when the window elapses. `mergeStateStatus` shows `UNSTABLE` the whole time. Leave it alone; merging by hand defeats the deliberate release-age gate.

## Canonical Auto-merge Workflow Template

```yaml
name: Auto-merge dependency PRs

on:
  pull_request_target:
    types: [opened, synchronize, reopened]

permissions:
  contents: write
  pull-requests: write

jobs:
  auto-merge:
    runs-on: ubuntu-latest
    # The bot must be the PR author (user.login) AND the actor of the event
    # (github.actor). The author alone lets a human push to a bot branch, or a
    # human reopen, get approved and merged unreviewed. github.actor keeps the
    # original actor on a re-run. zizmor's bot-conditions audit flags every
    # github.actor check; here it only narrows the author check.
    if: >- # zizmor: ignore[bot-conditions] -- in addition to the author check
      (github.event.pull_request.user.login == 'dependabot[bot]' ||
       github.event.pull_request.user.login == 'renovate[bot]') &&
      (github.actor == 'dependabot[bot]' ||
       github.actor == 'renovate[bot]')
    steps:
      - name: Approve PR
        env:
          PR_URL: ${{ github.event.pull_request.html_url }}
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: gh pr review --approve "$PR_URL"

      - name: Enable auto-merge
        env:
          PR_URL: ${{ github.event.pull_request.html_url }}
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          REPO: ${{ github.repository }}
        run: |
          STRATEGY=$(gh api "repos/$REPO" --jq '
            if .allow_squash_merge then "--squash"
            elif .allow_merge_commit then "--merge"
            elif .allow_rebase_merge then "--rebase"
            else "--merge" end')
          gh pr merge --auto "$STRATEGY" "$PR_URL"
```

### Key Design Decisions

- **`pull_request_target`**: Required for bot PRs — `pull_request` runs with read-only tokens for fork-like contexts
- **`user.login` and `github.actor`**: the bot must be the PR author and the actor of the event; the author alone merges a human's push to a bot branch (see dependency-management.md, "Bot Detection Needs the Author AND the Actor")
- **`--auto`**: Respects branch protection, merge queues, and required checks — direct merge bypasses these
- **Dynamic strategy**: Repos may only allow specific merge methods — hardcoding breaks when config changes

## Branch Protection for Auto-merge

```bash
# Check required checks vs actual check names
gh api repos/OWNER/REPO/branches/main/protection/required_status_checks --jq '.checks[].context'

# Check code owner requirement (should be false for auto-merge)
gh api repos/OWNER/REPO/branches/main/protection/required_pull_request_reviews --jq '.require_code_owner_reviews'

# Check bypass apps
gh api repos/OWNER/REPO/branches/main/protection/required_pull_request_reviews --jq '.bypass_pull_request_allowances.apps[].slug'

# Fix: Disable code owner reviews, add bypass apps
gh api repos/OWNER/REPO/branches/main/protection/required_pull_request_reviews -X PATCH \
  --input - << 'EOF'
{
  "require_code_owner_reviews": false,
  "required_approving_review_count": 1,
  "bypass_pull_request_allowances": {
    "apps": ["dependabot", "renovate"]
  }
}
EOF
```

## Auto-merged PRs leave the base branch without post-merge CI

A merge performed with `GITHUB_TOKEN` — which is what the auto-merge workflow
uses, directly or via `gh pr merge --auto` — does not trigger further workflow
runs. GitHub suppresses workflow triggers for events created by that token, so
the `push` to the base branch produces nothing. Measured on one repository:

| Merge commit | Merged by | push-triggered CI runs on `main` |
|---|---|---|
| `699df245` | maintainer (`gh pr merge`) | 5 |
| `162c57b7` | maintainer (`gh pr merge`) | 5 |
| `ddc3810a` | auto-merge workflow | **0** |
| `5a513fe1` | auto-merge workflow | **0** |
| `875fb1a4` | auto-merge workflow | **0** |
| `c61d560f` | auto-merge workflow | **0** |

Rule out the cheaper explanation first — a `paths`/`paths-ignore` filter on the
`push` trigger produces the same symptom:

```bash
gh api repos/$R/contents/.github/workflows/ci.yml --jq .content | base64 -d | yq '.on'
```

On its own the missing run is tolerable, because the PR's own CI covered the
head commit. It becomes a hole when combined with a non-strict status-check
policy: the PR may have been tested against a `main` that has since advanced,
and nothing ever tests the combination.

```bash
gh api repos/$R/rules/branches/main \
  --jq '.[]|select(.type=="required_status_checks")|.parameters'
# strict_required_status_checks_policy: false  →  stale PRs may merge untested
```

Two fixes, in increasing strength:

1. **`strict_required_status_checks_policy: true`** — one flag. GitHub holds the
   merge until the branch is current, so the tested tree equals the merged tree
   and the missing post-merge run stops mattering. Cost: every base-branch push
   invalidates open PRs, which then need an update (`allow_update_branch: true`
   and the bots handle their own). Reversible with one API call — back the
   ruleset up first (`gh api repos/$R/rulesets/$ID > backup.json`).
2. **Merge queue** — tests the merge *result* before it lands, and covers
   maintainer merges too. Needs a `merge_group:` trigger in the CI workflow and
   queue configuration in the ruleset.

Do **not** try to bolt a post-merge `workflow run` dispatch onto the auto-merge
job. `workflow_dispatch` and `repository_dispatch` are indeed the documented
exceptions to the `GITHUB_TOKEN` suppression, but when the base branch has
required checks the job takes the native path — `gh pr merge --auto` followed by
`exit 0` — and finishes long before GitHub performs the merge. There is no point
in that job at which the merge commit exists.

## Auto-merge can land a bot PR while you are still fixing it

In a repo with an auto-merge deps workflow, pushing a fix to a bot PR's branch
starts a clock: as soon as the required checks go green the workflow merges,
with no further confirmation. Two dependency PRs merged four minutes apart while
a correction to one of them was still being verified locally — the flawed commit
reached the base branch and needed a follow-up PR instead of an amend.

Treat "pushed and green" as "merged" on those branches:

- Finish verification *before* the push that turns the PR green, not after.
- Once it is green, plan on a follow-up PR against the base branch. Amending and
  force-pushing races the workflow and fails with `stale info` once the branch
  is deleted post-merge.
- Check whether the merge already happened before diagnosing a push failure:
  `gh pr view $PR --repo $R --json state,mergedAt,mergedBy`.

## Auto-merge proves only what the PR's own checks run

A green dependency PR says nothing about a workflow that no check on that PR
executes. A workflow triggered only by `schedule` or `workflow_dispatch` is the
common case: when Renovate bumps `python-version`, an action or a pinned tool
inside it, the PR's checks are the *other* workflows, they pass, and the
auto-merge workflow merges. The bumped workflow first runs at its next schedule
or dispatch, on the base branch, and fails there.

Measured on one repository: Renovate moved a nightly dashboard workflow from
Python 3.14 to 3.15. Its install step is
`pip install --only-binary :all: … PyYAML==6.0.3`, and PyYAML 6.0.3 publishes
no cp315 wheel, so every nightly run failed with
`No matching distribution found for PyYAML==6.0.3`. The PR had merged green,
because the test workflow installs a different requirements file. Eight
nightly runs failed before the fix merged.

Find the workflows that a bump PR cannot exercise:

```bash
# Workflows without a pull_request / pull_request_target / merge_group trigger
for f in .github/workflows/*.y*ml; do
  yq -e '.on | has("pull_request") or has("pull_request_target") or has("merge_group")' "$f" >/dev/null 2>&1 \
    || echo "$f: $(yq -o=json -I=0 '.on | keys' "$f")"
done
```

Give each such workflow a PR-time check that runs its fragile steps — the
runtime setup and the dependency install — and nothing that writes:

```yaml
on:
  schedule:
    - cron: '0 3 * * *'
  workflow_dispatch:
  pull_request:
    paths:
      - .github/workflows/impact-dashboard.yml   # only PRs that change this file

permissions:
  contents: read                                 # the default for every job

env:
  DASHBOARD_DEPS: requests==2.34.2 PyYAML==6.0.3 Jinja2==3.1.6

jobs:
  install-check:
    if: github.event_name == 'pull_request'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/setup-python@<sha>  # vX
        with:
          python-version: '3.14'                 # keep identical to the build job
      - run: |
          # shellcheck disable=SC2086
          pip install --only-binary :all: $DASHBOARD_DEPS

  build:
    # Name the events that may publish. `!= 'pull_request'` would also run the
    # publisher on a merge_group trigger added later.
    if: github.event_name == 'schedule' || github.event_name == 'workflow_dispatch'
    runs-on: ubuntu-latest
    permissions:
      contents: write                            # publishing needs it, the check does not
    concurrency:                                 # job level: PR checks must not queue
      group: impact-dashboard                    # behind the nightly publisher
      cancel-in-progress: false
    # … unchanged steps, installing $DASHBOARD_DEPS …
```

Three details decide whether the check works:

- **Keep `python-version` a literal in both jobs.** Renovate opened the bump
  from the literal `with:` value of `setup-python`, and one PR updated every
  such literal in the repository. An `${{ env.… }}` expression in that place is
  not a version string; do not trade the duplicated literal for one, or the
  bump PR, and with it the check, may never come.
- **The auto-merge workflow must wait for this check.** Read which path the
  repository takes (§ *`mergeStateStatus: BLOCKED` — Check Required vs
  Non-Required Checks First*).
  - Without required checks, the shared `auto-merge-deps.yml` gates on every
    check of the PR itself; a failed `install-check` stops the merge, and the
    `paths:` filter above is fine.
  - With required status checks, only those hold a native auto-merge, so
    `install-check` has to become one. Then drop the workflow-level `paths:`
    filter: a required check whose workflow a path filter skipped stays
    pending, and every unrelated PR is blocked. Run the job on every PR; it
    takes seconds. To limit it to changes of this file anyway, trigger on
    every PR and decide inside the job whether to run the install steps, so
    the job always reports.
  - With a merge queue, also add `merge_group:` to `on:` and let
    `install-check` run for it (`if: github.event_name == 'pull_request' ||
    github.event_name == 'merge_group'`); a required check that never reports
    on the merge-group commit holds the queue.
- **Prove the check against the failing version before relying on it.** Run the
  step from the file, not a retyped copy, in the official image of both
  versions; the old one must pass and the new one must fail:

  ```bash
  RUN="$(yq -r '.jobs.build.steps[] | select(.name=="Install dependencies") | .run' .github/workflows/impact-dashboard.yml)"
  for v in 3.14 3.15; do
    docker run --rm -e DASHBOARD_DEPS="$(yq -r .env.DASHBOARD_DEPS .github/workflows/impact-dashboard.yml)" \
      python:$v bash -ec "$RUN"; echo "$v exit=$?"
  done
  ```

The check fails a premature bump and passes on its own once the dependency
ships support, so it needs no later clean-up. A Renovate `allowedVersions` cap
reaches the same safety but stays in place until someone remembers to lift it.

A converted `run:` line can also break the file itself:
`pip install --only-binary :all: $DEPS` is not a valid plain YAML scalar,
because a colon followed by a space starts a mapping. Keep a block scalar
(`run: |` or `run: >-`) and run `actionlint` before pushing.



--- FILE: skills/github-project/references/branch-migration.md ---

<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->
<!-- SPDX-FileCopyrightText: Netresearch DTT GmbH -->

# Branch Migration Reference

Guide for migrating from `master` to `main` as default branch.

## Migration Steps

### Step 1: Rename the branch on GitHub

GitHub renames a branch in one call. The rename moves the branch
protection, retargets open pull requests, redirects old URLs, and — for
the default branch — changes `default_branch` too:

```bash
# Back up the current protection first (admin-only endpoint)
gh api repos/{owner}/{repo}/branches/master/protection > master-protection.backup.json

gh api -X POST repos/{owner}/{repo}/branches/master/rename -f new_name=main \
  --jq '{name, protected}'

# Read back — a 2xx is not proof
gh api repos/{owner}/{repo} --jq .default_branch            # main
gh api repos/{owner}/{repo}/branches --jq '.[].name'         # no master
gh api repos/{owner}/{repo}/branches/main/protection \
  --jq '{rcr: .required_conversation_resolution.enabled, fp: .allow_force_pushes.enabled}'
```

Do not push `main` and delete `master` by hand instead. GitHub refuses to
delete the default branch, and the manual path leaves open pull requests on
a base that no longer exists.

### Step 2: Prevent master from being re-created

Block the name with a **ruleset**, the same shape the Netresearch fleet uses
(e.g. `netresearch/go-cron`, ruleset "Block master branch recreation"):

```bash
gh api -X POST repos/{owner}/{repo}/rulesets --input - <<'EOF'
{"name": "Block master branch recreation", "target": "branch",
 "enforcement": "active", "bypass_actors": [],
 "conditions": {"ref_name": {"include": ["refs/heads/master"], "exclude": []}},
 "rules": [{"type": "creation"}]}
EOF

gh api repos/{owner}/{repo}/rules/branches/master --jq '[.[].type]'   # ["creation"]
```

Prove the guard fails before relying on it — a push of `master` must be
refused, admins included:

```bash
git push origin refs/remotes/origin/main:refs/heads/master
# remote: - Cannot create ref due to creations being restricted.
# ! [remote rejected] ... (push declined due to repository rule violations)
```

Classic branch protection cannot do this: `PUT .../branches/master/protection`
answers `404 Branch not found` once the branch is gone. Rulesets are available
on public repositories and on paid plans; a free-plan private repository
answers 403.

### Step 3: Update the local clone

```bash
git branch -m master main
git fetch origin --prune
git branch -u origin/main main
git remote set-head origin -a
```

In a bare-repo worktree layout (`.bare/` + one folder per branch) the bare
repository's `HEAD` points at `master` too:

```bash
git -C .bare worktree remove ../master
git -C .bare branch -m master main
git -C .bare symbolic-ref HEAD refs/heads/main
git -C .bare fetch --prune origin
git -C .bare branch -u origin/main main
git -C .bare worktree add ../main main
git -C .bare remote set-head origin -a
```

### Step 4: Update CI/CD workflows

```bash
grep -rn "master" .github/workflows/
# Common patterns to update:
# - branches: [master] → branches: [main]
# - refs/heads/master → refs/heads/main
```

**Check `.github/template.yaml` first.** In a repository managed by a
`netresearch/.github` template, the workflow files are copies of the
template, and the `Template Drift` check fails on any local edit. The
templates keep `branches: [main, master]` on purpose, so leave those lines
alone; a blanket `sed s/master/main/g` breaks the drift check. Do not touch
`dev-master` constraints on *dependencies* in `composer.json` either — they
name the dependency's branch, not this repository's.

### Step 5: Update documentation

Search and replace branch references:
```bash
# Find all references to master branch in docs
grep -rn "master" --include="*.md" --include="*.rst" --include="*.txt"
```

| File | Pattern | Update to |
|------|---------|-----------|
| README.md | `badge/branch-master` | `badge/branch-main` |
| README.md | `github.com/org/repo/tree/master` | `tree/main` |
| README.md | `github.com/org/repo/blob/master` | `blob/main` |
| README.md | `?branch=master` | `?branch=main` |
| CONTRIBUTING.md | "merge into master" | "merge into main" |
| docs/*.md | `/master/` links | `/main/` |
| package.json | `"repository": "...#master"` | `#main` |
| composer.json | `"dev-master"` or `#master` | `"dev-main"` or `#main` |

```bash
# Bulk update in markdown files
find . -name "*.md" -exec sed -i 's|/master/|/main/|g; s|/master"|/main"|g; s|branch-master|branch-main|g' {} \;
```

### Step 6: Notify team

Team members must update local repos:
```bash
git checkout master
git branch -m master main
git fetch origin
git branch -u origin/main main
git remote set-head origin -a
```



--- FILE: skills/github-project/references/ci-runner-capacity.md ---

<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->
<!-- SPDX-FileCopyrightText: Netresearch DTT GmbH -->

# CI Runner Capacity — Diagnose Before You Optimize

A PR-to-release delay can contain review wait, workflow concurrency wait,
dependency wait, runner acquisition, execution, artifact transfer and publication.
Measure the complete path before changing parallelism. A below-cap peak alone
cannot distinguish an idle dependency graph from delayed runner acquisition.

## Establish the scope and quality contract

Inventory workflow **files**, triggered **runs**, expanded **jobs**, assigned
runner records and actual executions separately. One file can expand into many
matrix cells; several trigger events can repeat the same work. Count the PR,
merge-group and main graphs independently, including reusable workflows,
`needs`, conditions, environments, concurrency groups and publication triggers.
Preserve the required checks, supported matrix, suites, thresholds and qualified
review policy while optimizing.

GitHub-hosted standard concurrency is shared by the owning account, across
repositories. Check the [current limits](https://docs.github.com/en/actions/reference/limits)
and the account's actual support-adjusted allocation and runner types. A plan's
published default is a reference, not proof of the effective cap. Larger,
macOS, GPU and self-hosted pools can have different constraints. Do not infer
pool membership from a runner ID alone.

## Collect a reproducible cohort

The read-only collector retains successful API response bodies with their endpoint
and read times, explicit API hostname and authenticated principal, paginates repositories,
runs and jobs, and reads every run attempt. It re-reads each run after its jobs
and compares the final run and organization-repository inventories; a revision
or repository identity change makes the report incomplete.
It never cancels, reruns, changes rules or enqueues anything.
Failed reads retain the endpoint, read times and redacted error class. Subprocess
arguments, stderr and credentials are not copied into the report.

```bash
uv run skills/github-project/scripts/collect-runner-capacity.py \
  --org OWNER --since 2026-10-28T00:00:00Z --until 2026-10-29T00:00:00Z \
  > capacity.json
# Or --repo OWNER/REPO (repeatable); optional --head OWNER/REPO=40_HEX_SHA
jq '{complete, scope, errors, reads: (.reads | length)}' capacity.json
```

The scope is runs **created** in the specified window, among repositories
visible to the token. A prior-day run still executing can be absent: widen the
window and check older active runs before claiming an organization-wide live
backlog. Reads are non-atomic. Repository visibility and any failed page are
coverage limits, never evidence that unseen work is absent. A run search at
GitHub's 1,000-result ceiling returns incomplete: split the time window and
collect again. `complete: true` means the declared cohort was collected without
a detected error; it does not certify token visibility or an atomic snapshot.

`--head` matches repository names without regard to case and labels other heads
as obsolete **without dropping their cost**. Repeated repository names that
differ only in case are collected once; the first spelling and supplied head
selectors remain in the scope record.
Conflicting SHA selectors for the same repository, including aliases that differ
only in case, are rejected before any API request. Equivalent duplicate selectors
are accepted.
Without an explicit expected head, currency is unspecified. Keep older pushes,
cancellations, duplicate events and reruns in the cost inventory; select the
current qualifying head separately for the release decision. Run attempts can
carry successful jobs with new administrative IDs and old execution times, so
do not sum attempt records as fresh executions. Use step times, runner identity
and logs to distinguish a real rerun from a carried result.

Sources: [workflow runs](https://docs.github.com/en/rest/actions/workflow-runs),
[workflow jobs](https://docs.github.com/en/rest/actions/workflow-jobs).

## Attribute time before choosing the lever

- **Assigned jobs:** a nonzero runner ID shows assignment. Unassigned queued
  records can still be waiting on `needs`, an environment approval or a
  concurrency group. A run-level `queued` status can coexist with running jobs;
  inspect jobs rather than treating every queued run as executor backlog.
- **Waiting:** `started_at - created_at` is an observed interval, not a measured
  executor queue. Establish when dependencies, conditions and approvals cleared
  from the workflow graph and event/log evidence. If that moment is unavailable,
  label readiness and executor wait unknown. Summed job waits overlap and do not
  equal the PR's elapsed wait.
- **Compute:** sum verified execution intervals for runner cost, grouped by
  runtime/pool. Compute peak occupancy by sweeping start/end events over the
  same observation window; separate historical carried records and incomplete
  intervals. An observed peak is a lower bound under incomplete coverage.
- **Critical path:** reconstruct dependencies and timestamps from PR creation
  through qualified reviews, checks, merge queue, main checks, release evidence
  and publication. Attribute each elapsed segment once. Contrast the critical
  path with summed runner time; faster off-path work can reduce cost without
  advancing publication.

Only diagnose a capacity cap when **ready** jobs compete with concurrent work
in the same constrained pool. A below-cap peak may instead mean dependencies,
conditions, serialized concurrency groups, different pools or missing data; it
does not establish acquisition-bound behavior or prove that job count is
irrelevant. Observe comparable windows across other repositories before blaming
GitHub's shared scheduler.

## Choose and verify the change

Reduce duplicate/obsolete PR work and repeated setup first. Coalescing jobs can
reduce acquisitions, but retain independent results, dependency/runtime
contracts, deadlines and failure diagnostics. Never trim a supported matrix or
move required tests to a schedule just to improve latency. More parallel jobs
can help an available pool and delay other repositories under contention.

Use PR cancellation for superseded PR revisions; preserve admitted merge-group,
main and release work. Tune merge-queue build concurrency against the entire
organization's ready width, not the target repo alone. Change required-context
names with their effective rules and validate every trigger path. Capacity
purchases or self-hosted runners require their own cost/security decision and
measured benefit; a higher cap does not guarantee faster acquisition.

Compare before/after cohorts with the same quality contract and similar queue
pressure. Report critical-path elapsed time, actual executions, runner-minutes,
obsolete work, coverage gaps and uncertainty. One faster run is an observation,
not a causal throughput result.

## Persist tool caches written inside `docker compose run --rm`

A linter/analyzer run inside `docker compose run --rm` writes to the container's
ephemeral filesystem — anything under the container's `/tmp` is discarded every
run and is uncacheable. Point the tool's cache at a **host-mounted** repo path
(PHPStan `tmpDir: var/cache/phpstan`, Rector `->withCache('var/cache/rector')`),
then `actions/cache` it:

- **Key** on `${{ github.run_id }}` (unique → never hits → always saves a fresh
  cache post-job) with `restore-keys` set to the key's prefix (restores the most
  recent prior cache) — save-fresh + restore-latest = incremental warmth.
- **Safe stale restore:** the tools self-invalidate (PHPStan salts on
  config+composer+PHP; Rector on the config-file hash), so a restored-but-stale
  cache only recomputes changed files, never a wrong result — so *don't* bake a
  content hash into the key; it just fragments the cache lineage.
- **uid:** the container writes as root (umask 022 → 0644 files), so the post-job
  save (runner user) reads them without a chmod.

Measured: a PHPStan-heavy Lint job dropped ~145s cold → ~72s warm.

## Verify every trigger path after a conditional change

When a workflow behaves differently by `github.event_name` / a flag / a matrix
cell, a green run of ONE path is not "done" — each path is separate code. Gating
coverage steps on `schedule` leaves the `pull_request` run green while the
coverage-on (`schedule`) path still hides a bug (e.g. a job that now exceeds its
`timeout-minutes`). Exercise the non-PR path on demand with `workflow_dispatch`
— but the trigger must already exist on the **default branch** to be
dispatchable. If it's *new in the PR*, that path is only verifiable after merge;
if it already exists on the default branch, you can dispatch the PR branch's
version directly. Either way, check it; don't assume.

## Scheduled runs cancelled by a push in the same concurrency group

A workflow with `concurrency: group: ${{ github.workflow }}-${{ github.ref }}`
puts `schedule`, `workflow_dispatch` and `push` runs on the default branch into
one group. With the default `queue: single`, GitHub keeps at most one
**pending** run per group: a newer run replaces the pending one even with
`cancel-in-progress: false`. That setting only protects the run that is already
**running**. (`queue: max` allows up to 100 pending runs, but GitHub rejects it
in combination with `cancel-in-progress: true` — see the fix below.)

A nightly run that waits behind a running push run is therefore cancelled by
the next push, before it starts a job. Observed in netresearch/t3x-nr-llm:
scheduled run 39209624988 (2026-10-19) was created at 06:23:25, waited behind
a push run that was still running, and was cancelled at 06:33:06 — one second
after push run 39210564782 was created.

Signature: conclusion `cancelled`, zero jobs, and a run of another event
created in the same group within a second of the cancellation. The second
command below lists candidates only: it shows creation times, not the group, so
confirm that the candidate's event and ref fall into the same group and that its
`created_at` matches the cancelled run's `updated_at`.

```bash
R=OWNER/REPO; RUN=RUN_ID
# 0 = the run never started a job
gh api "repos/$R/actions/runs/$RUN/jobs?per_page=100" --paginate --jq '.jobs|length'
# The cancellation time of the run under suspicion
gh api "repos/$R/actions/runs/$RUN" --jq '"\(.event) \(.head_branch) \(.updated_at)"'
# Candidates for the replacing run (same workflow and branch, created around then)
gh api "repos/$R/actions/workflows/ci.yml/runs?branch=main&created=FROM..TO" \
  --jq '.workflow_runs[] | "\(.id) \(.event) \(.created_at) \(.conclusion)"'
```

Fix: give schedule and manual runs their own group and leave the other groups
as they are:

```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}${{ (github.event_name == 'schedule' || github.event_name == 'workflow_dispatch') && format('-{0}', github.event_name) || '' }}
  cancel-in-progress: ${{ github.event_name == 'pull_request' }}
```

Push and pull-request runs keep the group they had; only pull-request runs
cancel their predecessor. `queue: max` is no alternative here: the
`cancel-in-progress` expression is true for pull requests, and GitHub refuses
`queue: max` together with `cancel-in-progress: true`. Where a workflow never
cancels in progress, `queue: max` in the shared group keeps the scheduled run
waiting instead. Applied in netresearch/t3x-nr-llm#1155
(<https://github.com/netresearch/t3x-nr-llm/pull/1155>).



--- FILE: skills/github-project/references/cross-repo-references.md ---

<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->
<!-- SPDX-FileCopyrightText: Netresearch DTT GmbH -->

# Cross-Repo Issue/PR References in Markdown

GitHub autolinks a bare `#NN` in an issue/PR/comment body to an issue or PR **in
the same repository**. When the number belongs to a *different* repo, a bare
`#NN` silently links to the wrong target — it does not error, it renders as a
valid link pointing somewhere unintended.

## The trap

The failure is invisible in the source and only wrong at render time. It bites
hardest in a repo literally named `.github`, where a stray `#137` resolves to
`owner/.github#137` — usually an unrelated PR that happens to share the number.

```markdown
<!-- Written in owner/.github, meaning owner/other-repo#137 -->
root-caused via owner/other-repo#136 / #137
                                        ^^^^  links to owner/.github#137 — WRONG
```

Note that `owner/other-repo#136` is fine (it carries the repo), while the
adjacent bare `#137` is not — mixed forms in one sentence are a common source of
this bug.

## The rule

A cross-repo reference must carry the repo. Use one of:

```markdown
owner/repo#137                                   <!-- full autolink form -->
[#137](https://github.com/owner/repo/pull/137)   <!-- explicit markdown link -->
```

A bare `#137` is correct **only** when it targets the same repo the body lives
in. When in doubt, use the explicit markdown link — it is unambiguous and
survives the body being copied into another repo.

## Verifying before you post

Render the body through GitHub's GFM API and check where each reference actually
points, rather than eyeballing the source:

```bash
jq -Rs --arg ctx "owner/repo" '{text:., mode:"gfm", context:$ctx}' body.md \
  | gh api -X POST /markdown --input - \
  | grep -oE 'href="[^"]*/(pull|issues)/[0-9]+"'
```

Any `href` pointing at a repo you did not intend is a bare-reference bug — fix
it to `owner/repo#NN` or a markdown link. A quick pre-scan for the risky pattern
(a `#NN` not preceded by a repo name) narrows where to look:

```bash
grep -noE '[^/A-Za-z0-9_.-]#[0-9]+' body.md
```

## Referencing code: a permalink needs a commit SHA

Pointing at source in an issue, PR or review comment fails the same way a bare
`#NN` does: the link looks right and quietly means something else.

GitHub renders the **embedded code preview** — file, line range, syntax
highlighting, always matching what it points at — only for a URL that carries a
**commit SHA** and sits alone on its own line:

```markdown
https://github.com/owner/repo/blob/0000000000000000000000000000000000000000/src/File.php#L164-L173
```

A `/blob/<tag>/…` or `/blob/<branch>/…` link is **not** a permalink. It renders
as a bare link with no preview, and later resolves to different code, because
both refs move. In the browser, `y` rewrites the address to the permalink form.

**The preview has two limits worth knowing before you rely on it.** It renders
only in a **comment** — issue, PR, review — never in a Markdown file in the
repository. And it renders only where the comment lives in the **same
repository** as the linked code; a permalink into another repository stays a
plain URL. Cross-repo, the SHA still buys the thing that matters most — the link
keeps pointing at the code you meant — so use it there too, and write the
sentence so it reads without the preview.

Two consequences follow:

**Do not paste the code next to the link.** A rendered permalink already shows
the source. A copy beside it is duplication that goes stale, and an abbreviated
one (`...` in the middle) is strictly worse than the preview it replaces.

**Resolve the SHA, then re-check the line numbers against that SHA.** Line
numbers taken from a tag or a local checkout may not line up with the commit you
end up linking. A report whose snippet does not match its line numbers invites
exactly the question you least want — "was the file modified locally?" — and
upstream maintainers have closed reports on that basis.

```bash
repo=owner/repo; ref=v1.2.3; path=src/File.php
sha=$(gh api "repos/$repo/commits/$ref" --jq .sha)
gh api "repos/$repo/contents/$path?ref=$sha" --jq .content \
  | base64 -d | sed -n '164,173p'     # confirm the range before linking it
```

The placeholders are variables on purpose: written inline as `<tag-or-branch>`,
the shell reads `<` as a redirection and the command runs without the ref
instead of failing loudly.



--- FILE: skills/github-project/references/dependency-management.md ---

<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->
<!-- SPDX-FileCopyrightText: Netresearch DTT GmbH -->

# Dependency Management Reference

Dependabot and Renovate configuration patterns, auto-merge workflows, and troubleshooting.

## Dependabot

### Ecosystem Hygiene — Only Declare What the Repo Actually Has

Dependabot's update job runs on the ecosystems configured, whether or not the manifest files exist. Some ecosystems **hard-fail** when their manifest is missing; others silently no-op. Declaring ecosystems that don't apply turns main red on every scheduled Dependabot run, for no benefit:

| Ecosystem | Missing manifest behavior |
|-----------|---------------------------|
| `npm` | **Hard error** — `dependency_file_not_found: /package.json not found` |
| `devcontainers` | **Hard error** — `no devcontainers configs found` |
| `docker` | Silent no-op (scans Dockerfile only if present) |
| `gomod` | Silent no-op (scans go.mod only if present) |
| `github-actions` | Silent no-op (scans workflows only if present) |
| `pip` | **Hard error** — fails if no requirements*.txt / pyproject.toml |
| `composer` | **Hard error** — fails if no composer.json |

**Rule:** match the template's ecosystem set to the **class** of repo. A `go-lib` template shouldn't ship with `npm` and `devcontainers` entries because libraries don't have `package.json` or `.devcontainer/`. A `go-app` template can reasonably include `npm` because some Go apps ship frontend assets — but the first consumer without frontend assets will fail weekly until someone removes the entry or adds the manifest.

**Diagnosing a weekly Dependabot failure on main:**

```bash
# Latest Dependabot run conclusions
gh api "repos/OWNER/REPO/actions/runs?per_page=10" --jq '
  [.workflow_runs[] | select(.name == "Dependabot Updates" or .name == "Dependabot")
    | {conclusion, created_at, html_url}]'

# Open the failing run's log to find the specific ecosystem:
gh run view <RUN_ID> --repo OWNER/REPO --log-failed |
  grep -iE "dependency_file_not_found|no .* configs found" | head -5
```

If the failure comes from a template-derived ecosystem that doesn't apply: fix the template (so new consumers inherit the fix) *and* open a consumer-side PR to drop the ecosystem (so the existing repo stops failing). Running only one half leaves the drift check failing on the PR or the schedule failing on main. See [multi-repo-operations.md](./multi-repo-operations.md) for the template-consumer coordination pattern.

### Maintained Release Branches — `target-branch`

Dependabot scans **only the default branch** by default. A repo that keeps long-lived release branches (e.g. `13.4`, `12.4` alongside `main`) receives action/dependency bumps on the default branch only; the release branches silently fall behind and their pinned actions go stale — a divergence nobody notices until, say, a backport PR renders with an old pinned action while `main` already moved on.

Add one update block **per maintained branch** with `target-branch`:

```yaml
version: 2
updates:
  # Default branch
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: weekly

  # Maintained release branches — Dependabot only scans the default branch
  # otherwise, so these bump the branch in place (no backport needed).
  - package-ecosystem: "github-actions"
    directory: "/"
    target-branch: "13.4"
    schedule:
      interval: weekly

  - package-ecosystem: "github-actions"
    directory: "/"
    target-branch: "12.4"
    schedule:
      interval: weekly
```

Notes:

- `target-branch` PRs open **against that branch**, not the default — no backport labels or cherry-picks involved.
- List only branches that actually exist and are maintained; a `target-branch` pointing at a missing branch makes that update run **fail** (visible in the repo's Dependabot update logs — see "Diagnosing a weekly Dependabot failure" above), it does not silently no-op.
- The alternative — labeling default-branch bump PRs for backport — works but reintroduces per-PR conflict resolution once branch workflows have drifted; `target-branch` bumps in place instead.
- `groups`, `cooldown`, `commit-message`, and `open-pull-requests-limit` apply per block.

### Grouping Dependencies
```yaml
updates:
  - package-ecosystem: "gomod"
    directory: "/"
    schedule:
      interval: "weekly"
    groups:
      all-dependencies:
        patterns:
          - "*"

      # Or group by type
      production:
        dependency-type: "production"
      development:
        dependency-type: "development"
```

### SHA-Pinned Actions — Comment Maintenance and Deprecation Warnings

**Dependabot maintains the version comment, not just the SHA.** With the `github-actions` ecosystem enabled, a bump rewrites both the pinned SHA **and** the trailing `# vX.Y.Z` comment in one diff:

```diff
- uses: actions/cache@cdf6c1fa76f9f475f3d7449005a359c84ca0f306 # v5.0.3
+ uses: actions/cache@55cc8345863c7cc4c66a329aec7e433d2d1c52a9 # v6.1.0
```

So annotating bare SHA pins once (with **API-verified** tags — resolve each SHA via `gh api repos/OWNER/ACTION/tags`) puts them in the exact format Dependabot then keeps current. Without the `github-actions` ecosystem declared, action pins are only ever updated by hand and silently drift.

**A runtime-deprecation warning is not cleared by a version bump unless the newer release changed the runtime.** Before claiming "bumping action X fixes the Node NN deprecation", check the target version's `action.yml`:

```bash
gh api -H "Accept: application/vnd.github.raw" \
  repos/OWNER/ACTION/contents/action.yml?ref=<tag> | grep -A1 '^runs:'
# runs.using: 'node20'  → still deprecated; the bump does NOT clear the warning
```

An action already pinned at its latest release can still emit the warning if upstream ships no newer-runtime build — the fix is then an upstream change or a replacement action, not a bump. Don't assert the warning is fixed off the version number alone.

### Bulk SHA resolution — verify the SHA maps *back* to the tag

Resolving tag → SHA for a set of actions is a loop, and a loop that prints
`action@<40-hex> # vX.Y.Z` looks authoritative whether or not it is right. Two
failure modes survive a confident-looking run, and neither is caught by
`actionlint` or by CI — a wrong-but-valid SHA pins silently:

**1. A SHA that belongs to no tag.** Verify the reverse direction — SHA → tag —
against the API, not against your own resolution step:

```bash
# For each pin, ask the tags API which tag(s) point at this SHA. Empty = fabricated or stale.
gh api "repos/$REPO/tags?per_page=100" --jq ".[] | select(.commit.sha==\"$SHA\") | .name"
```

In one run this caught a pin for `juliangruber/read-file-action` whose SHA mapped
to **no tag at all** — six of seven resolved correctly, which is exactly why the
seventh was easy to miss.

**2. A regex that mis-ranks tags.** Picking "latest" by pattern-matching tag names
breaks on any project not using three-part semver. A `^v?[0-9]+\.[0-9]+\.[0-9]+$`
filter silently skips two-part tags, so `github/issue-labeler` — whose releases are
`v3.4`, `v3.3`, `v3.2` — resolved to "latest `v2.4.1`", i.e. a **downgrade
disguised as an upgrade**.

Ask GitHub for latest instead of deriving it:

```bash
gh api "repos/$REPO/releases/latest" --jq .tag_name   # authoritative
```

Note the endpoint 404s for repos that tag without publishing releases — fall back
to the tags list *and reason about the versioning scheme*, rather than assuming a
shape.

**A downgrade is the tell.** If a "latest" lookup ever resolves *below* what the
repo already pins, the lookup is wrong until proven otherwise — that direction is
almost never a real upgrade.

### Dependency PRs must trigger the test job

A `paths:` filter listing source globs only does **not** match the manifest, so
every dependency PR — including Dependabot's and Renovate's — **skips the test job
and merges untested**. The PR looks green because the tests never ran.

```yaml
# Before: a go.mod-only change matches nothing here, so no tests run
on:
  pull_request:
    paths:
      - '**.go'
```

Include the manifest, its lockfile, any toolchain pin, and the workflow itself:

```yaml
on:
  pull_request:
    paths:
      - '**.go'
      - 'go.mod'
      - 'go.sum'
      - '.go-version'
      - '.github/workflows/unit_tests.yaml'
```

Same shape in every ecosystem: `package.json`/`package-lock.json`, `composer.json`/`composer.lock`, `pyproject.toml`/`uv.lock`.

**Verify by observation, not by reading the YAML** — check that the test job
actually appears on a manifest-only PR:

```bash
gh pr view "$PR" --repo "$R" --json statusCheckRollup \
  --jq '[.statusCheckRollup[]?.name] | index("unit_tests") // "TEST JOB DID NOT RUN"'
```

**Real case:** a Go provider whose `unit_tests` filter was `'**.go'`. Its
dependency upgrade PR ran only `triage` and `DCO`; adding the manifest paths made
`unit_tests` appear on the same PR and pass. Every prior dependency bump in that
repo had merged without a single test running.

## Renovate

### Forks are skipped, and the opt-in is only read from the repository root

A fork with a perfectly valid `renovate.json` can sit there for months without Renovate ever running: no pull requests, no Dependency Dashboard, nothing in the log. The configuration is not the problem.

`forkProcessing` defaults to `"auto"`, which means **disabled when Renovate runs in autodiscover mode** — and installing the Mend app against *All repositories* is autodiscover. Forks are then skipped with:

```
Repository is a fork and not manually configured - skipping
```

Installing against *Select repositories* instead processes forks, so the same organisation can have working and silent forks with byte-identical config.

To opt a fork back in:

```json
{
  "$schema": "https://docs.renovatebot.com/renovate-schema.json",
  "extends": ["github>myorg/renovate-config"],
  "forkProcessing": "enabled"
}
```

**The setting is read only from a `renovate.json` in the repository root.** A `.github/renovate.json` cannot carry it. And a repository must not hold two Renovate config files — that is a configuration error, not a merge — so a repo whose config lives under `.github/` has to **move** the file to the root rather than add a second one:

```bash
git mv .github/renovate.json renovate.json   # then add forkProcessing
```

Diagnosing this from GitHub alone is hard, because every visible signal looks healthy — the app is installed org-wide, the config extends the org preset, nothing is archived. The tells are the *absence* of a Dependency Dashboard issue and `repository_selection` on the installation:

```bash
gh api /orgs/ORG/installations --jq '.installations[] | select(.app_slug=="renovate") | .repository_selection'
gh api "repos/ORG/REPO" --jq .fork
```

`repository_selection: all` plus `fork: true` plus no dashboard is the signature.

### A push by anyone else takes the PR out of Renovate's hands

Renovate treats a PR as modified as soon as another Git author adds a commit to its branch — a lockfile repair, a fixed test, a formatting commit. From then on it makes no further commits to that branch: it does not rebase it on conflicts and does not update it to a newer version. When the dependency later reaches the target version some other way, Renovate also does not delete the stale branch or autoclose the PR: it renames the PR to `<title> - abandoned` and comments that autoclosing is skipped. The PR stays open until someone closes it.

Whoever pushed to the branch owns the PR from then on: track it to merge, or close it with a comment naming what superseded it (`gh pr close <n> --delete-branch --comment "Superseded by #<m>"`). Two ways to hand a branch back instead:

- Apply the rebase label (`rebaseLabel`, default `rebase`): Renovate then regenerates its commit even on a modified branch, which discards the foreign commit.
- For another bot that routinely commits on top of Renovate PRs, list its commit-author email (or a glob or regex matching it) in `gitIgnoredAuthors`, so its pushes do not count as a modification.

### Asking Renovate to rebase from the CLI

Add the rebase label first. It touches no PR body, while ticking the box below means rewriting a bot-authored body, which republishes text you did not write:

```bash
gh pr edit 123 --repo OWNER/REPO --add-label rebase
```

`gh pr edit --add-label` fails when the label does not exist in the repository: create it once with `gh label create rebase --repo OWNER/REPO`, or use the name the repository configures in `rebaseLabel` (default `rebase`). Renovate removes the label when it rebases; the removed label and a new commit on the branch are the confirmation.

Where a label cannot be used, tick the rebase box instead. Every Renovate PR body carries the line `- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box`. Ticking it asks Renovate to rebase or retry the branch, and it works without the web UI: replace `- [ ] <!-- rebase-check -->` with `- [x] <!-- rebase-check -->` in the body and PATCH the body back. Replace only the first occurrence, and keep the body in a file rather than on the command line, because Renovate bodies with release notes run to tens of kilobytes:

```bash
R=OWNER/REPO; N=123
gh api "repos/$R/pulls/$N" --jq .body > body.md
python3 - body.md <<'PY'
import sys
p = sys.argv[1]
s = open(p).read()
old, new = "- [ ] <!-- rebase-check -->", "- [x] <!-- rebase-check -->"
assert old in s, "no unticked rebase box: already ticked, or not a Renovate PR"
open(p, "w").write(s.replace(old, new, 1))
PY
# PATCH only a body that carries the tick; -F reads the value from the file
grep -qF -- '- [x] <!-- rebase-check -->' body.md \
  && gh api "repos/$R/pulls/$N" -X PATCH -F body=@body.md --silent
# Read it back: expect 1
gh api "repos/$R/pulls/$N" --jq .body | grep -cF -- '- [x] <!-- rebase-check -->'
```

For both the label and the box, Renovate acts on its next run, which can be minutes or hours away. Until then `pr-status.sh` keeps reporting the branch as behind its base; that is the expected state, not a failed request. Do not label or tick again and do not poll: the label on the PR or the read-back above is the confirmation that the request is in, and the rebased push is what wakes the PR's checks.

### A version that lives outside an image tag needs a custom manager

Renovate's built-in managers read image tags, actions and lock files. A version stated as `ARG APP_VERSION=1.2.3`, as a Compose default (`${APP_VERSION:-1.2.3}`), in `.env.example`, in a CI `env:` block or in a README table is invisible to them, so the application itself is the one dependency no bot ever proposes — while its base images update weekly. A `customManagers` entry of `customType: regex` closes that; the points that cost a detour in `netresearch/moodle-docker` (PR #94):

- **One manager per file shape, the same `depNameTemplate`.** Put the pair that must move together in one `matchStrings` entry spanning both lines, and capture a pinned commit as `currentDigest`. Give that manager `autoReplaceStringTemplate` (`ARG V={{{newValue}}}\nARG COMMIT={{{newDigest}}}`) so both lines are rewritten together — a version bump with the old pin fails the integrity check on the next build. Whether Renovate's default replacement would also rewrite the digest was not measured; the template removes the question. For a `github-tags` datasource on an *annotated* tag the digest Renovate returns is the commit, not the tag object (checked: `344232c…`, not `f9158b1…`), which is what `git ls-remote <repo> 'refs/tags/vX^{}'` gives.
- **Add a `packageRules` entry with `groupName` for the dependency.** Separate managers that share a `depName` are not guaranteed to land in one update, and an auto-merged patch PR that changes the Compose defaults but not the Dockerfile leaves a stack that refuses to start when the two disagree. CodeRabbit raised this on the PR; the lookup had already shown one branch name, but that is an accident of naming and `groupName` makes it a rule.
- **Automerge patch only.** `matchUpdateTypes: ["patch"]` with `automerge: true`, and for minor and major `automerge: false` plus the label your auto-merge workflow refuses (the `netresearch/.github` reusable skips `deps-no-automerge` and `deps-major`). A reusable that trusts every Renovate PR merges a minor release the moment the checks pass unless the label is there.
- **`managerFilePatterns` is the current key; older Renovate calls it `fileMatch`.** `npx renovate-config-validator` resolved to 37.x here and answered `Custom Manager contains disallowed fields: managerFilePatterns`; `npx --package renovate@latest renovate-config-validator` (44.x) accepted the same file. Run the validator from the version the hosted app runs, not from whatever `npx` cached.

Verify before opening the PR, locally, without changing tracked files (the `run.json` log is an untracked file, so keep it out of the commit):

```bash
GITHUB_COM_TOKEN=$(gh auth token) LOG_FORMAT=json LOG_LEVEL=debug RENOVATE_ONBOARDING=false \
  npx -y renovate@latest --platform=local --dry-run=lookup > run.json
jq -c 'select(.msg|test("packageFiles with updates")) | .config.regex[]
       | {file:.packageFile, deps:[.deps[]|{currentValue,currentDigest,updates}]}' run.json
```

That proves extraction: every occurrence listed, digest captured. It cannot show an update while the tree is already current, so prove the positive case on a copy **outside any repository** with the version and pin set back one release (the repository's own `renovate.json` would otherwise be discovered and the comparison measures the wrong pair): the lookup must offer the next release with the right `newDigest`, and one `branchName` for every occurrence (with `groupName` set it is `renovate/<group>`; the `groupName` field itself printed `null` in the lookup output, so read the branch name, not that field). What a local lookup does not exercise is the file rewrite and the merge; those only happen in the hosted run, so say so in the PR.

### Changing how a tool is installed must keep it tracked

Replacing the install form of a dependency — an action by `go install`, an image by a downloaded binary, a registry release by a git pin — often moves it out of every manager Renovate runs. The old form was tracked by a built-in manager (`github-actions`, `dockerfile`, …); the new line is plain text that nothing reads. Losing automatic updates that way is a regression, not a footnote for the PR body.

Before opening such a change, name the manager that tracks the new form, and prove it with the local lookup above, narrowed to that manager (`RENOVATE_ENABLED_MANAGERS=custom.regex` for a custom one; for a built-in manager, read `.config.<manager>[]`, e.g. `.config.dockerfile[]`, instead of `.config.regex[]` in the `jq` filter): the dependency must appear as extracted, and on a copy set back one version, an update must be proposed. netresearch/.github#504 moved gosec from the `securego/gosec` action to a `go install` at a commit on gosec's `master`, and said in the PR that Renovate would no longer bump it; netresearch/.github#505 restored the updates with a `customType: regex` manager on `datasourceTemplate: git-refs`, whose `currentValue` is the branch name and `currentDigest` the pinned commit.

### Hash-pinned `requirements.lock` files Renovate cannot regenerate

A Python sidecar that pins `requirements.txt` and keeps a separate `--hash`-pinned `requirements.lock` beside it, made by hand rather than by a manager Renovate runs, breaks on every Python update: Renovate bumps `requirements.txt` and leaves the lock as it is, so the check comparing the two fails on every such PR. If that check is not required and the PR automerges, the disagreement lands on `main`. netresearch/t3x-nr-llm#1005 merged that way: `requirements.txt` then said `transformers==5.19.0`, the lock still said 5.17.0, and the image went on installing 5.17.0.

The durable fix is a lock Renovate maintains itself:

- **uv:** `pyproject.toml` plus `uv.lock`; Renovate's `pep621` manager regenerates `uv.lock` on each update (netresearch/t3x-nr-llm#1138).
- **pip-compile:** Renovate's `pip-compile` manager, which regenerates the output file with the command it reads from that file's header. Its `managerFilePatterns` is empty by default, so it has to be pointed at the output `.txt` file, and the file must keep pip-compile's default header. The manager parses that header strictly (`lib/modules/manager/pip-compile/common.ts`), and `uv pip compile` headers count too:
  - The header must name the input file, for example `requirements/tests.in`. A lock compiled from stdin (`-`) is rejected, because `-` reads as an unknown option.
  - Every option that takes an argument must use the `--option=value` form: `--output-file=requirements/tests.txt`, `--python-version=3.12`. `-o` and `--option value` stop the manager. For uv, `--universal` and `--generate-hashes` are accepted.
  - So compile with exactly the form the header should carry: `uv pip compile --universal --generate-hashes --python-version=3.12 --output-file=requirements/tests.txt requirements/tests.in`. uv keeps the existing pins of the output file, so switching an old header to this form changes only the header and the `# via` comments.
  - `pip_requirements` is no substitute for a hash lock. With `--hash` lines it updates through `hashin`, which rewrites the pins already in the file but never adds a transitive dependency a new release introduces; the next `--require-hashes` install then fails. Its default pattern also misses files in a `requirements/` folder (`requirements/tests.txt`) and names without "requirements" (`pip-audit.txt`), so such a lock is not updated at all until a manager is pointed at it.
  - A transitive pin that is not in the `.in` file gets a security fix only through lock-file maintenance ("refresh pip-compile outputs" on the Dependency Dashboard). Renovate's global default leaves lock-file maintenance off, but the `pip-compile` manager turns it on in its own defaults, with Renovate's default schedule of "before 4am on monday", so once a week. A critical advisory against such a pin can need a manual `--upgrade-package <name>` before then.

Until then, a single bump can be finished by hand. When PyPI lists the same base requirements for the old and the new version, only the package's own entry and its wheel hash change in the lock. Compare both from PyPI's JSON API, and take the hash from there rather than from a local download:

```bash
set -euo pipefail
PKG=transformers; OLD=5.17.0; NEW=5.19.0
# Fail closed: a failed request or an unexpected body must stop here, never
# reach the comparison as an empty list that reads as "identical".
meta() { curl -fsS "https://pypi.org/pypi/$PKG/$1/json"; }
reqs() { jq -r 'if (.info | has("requires_dist")) then (.info.requires_dist // [])
                else error("no requires_dist in the PyPI response") end
                | map(select(test("extra ==") | not)) | sort | .[]' <<<"$1"; }
old_json=$(meta "$OLD"); new_json=$(meta "$NEW")
old_reqs=$(reqs "$old_json"); new_reqs=$(reqs "$new_json")
if diff <(printf '%s\n' "$old_reqs") <(printf '%s\n' "$new_reqs"); then
  echo "base requirements identical"
fi
jq -er '.urls[] | select(.packagetype == "bdist_wheel") | "\(.filename) sha256:\(.digests.sha256)"' <<<"$new_json"
```

If `diff` prints anything, the dependency set moved with the package (for this pair it does: `huggingface-hub` changes its range), and the lock has to be regenerated rather than edited.

### Migrating from Dependabot to Renovate

Renovate replaces Dependabot only where Renovate **runs**. A `renovate.json` in the tree is a declaration, not a run: on `netresearch` (2026-09-24), 27 of 137 repositories with a Renovate config had no Renovate PR in three months, most none since the onboarding wave of February 2025 — one had lost its onboarding merge in a history rewrite. Switching Dependabot off there leaves the repository with no update bot at all.

1. **Measure activity per repository, not config presence.**

   ```bash
   gh pr list -R ORG/REPO --author app/renovate --state all --limit 1 \
     --json createdAt --jq '.[0].createdAt // "never"'
   ```

   Query per repository. The search API (`search/issues?q=org:ORG+author:app/renovate`) stops at 1,000 results, so an org-wide tally of an active bot is truncated. Treat "no PR in ~3 months" as unproven, not as quiet: keep Dependabot there until Renovate is shown to work.

2. **Security updates** are usually held on by an enforced org code-security configuration, so the per-repo `DELETE …/automated-security-fixes` answers 422. Attach a variant configuration with `dependabot_security_updates: disabled` to the proven repositories only — see `security-config.md`, "An `enforced` configuration blocks per-repo changes". Keep `dependabot_alerts` enabled: Renovate's `vulnerabilityAlerts` reads them to open its security PRs. Recent version-update PRs do not prove that path, so check both halves before disabling:

   ```bash
   # The Renovate app may read the alerts (expect "read")
   gh api orgs/ORG/installations \
     --jq '.installations[] | select(.app_slug=="renovate") | .permissions.vulnerability_alerts'
   # The effective config enables vulnerabilityAlerts — the org preset, or
   # a repo renovate.json that overrides it
   gh api repos/ORG/renovate-config/contents/default.json --jq .content | base64 -d \
     | jq '.vulnerabilityAlerts'
   ```

3. **Version updates** (`.github/dependabot.yml`): the file often carries decisions, not just a schedule. Port each into `renovate.json` before deleting the file:

   | In `dependabot.yml` | In `renovate.json` |
   |---|---|
   | `ignore: dependency-name: X, versions: [">= 6.1"]` | `packageRules: [{matchPackageNames: ["X"], allowedVersions: "< 6.1"}]` |
   | `ignore: update-types: [version-update:semver-major, version-update:semver-minor]` on one ecosystem | `packageRules: [{matchManagers: ["docker-compose"], matchUpdateTypes: ["major","minor"], enabled: false}]` |
   | ecosystem owned by Dependabot on purpose (a split between the bots) | remove the matching `enabled: false` rule from `renovate.json` |

   Read the history of both files first (`gh api "repos/ORG/REPO/commits?path=.github/dependabot.yml"`): a split between the bots usually has an issue behind it, and the PR should name the decision it reverses.

4. **Template-managed repositories:** a `dependabot.yml` kept on purpose is listed under `intentional-drift` in `.github/template.yaml`; remove that entry together with the file. Check that no `netresearch/.github` template ships a `dependabot.yml`, or the drift check re-adds it.

5. **Prose:** grep the repository for "Dependabot" — Dockerfile comments, lint-config rationales and OpenSSF badge evidence name the updater and turn false with the file.

### Auto-merge Configuration (Recommended)

**IMPORTANT:** Use `platformAutomerge: true` to leverage Renovate's bypass permissions:

```json
{
  "$schema": "https://docs.renovatebot.com/renovate-schema.json",
  "extends": ["config:recommended"],
  "automergeType": "pr",
  "platformAutomerge": true,
  "packageRules": [
    {
      "matchUpdateTypes": ["patch", "minor", "pin", "digest"],
      "automerge": true
    }
  ]
}
```

| Setting | Value | Purpose |
|---------|-------|---------|
| `automergeType` | `"pr"` | Merge via PR (not branch) for visibility |
| `platformAutomerge` | `true` | Use GitHub's auto-merge (Renovate enables it) |
| `automerge` | `true` | Enable auto-merge for matching packages |

### GitHub Actions digest pinning — exempt org-owned resources (last-match-wins)

Renovate applies the **last matching `packageRule`**, so rule order decides pinning. If a repo opts into `helpers:pinGitHubActionDigests` (which SHA-pins *all* actions), an exemption for org-owned resources placed only in a *shared* preset is overridden by the later opt-in preset — and Renovate SHA-pins your own reusable workflows (`org/.github/...@main` → `@<sha>`), which are meant to track a branch so fixes reach every consumer without a per-repo digest bump.

Put the exemption where it wins:

- **Repo-level** — in the repo's own `packageRules` (evaluated after all `extends`):

  ```json
  {
    "matchManagers": ["github-actions"],
    "matchPackageNames": ["myorg/**"],
    "pinDigests": false
  }
  ```

- **Better, org-wide** — a bundled sub-preset that extends the pin preset and applies the exemption *after* it, so consumers just `extends: ["github>myorg/renovate-config:pinning"]` and cannot omit or mis-order it:

  ```json
  {
    "extends": ["github>myorg/renovate-config", "helpers:pinGitHubActionDigests"],
    "packageRules": [
      { "matchManagers": ["github-actions"], "matchPackageNames": ["myorg/**"], "pinDigests": false }
    ]
  }
  ```

A shared-preset exemption alone gives false confidence: it is silently overridden the moment a repo extends the pin preset after it. This surfaced when Renovate auto-merged a PR that SHA-pinned an `org/.github` reusable workflow against the org's stated policy.

## Auto-merge Workflow

### Auto-merge Decision Matrix

| Repository Configuration | Workflow Pattern | Key Difference |
|--------------------------|------------------|----------------|
| Merge queue enabled | GraphQL `enqueuePullRequest` | Adds PR to queue, queue handles merge |
| Branch protection (no queue) | `gh pr merge --auto` | Enables auto-merge, GitHub merges when checks pass |
| No branch protection | `gh pr merge --rebase` | Direct merge, no waiting |

### Renovate vs Dependabot Auto-merge

| Capability | Renovate | Dependabot |
|------------|----------|------------|
| Native auto-merge | ✅ `platformAutomerge` | ❌ Needs workflow |
| Bypass permissions | ✅ When in bypass list | ❌ Via `GITHUB_TOKEN` only |
| Lock file maintenance | ✅ Built-in | ❌ Manual |
| Who enables auto-merge | `app/renovate` | `app/github-actions` |

**Critical difference:** When Renovate enables auto-merge via `platformAutomerge`, it appears as `enabledBy: app/renovate` and can use bypass permissions. When a workflow enables auto-merge, it appears as `enabledBy: app/github-actions` which may NOT have bypass permissions.

### GitHub Actions Auto-merge (Dependabot Only)

For Renovate PRs, let Renovate handle auto-merge via `platformAutomerge`. Only use workflows for Dependabot:

```yaml
# .github/workflows/auto-merge-deps.yml
# For Renovate: Only approve (Renovate handles auto-merge via platformAutomerge)
# For Dependabot: Approve and enable auto-merge
name: Auto-merge dependency PRs

on:
  pull_request_target:
    types: [opened, synchronize, reopened]

permissions: {}

jobs:
  auto-merge:
    runs-on: ubuntu-latest
    # The bot must be the PR author (user.login) AND the actor of the event
    # (github.actor). The author alone lets a human push to a bot branch, or a
    # human reopen, get approved and merged unreviewed. github.actor keeps the
    # original actor on a re-run. zizmor's bot-conditions audit flags every
    # github.actor check; here it only narrows the author check.
    if: >- # zizmor: ignore[bot-conditions] -- in addition to the author check
      (github.event.pull_request.user.login == 'dependabot[bot]' ||
       github.event.pull_request.user.login == 'renovate[bot]') &&
      (github.actor == 'dependabot[bot]' ||
       github.actor == 'renovate[bot]')
    permissions:
      contents: write
      pull-requests: write

    steps:
      - name: Harden Runner
        uses: step-security/harden-runner@v2
        with:
          egress-policy: audit

      - name: Dependabot metadata
        id: metadata
        if: github.event.pull_request.user.login == 'dependabot[bot]'
        uses: dependabot/fetch-metadata@v2
        with:
          github-token: "${{ secrets.GITHUB_TOKEN }}"

      - name: Auto-approve PR
        run: gh pr review --approve "$PR_URL"
        env:
          PR_URL: ${{ github.event.pull_request.html_url }}
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}

      # Only enable auto-merge for Dependabot PRs
      # Renovate handles its own auto-merge via platformAutomerge
      - name: Enable auto-merge (Dependabot only)
        if: github.event.pull_request.user.login == 'dependabot[bot]'
        run: gh pr merge --auto --merge "$PR_URL"
        env:
          PR_URL: ${{ github.event.pull_request.html_url }}
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### GitHub Actions Auto-merge (Merge Queue)
```yaml
# .github/workflows/auto-merge-deps.yml
# Use when: Repository has merge queue enabled
# IMPORTANT: mergeMethod is NOT a valid argument for enqueuePullRequest
name: Auto-merge dependency PRs

on:
  pull_request_target:
    types: [opened, synchronize, reopened]

permissions:
  contents: write
  pull-requests: write

jobs:
  auto-merge:
    runs-on: ubuntu-latest
    # The bot must be the PR author (user.login) AND the actor of the event
    # (github.actor). The author alone lets a human push to a bot branch, or a
    # human reopen, get approved and merged unreviewed. github.actor keeps the
    # original actor on a re-run. zizmor's bot-conditions audit flags every
    # github.actor check; here it only narrows the author check.
    if: >- # zizmor: ignore[bot-conditions] -- in addition to the author check
      (github.event.pull_request.user.login == 'dependabot[bot]' ||
       github.event.pull_request.user.login == 'renovate[bot]') &&
      (github.actor == 'dependabot[bot]' ||
       github.actor == 'renovate[bot]')
    steps:
      - name: Auto-approve PR
        run: gh pr review --approve "$PR_URL"
        env:
          PR_URL: ${{ github.event.pull_request.html_url }}
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}

      - name: Add to merge queue
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          PR_NODE_ID: ${{ github.event.pull_request.node_id }}
        run: |
          gh api graphql -f query='
            mutation($pullRequestId: ID!) {
              enqueuePullRequest(input: {pullRequestId: $pullRequestId}) {
                mergeQueueEntry { id }
              }
            }' -f pullRequestId="$PR_NODE_ID"
```

## Branch Protection Configuration

### Required Status Checks - CRITICAL

**Check names MUST match exactly.** Matrix jobs produce names with suffixes:

| Workflow Definition | Actual Check Name |
|---------------------|-------------------|
| `job-name:` | `job-name` |
| `name: job (${{ matrix.variant }})` | `job (variant-value)` |

**Example:** If workflow has:
```yaml
jobs:
  smoke-test:
    strategy:
      matrix:
        variant: [minimal, full]
    name: smoke-test (${{ matrix.name }})
```

Branch protection must list:
- `smoke-test (minimal)`
- `smoke-test (full)`

NOT just `smoke-test`.

### Bypass Permissions for Auto-merge

Add Renovate and Dependabot to bypass list:

```bash
gh api repos/OWNER/REPO/branches/main/protection/required_pull_request_reviews -X PATCH \
  --input - << 'EOF'
{
  "dismiss_stale_reviews": false,
  "require_code_owner_reviews": false,
  "required_approving_review_count": 1,
  "bypass_pull_request_allowances": {
    "apps": ["dependabot", "renovate"]
  }
}
EOF
```

### Code Owner Reviews - AVOID with Auto-merge

**Problem:** `require_code_owner_reviews: true` blocks auto-merge even when the bot is in the bypass list.

| Setting | Effect on Auto-merge |
|---------|---------------------|
| `require_code_owner_reviews: false` | ✅ Works - any approval counts |
| `require_code_owner_reviews: true` | ❌ Blocked - `github-actions` approval doesn't satisfy code owner requirement |

**Why:** Bypass permissions only apply at merge time, but GitHub's `mergeStateStatus` shows `BLOCKED` before that, preventing auto-merge from being attempted.

**Solution:** Disable `require_code_owner_reviews` for repos with dependency auto-merge:

```bash
gh api repos/OWNER/REPO/branches/main/protection/required_pull_request_reviews -X PATCH \
  -f require_code_owner_reviews=false
```

### Merge Strategy Requirements

| Branch Protection Setting | Allowed Merge Methods |
|---------------------------|----------------------|
| `required_linear_history: true` | Rebase only (`--rebase`) |
| `required_linear_history: false` | Merge, squash, or rebase |

If you see "Merge method X is not allowed", check:
```bash
gh api repos/OWNER/REPO/branches/main/protection --jq '.required_linear_history'
```

### Strict Status Checks

With `strict: true`, PRs must be up-to-date with main before merging:

```bash
# Check if strict is enabled
gh api repos/OWNER/REPO/branches/main/protection/required_status_checks --jq '.strict'
```

**Impact:** After one PR merges, others become "behind" and need rebasing. Renovate handles this automatically via `@renovate rebase` or its scheduling.

## Troubleshooting Auto-merge

### PR Shows BLOCKED Despite Passing Checks

1. **Check names mismatch:**
   ```bash
   # Get actual check names from PR
   gh api graphql -f query='query($owner:String!,$repo:String!,$pr:Int!){
     repository(owner:$owner,name:$repo){
       pullRequest(number:$pr){
         commits(last:1){nodes{commit{statusCheckRollup{contexts(first:50){
           nodes{...on CheckRun{name conclusion}}
         }}}}}
       }
     }
   }' -f owner=OWNER -f repo=REPO -F pr=NUMBER --jq '.data.repository.pullRequest.commits.nodes[0].commit.statusCheckRollup.contexts.nodes[].name'

   # Compare with required checks
   gh api repos/OWNER/REPO/branches/main/protection/required_status_checks --jq '.checks[].context'
   ```

2. **Code owner reviews required:**
   ```bash
   gh api repos/OWNER/REPO/branches/main/protection/required_pull_request_reviews --jq '.require_code_owner_reviews'
   ```

3. **Branch behind main:**
   ```bash
   gh api graphql -f query='query{repository(owner:"OWNER",name:"REPO"){
     pullRequest(number:PR){mergeStateStatus}
   }}' --jq '.data.repository.pullRequest.mergeStateStatus'
   # BEHIND = needs rebase
   ```

### Workflow Not Triggering

**Problem:** Multiple PRs merged rapidly may skip push events for subsequent commits.

**Solution:** Add `workflow_dispatch` for manual triggering:
```yaml
on:
  push:
    branches: [main]
  workflow_dispatch:  # Allow manual trigger
```

Then trigger manually:
```bash
gh workflow run build.yml --repo OWNER/REPO --ref main
```

### CI Cannot Push to Protected Branch

**Error:** `GH006: Protected branch update failed - Changes must be made through a pull request`

**Cause:** Workflow tries to push directly to main (e.g., lock file updates).

**Solution:** Use Renovate's `lockFileMaintenance` instead of CI pushing directly:
```json
{
  "lockFileMaintenance": {
    "enabled": true,
    "schedule": ["before 6am on monday"]
  }
}
```

### Auto-merge Enabled by Wrong Actor

**Problem:** Auto-merge shows `enabledBy: github-actions` instead of `enabledBy: renovate`.

**Impact:** `github-actions` may not have bypass permissions.

**Solution:** For Renovate PRs, don't enable auto-merge in workflows. Let Renovate handle it via `platformAutomerge: true`.

### Merge Method Mismatch in Auto-merge Workflow

**Error:** `Merge method 'rebase' is not allowed on this repository` (or squash/merge)

**Cause:** The auto-merge workflow uses `--rebase` but the repository only allows merge commits (or vice versa).

**Diagnosis:**
```bash
# Check which merge methods are allowed
gh api repos/OWNER/REPO --jq '{merge: .allow_merge_commit, squash: .allow_squash_merge, rebase: .allow_rebase_merge}'
```

**Solution:** Update the workflow's merge command to match:
```yaml
# Use the method that matches repo settings:
run: gh pr merge --auto --merge "$PR_URL"   # if allow_merge_commit: true
run: gh pr merge --auto --squash "$PR_URL"  # if allow_squash_merge: true
run: gh pr merge --auto --rebase "$PR_URL"  # if allow_rebase_merge: true
```

### Bot Detection Needs the Author AND the Actor

**Problem:** A check on one field lets the wrong pull request through.

**Cause:** `github.event.pull_request.user.login` is the PR author and never changes. `github.actor` is whoever caused the event: a human who pushes to a `renovate/*` branch or reopens a bot PR becomes the actor, while the author stays the bot. On a re-run `github.actor` keeps the original actor; only `github.triggering_actor` changes ([GitHub contexts reference](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts)).

- `github.actor` alone can be satisfied by a bot push on top of attacker commits; zizmor's `bot-conditions` audit flags it.
- `user.login` alone approves and merges a human's push to a bot branch without review.

**Solution:** Require both. zizmor still flags the `github.actor` half; suppress it inline after the block-scalar indicator, which keeps the parsed expression unchanged:
```yaml
if: >- # zizmor: ignore[bot-conditions] -- in addition to the author check
  (github.event.pull_request.user.login == 'dependabot[bot]' ||
   github.event.pull_request.user.login == 'renovate[bot]') &&
  (github.actor == 'dependabot[bot]' ||
   github.actor == 'renovate[bot]')
```

The org reusable `netresearch/.github/.github/workflows/auto-merge-deps.yml` checks both. When a local workflow is replaced by a reusable, compare every condition of the old job with the reusable's: netresearch/docker-ftp-server#132 dropped a local `github.actor` check this way, and the reusable lacked it until netresearch/.github#526.

### The gitleaks Action Fails on Dependabot/Renovate PRs

**Error:** `gitleaks-action@v2` fails with a license error on bot PRs.

**Cause:** `gitleaks-action@v2` requires a `GITLEAKS_LICENSE` secret for organization repositories, and Dependabot runs with restricted secret access — it can only read secrets prefixed with `DEPENDABOT_`. So the scan cannot be licensed on exactly the PRs that need it.

**Solution:** Call the org reusable, which runs betterleaks. (This is the third-party scan in your workflow, not GitHub's own secret scanning, which is configured per repository and unaffected.) It is OSS, needs no license, and therefore has no bot-PR failure mode — no secret is passed to it at all:
```yaml
jobs:
  gitleaks:
    uses: netresearch/.github/.github/workflows/betterleaks.yml@main
```

Do not skip the scan for bot PRs: a dependency update can carry a secret like any other change. For known false positives, add a `.gitleaks.toml` allowlist — the repo's own file is honoured, so tune it there rather than disabling the job.

### One False Positive Turns the Scan Red on Every Open PR

**Error:** `gitleaks / Secret Scanning` fails on pull requests whose diff contains nothing secret-like, including other people's.

**Cause:** the reusable runs `betterleaks git` over the checked-out history, and on a pull request that history includes every branch the checkout fetched — in practice, commits of other open PRs. The generic rules match prose as readily as code: `generic-api-key` fired on a SECURITY.md sentence in which the plural of "key" was followed by a comma and then a long cipher name — keyword, separator, long token. (This page names the pattern instead of quoting it, because a quote would trip the same rule.) One such commit on one branch made the scan red on all five open PRs of the repository, among them an unrelated one by another author. Code scanning shows the finding with `commit_sha` of the offending commit, which is how you find the branch.

**Solution:**
- Reword the line so no separator and long token follow the keyword, and **replace the commit** (amend or rebase, then `git push --force-with-lease`). A follow-up commit leaves the matching text in history, and the history scan keeps finding it.
- Check before pushing with the scanner version the reusable pins, over the branch's own commits only: `betterleaks git . --log-opts="origin/main..HEAD" --redact`. Scanning the old and the new wording as two files (`betterleaks dir`) confirms the rewording actually clears the rule.
- Re-run the red scans on the other PRs **after** each run has finished: `gh run rerun --job <job-database-id>` answers `cannot be rerun` while its run is still in progress (the database ID, not the number in the Actions URL: `gh run view <run-id> --json jobs --jq '.jobs[] | {name, databaseId}'`). Once it has finished, `gh run rerun <run-id> --failed` also re-runs the aggregate job ("All security checks") that went red only because the scan did.
- Prefer rewording over an allowlist entry: a path allowlist on `SECURITY.md` or a regex for the phrase would also hide a real key pasted into that file later.
- Where the commit cannot be replaced — it is already on `main` — ignore that one finding by fingerprint in `.gitleaksignore` at the repository root (betterleaks reads `.betterleaksignore` if it exists and `.gitleaksignore` only otherwise, so a repository keeps one of the two). Unlike a `.gitleaks.toml` allowlist, which suppresses a rule or path everywhere, a fingerprint names one finding in one commit: `<commit-sha>:<file-path>:<rule-id>:<line>`, one per line, for example `e3f7fe2451e80ba75af6b02f8fe843f76dfe82c6:docs/sonarcloud.md:curl-auth-user:228`. The ignore file is committed like any other file, so the history scan reads it too: keep it to bare fingerprint lines, with no comment that quotes or paraphrases the flagged text.

### Pre-existing PRs Don't Auto-merge

**Problem:** PRs opened before the auto-merge workflow was added don't get auto-merged.

**Cause:** The workflow triggers on `opened`, `synchronize`, and `reopened`. Pre-existing PRs already had their `opened` event.

**Solution:** Either:
1. Comment `@dependabot rebase` or `@renovate rebase` to trigger a `synchronize` event
2. Close and reopen the PR to trigger `reopened`
3. Manually merge the pre-existing PRs

### GITHUB_TOKEN Cannot Modify Workflow Files

**Problem:** Auto-merge fails for PRs that update `.github/workflows/` files.

**Cause:** `GITHUB_TOKEN` (OAuth `gho_*` tokens) lack the `workflows` scope and cannot push or merge changes to workflow files. This is a GitHub security restriction.

**Solution:** The `auto-merge-direct.yml` template includes a check for workflow file changes and skips auto-merge for those PRs, leaving a comment instead:
```yaml
- name: Check for workflow file changes
  run: |
    WORKFLOW_FILES=$(gh pr diff "$PR_URL" --name-only | grep -E '^\\.github/workflows/' || true)
    if [ -n "$WORKFLOW_FILES" ]; then
      echo "modifies_workflows=true" >> "$GITHUB_OUTPUT"
    fi

- name: Merge PR
  if: steps.check-workflows.outputs.modifies_workflows != 'true'
  run: gh pr merge --rebase "$PR_URL"
```

PRs modifying workflow files require manual merge by a repository admin.

### Nameless `package.json` Pollutes the Lockfile With the Worktree Dir Name

**Problem:** Working on a Dependabot/Renovate npm PR in a git worktree (e.g. `fix-dependabot-npm-uuid/`) and running `npm install` produces a spurious `package-lock.json` change — the root package `"name"` flips to the worktree directory name — that a reviewer or CI flags as an unrelated diff.

**Cause:** When `package.json` has **no `name` field**, npm falls back to stamping the **checkout directory name** into `package-lock.json` as the root package name. In the git worktree convention, the checkout dir is *branch-named* (e.g. `fix-dependabot-npm-uuid`) rather than the repo name, so every `npm install` rewrites the lockfile's `name` to whatever branch folder you happen to be in.

```jsonc
// package-lock.json after `npm install` in a worktree named fix-dependabot-npm-uuid/
{
  "name": "fix-dependabot-npm-uuid",   // ← polluted: was absent / repo name before
  "lockfileVersion": 3,
  ...
}
```

**Solution:** Add an explicit `name` field to `package.json` so npm stops deriving it from the directory:
```jsonc
// package.json
{
  "name": "my-repo",
  "version": "1.0.0",
  ...
}
```

The lockfile `name` then stays stable regardless of which worktree folder you run `npm install` in. This bites specifically in git worktree workflows; a plain clone (dir == repo name) masks it.

## Enforcing Signed Commits + DCO Without Blocking the Bots

Requiring **signed commits** (`required_signatures`) and/or **DCO sign-off** across repos collides head-on with dependency automation, because bot commits are typically **unsigned** and carry **no `Signed-off-by`**:

- `required_signatures` has **no bot exemption** — it applies to every commit. Renovate commits pushed over git are unverified; Dependabot commits are *inconsistently* signed (some `verification.verified=true`, some `unsigned` in the same org). So turning it on blocks those PRs.
- DCO requires a `Signed-off-by` trailer bots don't add — a naive DCO gate blocks **every** Dependabot/Renovate PR.

Verify the blast radius before flipping anything on:

```bash
# Are bot commits signed?
gh api "repos/OWNER/REPO/commits?per_page=40" \
  --jq '[.[]|select(.commit.author.name|test("dependabot|renovate";"i"))][0]
        | {verified:.commit.verification.verified, signoff:(.commit.message|test("Signed-off-by"))}'
```

**A working recipe (per repo — GitHub Free has no org-level rulesets, so there is no org-wide shortcut):**

1. **Make Renovate sign.** Set `platformCommit: enabled` in the shared Renovate preset (or repo config). Renovate then creates commits through the GitHub API, which GitHub signs → `verified`.
2. **Drop Dependabot** where signatures are required — it can't be made to sign reliably. Standardise on Renovate (which now signs). This also ends the double-manager problem if both were configured.
3. **Exempt bots from DCO**, not from signatures. A reusable DCO check with a bot-login allowlist (`dependabot[bot],renovate[bot],github-actions[bot]`) lets bot PRs pass while still requiring humans to `git commit -s`. (Bots stay unsigned-off but are allowlisted; they are *signed* via step 1.)
4. **Enforce.** `required_signatures` via classic protection `POST repos/OWNER/REPO/branches/main/protection/required_signatures`, or — on repos with **no classic protection** (rulesets only) — a ruleset rule `{"type":"required_signatures"}`. Add the DCO check as a required context the same way (classic `required_status_checks` or a `required_status_checks` ruleset rule).

Note the classic `PATCH …/required_status_checks` **404s** ("Required status checks not enabled") when that component isn't already configured — add the check via a ruleset instead, which works regardless of classic protection.
## Cross-repo release race: dependent PR CI resolves composer too early

When repo B depends on a version of repo A that was *just* released, the order is: merge the upstream PR → tag → **wait for A's release workflow AND the package registry (Packagist) to publish** → only then act on the dependent PR in B (push commits to its branch, or flip it from draft to ready). Doing either earlier gives a CI run whose composer/npm resolve step reads stale registry metadata — every dependency-installing job fails at once. That failure pattern (all jobs red at the install step, right after an upstream release) is pure timing: re-run the checks, don't debug the PR.

## Dependabot alert dismissal: 280-character comment cap

`gh api -X PATCH repos/OWNER/REPO/dependabot/alerts/N` rejects a `dismissed_comment` over 280 characters with HTTP 422 (`Only 280 characters are allowed`) — check `${#COMMENT}` before the call. Valid `dismissed_reason` values: `fix_started`, `inaccurate`, `no_bandwidth`, `not_used`, `tolerable_risk` (use `not_used` for "vulnerable code not in execution path").

## Org Dependabot alerts: no advisory filter, and an unknown parameter is ignored

`GET /orgs/ORG/dependabot/alerts` cannot filter by GHSA or CVE ID. The [endpoint documentation](https://docs.github.com/en/rest/dependabot/alerts?apiVersion=2022-11-28#list-dependabot-alerts-for-an-organization) lists `classification`, `state`, `severity`, `ecosystem`, `package`, `epss_percentage`, `artifact_registry_url`, `artifact_registry`, `has`, `assignee`, `runtime_risk`, `scope` and `relationship`, plus sorting and paging; `ghsa_id` and `cve_id` exist only in the response. A `ghsa=` parameter is silently ignored and the call returns every open alert of the organisation: measured on `netresearch` 2026-10-22, 331 rows with `&ghsa=GHSA-6q48-6c7w-9gw2` and 331 without. Narrow by package and filter the advisory client-side:

```bash
gh api --paginate "orgs/ORG/dependabot/alerts?state=open&package=certifi&per_page=100" \
  --jq '.[] | select(.security_advisory.ghsa_id=="GHSA-6q48-6c7w-9gw2") | "\(.repository.full_name) #\(.number)"'
```

## Merging the workflow-file bot PRs that auto-merge skipped

The "GITHUB_TOKEN Cannot Modify Workflow Files" section above explains why auto-merge skips these PRs. To land them by hand: clone and merge locally — SSH (`git clone git@github.com:…`) is the reliable path in environments without a working credential helper (HTTPS works only when credentials are explicitly available). For repos with several workflow PRs, merge them one at a time — they typically touch the same files.

## Updating GitHub Actions versions: fetch the latest from the API, never guess

```bash
gh api 'repos/OWNER/REPO/tags?per_page=1' --jq '.[0] | "\(.name) \(.commit.sha)"'
```

Verify the SHA is valid AND that it is the latest version (a valid SHA of an old tag passes review while staying outdated), then update ALL occurrences across `.github/workflows/*.yml`, not just the failing one.

## `composer audit` flags a transitive CVE nothing can bump — mirror the audit-ignore

A transitive package can be pinned below its fixed version by a direct dependency you don't control (e.g. `firebase/php-jwt < 7` held back by an OAuth lib's constraint, which is itself pinned by a wrapper library). No `composer update` in the app repo can fix that. The default branch usually already tolerates the CVE via `config.audit.ignore` in `composer.json` — mirror the identical entry onto the diverging branch: JSON-only, lock untouched, no behavior change. Verify with the exact CI command (`composer audit --locked …` → exit 0, advisory listed as "ignored"). The real fix — releasing the pinning library with a loosened constraint — is a separate effort; don't block the immediate green on it.

## `pnpm/action-setup` must run BEFORE `actions/setup-node` with `cache: "pnpm"`

`actions/setup-node` with pnpm caching resolves the pnpm executable at setup time — if `pnpm/action-setup` hasn't run yet, it fails with `Unable to locate executable: pnpm`. Order the steps pnpm-first in any workflow using both.

## Migrating to bun: the reusable audit still runs `npm audit`

`netresearch/.github/.github/workflows/node-audit.yml` accepts `package-manager: bun`, but its bun path only installs with bun: it then synthesizes a lockfile with `npm i --package-lock-only --ignore-scripts` and gates on `npm audit --audit-level=…`. npm's resolver is stricter than bun's, so a peer-dependency conflict that `bun install` resolves can fail that step with `ERESOLVE`, and `npm audit` and `bun audit` can report different findings or severities. A green `bun audit` locally therefore does not predict the gate — reproduce it with the same two npm commands. Such a failure can predate the migration: check whether the npm path is already red on `main` before blaming the switch.

Pin the third-party actions the migration adds (`oven-sh/setup-bun` and the like) by commit SHA in the first commit that adds them. SonarCloud's `githubactions:S7637` ("External GitHub Actions and workflows should be pinned to a commit hash") flags a tag-pinned line, and SonarCloud also reports it to GitHub code scanning (tool `SonarCloud`), where the alert stays until a new analysis clears it. The org's own reusables stay `@main` (see `reusable-workflow-pitfalls.md`, "Own reusables stay `@main`").



--- FILE: skills/github-project/references/gh-cli-reference.md ---

<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->
<!-- SPDX-FileCopyrightText: Netresearch DTT GmbH -->

# gh CLI Commands Reference

Non-obvious `gh` CLI gotchas and troubleshooting patterns for GitHub repository management. For basic `gh pr`/`gh run`/`gh api` usage, `gh help` and `gh <command> --help` cover it.

## Packages (GHCR)

```bash
# List org container packages
gh api "orgs/ORG/packages?package_type=container"

# Inspect a package (needs read:packages)
gh api "orgs/ORG/packages/container/PACKAGE"

# Delete a package — needs BOTH read:packages AND delete:packages.
# admin:org alone is NOT enough; delete:packages alone still 403s.
gh auth refresh -h github.com -s read:packages,delete:packages
gh api -X DELETE "orgs/ORG/packages/container/PACKAGE"   # 204; GET then 404
```

Verify the token's effective scopes from GitHub's response header, not `gh auth status` (which can lag):

```bash
gh api "" --include 2>&1 | grep -i '^X-Oauth-Scopes:'
```

### GHCR cleanup can brick every tag of a multi-arch image

`actions/delete-package-versions` with `delete-only-untagged-versions: true` is NOT manifest-list aware: for a multi-arch image the per-arch child manifests and the cosign/SLSA referrers are stored as separate UNTAGGED versions — the cleanup deletes them and every tagged index then points at missing children (`docker pull` fails with manifest errors). Cleanup for multi-arch GHCR images must resolve which untagged digests are referenced by tagged indexes/referrers and keep them.

### Contents/Git-Data API commits are unsigned and carry no sign-off

A `PUT /repos/…/contents/…` commit is created server-side — `-S` and `--signoff` never apply, so it lands `verified: false` without a DCO trailer, and an archived repo makes it unfixable. When commits must be signed/signed-off (always, per policy): clone and commit locally; land signed commits BEFORE archiving.


## Org billing — which repository is spending the allowance

A "You have used 100% of the Git LFS bandwidth" (or Actions minutes / storage)
mail names the org, never the repository. The per-repository answer is the
billing usage report; the older `orgs/ORG/settings/billing/shared-storage` and
`…/actions` endpoints answer `410 This endpoint has been moved`.

```bash
# Every usage line item of a month, per product / SKU / repository.
# Products seen so far: actions, code_quality, copilot, git_lfs.
# LFS SKUs: "Git LFS bandwidth" (unitType Gigabytes) and "Git LFS storage"
# (unitType GigabyteHours) — a quantity is only comparable within one SKU,
# so filter on the SKU before converting a unit.
gh api "organizations/ORG/settings/billing/usage?year=2026&month=8" \
  | jq -r '.usageItems[] | select(.product=="git_lfs" and .sku=="Git LFS bandwidth")
           | [.date[0:10], .repositoryName, (.quantity*1000|floor|tostring)+" MB"] | @tsv'
```

Two readings to keep straight (typo3-demo, 2026-08-29): the report lags the
alert by about two weeks (rows ended on the 14th while the mail on the 29th
said 10 GB; the rows summed to 6.8 GB), and bandwidth is spent by *downloads*
of LFS objects — CI checkouts with `lfs: true`, `git lfs pull` on deploy
hosts, clones of forks, source archives that include LFS objects — never by
pushes. Look for those before looking for who uploaded what. For the fix when
the tracked set is small, see git-workflow's `advanced-git.md`, "Removing LFS
without a history rewrite".

## Common Troubleshooting Patterns

### Wait for CI with the native watcher, not a hand-rolled loop

To wait for PR checks, run `gh pr checks NUMBER --repo OWNER/REPO --watch [--fail-fast]` (or `gh run watch RUN_ID` for a specific run) as a background command — do **not** hand-write a `jq` poll loop. The native watcher already handles pending-state representation, new-check appearance, and refresh; hand-rolled loops re-derive those semantics from undocumented field shapes (`conclusion` may be `""`, `null`, or absent while a check is running) and reliably get them wrong.

Three recurring bugs in ad-hoc watchers:

- An empty-string `conclusion` not matched by the "pending" filter → false "all checks done".
- A bare `pending -eq 0 && break` snapshot, which is true both **before** runs register and **after** they finish. Run immediately after a push (or a close/reopen), it reads "0 pending" before the freshly-triggered run has appeared → false "all green" → premature merge.
- A wrong `createdAt` cutoff that skips the actual run → false timeout.

`gh pr checks` exits non-zero when checks fail — gate on the exit code. If you must hand-roll (watching something `gh` has no watcher for), gate on a **named required check reaching a terminal pass/fail state**, never on a 0-pending count. After pushing, capture the new SHA and confirm `headRefOid` matches before trusting any watch.

### `gh run rerun` re-runs the OLD state — only for genuine flakes

`gh run rerun [--failed]` reuses the original `GITHUB_SHA`/`GITHUB_REF` recorded at run-creation time. Two consequences:

- For `pull_request` workflows that SHA is the **merge commit** computed when the run was first created, so a rerun still tests the PR against the **old base**. After fixing a base-branch breakage, a rerun reproduces the old failure. To pick up new base state, create a new event: rebase the PR branch onto the fixed base and push (an empty commit works). (Reusable-workflow `@ref` resolution is also pinned at run-creation — see `reusable-workflow-pitfalls.md`.)
- Reruns are correct only for genuinely transient infra failures where the same code state should pass: runner/network blips, registry pull flakes (e.g. `Get "https://registry-1.docker.io/v2/": context deadline exceeded`), Sigstore/Rekor 409s. Don't debug the workflow for those — just `gh run rerun --failed`.
- **A bad Codecov report is not one of them.** Codecov keys its report by commit SHA, so a rerun against the same SHA is served the report it already has; an incomplete upload survives it unchanged. The identical number on the second attempt then reads as a reproduction and invites the wrong diagnosis — "the coverage is unstable" — when the measurement simply never ran again. Force a fresh upload with a new SHA carrying the same tree: `git commit --amend --no-edit -S && git push --force-with-lease`. (Observed on a pull request whose diff deleted one YAML file and could not affect coverage: `codecov/project` reported `-0.38%`, a workflow rerun reported `-0.38%` again, and the amended commit came back green on all 20 checks.)

### A startup-failed run is invisible in `gh pr checks` and `statusCheckRollup`

`conclusion: startup_failure` means GitHub rejected the workflow before any job began — invalid YAML, a missing reusable, or an action the repository's Actions allowlist forbids. Such a run creates **no check run**, and both `gh pr checks` and `statusCheckRollup` enumerate check runs, not workflow runs. A workflow that never started therefore contributes nothing to enumerate, and its absence is indistinguishable from "not applicable". (The reusable-workflow causes that produce this — a dead `uses:` reference, a permission mismatch — are in `reusable-workflow-pitfalls.md`; this is the gh-CLI side of the same blind spot.)

**Whether that silence also lets the merge through depends on the check's configuration.** If the absent check is *required* by branch protection or a ruleset, GitHub holds it at `Expected` and blocks the merge — visibly stuck, if unexplained. If it is **not** required, nothing holds it: the pull request reads green, `mergeStateStatus` reaches `CLEAN`, and a whole workflow having never run leaves no trace at all. The second case is the dangerous one, and it is the common one for a repository whose required-check list has not kept up with its workflow list.

Before merging, list workflow **runs**, not just checks — bound to the commit under test, and printing `headSha` as a cross-check:

```bash
gh run list --repo O/R --commit "$SHA" --limit 20 \
  --json workflowName,headSha,status,conclusion \
  --jq '.[] | "\(.workflowName) [\(.headSha[0:8])]: \(.status)/\(.conclusion)"'
```

Use `--commit`, not `--branch`: the latter spans every commit on the branch, so an older green run reads exactly like a current one. This holds for `pull_request` runs as well — **a run's `headSha` is the pull request's head commit**, so the branch tip is the right value to pass. (Do not confuse that field with `GITHUB_SHA` *inside* a `pull_request` run, which is the computed merge commit — that is what the `gh run rerun` section above is about. The run's API metadata and the checkout the job sees name two different commits.) Measured on this repository: `gh run list --commit <branch tip>` returns the `pull_request` and `pull_request_target` runs for that head.

Two follow-ons. A run's top-level `status` can still read `queued` while its jobs are nearly done, so report progress from `runs/<id>/jobs` rather than the run field. And a startup-failed run cannot be re-run at all (`This workflow run cannot be retried`) — it needs a fresh triggering event.

### A Copilot review request can evaporate — verify after requesting

`POST …/requested_reviewers` for `copilot-pull-request-reviewer[bot]` returns success, but the request can silently vanish without a review ever landing: `reviewRequests` comes back `[]` and `latestReviews` stays empty on the head. Observed after a force-push replaced the head shortly after the request. After requesting, verify (`gh pr view N --json reviewRequests,latestReviews`); if both are empty a few minutes later, re-request once — the second request reliably sticks.

### Verify every `--json` field name before a watcher depends on it

A guessed `--json` field fails the **whole** call — `gh` exits non-zero and prints "Unknown JSON field" — so a loop that reads the empty result as state answers confidently and wrongly. Run `gh pr view <n> --json` with no value once and read the printed field list before writing the loop. Two names that are commonly guessed and do not exist: `merged` (the rollup field is `mergedAt`, null while open; or ask `state` for `MERGED`/`OPEN`/`CLOSED` — GraphQL's `pullRequest.merged` does have the boolean) and `mergeQueueEntry` (queue state is GraphQL-only: `pullRequest { mergeQueueEntry { state position } }`).

Two guards that belong in any hand-rolled watcher. **An empty or failed query is a retry, never a terminal state** — see the rate-limit section below for why a 403 mid-loop is a transport answer, not a finding. And **an empty `conclusion` means unfinished, not failed**: `gh run list --json conclusion` returns `""`, not `null`, while a run is queued or in progress, so a red-check filter written as `select(.conclusion != null and .conclusion != "success")` counts every *running* job as a failure. Test `!= null and != "" and != "success" and != "skipped" and != "neutral"` — GitHub counts `neutral` alongside `success` and `skipped` as satisfying a required check, so leaving it out of the filter reports a passing run as red. Bind the set to the commit under test with `--commit <sha>` rather than `--branch`, which spans the whole branch.

Bound the loop as well. A check that no workflow produces never reaches a terminal state, so a watcher waiting for it by name waits forever; cap the rounds and report "no applicable check" as its own outcome, distinct from pass and from fail.

### `/stats/*` answers HTTP 202 with the body `{}` — call it again

The repository statistics endpoints (`/stats/contributors`, `/stats/commit_activity`, `/stats/participation`, …) are computed on demand and cached. On a cold cache GitHub starts the job and answers **202 Accepted with the body `{}`** rather than waiting; the numbers arrive on a later call, once the job has finished. Nothing about the `gh api` invocation looks wrong: it exits **0**, and `--jq 'length'` returns **0** — indistinguishable from a repository that genuinely has no contributors. The Contributors graph in the web UI shows the same shape — blank on one visit, populated on a reload — though which endpoint it calls is not something these measurements establish.

Measured across four repositories in one sweep: two answered 202, two answered 200 — a cold cache is the normal state for anything nobody has queried recently, not an error.

```bash
# Ask the status line; never infer "empty" from an empty result
gh api repos/OWNER/REPO/stats/contributors -i 2>/dev/null | awk 'NR==1{print $2}'   # 202 -> not ready
```

Poll the status rather than the payload, and give the job time — a second call moments later is still 202; the computation, not the cache write, is what you are waiting for:

```bash
code=""
for _ in 1 2 3 4 5; do
  code=$(gh api repos/OWNER/REPO/stats/contributors -i 2>/dev/null | awk 'NR==1{print $2}')
  [ "$code" = "200" ] && break
  sleep 10
done
# Exhausting the retries is NOT an empty repository — say so and fail, or the
# next line prints the 0 this whole section exists to stop you believing.
[ "$code" = "200" ] || { echo "stats still not ready (last status: ${code:-none})" >&2; exit 1; }
gh api repos/OWNER/REPO/stats/contributors --jq 'length'
```

The general shape: test the status code, never the emptiness of the output.

### `author_association` depends on who reads it

`author_association` on issues, comments and pull requests is computed for the reader, not stored with the author. An organization member whose membership is private shows as `MEMBER` only to readers who can see that membership, which in practice means other members. An anonymous request, or a token whose owner is not a member, sees the same author as `CONTRIBUTOR` or `NONE`.

Measured 2026-10-21 and again 2026-10-22 in TYPO3-Documentation: one comment by a private member read `MEMBER` with a member's token and `NONE` through an unauthenticated `curl`. 58 of the organization's 66 members had private membership (`orgs/ORG/members` minus `orgs/ORG/public_members`), so most of the team looked like outsiders to a non-member.

Before classifying comments as "from the team" by `author_association`, check that the token belongs to an active member of that organization:

```bash
gh api user/memberships/orgs/ORG --jq .state   # "active" -> MEMBER values are reliable
```

Any other result means team membership is unknown. `pending` is an open invitation. A failure with HTTP 404 has two causes that `gh` does not tell apart: the token owner is not a member, or the token lacks the scope to read the membership (`gh` then adds a hint to run `gh auth refresh -s user`). Test the exit status, not the printed text: on the 404 `gh` prints the JSON error body and exits 1.

### Rapid `gh api` calls intermittently return HTTP 401

Rapid sequences of `gh api` calls (REST + GraphQL) sometimes return `401 "Requires authentication"` even with valid auth — transient, clears with ~5-10s spacing and a retry. **Trap:** piping a `gh` listing straight into `while read` consumes the 401 error text as data when a call fails (e.g. JSON error braces get fed into a GraphQL mutation as "thread IDs"). Always capture output into a variable first, check the exit status, then iterate; add a `sleep 5-10` between bulk review-thread replies/resolves.

### Reading a run's log: grep the error text, not the status code

`gh run view --job=<id> --log` prefixes every line with the step name. Four traps when you read errors in it:

- **`--log-failed | tail` shows the wrong end of the log.** On a repo running `step-security/harden-runner`, the post-job step appends its egress-audit dump — DNS resolutions, `sudo` calls, the full `agent.service` journal — *after* the step that failed. Tailing a failed job therefore returns pages of runner telemetry and none of the error. Redirect to a file and grep for the annotation marker instead:
  ```bash
  gh run view <RUN_ID> --repo OWNER/REPO --log-failed > run.log
  grep -nE '##\[error\]' run.log      # then read the ~20 lines above each hit
  ```
  The lines above the marker carry the actual cause (the failing command's own output); the marker line itself is often just `Process completed with exit code 1`.

- **A bare status code matches things that are not errors.** `grep -c 403` over a job log also hits commit SHAs, ref names and git plumbing output in the `Checkout` step. A real case: a fixed run still showed 8 hits for `403` — all from `Checkout`, none an API error — which reads as "still broken". Match the error *text* (`Client Error: Forbidden`), and scope the count to the step that makes the calls.

  Each line is `<job>\t<step>\t<timestamp> <text>`, so anchor the step to the start of the line — an unanchored step name also matches log *prose* that mentions it:
  ```bash
  gh run view --job="$JOB" --log > job.log
  grep -c 'Client Error: Forbidden' job.log                  # not: grep -c 403
  grep -cP '^build\tRun tests\t.*Client Error: Forbidden' job.log  # + scoped to <job>\t<step>
  ```
- **Count what failed, not what succeeded.** A step can print `Found: 0 items` because there is nothing new *or* because every fetch failed. Those are the same line. Assert on the failure count (`grep -c 'Failed to get'`) before reading a zero as good news.
- **`gh api …/actions/jobs/<id>/logs` refuses a colourised log.** When the job output carries ANSI colour codes (Composer, PHPUnit and Rector all emit them), `gh` prints `the response contains terminal escape sequences; pass --allow-escape-sequences to output it anyway` and exits 1. Redirected to a file, that is a one-line file and exit code 1 — easy to read as "the log is empty" or "the job has no log". Pass the flag and strip the codes before grepping:
  ```bash
  gh api repos/OWNER/REPO/actions/jobs/$JOB/logs --allow-escape-sequences > job.raw
  sed -E 's/\x1b\[[0-9;]*m//g; s/^[0-9T:.Z-]+ //' job.raw > job.log   # drop colour codes and timestamps
  ```

### Python steps: timestamps are flush times, not print times

The log's per-line timestamps come from when the runner *received* the line. Python block-buffers stdout when it is not a TTY, so a whole run's output arrives in one flush and every line carries the same timestamp — 1670 lines sharing one second is normal, not a hang. Any timing analysis ("it broke 19 minutes in") read off those timestamps is invalid.

Set `PYTHONUNBUFFERED: 1` in the step's `env:` (or run `python -u`) when you need per-line timing. Node, Go and shell are line-buffered to a pipe and do not need this.

### PR/issue body prose: one line per paragraph

In PR/issue **bodies and comments**, GitHub's renderer turns a single newline into a hard line break (`<br>`) — it enables hard line breaks for issue/PR/comment text, unlike the CommonMark default (where a single newline is a soft break and an intentional break needs two trailing spaces, a trailing `\`, or an explicit `<br>`). So a prose paragraph hard-wrapped at ~80 columns renders as jagged, mid-sentence lines. Write each prose paragraph as one continuous line and separate paragraphs with a blank line; keep line breaks only where the break is the content (inside fenced code blocks, one item per line in a list). Source files behave the other way — reStructuredText and CommonMark `.md` render a single newline as a *soft* break, and a commit-message body is plain text, so all three are conventionally wrapped at ~72–80 columns and the wrap never shows. The rule follows how the destination treats a single newline, not whether the text is Markdown. When generating a body with `gh pr create --body-file` / `gh issue create --body-file`, do not pipe it through a hard-wrapper.

### Escape every `@`-token — GitHub mentions are live

Any raw `@something` in interactive GitHub surfaces (PR/issue/discussion bodies and comments, release notes) is parsed as a user mention and — when it resolves to an existing user or team — can notify that account — `@main` in a workflow-pinning discussion repeatedly pinged the real GitHub user named "main". Repository docs (README, wiki) render the link but generally do not notify. Wrap every non-mention `@`-token in backticks (`` `@main` ``) or escape it (`\@main`) before posting; audit generated bodies for bare `@` before sending.

### Add an image to an issue or PR (no browser needed)

GitHub's native attachment uploader (`user-attachments/assets/…`) needs a browser session + CSRF and cannot be driven by `gh`/the API — but that does **not** mean images are impossible. Commit the PNGs to a dedicated branch (in a fork if you lack push to the target), then embed the raw URL in the body/comment:

```bash
git push fork HEAD:issue-NNNN-screenshots
# In the issue/PR body:
# ![before](https://raw.githubusercontent.com/USER/REPO/BRANCH/before.png)
```

`raw.githubusercontent.com` serves `image/png` and GitHub renders it inline. Generate the image first; for a JS-populated widget, point the page at a local copy of the real data and screenshot the rendered result.

To **replace** an already-embedded image, do not overwrite the file under the same path — publish under a new filename and point the body at it. Images on `raw.githubusercontent.com` are served directly from GitHub's own domain (not through the camo proxy, which only fronts external images), behind a CDN with a short cache lifetime — so after you replace the file, a branch-based raw URL can keep returning the old bytes until the cache expires, and a `?v=` query is not a reliable bust. A new filename is a fresh path the CDN has not cached, so it loads immediately. Confirm the new raw URL serves the new file (`curl -fsSL RAW_URL | sha256sum`, compare to the local file — `-f` fails on HTTP errors so you don't hash a 404 page) before editing the body.

### Debug Auto-merge Pipeline

```bash
# 1. Check PR status
gh pr view NUMBER --repo OWNER/REPO --json mergeStateStatus,reviewDecision,autoMergeRequest

# 2. Check actual vs required checks
echo "=== Required checks ===" && \
gh api repos/OWNER/REPO/branches/main/protection/required_status_checks --jq '.checks[].context' && \
echo "=== Actual checks ===" && \
gh api graphql -f query='query{repository(owner:"OWNER",name:"REPO"){
  pullRequest(number:NUMBER){commits(last:1){nodes{commit{
    statusCheckRollup{contexts(first:30){nodes{...on CheckRun{name conclusion}}}}
  }}}}
}}' --jq '.data.repository.pullRequest.commits.nodes[0].commit.statusCheckRollup.contexts.nodes[].name'

# 3. Check bypass permissions
gh api repos/OWNER/REPO/branches/main/protection/required_pull_request_reviews \
  --jq '{code_owner: .require_code_owner_reviews, bypass: .bypass_pull_request_allowances.apps[].slug}'

# 4. Check if branch is behind
gh api graphql -f query='query{repository(owner:"OWNER",name:"REPO"){
  pullRequest(number:NUMBER){mergeStateStatus}
}}' --jq '.data.repository.pullRequest.mergeStateStatus'
```

### Fix Stale Merge Base on Fork PRs

When a fork's `main` is behind upstream and a PR is created after syncing, GitHub may cache the old merge base. The PR shows too many commits (e.g., N+1 instead of 1). Neither `update-branch` API nor force-pushing fixes it because the SHA hasn't changed.

```bash
# Close and reopen the PR to force merge base recalculation
gh pr close NUMBER --repo OWNER/REPO && sleep 2 && gh pr reopen NUMBER --repo OWNER/REPO
```

### Inline `--body` with Backticks EXECUTES Them — Always `--body-file`

An inline body in double quotes — `gh pr create --body "..."` with a Markdown code span inside — makes bash run the span's **unescaped** backtick contents as command substitution before `gh` ever sees the text (escaped backticks or a single-quoted body stay literal — but bodies are routinely assembled unescaped). In one real session this executed `bun audit`, `npm login`, and `npm publish` (only an ENEEDAUTH failure prevented an actual publish), and the resulting bodies were garbled with the substituted output. Any double-quoted body whose code spans are not escaped will misfire.

```bash
# WRONG: unescaped backticks execute npm test, $ expands
gh pr create --body "Run `npm test` first"

# RIGHT: quoted heredoc (no expansion) + --body-file
cat > /tmp/body.md <<'EOF'
Run `npm test` first
EOF
gh pr create --body-file /tmp/body.md
```

Applies equally to `gh issue create/comment`, `gh release create --notes`, `gh pr comment`, and `git commit -m` with backticks (`-F file` there). Verify the posted body afterward (`gh pr view N --json body`) — garbling is silent.

### GraphQL with Special Characters (--input pattern)

When GraphQL variables contain backticks, dollar signs, or other characters that cause bash escaping issues, pipe JSON via `--input -`:

```bash
# PROBLEM: Backticks and $ in body cause bash escaping errors
gh api graphql -f query='mutation($body: String!) { ... }' -f body='Fixed `@rollup/plugin-terser`'
# Error: Expected VAR_SIGN, actual: UNKNOWN_CHAR

# SOLUTION: Use --input with stdin
cat << 'ENDJSON' | gh api graphql --input -
{
  "query": "mutation($body: String!, $threadId: ID!) { addPullRequestReviewThreadReply(input: {body: $body, pullRequestReviewThreadId: $threadId}) { comment { id } } }",
  "variables": {
    "body": "Fixed `@rollup/plugin-terser` in `dependencies`.",
    "threadId": "PRRT_kwDOxxxxxx"
  }
}
ENDJSON
```

This pattern is especially useful when:
- Replying to PR review threads with markdown formatting
- Any GraphQL mutation where the body contains code references
- Variables contain characters that interact with bash quoting (`$`, `` ` ``, `!`, `\`)

### Fix Common Issues

```bash
# Fix: Update check names in branch protection
gh api repos/OWNER/REPO/branches/main/protection/required_status_checks -X PATCH \
  -f strict=true \
  --input - << 'EOF'
{"checks": [{"context": "job-name (variant)"}]}
EOF

# Fix: Disable code owner reviews blocking auto-merge
gh api repos/OWNER/REPO/branches/main/protection/required_pull_request_reviews -X PATCH \
  -f require_code_owner_reviews=false

# Fix: Add bypass apps
gh api repos/OWNER/REPO/branches/main/protection/required_pull_request_reviews -X PATCH \
  --input - << 'EOF'
{"bypass_pull_request_allowances": {"apps": ["dependabot", "renovate"]}}
EOF
```

## Rate Limits — GITHUB_TOKEN in Actions

The `GITHUB_TOKEN` (installation token) that Actions injects is **not** billed
against your user quota. It has its own, much tighter cap:

- **1,000 REST requests per hour**, charged to the token issued for the
  **repository whose workflow is running** — and shared across *every* call that
  token makes, **including calls to other repositories**. Calling 100 repos from
  one workflow does not give you 100 separate budgets; it draws down the one
  workflow-repo budget. (Separate from the 5,000/hr user limit and the GraphQL
  point budget.)

A workflow that probes many paths across many repos exhausts this fast — e.g. a
collector doing ~15 per-file `contents` calls across ~100 repos ≈ 1,500 calls in
one run, all against the single workflow-repo budget.

**Symptom that misleads:** the `build` job succeeds while the `deploy` /
`deploy-pages` job fails with a 403 — the same exhausted token 403s the Pages
deployment API call, so it reads like a Pages/deploy bug rather than a
rate-limit one.

**Fix — one recursive git-tree call instead of N per-file probes.** To test which
files exist in a repo, fetch the whole tree once and check paths in memory. The
trees endpoint resolves a ref (branch name or SHA) directly, so this is genuinely
one call per repo:

```bash
# One call lists every path at a ref (recursive), vs one call per file
gh api "repos/OWNER/REPO/git/trees/main?recursive=1" \
  --jq '.tree[]? | select(.type == "blob") | .path'
# then: does "SECURITY.md" appear? -> no extra request
```

This drops a ~100-repo sweep from ~1,500 calls to a few hundred (one tree call
per repo) and keeps a nightly Pages build well under the cap.

**Before a long collector loop,** check headroom (the `rate_limit` endpoint does
NOT count against the quota):

```bash
gh api rate_limit --jq '(.resources.core? // empty) | {remaining, reset}'
```

### REST and GraphQL are separate budgets — read both, and never score an error as a state

A user token carries two budgets that reset independently, **and they are not
counted in the same unit**: REST allows **5,000 requests per hour**, GraphQL
**5,000 points per hour**, where a query's point cost rises with the connections
and node depth it requests. `gh api` spends the first; `gh pr view` and
`gh pr checks` spend the second. A long watch therefore exhausts one while the
other still looks healthy — and the single-resource check above will not show
it:

```bash
gh api rate_limit --jq '{core: .resources.core, graphql: .resources.graphql}'
```

**For GraphQL headroom, ask GraphQL itself.** On 2026-10-21 at 13:06 UTC
`gh api rate_limit` reported `graphql.remaining` 3920 of 5000, while the
query below returned `remaining: 0` (reset 13:10:41) and every GraphQL call
failed with "API rate limit already exceeded":

```bash
gh api graphql -f query='{rateLimit{remaining resetAt cost}}'
```

**Pace from the reported `graphql.remaining`, never from a call count.** Because
points are not requests, arithmetic over the number of `gh pr view` invocations
misstates how much GraphQL headroom is left — the same loop costs more against a
PR with many checks and review threads than against a quiet one.

Watch loops are what actually empties these. A 20-PR merge campaign running
`gh pr view` every 150 s across several parallel watchers drained GraphQL first
and REST shortly after, forcing a ~35-minute pause mid-merge; the campaign's
sheer round count — 21 pull requests, every 150 s, several watchers in
parallel — made it invisible until both budgets were gone. Use one watcher for a
fleet, never several against the same list, and an interval of 5–10 minutes.

**The failure mode that costs most is not the pause, it is the misreading.** A
403 inside a loop scored as "pull request closed" makes the loop report that
everything is finished when in truth the budget is empty. Carry the error path
explicitly as `unknown` and stop the loop loudly; a transport failure is a
statement about the request, never about the world.

**When GraphQL is exhausted, fall back to REST** for what REST can answer:
`gh api repos/<owner>/<repo>/pulls/N --jq .mergeable_state` for state, and
`gh api -X POST repos/<owner>/<repo>/pulls -f title=… -f head=<branch> -f
base=main -f body=…` to open one (it returns `.html_url`). Keep GraphQL for what
only it does — review-thread resolution, `enqueuePullRequest`. **Merging stays
on `gh pr merge`**: a REST `PUT /merge` bypasses local merge gating and is not a
substitute.

**GraphQL can refuse while `graphql.remaining` still shows thousands.** On
2026-10-18 every `gh pr create`, `gh pr ready` and `gh issue comment` failed
with `GraphQL: API rate limit already exceeded for user ID …` for about 45
minutes, until the reported `graphql.reset`, while `gh api rate_limit` showed
4441 GraphQL points left. The counter did not show this wall; the refusal text
is the signal. REST kept working throughout:
open the pull request with `"draft": true` in the `POST …/pulls` body, comment
with `POST repos/<owner>/<repo>/issues/N/comments`, change title, body or state
with `PATCH`, and reply to a review comment with
`POST repos/<owner>/<repo>/pulls/N/comments/<comment id>/replies`. Leaving
draft (`gh pr ready`) and resolving review threads have no REST form; retry
those after `graphql.reset` in one background loop.

**When REST is exhausted, read files without the API.** `gh api
repos/<owner>/<repo>/contents/<path>` answers `HTTP 403 … API rate limit
exceeded` once the REST budget is gone. A file in a public repository is still
served by `curl -sfL https://raw.githubusercontent.com/<owner>/<repo>/<ref>/<path>`,
which sends no token; a private file needs git. Current files come from
`git clone --depth=1`, a history search needs a full clone or a deepening fetch.



--- FILE: skills/github-project/references/merge-strategy.md ---

<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->
<!-- SPDX-FileCopyrightText: Netresearch DTT GmbH -->

# Merge Strategy for Signed Commits

This guide explains how to configure GitHub repositories that require both signed commits and clean git history.

## The Problem

GitHub's branch protection offers two relevant settings that conflict:

| Setting | Effect |
|---------|--------|
| `required_signatures` | All commits on protected branch must be signed |
| `required_linear_history` | Only squash or rebase merges allowed (no merge commits) |

**The conflict:** GitHub cannot sign commits during squash or rebase merge operations. When `required_linear_history` is enabled, GitHub rewrites commits server-side, but cannot sign them with your GPG/SSH key.

## The Solution

Use **local rebase + merge commit**:

1. Developers rebase their PR branch locally (signing commits with their key)
2. Force-push the rebased branch
3. Merge via merge commit (GitHub signs the merge commit with its key)

This gives you:
- ✅ Clean, linear history on feature branches
- ✅ Clear merge points on main branch
- ✅ All commits verified (developers sign feature commits, GitHub signs merge commits)

## Repository Settings

Configure via API:

```bash
gh api repos/{owner}/{repo} -X PATCH \
  -f allow_merge_commit=true \
  -f allow_rebase_merge=true \
  -f allow_squash_merge=false
```

| Setting | Value | Reason |
|---------|-------|--------|
| `allow_merge_commit` | `true` | Required for signed commits workflow |
| `allow_rebase_merge` | `true` | GitHub requires at least one of squash/rebase |
| `allow_squash_merge` | `false` | Destroys individual commit history and signatures |

**Note:** GitHub requires at least one of `allow_squash_merge` or `allow_rebase_merge` to be true. Keep `allow_rebase_merge` enabled but don't use it for PRs requiring signatures.

## Branch Protection Settings

Configure via API:

```bash
gh api repos/{owner}/{repo}/branches/main/protection -X PUT \
  --input - << 'EOF'
{
  "required_status_checks": {
    "strict": true,
    "contexts": ["ci"]
  },
  "enforce_admins": true,
  "required_pull_request_reviews": {
    "required_approving_review_count": 1
  },
  "restrictions": null,
  "required_linear_history": false,
  "required_signatures": true,
  "required_conversation_resolution": true
}
EOF
```

| Setting | Value | Reason |
|---------|-------|--------|
| `required_signatures` | `true` | Enforces signed commits |
| `required_linear_history` | `false` | **Must be false** - blocks merge commits |
| `required_conversation_resolution` | `true` | All review threads must be resolved before merge |

## Developer Workflow

### Before Opening PR

```bash
# Ensure commits are signed
git config commit.gpgsign true
```

### Before Merging

```bash
# 1. Fetch latest main
git fetch origin

# 2. Rebase on main (re-signs commits)
git rebase origin/main

# 3. Force-push rebased branch
git push --force-with-lease
```

### Merging

```bash
# Use merge commit strategy
gh pr merge <number> --merge
```

## Auto-Merge Configuration

Auto-merge works with signed commits **only when using merge commit strategy**.

| Strategy | Compatible | Reason |
|----------|------------|--------|
| Merge commit | ✅ | GitHub signs merge commit with its key |
| Rebase | ❌ | GitHub cannot sign rewritten commits |
| Squash | ❌ | GitHub cannot sign squashed commit |

When configuring auto-merge workflows, ensure they use `--merge`:

```yaml
- name: Enable auto-merge
  run: gh pr merge --auto --merge "$PR_NUMBER"
```

## How GitHub Signing Works

When you merge via the GitHub UI or API with merge commit:

1. **Feature branch commits**: Retain original GPG/SSH signatures from developers
2. **Merge commit**: Signed by GitHub's web-flow key (`noreply@github.com`)

Both are marked as "Verified" in the GitHub UI:
- Developer commits show the developer's GPG key
- Merge commits show "Verified" with GitHub as the signer

### "Update branch" and signing (who has to act on "branch out of date")

- **"Update branch" (merge variant)**: the update-merge commit is created and signed by GitHub's web-flow key — satisfies "require signed commits" with zero author involvement. In a squash-merge repo the update commit is squashed away at landing anyway.
- **"Update with rebase" button / rebase merges**: GitHub **cannot re-sign rewritten commits** — fails on signed-commit-protected repos.
- **Local rebase**: signature verification is against the **committer**, not the author. Anyone with head-branch push access (author, or maintainers when "Allow edits from maintainers" is on) can `git rebase -S && git push --force-with-lease`, re-signing with *their own* verified key — authorship and `Signed-off-by` trailers survive. The original author does not have to be the one who rebases.

## Stale-green merge refs: two green PRs can still break main

A PR's `pull_request` checks run against a **snapshot merge ref** (`refs/pull/N/merge` = PR + base *at the moment the run starts*). GitHub never re-runs a PR's checks when the base branch moves afterward — the green badge silently goes stale (observed: an 8-day-old green used to merge). Two PRs that are **textually disjoint** (no git conflict, `MERGEABLE`) can be **semantically conflicting** — e.g. one adds a test fixture rendered from a template the other PR changes. Whichever merges second turns main red, and every open PR then inherits the failure through its merge ref.

Mitigations, in increasing strength:

1. **Required checks + strict up-to-date.** `strict: true` ("Require branches to be up to date") applies **only to the checks listed in `required_status_checks`** (`checks` is the canonical field; `contexts` is its deprecated mirror) — with an empty list it is a **complete no-op**, and red CI does not block merging at all. Audit the flag and both list fields together:

   ```bash
   gh api repos/OWNER/REPO/branches/main/protection \
     --jq '{strict: (.required_status_checks?.strict // false),
            contexts: (.required_status_checks?.contexts // []),
            checks: (.required_status_checks?.checks // [])}'
   # strict=true + empty contexts AND checks → the flag does nothing; populate the checks list
   ```

2. **Merge queue.** Tests `latest main + queued PRs + this PR` (`merge_group` event) before landing; a semantically conflicting PR is ejected instead of breaking main. Prerequisites: workflows must add a `merge_group:` trigger (or checks never report and the queue stalls), and the queue only gates **required** checks — an empty contexts list makes it vacuous too.

Neither catches a semantic conflict no test covers. Post-merge push CI on the default branch stays the last line of defence — keep it.

## Enabling a merge queue

A merge queue on the default branch is the Netresearch standard. The classic branch-protection REST API does **not** expose a merge-queue toggle, so a repository **ruleset** is the only scriptable path. The `merge_queue` rule is **repository-level only** — an org-level ruleset rejects it, so every repository gets its own.

The bootstrap script sets it up. Run it as the third step, after the baseline and after `--from-current-checks`, so the required checks exist when the queue starts gating:

```bash
bash <skill-root>/skills/github-project/scripts/init-branch-protection.sh OWNER/REPO --merge-queue
```

It reads first and refuses without writing when merge commits are disabled, when a required context is one that never reports on a `merge_group` ref (exit 6, see below; a context of the same name pinned to the GitHub Actions app, `15368`, is a workflow job and passes) or an `Analyze (<language>)` context while CodeQL default setup is configured (exit 6), when a ruleset `code_scanning` rule requires CodeQL while default setup is configured (exit 6), when a ruleset requires branches to be up to date, or when a queue already exists with other parameters (exit 1, per-field diff). Otherwise it creates a ruleset `merge-queue` that holds only the queue, reads it back, sets the classic `strict` flag to `false`, and sets the repository's `allow_auto_merge` to `true` with a read-back (with it `false`, `gh pr merge --auto` cannot enqueue: "Auto merge is not allowed for this repository", measured in six netresearch repositories on 2026-10-21/22). A standard queue that is already in place is left alone. `--from-current-checks` keeps `strict` at `false` once a queue is in effect. By hand, the same ruleset is:

```bash
gh api -X POST repos/OWNER/REPO/rulesets --input - <<'JSON'
{
  "name": "merge-queue",
  "target": "branch",
  "enforcement": "active",
  "bypass_actors": [],
  "conditions": { "ref_name": { "include": ["~DEFAULT_BRANCH"], "exclude": [] } },
  "rules": [
    {
      "type": "merge_queue",
      "parameters": {
        "merge_method": "MERGE",
        "grouping_strategy": "ALLGREEN",
        "check_response_timeout_minutes": 180,
        "max_entries_to_build": 10,
        "max_entries_to_merge": 10,
        "min_entries_to_merge": 1,
        "min_entries_to_merge_wait_minutes": 5
      }
    }
  ]
}
JSON
```

These are the org parameters (ruleset `t3x-baseline` in netresearch/t3x-nr-vault). Parameters and gotchas:

- `merge_method`: `SQUASH` | `MERGE` | `REBASE`. The queue owns the merge method for every entry, so per-PR choice disappears. The org uses `MERGE`: it lands with merge commits, which GitHub signs. `REBASE` re-creates commits **unsigned** and fails on a signed-commits branch.
- `grouping_strategy`: `ALLGREEN` (every queued entry must pass) or `HEADGREEN` (only the group's head commit — all changes combined — must pass). `ALLGREEN` is the safe default; `HEADGREEN` only saves CI under contention.
- `check_response_timeout_minutes`: a required check that has not reported by then is treated as **failed** and the entry is ejected. The org uses 180 because 60 was measured to eject green entries under the org's own job backlog — see *A bulk operation of your own can eject queue entries* below.
- `min_entries_to_merge` + `min_entries_to_merge_wait_minutes`: the wait only holds a smaller-than-minimum group. With `min_entries_to_merge: 1` **the wait value is inert** — a single entry already meets the minimum, so it never batches. Only raise the minimum (and the wait) if you actually want to batch, e.g. a Dependabot burst.
- **Every required context must report on `merge_group`.** A workflow-produced context does so only if its workflow has `merge_group:` in `on:`. The app contexts `CodeQL`, `Opengrep OSS`, `betterleaks`, `zizmor` and `SonarCloud Code Analysis` are posted against the pull request only and never on a `merge_group` ref; as required contexts they make every queue entry time out. Drop them from the required checks; for the code-scanning tools a ruleset `code_scanning` rule gates the pull request instead, one entry per tool: `{"type":"code_scanning","parameters":{"code_scanning_tools":[{"tool":"CodeQL","alerts_threshold":"errors","security_alerts_threshold":"high_or_higher"}]}}` (the shape netresearch/t3x-rte_ckeditor_image uses). CodeQL **default setup** is the same case under another name: it posts `Analyze (<language>)` check runs under the GitHub Actions app (`15368`), yet never runs on a `merge_group` ref. On netresearch/typo3-demo the `Analyze (*)` runs on a queue commit belonged to a check suite on `main` created after the merge (the queue fast-forwards, so the SHA is shared), and 0 of 100 `merge_group` runs were CodeQL; on netresearch/typo3-ci-workflows 0 of the last 79 default-setup runs were on a queue branch (measured 2026-10-21). The script therefore refuses a required `Analyze (…)` context whenever `GET repos/{o}/{r}/code-scanning/default-setup` reads `state: configured`. Drop those contexts and replace default setup with a workflow job that calls `netresearch/.github/.github/workflows/codeql.yml@main` (see *CodeQL default setup never analyzes fork PRs* below); only then add the `code_scanning` rule above. netresearch/t3x-nr-bug-reporter#26 merged through its queue with that rule on 2026-10-21; that repository runs advanced setup. **Together with default setup the rule blocks every fork pull request**, because default setup never analyses one: netresearch/enterprise-readiness-skill#151 and netresearch/enterprise-readiness-skill#152 stayed `BLOCKED` with every check green (2026-10-22). The script refuses that combination as well (exit 6). A workflow-prefixed `codeql / Analyze (…)` from a repository's own `codeql.yml` with `merge_group:` reports in the queue and is not refused. In a printed PATCH for classic protection, contexts that were not pinned to an app carry `"app_id": -1`: an omitted `app_id` pins the check to the app that posted it recently, `-1` keeps "any app". `DCO` (app) and `dco / DCO` (workflow) do report on `merge_group`.
- **Publish steps gated on `github.event_name != 'pull_request'` also run on `merge_group`.** Before adding `merge_group:` to a workflow, look for registry login, push, sign, SBOM and attest steps behind that condition. netresearch/phpbu-docker and netresearch/phpmyadmin-docker-compose-stack would have pushed images from `gh-readonly-queue/*` refs out of `build.yml`; both now treat `merge_group` like `pull_request`. phpmyadmin also needed a `type=sha,enable=${{ github.event_name == 'merge_group' }}` metadata tag, because a queue entry has no PR tag for its local identity check.
- **A SARIF upload fails on `merge_group` after a clean scan.** GitHub deletes the `gh-readonly-queue/*` branch as soon as the queue merges, so `github/codeql-action/upload-sarif` (or CodeQL's own upload) races the deletion and fails with `ref 'refs/heads/gh-readonly-queue/…' not found`. The merge commit then shows a red security check while the push run on the same SHA is green; on 2026-10-23 this was the only error in the failed queue run of 10 skill repos. Keep the scan as the queue gate and skip only the upload on that event (`if: always() && github.event_name != 'merge_group'`; netresearch/.github `codeql.yml` sets `upload: never` there). Check what then uploads for the default branch: a preflight that skips a push run once a green `merge_group` run exists for the SHA also skips the scan, and the Security tab is refreshed only by the schedule — exempt the scanning job on `push`, as netresearch/typo3-ci-workflows#315 does for Opengrep. Re-running the failed queue run cannot turn it green, because the re-run targets the deleted branch again; the mark clears with the next merge.
- **A queue that existed before a rollout may carry other parameters.** netresearch/t3x-nr-wellknown had `check_response_timeout_minutes: 60` and `strict_required_status_checks_policy: true`; its PR #28 was removed from the queue with `checks_timed_out` at 16:32:43 UTC on 2026-10-21, while its `ci.yml` run finished 3 s later. When standardizing, read every existing queue's parameters (`GET repos/{o}/{r}/rules/branches/{branch}` and the rulesets) and align the timeout and `strict`; see *A bulk operation of your own can eject queue entries* below.
- **"Require branches to be up to date" must be off** under a queue — classic `strict`, ruleset `strict_required_status_checks_policy`. It forces the author-side rebase the queue replaces. Required checks may stay in classic protection (where `--from-current-checks` writes them) or in a ruleset; the queue gates whichever applies.
- In a ruleset `required_status_checks` rule, `integration_id: 15368` pins a context to the **GitHub Actions app**, so another app cannot satisfy (spoof) it.
- `enforcement: "evaluate"` dry-runs the ruleset (logs what it *would* block) without enforcing — a soft launch before `active`. Rollback is one call: delete the ruleset (or set `enforcement: "disabled"`) and restore the classic `strict` flag.

## Troubleshooting

### Diagnose `mergeStateStatus: BLOCKED` before naming a cause

When a PR is `BLOCKED`, **do not assert a cause** (and never reflexively say "blocked on review" / "waiting for a reviewer") until you have fetched the effective ruleset and named the exact gating rule. `mergeStateStatus` alone does not tell you why; a human-approval gate is almost never the reason. The PR page states the reason in plain text ("All comments must be resolved", "Required statuses must pass") — read it, and the same facts are queryable.

The single most common cause is **unresolved review threads** (including from bots) — check that first:

```bash
# reviewThreads is ONLY available via GraphQL — it is NOT a valid `gh pr view --json` field
gh api graphql -f query='query($owner:String!,$repo:String!,$pr:Int!){
  repository(owner:$owner,name:$repo){pullRequest(number:$pr){
    reviewThreads(first:50){nodes{id isResolved}}}}}' -f owner=O -f repo=R -F pr=N \
  --jq '[.data.repository.pullRequest?.reviewThreads?.nodes[]?|select(.isResolved==false)]|length'
```

Passing `reviewThreads` to `gh pr view --json` errors "Unknown JSON field" — a merge-gate script that does this silently fails open and allows every merge. If the unresolved count is >0, address each comment, reply citing the fix commit, resolve. Only if it is 0 do you inspect the ruleset:

```bash
gh api repos/{owner}/{repo}/rules/branches/{BASE} --jq 'group_by(.type)[]|{type:.[0].type,n:length}'
gh pr view N --json reviewDecision,mergeStateStatus,statusCheckRollup
```

Then name the specific rule (`copilot_code_review`, `required_status_checks`, `non_fast_forward`, merge queue, …). A `pull_request` rule with `reviewDecision: ""` means there is **no human-approval requirement at all**.

**BLOCKED with every visible check green: look for a second, still-running check suite.** `gh run list --commit $SHA` only shows runs with known triggers (push, pull_request, schedule, dispatch) — GitHub-managed **default code scanning and Copilot review run as "dynamic" events and never appear there**. Check-runs are equally misleading for a different reason: the API does include in-progress runs, but a *second* suite from the same app may not have created any check runs yet — so every required context name shows green while that suite is still in progress, and it is the actual blocker. Before concluding the block is structural, list the suites:

```bash
gh api "repos/{owner}/{repo}/commits/{SHA}/check-suites" \
  --jq '.check_suites[] | "\(.status)/\(.conclusion // "—")\t\(.app.slug)\trun_count=\(.latest_check_runs_count)"'
```

An `in_progress` row here with all visible checks green means the BLOCKED state is transient — wait for that suite instead of diagnosing rulesets. (A suite that never concludes is the adjacent, different case — see "CodeQL default-setup check queued forever" below.)

**When every gate checks out, re-query before diagnosing further — `mergeStateStatus` goes stale.** It can still read `BLOCKED` after the condition that set it is gone. GitHub documents the adjacent REST field `mergeable` as returning `null` while *"GitHub has started a background job to compute the mergeability. After giving the job time to complete, resubmit the request."* — `mergeStateStatus` has no such documented note, but was observed to lag the same way; treat the resubmit advice as applying to it too. The tell is a diagnosis that runs out of candidates: every required context present and successful, the approval in place, zero unresolved threads, no second suite in flight, `require_last_push_approval` off — and the state still `BLOCKED`. At that point the cheapest next step is not another ruleset query but the same query again; a second read minutes later returning `CLEAN` on an unchanged head SHA is the confirmation. Two guards make this safe rather than wishful: pin the head SHA across both reads so you know nothing moved, and never treat "probably stale" as merge authority — act on the `CLEAN` read, not on the assumption that produced it. (Observed on `netresearch/ofelia` [#827](https://github.com/netresearch/ofelia/pull/827): signatures, context presence, context conclusions and `require_last_push_approval` were each ruled out before the re-query returned `CLEAN` at the same SHA.)

**When you are about to merge anyway, the REST merge call names the blocker.** `mergeStateStatus: BLOCKED` carries no reason, but a refused `gh api -X PUT repos/{owner}/{repo}/pulls/{n}/merge -f merge_method=merge -f sha=<head SHA you checked>` answers with one line such as `Required status check "betterleaks" is expected`. Observed on two Dependabot PRs that read clean on every queryable gate (required checks green or skipped, branch current, signatures verified, `reviewDecision: APPROVED`); the first guess, the `copilot_code_review` rule, was wrong, and the merge call named a required check that never ran for that actor. The call **merges** when nothing blocks, so it is a diagnosis only where a merge is already authorised — never a probe.

### Never merge while a review is announced or in flight

Once a reviewer is requested or has *started* (by you, a ruleset, or automation), its pendency blocks the merge until it resolves — regardless of `mergeStateStatus`. `CLEAN` is necessary but never sufficient: a `copilot_code_review` ruleset with `review_on_push: false` reports `CLEAN` off an *earlier* commit's review while a new one is still running, and a reviewer that has *started* drops off the request list without submitting — so `reviewRequests: []` is **not** "all clear". Check the timeline / pending-review state, not just `reviewRequests`. Do not request or re-request a reviewer as a pre-merge step (announcing one commits you to waiting). The absence of a review is not itself a blocker — you cannot require a review to *exist* (bots fail, decline, or are unconfigured) — but an *announced* one must be allowed to finish.

### CodeQL default-setup check queued forever on a diff with nothing to analyze

CodeQL **default setup** (app `github-advanced-security`, check name `CodeQL`)
can sit `queued` indefinitely on a PR whose diff contains **no files of any
configured language** — e.g. default setup configured for `actions` only and a
docs-only diff (`SKILL.md` + `plugin.json`). Instead of auto-passing, the check
never concludes, and `mergeStateStatus` stays `UNSTABLE` (or `BLOCKED` if the
check is required). Verified behaviors (2026-08-03, two wedged suites on one PR):

- `POST /repos/{owner}/{repo}/check-suites/{check_suite_id}/rerequest` returns
  **404** for default-setup suites — there is no workflow run to re-run either.
- **Close/reopen spawns a fresh suite that wedges identically** — the re-run
  has the same nothing-to-analyze diff.
- Diagnose with: `gh api repos/{owner}/{repo}/code-scanning/default-setup`
  (languages) vs. the PR's changed files.

Escape paths, in preference order: (1) if the check is not required, get
explicit human authorization and merge via the REST endpoint
(`gh api -X PUT repos/{owner}/{repo}/pulls/{n}/merge -f merge_method=merge` —
see the section below on REST-vs-GraphQL); (2) touch a file of a configured language so the
analysis has an object; (3) wait — GitHub sometimes expires wedged queued
check-runs after several hours, but neither timing nor outcome is dependable.

### CodeQL default setup never analyzes fork PRs — required `Analyze` contexts become unsatisfiable

The sibling failure to the wedge above, structural instead of transient:
CodeQL **default setup** does not analyze pull requests from forks at all.
Where its contexts (`Analyze (actions)`, `Analyze (python)`, …) are **required**
in branch protection, every fork PR sits at `mergeStateStatus: BLOCKED` with
all visible gates green — the contexts simply never appear on the head commit.
Same-repo PRs merge fine, so the hole stays invisible until the first outside
contribution (observed 2026-08-26, netresearch/git-workflow-skill#226).

A ruleset `code_scanning` rule for CodeQL has the same effect: it waits for a
CodeQL result on the pull request, and default setup never produces one for a
fork. No context is missing from the rollup here, so the PR looks fully green.
The 2026-10-21 merge-queue rollout added that rule to 32 repositories, 31 of
them on default setup; netresearch/enterprise-readiness-skill#151 was the first
fork PR to hit it. The head's `github-advanced-security` suite showing only
SonarCloud uploads is the same tell.

Two things make the diagnosis slow if you do not know them:

- The requirement usually hides in **classic branch protection**
  (`repos/{r}/branches/{base}/protection`, admin-only), which the
  `rules/branches/{base}` endpoint never shows — the ruleset view looks
  permissive while the classic list names the Analyze contexts.
- The missing contexts leave **no trace in the rollup**. Diagnose with GraphQL
  `statusCheckRollup { contexts { ... isRequired(pullRequestNumber: N) } }`:
  the required-but-absent names are the ones not in the list at all. The head's
  `github-advanced-security` check suite carrying only third-party SARIF
  uploads (Sonar, zizmor, …) confirms default setup never ran.

**Workaround to land the blocked fork PR:** push the identical head commit as
a base-repo branch and open a helper draft PR — default setup analyzes that
one and attaches its `Analyze` check runs to the SHA, which the fork PR shares,
so it unblocks. After the fork PR merges, GitHub marks the helper PR "merged"
by reachability and auto-deletes its branch; no separate cleanup.

**Durable fix:** replace default setup with an advanced-setup `codeql.yml`
whose job is named `Analyze` with a language matrix — the check runs then carry
exactly the context names the protection already requires, so the required list
stays untouched. Order matters: **disable default setup first**
(`gh api -X PATCH repos/{r}/code-scanning/default-setup -f state=not-configured`)
— while it is enabled, GitHub refuses SARIF uploads from advanced
configurations and the new workflow's Analyze jobs fail. Mirror the old
config (`gh api repos/{r}/code-scanning/default-setup` shows languages, query
suite, schedule). As a workflow it runs on fork PRs like any other, subject to
the usual once-per-push run approval (fixed this way in
netresearch/git-workflow-skill#240). Where a `code_scanning` rule gates instead
of required contexts, the job name does not matter: call the shared
`netresearch/.github/.github/workflows/codeql.yml@main` with `languages: auto`,
as the `skill` and `typo3-extension` templates of netresearch/.github do.
Fork PRs of netresearch/t3x-rte_ckeditor_image and netresearch/ldap-manager got
their CodeQL results that way.

### A fork PR BLOCKED with green checks usually has more than one cause

The GitHub page shows one blocking reason at a time, so a fork PR that is
`BLOCKED` with every check green can carry several independent blockers. Check
all of these before saying "only X blocks" (observed together on
netresearch/netresearch-branding-skill#110):

1. **Unsigned contributor commits under classic `required_signatures`.** The
   merge is refused with "Commits must have verified signatures". Like the
   CodeQL contexts above, this lives in classic branch protection, which the
   rulesets endpoint does not show:
   `gh api repos/{owner}/{repo}/branches/{base}/protection/required_signatures --jq .enabled`.
2. **The `code_scanning` rule waiting for a CodeQL result** that default setup
   never produces for a fork head (previous section; same helper-branch
   workaround).
3. **Workflow runs waiting for approval.** Where the repository's approval
   policy covers the contributor (Settings → Actions → "Approval for running
   fork pull request workflows"), fork runs need a maintainer's approval after
   every new head SHA
   (`gh api -X POST repos/{owner}/{repo}/actions/runs/{run_id}/approve`);
   `pr-status.sh` from the git-workflow skill prints those commands.

To sign the contributor's commits without losing their history — the branch
needs "Allow edits from maintainers" — re-create every commit with its own
tree, message and author, remapping the parents, so the branch's own merge
commits survive. A linear `git rebase -S` replays the contributor's commits
without those merges and hits conflicts the merges had already resolved.

```bash
# Run in a clone of the upstream repository, on a local branch tracking the
# fork head. BASE is the PR's base branch on the upstream remote (origin here).
git fetch origin
BASE=origin/main
OLD=$(git rev-parse HEAD)   # the fork head being rewritten; the push expects it
declare -A map
while read -r c; do
  args=()
  for p in $(git rev-list --parents -n1 "$c" | cut -d' ' -f2-); do
    args+=(-p "${map[$p]:-$p}")
  done
  map[$c]=$(
    GIT_AUTHOR_NAME="$(git log -1 --format=%an "$c")" \
    GIT_AUTHOR_EMAIL="$(git log -1 --format=%ae "$c")" \
    GIT_AUTHOR_DATE="$(git log -1 --format=%aD "$c")" \
    git commit-tree -S "${args[@]}" -m "$(git log -1 --format=%B "$c")" "$c^{tree}"
  ) || { echo "signing failed for $c" >&2; break; }
done < <(git rev-list --reverse --topo-order "$BASE..HEAD")
new=${map[$OLD]}
[ -n "$new" ] && git diff --quiet HEAD "$new" && git reset --keep "$new"   # same tree, now signed
```

Then bring the branch up to date with a signed `git merge -S "$BASE"` and push
it to the fork with the rewritten SHA as the expected value,
`git push <fork-remote> HEAD:<branch> --force-with-lease=<branch>:"$OLD"`, so a
commit the contributor pushed meanwhile is not overwritten. The committer of every re-created
commit is you, which is what signature verification checks; authorship and
`Signed-off-by` trailers stay the contributor's.

### `gh pr merge` falsely reports "base branch policy prohibits the merge"

`gh pr merge` (GraphQL path) can fail with "the base branch policy prohibits the merge" even when every requirement is verifiably satisfied (rollup SUCCESS, signature valid, 0 required approvals, 0 unresolved threads, branch up to date, no blocking rulesets), and `--auto` never fires either. The REST endpoint succeeds immediately on the same head SHA:

```bash
gh api -X PUT repos/{owner}/{repo}/pulls/{n}/merge -f merge_method=merge
```

Use this **only after the merge gate is genuinely verified** — the REST path bypasses whatever GraphQL mis-evaluated, so it must not be used to force past a *real* policy block.

### All merge methods rejected — merge-method ruleset deadlock

When every `gh pr merge --merge/--rebase/--squash` (and REST `PUT .../merge`) returns `"<method> merges are not allowed on this repository"` (HTTP 405) even though `gh api repos/<r> --jq '{allow_merge_commit,allow_squash_merge,allow_rebase_merge}'` shows a method enabled, the cause is a deadlock: an **org-level ruleset** sets `pull_request.allowed_merge_methods`, and the effective allowed set is the **intersection** of that with the repo's `allow_*_merge` flags. If the org allows only `squash` but the repo has `allow_squash_merge: false`, the intersection is empty and nothing merges.

Diagnosis gotcha: `repos/<r>/rules/branches/main` may show a *permissive* list because `orgs/<org>/rulesets` is not listable without org-admin, so the stricter org ruleset is invisible and the contradiction looks like a GitHub bug — it isn't. `--admin` does **not** bypass `allowed_merge_methods` (it only bypasses status checks / required reviews). The only fixes are repo/org-admin actions (enable the org-required method at the repo level, exempt the repo, or adjust the org ruleset). Do not toggle repo merge settings autonomously on an inference — flag it for the owner.

### A quota-limited Copilot review does not block the merge

`copilot_code_review` in a ruleset is an **automation** rule — "automatically request Copilot code review" — not a merge gate. Per [GitHub's docs](https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/configure-automatic-review), Copilot always leaves a *Comment* review, it never counts toward required approvals, and it does not block merging. Its two parameters (`review_draft_pull_requests`, `review_on_push`) only widen *when* the request fires.

So when Copilot is quota-limited and posts `COMMENTED` — *"unable to review … reached their quota limit"* — nothing is gated by it. Observed in `netresearch/t3x-nr-image-optimize` PR #140: the `copilot_code_review` rule was active on `main`, Copilot posted exactly that quota review, `mergeStateStatus` went `CLEAN`, and a plain `gh pr merge --merge` succeeded without `--admin`.

**Never reach for `--admin` on this diagnosis.** If a PR is `BLOCKED` while the Copilot check is red, the cause is elsewhere — find it before escalating:

```bash
# 1. Which rules actually gate this branch? (copilot_code_review is not one)
gh api repos/$R/rules/branches/main --jq '[.[].type]'

# 2. The required contexts — the only checks that can BLOCK
gh api repos/$R/rules/branches/main \
  --jq '.[] | select(.type=="required_status_checks")
        | .parameters.required_status_checks[].context'

# 3. Are approvals required, and is one outstanding?
gh api repos/$R/rules/branches/main --jq '.[] | select(.type=="pull_request")'
gh pr view $PR --repo $R --json reviewDecision,latestReviews
```

The usual real causes: a required check still pending (see "`mergeStateStatus: BLOCKED` — Check Required vs Non-Required Checks First" in `auto-merge-guide.md`), unresolved review threads, or a `pull_request` rule whose required approval is missing because the auto-approve job raced the Copilot review request (see "Auto-Approve Race Condition"). A quota-limited Copilot review is never the reason.

**The real hazard runs the other way.** The gate reads as satisfied while no review happened: the `COMMENTED` review object exists, checks go green, the PR merges — and nothing reviewed the diff. Treat a quota-limited Copilot review as *no review*, and decide on that basis whether the change needs human eyes before merging.

**CLEAN variant — the quota review does NOT always block.** With a ruleset configured `review_on_push: false`, a quota-limited Copilot review (same `COMMENTED` "reached their quota limit" body) can leave `mergeStateStatus: CLEAN` and `gh pr merge` succeeds without `--admin` (observed 2026-07-30, three consecutive PRs on one repo). Do not expect `BLOCKED` as proof of the quota condition — check the review body itself. The risk inverts here: the merge is *allowed* but lands with zero substantive review. Treat the quota review as landed-but-content-free — the merge gate may proceed, but explicitly flag the PR (in the report to the user) for retroactive review once quota resets, instead of letting it merge silently unreviewed.

### SonarCloud PR gate re-attributes pre-existing issues to a refactor

SonarCloud measures "new code" as lines touched by the PR, so mechanical refactors (e.g. method extraction, literal→const swaps) re-attribute pre-existing duplication and uncovered lines to the PR, failing `new_duplicated_lines_density` or `codecov/patch`. Don't resort to test-theater or risky out-of-scope de-duplication inside a behavior-preserving PR. First fix what is genuinely cheap and meaningful (a small unit test for an extracted helper often flips `codecov/project` green). For the structural residue, confirm the gate is **non-required** (`mergeStateStatus: UNSTABLE`, not `BLOCKED`), write a "Quality gate note" section into the PR body naming the metric, the cause, and why it is out of scope, then merge. Style-rule whack-a-mole (each push surfacing the next batch) is best handled by modernizing the whole file in one pass — but verify bulk codemods with the language's own parser (a naive `var`→`const` regex turns `var x;` into invalid `const x;`).


### SonarCloud operational gotchas (onboarding + Automatic Analysis)

- **The project's "Main Branch" slot defaults to `master`** regardless of the GitHub default branch, so first scans of a `main`-repo land on a short-lived branch literally named `main` and the overview claims "master branch has not been analyzed yet". Fix in Project → Administration → Branches: delete the short-lived `main` first (else the rename fails with "name already exists"), rename the Main Branch to `main`, trigger a fresh scan.
- **What Automatic Analysis honors vs. ignores**: `.sonarcloud.properties` file exclusions and inline `// NOSONAR` comments work; `sonar.issue.ignore.multicriteria` rule-ignores are a **no-op** there — don't spend a round-trip on them, use exclusions or NOSONAR.
- **Automatic Analysis (GitHub-App mode) silently ignores `sonar-project.properties`.** The file it honors is **`.sonarcloud.properties`** at repo root (Java-properties syntax), on the analyzed branch; it overrides UI Analysis-Scope settings. For false-positive sensors on template files (e.g. TYPO3 Fluid tripping the HTML sensor), plain `sonar.exclusions=...` removes the files from scope and cannot break analysis — prefer it over disabling sensors or `sonar.issue.ignore.multicriteria`.

### "Merge commits are not allowed on this repository"

**Cause:** `allow_merge_commit` is false in repository settings.

**Fix:**
```bash
gh api repos/{owner}/{repo} -X PATCH -f allow_merge_commit=true
```

### "Base branch requires signed commits. Rebase merges cannot be automatically signed"

**Cause:** `required_linear_history` is true, forcing rebase merge which GitHub cannot sign.

**Fix:**
```bash
gh api repos/{owner}/{repo}/branches/main/protection -X PUT \
  --input - << 'EOF'
{
  ...existing settings...,
  "required_linear_history": false
}
EOF
```

### Auto-merge fails with signature error

**Cause:** Auto-merge configured with rebase or squash strategy.

**Fix:** Update auto-merge workflow to use `--merge` flag instead of `--rebase` or `--squash`.

### Rulesets cannot block merge on a pending review

Neither branch protection nor rulesets support "block merge while any requested reviewer hasn't submitted yet". The options available are adjacent but not equivalent:

| Setting | What it does | Not what you want |
|---|---|---|
| `required_approving_review_count: 1` | Needs **one approval** | Doesn't wait for other requested reviewers |
| `required_review_thread_resolution: true` | Blocks on **unresolved threads** | Doesn't block before any thread is created |

If you need to hold merge until Copilot (or any other requested reviewer) has actually posted its review, the workaround is a custom GitHub Actions status check that queries pending reviewers and fails if any are outstanding — then require that check in branch protection.

```bash
# Example: fail the check if any reviewer — user or team — is still requested.
pending=$(gh api "repos/$REPO/pulls/$PR" \
  --jq '((.requested_reviewers // []) | length) + ((.requested_teams // []) | length)')
if [[ "$pending" -gt 0 ]]; then
  echo "::error::Still waiting on $pending review request(s) (user/team)"
  exit 1
fi
```

### Renaming a CI job orphans its required status check → PR stuck "Expected"

**Every CI step that runs on a PR belongs in `required_status_checks` — advisory checks are decorative.** If a job's result would not stop a merge, the job provides no protection; a "flaky" or "in flux" check gets fixed or removed, not demoted to advisory. When adding a new CI job, add its context name to the ruleset in the same change; when a future shape change (sharding, matrix expansion) will rename the contexts, edit the ruleset twice — once now to lock the current shape, once at the change — rather than deferring the lock.

Required status checks are matched by **exact context name**. Renaming a job — including changing a **matrix value** that appears in the job name (e.g. `PHPStan (8.2, ^14.0)` → `PHPStan (8.2, ^14.3)`) — produces a *new* context name. The old required context no longer reports, so it sits "Expected — Waiting for status to be reported" forever and the PR is `BLOCKED`, even though every job is green.

This is a silent trap: the CI change looks self-contained, but the required-checks list in branch protection / the ruleset still names the old job. Treat the required-checks list as a declared value that must be swept whenever a job name changes.

**The same orphan happens when you *enable a previously-disabled/skipped* matrix job** — and this one is nastier because nothing was renamed. While the job is disabled it still reports its **bare** context (e.g. `ci / Functional Tests SQLite`) as a `skipped`/`neutral` run, which *satisfies* the required check — so the required-checks list looks correct and merges pass. The moment you enable it, GitHub expands that one bare context into N **matrix** contexts (`ci / Functional Tests SQLite (8.2, ^13.4)` … `(8.5, ^14.3)`); the bare required context now has no matching run and the PR is permanently `BLOCKED` — with **every visible check green** (the missing required context does not appear in `gh pr checks`). Diagnose by diffing the ruleset's `required_status_checks[].context` list against the actual `repos/$REPO/commits/$SHA/check-runs[].name` values; the fix is the same ruleset/branch-protection update below (swap the bare context for the matrix-expanded ones). This ALSO is what finally makes a newly-enabled job actually *gate* merges.

```bash
# After renaming any matrixed/required job, update the ruleset's contexts.
# Rulesets (PUT the full ruleset; required_status_checks is nested under rules):
gh api "repos/$REPO/rulesets/$ID" > /tmp/rs.json    # back up first
# edit the .rules[] required_status_checks[].context entries, then:
gh api -X PUT "repos/$REPO/rulesets/$ID" --input /tmp/rs.json

# Classic branch protection: this endpoint REPLACES the entire contexts list,
# so you must send ALL required contexts (renamed + unchanged), or you silently
# drop the others. Read the current list, swap the renamed entries, send it back.
gh api "repos/$REPO/branches/main/protection/required_status_checks" \
  --jq '{strict: .strict, contexts: .contexts}' \
  | jq '.contexts |= map(sub("\\^14\\.0"; "^14.3"))' > /tmp/rsc.json
gh api -X PATCH "repos/$REPO/branches/main/protection/required_status_checks" --input /tmp/rsc.json
```

Verify the contexts match the jobs the workflow now emits. The context string is the **check-run name** from `repos/$REPO/commits/$SHA/check-runs[].name`, which for reusable-/multi-job workflows includes the `workflow / job (matrix)` prefix (e.g. `ci / PHPStan (8.2, ^14.3)`) — not the bare job name. (This is the same source `init-branch-protection.sh` uses; the `/actions/runs/{id}/jobs` endpoint returns the bare job name and is wrong for context matching.)

### A job skipped on one event orphans its required check → draft PRs stuck "Expected"

**Require a workflow's aggregate check, not the individual jobs of a workflow that skips jobs per event.** The `checks.yml` in netresearch TYPO3 extensions (read in t3x-nr-image-optimize) runs on `pull_request` with `types: [opened, synchronize, reopened, ready_for_review]` and gives `security`, `betterleaks`, `zizmor`, `fuzz`, `license-check` and `codeql` the condition `if: github.event.action != 'ready_for_review'`. Marking a draft ready therefore starts a second run of the same workflow on the same head SHA in which those jobs are skipped, and a skipped `uses:` job never materialises its inner check names. A ruleset that requires one of them by name — `security / Composer Audit` — then shows "Expected — Waiting for status to be reported" with every check green, and the PR stays `BLOCKED`.

The passing result from the earlier run does not count, and re-running the job inside that earlier run does not clear it. Removing the individual context cleared it at once. This points to GitHub evaluating the newest run of the workflow, which is an inference from those two tests, not documented behaviour. Observed 2026-09-26 on netresearch/t3x-nr-image-optimize#207 (runs 212 and 213 of "Checks").

The fix is the one the template's own `gate` job comment gives: require `All security checks`, which depends on every job and keeps its name on every event, and drop the individual job contexts. The same reasoning covers `merge_group`, where pull-request-only jobs never appear. To find repositories with the trap:

```bash
# Required contexts that name an individual job of an event-gated workflow,
# on the default branch (pass another branch name to check a release branch)
BRANCH=$(gh api "repos/$REPO" --jq .default_branch)
gh api "repos/$REPO/rules/branches/$BRANCH" --jq '
  [.[] | select(.type=="required_status_checks") | .ruleset_id as $id
   | .parameters.required_status_checks[].context
   | select(test("^(security|betterleaks|zizmor|fuzz|license-check|codeql) /"))
   | "\(.) (ruleset \($id))"]'
```

The gate fails when one of its jobs fails or is cancelled, so it does not block a finding from a scanner that runs report-only. zizmor is one: the shared `zizmor.yml` uploads its findings as SARIF and its job succeeds whatever it finds, so `All security checks` passes on a zizmor finding. betterleaks is not report-only (`--exit-code 2` fails its job on a finding). A report-only finding blocks a pull request only through a ruleset `code_scanning` rule, so dropping the individual contexts must not drop such a rule. Raised by CodeRabbit on netresearch/magento2-patches#8; the template comments were corrected in netresearch/.github#553.

### Required "SonarCloud Code Analysis" status absent — AutoScan never analyzed the PR

The same "BLOCKED with every visible check green" symptom also occurs with a *correct* required-checks list when the context comes from an external app that never ran. SonarCloud AutoScan sometimes never analyzes a PR: its `sonarqubecloud` check-suite sits `queued` with zero check runs, so the required `SonarCloud Code Analysis` context never reports (and, as above, a missing context does not appear in `gh pr checks`). Diagnose:

```bash
# The sonarqubecloud check-suite is queued with no runs
gh api "repos/$REPO/commits/$SHA/check-suites" \
  --jq '.check_suites[] | {app: .app.slug, status, runs: .latest_check_runs_count}'
# → {"app":"sonarqubecloud","status":"queued","runs":0}

# The project's last analysis on sonarcloud.io predates the PR
curl -s "https://sonarcloud.io/api/components/show?component=$SONAR_PROJECT_KEY" \
  | jq -r '.component.analysisDate'
```

**Fix:** push a new head to the PR branch — an empty commit suffices; the push re-fires the webhook and analysis completes:

```bash
git commit -S --signoff --allow-empty -m "chore: retrigger CI"
git push
```

### Merge queue silently fails to enqueue a green PR

On a repo with a `merge_queue` ruleset rule, an all-green PR with auto-merge armed (`mergeStateStatus: CLEAN`) sometimes never enters the queue — no queue entry, no `merge_group` build, it just sits OPEN. Confirm it is genuinely stuck before acting:

```bash
gh api graphql -f query='query($owner:String!,$repo:String!,$branch:String!){
  repository(owner:$owner,name:$repo){
    mergeQueue(branch:$branch){entries(first:10){nodes{pullRequest{number} state position}}}
  }
}' -f owner=OWNER -f repo=REPO -f branch=main \
  --jq '.data.repository.mergeQueue?.entries?.nodes[]? // empty'
gh run list --repo OWNER/REPO --event merge_group -L 5   # any build for this PR?
```

If there is no entry and no `merge_group` run after the required checks have passed, an admin merge with the queue's configured method (preserves signatures with `--merge`) is possible **only when the ruleset that holds the `merge_queue` rule lists you as a bypass actor**. A ruleset is bypassed only by the actors on its bypass list; being a repository admin is not enough. Read it first:

```bash
gh api "repos/OWNER/REPO/rulesets/<id>" --jq '{name, bypass_actors, current_user_can_bypass}'
```

The org-standard queue has `bypass_actors: []` (ruleset `t3x-baseline` in netresearch/t3x-nr-vault, and the ruleset `init-branch-protection.sh --merge-queue` creates). There `current_user_can_bypass` reads `never` even for an org admin, so `--admin` does not get past the queue. What is left is to arm auto-merge again (`gh pr merge <PR> --disable-auto`, then `gh pr merge <PR> --auto`); whether that clears this failure mode has not been measured. Where the answer is `always` or `pull_requests_only`:

```bash
gh pr merge <PR> --repo OWNER/REPO --merge --admin
```

> **Scope of this escape hatch:** only in repos whose governance is ours, only for this stuck-queue failure mode, and only with the operator's explicit go for that PR. `--admin` bypasses required reviews and status checks wholesale — on upstream/community repos (or to merge your own unreviewed PR anywhere) it is never appropriate, no matter how trivial the fix or how red the main branch. Holding admin permission is a trust grant, not a merge mandate.

### A bulk operation of your own can eject queue entries

`check_response_timeout_minutes` ejects an entry whose required checks have not *reported* in time. The sizing advice above — "above one CI cycle" — assumes normal load. A fan-out you initiate breaks that assumption, and the failure looks nothing like a timeout.

The signature is a PR that is **green and ejected**: `state: OPEN`, `mergeStateStatus: CLEAN`, `reviewDecision: APPROVED`, the merge queue empty, `isInMergeQueue: false`, **every `merge_group` run green**, and no red check anywhere. `pr-status.sh` reports `NEXT: merge — clean`, because from its side nothing is wrong; the entry is simply gone. Nothing names the timeout — you have to compare elapsed time against it yourself.

Measured 2026-09-18: a 21-repository template sync produced 237 queued jobs org-wide. Two consumers with merge queues (`check_response_timeout_minutes: 60`, 40 and 16 required contexts on `merge_group`) each had their PR ejected **twice**. At the point of diagnosis one entry's `CI` run had been executing for 65 minutes against a 60-minute budget. Neither PR had a failing check at any point.

```bash
# Is this an ejection-by-timeout rather than a failure?
gh api "repos/$R/rulesets" --jq '.[].id' | while read -r id; do
  gh api "repos/$R/rulesets/$id" --jq '.rules[]? | select(.type=="merge_queue") | .parameters'
done                                   # read check_response_timeout_minutes
gh api "repos/$R/actions/runs?event=merge_group&per_page=20" \
  --jq '.workflow_runs[] | [.created_at, .name, .status, (.conclusion // "-")] | @tsv'
# a run still `in_progress` older than the timeout IS the cause
```

**The ordering rule:** let the backlog drain before enqueueing into a merge-queue repo. Re-enqueueing into the same congestion restarts the entry's checks and buys another ejection. Where a batch touches both plain and merge-queue repos, merge the plain ones first and hold the queued ones until the org's job backlog is near zero — measure it per [`ci-runner-capacity.md`](ci-runner-capacity.md), at the **job** level.

Do not reach for `--admin` here. The escape hatch above is for a queue that never builds; this queue built, passed, and ran out of clock. Waiting is the fix.

### Arming a merge queue PR: `--auto` with no strategy flag

On a `merge_queue` repo the **queue owns the merge method**, so passing an
explicit strategy to `gh pr merge` prints a warning (the command still
succeeds and enqueues the PR):

```bash
gh pr merge <PR> --repo OWNER/REPO --merge --auto
# gh output: ! The merge strategy for main is set by the merge queue
```

To avoid the confusing warning, arm it with a bare `--auto` (no
`--merge`/`--squash`/`--rebase`); the queue applies its configured method when
the PR reaches the front:

```bash
gh pr merge <PR> --repo OWNER/REPO --auto     # enqueues when the gate passes
```

(The explicit-strategy form is still correct for `--admin` bypass merges, which
run outside the queue — as in the enqueue-failure fallback above, and only for
a bypass actor of the queue's ruleset.)

### Batch review-fix commits before pushing — each push re-runs the full PR CI

Merge queue repos typically re-run the **entire** required matrix (functional
across every PHP × TYPO3 combo, e2e, etc.) on every push to the PR head (the
standard PR status checks; the queue's own CI runs later on the merge group),
which can be ~8+ minutes. Fixing reviewer nitpicks one-commit-one-push then
turns into many full-matrix cycles for trivial edits.

Collect **all** outstanding review fixes across every open thread, apply them
locally, run the relevant suites once, and push a **single** commit. Only then
reply to and resolve the threads. This costs one CI cycle instead of N, and avoids
racing a half-fixed head into the queue.


### A red non-required check on a commit its tool reports clean is a stale mirror — wait for the next analysis, never dismiss

Two non-required checks regularly go red *after* the underlying problem is gone, and both keep `mergeStateStatus` at `UNSTABLE` until they clear:

- **SonarCloud code-scanning (`SonarCloud`, the SARIF upload)** lags SonarCloud's own analysis. On `netresearch/t3x-nr-image-optimize` PR #174 the fix commit's analysis closed the `tssecurity:S8707` issue at 11:22:48Z (`api/issues/search … status=CLOSED`, quality gate `OK`), yet the SARIF uploaded at 11:23:12Z still carried it, so GitHub opened a code-scanning alert and the `SonarCloud` check failed on the very commit that fixed it. The `SonarCloud Code Analysis` check (the quality gate) was green the whole time.
- **`codecov/project`** posts an interim status after the *first* flag upload. With a unit and a functional flag, the first status compares the unit-only total against the full base (`89.38% (-4.60%) compared to …`) and goes red; it flips green once the functional upload arrives. `api.codecov.io/api/v2/github/<org>/repos/<repo>/pulls/<n>` shows `head_totals` = `base_totals` while the check still says red.

Diagnose at the source, not at the badge:

```bash
# SonarCloud: is anything actually open on this PR?
curl -sS "https://sonarcloud.io/api/qualitygates/project_status?projectKey=$KEY&pullRequest=$PR" | jq '.projectStatus.status'
curl -sS "https://sonarcloud.io/api/issues/search?componentKeys=$KEY&pullRequest=$PR&issueStatuses=OPEN,CONFIRMED" | jq '.total'   # `statuses` is deprecated; REOPENED is not an issueStatuses value
# When did the analysis close the issue vs. when was the SARIF uploaded?
curl -sS "https://sonarcloud.io/api/issues/search?componentKeys=$KEY&pullRequest=$PR&rules=$RULE&additionalFields=_all" | jq '.issues[] | {status, closeDate}'
gh api "repos/$R/code-scanning/analyses?pr=$PR&tool_name=SonarCloud&per_page=3"   # pr=, not ref=: an upload against refs/pull/$PR/merge is invisible to the ref filter --jq '.[] | "\(.created_at) \(.commit_sha[0:8]) results=\(.results_count)"'
# codecov: head vs base totals, independent of the interim status
curl -sS ${CODECOV_TOKEN:+-H "Authorization: Bearer $CODECOV_TOKEN"} "https://api.codecov.io/api/v2/github/$ORG/repos/$REPO/pulls/$PR" | jq '{head: .head_totals.coverage, base: .base_totals.coverage}'
```

If the source is clean: do **not** dismiss the code-scanning alert or mark anything "safe" — the next analysis closes the alert and the check with it; a check-run's conclusion is immutable, so on the current commit `UNSTABLE` stays until then. Since the fix is already in the tree, this is the one case where an otherwise idle push is the remedy rather than a workaround — but it must be one that actually triggers an analysis. Automatic Analysis runs on any push; a CI-based analysis runs only when its workflow handles the event, so check which `pull_request` types the workflow subscribes to before assuming a rebase will clear it. If the source is *not* clean, the finding is real: read the taint flow (`additionalFields=_all` → `.flows`) before touching code — the rule title names the category, the flow names the sink.

### A green `main` and a red PR on the same tree: a tool resolved at CI time has released

When a PR turns red on a check whose files it does not touch, and `main` is green on the same tree, look for a tool that CI installs at run time rather than from a pinned version. php-cs-fixer v3.95.19 changed `binary_operator_spaces` padding inside array literals and turned three repositories' `ci / Code Style` red overnight with no commit anywhere. `main`'s green run dated before that release is stale evidence, not an all-clear: compare its timestamp with the tool's release date, or re-run it.

Where that check is required, every PR in the repository is blocked by it, including ones that change no code. In the case above, the route that worked was to apply the new style in the blocked PR itself, so that the style fix and the blocked change landed together.

## References

- [GitHub Branch Protection](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches)
- [Signing Commits](https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-commits)
- [About Merge Methods](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/about-merge-methods-on-github)



--- FILE: skills/github-project/references/multi-repo-operations.md ---

<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->
<!-- SPDX-FileCopyrightText: Netresearch DTT GmbH -->

# Multi-Repo Operations

Batch and fleet-wide operations — releases, rebases, lint fixes, config rollouts — across many repositories in one sweep.

## Hard Rule: Dry-Run Before Any >3-Repo Operation

Batch ops amplify small mistakes linearly. A version-bump ordering bug that affects 1 repo is a nuisance; across 30 repos it's 30 broken release workflows. Before executing on more than 3 repos, produce a dry-run manifest and get explicit approval.

### Copying a template file across repos: gate on a purely additive diff

Syncing a shared file (`checks.yml`, a lint config, a workflow) by writing the template over each consumer destroys repo-specific content **silently**. Nothing errors, nothing is reported, and the loss only surfaces when someone misses the thing that used to be there.

Make the sweep decide per repo, and let removals stop it. As one function per repository — the early `return` below needs that, and a paste into a bare loop wants `continue` instead:

```bash
sync_one() {   # $current = the consumer's copy, $template = the shared source
d=$(diff -u "$current" "$template" 2>/dev/null); rc=$?
[ "$rc" -ge 2 ] && { echo "$REPO: CANNOT COMPARE (file missing?)"; return; }

# Drop the two `---`/`+++` header lines, then count every marked line.
added=$(printf '%s\n'   "$d" | tail -n +3 | grep -c '^+' || true)
removed=$(printf '%s\n' "$d" | tail -n +3 | grep -c '^-' || true)

if   [ "$added" = 0 ] && [ "$removed" = 0 ]; then echo "$REPO: already current"
elif [ "$removed" != 0 ]; then echo "$REPO: MANUAL +$added/-$removed"; printf '%s\n' "$d" | tail -n +3 | grep '^-'
else apply_and_open_pr
fi
}
```

Two details in that snippet are load-bearing, and the obvious shorter forms are wrong:

- **Strip the header, do not exclude a second character.** `grep -cE '^-[^-]'` looks right — it skips the `--- file` header — but it also skips every removed **blank** line and every removed line whose own first character is `-`, which is what a YAML list item at column 0 looks like. Both then count as zero removals and the repo lands in the *first* branch: reported as already current, never flagged, never opened. The gate fails exactly in the case it exists for. (`cur='on:\n- push\n- local\n'` vs `tpl='on:\n- push\n'` scores `+0/-0` under the short form and `+0/-1` under this one.)
- **Check `diff`'s exit status before trusting the counts.** If the consumer does not have the file yet, `diff` exits 2 with empty stdout, both counts are 0, and `|| true` swallows the failure — so the repositories that are *missing* the shared file are the ones reported as synced. `|| true` is still required on the `grep -c` (no matches exits 1, fatal under `set -e`), it just must not be the only status handling.

Removals are not automatically wrong — they are **unclassified**. In a 21-repository sweep on 2026-08-21 one repository came back non-additive (`+24/-1`) and the removed line turned out to be a stale action pin the template updates, not local customisation; it was then done as its own PR with the replaced line quoted in the body. That sweep used the short pattern above, so "the other twenty removed nothing" is only established for removals that pattern can see.

Two things the gate must not skip:

- **Honour declared exemptions by reading the key, not the file.** `intentional-drift:` lives in `.github/template.yaml`, and those manifests also mention managed files in prose — a comment reading *"byte-identical, drift-enforced checks.yml"* matches a grep for `checks.yml` and means the opposite. Use `yq '.["intentional-drift"]'` and test for the path.
- **Distrust an implausible classification rate.** If a dry run reports that most of the fleet has deliberately opted out of one shared file, the query is broken, not the fleet. Read one matched item in full before believing the aggregate.

### Dry-run manifest format

Emit a table — one row per repo, one column per step. Do not execute until the user approves the plan.

| Repo | Precondition | Action | Postcondition |
|------|--------------|--------|---------------|
| owner/repo-a | main clean, CI green | bump plugin.json 1.2.3 → 1.2.4, open PR | PR URL, auto-merge enabled |
| owner/repo-b | main clean, CI green | bump plugin.json 1.2.3 → 1.2.4, open PR | PR URL, auto-merge enabled |

Columns must be concrete — exact commands, exact file paths, exact version strings. A plan that says "update version" is not a plan; it's an intention.

### Approval prompt template

```
I'll now execute the above plan across N repos. Proceed? (reply "go" to execute, or
name specific repos to skip.)
```

Wait for "go" (or an equivalent affirmative). Silence is not approval.

## Pre-Flight Per-Repo Checks

Before touching each repo in the batch, check three things the dry-run manifest won't catch — they tend to surface as 30 silent failures across a fleet loop:

### 1. Default branch name

Not every repo uses `main`. Some legacy repos are on `master`; forks can be on anything.

```bash
DEFAULT_BRANCH=$(gh api "repos/$REPO" --jq '.default_branch')
```

Use `$DEFAULT_BRANCH` everywhere a script would otherwise hard-code `main`. Pushing to the wrong branch either silently creates a new branch or fails with a confusing rejection.

### 2. Archived repos

Archived repos reject most writes with a generic permission error. Dependabot/Renovate sometimes still open PRs on them (via the pre-archive config), and a batch loop that tries to merge them fails cryptically.

```bash
ARCHIVED=$(gh api "repos/$REPO" --jq '.archived')
if [[ "$ARCHIVED" == "true" ]]; then
  # Skip, or handle specially: unarchive → close PR → re-archive.
  continue
fi
```

Never enable auto-merge on archived repos — the auto-merge plumbing fails at set-up time with "archived" errors.

### 3. Contents API vs branch protection

`gh api -X PUT repos/.../contents/...` is the fastest path for tiny single-file edits across a fleet — but it returns HTTP 409 on any repo that requires PRs, a merge queue, or signed commits. If your batch mixes repos with and without branch protection, this path breaks mid-loop and leaves half the fleet updated.

**Safer default for batch file edits**: open a one-commit PR per repo even when the Contents API would work. Gives you a reviewable diff, matches any future signing/protection rule tightening, and keeps behavior consistent across the fleet.

### 4. Forks: "0 ahead" on the default branch does not mean "dead"

Fleet cleanups and advisory sweeps both reach the same question — is this fork
still needed, or can it go? The usual check compares the *default* branch:

```bash
gh api "repos/$UPSTREAM/compare/$DEFAULT...${OWNER}:$DEFAULT" --jq '.ahead_by'
```

`ahead_by: 0` plus no open upstream PRs reads as a pure mirror with nothing to
lose. It is not sufficient. One fork that reported `0 ahead / 1 behind` on
`master`, with issues disabled, no releases, no stars and no upstream PRs, held
**26 commits across 8 non-default branches** — `task/build-setup` (9),
`bugfix/sticky-header-scroll-flicker` (8), `task/simplify-tca` (4) and five more
at 1 each. Deleting it would have destroyed all of them.

Enumerate every branch before deleting or archiving a fork:

```bash
UPSTREAM=upstream-owner/repo; FORK=our-org/repo; DEFAULT=$(gh api "repos/$UPSTREAM" --jq .default_branch)
for b in $(gh api "repos/$FORK/branches" --paginate --jq '.[].name'); do
  n=$(gh api "repos/$UPSTREAM/compare/$DEFAULT...${FORK%%/*}:$b" --jq '.ahead_by' 2>/dev/null)
  [ "${n:-0}" -gt 0 ] && echo "$b ahead=$n"
done
```

Any non-zero result is unmerged local work: land it upstream or preserve it
before the repo goes. Note that `open_issues_count` includes PRs, so a fork with
issues disabled can still report `1` — resolve what it is rather than assuming.

When the goal was only to clear the fork's Dependabot alerts, prefer dismissing
them over deleting the repo. A fork's lockfile belongs to upstream; patching it
diverges the fork without removing exposure that a never-built fork does not
have.

```bash
gh api -X PATCH "repos/$FORK/dependabot/alerts/$N" \
  -f state=dismissed -f dismissed_reason=not_used \
  -f dismissed_comment="$COMMENT"   # 280 chars max, or HTTP 422
```

Say *why* in the comment — that the lockfile is upstream's, that upstream is
still on the vulnerable version, and that the fork is never built or deployed.
"not_used" alone tells the next reader nothing.

## Parallel PR Rebasing

For N PRs that need rebasing on their default branches, dispatch parallel subagents — one per PR — with failure isolation.

```bash
# 1. Enumerate open PRs needing rebase
gh pr list --state open --json number,headRefName,baseRefName,mergeStateStatus \
  --jq '.[] | select(.mergeStateStatus == "BEHIND" or .mergeStateStatus == "DIRTY")'
```

### Parallel-agent prompt skeleton

For each PR, spawn a subagent with this task (run them in one message for concurrency):

```
PR #<NUM> on <owner/repo>:
1. Checkout the PR branch in a fresh worktree
2. Rebase onto origin/<base-branch>
3. If conflicts: do NOT resolve speculatively — abort the rebase, report the files
4. If clean: force-push with --force-with-lease
5. Re-check PR status; report "rebased" or "conflicts: <files>"
```

### Failure isolation

One bad rebase must not block the rest. Structure the supervisor prompt so each PR reports independently. Collect results into a summary table:

| PR | Status | Note |
|----|--------|------|
| #101 | rebased | clean |
| #102 | conflicts | internal/server/handler.go |
| #103 | rebased | clean |

Then address conflicts one by one — never batch-resolve.

## Multi-Repo Release Orchestration

The canonical order is: **version-bump PR merged → tag pushed**, never the reverse. Tag-before-bump causes Release workflows to run against the wrong version and fail.

### Pre-flight validation (per repo)

Before touching any repo, validate:

- `plugin.json.version` is present (authoritative) and `composer.json` has **no** `version` field (Packagist derives the version from git tags); if `SKILL.md` frontmatter carries a `metadata.version`, it must match `plugin.json.version`
- For repos that also ship via npm: `package.json.version` is either the placeholder `0.0.0-source` (publish-time-rewritten by the Release workflow) **or** matches `plugin.json` (for coordinator-style packages, e.g. `@netresearch/agent-skill-coordinator`). Mixing the two within one repo is the bug pattern to look for.
- Current git tag on default branch is not already the target version
- CI on default branch is green
- No pending version-bump PR already open

For Netresearch skill repos, use the shipped `scripts/check-version-parity.sh` from `skill-repo-skill`:

```bash
# From the target repo root
skills/skill-repo/scripts/check-version-parity.sh            # parity only
skills/skill-repo/scripts/check-version-parity.sh v1.2.4     # also require tag parity
```

That script handles the Netresearch conventions (`plugin.json` has the authoritative version, `composer.json` must not have one, `SKILL.md` `metadata.version` in frontmatter matches `plugin.json`, and `package.json.version` is either `0.0.0-source` for git-installed skill packages or matches `plugin.json` for npm-published coordinator-style packages). Don't copy the snippet below inline — it was a sketch for illustration; the real script handles empty-arg mode, missing files, glob-empty iteration, and the quoted-or-unquoted frontmatter form. Call the shipped script.

```bash
# Illustrative only — for non-skill repos, adapt the shape but handle empties
PLUGIN_VERSION=$(jq -r '.version // empty' .claude-plugin/plugin.json 2>/dev/null)
[[ -z "$PLUGIN_VERSION" ]] && { echo "no plugin.json.version"; exit 1; }
# ...same shape, using jq // empty to avoid "null" strings, and quoting frontmatter regex
```

### Release sequence (per repo)

1. Open version-bump PR → wait for CI green and review
2. Merge version-bump PR (respects merge gate from `git-workflow` skill)
3. Pull default branch locally; verify the merged version is present
4. Create **signed** tag: `git tag -s vX.Y.Z -m "vX.Y.Z"`
5. Push tag: `git push origin vX.Y.Z`
6. Monitor the Release workflow to green
7. **Only after green** declare the repo released

### Supervisor halts on first failure

If any repo's Release workflow fails, **halt further releases**. Do not continue to the next repo. Produce a rollback plan (`gh release delete`, or version-bump-back PR) before the user asks. This prevents the 30-failed-plugin-releases pattern.

### Final report

After all releases complete, output a table:

| Repo | Old | New | Tag URL | Release Workflow |
|------|-----|-----|---------|------------------|
| owner/a | 1.2.3 | 1.2.4 | link | ✅ green |
| owner/b | 1.2.3 | 1.2.4 | link | ❌ failed — see link |

## Enumerating Target Repos

```bash
# All repos in an org with a given topic. --limit 100 caps the page;
# for larger orgs, raise or iterate with pagination.
gh repo list OWNER --topic claude-skill --limit 500 --json name,url,defaultBranchRef

# All repos matching a name pattern
gh repo list OWNER --limit 500 --json name,url | jq '.[] | select(.name | endswith("-skill"))'

# Local worktree discovery
find ~/projects -maxdepth 3 -name ".bare" -type d | sed 's|/.bare||'
```

### Never enumerate by content with `gh search code`

`gh search code` silently under-reports and returns `null` for `repository`
fields under `--json`. Two enumerations in one session came back wrong: a
secret referenced in **63** repos was reported as **1**, and a consumer set of
**51** came back as **39**. Acting on either number would have deleted an
org-level secret while dozens of callers still passed it.

Use the REST endpoint instead:

```bash
gh api --paginate "search/code?q=SEARCHTERM+org:OWNER&per_page=100" \
  --jq '.items[] | "\(.repository.name)|\(.path)"' | sort -u
```

**Always validate a content search against a known-positive baseline before
trusting a low or zero count.** Pick a string you already know appears in many
repos and confirm the search finds them:

```bash
# Sanity probe: this string is in every consumer, so a low count means the
# search is lying, not that the consumers are gone. Deliberately unpaginated —
# compare total_count against the page size to see whether results are capped.
gh api "search/code?q=%22KNOWN_STRING%22+org:OWNER&per_page=100" \
  --jq '"total=\(.total_count) on_this_page=\(.items|length)"'
```

`--paginate` is required for any enumeration you intend to act on, but it does
not remove the ceiling: the Search API stops at **1000 results** regardless of
paging. If `total_count` approaches that, the result set is truncated and no
amount of paging will complete it — narrow the query (per path, per topic, per
repo batch) or switch to structural enumeration.

A zero or suspiciously small result is a **search failure until proven
otherwise** — the index also lags recent pushes, so a repo you changed minutes
ago may not appear. Where correctness matters (deleting a secret, removing a
declaration other repos depend on), enumerate structurally instead: probe each
repo for the marker file with `gh api repos/OWNER/REPO/contents/<path>`, which
reads the live tree rather than an index.

### Probing paths answers a narrower question than it looks

The `contents/<path>` probe above is right about the index, but it only ever
answers *is the file at this path*. A sweep built from a list of plausible paths
reports the same "absent" for a file that does not exist and for one that sits
somewhere the list does not name — and the resulting count reads like a
measurement.

Measured across 25 extensions: a sweep of five plausible `php-cs-fixer` config
paths reported 11 repositories with no config. Ten of them had one, at a sixth
path that was the single most common layout in that fleet. The real figure for
the defect being tracked was 13 repositories, not 3, and the number had already
reached an issue and a colleague. Worse, the fix under review had been built
from the same guessed list, so it repaired the flag and left ten repositories
exactly as broken as before.

A candidate list is assembled from the layouts you already know. The layouts you
do not know are the reason the sweep exists. So list the tree and classify what
comes back:

```bash
# Every matching path, whatever the layout — one request per repo
gh api "repos/OWNER/REPO/git/trees/BRANCH?recursive=1" \
  --jq '[.tree[] | select(.path|test("php-cs-fixer";"i"))
        | select(.path|test("^vendor/|^\\.Build/")|not) | .path] | join(" ")'
```

Where probing is genuinely the only option, do not name the empty bucket
"absent". Call it "none of the paths checked" and print which ones were checked,
so the next reader can see the hole instead of inheriting the number.

### Reading one directory's files across the org, 20 repos per request

When the question is about file *content* in a known directory (which
workflows call action X), one `contents` call per file costs thousands of
requests across a fleet. GraphQL reads a directory's tree with every blob's
text, and one query can carry 20 repositories as aliases:

```graphql
query {
  r0: repository(owner: "OWNER", name: "REPO_A") {
    object(expression: "HEAD:.github/workflows") {
      ... on Tree { entries { name object { ... on Blob { text isTruncated } } } }
    }
  }
  r1: repository(owner: "OWNER", name: "REPO_B") { ... }
}
```

`HEAD` is the default branch. A repository without the directory returns
`object: null`; an oversized blob returns `isTruncated: true`, so count those
separately rather than as "no match". Count failed requests too: a sweep that
drops a failed batch reports its 20 repositories as clean.

**Measured:** 245 active repositories in 13 GraphQL requests plus one
`gh repo list`, 0 failed batches. Org code
search had returned 0 for the same string, and so had its positive control
against a repository known to contain it.

## Cache-Safety for Batch Operations

When iterating across many local worktrees, it's easy to edit an installed skill/plugin cache by mistake. Before any write in a multi-repo loop:

```bash
for repo in "${REPOS[@]}"; do
  # `cd` can fail (missing dir, permissions) — bail the iteration so the
  # work below doesn't run in the previous repo's cwd, which would silently
  # corrupt that repo.
  if ! cd "$repo"; then
    echo "SKIP: cannot cd to $repo" >&2
    continue
  fi

  pwd_real=$(realpath .)
  case "$pwd_real" in
    */.claude/skills/*|*/.claude/skills|*/.claude/plugins/cache/*|*/.claude/plugins/cache|*/.bare/*|*/.bare)
      echo "REFUSING to edit cache path: $pwd_real" >&2
      cd - >/dev/null || exit 1
      continue
      ;;
  esac

  # ... actual work ...

  cd - >/dev/null || exit 1   # pop back before the next iteration
done
```

`cd -` restores the original working directory between iterations so a failure partway through doesn't leave the shell in the wrong repo. `continue` (not `exit`) on a single-repo failure keeps the rest of the batch moving — a single bad repo should not abort the run; the summary table at the end reports it.

This is the same worktree-authority rule as `git-workflow`, enforced inside the batch loop.

## Template-Drift Resolution Pattern

When a consumer repo's template-drift check fails and the fix is "remove a thing that doesn't apply here" (ecosystem, workflow, config entry), the drift is usually a **template bug**, not a consumer bug — the template was written too broad for the class of repo it's applied to.

**Naive fix:** patch only the consumer. The drift check stays red forever because the template still declares the thing the consumer is missing. Adding an `intentional-drift:` exception works but accumulates per-repo carve-outs that future template authors don't see.

**Correct fix:** patch the template AND the consumer in the same sweep. The template PR is the forward fix (next consumer inherits the correction); the consumer PR clears the current red.

```
1. Identify all consumers of the affected template path
   # Use the REST endpoint, NOT `gh search code` — see "Enumerating repos" below.
   gh api --paginate "search/code?q=%22templates/<template-name>%22+org:netresearch&per_page=100" \
     --jq '.items[] | "\(.repository.name)|\(.path)"' | sort -u

2. Open the template-side PR first
   - Remove the bad entry / tighten the template
   - Reference the first observed consumer failure (URL of the red run)
   - Flag that consumers will drift until synced; list them in the PR body

3. Open the consumer-side PR(s) matching the template change
   - Cross-reference: "Matches netresearch/.github#NN"
   - Merge both in the same session so the drift window closes quickly

4. Enable auto-merge on both. The consumer waits on its drift check,
   which starts passing the moment the template PR lands.
```

**Rule of thumb for template scope:** the template should carry only what EVERY consumer of that class actually needs. A `go-lib` template with an `npm` dependabot entry is wrong because most Go libraries don't ship `package.json`. A `go-app` template with an `npm` entry is defensible — some go-apps DO ship frontend assets — but the class is loose enough that per-consumer overrides become common. When you see carve-outs accumulating in `intentional-drift:` lists, that's a signal the template is too broad for its consumer base and the classes should be split (e.g. `go-app` vs `go-app-headless`).

### Applying a template to one repository by hand

`netresearch/.github/scripts/sync-template.sh <template> <owner/repo>` clones
the target, copies `templates/<template>/.github/`, commits with a fixed
message and opens a **ready** PR. Where the commit must carry the operator's
disclosure trailers or the PR must start as a draft, make the same copy in
your own worktree:

```bash
# From a local netresearch/.github clone, fetched first
git -C <dotgithub>/.bare archive origin/main "templates/<template>/.github" \
  | tar -x -C "$TMP"
cp -a "$TMP/templates/<template>/.github/." <worktree>/.github/
git -C <worktree> status --porcelain     # add exactly these paths, never -A
```

Name the template commit in the commit message
(`git -C <dotgithub>/.bare rev-parse --short origin/main`), so the drift
baseline is traceable. The script never overwrites an existing
`.github/template.yaml`; when re-syncing by hand, restore it after the copy.

**What the drift check compares.** `scripts/drift_compare.py` in
netresearch/.github (used by `check-drift.sh` and the reusable drift job)
compares YAML files as parsed documents: a difference only in comments, key
order or whitespace is reported as cosmetic and does not fail. Non-YAML files
are compared byte for byte, and a YAML file that does not parse counts as
drift. A workflow whose only difference is the full commit SHA a `uses:` is
pinned to is reported as a pin notice, not drift, so Renovate moving the
template and a consumer on different days does not redden either; a consumer
with `strict-pins: true` in `.github/template.yaml` makes those differences
fail. A comment in a consumer's `template.yaml` that calls the files
"byte-identical" predates this and does not describe the check.

See [dependency-management.md](./dependency-management.md) for which Dependabot ecosystems hard-fail when their manifest is missing (the common source of template drift on Go repos).

## Keeping a private copy of a public repository in sync

Some consumers accept only a private repository — the Claude organization marketplace is one — so a public repository gets a private twin. GitHub has no push mirroring, and a copy maintained by carrying changes over in pull requests drifts: `netresearch/claude-code-marketplace-P` had diverged in workflows, site code and the lockfile before its sync was automated. Make the copy a byte-identical mirror of the source's default branch and let the source push it.

- **Push from the source, with a write deploy key of the copy.** Generate an ed25519 key, add the public half to the copy (`POST /repos/<copy>/keys` with `read_only=false`) and store the private half as a secret in a source **environment** whose deployment branch policy allows only `main`. A deploy key is scoped to that one repository, and unlike `GITHUB_TOKEN` it can push changes to `.github/workflows/`. A scheduled workflow in the copy pushing with its own `GITHUB_TOKEN` looks simpler and fails on the first upstream workflow change.
- **Push `origin/main` as fetched at run time, not `GITHUB_SHA`**, with `--force`. `GITHUB_SHA` is fixed per run, so re-running an old run would roll the copy back. Checkout needs `fetch-depth: 0` and `persist-credentials: false`; pin the host key (`github.com ssh-ed25519 …` from `GET /meta`) instead of trusting on first use.
- **Exempt the copy from this skill's branch-protection baseline.** The baseline sets `allow_force_pushes: false`, which rejects every sync. The copy is not where review happens — nobody merges there — so leave its `main` unprotected, or, where a ruleset must stay, add the deploy key as a bypass actor (`"actor_type": "DeployKey"`, `bypass_mode: always`); with classic protection set `allow_force_pushes` to `true`. Branch protection and rulesets on a private repository need a paid plan anyway, so on a free organization the question does not arise.
- **Guard the job with `if: github.repository == '<source>'`** and put it in a `concurrency` group without `cancel-in-progress`.
- **Disable Actions in the copy entirely** (`PUT /repos/<copy>/actions/permissions -F enabled=false`). It receives every workflow file of the source; per-workflow `gh workflow disable` misses each file added later.
- **Keep bots off the copy.** When the Renovate app is installed on all org repositories, narrowing the installation would change it org-wide; instead add a rule to the source's `renovate.json`, which reaches the copy with the next push:

  ```json
  "packageRules": [
    { "matchRepositories": ["<org>/<copy>"], "enabled": false }
  ]
  ```

  `matchRepositories` matches the repository Renovate is processing, not a dependency's source (`lib/util/package-rules/repositories.ts` compares it against the processed `repository`); an AI reviewer claiming otherwise is wrong. Close the bot pull requests already open in the copy, and turn off Dependabot security updates there (`DELETE /repos/<copy>/automated-security-fixes`).
- **The first run replaces the copy's own history.** Move anything that exists only in the copy (a README section, a note) into the source first, and say in the pull request that the copy's own commits will be orphaned.

## Common Anti-Patterns

| Anti-pattern | Consequence | Fix |
|--------------|-------------|-----|
| Tag pushed before version-bump PR merged | Release workflow runs on old version | Enforce order in supervisor prompt |
| Sequential (not parallel) processing of independent repos | Hours wasted; user interrupts | Dispatch as parallel subagents |
| "Should work now, try it" without per-repo verification | One failure poisons the batch | Collect results in a table, verify each |
| Shared branch name across repos (e.g. `bump-version`) | PR searches return wrong repo | Include repo name in branch: `bump-<repo>-v1.2.4` |
| Squash-merging version-bump PRs when repo uses atomic commits | Lost signatures, CI confusion | Respect repo merge policy per `git-workflow` |



--- FILE: skills/github-project/references/no-editorializing.md ---

<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->
<!-- SPDX-FileCopyrightText: Netresearch DTT GmbH -->

# No editorializing — inform, don't sell (tone, not wordlist)

Canonical copy: [no-editorializing.md](https://github.com/netresearch/git-workflow-skill/blob/main/skills/git-workflow/references/no-editorializing.md). See there.



--- FILE: skills/github-project/references/org-security-settings.md ---

<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->
<!-- SPDX-FileCopyrightText: Netresearch DTT GmbH -->

# Organization Security Settings Reference

Org-level GitHub security settings for Actions permissions, SHA pinning, and action allow-lists.

## SHA Pinning Requirement (`sha_pinning_required`)

Forces all GitHub Actions in the organization to use full SHA references instead of tags or branches.

### Key behavior

- **Enforced:** All `uses:` directives must reference actions by full commit SHA (e.g., `actions/checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd`)
- **Exempt:** Reusable workflows called with `@main` or `@vX.Y.Z` are exempt -- they can still use branch/tag refs
- **Scope:** Applies to all repositories in the organization

### Enable via API

```bash
gh api orgs/ORG/actions/permissions -X PUT -F sha_pinning_required=true
```

### Verify current setting

```bash
gh api orgs/ORG/actions/permissions --jq '.sha_pinning_required'
```

## `pin-github-action` Tool

CLI tool to automatically convert tag-based action references to SHA-pinned references.

### Install and run

```bash
# Pin all workflows in a repo
npx pin-github-action@latest .github/workflows/*.yml

# Exclude internal org refs (keeps reusable workflow @main/@tag refs)
npx pin-github-action@latest .github/workflows/*.yml --allow "myorg/*"

# Continue on resolution errors (useful for batch operations)
npx pin-github-action@latest .github/workflows/*.yml --continue-on-error

# Use authenticated requests for higher rate limits
GITHUB_TOKEN=$(gh auth token) npx pin-github-action@latest .github/workflows/*.yml
```

### Batch script pattern for an entire org

```bash
#!/usr/bin/env bash
set -euo pipefail

ORG="myorg"
REPOS=$(gh repo list "$ORG" --no-archived --json nameWithOwner -q '.[].nameWithOwner')

for REPO in $REPOS; do
    echo "Processing $REPO..."
    TMPDIR=$(mktemp -d)
    if ! gh repo clone "$REPO" "$TMPDIR" -- --depth 1; then
        echo "Error: Failed to clone $REPO. Skipping." >&2
        rm -rf "$TMPDIR"
        continue
    fi

    WORKFLOWS=("$TMPDIR/.github/workflows/"*.yml)
    [[ -e "${WORKFLOWS[0]}" ]] || { rm -rf "$TMPDIR"; continue; }

    GITHUB_TOKEN=$(gh auth token) npx pin-github-action@latest "${WORKFLOWS[@]}" \
        --allow "$ORG/*" --continue-on-error

    cd "$TMPDIR"
    if ! git diff --quiet .github/workflows/; then
        git checkout -b chore/pin-actions
        git add .github/workflows/
        git commit -S --signoff -m "fix: SHA-pin GitHub Actions"
        git push -u origin chore/pin-actions
        gh pr create --title "fix: SHA-pin GitHub Actions" \
            --body "Pin all third-party GitHub Actions to full SHA refs for supply-chain security."
    fi
    cd -
    rm -rf "$TMPDIR"
done
```

## Allowed Actions Policy (`allowed_actions`)

Controls which actions can be used across the organization.

| Value | Effect |
|-------|--------|
| `all` | Any action can be used (no restrictions) |
| `local_only` | Only actions defined in the same repository |
| `selected` | Only actions matching the allow-list |

### Configure via API

```bash
# Set to selected (most secure)
gh api orgs/ORG/actions/permissions -X PUT \
    -f allowed_actions=selected

# View current policy
gh api orgs/ORG/actions/permissions --jq '.allowed_actions'
```

## Action Allow-Lists

When `allowed_actions` is `selected`, configure which actions are permitted.

### View current allow-list

```bash
gh api orgs/ORG/actions/permissions/selected-actions --jq '{
    github_owned_actions_allowed: .github_owned_actions_allowed,
    verified_allowed: .verified_allowed,
    patterns_allowed: .patterns_allowed
}'
```

### Update allow-list

```bash
gh api orgs/ORG/actions/permissions/selected-actions -X PUT --input - <<'EOF'
{
    "github_owned_actions_allowed": true,
    "verified_allowed": true,
    "patterns_allowed": [
        "slsa-framework/*",
        "sigstore/*",
        "reviewdog/*",
        "myorg/*"
    ]
}
EOF
```

### Fields

| Field | Description |
|-------|-------------|
| `github_owned_actions_allowed` | Allow all `actions/*` and `github/*` actions |
| `verified_allowed` | Allow actions from verified marketplace creators |
| `patterns_allowed` | List of glob patterns for additional allowed actions |

> **Important:** Composite actions' internal sub-actions must also be in the allow-list. See [`security-config.md`](./security-config.md#composite-action-sub-action-allow-list-gotcha) for the Composite Action Sub-Action Allow-List Gotcha.

## Organization secrets with `visibility: selected`

An organization secret whose visibility is `selected` exists only for the repositories on its list. In any other repository `${{ secrets.NAME }}` resolves to an empty string — no error, no warning. A caller that passes it on to a reusable workflow hands over `""`, and a publish step that needs it either fails deep inside the reusable or skips its work while the run reports success.

`gh secret list` without `--org` lists repository secrets only, so an empty listing in the repository proves nothing. Check from the repository side (the secret's name must appear; both list endpoints are paginated, so fetch every page):

```bash
gh api --paginate "repos/ORG/REPO/actions/organization-secrets?per_page=100" --jq '.secrets[].name'
```

And from the organization side, with an org admin token:

```bash
gh api orgs/ORG/actions/secrets/NAME --jq .visibility                                                    # selected?
gh api --paginate "orgs/ORG/actions/secrets/NAME/repositories?per_page=100" --jq '.repositories[].name'  # the list
gh api -X PUT orgs/ORG/actions/secrets/NAME/repositories/REPO_ID                                         # grant one repo
```

`REPO_ID` is the numeric ID (`gh api repos/ORG/REPO --jq .id`). Check this whenever a new repository starts using a shared publishing secret, before its first release.

## Push protection vs. secret-shaped test fixtures

With push protection enabled, a complete secret-shaped literal in any committed file rejects the whole push (`GH013 … Push cannot contain secrets`) — even an obvious fixture in a redaction test. The scanner matches one contiguous literal, so build fixtures by concatenation instead: `'sk_live_' . str_repeat('9', 24)` passes, while the same value written out as one contiguous literal is blocked. (This document cannot even *show* the blocked form — writing it here rejected the push of this very section.) Never "fix" this by weakening push protection or using a real-looking key with one character changed (still matches some patterns) — concatenate.



--- FILE: skills/github-project/references/pages-and-collector-workflows.md ---

<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->
<!-- SPDX-FileCopyrightText: Netresearch DTT GmbH -->

# Publishing a generated site to GitHub Pages (and org-data collectors)

Lessons from shipping a nightly workflow that inventories an organization's repos and publishes a generated dashboard to GitHub Pages. Two classes of failure that a `200 OK` and a green build both hide.

## Hidden rate limits break the workflow and the deploy

A workflow that walks an org (per-repo file probes + issue/PR counts) exhausts limits that are separate from the familiar 5,000/hour user quota:

- **`GITHUB_TOKEN` installation limit — ~1,000 requests/hour, scoped to the repository the workflow runs in** (where the token is issued — *not* a separate quota per target repo you query). This is the token Actions injects, *distinct* from a PAT's 5,000/hr user limit. A collector that spends ~15 `GET /repos/{repo}/contents/{path}` probes per repo across ~100 target repos burns ~1,500 calls against that single budget and exhausts it — after which the **`deploy-pages` step 403s** ("API rate limit exceeded for installation") even though it makes one call. The build job starves the deploy job because they share the one installation quota.
- **Search API primary limit — 30 requests/minute (authenticated).** `GET /search/issues` for open-issue/PR/stale counts hits this within the first minute across a large org, and rate-limited responses come back as **403 that looks like "no data"** — counts silently become `null`/0 and the dashboard shows wrong numbers with a green build.

### Fixes

- **File presence: one `git/trees` call per repo, not N `contents` probes.** `GET /repos/{owner}/{repo}/git/trees/{ref}?recursive=1` returns the whole file listing in one request; test for `README`/`CODEOWNERS`/`SECURITY`/etc. against that set. ~3 calls/repo instead of ~15.
- **Counts: GraphQL, not the Search API.** One GraphQL sweep over `organization.repositories` returning `issues(states:OPEN){totalCount}` and `pullRequests(states:OPEN){totalCount}` is accurate for every repo and spends a handful of the 5,000-point/hour GraphQL budget. For stale-PR counts use `pullRequests(states:OPEN, first:100, orderBy:{field:UPDATED_AT, direction:ASC}){nodes{updatedAt}}` — `orderBy` takes an `IssueOrder` **object** (`{field,direction}`), not a bare enum; ASC lets you stop once past the cutoff, and you must paginate (or cap and flag) for repos with >100 open PRs or the count is silently low.
- **Retry only what's transient.** Retry 5xx and secondary-rate-limit responses (they carry `Retry-After`); let the primary Search limit fast-degrade to `null` rather than blocking. One flaky response should not abort a run whose output is written only at the end.
- **Budget the run.** Keep a full collection under ~1,000 REST calls so the shared installation token survives the `deploy-pages` job in the same workflow.

## Not every 403 is a rate limit — classify before reacting

A collector meets three different 403s, and they need opposite responses. Read the headers rather than the status code:

| 403 | Signal | Response |
|---|---|---|
| Primary rate limit | `x-ratelimit-remaining: 0` | Transient. Back off or degrade. |
| Secondary rate limit | `retry-after` present, *or* only the body says `"secondary rate limit"` | Transient. Honour `retry-after`. |
| Permission | Neither of the above; body names the cause (`Resource not accessible by integration`) | **Not** transient. Retrying burns the run and hides the cause. |

The secondary limit is the trap: it does **not** zero `x-ratelimit-remaining`, so `remaining == 0` alone misfiles it as a permission error and aborts a run that should have waited. And `retry-after` is sufficient but not necessary — [the docs](https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api) only say it *may* be present — so the body is the last resort:

```python
def is_rate_limited(response):
    if response.headers.get("X-RateLimit-Remaining") == "0":
        return True
    if "Retry-After" in response.headers:
        return True
    return "secondary rate limit" in response.text.lower()
```

**Diagnostic: a sibling endpoint that still works disproves a rate limit in one step.** A budget is token-wide, so it cannot spare one endpoint and starve another. When `/stargazers` 403s on all 278 repos but `/forks` never fails once, on the same token in the same run, the cause is per-endpoint permission — no header reading required.

### Stargazers and subscribers are admin/collaborator-only (since 2026-06-30)

[GitHub restricted](https://github.blog/changelog/2026-06-30-upcoming-access-restrictions-to-public-api-endpoints-and-ui-views/) `GET /repos/{o}/{r}/stargazers` and `GET /repos/{o}/{r}/subscribers` to each repo's admins and collaborators — they were being scraped to harvest user data. `GET /users/{u}/subscriptions` is deprecated and returns empty. The UI views `/stargazers`, `/stargazers/you_know` and `/watchers` are restricted too; `/network/dependents` is not.

- **The Actions `GITHUB_TOKEN` is neither an admin nor a collaborator**, so it 403s on *every* repo — including the one the workflow runs in, with `Metadata: read` granted. `/forks` is unaffected.
- **Fix: a fine-grained PAT** whose owner is a collaborator. Both endpoints need only [Metadata: read](https://docs.github.com/en/rest/authentication/permissions-required-for-fine-grained-personal-access-tokens), which every fine-grained PAT carries by default — no extra permission to tick, and nothing under "Organization permissions".
- **Scope the PAT to *All repositories*, not a hand-picked list** (org policy permitting). A collector walks the org from `GET /orgs/{org}/repos`, so a select-repository PAT keeps discovering repos it may not read: every repo created after the PAT was minted degrades to a permission 403 and, in a collector that swallows per-item errors, disappears from the output with no signal. The failure grows silently as the org does.
- **The status code differs by token type:** an Actions token gets `403`; a user PAT gets **`404`** on repos where it is not a collaborator (GitHub hides existence rather than admitting the block). Don't read that 404 as "repo gone".
- A PAT expires. Make the run fail loudly and name the secret, or the collector silently reverts to reporting no news.

## A systemic error must abort; only per-item errors may degrade

"Retry only what's transient" (above) has a corollary: a collector that catches every error per repo, keeps the last known state and exits `0` reports **"0 new"** — indistinguishable from a genuine quiet period. A star-notification collector hid a total outage this way for 9+ days across ~900 runs; nobody was watching a green check that said `Found: 0 star(s)`.

- **Auth failures (401/403-permission) are systemic, never per-item.** Raise a distinct exception that the per-item handler cannot catch, so the job goes red with an actionable annotation:
  ```python
  class AuthError(Exception): ...          # not a RequestException
  ...
  except requests.exceptions.RequestException:   # per-repo, may degrade
      return None
  ```
- **Read the token with a default, and check it.** `os.environ["TOKEN"]` raises `KeyError` before any handler is installed; worse, Actions sets a *missing* secret to the **empty string**, so the variable exists and the failure is a silent 401. `os.environ.get("TOKEN", "")` plus an explicit emptiness check catches both.
- **A green run proves nothing on its own — assert on the failure count.** `Found: 0 star(s)` with 0 failed fetches is real; with 556 failed fetches it is an outage.

### Cross-run state: `dawidd6/action-download-artifact` matches any branch

Collectors persist state between runs by uploading an artifact and pulling it back with `dawidd6/action-download-artifact`. Its `branch` input has **no default**, so it takes the latest successful run of the workflow on *any* branch. A `workflow_dispatch` test on a feature branch therefore loads (and its upload then becomes) production state. Convenient for testing a fix against real data; set `branch:` explicitly if you need isolation.

## A Pages "200 OK" is not proof the page rendered

For a **JS-rendered** page (data embedded in the HTML, DOM built client-side), `curl` returning `200` with the correct `<title>` proves nothing — the body can be blank. Real incident: a `String.prototype.replace(placeholder, json)` bug (replaces only the first of two identical tokens) shipped `window.{…json…} = __PLACEHOLDER__;` — a syntax error, blank dashboard, green build, 200 response.

- **Verify by rendering, not by status.** Render headless and assert DOM population (a KPI value, a table row), e.g. `google-chrome --headless --dump-dom --virtual-time-budget=5000 <url>` then grep the post-JS DOM; or drive one interaction with Playwright and assert zero console errors.
- **Don't read deploy success from a Pages endpoint 404.** There is no `GET /repos/{o}/{r}/pages/deployments` list endpoint (it 404s); list deployments via `GET /repos/{o}/{r}/deployments`, or just trust the `deploy` job's own conclusion.

## Verify a workflow edit actually landed before claiming it

A silent editor failure (edit reported an error, never retried) left GitHub Actions pinned to old `@v4`/`@v3` majors while the summary claimed "SHA-pinned." The **CI annotation** (`Node.js 20 is deprecated…`) exposed it — the pass/fail status did not.

- After editing action versions/pins, read the run's **annotations** and the committed workflow file — do not claim "pinned/updated" from a green check alone. See the "CI Annotations" section in `references/security-config.md`.



--- FILE: skills/github-project/references/pr-commit-cleanup.md ---

<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->
<!-- SPDX-FileCopyrightText: Netresearch DTT GmbH -->

# PR Shows Too Many Commits (Stale Merge Base on Forks)

When a fork's `main` is behind upstream and you create a PR after syncing, GitHub may cache the old merge base and show too many commits (e.g., 38 commits when only 1 is new). The `update-branch` API returns "There are no new commits on the base branch" and force-pushing says "Everything up-to-date" since the SHA hasn't changed.

## Steps to Reproduce

1. Fork is behind upstream by N commits
2. Create feature branch from upstream main
3. Push fork main to catch up
4. PR still shows N+1 commits instead of 1

## Fix

Close and reopen the PR to force GitHub to recalculate the merge base:

```bash
gh pr close NUMBER --repo OWNER/REPO && sleep 2 && gh pr reopen NUMBER --repo OWNER/REPO
```

This forces GitHub to re-evaluate the common ancestor between your branch and the target branch.

## Why This Happens

GitHub computes the merge base (common ancestor) when the PR is created and caches it. If the fork's default branch is later updated (synced with upstream), the cached merge base is not recalculated automatically. The close/reopen cycle invalidates the cache and triggers fresh merge-base computation.

## Alternative Approaches

If close/reopen doesn't work:

1. **Create a new PR:** Push the same branch and create a fresh PR
2. **Rebase onto upstream:** `git rebase upstream/main && git push --force-with-lease`
3. **Update fork first:** Sync fork's main before creating the feature branch

## Never reset a PR's head branch to its base commit

Force-updating an open PR's head ref so it momentarily points at the base branch's commit (zero diff vs. base) causes GitHub to **auto-close the PR**. Reopening then fails ("Could not open the pull request") and you must open a fresh PR.

This bites when replacing a PR's commits (e.g. to re-sign unsigned ones): patching the branch ref back to base before re-committing produces the zero-diff state. Instead, build the replacement commits on top of base **locally** and force-push in one step, so the branch always has ≥1 commit ahead of base:

```bash
git reset --soft origin/main   # keep the working tree; do NOT push this state
git commit -s -m "…"           # rebuild the commit(s)
git push --force-with-lease    # branch is never momentarily zero-diff on the remote
```

If a PR does get auto-closed this way, just open a new PR from the (now-correct) branch rather than fighting reopen.



--- FILE: skills/github-project/references/release-labeling.md ---

<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->
<!-- SPDX-FileCopyrightText: Netresearch DTT GmbH -->

# Release Labeling Reference

**Purpose:** Automatically track which PRs and issues shipped in each release using labels.

## Overview

When a release is published, the release-labeler workflow:
1. Creates a discussion announcement in the Announcements category
2. Creates a label `released:vX.Y.Z`
3. Finds all PRs merged since the previous release
4. Labels those PRs and their linked issues
5. Adds comments linking to the release

## Release Announcements

The `announce-release` job automatically creates a discussion in the repository's **Discussions > Announcements** category whenever a release is published.

### How it works

- **Dynamic category resolution:** The Announcements category ID is resolved at runtime via a GraphQL query by name, making the workflow portable across any repository with Discussions enabled.
- **Duplicate detection:** Before creating a discussion, the job checks the first 100 existing discussions in the Announcements category for a matching title (the release tag). If one already exists, creation is skipped.
- **Safe body construction:** The discussion body is built using `printf` to a temporary file and passed to the GraphQL mutation via `-F body=@file`. This avoids shell expansion issues with special characters in release notes (backticks, quotes, dollar signs, etc.).
- **Conditional execution:** The creation step only runs when `steps.category.outputs.found == 'true'`. If the repository has no Announcements category, a warning annotation is emitted and the job exits cleanly.
- **Permissions:** Requires `discussions: write` at the job level. The top-level workflow permissions remain minimal (`contents: read` only).

### Setup

1. **Enable Discussions** on the repository: Settings > General > Features > Discussions
2. Ensure an **Announcements** category exists (GitHub creates this by default when Discussions is enabled)
3. The workflow template already includes the `announce-release` job -- no additional configuration needed

## Benefits

| Benefit | Description |
|---------|-------------|
| **Traceability** | Know exactly which release contains a fix or feature |
| **User communication** | Issue reporters see when their request shipped |
| **Release notes** | Easy to generate changelogs from labeled PRs |
| **Audit trail** | Historical record of what shipped when |

## Label Format

```
released:vX.Y.Z
```

- **Prefix:** `released:` (consistent, searchable)
- **Version:** Full semver tag (e.g., `v1.2.3`, `v13.2.0`)
- **Color:** Green (`#0e8a16`) indicating shipped/done

## Setup

### 1. Add the workflow

Copy `assets/release-labeler.yml.template` to `.github/workflows/release-labeler.yml`:

```bash
curl -o .github/workflows/release-labeler.yml \
  https://raw.githubusercontent.com/netresearch/github-project-skill/main/skills/github-project/assets/release-labeler.yml.template
```

### 2. Enable Discussions (for announcements)

Go to Settings > General > Features and enable **Discussions**. Ensure an **Announcements** category exists (created by default).

### 3. Ensure permissions

The workflow needs:
- `issues: write` - To label issues and add comments
- `pull-requests: write` - To label PRs and add comments
- `contents: read` - To compare releases
- `discussions: write` - To create announcement discussions

### 4. Link issues to PRs

For automatic issue labeling, PRs must reference issues using:
- `Fixes #123`
- `Closes #123`
- `Resolves #123`

GitHub automatically creates the linking when these keywords are used.

## How It Works

```
┌─────────────────┐
│ Release v1.2.0  │
│   published     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Get previous    │
│ release (v1.1.0)│
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Find commits    │
│ v1.1.0...v1.2.0 │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Find PRs for    │
│ those commits   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐     ┌─────────────────┐
│ Label PRs with  │────▶│ Find linked     │
│ released:v1.2.0 │     │ issues          │
└─────────────────┘     └────────┬────────┘
                                 │
                                 ▼
                        ┌─────────────────┐
                        │ Label issues    │
                        │ released:v1.2.0 │
                        └─────────────────┘
```

## Querying Releases

### Find all items in a release

```bash
gh issue list --repo OWNER/REPO --label "released:v1.2.0" --state all
gh pr list --repo OWNER/REPO --label "released:v1.2.0" --state all
```

### GitHub web search

```
https://github.com/OWNER/REPO/issues?q=label:released:v1.2.0
```

### Find which release contains an issue

```bash
gh issue view 123 --json labels --jq '.labels[].name | select(startswith("released:"))'
```

## Manual Labeling

If you need to manually label items for a release:

```bash
# Create label
gh label create "released:v1.2.0" --color 0e8a16 --description "Released in v1.2.0"

# Label PRs
gh pr edit 100 101 102 --add-label "released:v1.2.0"

# Label issues
gh issue edit 50 51 --add-label "released:v1.2.0"

# Add comments
gh issue comment 50 --body "Fixed in [v1.2.0](https://github.com/OWNER/REPO/releases/tag/v1.2.0)"
```

## Integration with Other Tools

### Changelog generation

Use labeled PRs to generate changelogs:

```bash
gh pr list --repo OWNER/REPO --label "released:v1.2.0" --state merged \
  --json number,title,labels \
  --jq '.[] | "- \(.title) (#\(.number))"'
```

### Release notes automation

Reference labels in release body:

```markdown
## What's Changed

See all changes: [released:v1.2.0](https://github.com/OWNER/REPO/issues?q=label:released:v1.2.0)
```

## Troubleshooting

### PRs not being labeled

1. **Check tag format** - Must be semver (e.g., `v1.2.0`)
2. **Check previous release** - Workflow compares between releases
3. **Check permissions** - Workflow needs `pull-requests: write`

### Issues not being labeled

1. **Check PR linking** - Issues must be linked with `Fixes #123`
2. **Check issue state** - Only closed issues are labeled
3. **Check permissions** - Workflow needs `issues: write`

### First release

For the first release (no previous release to compare), the workflow labels recently merged PRs as a fallback.

## Examples

### Real-world usage

- [netresearch/ofelia](https://github.com/netresearch/ofelia/issues?q=label%3Areleased%3Av0.18.0)
- [netresearch/t3x-rte_ckeditor_image](https://github.com/netresearch/t3x-rte_ckeditor_image/issues?q=label%3Areleased%3Av13.2.0)



--- FILE: skills/github-project/references/repo-bootstrap.md ---

<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->
<!-- SPDX-FileCopyrightText: Netresearch DTT GmbH -->

# Repository Bootstrap — Required First Step After `gh repo create`

After creating any new Netresearch repository — `gh repo create`, push your initial commit, **then before opening the first PR** — you MUST apply branch protection. (The default branch ref must exist; the script exits 4 on empty repos.) Without this, the unresolved-threads workflow rule is unenforceable — operator discipline alone has demonstrably failed.

**Concrete incident:** [netresearch/snipe-it-docker-compose-stack#17](https://github.com/netresearch/snipe-it-docker-compose-stack/pull/17). The repo was created mid-session, branch protection was never applied, and three of the next eight merged PRs shipped with unresolved bot-reviewer threads — including a HIGH-severity token leak that both Copilot and gemini-code-assist had flagged. The structural enforcement (`required_conversation_resolution: true`) would have blocked those merges. The skill had the docs; nothing prompted the apply.

## Creating the repo from a bare-repo worktree

`gh repo create OWNER/REPO --public --source . --remote origin --push` run inside a worktree of a bare repository (`.bare/` + `main/` layout) fails with `current directory is not a git repository. Run 'git init' to initialize it` (exit 1) and does **not** create the repository (observed with gh on 2026-09-14). Create it without `--source`, then wire the remote by hand:

```bash
gh repo create OWNER/REPO --public --description "..."
git -C <worktree> remote add origin git@github.com:OWNER/REPO.git
git -C <worktree> config remote.origin.fetch '+refs/heads/*:refs/remotes/origin/*'
git -C <worktree> push -u origin main
```

## Bootstrap flow

```bash
# 1. Immediately after `gh repo create` and the first push:
bash <skill-root>/skills/github-project/scripts/init-branch-protection.sh OWNER/REPO
#    Applies the baseline:
#      required_conversation_resolution: true   (load-bearing)
#      required_approving_review_count:  1
#      allow_force_pushes:               false
#      allow_deletions:                  false
#      required_linear_history:          false   (needed for merge-commit
#                                                 signing strategy)
#    Required status checks are intentionally NOT set yet — a brand-new repo
#    has no CI history to discover context names from.
#
#    Single maintainer without pr-quality.yml? Use --solo instead: same
#    baseline with required_approving_review_count 0, because an author
#    cannot approve their own PR (see auto-merge-guide.md, "Choose One of
#    Two Setups"):
#      bash <skill-root>/skills/github-project/scripts/init-branch-protection.sh OWNER/REPO --solo

# 2. After the first CI run completes on the default branch:
bash <skill-root>/skills/github-project/scripts/init-branch-protection.sh OWNER/REPO --from-current-checks
#    Discovers successful check-run names from /commits/{default}/check-runs
#    and sets them as required contexts with strict=true (false once a merge
#    queue is in effect): PATCHes the
#    existing status-check block, or — when step 1 left none — re-PUTs the
#    protection with every current setting carried over (the PATCH
#    subresource answers 404 "Required status checks not enabled").

# 3. Then add the org-standard merge queue:
bash <skill-root>/skills/github-project/scripts/init-branch-protection.sh OWNER/REPO --merge-queue
#    Creates a repository ruleset "merge-queue" on ~DEFAULT_BRANCH, sets
#    classic strict to false and allow_auto_merge to true. Refuses (exit 6)
#    while a required context is one that never reports on merge_group
#    (CodeQL, Opengrep OSS, betterleaks, zizmor, SonarCloud Code Analysis,
#    and "Analyze (<language>)" while CodeQL default setup is configured),
#    and while a ruleset code_scanning rule requires CodeQL under default
#    setup, which blocks every fork pull request — see merge-strategy.md,
#    "Enabling a merge queue".
#    Prerequisite the script cannot check: every workflow that produces a
#    required context has `merge_group:` in `on:`. Without it that context
#    never reports in the queue and every entry times out.
```

The script is idempotent: re-running on an already-compliant repo reports `already compliant` and exits 0. Drift on opinionated fields exits 1 with a per-field diff (no silent clobber of admin choices).

## Deliberately permissive knobs

- **`enforce_admins`** — explicitly `false` in the template. Solo-maintainer Netresearch repos (snipe-it-docker-compose-stack, ldap-selfservice-…, usercentrics-widgets, etc.) need admin bypass for emergency response. Tighten per-repo once the team validates the workflow:
  ```bash
  gh api repos/OWNER/REPO/branches/DEFAULT/protection/enforce_admins -X POST
  ```
- **`required_signatures`** — *omitted entirely* from the template (not set to `false`). PUTting the template would otherwise reset repos that have already opted into signing. The script never touches this field. Tighten per-repo:
  ```bash
  gh api repos/OWNER/REPO/branches/DEFAULT/protection/required_signatures -X POST
  ```

Both knobs flip to `true` only after the team has signing infrastructure for bot accounts (Dependabot, Renovate) so those PRs don't immediately get blocked.

## Verification

Read-only audit of an existing repo:

```bash
gh api repos/OWNER/REPO/branches/$(gh api repos/OWNER/REPO --jq .default_branch)/protection \
  --jq '.required_conversation_resolution.enabled // false'
```

Or invoke `/assess github-project` — checkpoint `GH-31` fails with `severity: error` if `required_conversation_resolution` is not enabled, with a `desc:` that names this exact failure mode.

## Gap NOT closed by the baseline

GitHub branch protection cannot block on *requested-but-pending* reviews (Copilot is mid-review, you merge anyway). The baseline closes the **unresolved-threads** class (which is what snipe-it#17 slipped through), not the **pending-reviewer** class. The pending-reviewer gap is a workflow-discipline rule audited via the GraphQL `reviewRequests` check before any merge — see `references/security-config.md` § "Required Reviews from All Requested Reviewers".

## Script exit codes

| Code | Meaning |
|------|---------|
| 0    | Applied, or already compliant |
| 1    | Drift detected on opinionated fields (per-field diff printed); script refuses to clobber |
| 2    | Invalid arguments / template missing |
| 3    | Repo not found or no API access |
| 4    | Default branch ref does not yet exist (empty repo — push first) |
| 5    | `--from-current-checks`: no completed CI run on default branch |

## Actions & Security Hardening (apply alongside branch protection)

`init-branch-protection.sh` covers branch protection only. A repo's **Actions permissions** and **security toggles** are a separate API surface that GitHub ships at insecure defaults: `GITHUB_TOKEN` read/write, workflows may approve PRs, no SHA-pinning, all actions allowed. Apply these in the same bootstrap step.

> **Org members:** if the org already sets these at `orgs/ORG/actions/permissions` (see [`org-security-settings.md`](org-security-settings.md)) the repo inherits them — the per-repo commands below are for standalone repos, or repos under a permissive org default. (Endpoint shapes verified against [AriESQ/gh-safe-repo](https://github.com/AriESQ/gh-safe-repo).)

### Workflow token: read-only, no self-approval

```bash
gh api repos/OWNER/REPO/actions/permissions/workflow -X PUT \
  -f default_workflow_permissions=read \
  -F can_approve_pull_request_reviews=false
```

- `default_workflow_permissions=read` — `GITHUB_TOKEN` defaults to read-only; jobs needing write opt in at job level (see [`security-config.md`](security-config.md) § Least-Privilege Workflow Permissions). GitHub's default is `write`.
- `can_approve_pull_request_reviews=false` — stops a workflow from approving its own PRs (which would otherwise satisfy `required_approving_review_count` without a real reviewer).

> **Interaction 1 — read-only token + reusable-workflow callers.** Once the default
> is `read`, a caller **job** that calls a reusable workflow and omits its own
> `permissions:` block inherits read-only and **fails at startup** (`startup_failure`,
> before any step) if the reusable declares a permission it wasn't granted. Symptom:
> a whole workflow shows `startup_failure` with no logs. Fix: give each caller job an
> explicit `permissions:` matching the reusable's documented caller requirements
> (e.g. `contents: read` + `security-events: write` for the security reusables). This
> bit the netresearch security.yml callers after hardening.
>
> **Interaction 2 — `can_approve_pull_request_reviews=false` disables auto-approve.** If the repo uses a
> `pr-quality`-style **auto-approve** workflow (solo-maintainer flow) or **dependabot
> auto-merge** with `required_approving_review_count >= 1`, those rely on a workflow
> approving the PR. Setting `can_approve_pull_request_reviews=false` silently breaks
> them — PRs then stick on `REVIEW_REQUIRED` and dependabot PRs never auto-merge.
> **Keep `can_approve_pull_request_reviews=true`** when you use auto-approve/auto-merge; the
> least-privilege win is already carried by `default_workflow_permissions=read`.

### Restrict which actions can run + require SHA pinning

```bash
# Allow only GitHub-owned + verified-creator actions, and require SHA pins.
# enabled=true is REQUIRED in this body or the PUT returns 422.
gh api repos/OWNER/REPO/actions/permissions -X PUT \
  -F enabled=true \
  -f allowed_actions=selected \
  -F sha_pinning_required=true

# Allow-list — only valid AFTER allowed_actions=selected (apply order matters):
gh api repos/OWNER/REPO/actions/permissions/selected-actions -X PUT --input - <<'EOF'
{ "github_owned_allowed": true, "verified_allowed": true, "patterns_allowed": ["OWNER/*"] }
EOF
```

- `sha_pinning_required=true` is the repo-level twin of the org setting — workflows must pin actions to a full commit SHA. Reusable-workflow `@main`/`@vX` refs are exempt; see [`reusable-workflow-security.md`](reusable-workflow-security.md).

### Fork-PR approval (public repos only)

Holds fork PRs — and the Actions minutes they would burn — until a maintainer approves. The endpoint exists only for public repos (returns null/404 on private):

```bash
gh api repos/OWNER/REPO/actions/permissions/fork-pr-contributor-approval -X PUT \
  -f approval_policy=all_external_contributors
```

| `approval_policy` | Who needs approval before fork-PR workflows run |
|---|---|
| `first_time_contributors_new_to_github` | Brand-new GitHub accounts only (GitHub default) |
| `first_time_contributors` | First-time contributors to this repo |
| `all_external_contributors` | Every external contributor (safest) |

**From the contributor side, this looks like a broken PR.** Every workflow reports `action_required` — `completed/action_required`, not `failure` — and `gh pr checks` shows only the handful of jobs that run without approval (`pull_request_target` ones, e.g. a PR-title linter). Nothing is wrong and there is nothing to fix; a maintainer has to click *Approve and run workflows*. Confirm rather than guess:

```bash
gh api "repos/OWNER/REPO/actions/runs?event=pull_request" \
  --jq '.workflow_runs[] | select(.head_branch=="MY-BRANCH")
        | "\(.name): \(.status)/\(.conclusion)"'
```

A uniform `completed/action_required` across every workflow is the approval gate, not a red build. Do not push "fix CI" commits at it.

### Security toggles

```bash
# Dependabot alerts + automatic security-update PRs (bodyless PUTs)
gh api repos/OWNER/REPO/vulnerability-alerts -X PUT
gh api repos/OWNER/REPO/automated-security-fixes -X PUT

# Private vulnerability reporting — a STANDALONE PUT, not a security_and_analysis field
gh api repos/OWNER/REPO/private-vulnerability-reporting -X PUT

# Secret-scanning push protection (paid/private; auto-on for public).
# secret_scanning MUST be sent alongside push protection or the PATCH is silently ignored.
gh api repos/OWNER/REPO -X PATCH --input - <<'EOF'
{ "security_and_analysis": {
    "secret_scanning": { "status": "enabled" },
    "secret_scanning_push_protection": { "status": "enabled" } } }
EOF
```

> **Plan gate:** rulesets, Dependabot, and secret scanning are unavailable on **free-plan private** repos — the API returns 403 (you can't even `GET .../rulesets`). Public repos and paid plans (the Netresearch org) get all of it. If a toggle 403s, check the repo's plan/visibility before debugging the call. More scripting quirks: [`security-config.md`](security-config.md) § GitHub Security API.



--- FILE: skills/github-project/references/repo-retirement.md ---

<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->
<!-- SPDX-FileCopyrightText: Netresearch DTT GmbH -->

# Retiring a Repository

A repository nobody consumes is retired, not upgraded. Measure the consumers
**before** the first upgrade step — the result decides which of the two
tasks you are doing. (Observed 2026-09-24 on `netresearch/deploy-rst`: the
default-branch rename, three rulesets and a template-sync PR were all done
before the consumer count — 29 downloads in total, 0 per month, 0
dependents — turned the task into an archive.)

## 1. Measure the consumers

```bash
# Packagist: downloads and dependent packages (Composer packages)
curl -s "https://packagist.org/packages/VENDOR/NAME.json" \
  | jq '{downloads: .package.downloads, dependents: .package.dependents}'

# Org-internal references — REST search, not `gh search code`
# (see multi-repo-operations.md § "Never enumerate by content with gh search code")
gh api --paginate "search/code?q=%22VENDOR/NAME%22+org:OWNER&per_page=100" \
  --jq '.items[] | "\(.repository.name)|\(.path)"' | sort -u
```

A hit list that contains only the repository itself is the known-positive
baseline: the index covers the repository, and nothing else references it.
An empty list proves nothing — the search may simply have failed.

Check the runtime premise too: a tool whose integration target is gone (for
example a SOAP client for a server product the organisation replaced with
the cloud edition) has no users to find, whatever the numbers say.

## 2. Mark the package as abandoned

For a Composer package, add the flag to `composer.json` on the default
branch:

```json
"abandoned": true
```

(or `"abandoned": "vendor/replacement"` to name a successor). Packagist
reads the flag from the default branch and marks the **whole package**
abandoned, including tagged versions that predate the change — no Packagist
login and no "Abandon" button needed.

Add a notice at the top of the README. In an `.rst` README use bold text
between `----` transitions — GitHub renders RST admonitions as plain text
(see `repository-structure.md`).

## 3. Merge, then let CI settle

Merge the change, then wait until every workflow run on the merge commit
has completed and passed. Pin the SHA, so a run for an older commit cannot
stand in for the last one; the archived repository then ends on a known
green state.

```bash
SHA=$(git rev-parse origin/main)
gh run list -R OWNER/REPO --commit "$SHA" \
  --json name,status,conclusion --jq '.[] | "\(.name): \(.status)/\(.conclusion)"'
```

## 4. Archive

```bash
gh repo archive OWNER/REPO --yes
gh api repos/OWNER/REPO --jq .archived     # true
```

## 5. Verify the registry — past its cache

`packagist.org/packages/VENDOR/NAME.json` is served from a cache and can
report `"abandoned": null` for several minutes after the update. The
Composer v2 metadata reflects the change first:

```bash
curl -s "https://repo.packagist.org/p2/VENDOR/NAME~dev.json" \
  | jq '[.packages["VENDOR/NAME"][] | {version, abandoned}]'
curl -s "https://packagist.org/packages/VENDOR/NAME.json?nocache=$(date +%s)" \
  | jq '.package.abandoned'
```

A `null` on the first read is a cache hit, not a missing flag — re-read
with the cache-buster before telling anyone to click anything.



--- FILE: skills/github-project/references/repo-setup-guide.md ---

<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->
<!-- SPDX-FileCopyrightText: Netresearch DTT GmbH -->

# Repository Setup Guide

Project-type-specific CI checklists and repository standards.

## Go Project CI Checklist

| Setting | Purpose | How |
|---------|---------|-----|
| Branch protection | Require tests pass before merge | Branch settings or Rulesets |
| Dependabot/Renovate | Automated dependency updates | `.github/dependabot.yml` or `renovate.json` |
| Auto-merge workflow | Merge minor/patch updates automatically | `assets/auto-merge*.yml` templates |
| Required checks | CI workflow names in branch protection | Match exact workflow job names |

## Polyglot Project CI Checklist (PHP + JavaScript)

| Requirement | Implementation | Why |
|-------------|----------------|-----|
| PHP test coverage | `phpunit --coverage-clover` for each test suite | Codecov needs all suites |
| JavaScript test coverage | `npm run test:coverage` with lcov output | Codecov aggregates all languages |
| vitest lcov reporter | `reporter: ['text', 'json', 'html', 'lcov']` | Required for Codecov compatibility |
| Codecov upload | List ALL coverage files in `files:` parameter | Ensures complete coverage picture |

### Example CI Configuration

```yaml
# Run all PHP test suites with coverage
- run: php -d pcov.enabled=1 .Build/bin/phpunit -c Build/phpunit/UnitTests.xml --coverage-clover .Build/coverage/unit.xml
- run: php -d pcov.enabled=1 .Build/bin/phpunit -c Build/phpunit/IntegrationTests.xml --coverage-clover .Build/coverage/integration.xml

# Run JavaScript tests with coverage
- uses: actions/setup-node@SHA # vX.Y.Z
  with:
    node-version: '22'
- run: npm install
- run: npm run test:coverage

# Upload ALL coverage files
- uses: codecov/codecov-action@SHA # vX.Y.Z
  with:
    files: .Build/coverage/unit.xml,.Build/coverage/integration.xml,coverage/lcov.info
```

### vitest Configuration

When using vitest, the `lcov` reporter is **required** for Codecov:

```javascript
// vitest.config.js
coverage: {
    provider: 'v8',
    reporter: ['text', 'json', 'html', 'lcov'],  // lcov REQUIRED
    reportsDirectory: 'coverage',
}
```

## TYPO3 Extension Repository Standards

### Repository Settings

Configure via GitHub UI or `gh` CLI:

```bash
# Enable Projects tab
gh repo edit --enable-projects

# Set description (template)
gh repo edit --description "TYPO3 extension for <purpose> - by Netresearch"

# Add topics
gh api repos/OWNER/REPO/topics -X PUT -f names='["typo3","typo3-extension","php","<domain-topics>"]'
```

| Setting | Value | Why |
|---------|-------|-----|
| `has_projects` | true | Project board for issue tracking |
| `has_wiki` | false | Use Documentation/ folder instead |
| Description | `<What it does> - by Netresearch` | Consistent branding |

### Required Topics

All TYPO3 extension repos MUST have these topics:

| Topic | Required | Example |
|-------|----------|---------|
| `typo3` | Always | - |
| `typo3-extension` | Always | - |
| `php` | Always | - |
| Domain-specific | 2-5 more | `ckeditor`, `llm`, `ai`, `rte` |

**Example from t3x-rte_ckeditor_image:**
```
typo3, typo3-extension, typo3cms-extension, ckeditor, ckeditor-plugin, rte-ckeditor, magic-images
```

**Example from t3x-nr-llm:**
```
typo3, typo3-extension, php, ai, llm, openai, anthropic, claude, gemini, gpt
```

### README Badge Order

Badges should appear in this order (see `netresearch-branding` skill for templates):

```markdown
<!-- Row 1: CI/Quality badges -->
[![CI](...)][ci]
[![codecov](...)][codecov]
[![Documentation](...)][docs]  <!-- if applicable -->

<!-- Row 2: Security badges -->
[![OpenSSF Scorecard](...)][scorecard]
[![OpenSSF Best Practices](...)][bestpractices]
[![SLSA 3](...)][slsa]

<!-- Row 3: Standards badges -->
[![PHPStan](...)][phpstan]
[![PHP 8.x+](...)][php]
[![TYPO3 vXX](...)][typo3]
[![License](...)][license]
[![Latest Release](...)][release]
[![Contributor Covenant](...)][covenant]

<!-- Row 4: TYPO3 TER badges (if published to TER) -->
![Composer](https://typo3-badges.dev/badge/EXT_KEY/composer/shields.svg)
![Downloads](https://typo3-badges.dev/badge/EXT_KEY/downloads/shields.svg)
![Extension](https://typo3-badges.dev/badge/EXT_KEY/extension/shields.svg)
![Stability](https://typo3-badges.dev/badge/EXT_KEY/stability/shields.svg)
![TYPO3](https://typo3-badges.dev/badge/EXT_KEY/typo3/shields.svg)
![Version](https://typo3-badges.dev/badge/EXT_KEY/version/shields.svg)
```

### Quick Setup Commands

```bash
# Set topics for TYPO3 extension
gh api repos/netresearch/t3x-EXTNAME/topics -X PUT \
  -f names='["typo3","typo3-extension","php","DOMAIN1","DOMAIN2"]'

# Enable projects
gh repo edit netresearch/t3x-EXTNAME --enable-projects

# Update description
gh repo edit netresearch/t3x-EXTNAME \
  --description "TYPO3 extension for PURPOSE - by Netresearch"
```

### Verification

Check repository compliance:

```bash
# Check topics
gh api repos/OWNER/REPO/topics --jq 'if (.names | contains(["typo3"]) and contains(["typo3-extension"]) and contains(["php"])) then "OK: Required topics present" else "MISSING: Required topics" end'

# Check has_projects
gh api repos/OWNER/REPO --jq 'if .has_projects then "OK: Projects enabled" else "MISSING: Projects disabled" end'
```

## SonarCloud Quality Gate Gotcha

A **wholesale structural change** to a file (e.g. converting a classic-script IIFE to an
ES module, or moving most of a class) makes SonarCloud attribute the **entire file** as
"new code". Every latent smell in it then counts against the new-code gate, so
`new_maintainability_rating` can flip to D from a change that "only refactored" — and the
gate blocks the merge.

Anticipate it: when you modernise a file's module structure, **fix all its latent smells
in the same change** rather than reverting — typically `var`→`const` (rule S3504), reduce
cognitive complexity by extracting helpers (S3776), and replace `innerHTML` with DOM
construction / `DOMParser` (also clears the XSS hotspot). The gate sees a brand-new file,
not a diff.

For Python, pre-check S3776 locally before pushing: `uvx --from complexipy complexipy
<file>` prints the cognitive complexity per function. The rule's default threshold is
15; a project's quality profile can change it, so read the profile assigned to the
project. complexipy is an independent tool, not SonarCloud's analyzer. On
`netresearch/data-tools-skill` its figures matched SonarCloud's for three functions
(18, 17 and 16, and 2 and 3 after a split), so a local run can save a push and a
re-analysis per attempt; SonarCloud's result on the PR stays the authority.

To raise one rule's threshold for one project, give the project its own quality profile
that inherits the profile it uses now, and override only that rule. The token needs the
organization's `Administer Quality Profiles` permission: `qualityprofiles/search?organization=<org>`
answers `"actions":{"create":true}` when it has it. Assigning the profile to a project also
works with the project's `Administer` permission. Four `POST` calls to
`https://sonarcloud.io/api/qualityprofiles/…`, each with `Authorization: Bearer <token>`:

1. `create` with `name`, `language` and `organization`. The new key is in `.profile.key`.
2. `change_parent` with `key=<new key>` and `parentKey=<key of the current profile>` and
   nothing else. With `organization`, `language` or `qualityProfile` added, the call
   answers HTTP 400: "When a quality profile key is set, 'organization' 'language' and
   'qualityProfile' can't be set".
3. `activate_rule` with `key=<new key>`, `rule=<rule>` and `params=<param>=<value>`, for
   example `rule=php:S1142` and `params=max=9`.
4. `add_project` with `key=<new key>` and `project=<projectKey>`.

Read the result back from `qualityprofiles/search?project=<projectKey>&organization=<org>`,
which lists `parentKey`. `qualityprofiles/show` returns `parentKey: null` for a profile
that has a parent, so it cannot confirm step 2. In
`rules/show?key=<rule>&organization=<org>&actives=true` the override carries
`inherit: OVERRIDES`. The next analysis of the branch closes the issues that the new
threshold no longer raises; issues above the new threshold stay open.
(`netresearch/t3x-nr-llm`, 2026-10-25: `php:S1142` from 3 to 9 returns; after the 22
methods above 9 were split, `main` went from 278 issues of that rule to 0.)

To see which new-code smells are blocking, query SonarCloud's `api/issues/search`
endpoint (authenticated with your SonarCloud token via HTTP basic auth — token as the
username, empty password) filtered to `types=CODE_SMELL&resolved=false` for the PR, e.g.:

```
GET https://sonarcloud.io/api/issues/search
      ?componentKeys=<projectKey>&pullRequest=<PR>&types=CODE_SMELL&resolved=false
      &s=SEVERITY&asc=false
```

Each issue's `rule` + `message` + `component:line` tells you exactly what to fix.



--- FILE: skills/github-project/references/repository-structure.md ---

<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->
<!-- SPDX-FileCopyrightText: Netresearch DTT GmbH -->

# Repository Structure Reference

Standard files and directories for GitHub open source projects.

## Root Directory Files

### README.md
Primary project documentation visible on repository homepage.

**Essential Sections:**
```markdown
# Project Name

Brief description (1-2 sentences)

## Features
- Key feature 1
- Key feature 2

## Installation
```bash
# Installation commands
```

## Quick Start
```bash
# Usage example
```

## Documentation
Link to full docs

## Contributing
Link to CONTRIBUTING.md

## License
License type with link
```

### LICENSE
Standard open source license file.

**Common Choices:**
| License | Use Case |
|---------|----------|
| MIT | Maximum permissiveness |
| Apache-2.0 | Patent protection |
| GPL-3.0 | Copyleft requirement |
| BSD-3-Clause | Simple permissive |

### CHANGELOG.md
Version history following [Keep a Changelog](https://keepachangelog.com/) format.

**Structure:**
```markdown
# Changelog

## [Unreleased]

## [1.2.0] - 2024-01-15
### Added
- New feature X

### Changed
- Updated behavior Y

### Fixed
- Bug in Z

### Removed
- Deprecated feature W
```

### CONTRIBUTING.md
Contributor guidelines and development setup.

**Essential Sections:**
- Development environment setup
- Code style requirements
- Testing expectations
- Pull request process
- Commit message format

### CODE_OF_CONDUCT.md
Community behavior standards.

**Recommended:** [Contributor Covenant](https://www.contributor-covenant.org/) v2.1

### SECURITY.md
Security policy and vulnerability reporting.

**Essential Sections:**
- Supported versions
- Reporting process (GitHub Security Advisories preferred)
- Response timeline
- Security measures in place

### GOVERNANCE.md
Project decision-making structure.

**Models:**
- BDFL (Benevolent Dictator For Life)
- Meritocracy
- Liberal contribution
- Technical steering committee

## .github Directory

### CODEOWNERS
Automatic review assignment.

```
# Default owners
* @org/maintainers

# Directory-specific
/src/ @org/core-team
/.github/ @org/maintainers
/SECURITY.md @org/security-team
```

### dependabot.yml
Automated dependency updates.

### renovate.json
Alternative to Dependabot with more configuration options.

### ISSUE_TEMPLATE/
- `bug_report.md` - Bug report template
- `feature_request.md` - Feature request template
- `config.yml` - Issue template chooser configuration

### PULL_REQUEST_TEMPLATE.md
Standard PR description format.

### workflows/
GitHub Actions workflow files.

**Common Workflows:**
| File | Purpose |
|------|---------|
| ci.yml | Continuous integration |
| release.yml | Release automation |
| scorecard.yml | OpenSSF Scorecard |
| auto-merge.yml | Dependency auto-merge |

## Language-Specific Files

### Go Projects
```
project/
├── go.mod
├── go.sum
├── .golangci.yml
├── .goreleaser.yml (optional)
└── .slsa-goreleaser/ (for SLSA releases)
```

### PHP/TYPO3 Projects
```
project/
├── composer.json
├── composer.lock
├── .php-cs-fixer.php
├── phpstan.neon
├── rector.php
└── Build/
    └── phpunit/
```

### Node.js Projects
```
project/
├── package.json
├── package-lock.json
├── .eslintrc.js
├── .prettierrc
└── tsconfig.json (TypeScript)
```

## Directory Structure Patterns

### By Feature (Recommended)
```
project/
├── cmd/           # Go: Entry points
├── internal/      # Go: Private packages
├── pkg/           # Go: Public packages
├── Classes/       # PHP: Source code
├── src/           # Generic: Source code
├── tests/         # Test files
├── docs/          # Documentation
└── scripts/       # Utility scripts
```

### By Layer
```
project/
├── controllers/
├── services/
├── repositories/
├── models/
└── utils/
```

## Fork Workflow Pattern

When contributing to upstream projects via a fork:

### Remote Naming Convention
```bash
# 'origin' should point to your fork (this is the default when you clone it).
# 'upstream' should point to the original project.
# After cloning your fork, you just need to add the upstream remote:
git remote add upstream https://github.com/upstream-org/project.git
```

### PR Strategy
1. **Upstream PRs**: Push branch to fork, create PR targeting upstream `main`
2. **Intra-fork PRs**: For changes not ready for upstream, create PR within fork. A PR opened in the fork first is reviewed by any AI reviewer enabled on the fork (such as Copilot or Gemini Code Assist) before the upstream maintainers see it.
3. **Branch hierarchy**: Feature branches based on fix branches for incremental work

```bash
# Push fixes upstream
gh pr create --repo upstream-org/project --head myorg:fix/branch --base main

# Intra-fork PR for additional work
gh pr create --repo myorg/project --head feat/new-feature --base fix/branch
```

### Archived Upstream Actions
Before inheriting CI workflows from upstream, verify all GitHub Actions are still maintained:
```bash
# Check if an action's repo is archived
gh api repos/OWNER/ACTION-REPO --jq '.archived'
```

Common archived TYPO3 CI actions:
- `TYPO3-Continuous-Integration/TYPO3-CI-Xliff-Lint` — archived 2021, Docker image 403
- Always check `TYPO3-Continuous-Integration/*` repos before relying on them

## Best Practices

1. **Keep root clean**: Only essential config files at root
2. **Group related files**: Use directories for organization
3. **Follow conventions**: Use standard names (src/, tests/, docs/)
4. **Document structure**: Include structure explanation in README
5. **Ignore properly**: Maintain comprehensive .gitignore

## RST READMEs: admonition directives do not render on GitHub

GitHub renders `.rst` through a bare docutils HTML writer with **no admonition CSS**: `.. danger::`/`.. warning::`/`.. caution::` come out as a literal `!DANGER!`/`!WARNING!` paragraph — no box, no colour — and `note/tip/important/hint` render as plain text. An admonition directive is worse than nothing there.

- For a prominent notice in GitHub-rendered RST, use top-level **bold paragraphs + emoji**, separated by `----` transitions (`<hr>`) — and check the rendered output for doubled rules before stacking a transition next to other elements that emit their own `<hr>`.
- A real coloured callout exists only in Markdown: `> [!WARNING]` / `> [!CAUTION]` / `> [!NOTE]` — one more reason to prefer `README.md` over `README.rst`.
- Verify the actual render without a browser: `gh api "repos/OWNER/REPO/readme?ref=BRANCH" -H "Accept: application/vnd.github.html"` (use the `?ref=` query form; confirm you got real HTML before grepping — a 404 body trivially contains 0 matches).



--- FILE: skills/github-project/references/reusable-workflow-pitfalls.md ---

<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->
<!-- SPDX-FileCopyrightText: Netresearch DTT GmbH -->

# Reusable Workflow Pitfalls

Operational and structural pitfalls when authoring reusable workflows and the composite actions they use. Distinct from `reusable-workflow-security.md` — that doc covers supply-chain trust and SHA pinning of *external* actions; this doc covers structural traps that have bitten in practice when building *internal* reusable workflows.

## 1. `./` does NOT resolve to the reusable workflow's repo

When a workflow is invoked via `workflow_call`, references like `uses: ./.github/actions/foo` are resolved against the **consumer's** workspace, not the reusable workflow's repo. The action will fail to load unless the consumer happens to have an identically-named local action.

GitHub documents this directly: "Local actions in workflows that are called as a reusable workflow are not supported." (See [Reusing workflows — limitations](https://docs.github.com/en/actions/sharing-automations/reusing-workflows#limitations).)

To call a composite action from a reusable workflow, reference it absolutely:

```yaml
# In the reusable workflow:
uses: org/repo/.github/actions/foo@<sha>   # works (absolute reference)
# uses: ./.github/actions/foo              # FAILS at the consumer
```

## 2. Composite-action references must be SHA-pinned

Internal `@main` references are accepted for **full reusable workflows** (`uses: org/repo/.github/workflows/foo.yml@main`) — see `reusable-workflow-security.md`. But **composite actions** (`uses: org/repo/.github/actions/foo@main`) are different: the consumer's runner resolves them under the consumer's allow-list policy. A consumer enforcing "all actions must be SHA-pinned" will reject the reusable workflow's job entirely, even though the reusable workflow file itself is unchanged.

This is enforced mechanically by checkpoint **GH-34**.

```yaml
# Inside a reusable workflow:
- uses: org/repo/.github/actions/preflight-gate@<40-char-sha>   # OK
# - uses: org/repo/.github/actions/preflight-gate@main          # breaks SHA-pinned consumers
```

When you self-reference a composite action inside the same repo that hosts the reusable workflow, you create a chicken-and-egg: the SHA you pin to must already exist in the same PR you're authoring. Two options: (a) inline the action's body as bash steps directly in the workflow (avoiding the cross-action `uses:`), or (b) land the composite action first, then SHA-pin to it in a follow-up PR.

## 3. `gh run rerun` caches `@ref` resolution

When a workflow run is created, GitHub records the resolved SHAs of every `uses: org/repo/...@ref` at that moment. **Re-running the same run replays those exact SHAs** — it does not re-evaluate the refs. This means: if you fix a bug in an upstream reusable workflow and merge the fix, then re-run a failed workflow that consumed `@main`, you will get the **old, broken** body.

To pick up upstream changes after merging the fix, you must create a **new** run — the ref is not re-resolved per-job or on rerun:

- **PR:** push a new commit (`git commit --allow-empty -m "trigger ci"`), or close + reopen the PR (`gh pr close N && gh pr reopen N`), or trigger a fresh `workflow_dispatch` run.
- **Scheduled / non-PR repo with no `workflow_dispatch`:** create a throwaway branch at the default-branch SHA to fire a fresh `push` run, then delete it:

  ```bash
  gh api -X POST repos/O/R/git/refs -f ref=refs/heads/ci/verify -f sha=<sha>
  gh api -X DELETE repos/O/R/git/refs/heads/ci/verify
  ```
- A scheduled-only repo whose default branch has no new commit keeps *displaying* the stale red run until its next push/schedule — the fix is in, the badge just hasn't refreshed.

`gh run rerun` is fine for genuinely transient failures (network blips, rate limits) — not for "I fixed the upstream reusable workflow." (Distinct from the consumer's own base-SHA staleness; see `gh-cli-reference.md` → "`gh run rerun` re-runs the OLD state".)

> **Re-triggering a tag workflow** after fixing the workflow file requires **moving the tag** (delete the remote tag, re-tag the fixed default-branch tip, push) — tag events fire against the workflow file *at the tag's commit*. DANGER: only safe when the package is on **no** registry — Packagist/npm webhooks publish within seconds and stable versions are immutable. "The release workflow failed" does not mean nothing was published; check the registry first and prefer fix-forward with a patch version.

## 4. Permissions ceiling — caller cannot grant what it lacks

A reusable workflow's `permissions:` block sets the **maximum** scopes the called job is allowed to use. The actual token issued is the **intersection** of the caller's job-level `permissions:` and the reusable workflow's declared `permissions:`. If the calling job sets `permissions: {}` (empty), the reusable job receives a token with **zero** scopes regardless of what the reusable workflow declares.

When a reusable workflow gains a new requirement (e.g., a step that calls `gh api` and needs `actions: read`), every consumer's calling job must also be updated to grant that scope. Otherwise the new step fails with a 403 in production but works in your test repo where you happen to have broader permissions.

```yaml
# Consumer side — must include EVERY scope the reusable workflow needs:
jobs:
    call-shared:
        permissions:
            contents: read
            actions: read           # required by the reusable workflow's gh api step
            pull-requests: write
        uses: org/ci-workflows/.github/workflows/shared.yml@<sha>
```

See [GitHub docs — access and permissions](https://docs.github.com/en/actions/sharing-automations/reusing-workflows#access-and-permissions) for the full intersection rules.

> **See also:** [`reusable-workflow-security.md`](./reusable-workflow-security.md) for SHA-pinning and supply-chain trust of *external* actions.

## 5. Inline `config_data` overrides the repo's own config file

Linter actions that accept an inline `config_data:` (e.g. yamllint via a
reusable workflow) **replace** the consumer repo's own config file entirely —
they do not merge. A repo with a carefully tuned `.yamllint.yml` (ignore paths,
relaxed rules) silently has all of it discarded the moment the reusable workflow
passes its own inline defaults.

Provide inline defaults only as a *fallback*, when the repo has no config of its own:

```yaml
- name: Provide default config if the repo has none
  run: |
    if [[ ! -f .yamllint.yml ]]; then
      cat > .yamllint.yml <<'EOF'
    extends: default
    rules: { line-length: disable }
    EOF
    fi
- name: Lint
  uses: some/yamllint-action@<sha>   # picks up the repo's config, or the fallback
```

## 6. Fix the gap in the shared workflow, not per-project

When CI or quality logic lives in a shared reusable workflow (e.g. `netresearch/typo3-ci-*`), a gap or bug that surfaces in one consumer is almost always a gap in the **shared** workflow. Fix it upstream so every consumer inherits the fix — do not patch the single project's `.github/workflows/`.

Per-project patches defeat the point of the reusable workflow: they reintroduce the duplication the shared workflow exists to remove, drift out of sync as the shared workflow evolves, and force the same fix to be rediscovered in the next repo.

Before adding a guard, check, or fix to a project's own workflow files, ask whether the shared reusable-workflow repo already owns that concern — or should. If it does, land the change there and let the consumer pick it up via its `@main` / `@vX.Y.Z` reference (per [`reusable-workflow-security.md`](./reusable-workflow-security.md), internal reusable workflows are referenced by tag/branch, not SHA). Keep logic in a consumer only when it is genuinely project-specific.

This is distinct from pitfalls #1–#5 above (which cover *how* to author and reference reusable workflows) — this is about *where* a fix belongs.

### The consumer-side tell

The rule is easiest to apply as a property of the consumer's workflow file: **every job in a
consumer repo is a `uses:` of a shared workflow.** A job with its own `steps:` — checkout,
setup, install, run — is the smell, and third-party actions (`actions/checkout`,
`shivammathur/setup-php`, …) appearing anywhere outside the shared-workflow repo is the same
smell stated in terms of `uses:`. Verify with:

```bash
grep -rn "uses:" .github/workflows/ | grep -vi "YOUR_ORG/"
```

Anything that returns is either a genuinely project-specific exception or work that belongs
upstream. Pinning such an action to a SHA does not make it compliant — the pin is a separate
requirement (`reusable-workflow-security.md`), not a substitute for this one.

### Extending the shared workflow instead

When the shared workflow has no input for what the consumer needs, add one — this is the
supported path, not a workaround:

- Add the input **defaulting to off** (`type: boolean`, `default: false`) and gate the new
  job on it, so every existing consumer is unaffected. Verify the diff is purely additive
  (`git diff origin/main... -U0 | grep -E '^-[^-]'` returns nothing) — an existing consumer must not change
  behaviour because another repo needed a feature.
- Copy the action pins verbatim from a neighbouring job in the same file rather than picking
  versions independently; a shared workflow with two different `actions/checkout` SHAs is its
  own maintenance problem.
- Give the new job a graceful skip (a `::notice::`) when the consumer lacks the underlying
  script, so enabling the input in a repo that is not ready cannot hard-fail.
- Land it, then flip the input on in the consumer. The consumer's change is one line.

Do not reach for `unit-test-command`-style override inputs to smuggle an extra suite into an
existing job: those replace the job's instrumented default command and silently drop whatever
it did (coverage upload, for instance).

## 7. Run with zero jobs whose name is the file path = workflow-validation failure

A run with `conclusion: startup_failure` (or `failure`), **zero jobs**, and a displayed name that falls back to the workflow **file path** failed at workflow *validation*, before any job started. The exact reason is **only in the Actions UI banner** — it is not exposed via the REST API (`gh run view --log[-failed]` returns "log not found"; run/annotations/check-suite endpoints are empty). If you can't see the UI, ask for the banner text. Two causes seen in practice:

1. **Dead reusable-workflow reference** — a `uses:` pointing at a reusable workflow file that no longer exists (e.g. a deleted shared workflow); callers fail silently, sometimes for months. Inspect the `uses:` lines and `gh api`/`curl` the referenced files for 404.
2. **Permission mismatch** — the caller's job omits an explicit `permissions:` block, the repo's `default_workflow_permissions` is `read`, but a nested reusable job requests e.g. `security-events: write`. UI error: "The nested job 'X' is requesting 'security-events: write', but is only allowed 'security-events: none'." Deceptive because a **byte-identical** workflow file passes in sibling repos whose repo-default permissions are permissive — it is repo-environmental, not a file diff. Fix at the caller per pitfall #4: grant the calling job exactly the scopes the reusable declares.

```bash
gh api repos/O/R/actions/permissions --jq '.default_workflow_permissions? // ""'   # reveals a restrictive 'read' default
```


## 8. `release: published` never fires for a release a workflow created

A workflow that reacts to releases with

```yaml
on:
  release:
    types: [published]
```

is **inert for every automated release**. GitHub does not raise events from
actions taken with the default `GITHUB_TOKEN` — a deliberate guard against
recursive runs — and the release is created by the release workflow using
exactly that token. The trigger only fires for releases a human creates in the
UI or via a PAT.

This fails silently in the worst way: the workflow is registered, `state:
active`, and simply never runs. Nothing appears in the Actions tab to explain
the absence.

Trigger off the producing workflow instead:

```yaml
on:
  workflow_run:
    workflows: ["Release"]
    types: [completed]

jobs:
  verify:
    # A run that failed has nothing to verify, and head_branch is only a tag
    # when the run came from a tag push.
    if: >-
      github.event.workflow_run.conclusion == 'success' &&
      startsWith(github.event.workflow_run.head_branch, 'v')
```

`workflow_run` observes a workflow *run*, not a repository event, so the
GITHUB_TOKEN suppression does not apply to it.

Two constraints come with it:

- The workflow file must be on the **default branch**. A `workflow_run`
  trigger added on a feature branch does nothing until it is merged — so it
  cannot be exercised on the PR that introduces it.
- **`workflow_run` does not chain.** A workflow started by `workflow_run`
  cannot itself trigger another one.

**A repo's history can mislead you here.** Checking for past `event=release`
runs is not evidence the trigger works today: a repo that once created releases
by hand will show dozens of them, all predating the automation.

### Corollary: test the trigger you ship, not a convenient one

Adding `workflow_dispatch` alongside the real trigger makes the workflow easy to
exercise — and a dispatch run proves only that the *jobs* work. It says nothing
about whether the event you actually depend on ever arrives. A gate can pass its
manual test and still be dead in production. If the real trigger cannot be
exercised before merge, say so rather than treating the dispatch run as proof.

## 9. Converting an inline job to a reusable call renames its check → update the required contexts

When you replace an inline job with a `uses:` reusable-workflow call, the surfaced
check name changes from `<job-id>` to **`<caller-job-id> / <reusable-job-name>`**.
Example: an inline `build:` job reported as `build`; after routing it through
`build-container-bake.yml` it reports as `build / Build Container (Bake)`.

Any branch-protection **required status check** or **merge-queue ruleset** that
still lists the *old* context (`build`) now waits on a check that will never
report — the PR sits `BLOCKED` / the merge-group is ejected, forever, even though
every visible check is green.

**Fix:** the required-context list must be migrated alongside the workflow change.
Because the exact new name isn't always predictable, observe it on the first run,
then update the gate:

```bash
# 1. New context name from the PR's first run
gh pr checks <PR> --repo OWNER/REPO | grep -i build

# 2a. Classic protection — preserve the other contexts, swap the renamed one
gh api repos/OWNER/REPO/branches/main/protection/required_status_checks \
  --jq '.contexts'                       # read current
# PATCH back with the old name replaced by "build / Build Container (Bake)"

# 2b. Merge-queue / ruleset — edit the ruleset's required_status_checks rule
gh api repos/OWNER/REPO/rulesets/<id>    # find the required_status_checks rule
# PUT the ruleset back with the context renamed
```

Do this in lockstep with merging the workflow PR, or the repo is unmergeable
until someone notices. (See also `dependency-management.md` for enabling a
required check via a ruleset when classic `required_status_checks` isn't set.)

## Own reusables stay `@main` — never SHA-pin them

Reusables in Netresearch-owned repos (`netresearch/.github`, typo3-ci-workflows) are called `@main`, NEVER by commit SHA: pinning freezes every consumer to a snapshot and defeats "fix once, all pick it up". The trust model differs from third-party actions (which DO get SHA-pinned). Three scanners flag every `@main` reusable line, and all three are false positives for first-party reusables: SonarCloud `githubactions:S7637`, CodeQL `actions/unpinned-tag` ("Unpinned tag for a non-immutable Action or reusable workflow") and zizmor `unpinned-uses`. Dismiss the finding as won't fix (or add an org-level exception for `netresearch/*/.github/workflows/**@main`); never capitulate with a SHA pin. On 2026-10-18 an agent pinned `script-check.yml` in netresearch-branding-skill "to resolve the unpinned reusable workflow finding" from CodeQL.

## Validating a new reusable: the first caller IS the test — use a temp branch pin

A new reusable is inert until a caller runs it. Loop: wire the first caller `@main`, let its PR CI fail, fix the reusable on a branch, and validate BEFORE merging by temporarily pointing the caller at the fix branch (`uses: …/x.yml@fix/branch` — GitHub allows branch refs). Once green: merge the reusable fix, revert the caller to `@main` (the fix branch dies on merge), confirm green, and squash the temp-pin/revert commits out of the caller PR.

## Inline → reusable migration checklist (each bit a real PR)

1. **The calling job must grant `permissions:`** (usually `contents: read`) — with workflow-level `permissions: {}` and no job grant the run **startup-fails** and the reusable's checks NEVER APPEAR; a repo without required checks then looks deceptively green. Verify the reusable RAN: `gh run list --branch <b> --json name,conclusion` shows `success`, not `startup_failure`.
2. **Required-check contexts go stale**: inline names (`PHP 8.2`) become `<caller-job-id> / <name>` (`php-ci / PHP 8.2`) — old contexts wait "Expected" forever. PATCH the protection contexts in the same change.
3. **`composer validate --strict`** (the reusable default) rejects intentional `*` constraints for virtual packages — pass `composer-validate: false` plus a non-strict `pre-install-cmd: "composer validate"`.



--- FILE: skills/github-project/references/reusable-workflow-security.md ---

<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->
<!-- SPDX-FileCopyrightText: Netresearch DTT GmbH -->

# Reusable Workflow Security Reference

Security model for internal vs external reusable workflows, transitive dependency risks, and audit practices.

## Internal vs External Reusable Workflows

### Internal workflows (`@org/repo/.github/workflows/x.yml@main`)

- Under your organization's control
- **Netresearch rule: call them at `@main`. Never pin them to a commit hash**, also not as `@<sha> # main`. They are maintained together with their callers; a hash freezes the caller on an old copy and makes Renovate open digest PRs for it. They are exempt from `sha_pinning_required`, so no ruleset needs the hash. A CodeQL `actions/unpinned-tag`, zizmor `unpinned-uses` or SonarCloud `githubactions:S7637` finding on one is a false positive: dismiss it as won't fix, never pin (`reusable-workflow-pitfalls.md`). Copy the ref form of the neighbouring callers. `validate-skill.sh` in skill-repo-skill fails a skill repo that pins one.
- Changes are visible in your org's commit history
- Trust model: same as trusting your own code

### External workflows (`@actions/*`, `@third-party/*`)

- Maintained by third parties outside your control
- **Must be SHA-pinned** to a full commit hash
- Audit before adoption -- review the workflow source and all transitive dependencies
- Subscribe to security advisories for the action's repository
- Use Dependabot or Renovate to track version updates with SHA pins

## Transitive Dependency Risks

A pinned action can internally reference other actions by tag, creating an unpinned transitive dependency chain.

### The problem

```yaml
# Your workflow: pinned to SHA -- looks secure
- uses: vendor/action@abc123def456  # v0.28

# But inside vendor/action's action.yml:
- uses: vendor/setup-tool@v0.2.1  # TAG -- not pinned!
```

If `vendor/setup-tool@v0.2.1` is compromised (tag moved to malicious commit), your workflow is vulnerable despite pinning the top-level action.

### Real-world example: trivy-action v0.28

The `aquasecurity/trivy-action@v0.28` composite action internally referenced `aquasecurity/setup-trivy@v0.2.1` by tag. A compromise of the `setup-trivy` tag would bypass the SHA pin on `trivy-action`.

### Mitigation

1. **Audit composite actions' `action.yml`** for internal `uses:` directives
2. **Prefer actions that SHA-pin their own dependencies** internally
3. **Fork and vendor** critical actions to control the full dependency chain
4. **Monitor advisories** for both the action and its transitive dependencies

## Audit Checklist for Reusable Workflows

Before adopting a new reusable workflow or action:

- [ ] **Read the source:** Review the workflow/action YAML and any scripts it runs
- [ ] **Check internal refs:** Look for `uses:` inside `action.yml` -- are they SHA-pinned?
- [ ] **Review permissions:** What `permissions` does the workflow request?
- [ ] **Check secrets access:** Does it require secrets? Which ones?
- [ ] **Verify publisher:** Is the action from a verified marketplace creator?
- [ ] **Check maintenance:** Is the repository actively maintained? Last commit date?
- [ ] **Review issues/CVEs:** Any open security issues or past incidents?
- [ ] **Test in isolation:** Run in a fork/test repo before deploying to production

### Audit internal refs of a composite action

```bash
# Download and inspect an action's internal references
gh api repos/OWNER/ACTION/contents/action.yml --jq '.content' | base64 --decode | grep 'uses:'
```

## Shared Workflow Repos Pattern

Centralized CI workflow repositories (e.g., `org/ci-workflows`, `org/skill-repo-skill`) provide consistent CI across many repos.

### Benefits

- **Consistency:** All repos use the same tested CI patterns
- **Maintenance:** Fix once, propagate everywhere via `@main` ref
- **Security:** Audit one repo instead of N copies
- **Standards:** Enforce org-wide policies (linting, testing, signing)

### Maintenance considerations

- **Breaking changes:** Updates to shared workflows affect all consumers immediately (when using `@main`)
- **Versioning:** Use tags (`@v1`, `@v2`) for stability; `@main` for always-latest
- **Testing:** Test workflow changes in a fork before merging to main
- **Documentation:** Document inputs, secrets, and expected behavior for consumers
- **Access control:** Shared workflow repos should have strict branch protection

### Example structure

```
org/ci-workflows/
├── .github/workflows/
│   ├── reusable-lint.yml        # Called by consumer repos
│   ├── reusable-test.yml
│   └── reusable-release.yml
└── README.md
```

Consumer repos reference these as:

```yaml
jobs:
    lint:
        uses: org/ci-workflows/.github/workflows/reusable-lint.yml@main
        with:
            language: go
```

> **See also:** [`org-security-settings.md`](./org-security-settings.md) for org-level SHA pinning and allow-list configuration.

## Never Use `secrets: inherit`

`secrets: inherit` forwards **every** secret available to the calling workflow
into the reusable workflow — and transitively into any action it calls. One
compromised action in the chain (cf. the chain-compromise risk above) then has
access to the full secret set: Docker credentials, publish tokens, signing keys.

Pass only what each workflow needs, explicitly by name:

```yaml
# Bad — hands the whole keyring to the reusable workflow and its dependencies
jobs:
    release:
        uses: org/ci-workflows/.github/workflows/release.yml@<sha>
        secrets: inherit

# Good — least privilege; blast radius limited to the named secrets
jobs:
    release:
        uses: org/ci-workflows/.github/workflows/release.yml@<sha>
        secrets:
            CODECOV_TOKEN: ${{ secrets.CODECOV_TOKEN }}
```

Org secrets do **not** auto-propagate into reusable workflows either — each
caller must forward them explicitly, which is what makes `inherit` look
convenient. Resist it; the explicit form is also the audit trail.

## A Secret and an Untrusted Build Do Not Share a Runner

Ordering a job so the token is minted *after* the build looks like isolation
and is not. The usual shape:

```yaml
# Looks safe, is not: one job, build first, token second
- run: npm ci --ignore-scripts && npm run build    # untrusted dependency tree
- uses: actions/create-github-app-token@<sha>      # token minted "after" it
- uses: actions/github-script@<sha>                # holds Contents:write
```

Minting later closes the direct read — the build cannot `echo $TOKEN` for a
secret that does not exist yet — and nothing else. A build step can append to
`$GITHUB_ENV` and `$GITHUB_PATH`, two ordinary writable files whose contents
the runner applies to **every subsequent step**:

- A directory prepended via `$GITHUB_PATH` intercepts the `gh` that a later
  `run:` step calls with `GH_TOKEN` exported, and any other binary those steps
  invoke by name.
- Any variable a later step or action reads from the environment can be set
  the same way through `$GITHUB_ENV`.

One escalation that does **not** work is worth knowing, because it is the one
people reach for: `NODE_OPTIONS` is on the runner's block list for this file
(`_setEnvBlockList` in `src/Runner.Worker/FileCommandManager.cs`), so writing
it to `$GITHUB_ENV` is skipped with a message and never reaches the Node
actions. The route through `$GITHUB_PATH` is not blocked.

Put the build and the token in **separate jobs** and pass the product between
them as an artifact:

```yaml
jobs:
  build:                       # no application or publishing secret in scope
    runs-on: ubuntu-latest
    permissions: { contents: read }
    steps:
      - uses: actions/checkout@<sha>
        with: { persist-credentials: false }
      - run: npm ci --ignore-scripts && npm run build
      - uses: actions/upload-artifact@<sha>
        with: { name: dist, path: dist }

  publish:                     # never checks out, never runs project code
    needs: build
    runs-on: ubuntu-latest
    steps:
      - uses: actions/download-artifact@<sha>
        with: { name: dist }
      - uses: actions/create-github-app-token@<sha>
        id: app-token
        with:
          app-id: "${{ secrets.APP_ID }}"
          private-key: "${{ secrets.APP_PRIVATE_KEY }}"
          permission-contents: write     # only what the publish needs
      - uses: actions/github-script@<sha>
        with: { github-token: "${{ steps.app-token.outputs.token }}" }
```

Two details in that skeleton are the difference between the pattern and a
slogan. `persist-credentials: false` on the checkout matters because the build
job is not secret-free by default: `contents: read` still issues a
`GITHUB_TOKEN`, and `actions/checkout` writes it into `.git/config`, where the
dependency tree it is about to execute can read it. And
`create-github-app-token` mints a token carrying **every** permission the
installation grants unless `permission-*` inputs narrow it, so an unscoped
token in the publishing job hands the whole installation to whatever that job
runs.

The artifact crosses as data: the publishing job reads its bytes and never
executes them. Two properties make this worth the extra job — the build job
holds no secret worth taking once the checkout credential is off disk, and the
token job runs no code from the repository under test.

This matters most where the workflow exists precisely to merge without a human:
a rebuild-and-auto-merge job for dependency bumps is the case where the runner
should be assumed hostile, because the change that triggered it is a new
version of somebody else's code.

## Gating Your Own Shared-Workflow Repo

The sections above are about auditing **external** actions before you adopt
them. This one is about the shared-workflow repo you **own**: because consumers
reference it at `@main`, every merge ships to all of them instantly — a broken
or insecure merge propagates org-wide before anyone reviews it. Gate `main` and
every PR with more than a linter:

| Dimension | Tool | Catches |
|-----------|------|---------|
| Lint | [actionlint](https://github.com/rhysd/actionlint) | Syntax, expression/input types, shellcheck on `run:` blocks |
| Style | [yamllint](https://github.com/adrienverge/yamllint) `--strict` | YAML conformance |
| Security | [zizmor](https://docs.zizmor.sh/) | Template injection, credential persistence, token misuse, missing cooldown |
| Conformance | small repo script | README ↔ workflow-file sync, `workflow_call`-only triggers, documented inputs |

### zizmor findings you *will* hit, and the correct fix

- **`artipacked` (credential persistence):** every `actions/checkout` on a
  read-only job needs `persist-credentials: false`, or the `GITHUB_TOKEN` is
  written to `.git/config` where any later `run:` step — or a compromised
  npm/composer postinstall — can read it.

  ```yaml
  - uses: actions/checkout@<sha>
    with:
      persist-credentials: false
  ```

- **`template-injection` on `run: ${{ inputs.x }}`:** for a *flag-list* input
  (`render-flags`, `composer-args`), route it through an `env:` var so it is
  never expanded into the script text:

  ```yaml
  - env:
      RENDER_FLAGS: ${{ inputs.render-flags }}
    run: |
      # shellcheck disable=SC2086  # intended word-splitting of a flag list
      tool $RENDER_FLAGS
  ```

  For a *whole-command* input that must be shell-interpreted (`command`,
  `test-unit-command`), env indirection is impossible — the input **is** code.
  Accept it as "code by contract" (set in the caller's committed workflow, the
  same trust level as the code) with a justified inline ignore, and document the
  contract:

  ```yaml
  # Command inputs are code by contract: set in the caller's committed workflow.
  - run: ${{ inputs.command }}  # zizmor: ignore[template-injection]
  ```

  In the input `description:` and the README, state: *command inputs must be
  static literals — never pass `github.event.*` data.* That closes the one real
  injection path the ignore leaves open (a careless consumer piping a PR title
  into the input).

- **`github-app` (unscoped token):** `actions/create-github-app-token` without
  `permission-*` inputs mints a token carrying **all** of the App's granted
  permissions. Scope it to what the job needs: `permission-contents: write`,
  `permission-pull-requests: write`, etc.

### Pin the gate's own tooling

The gate is only as trustworthy as the tools it installs.

- **pip tools** — hash-lock them; don't `pip install foo==1.2.3` bare:

  ```bash
  # requirements.txt generated with: uv pip compile --generate-hashes
  pip install --require-hashes --only-binary ':all:' -r .github/requirements.txt
  ```

  Add a `pip` Dependabot ecosystem (`directory: /.github`) so the pins stay
  fresh.

- **CLI binaries** — download by pinned version and verify the checksum, failing
  closed on mismatch:

  ```bash
  curl -sSfL -o actionlint.tar.gz \
    "https://github.com/rhysd/actionlint/releases/download/v1.7.12/actionlint_1.7.12_linux_amd64.tar.gz"
  echo "<sha256>  actionlint.tar.gz" | sha256sum -c -
  tar xzf actionlint.tar.gz actionlint
  ```

  A curl-installed binary is **not** covered by Dependabot — bump its version +
  checksum by hand, and note that in a comment so it is not mistaken for
  auto-maintained. (Do **not** try to pin it via `uses: docker://IMAGE@sha256:…`
  — digest-form `docker://` refs fail workflow startup; see
  [`actionlint-guide.md`](./actionlint-guide.md).)

## Gate a SAST Check on PR-Introduced Findings, Not Ruleset Drift

A SAST step that runs with an auto-updating ruleset (Opengrep/Semgrep
`--config auto`, and similar) and is wired as a **required** merge check has a
trap: the ruleset it fetches drifts over time. Your `main` was green when it was
last scanned; the community then adds a rule; the *next* PR — even a docs-only
one — scans with the newer ruleset, finds pre-existing violations on files it
never touched, and is **blocked from merging** by them. So a contributor's PR is
held hostage by drift on code they didn't write, and it recurs on every repo
sharing the workflow, on any PR.

Two tempting "fixes" are both wrong:

- **Pin the ruleset** (drop `--config auto` for a fixed set) — stops the drift,
  but also stops auto-adoption of new rules. A security scanner that no longer
  learns new issue classes is the wrong trade.
- **Report-only** (upload findings, never fail the check) — stops the blocking,
  but now a PR that genuinely *introduces* a vulnerability sails through. Also
  unacceptable.

The shape that satisfies all three requirements — block real new issues, don't
block on drift, keep adopting new rules — is **diff/baseline-aware gating**: keep
the check blocking, but fail only on findings the PR **introduces relative to the
merge-base**, not on the repo's accumulated state.

- A real new vuln → present at the PR head, absent at baseline → **fails.**
- A pre-existing finding / drift on untouched files → present at *both* → **passes.**
- `--config auto` still pulls the latest rules, so a newly-added rule still
  catches a newly-introduced violation.

Two mechanisms:

- **Scanner baseline:** Semgrep supports `--baseline-commit <merge-base>` (fail
  only on findings introduced since that commit). **Verify the exact flag against
  the scanner you actually run** — a fork (e.g. Opengrep) may name or support it
  differently; do not assume it is identical.
- **GitHub-native:** upload the SARIF to code scanning and let the **Code
  Scanning PR check** gate — GitHub can be set to fail the check only on alerts
  **introduced by the PR**, which is diff-aware without a CLI flag.

Symptom that you have this problem: a required SAST check flips a *docs* or
otherwise-unrelated PR from green to red, and the findings are all on files the
PR never touched. To read them, list the analyses via
`repos/OWNER/REPO/code-scanning/analyses?ref=refs/pull/<PR>/merge`, take the
newest analysis `id`, then fetch that analysis's SARIF —
`gh api repos/OWNER/REPO/code-scanning/analyses/<id> -H 'Accept: application/sarif+json'`
— and inspect the result locations. Fix the reusable workflow, not the innocent PR.

## Some things should not be a reusable — the security gates are telling you

Before wrapping an action in a shared workflow, ask whether the wrapper *fights*
the org's own scanners. Two patterns that surfaced against zizmor + CodeQL:

**A reusable that runs a caller-supplied script.** A generic "ssh-deploy" that
executes `inputs.script` on a remote host is flagged by both zizmor
(*template-injection*) and CodeQL (*code injection*) — **by design**, because a
reusable input is attacker-influenceable if a caller ever wires it to an
untrusted trigger. Routing the script through `env:` (`env.X`) silences zizmor
but **not** CodeQL, which still traces `env.X ← inputs.script`. The gate is
correct: a run-arbitrary-caller-code leaf is exactly what the injection rules
exist to prevent. If the value the reusable adds is only "centralise one
infrequently-bumped action," the honest call is often to **keep the single
pinned action inline** as a documented exception rather than suppress security
alerts on a production-deploy reusable.

**Prefer the runner's `gh` CLI over wrapping a third-party release action.**
zizmor flags `softprops/action-gh-release` with *"action functionality is
already included by the runner: use `gh release` in a script step."* Rewriting
the reusable to `gh release create`/`edit` (with the notes body passed through
`env` and written via `--notes-file`) is both zizmor- and CodeQL-clean **and**
leaves **zero external actions** in the chain — the ideal end state for an
"actions live only in shared workflows" policy. General rule: if the runner
already ships a CLI that does the job (`gh`, `docker`, `cosign`), a reusable
built on that CLI beats one that pins yet another third-party action.



--- FILE: skills/github-project/references/review-policy-contract.md ---

<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->
<!-- SPDX-FileCopyrightText: Netresearch DTT GmbH -->

# Preserve the Review Policy Before Changing the Merge Process

Before a critical workflow, release, CODEOWNERS or merge-policy change, compare
the **documented policy** with the **effective enforcement on the PR's actual
base branch**. A green merge button, a team assignment and an approval record
prove different things.

## Record the contract and its enforcement

Record the source of each requirement: required number of distinct reviewers,
whether they must be humans, required qualification/team, covered paths,
current-revision approval, unresolved-thread policy, and any authorized bypass.
Do not infer this contract from a generic solo-maintainer template or copy a
weaker neighboring project's settings over an explicit project policy.

Read classic branch protection **and** effective rulesets for the actual base
([security-config.md](security-config.md#effective-branch-rules)). Resolve active
ruleset conditions, covered paths, required teams and bypass actors from their
full definitions. Record the endpoints and revision/time checked. A zero generic
approval count in one rule does not cancel a stricter team/path rule elsewhere.
A 403, ambiguous 404 or missing permission leaves enforcement unknown; it does
not prove the branch is unprotected.

For example, a policy requiring **two qualified human team members** is not met
by one generic approval, two bots, or a CODEOWNERS team with eight members and
zero actual approvals. Where the platform supports the exact team/path/count
constraint, prefer native enforcement. If it cannot enforce qualification, keep
an explicit operator gate and identify the gap; do not claim configuration alone
establishes reviewer expertise or lower the count to make a PR mergeable.

## Establish reviewer eligibility and actual approval

1. Inspect the CODEOWNERS file from the PR's **base branch**, including matching
   path precedence and syntax errors. Confirm the owner/team is valid and has
   the repository access required by GitHub. Team membership or write access is
   evidence of eligibility only; required domain qualification needs its own
   documented basis. Ask for the missing owner/qualified reviewer when needed.
2. Read submitted reviews, their author identity/type, state and commit ID. An
   author cannot approve their own PR. Count distinct eligible non-author humans
   when the project requires humans; bot reviews and automated approvals can
   supply feedback but cannot satisfy that human requirement.
3. Apply the current-revision rule from the contract. A review of an old head is
   not proof of approval of new code. Requalify after a substantive push; do not
   count dismissed reviews, comments, requested-but-unsubmitted reviews or team
   review requests as approval. Check blocking change requests and unresolved
   threads separately.
4. Before enqueue/merge, re-read the PR head and base, effective rules, approvals
   and checks. Bind the decision to those revisions. Independent agent review
   validates the patch; it does not impersonate or replace a required human.

## Guard stacked PRs on temporary branches

A child PR targeting its parent's feature branch may fall outside rulesets
limited to the default branch. It also reads CODEOWNERS from that temporary
base. Passing checks on the child do not establish default-branch protection.

Keep the child **draft** (and do not arm auto-merge or enqueue it) while its
temporary base lacks the intended policy. Record its intended final base and
the parent dependency in the body. Draft status is a concrete merge guard,
but not a substitute for native rules on the final target.

After the parent is actually merged:

1. Retarget the child to the intended protected branch; never merge it into the
   temporary parent branch just to satisfy the stack.
2. Re-read the new head/base and diff. Confirm the parent's changes are no
   longer duplicated and all intended child changes remain.
3. Recheck effective branch/path rules and CODEOWNERS, run the applicable checks
   for the retargeted diff, and obtain the contract's qualified approvals for
   the current revision. A retarget can change what reviewers must assess.
4. Mark ready only when the guarded transition is safe; enqueue/merge through
   the normal protected process once every requirement is met.

Do not repeatedly rebase or rerun every stacked PR while waiting: requalify the
actual transition and changed evidence, preserving current proofs where valid.

Sources: [CODEOWNERS and base-branch behavior](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners),
[protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches),
[available rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets).



--- FILE: skills/github-project/references/security-config.md ---

<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->
<!-- SPDX-FileCopyrightText: Netresearch DTT GmbH -->

# Security Configuration Reference

Repository security best practices: permissions, branch protection, CodeQL, signed commits, and PR merge requirements.

## Least-Privilege Workflow Permissions

All `write` permissions MUST be at **job-level** only. Workflow-level should be `read` or empty.

### Pattern: Workflow-level read, job-level write

```yaml
# CORRECT -- write at job level only
permissions:
    contents: read          # workflow-level: read only

jobs:
    release:
        permissions:
            contents: write  # job-level: narrowed to this job
        steps: ...

    read-only-job:
        permissions:
            contents: read   # job-level: explicit read
        steps: ...

# WRONG -- write at workflow level
permissions:
    contents: read
    pull-requests: write    # Too broad -- move to job level!
```

### Common Workflows That Need Fixing

| Workflow | Typical violation | Fix |
|----------|-------------------|-----|
| `pr-quality.yml` | `pull-requests: write` at top | Move to auto-approve job only |
| `release-labeler.yml` | `issues: write, pull-requests: write` at top | Move to label-release job |
| `create-release.yml` | `contents: write` at top | Move to create-release job |

> **Scorecard note:** The OpenSSF Scorecard Token-Permissions check flags workflow-level `write` permissions.

### Anti-pattern: `permissions: read-all`

`read-all` is the lazy "make Scorecard stop complaining about missing permissions" knob — but it scores **0** on the Token-Permissions check, not full marks. The check wants **explicit, per-permission scopes** so a reviewer can audit what each workflow actually needs.

```yaml
# WRONG — scores 0 on Token-Permissions
permissions: read-all

# RIGHT — explicit scopes, scores 10
permissions:
    contents: read
    # add only what's needed (e.g. pull-requests: read for label/check workflows)
```

If a workflow only reads code, just `contents: read` is enough. Add other read scopes one-by-one as steps need them. Never use `read-all` as a placeholder you mean to tighten "later" — Scorecard treats it as wide-open.

### SLSA Provenance: Use actions/attest-build-provenance (not slsa-github-generator)

`slsa-framework/slsa-github-generator` **cannot be SHA-pinned** — known unfixable limitation ([#4440](https://github.com/slsa-framework/slsa-github-generator/issues/4440), [slsa-verifier#12](https://github.com/slsa-framework/slsa-verifier/issues/12)). Its internal actions use tag refs that conflict with SHA-pinning rulesets.

**Recommended replacement:** `actions/attest-build-provenance` (v4.1.0+), fully SHA-pinnable. For SLSA Build Level 3, host the build workflow as a **reusable workflow in the org `.github` repo** (e.g., `org/.github/.github/workflows/build-go-attest.yml`). This provides true L3 isolation — callers cannot modify the build process.

Verification uses `gh attestation verify` instead of `slsa-verifier`:
```bash
gh attestation verify binary-name --repo OWNER/REPO
```

> **Immutable releases and tags:** GitHub releases are immutable. Once a release is published and deleted, the `tag_name` is permanently locked -- you cannot create a new release on the same tag. Signed tags are cryptographic commitments and must never be deleted or recreated. If a release has issues, bump the version and create a new tag.

### require_last_push_approval + Merge Queue Incompatibility

`require_last_push_approval: true` is **incompatible with merge queues** for solo-maintainer projects. The merge queue creates a new merge commit (a new "push") which dismisses the existing approval. The auto-approve bot cannot re-approve within the merge queue context, permanently blocking PRs.

**Keep `require_last_push_approval: false`** when using merge queues with auto-approve.

### Composite Action Sub-Action Allow-List Gotcha

When a GitHub org has an **Actions allow-list**, composite actions' **internal sub-actions** must ALSO be in the allow-list. Even if the top-level action is permitted (e.g. `ddev/github-action-add-on-test@*`), any `uses:` inside its `action.yaml` must independently pass the org's allow-list check.

**Symptoms:** CI fails at "Set up job" with error listing disallowed actions from inside the composite action.

**Fix options:**
1. Add the sub-actions to the org allow-list (requires org admin)
2. Inline the composite action's steps directly in your workflow using only allowed actions + shell commands
3. Fork/vendor the composite action and replace disallowed sub-actions
4. Ask the composite action's maintainer to SHA-pin its internal sub-actions, then pin the composite action itself to that commit's full SHA. Use this when the org also requires every action to be pinned to a full commit SHA: the "Set up job" error then ends with "All actions must also be pinned to a full-…", and it rejects tag- or branch-pinned sub-actions even where their owner is allow-listed (`actions/checkout@v4` against an `actions/checkout@*` entry).

**Example:** `ddev/github-action-add-on-test` internally uses `homebrew/actions/setup-homebrew@main` and `mxschmitt/action-tmate@v3` — neither is typically in org allow-lists. Solution: inline the steps (checkout + brew install via shell + bats).

**Option 4 in practice:** `TYPO3-Documentation/ddev-typo3-docs` allow-lists `ddev/github-action-add-on-test@*` and requires full-SHA pins. With the action pinned at `1a55661`, whose `action.yaml` still used `@main`, `@v3` and `@v4`, every run failed at "Set up job". Upstream then SHA-pinned all three sub-actions (`f040e6e`). After the workflow moved to that SHA, the next run passed "Set up job". Whether the org allow-list changed in between is not readable without org-admin access.

**Tip:** `ubuntu-latest` runners have Homebrew pre-installed. Instead of `homebrew/actions/setup-homebrew`, just add PATH entries:
```bash
printf "%s\n" "/home/linuxbrew/.linuxbrew/bin" "/home/linuxbrew/.linuxbrew/sbin" >> "$GITHUB_PATH"
```

## Branch Protection: Enforce for Admins

`enforce_admins` **SHOULD be `true`** on mature multi-maintainer repos as a hardening target. The [init script](repo-bootstrap.md) ships `false` as the pragmatic baseline — solo-maintainer Netresearch repos benefit from admin-bypass in emergencies (stuck required checks, ruleset races, dependency outages). Once the team has documented its emergency-merge paths and on-call coverage, tighten:

```bash
# Check current state
gh api repos/OWNER/REPO/branches/main/protection --jq '.enforce_admins.enabled'

# Enable enforce_admins (target hardening)
gh api repos/OWNER/REPO/branches/main/protection/enforce_admins -X POST

# Verify
gh api repos/OWNER/REPO/branches/main/protection --jq 'if .enforce_admins.enabled then "OK: Admin enforcement enabled" else "INFO: Admins can bypass branch protection (acceptable on solo-maintainer repos)" end'
```

> **Security note:** Even with `required_conversation_resolution: true`, admins can merge with unresolved review threads if `enforce_admins` is `false`. For repos where the bypass is the safety valve (single maintainer, no on-call), accept the trade-off and discipline-enforce the unresolved-threads check at the operator level (see [the bootstrap reference](repo-bootstrap.md) for the pre-merge GraphQL query operators should run before every `gh pr merge`). For repos with multiple maintainers, both settings should be enabled together.

## Branch Protection: Required Reviews

- **Preserve the project's documented contract first:** reviewer count, human/qualification requirements and path coverage can exceed the generic baselines below. Compare them with effective rules on the PR's actual base before changing enforcement; see [review-policy-contract.md](review-policy-contract.md). A bot approval does not satisfy a qualified-human requirement.
- **Team projects:** MUST have `required_approving_review_count >= 1`; reviews come from team members.
- **Single-maintainer projects:** choose one of the two setups in `references/auto-merge-guide.md` → "Solo Maintainer: Choose One of Two Setups":
  - **A:** `required_approving_review_count >= 1` with the `pr-quality.yml` auto-approve workflow.
  - **B:** `required_approving_review_count: 0` via `init-branch-protection.sh --solo`, keeping `required_conversation_resolution` and required status checks. GitHub does not let an author approve their own PR, so `>= 1` without A leaves only an admin bypass.

> **Scorecard note:** The OpenSSF Scorecard Branch-Protection check scores the `required_approving_review_count >= 1` setting, and the Code-Review check scores whether recently merged changes carried an approval. Setup B lowers both scores; prefer A where the Scorecard result matters.

## Repository Rulesets vs Branch Protection

Repository rulesets (newer API) offer more granular control than branch protection:

```bash
# List rulesets
gh api repos/OWNER/REPO/rulesets --jq '.[] | {id, name, enforcement}'

# Add pull_request rule to existing ruleset
gh api repos/OWNER/REPO/rulesets/RULESET_ID -X PUT --input - <<'EOF'
{
  "rules": [
    {"type": "pull_request", "parameters": {
      "required_approving_review_count": 0,
      "dismiss_stale_reviews_on_push": true,
      "required_review_thread_resolution": true
    }}
  ]
}
EOF
```

### Limitation: Cannot Block on Pending Reviews

Neither branch protection NOR rulesets can block merge when a review is **requested but not yet submitted**.

- `required_approving_review_count: 1` requires an approval (blocks always until approved, not just when pending)
- `required_review_thread_resolution: true` blocks on unresolved threads, not pending reviews
- `copilot_code_review` ruleset triggers review but doesn't block merge while reviewing

**Workaround:** GitHub Actions status check that queries pending reviewers via API and fails if any are outstanding.

## Merge Strategy & Signed Commits

For signed commits workflow (rebase locally + merge commit):

| Repository Setting | Value | Why |
|--------------------|-------|-----|
| `allow_merge_commit` | **true** | Preserves signatures on feature branch commits |
| `allow_rebase_merge` | true | GitHub requires at least one of squash/rebase |
| `allow_squash_merge` | false | Destroys individual commit signatures |

| Branch Protection | Value | Why |
|-------------------|-------|-----|
| `required_signatures` | target: `true`; [init](repo-bootstrap.md): unset | Enforces GPG/SSH signed commits. Init script omits this so Dependabot/Renovate bot PRs aren't blocked before each bot's signing flow is configured per-repo. Turn on once you've verified bot signing works: `gh api repos/OWNER/REPO/branches/main/protection/required_signatures -X POST`. Verify with `gh api repos/OWNER/REPO/branches/main/protection --jq '.required_signatures.enabled'`. |
| `required_linear_history` | **false** | Must be false - conflicts with merge commits |
| `required_conversation_resolution` | true | All review threads must be resolved before merge |

### Workflow

```bash
# 1. Developer rebases PR branch locally (signs commits)
git fetch origin && git rebase origin/main
git push --force-with-lease

# 2. Merge via merge commit (preserves signatures)
gh pr merge <number> --merge
```

### Auto-Merge Compatibility

| Merge Strategy | Works with `required_signatures`? |
|----------------|-----------------------------------|
| Merge commit | Yes - GitHub signs the merge commit |
| Rebase merge | No - GitHub cannot sign rewritten commits |
| Squash merge | No - GitHub cannot sign squashed commit |

**Important:** When enabling auto-merge, select "Create a merge commit" strategy.

For the full merge strategy guide, see `references/merge-strategy.md`.

## CodeQL Configuration

> **Deprecation:** CodeQL Action v3 will be deprecated in December 2026. Migrate all `github/codeql-action/*` references to v4. Check with:
> ```bash
> grep -r 'uses: github/codeql-action/' .github/workflows/ | grep -v '@v4'
> ```

Netresearch projects use custom CodeQL workflows (`.github/workflows/codeql.yml`). GitHub's "Default Setup" **MUST be disabled** -- they cannot coexist.

### The Problem

When both Default Setup and a custom workflow exist, CI fails with:
```
CodeQL analyses from advanced configurations cannot be processed when the default setup is enabled
```

### Required Action

**Before pushing a custom CodeQL workflow**, disable Default Setup:

```bash
# Check current state
gh api repos/OWNER/REPO/code-scanning/default-setup --jq '.state'

# Disable default setup (MANDATORY)
gh api repos/OWNER/REPO/code-scanning/default-setup -X PATCH -f state=not-configured
```

### Verification

```bash
gh api repos/OWNER/REPO/code-scanning/default-setup --jq 'if .state == "not-configured" then "OK: Default Setup disabled" else "FAIL: Default Setup still enabled - DISABLE IT" end'
```

### An `enforced` org configuration does NOT hold the per-repo toggle on

An org code-security configuration attached with `enforcement: enforced` and `code_scanning_default_setup: enabled` looks like it guarantees the scanner is on. It does not — the per-repo toggle can be off while the attachment still reads `enforced`, and nothing reports the divergence. So **org configuration state is not evidence about a repository**; query the repository.

```bash
# What the org configuration CLAIMS, per repo
gh api "orgs/ORG/code-security/configurations/ID/repositories?per_page=100" --paginate \
  --jq '.[] | [.status, .repository.name] | @tsv'

# What is actually true for one repo — the only answer that counts
gh api repos/OWNER/REPO/code-scanning/default-setup --jq '.state'
```

Measured on `netresearch` 2026-09-17: of 287 public repos, configuration 425 reported `enforced` for 278 and `failed` for 9. Among the 278 `enforced`, `simple-ldap-go`, `jira-skill`, `git-workflow-skill`, `timetracker` and `claude-code-marketplace` each reported `not-configured` at the repo endpoint — correctly so, since all five run advanced setup, which requires default setup off. A repo can therefore sit in permanent, silent contradiction with its org policy.

The `failed` status is the second thing this listing exposes: a configuration that never applied at all, so none of its settings are in force. Those 9 were in that state and nothing alarmed on it.

### An `enforced` configuration blocks per-repo changes — change a subset through a variant configuration

The reverse also holds: a setting that an `enforced` configuration declares cannot be changed at the repository. The per-repo endpoint refuses:

```text
DELETE repos/OWNER/REPO/automated-security-fixes
→ 422 An enforced security configuration prevented modifying dependabot
  security updates enablement. Contact your organization owner for details.
```

Editing the configuration itself changes every attached repository. To change one setting for a **subset**, create a variant of the configuration and attach it to that subset only:

```bash
# 1. Copy the configuration, drop the server fields, change ONE field
gh api orgs/ORG/code-security/configurations/ID > cfg.json
jq '{name: "Variant name", description: "Why it differs"}
    + (del(.id,.url,.html_url,.created_at,.updated_at,.target_type,.name,.description,.enforcement)
       | with_entries(select(.value != null)))
    | .dependabot_security_updates = "disabled"' cfg.json > cfg-new.json
NEW=$(gh api -X POST orgs/ORG/code-security/configurations --input cfg-new.json --jq .id)

# 2. Diff the created configuration against the original — GitHub fills defaults
diff <(jq -S 'del(.id,.url,.html_url,.created_at,.updated_at,.name,.description)' cfg.json) \
     <(gh api orgs/ORG/code-security/configurations/$NEW \
       | jq -S 'del(.id,.url,.html_url,.created_at,.updated_at,.name,.description)')

# 3. Canary: attach one repository, read the repository back
gh api -X POST orgs/ORG/code-security/configurations/$NEW/attach \
  --input - <<<'{"scope":"selected","selected_repository_ids":[REPO_ID]}'
gh api repos/ORG/REPO --jq .security_and_analysis.dependabot_security_updates.status

# 4. Attach the rest (repository IDs from `orgs/ORG/repos`, not `gh repo list`)
```

Four things the steps above exist for:

- The diff is not optional. Measured on `netresearch` 2026-09-24: the variant showed `dependabot_delegated_alert_dismissal` changed from `null` to `"disabled"` although the request never named it — GitHub fills its default.
- `attach` answers `{}` immediately and applies **asynchronously**. `…/configurations/$NEW/repositories` lists each repository as `attaching` and then `enforced`; 29 of 137 were listed a minute after the call. Wait until every repository reports `enforced`, then read the **repository** endpoint — the configuration status is a claim (see the section above).
- The rollback is one call: attach the original configuration to the same IDs.
- `gh repo list --json` has no numeric repository ID field; take `id` from `gh api --paginate "orgs/ORG/repos?per_page=100&type=all"`.

### A default-setup analysis with no source does not close stale alerts

When default setup runs a language for which the repository contains **no source files**, the analysis completes but records `error: "unsuccessful execution"` with `results_count: 0` and `rules_count: 0`. Such an analysis does **not** count as having re-observed the code, so existing alerts for that language are not closed — deleting the offending file does not retire the alert, and if the scanner is disabled afterwards, nothing will ever close it automatically. The honest manual close in that case is `mitigated`: removing the code is a mitigation, whereas `false positive`, `won't fix` and `used in tests` all assert something untrue about code that no longer exists.

```bash
# Why did a deletion not close the alert? Check the analysis, not the alert.
gh api "repos/OWNER/REPO/code-scanning/analyses?tool_name=CodeQL&ref=refs/heads/main&per_page=20" \
  --jq '.[] | [.created_at, .commit_sha[0:7], .category, (.results_count|tostring), (.error // "-")] | @tsv'
```

Seen on `netresearch/claude-code-marketplace`: a `/language:python` analysis ran *after* the commit that deleted the only Python file, but the repo held 0 `.py` files at that commit, so the analysis errored empty and a `py/clear-text-storage-sensitive-data` alert stayed open for eight months. It closed only once a scanner ran against a tree that actually contained Python.

### An alert whose `analysis_key` names a renamed workflow never closes on its own

GitHub supersedes alerts per `analysis_key` — the workflow path plus job id,
e.g. `.github/workflows/ci.yml:gosec` (exposed separately from `category`,
though the two often carry the same string). Rename the workflow file and new
uploads land under a *new* key; the old alerts keep theirs, nothing ever
supersedes them, and they stay open while the tool itself reports clean.
Automatic closure is what is lost — closing them by hand still works, and is
the only thing that will.

The tell is an alert whose line number no longer matches what is there, on a
tool that currently passes locally. Ask the alert directly, and compare against
**every** key the tool writes under today, not the newest one — a tool with a
matrix uploads several (`/language:go`, `/language:actions`, …) and the first
row is frequently a different job:

```bash
# the one alert, by number — not a rule filter over page 1
gh api "repos/OWNER/REPO/code-scanning/alerts/N" \
  --jq '.most_recent_instance.analysis_key'

# every key this tool currently uploads under.
# Real jq, not --jq: gh applies its built-in filter PER PAGE, so a
# `| unique` inside --jq de-duplicates each page on its own and prints the
# same key once per page. (`--slurp` does not rescue it — gh refuses to
# combine it with --jq.)
gh api "repos/OWNER/REPO/code-scanning/analyses?ref=refs/heads/main&per_page=100" --paginate \
  | jq -s '[.[][] | select(.tool.name=="TOOL") | .analysis_key] | unique[]'
```

The alert is orphaned only when its key is **absent from that whole set**. A
key that is merely not the newest says nothing — treating it as orphaned would
close a live finding, which is the expensive direction of this mistake. Once
absent is established, close it by hand and put the reason in the comment.

Seen on `netresearch/ldap-selfservice-password-changer`: four `gosec` G115
alerts sat under `.github/workflows/check.yml:gosec` while every run since the
rename uploaded to `.github/workflows/ci.yml:gosec`. `gosec ./...` had exited 0
for months, and the code carried reviewed `#nosec` justifications.

### A repository that only PUBLISHES the reusable CodeQL workflow is scanned by default setup

The rule above — default setup off, custom workflow on — applies to
*consumers*. The repository that **hosts** the reusable workflow often calls it
nowhere, so it has no advanced setup of its own and default setup stays on:
`code-scanning/default-setup` reads `state: configured`.

That matters the moment the reusable workflow carries analysis configuration,
because **default setup reads none of it**. A `config:` block, `query-filters`,
`paths-ignore` — all of it reaches consumers and none of it reaches the hosting
repository's own alerts.

```bash
# In the repo that publishes the reusable workflow, ask BOTH:
gh api repos/ORG/.github/code-scanning/default-setup --jq '.state'

# does it run CodeQL on itself at all — via the reusable OR directly?
grep -rnE 'uses:[[:space:]]*[^[:space:]]*/codeql\.yml@|uses:[[:space:]]*github/codeql-action/' \
  .github/workflows/
```

Measured on `netresearch/.github` 2026-09-20: adding a `query-filters` exclusion
to the reusable `codeql.yml` took a consumer repository from 14 open
`actions/unpinned-tag` alerts to 0, while the publishing repository stayed at 24
— it scans itself through default setup, which ignored the filter entirely.

### Scorecard `PinnedDependenciesID` flags every `@main` org reusable

Scorecard's Pinned-Dependencies check treats every `uses:` line without a commit
SHA alike, the organisation's own `netresearch/*` reusables at `@main`
included. Its [check documentation](https://github.com/ossf/scorecard/blob/main/docs/checks.md#pinned-dependencies)
speaks of workflows "used in building and releasing your project", but the
alerts below also hit workflows that build nothing (`lint.yml`, `labeler.yml`,
`auto-merge-deps.yml`). The documentation names no exception for first-party
actions or reusable workflows, so each new reusable call raises a new alert. Under the `@main` policy these alerts are
false positives: dismiss them as `won't fix`, never pin.

Measured 2026-10-22: 40 `PinnedDependenciesID` alerts dismissed that day in
`skill-repo-skill`, `git-workflow-skill` and `github-project-skill`. Read at
each alert's commit, 39 were a `netresearch/*` reusable at `@main`; one was an
`npm install -g` pin, which is a different finding.

There is no per-path or per-dependency exclusion to configure instead.
`scorecard-action` has no input for it, and Scorecard's
[maintainer annotations](https://github.com/ossf/scorecard/blob/main/config/README.md)
(`scorecard.yml`) attach a reason to a whole check, not to a path or a
dependency. Their documentation says they give users "additional information"
and does not say that they change the score or the code-scanning alerts.

### Dismissal comments are capped at 280 characters here too

`PATCH /repos/OWNER/REPO/code-scanning/alerts/N` rejects a `dismissed_comment` over 280 characters with HTTP 422, exactly like the Dependabot endpoint ([`dependency-management.md`](dependency-management.md)) — but the reason enum is different: `false positive`, `won't fix`, `used in tests`, `mitigated` (with spaces, not underscores). The membership is not guesswork: sending an invalid value returns a 422 that lists all four, which is the cheapest way to check an enum you are unsure about.

### Supported Languages — PHP Is NOT Supported

CodeQL does **not** support PHP (as of 2026; tracked in [community discussion #158392](https://github.com/orgs/community/discussions/158392)). On a PHP/TYPO3 repo, the only languages worth scanning are:

- `javascript-typescript` — covers JS, TS, and JSX/TSX in `Resources/Public/JavaScript/` and similar
- `actions` — scans `.github/workflows/*.yml` for misconfigurations

A PHP-only repo with neither JS nor non-trivial workflows has **nothing CodeQL can scan** — disabling Default Setup and skipping the custom workflow is correct.

```yaml
# .github/workflows/codeql.yml — PHP/TYPO3 repo
strategy:
  matrix:
    language: [javascript-typescript, actions]   # NOT 'php'
```

If you list `php` in the matrix, the workflow fails at the `init` step with "Unrecognised language: php". If you list `javascript` (the old name), CodeQL Action v3+ rejects it — use `javascript-typescript`.

## Required Reviews from All Requested Reviewers (MANDATORY)

PRs must **not be merged until all requested reviewers have submitted their review**. This includes human reviewers and automated reviewers (e.g., GitHub Copilot). Do not merge while any reviewer's status is still "PENDING".

> **Note:** GitHub branch protection only enforces a *minimum* approval count, not "all requested reviewers must respond." This rule is enforced as a **workflow policy** -- agents and humans must verify before merging.

### Check Reviewer Status Before Merging

```bash
# List all requested reviewers and their review state
gh pr view NUMBER --repo OWNER/REPO --json reviewRequests,reviews --jq '{
  pending: [.reviewRequests[].login],
  completed: [.reviews[] | {user: .author.login, state: .state}]
}'

# GraphQL: full reviewer status (requested + completed)
gh api graphql -f query='query($owner:String!,$repo:String!,$pr:Int!){
  repository(owner:$owner,name:$repo){pullRequest(number:$pr){
    reviewRequests(first:20){nodes{requestedReviewer{...on User{login}...on Bot{login}}}}
    reviews(last:20){nodes{author{login}state}}
  }}
}' -f owner=OWNER -f repo=REPO -F pr=NUMBER --jq '.data.repository.pullRequest | {
  awaiting: [.reviewRequests.nodes[].requestedReviewer.login],
  reviews: [.reviews.nodes[] | {user: .author.login, state: .state}]
}'
```

If `awaiting` is non-empty, the PR is **not ready to merge** -- those reviewers haven't responded yet.

## Required Conversation Resolution

All review threads on a PR **must be resolved** before merging. Combined with `enforce_admins: true`, this ensures unresolved review threads block **ALL** merges, including those by admins.

```bash
# Enable
gh api repos/OWNER/REPO/branches/main/protection -X PUT \
  --input - << 'EOF'
{
  ...existing settings...,
  "required_conversation_resolution": true
}
EOF

# Verify both conversation resolution AND admin enforcement
gh api repos/OWNER/REPO/branches/main/protection --jq '{
  conversation_resolution: .required_conversation_resolution.enabled,
  enforce_admins: .enforce_admins.enabled
} | if .conversation_resolution and .enforce_admins then "OK: Review threads enforced for all users"
  elif .conversation_resolution then "PARTIAL: Conversation resolution enabled but admins can bypass (enable enforce_admins)"
  else "FAIL: Conversation resolution NOT required - ENABLE IT" end'

# List unresolved threads
gh api graphql -f query='query($owner:String!,$repo:String!,$pr:Int!){
  repository(owner:$owner,name:$repo){pullRequest(number:$pr){
    reviewThreads(first:50){nodes{id isResolved comments(first:1){nodes{body}}}}
  }}
}' -f owner=OWNER -f repo=REPO -F pr=NUMBER --jq '.data.repository.pullRequest.reviewThreads.nodes[] | select(.isResolved == false) | {id, body: .comments.nodes[0].body}'

# Resolve a thread
gh api graphql -f query='mutation($id:ID!){resolveReviewThread(input:{threadId:$id}){thread{isResolved}}}' -f id=THREAD_NODE_ID
```

## CI Annotations

CI checks can **PASS** while emitting warning annotations (e.g., actionlint/shellcheck via reviewdog, CodeQL deprecation notices). Always check before declaring a PR clean.

```bash
# Find check runs with annotations
gh api "repos/OWNER/REPO/commits/SHA/check-runs" \
  --jq '.check_runs[] | select(.output.annotations_count > 0) | {name: .name, id: .id, annotations: .output.annotations_count}'

# View specific annotations
gh api repos/OWNER/REPO/check-runs/CHECK_RUN_ID/annotations \
  --jq '.[] | {message, annotation_level, path, start_line}'
```

**Prevention:** Configure reviewdog actions with `fail_level: error` (not deprecated `fail_on_error` + `level`).

## PR Merge Checklist

| # | Prerequisite | How to check |
|---|-------------|--------------|
| 1 | All CI checks pass | `gh pr checks NUMBER` |
| 2 | No CI annotations | Check annotations via API (see above) |
| 3 | All requested reviewers responded | `gh pr view NUMBER --json reviewRequests` must be empty |
| 4 | All review threads resolved | GraphQL reviewThreads query |
| 5 | Branch rebased on target | `gh pr view NUMBER --json mergeStateStatus` is `CLEAN` |

## Secret Scanning: A Config File Replaces the Ruleset

gitleaks does **not** merge your config with its built-in rules. A
`.gitleaks.toml` that declares only an allowlist declares *no rules at all*, and
the scan then matches nothing — reporting `no leaks found` for every input,
including a live credential sitting in the diff.

```toml
# Without this block, everything below replaces the defaults
# instead of extending them.
[extend]
useDefault = true

[allowlist]
paths = ['''testdata/''']
```

The failure is invisible by construction: a scanner that finds nothing looks
exactly like a clean repository. A green secret-scanning check is therefore not
evidence of anything until you have seen it fail once.

**Verify by planting one.** Write a value matching a rule you expect to fire
into a scratch file **outside the repository** and confirm the scan reports it:

```bash
# Assemble the probe so no secret-shaped literal is ever committed.
printf 'token = "%s-1234567890-abcdefghijklmnopqrstuvwx"\n' 'xoxb' \
  > /tmp/leak-probe.txt
gitleaks dir /tmp --no-banner        # expect: leaks found: 1
```

Keep the probe out of the repository, and out of the documentation too:
GitHub's push protection scans what you push and will **block a commit that
merely documents a realistic-looking token** — including a page explaining how
to test secret scanning. The block is correct behaviour; work around it by
assembling the value at runtime rather than by requesting an exemption.

Three traps when testing:

- **Well-known example credentials are allowlisted upstream.** AWS's
  `AKIAIOSFODNN7EXAMPLE` and friends will not be reported no matter what.
  Use a value that is not in anyone's allowlist.
- **gitleaks auto-discovers a config in the scanned directory.** Copying the
  repo's `.gitleaks.toml` next to the probe file silently re-applies the config
  you were trying to test without.

Also distinguish the two scan modes: `gitleaks dir` scans the working tree,
`gitleaks git` scans history. A repo can be clean on disk and still carry a
credential in a commit from months ago — and replacing the file does not remove
it from history, so a leaked credential still needs rotating.

## OpenSSF Scorecard Quick Reference

If your Scorecard score is low, check these common issues:

| Scorecard Check | Requirement | Reference |
|----------------|-------------|-----------|
| Token-Permissions | No workflow-level `write` permissions | See "Least-Privilege Workflow Permissions" above |
| Branch-Protection | `required_approving_review_count >= 1` | See "Branch Protection: Required Reviews" above |
| Pinned-Dependencies | All actions pinned to full SHA | Pin with `uses: action@SHA # vX.Y.Z` comment. Use `pin-github-action` tool for batch pinning (see [`org-security-settings.md`](./org-security-settings.md)). Note: composite action sub-actions must also be pinned/allowed (see [Composite Action Sub-Action Allow-List Gotcha](#composite-action-sub-action-allow-list-gotcha)). For transitive dependency risks, see [`reusable-workflow-security.md`](./reusable-workflow-security.md). |
| Code-Review | PRs reviewed before merge | Auto-approve + `required_approving_review_count >= 1` satisfies this |
| SAST | Static analysis enabled | CodeQL workflow (see above) |

## GitHub Security API: Scripting Gotchas

Endpoint quirks when scripting repo security settings, verified against the GitHub REST spec (source: [AriESQ/gh-safe-repo](https://github.com/AriESQ/gh-safe-repo)). For the bootstrap commands these annotate, see [`repo-bootstrap.md`](repo-bootstrap.md) § Actions & Security Hardening.

- **`PATCH /repos/{o}/{r}` can 404 immediately after `POST /user/repos`.** Repo creation is eventually consistent — the object exists but isn't routable for settings updates for a brief window. Retry the PATCH with backoff (e.g. 1s/2s/4s) when it directly follows a create; standalone PATCHes don't need it.
- **"Enabled?" probe status is not uniformly 204.** `GET .../vulnerability-alerts` returns **204** when enabled, but `GET .../private-vulnerability-reporting` and `GET .../automated-security-fixes` return **200**. Test the **2xx range** (`200 <= status < 300`), not `== 204`, or the probe is wrong for half the endpoints.
- **`secret_scanning_push_protection` is silently ignored unless `secret_scanning` is in the same PATCH.** Send both keys in the `security_and_analysis` body together.
- **Grouped security updates, automatic dependency submission, and dependency graph have no per-repo REST API.** They exist only as org-level code-security configuration fields (`/orgs/{org}/code-security/configurations`) and in the UI. A `PATCH /repos security_and_analysis` with `dependency_graph_autosubmit_action` returns 200 but is silently ignored. For per-repo grouped security updates use `dependabot.yml` groups (see [`dependency-management.md`](dependency-management.md)).
- **Free-plan private repos 403 on all ruleset / Dependabot / secret-scanning APIs** — you can't even `GET .../rulesets`. Public repos and paid plans (the Netresearch org) are unaffected.

## SonarCloud: automatic analysis reads `.sonarcloud.properties`, not `sonar-project.properties`

Exclusions placed in `sonar-project.properties` are **silently inert** under
automatic analysis — the mode every Netresearch repository uses, since none runs
a scanner in CI. Per the SonarQube Cloud docs: *"If you import a project that
already contains a `sonar-project.properties` file, SonarQube Cloud will ignore
the parameters in your `sonar-project.properties` file."* That file is what a
**CI-run scanner** reads; automatic analysis reads `.sonarcloud.properties` on
the default branch.

The failure is quiet and looks like a code problem. One repo carried

```properties
sonar.exclusions=data/**
sonar.cpd.exclusions=data/**
```

in `sonar-project.properties` for months while the duplication gate kept failing
on exactly those files — 50 % on one PR, 91.5 % on the next, against a 3 %
threshold — and both had to be merged with a red gate. Renaming the file (same
two settings, byte-identical) moved the project from 40 analysed files to 32,
and duplicated lines from 2188 to 0.

```bash
# Are exclusions set server-side instead? (empty result = nothing configured)
curl -fsSL "https://sonarcloud.io/api/settings/values?component=KEY&keys=sonar.exclusions,sonar.cpd.exclusions" \
  | jq '.settings'
# Which files does Sonar actually analyse? Grep the paths you meant to exclude.
curl -fsSL "https://sonarcloud.io/api/components/tree?component=KEY&qualifiers=FIL&ps=500" \
  | jq -r '.components[].path' | grep '^data/'
```

Diagnose in that order — a *present* `sonar-project.properties` plus *empty*
server-side settings plus the excluded paths still showing up in the file tree
is the signature. Do not reshape the diff to satisfy the gate: fixture data,
generated files and database seeds are duplicated by design. If the project ever
switches to a CI-run scanner, the file has to be renamed back.

## SonarCloud Quality Gate: PR (new code) vs Branch (overall)

A PR can pass SonarCloud's **new-code** quality gate (0 new issues) yet turn the
**default-branch** gate **red after merge** — the two gates evaluate different
conditions. The branch gate adds conditions the PR analysis doesn't, most often
`new_security_hotspots_reviewed` (must be **100%**) and overall coverage.

- **Security Hotspots need *reviewing*, not fixing.** They are security-sensitive
  code flagged for a human to mark **Safe** / **Fixed** in the SonarCloud UI (or
  via `POST api/hotspots/change_status`). An unreviewed hotspot fails the gate even
  though it is not a bug.
- **The offenders are frequently pre-existing**, in files the PR never touched
  (e.g. `curl | bash`, shell `[ ]`, a regex). Don't assume the merged PR caused it
  — confirm against the hotspot list first.

```bash
# which branch-gate condition failed
curl -fsSL "https://sonarcloud.io/api/qualitygates/project_status?projectKey=KEY&branch=main" \
  | jq '.projectStatus.conditions[]? | select(.status != "OK")'
# the to-review hotspots (verify before blaming the merge)
curl -fsSL "https://sonarcloud.io/api/hotspots/search?projectKey=KEY&branch=main&status=TO_REVIEW&ps=30" \
  | jq -r '.hotspots[]? | "\(.component | sub(".*:"; "")):\(.line // "?") \(.securityCategory // "")"'
```

## Effective Branch Rules

Reading what a branch actually enforces, and auditing whether a required check
can fail.

### Two rule sources, and only one of them is obvious

A branch can be governed by **classic branch protection** and by **rulesets**
at the same time. GitHub composes them and applies the most restrictive result.
The classic endpoint cannot see rulesets, so reading it alone reports a branch
as unprotected that is in fact fully gated:

```bash
# Classic protection — returns real values, but is BLIND to rulesets
gh api repos/OWNER/REPO/branches/main/protection

# Rulesets — the effective rules from every active ruleset on the branch
gh api repos/OWNER/REPO/rules/branches/main
```

Observed on a repository where both were configured:

| Field, classic endpoint | Reads as | Reality (rulesets) |
|---|---|---|
| `required_status_checks: null` | nothing is required | 23 required contexts |
| `required_approving_review_count: 0` | no review required | 1 required approval |
| `required_conversation_resolution: true` | correct | also required |
| `enforce_admins: false` | correct | plus per-ruleset bypass actors |

The two failure shapes are asymmetric and both are bad:

- **`null` reads as "not configured".** `required_status_checks` is absent from
  the classic payload entirely when a ruleset supplies the checks.
- **`0` reads as a real answer.** `required_approving_review_count: 0` is the
  *classic* setting, not the effective one. Nothing in the response says a
  ruleset requires 1.

A compliance document was written off the classic endpoint alone and attested
that the repository required neither review nor status checks. Both statements
were false, and nothing in the response hinted at it.

**Read both. When they disagree, the effective answer is the more restrictive
one.** Name which endpoint a claim came from whenever the claim lands in a
document, an issue or a PR body.

### Bypass actors live on the ruleset, not on the branch

`enforce_admins` covers classic protection only. Rulesets carry their own list:

```bash
gh api repos/OWNER/REPO/rulesets/RULESET_ID \
  --jq '{name, enforcement, bypass: [.bypass_actors[]? | {actor_type, actor_id, bypass_mode}]}'
```

`bypass_mode: always` lets the actor push straight past the rule;
`pull_request` lets it merge a pull request that does not satisfy it. The REST
API returns `actor_id` as a number and does not resolve it to a role name — say
"repository role id 5" rather than guessing "admin" unless you resolved it.

### Auditing whether a required check can actually fail

A context being in the required list does not mean it gates anything.

### A required check that is always skipped enforces nothing

```bash
gh api "repos/OWNER/REPO/commits/SHA/check-runs?per_page=100" \
  --jq '.check_runs[] | "\(.conclusion // .status)\t\(.name)"' | sort -u
```

Cross-check every required context against that list. A context whose
conclusion is `skipped` on every commit is a requirement that no state of the
code can violate. Observed case: `fuzz / Fuzz Tests` was required and always
skipped, because the job that produced it passed no inputs to its reusable
workflow and the suite defaulted to off. The job that actually ran the suite was
a different context and was not required at all.

### Check-run names come from the JOB name, not the workflow

Two jobs calling the same reusable workflow produce check-runs under
**different** prefixes, because the prefix is the calling job's name:

```yaml
# .github/workflows/checks.yml
jobs:
  fuzz:            # -> "fuzz / Fuzz Tests"
    uses: org/reusables/.github/workflows/fuzz.yml@main

# .github/workflows/ci.yml
jobs:
  fuzz-mutation:   # -> "fuzz-mutation / Fuzz Tests"
    uses: org/reusables/.github/workflows/fuzz.yml@main
    with: { run-fuzz-tests: true }
```

The two names look interchangeable and are not. Do not infer which workflow
emits a context — measure it:

```bash
for id in $(gh run list --repo OWNER/REPO --commit SHA --limit 30 --json databaseId --jq '.[].databaseId'); do
  wf=$(gh api repos/OWNER/REPO/actions/runs/$id --jq .path)
  gh api "repos/OWNER/REPO/actions/runs/$id/jobs?per_page=100" --jq '.jobs[].name' \
    | sed "s|^|$(basename "$wf")\t|"
done | sort -u
```

### A gate job is only worth requiring if it reads its own `needs`

Requiring one aggregate context instead of many is a good pattern — it makes a
job that is missing from `gate.needs` the only failure mode, rather than a
silent coverage loss. It is only sound if the gate actually evaluates its
dependencies:

```yaml
- name: Fail unless every job succeeded or was skipped
  env:
    RESULTS: ${{ toJSON(needs) }}
  run: |
    bad=$(jq -r 'to_entries[] | select(.value.result != "success" and .value.result != "skipped") | "\(.key)=\(.value.result)"' <<<"$RESULTS")
    [ -z "$bad" ] || { echo "::error::gate failed — $bad"; exit 1; }
```

Read the gate's steps before requiring it. A job with `if: always()` and no
result evaluation is a green rubber stamp, and requiring it would be worse than
requiring nothing. Treating `skipped` as passing is deliberate: jobs skipped by
an event gate must not block the merge queue.

A gate that narrows this — allowing `skipped` only for named jobs, so that a
scanner which silently skipped fails the gate — must still allow the shared
workflows that skip themselves. In `netresearch/.github`, `betterleaks.yml` and
`zizmor.yml` skip on `merge_group`, having scanned the same commits on the pull
request; `dependency-review.yml` runs on `pull_request` only and skips on every
other event, including `push` and `schedule`. Allow each skip on exactly those
events. The keys of `needs`
are the job IDs in YOUR workflow that call those reusables — `betterleaks`,
`zizmor` and `dependency-review` in the `skill` and `php-module` templates, as
below; a repository that
named them differently uses its own. Add the clause as one more `or` beside the
exceptions your gate already has:

```yaml
- name: Fail unless every job succeeded or skipped where allowed
  env:
    RESULTS: ${{ toJSON(needs) }}
    EVENT_NAME: ${{ github.event_name }}
  run: |
    jq -e --arg event "$EVENT_NAME" '
      length > 0 and all(to_entries[];
        .value.result == "success" or
        (.key | IN("betterleaks", "zizmor")) and $event == "merge_group" and .value.result == "skipped" or
        .key == "dependency-review" and $event != "pull_request" and .value.result == "skipped"
      )' <<< "$RESULTS"
```

Without the `merge_group` exception the gate passes every pull request and
fails every queue run, so nothing can merge through the queue; without the
`dependency-review` one it also fails every push to the default branch. Observed 2026-10-23 on
netresearch/typo3_http_guard: the queue ejected #25 fifteen times until #26
added the exception.

### Before changing a required-context list

1. Back up the ruleset: `gh api repos/OWNER/REPO/rulesets/ID > backup.json`.
2. Confirm every context you are about to require reports on `merge_group`, not
   only on `pull_request` — requiring a context the queue never produces wedges
   the queue for everyone.
3. Apply with `gh api -X PUT repos/OWNER/REPO/rulesets/ID --input new.json`.
4. Read the effective list back from `rules/branches/BRANCH` and confirm the
   next pull request reports every newly required context.

Removing a workflow, or removing or renaming a job in it (for a reusable: the
calling job's ID, or the `name:` of the job inside the reusable, which renames
the context in every calling repository at once), changes the list too, whether or not you touch the ruleset.
Before the change merges, read the required contexts of every repository that
runs the workflow — the ruleset and the classic branch protection
(`branches/BRANCH/protection/required_status_checks`), since either can hold
them — and replace each context that disappears with its successor in the same
step. The classic-protection endpoint answers 404 to a token without admin
rights on the repository, which reads exactly like "nothing required"; read it
with an admin token. A required context that never reports again wedges the queue;
one dropped without a successor silently removes the requirement. Observed
2026-10-23 when CodeQL moved into `security.yml`: in
netresearch/typo3-site-conformance-skill the dropped `Analyze (actions)` left
no security check required until `All security checks` was added.



--- FILE: skills/github-project/references/sub-issues.md ---

<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->
<!-- SPDX-FileCopyrightText: Netresearch DTT GmbH -->

# Sub-Issues Reference

GitHub's sub-issues feature enables parent-child relationships between issues, supporting up to 8 levels of hierarchy and 100 sub-issues per parent. This replaced the deprecated tasklists feature (sunset April 2025).

**Important:** The `gh` CLI does not support sub-issues directly. You must use the GraphQL API.

## Creating Sub-Issues

**Step 1: Create the issues normally**
```bash
# Create parent issue
gh issue create --title "Parent feature request" --body "Main tracking issue"
# Returns: https://github.com/owner/repo/issues/100

# Create child issues
gh issue create --title "Sub-task 1" --body "First sub-task"
# Returns: https://github.com/owner/repo/issues/101

gh issue create --title "Sub-task 2" --body "Second sub-task"
# Returns: https://github.com/owner/repo/issues/102
```

**Step 2: Get issue node IDs (required for GraphQL)**
```bash
gh api graphql -f query='
{
  repository(owner: "OWNER", name: "REPO") {
    parent: issue(number: 100) { id }
    child1: issue(number: 101) { id }
    child2: issue(number: 102) { id }
  }
}'
```

Output:
```json
{
  "data": {
    "repository": {
      "parent": { "id": "I_kwDOXXXXXX" },
      "child1": { "id": "I_kwDOYYYYYY" },
      "child2": { "id": "I_kwDOZZZZZZ" }
    }
  }
}
```

**Step 3: Link sub-issues to parent**
```bash
# Add first sub-issue
gh api graphql -f query='
mutation {
  addSubIssue(input: {
    issueId: "I_kwDOXXXXXX",
    subIssueId: "I_kwDOYYYYYY"
  }) {
    issue { number title }
    subIssue { number title }
  }
}'

# Add second sub-issue
gh api graphql -f query='
mutation {
  addSubIssue(input: {
    issueId: "I_kwDOXXXXXX",
    subIssueId: "I_kwDOZZZZZZ"
  }) {
    issue { number title }
    subIssue { number title }
  }
}'
```

## Querying Sub-Issues

**List all sub-issues of a parent:**
```bash
gh api graphql -f query='
{
  repository(owner: "OWNER", name: "REPO") {
    issue(number: 100) {
      number
      title
      subIssues(first: 50) {
        nodes {
          number
          title
          state
        }
        totalCount
      }
    }
  }
}'
```

**Get parent of a sub-issue:**
```bash
gh api graphql -f query='
{
  repository(owner: "OWNER", name: "REPO") {
    issue(number: 101) {
      number
      title
      parent {
        number
        title
      }
    }
  }
}'
```

## Removing Sub-Issues

```bash
gh api graphql -f query='
mutation {
  removeSubIssue(input: {
    issueId: "I_kwDOXXXXXX",
    subIssueId: "I_kwDOYYYYYY"
  }) {
    issue { number }
    subIssue { number }
  }
}'
```

## Best Practices

| Practice | Rationale |
|----------|-----------|
| Use parent as tracking/meta issue | Provides overview and progress tracking |
| Add "tracking" label to parent | Identifies meta-issues in issue lists |
| Keep hierarchy ≤3 levels | Deeper hierarchies become hard to manage |
| Reference upstream PRs in body | Link to external sources for context |
| One sub-issue per distinct feature | Enables independent progress and assignment |

## Sub-Issues Behavior

- **Inheritance**: Sub-issues inherit Project and Milestone from parent by default
- **Cross-org support**: Sub-issues can belong to different organizations than parent
- **Progress tracking**: Parent issue shows completion percentage in GitHub UI
- **Limits**: Maximum 100 sub-issues per parent, 8 levels of nesting

## Migration from Tasklists

Tasklists were sunset April 30, 2025. To convert old tasklist items:

1. Identify issues with tasklist markdown (`- [ ] #123`)
2. Create sub-issue relationships using GraphQL API above
3. Remove tasklist markdown from issue body (or leave as reference)

## Quick Reference

```bash
# Get issue node ID
gh api graphql -f query='{repository(owner:"OWNER",name:"REPO"){issue(number:123){id}}}'

# Add sub-issue (requires node IDs)
gh api graphql -f query='mutation{addSubIssue(input:{issueId:"PARENT_ID",subIssueId:"CHILD_ID"}){issue{number}subIssue{number}}}'

# List sub-issues
gh api graphql -f query='{repository(owner:"OWNER",name:"REPO"){issue(number:123){subIssues(first:50){nodes{number title state}}}}}'

# Remove sub-issue
gh api graphql -f query='mutation{removeSubIssue(input:{issueId:"PARENT_ID",subIssueId:"CHILD_ID"}){issue{number}}}'
```



--- FILE: skills/github-project/references/tag-validation.md ---

<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->
<!-- SPDX-FileCopyrightText: Netresearch DTT GmbH -->

# Tag-Version Validation Reference

**Purpose:** Document patterns for validating that version tags match in-repo version files, working around GitHub.com's lack of server-side pre-receive hooks.

## The Problem

GitHub.com (cloud) does not support custom **pre-receive hooks** — those are only available on GitHub Enterprise Server. This means you cannot reject a tag push server-side based on custom validation logic (e.g., checking that a tag matches a version file).

## Defense-in-Depth Pattern

Use three layers of protection:

1. **Local git hook** (pre-push) — catches mistakes before they leave the developer's machine
2. **CI lint validation** — catches anything that slips through (force-push, web UI tag creation, etc.)
3. **Release workflow validation** — final gate before packaging/publishing

```
Developer                     GitHub
    │                            │
    ├─ bump version file         │
    ├─ git commit -S             │
    ├─ git tag -s v1.2.3         │
    ├─ git push --tags           │
    │   └─ pre-push hook ─ FAIL  │  ← Layer 1: Local gate
    │      "version mismatch"    │
    │                            │
    ├─ fix version, amend, push  │
    │   └─ pre-push hook ─ PASS ─┼─► tag pushed
    │                            │
    │                            ├─ Lint workflow (tag trigger)
    │                            ├─ Validate version ─ PASS  ← Layer 2: CI safety net
    │                            │
    │                            ├─ Release workflow (tag trigger)
    │                            ├─ Validate version ─ PASS  ← Layer 3: Release gate
    │                            └─ Package & publish
```

### Critical: Never Bump Versions in Release Workflows

The release workflow must **only validate**, never bump version files:

- The signed tag already points at a specific commit
- Bumping the version file after tagging creates a **new commit** that the tag does NOT point to
- The tag would then reference a commit with the wrong version — defeating the purpose
- Correct flow: bump version → commit → sign tag → push → release validates and packages

## Local Pre-Push Hook

Generic pattern for any project with a version file:

```bash
#!/usr/bin/env bash
set -euo pipefail

# Find semver tags at HEAD (with or without v prefix), normalize to bare version
TAGS=$(git tag --points-at HEAD | sed -nE 's/^v?([0-9]+\.[0-9]+\.[0-9]+)$/\1/p' || true)
[[ -z "${TAGS}" ]] && exit 0

# Extract version from your version file (adapt sed pattern per project)
FILE_VERSION=$(sed -nE "s/.*'version'[[:space:]]*=>[[:space:]]*'([^']+)'.*/\1/p" version-file.ext)

if [[ -z "${FILE_VERSION}" ]]; then
    echo "ERROR: Could not extract version from version-file.ext"
    exit 1
fi

# Check if file version matches any of the tags at HEAD
if ! echo "${TAGS}" | grep -qFx "${FILE_VERSION}"; then
    echo "ERROR: version file (${FILE_VERSION}) does not match any semver tag at HEAD"
    echo "Tags found at HEAD:"
    echo "${TAGS}"
    exit 1
fi
```

### Hook Installation Methods

#### direnv + `core.hooksPath` (no dependencies)

For repos without Node.js or PHP tooling. Uses `Build/hooks/` directory with direnv auto-setup:

**`Build/hooks/pre-push`:**

```bash
#!/usr/bin/env bash
"$(dirname "$0")/../Scripts/check-plugin-version.sh"
```

**`.envrc`:**

```bash
# Install git hooks for version validation
git config core.hooksPath Build/hooks
```

Developers run `direnv allow` once — hooks are active automatically on every `cd` into the project.

#### CaptainHook (PHP projects)

```json
{
    "pre-push": {
        "enabled": true,
        "actions": [
            { "action": "Build/Scripts/check-tag-version.sh" }
        ]
    }
}
```

#### Husky (Node.js projects)

**`.husky/pre-push`:**

```bash
#!/usr/bin/env sh
Build/Scripts/check-tag-version.sh
```

## CI Lint Validation Step (GitHub Actions)

Add to `lint.yml` with `tags: ['v*']` trigger. Runs on every tag push as a safety net:

```yaml
  version:
    name: Plugin Version
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7
      - name: Validate version file matches tag
        run: |
          # Adapt extraction per ecosystem (see table below)
          FILE_VERSION=$(sed -nE "s/.*'version'[[:space:]]*=>[[:space:]]*'([^']+)'.*/\1/p" version-file.ext)
          if [[ -z "${FILE_VERSION}" ]]; then
            echo "::error file=version-file.ext::Could not extract version from version-file.ext"
            exit 1
          fi
          # On tag push, verify tag matches version file
          if [[ "$GITHUB_REF" == refs/tags/v* ]]; then
            TAG_VERSION="${GITHUB_REF#refs/tags/v}"
            if [[ "${TAG_VERSION}" != "${FILE_VERSION}" ]]; then
              echo "::error file=version-file.ext::Tag v${TAG_VERSION} does not match version file ${FILE_VERSION}"
              exit 1
            fi
            echo "Version match confirmed: v${TAG_VERSION}"
          else
            # Non-tag push: just validate format
            echo "Version format valid: ${FILE_VERSION}"
          fi
```

## Release Workflow Validation (GitHub Actions)

Add **before** any packaging/publish step in the release workflow. This is the final gate — validation only:

```yaml
      - name: Validate version file matches tag
        env:
          TAG_VERSION: ${{ github.ref_name }}
        run: |
          # Adapt extraction command per ecosystem (see table below)
          FILE_VERSION=$(python3 -c "import json; print(json.load(open('.claude-plugin/plugin.json'))['version'])")
          TAG_BARE="${TAG_VERSION#v}"
          if [[ "${TAG_BARE}" != "${FILE_VERSION}" ]]; then
            echo "::error file=.claude-plugin/plugin.json::Tag ${TAG_VERSION} does not match version file ${FILE_VERSION}"
            exit 1
          fi
          echo "Version validated: ${TAG_VERSION} matches ${FILE_VERSION}"
```

**Important:** Use `env:` to pass `github.ref_name` — never interpolate `${{ }}` directly in `run:` blocks (script injection risk).

## Common Version File Patterns

| Ecosystem | File | Extraction |
|-----------|------|------------|
| TYPO3 | `ext_emconf.php` | `sed -nE "s/.*'version'[[:space:]]*=>[[:space:]]*'([^']+)'.*/\1/p"` |
| Node.js | `package.json` | `jq -r .version` |
| Python | `pyproject.toml` | `sed -nE 's/^version[[:space:]]*=[[:space:]]*"([^"]+)".*/\1/p'` |
| Go | `version.go` | `sed -nE 's/.*Version[[:space:]]*=[[:space:]]*"([^"]+)".*/\1/p'` |
| Rust | `Cargo.toml` | `sed -nE 's/^version[[:space:]]*=[[:space:]]*"([^"]+)".*/\1/p'` |
| Claude Code Plugin | `.claude-plugin/plugin.json` | `python3 -c "import json; print(json.load(open('.claude-plugin/plugin.json'))['version'])"` |

## Composer Audit Blocking Installs

Composer 2.7+ blocks `composer install/require` if a dependency has a known security advisory (exit code 2). This can break CI even when the advisory is in a transitive dependency you don't control.

**Temporary exemption in `composer.json`:**
```json
{
    "config": {
        "audit": {
            "ignore": {
                "PKSA-xxxx-yyyy": "Upstream issue via dependency-name, no fix available yet"
            }
        }
    }
}
```

Remove the exemption once the upstream fix is released.

## Batch PR Merging Gotchas

When merging PRs across many repos:

- **Check allowed merge methods** — repos may only allow rebase, squash, or merge commits. Use `gh api repos/OWNER/REPO --jq '{allow_merge: .allow_merge_commit, allow_rebase: .allow_rebase_merge, allow_squash: .allow_squash_merge}'`. Detection snippet + the rebase-merge-cannot-be-signed caveat are in [`auto-merge-guide.md`](./auto-merge-guide.md) → "Signed Commits and Merge Strategy Compatibility". Real-world heterogeneity to expect: across one Netresearch fleet alone, some repos allow only rebase, some only merge commits, and some all three.
- **`--admin` bypasses branch protection** — useful when `enforce_admins` is false and you're a repo admin
- **`dismiss_stale_reviews` clears approvals on force-push** — after rebasing, prior approvals are dismissed and any auto-approve workflow must re-run. This is expected behavior, not a bug. See [`auto-merge-guide.md`](./auto-merge-guide.md) → "Auto-Approve Race Condition with Copilot Reviewer" for the variant where auto-approve fires before Copilot finishes reviewing and the PR ends up `REVIEW_REQUIRED` blocked.

### `gh pr merge --delete-branch` fails with merge queues

Repos with merge queues enabled reject the `-d` / `--delete-branch` flag — the queue manages the head-branch lifecycle itself. Symptom: `gh pr merge` exits non-zero with an error mentioning the merge queue, even though the PR was added to the queue successfully.

**Fix — detect the queue first, then conditionally drop the flag.** Note: `gh api "repos/$REPO"` does NOT return a `merge_queue` field; query GraphQL `Repository.mergeQueue` instead, which returns `null` when no queue is configured:

```bash
OWNER="${REPO%/*}"; NAME="${REPO#*/}"
has_queue=$(gh api graphql -f query="{ repository(owner: \"$OWNER\", name: \"$NAME\") { mergeQueue { id } } }" \
  --jq '.data.repository.mergeQueue // "null"')
if [[ "$?" -ne 0 ]]; then
  echo "Error: failed to query merge queue status for $REPO" >&2
  exit 1
fi
# Auto-detect allowed merge strategy too — repos may not allow `--merge`.
# See auto-merge-guide.md → "Signed Commits and Merge Strategy Compatibility".
STRATEGY=$(gh api "repos/$REPO" --jq '
  if .allow_squash_merge then "--squash"
  elif .allow_merge_commit then "--merge"
  elif .allow_rebase_merge then "--rebase"
  else "--squash" end')

if [[ "$has_queue" == "null" ]]; then
  gh pr merge "$PR" --repo "$REPO" "$STRATEGY" --delete-branch
else
  gh pr merge "$PR" --repo "$REPO" "$STRATEGY"   # queue handles branch deletion
fi
```

In a batch loop across mixed repos, always run **both** detections per repo — assuming "no queue" silently leaves stale branches behind on the queue-enabled ones, assuming "queue" causes `--delete-branch` failures on the unqueued ones, and hardcoding `--merge` causes "merge method not allowed" failures on repos that only permit squash or rebase.

### Contents API commits don't satisfy `required_signatures`

`gh api -X PUT repos/.../contents/...` is the fastest way to land a one-line edit across many repos, but the resulting commits use GitHub's `web-flow` committer identity — they are **not signed with your GPG/SSH key**. On any repo with branch protection `required_signatures: true`, those commits are rejected by the merge gate.

**Symptom:** the API push itself succeeds (HTTP 201), but a follow-up PR or the same-branch merge fails with:

```
Required signatures: At least one of the commits is not signed.
```

Or, on default-branch direct pushes, HTTP 409 from the contents API itself when branch protection blocks unsigned commits.

**Workarounds (pick the one that matches your situation):**

1. **`gh pr merge --admin`** — bypass branch protection on a per-merge basis. Requires `enforce_admins: false` AND admin role on the repo. Cleanest for solo-maintainer batch ops.
2. **Push real local commits via SSH** instead of using the contents API. Slightly slower per repo, but the commits carry your signature and need no bypass. This is the safer default when the batch mixes signing-required and signing-optional repos — it works uniformly.
3. **GitHub App with verified signing** — if the batch tool is something other people will run too, register a GitHub App with a verified signing identity and have it commit on your behalf. Heavier setup, but no per-repo admin bypass and no per-user keys.

See also [`multi-repo-operations.md`](./multi-repo-operations.md) → "Contents API vs branch protection" for the related HTTP 409 angle (PR-required / merge-queue-required repos rejecting contents API pushes regardless of signing).

## Why Not Just Use `tailor set-version`?

Some tools (like TYPO3's `tailor`) can set the version at publish time. However:

- **Fail-fast is better** — catching mismatches early (pre-push or CI start) is cheaper than failing mid-publish
- **Consistency** — the repository should always reflect the correct version at the tagged commit
- **Auditability** — `git show v1.2.3:ext_emconf.php` should show the matching version



--- FILE: skills/github-project/references/upstream-contributions.md ---

<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->
<!-- SPDX-FileCopyrightText: Netresearch DTT GmbH -->

# Contributing to Repositories You Do Not Own

First contribution to a foreign repo — an issue, a PR, or both. Every step here
exists because skipping it produced a public artifact that had to be walked
back.

## Before filing anything: read the lists, not just search results

Read the **open issue list AND the open PR list** before writing a word.
Keyword searches find your phrasing, not the problem: three searches
("dry-run exit", "changed_files", "xliff diff") all came back empty against a
repo whose issue #427 described the same defect as "don't return **error
code**" — and whose open PR #430 already fixed it. The repo had six open
issues; reading the list would have taken a minute. The duplicate issue and PR
both had to be closed with thanks.

```bash
gh issue list -R OWNER/REPO --state open   # read it, all of it if small
gh pr list -R OWNER/REPO --state open      # the fix may already be in flight
```

An empty keyword search is first a broken query, never evidence of absence.

**Read Discussions too, and do not read a bot-closed issue as a decision.** Where
a project routes feature requests to Discussions, the issue tracker takes bug
reports only and a bot closes everything else within the minute — `NOT_PLANNED`
there is triage, not a verdict, while the live thread sits open in Discussions
with the same title. herdrdev/herdr#2045 was closed that way; the same request
was open as discussion #2047 with no maintainer answer.

```bash
# search by keyword, not the newest N — a matching thread can be years old
gh api graphql -f q='repo:OWNER/REPO <keywords>' -f query='query($q:String!){search(query:$q,type:DISCUSSION,first:25){nodes{... on Discussion{number title closed url}}}}'
```

**Check whether the repo accepts pull requests from you at all — before writing
code.** Some projects gate contributions on an allowlist: `CONTRIBUTING.md` says
unsolicited pull requests are closed automatically, and only accounts listed in
a file such as `.github/APPROVED_CONTRIBUTORS` (or the maintainers file) may
open one. A finished patch then has no route in there. Follow whatever process the
repository documents for getting access — and where it documents none, or
forbids asking (herdr's `CONTRIBUTING.md` does), the remaining step is a comment
on the relevant discussion. Read those two files with the issue and PR lists,
and match them against the account `gh auth status` reports.

## Read the contribution contract — and run ALL of it

`CONTRIBUTING.md` or the README's contributing section, every linked step, the
issue/PR templates, and the workflows under `.github/workflows/` (they encode
gates prose never mentions: linear-history checks, rebase-on-latest-main
requirements). Running four of five documented steps is not compliance — the
skipped `composer docs` step is the one the maintainer notices.

Conventions are read from artifacts, not assumed:

- **Commit style** from `git log --oneline -10` (e.g. `[BUGFIX]`/`[TASK]`
  prefixes vs conventional commits).
- **Sign-off** from recent commit trailers — a repo where 0 of the last 6
  commits carry `Signed-off-by` does not want yours enforced; carrying your own
  disclosure trailers is fine where nothing bans them.

## Match the code style you measure, not the style you brought

House style does not travel. Before writing code, measure the target:

```bash
# comment density and the longest comment block in their source
find src -name '*.php' | xargs grep -cE '^\s*//' | awk -F: '{s+=$2; n++} END {print s/n " avg comment lines/file"}'
```

A codebase whose largest existing comment block is two lines does not want
your six-line rationale inline — that context belongs in the commit message
and PR body, which is where such projects keep it. Two five-line comment
blocks were the longest in an entire codebase until a reviewer asked why.

## Open the PR as a draft

A first-time PR into a foreign org starts in draft. It signals "for your
judgment" rather than "merge me", costs one click to promote, and gives the
maintainers the first move. Converting later: `gh pr ready <n>`.

## Their fixers are not your diff

Project-level format/rectify gates may rewrite files you never touched (their
main simply drifted). Revert those before committing — a first PR that
reformats four unrelated files reads as carelessness:

```bash
git checkout -- <paths the fixer touched that you did not>
```

## When a maintainer asks "does X fix your problem?" — run X

Check out the competing branch and run it against **your own reproduction**,
then answer with the measured result. A table of before/after numbers settles
in one comment what diff-reading speculation cannot — and if the other fix is
better, say so plainly and close your own PR in its favour, with thanks.

## Closing your superseded work

Close with a reference to what supersedes it and what, if anything, of yours
remains useful (offer it as a follow-up, do not relitigate). The goodwill from
a clean retreat is worth more than the PR was.



--- FILE: skills/github-project/references/workflow-bash-patterns.md ---

<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->
<!-- SPDX-FileCopyrightText: Netresearch DTT GmbH -->

# Bash Patterns in GitHub Actions `run:` Steps

Recurring shell-scripting gotchas that turn workflow `run:` steps into silent data-loss bugs or, worse, build-passing-while-broken releases. Every entry here has caused a real incident in the netresearch fleet; fix each case up-front when you write new reusable workflows.

## Quick Index

| Symptom | Cause | See |
|---|---|---|
| Custom `::error::` never fires; step just exits non-zero with a one-line `exit` | `set -e` aborts on `VAR=$(failing-cmd)` BEFORE your diagnostic runs | [Generic shell pitfalls](#generic-shell-pitfalls) |
| Detection works for one match but "forgets" when several match | SIGPIPE race under `set -o pipefail` with early-exiting readers | [Generic shell pitfalls](#generic-shell-pitfalls) |
| Binary has mangled version/ldflag; release log "looks fine" | `2>&1` merged stderr into a captured variable | [Generic shell pitfalls](#generic-shell-pitfalls) |
| ldflags silently drop values; no error | Expression in top-level job `with:` evaluated BEFORE reusable checkout | [Expression context availability](#expression-context-availability) |
| Matrix cell keeps receiving an input the condition was meant to suppress; the fix looks applied and changes nothing | `''` is falsy, so `cond && '' \|\| value` always yields `value` | [The empty string is falsy](#the-empty-string-is-falsy-in-actions-expressions) |
| Workflow runs on triggers it shouldn't, all jobs fail instantly | File failed validation — GitHub creates a failing run regardless of `on:` match | [Workflow-file validation failure](#workflow-file-validation-failure) |
| Random startup_failure across the whole fleet after a template change | Caller job permissions < reusable job's declared permissions | [Permission propagation](#permission-propagation) |
| Dispatch payload reaches `rm -Rf`, `git clone` or a console command | `client_payload.*` interpolated into a script instead of passed as an env var | [Untrusted payload fields](#untrusted-payload-fields-in-a-run-step-or-a-remote-script) |
| Annotations stop appearing mid-job after a rejected input | An error message echoed an untrusted value containing `\n::stop-commands::` | [Untrusted payload fields](#untrusted-payload-fields-in-a-run-step-or-a-remote-script) |
| Expression fails to evaluate; the file "looks right" | `''` inside a single-quoted YAML scalar collapsed to one quote | [toJSON in a single-quoted scalar](#tojson-inside-a-single-quoted-yaml-scalar) |
| `gh` fails with `fatal: not a git repository`, in a job that never checks out | `gh` infers the repository from a git remote, and there is none | [gh in a checkout-less job](#gh-in-a-job-that-does-not-check-out) |
| A `run:` step passed every local case and still broke in CI | The stub answered regardless of the environment the step actually runs in | [Exercising a run: step locally](#exercising-a-run-step-locally) |

## Generic shell pitfalls

`set -e` with `$(…)`, SIGPIPE under `pipefail` with an early reader, and `2>&1` inside a capture are not specific to Actions `run:` steps. The cli-tools skill's [shell pitfalls reference](https://github.com/netresearch/coding_agent_cli_toolset/blob/main/skills/cli-tools/references/shell-pitfalls.md) covers them, measured and under test, together with the other shell constructs that report success or emptiness that is not real. Two details matter most in a workflow step:

- An `::error::` line placed after a failing `VAR=$(cmd)` is never reached under `set -e`, so the log shows only the bare exit code. Put the assignment in the condition: `if ! VAR=$(cmd); then echo "::error::…"; exit 1; fi`, and check for empty output separately.
- For "does any file match", `find … -exec grep -q PATTERN {} \; -print -quit` stops after the first hit without a pipe, so there is no reader for SIGPIPE to race.

## Expression context availability

**Bug:**

```yaml
jobs:
  build:
    uses: org/.github/.github/workflows/reusable.yml@main
    with:
      # This WAS the template's conditional bun setup:
      setup-bun: ${{ hashFiles('package.json') != '' }}
```

`hashFiles()` is only valid in step-level expressions (`steps.*.env`, `steps.*.if`, `steps.*.run`, `steps.*.with`). GitHub rejects the whole workflow file at validation time. **The workflow then runs on every trigger and fails instantly** — not just triggers that match `on:` — because a validation-failed workflow emits a run record regardless.

Even worse: on reusable-workflow callers with no steps of their own, `hashFiles()` in `with:` would semantically evaluate *before* the reusable workflow's own checkout anyway, so even if actionlint didn't catch it, the function would see an empty workspace.

**Fix:** either move the conditional into the reusable workflow's steps (post-checkout), OR accept the cost of the unconditional setup. For `setup-bun` specifically, `bun install` takes ~10s and the commands behind it can be gated with `if [ -f package.json ]` inside the script.

**Rule of thumb:** the caller's `with:` block is static-ish — `github.*` context is available, `steps.*` / `hashFiles()` are not. Use `actionlint` locally before pushing.

## The empty string is falsy in Actions expressions

**Bug:**

```yaml
${{ matrix.prefer-lowest && '' || matrix.symfony }}   # ALWAYS yields matrix.symfony
```

GitHub-Actions expressions treat `''` as falsy, so the truthy branch is discarded and the `||` branch wins unconditionally. The cell keeps receiving the input the condition was meant to suppress, and the fix looks applied while doing nothing.

**Fix:** the non-empty value belongs in the truthy branch. To suppress an input, invert the condition and put `''` behind `||`:

```yaml
${{ !matrix.prefer-lowest && matrix.symfony || '' }}  # correct
```

Ternaries with a non-empty string in both branches (`cond && 'lowest' || 'highest'`) are unaffected.

**Sweep for the broken form:** `grep -rnE "&& '' \|\|" .github/workflows/`.

The reason this is worth a rule rather than a footnote is how it fails: the workflow stays valid, actionlint says nothing, and the matrix cell simply stays red — which invites a diagnosis somewhere else entirely. Confirm the fix actually ran (`gh run view <id> --json headSha`) before blaming a dependency.

## Workflow-file validation failure

**Symptom:** `gh run list` shows a failing run with `name: .github/workflows/foo.yml` (the file path shown INSTEAD of the workflow's `name:` field), triggered on an event your `on:` block shouldn't match.

**Cause:** the workflow file failed validation. GitHub couldn't even resolve `name:`, so it shows the path. Validation-failed workflows emit a failure run on *every* trigger the repo receives, regardless of whether `on:` matches.

**Diagnose:**

```bash
gh run view <run-id> --repo <repo>
# "This run likely failed because of a workflow file issue." confirms validation failure
```

**Fix:** run `actionlint` against the file. Common culprits:

- `hashFiles()` or `steps.*` in top-level `with:` (see above).
- Invalid matrix variable reference (e.g. `matrix.goarm` in `with:` when the narrowed matrix no longer includes an `arm/v*` entry).
- Missing required input on a reusable workflow call.
- YAML-level: tab/space mixing, unquoted special characters in flow-style arrays.

## Permission propagation

Reusable workflows run under the **caller's** token. If the reusable job declares `permissions: { security-events: write }` but the caller grants only `contents: read`, GitHub rejects the job at startup and you get `startup_failure` across every invocation — fleet-wide, if the broken template is shared.

**The specific netresearch incident:** a `gitleaks.yml` caller granted `contents: read` only; the reusable `gitleaks.yml` needed `security-events: write` to upload SARIF. Every consumer's gitleaks workflow startup_failure'd for 24+ hours, meaning zero secret scanning happened on any main push, while `gh run list` showed the `startup_failure` status but nothing in CI jobs to diagnose.

**Rule:** when writing a reusable workflow, put a **CALLER REQUIREMENTS** block at the top of the file listing every permission the caller must grant. Keep it copy-pasteable:

```yaml
# CALLER REQUIREMENTS
# ===================
# The caller's job-level `permissions:` block MUST grant at least:
#
#   permissions:
#     contents: read
#     security-events: write  # required for SARIF upload at the end
#     packages: write         # required to push the image to ghcr.io
#
# Less than this fails at workflow startup with a `startup_failure`
# run and no job output — GitHub rejects the caller before any step
# executes.
```

When reviewing PRs that touch caller workflows, the first thing to check is that the caller's `permissions:` is ≥ what every reusable workflow it calls declares.

## Expression gotchas — release & multi-trigger workflows

Workflows that accept both a "normal" trigger (e.g. `push: tags`) and a manual override (`workflow_dispatch` with inputs) repeatedly trip over the same expression-context quirks. Each cost us a round of Copilot back-and-forth in the release-process doc; bundling them here so the next reader finds them in one place.

### `inputs.*` is not defined outside `workflow_dispatch` / `workflow_call`

```yaml
on:
  push:
    tags: ['v*']
  workflow_dispatch:
    inputs:
      tag: { required: true }

jobs:
  publish:
    steps:
      - uses: actions/checkout@...
        with:
          ref: ${{ inputs.tag || github.ref_name }}   # FAILS on push.tags
```

On `push.tags`, GitHub evaluates `inputs.tag` and raises *"Unrecognized named-value: 'inputs'"*. The workflow fails before any step runs.

**Fix:** use `github.event.inputs.*`, which resolves to an empty string on non-dispatch events:

```yaml
          ref: ${{ github.event.inputs.tag || github.ref_name }}
```

### On `workflow_dispatch`, `github.ref_name` is the dispatch source, not a tag

A workflow triggered via the Actions UI from `main` has `github.ref_name == 'main'`, even if the user supplied a tag via an input. Tag-source-of-truth workflows (release publishes, asset builds) must **explicitly** checkout the input tag, or they'll build assets from `main` HEAD and upload them to the tag's release:

```yaml
      - uses: actions/checkout@...
        with:
          ref: ${{ github.event.inputs.tag || github.ref_name }}
          fetch-tags: true
```

### GitHub Actions expressions have no ternary

`a ? b : c` is a YAML-level syntax error — GHA expressions only support `&&` / `||`. The idiom is:

```yaml
# "if cond then A else B" -->  cond && A || B
make_latest: ${{ github.event_name == 'workflow_dispatch' && 'false' || 'true' }}
```

Watch for the **truthy-string trap**: `'false'` is a non-empty string, so it's truthy. If you're branching on a boolean input, wrap it in `fromJSON()` to convert the string `'false'` to actual `false`:

```yaml
make_latest: ${{ fromJSON(github.event.inputs.make_latest || 'true') && 'true' || 'false' }}
```

Without `fromJSON`, `'false' && 'true' || 'false'` evaluates to `'true'` because the string `'false'` is truthy.

### Hyphenated input names force bracket-expression access

```yaml
inputs:
  make-latest: { type: boolean }   # hyphen

# Must be referenced as:
${{ inputs['make-latest'] }}       # not inputs.make-latest (parsed as subtraction!)
```

Prefer underscored names (`make_latest`) so dot-notation works. Matches GitHub's own action parameter style (`softprops/action-gh-release` uses `make_latest`, not `make-latest`).

## Untrusted payload fields in a `run:` step or a remote script

`repository_dispatch` `client_payload.*` is the same trust class as an issue title: whoever holds a write token on the repo composes it, and the sender usually forwards a value it took from somewhere else (a branch name, a `composer.json`). Three rules, all from t3docs-ci-deploy, where `rm -Rf ${{ … }}/${{ … }}` ran against the production documentation host.

**1. Validate the fields as what they are, in a step of their own, first in the job.** For a path segment: no character outside `[A-Za-z0-9._-]`, no `..`, no leading `.` or `-`. The leading dash is not cosmetic — `-q` reaching a Symfony console command as a positional argument is parsed as an option cluster.

```bash
for name in TYPE_SHORT VENDOR NAME; do
  value="${!name}"
  case "$value" in
    *[!A-Za-z0-9._-]* | *..* | .* | -* | '')
      echo "::error::client_payload field $name is not a plain path segment"
      exit 1
      ;;
  esac
done
```

**2. Never echo the value in the diagnostic.** A payload field may contain a newline, and the runner reads every line of step output: a value of `x\n::stop-commands::abc` disables annotations for the rest of the job, `\n::add-mask::/` masks unrelated log lines. The field name identifies the problem; the value adds nothing a rejected dispatch needs.

**3. Into a remote script, pass values as environment variables, never as text.** `appleboy/ssh-action`'s `envs:` input names variables from the step `env:`; drone-ssh uppercases each name and emits `export NAME='value'` with the value single-quote-escaped (`escapeArg`), so no payload character can leave its argument. Quote at the point of use, and require the variable — an empty segment silently collapses a path onto its root:

```yaml
# The validation step from rule 1 runs first in this job; without it the
# transport is safe but the value is still whatever the sender put in.
- uses: appleboy/ssh-action@<sha>
  env:
    TARGET_PATH: ${{ secrets.TARGET_PATH }}
    VENDOR: ${{ github.event.client_payload.vendor }}
  with:
    envs: TARGET_PATH,VENDOR
    script: |
      : "${TARGET_PATH:?not set}" "${VENDOR:?not set}"
      rm -Rf "$TARGET_PATH/$VENDOR"
```

An **action input** cannot take this route — `appleboy/scp-action`'s `target:` is interpolated by the action itself, so a destructive `rm: true` upload depends on the validation step having run first in the same job. Say so in a comment above it; step order is the only thing holding it.

## `toJSON()` inside a single-quoted YAML scalar

```yaml
# Broken - YAML turns '' into ' before the expression is ever evaluated
data: '{"id":${{ toJSON(github.event.client_payload.id || '') }}}'

# Correct - a folded scalar carries the expression verbatim
data: >-
  {"id":${{ toJSON(format('{0}', github.event.client_payload.id)) }}}
```

Expression strings are single-quoted, and inside a single-quoted YAML scalar `''` is the escape for one quote. The parser hands the runner `… || ')` and the workflow fails at expression evaluation, far from the line that caused it. A single-quoted scalar is not ruled out — it works when every quote of the expression is doubled (`format(''{0}'', x)`, an empty string as `''''`) — but the folded scalar removes that bookkeeping, and one missed doubling changes the expression silently. Check what the file actually parses to (`yq '.jobs.x.steps[0].env.data'`) rather than what it looks like.

Two related points on building JSON in a workflow: `toJSON` emits the value's native type, so an id that arrives as a number is no longer a JSON string for the receiver — wrap it (`toJSON(format('{0}', …))`) when the consumer expects one. And hand-quoting the field (`"id":"${{ … }}"`) is the injection: a quote in the value appends keys to your body, which a downstream `jq -c .` then resolves in the attacker's favour.

## `gh` in a job that does not check out

**Bug:** a job that only downloads an artifact — a release-publishing job, an evidence collector, anything that works on `dist/` rather than on the tree — calls `gh` and gets:

```
fatal: not a git repository (or any of the parent directories): .git
```

`gh` resolves the repository from a git remote in the working directory. `GH_TOKEN` is set, the API is reachable, the permissions are right, and it still cannot tell which repository you mean.

**Fix:** name it, from the context GitHub already provides.

```yaml
env:
  GH_TOKEN: ${{ github.token }}
  REPO: ${{ github.repository }}
run: |
  gh release view "$TAG" --repo "$REPO" --json assets
```

Cheap source check before shipping such a step — per invocation, not per line, because two `gh` calls can share a line and a `gh pr`/`gh run` is just as affected as a `gh release`:

```bash
# extract first, then read the shell — the second grep works on the step body,
# not on the YAML, and a `yq | grep` pipeline is the shape the data-tools hook
# stops (rightly, for field access) even when the grep is aimed at the output.
yq -r '.jobs.<job>.steps[-1].run' .github/workflows/x.yml > step.sh
grep -oE 'gh [a-z-]+ [a-z-]+[^|;&]*' step.sh \
  | grep -v -- '--repo' \
  || echo 'every gh invocation names its repository'
```

Anything printed is an invocation to fix. This shipped to a fleet-wide reusable workflow and failed on every release until it was caught.

## Exercising a `run:` step locally

A `run:` step is shell, so it can be run before it reaches CI — which is worth doing for anything that gates a release, because its failure path is the part CI will not exercise on a good day.

```bash
HARNESS=$(mktemp -d)

# the step itself, verbatim, without hand-copying it out of the YAML
yq -r '.jobs.<job>.steps[-1].run' .github/workflows/x.yml > "$HARNESS/step.sh"

# a stub for whatever CLI it drives, first on PATH
mkdir -p "$HARNESS/bin" && cat > "$HARNESS/bin/gh" <<'SHIM'
#!/usr/bin/env bash
...answer per $MODE...
SHIM
chmod +x "$HARNESS/bin/gh"

# one case per invocation, with a captured status. Absolute paths: the step
# runs from a sandbox directory, so a relative `step.sh` would not resolve.
mkdir -p "$HARNESS/sandbox"
( cd "$HARNESS/sandbox"
  PATH="$HARNESS/bin:$PATH" MODE=missing GITHUB_OUTPUT=out.txt \
    bash -eo pipefail "$HARNESS/step.sh"
  echo "rc=$?" )
```

`bash -eo pipefail` because the extracted body is only what was under `run:` — the runner supplies `bash -e {0}`, and `pipefail` comes from a `set -o pipefail` inside the body. A step that sets its own options makes the flags redundant, which is harmless; a step that relies on the runner's needs them, or the harness silently passes failures the job would have caught.

One case per subshell matters for the same reason it does anywhere: `set -e` behaves differently when a command's status is consumed by a pipe or a `||`, so a harness that wraps the variants in functions measures the harness.

**The stub must model the environment, not only the logic.** A stub that answers every call regardless of context proves the branches and nothing about where the step runs. Four such cases passed for a step that then failed in CI on `fatal: not a git repository` — the stub had never cared which directory it was called from. Teaching it to refuse a call that omits `--repo` when the working directory is not a checkout turned that defect into a failing case:

```bash
if ! printf '%s\n' "$@" | grep -qx -- '--repo'; then
  git rev-parse --git-dir >/dev/null 2>&1 || { echo "failed to run git: fatal: not a git repository" >&2; exit 1; }
fi
```

Ask of any such harness: *if the real thing broke the way it actually breaks, would this stub notice?*

## Related

- [actionlint-guide.md](./actionlint-guide.md) — how to catch these at author-time
- [reusable-workflow-security.md](./reusable-workflow-security.md) — trust model for external workflows
