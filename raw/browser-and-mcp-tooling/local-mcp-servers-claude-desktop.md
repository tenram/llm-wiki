# Getting Started with Local MCP Servers on Claude Desktop

> Source: https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop
> Collected: 2026-07-31
> Published: Unknown

MCP enables integration between LLM applications and external data sources through desktop extensions: single-click installable packages that simplify setup versus manual JSON configuration.

## Installing from the directory

1. Settings > Extensions in Claude Desktop
2. "Browse extensions" to view Anthropic-reviewed tools
3. Select and Install
4. Configure required settings (e.g. API keys)
5. Extension becomes immediately available in conversations

## Installing custom extensions

1. Settings > Extensions
2. "Advanced settings" > Extension Developer section
3. "Install Extension…"
4. Choose the `.mcpb` file and follow prompts

## Notes

Supports Node.js, Python, and binary MCP servers; Claude Desktop ships a built-in Node.js environment. Sensitive configuration fields are automatically encrypted using the OS credential store (Keychain, Credential Manager, or Linux keychain). Connection status can be verified via the "+" button in the chat box → Connectors, or Developer settings.
