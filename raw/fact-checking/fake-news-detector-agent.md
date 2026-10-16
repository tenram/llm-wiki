# Fake News Detection Multi-Agent System

> Source: https://github.com/IAmUnbounded/fake-news-detector-agent
> Collected: 2026-10-05
> Published: Unknown

This project implements a multi-agent system for detecting fake news. It has three agents:

1. Orchestrator Agent: Coordinates the overall process and manages communication between agents.
2. Search Agent: Searches historical news articles for fact-checking information using Google Search MCP Server.
3. Scorer Agent: Analyzes news content and determines authenticity using Google's Gemini API.

The system accepts a news article or claim and returns an authenticity score with supporting evidence. It requires a Google API key and a configured Google Search MCP server.
