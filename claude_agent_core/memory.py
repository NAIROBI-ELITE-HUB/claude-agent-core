import json
from pathlib import Path

class MemoryStore:
    def __init__(self):
        self.memory_file = Path.home() / '.claude_agent_core' / 'memory.json'
        self.memory_file.parent.mkdir(exist_ok=True)
        self.load()

    def load(self):
        if self.memory_file.exists():
            with open(self.memory_file) as f:
                self.data = json.load(f)
        else:
            self.data = {'conversations': [], 'lessons': []}

    def save(self):
        with open(self.memory_file, 'w') as f:
            json.dump(self.data, f, indent=2)

    def add_conversation(self, prompt, response):
        self.data['conversations'].append({'prompt': prompt, 'response': response})
        self.save()

    def add_lesson(self, lesson):
        self.data['lessons'].append(lesson)
        self.save()