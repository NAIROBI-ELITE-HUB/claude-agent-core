# claude-agent-core

**Self-evolving, Zero-Trust Claude Agent Framework**

Lightweight wrapper for all Anthropic Claude models with built-in Fortress human gate, Zero-Trust security, and self-improvement capabilities.

## Key Features
- Multi-model support (Sonnet, Opus, Haiku)
- SecureFortressGate (Human + TOTP)
- Zero-Trust Security Layer
- Self-reflection & Code Evolution Engine
- Persistent Memory

## Quick Start

```bash
pip install -e .
```

```python
from claude_agent_core import ClaudeAgent

agent = ClaudeAgent()
response = agent.chat("Hello")
```