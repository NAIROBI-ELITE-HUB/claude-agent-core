from claude_agent_core import ClaudeAgent
import os
from pathlib import Path

def main():
    agent = ClaudeAgent()
    
    downloads = str(Path.home() / "Downloads")
    
    prompt = f"""
    You are a helpful file organizer.
    Analyze the Downloads folder at: {downloads}
    Suggest a clean organization structure (categories like Documents, Images, Code, etc.).
    Be safe and conservative.
    """
    
    print("Running Downloads Organizer Demo...\n")
    response = agent.chat(prompt)
    print(response.content)

if __name__ == "__main__":
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("Error: ANTHROPIC_API_KEY environment variable not set.")
    else:
        main()