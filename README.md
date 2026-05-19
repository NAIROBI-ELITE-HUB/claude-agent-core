# claude-agent-core

Lightweight Python wrapper for Claude 3.5 Sonnet, focused on agentic workflows with strong safety controls.

## Features
- Clean `ClaudeAgent` interface
- Tool calling support
- ToolPolicy with risk scoring
- Fortress Gate (human approval + TOTP)
- Conversation memory
- Secure vault handling (DPAPI on Windows)

## Installation

```bash
git clone https://github.com/Informant254/claude-agent-core.git
cd claude-agent-core
pip install -e .
```

## Quick Start

```python
from claude_agent_core import ClaudeAgent

agent = ClaudeAgent()  # Uses ANTHROPIC_API_KEY from environment

response = agent.chat("Hello, who are you?")
print(response.content)
```

## Secure Mode (Recommended)

```python
from claude_agent_core import ClaudeAgent, SecureFortressGate, ToolPolicy

fortress = SecureFortressGate()
policy = ToolPolicy(enforcement_level="strict")

agent = ClaudeAgent(fortress=fortress, policy=policy)

response = agent.chat("Organize my Downloads folder")
```

## Examples
- `examples/killer_downloads_organizer.py` — Practical demo with Fortress
- `examples/secure_fortress_usage.py` — Full secure setup

## Project Status
Early stage. Actively developed.