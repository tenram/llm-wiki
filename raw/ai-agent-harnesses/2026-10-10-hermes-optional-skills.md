# Hermes Optional Skills

> Source: https://github.com/NousResearch/hermes-agent/tree/main/optional-skills
> Collected: 2026-10-10
> Published: Unknown

## Optional Skills

Official skills maintained by Nous Research that are **not activated by default**.

These skills ship with the hermes-agent repository but are not copied to
`~/.hermes/skills/` during setup. They are discoverable via the Skills Hub:

```bash
hermes skills browse
hermes skills browse --source official
hermes skills search <query>
hermes skills install <identifier>
```

## Why optional?

Some skills are useful but not broadly needed by every user:

- **Niche integrations** — specific paid services, specialized tools
- **Experimental features** — promising but not yet proven
- **Heavyweight dependencies** — require significant setup (API keys, installs)

By keeping them optional, the default skill set stays lean while curated, tested, official skills remain available to users who want them.

The repository directory is organized by domains including autonomous agents, blockchain, communication, creative work, data science, DevOps, email, finance, gaming, health, MCP, migration, MLOps, payments, productivity, research, security, smart home, social media, software development, web development, and Yuanbao.
