import json
from pathlib import Path
from datetime import datetime

class MemoryStore:
    def __init__(self):
        self.memory_path = Path.home() / ".claude_agent_core" / "memory.json"
        self.memory_path.parent.mkdir(exist_ok=True)
        self.load()
    
    def load(self):
        pass
    
    def save_interaction(self, prompt, response):
        pass
