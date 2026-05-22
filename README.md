# claude-agent-core

**Self-Evolving • Zero-Trust • Secure** Claude Agent Framework

A powerful, lightweight wrapper for Anthropic Claude models with built-in self-improvement, Zero-Trust security, and Fortress human gate.

## Features
- Multi-model support (Sonnet, Opus, Haiku, etc.)
- Self-evolving system (memory + reflection + code improvement)
- Zero-Trust security layer
- Fortress human + TOTP gate
- Persistent learning

## Quick Start

```python
from claude_agent_core import ClaudeAgent

agent = ClaudeAgent()
response = agent.chat("Hello")
print(response)
```

Star if you like it ⭐