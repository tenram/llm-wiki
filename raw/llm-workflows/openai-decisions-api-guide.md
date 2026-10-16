# What Is OpenAI Decisions API? A Practical Guide

> Source: https://huggingface.co/blog/sora-2/what-is-openai-decisions-api-a-practical-guide
> Collected: 2026-10-05
> Published: 2026-09-30

OpenAI Decisions API is described as a new, limited-preview interface for applications that need an answer to a bounded question rather than generated prose. A developer defines a finite answer space, sends context, and receives a decision for classification, routing, or an agent's next step.

The author says public reporting describes the API as a specialized GPT-6 Luna interface introduced at DevDay 2026. The author explicitly warns that the preview is changing and production teams must verify the official OpenAI contract before use.

The article contrasts this flow:

```text
prompt -> generated text -> parser -> schema validation -> retry -> action
```

with:

```text
state + bounded question -> typed decision -> policy check -> action
```

It recommends bounded questions, policy and permission checks in code, offline evaluation, shadow traffic, calibration measurements, and human review for high-impact actions. It says confidence is a routing signal, not proof or authorization.

The article is a Hugging Face community post. Its comments note that an official source was unavailable and that a third-party reference link would be replaced later.
