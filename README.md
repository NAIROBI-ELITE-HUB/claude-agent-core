# claude-agent-core

Lightweight Python wrapper for Claude 3.5 Sonnet focused on agentic workflows with strong safety features.

## Features
- Clean ClaudeAgent interface
- Tool calling support
- ToolPolicy with risk scoring
- Fortress Gate (human + TOTP approval)
- Conversation memory
- Secure vault support

## Installation

```bash
git clone https://github.com/Informant254/claude-agent-core.git
cd claude-agent-core
pip install -e .
```

## Quick Start

```python
from claude_agent_core import ClaudeAgent

agent = ClaudeAgent()
response = agent.chat("Hello! Tell me a joke.")
print(response.content)
```