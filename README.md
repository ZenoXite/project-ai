# Autonomous AI Coding Agent

A lightweight, CLI-based autonomous developer agent built with Python. The agent leverages LLM function-calling capabilities to inspect, debug, and modify local codebases through natural language prompts.

## Features

- **Autonomous Agent Loop:** Uses an iterative ReAct pattern to plan actions, execute tool calls, observe results, and self-correct until tasks are resolved.
- **Local Tool Execution:** Equipped with filesystem inspection, file modification, and terminal execution tools using structured JSON schemas.
- **Multi-Model Support:** Configured via OpenRouter / OpenAI-compatible APIs to support various open-source and proprietary foundation models.
- **Error Handling:** Captures runtime and filesystem errors during tool execution and feeds them back into context for iterative debugging.

## Architecture

1. **User Prompt:** Receives a natural language task (e.g., *"Find and fix the syntax error in main.py"*).
2. **Reasoning & Tool Selection:** Model assesses the request and issues structured function calls.
3. **Local Dispatch:** Python runtime validates arguments and executes the requested action on the filesystem.
4. **Observation & Synthesis:** Tool output is injected back into the message history until the model determines the task is complete.

## Prerequisites

- Python 3.10+
- An API key from [OpenRouter](https://openrouter.ai/) (or OpenAI)

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ZenoXite/project-ai.git
   cd project-ai

2.Set up a virtual environment:

  python3 -m venv venv
  source venv/bin/activate

3.Install dependencies:

  pip install -r requirements.txt

4.Configure environment variables:
  
  Create a .env file in the root directory:
  OPENROUTER_API_KEY=your_api_key_here

5. Run the Agent Via Terminal :
  python main.py "Locate tests that are failing and update the implementation to pass them."

Security Notice
This agent executes file writes and commands directly on your local machine. Use caution when running it inside non-containerized environments or outside of version-controlled repositories.
