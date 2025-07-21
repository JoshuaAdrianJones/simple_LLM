# Simple LLM Project

## Project Overview
Starter pack for using local LLMs with Ollama, providing structured chat integration and development environment configuration.

## Project Structure
- `main.py` - Core Ollama chat integration with Pydantic models
- `.devcontainer/` - VS Code development container configuration
- `CLAUDE.md` - Project documentation and development context

## Development Environment
- **Platform**: macOS (Darwin 24.4.0) with Apple Silicon support
- **Containerized Development**: Uses devcontainer with host Ollama integration
- **Dependencies**: Python 3.11, Ollama client library, Pydantic for structured output

## Ollama Configuration
### Available Models
- **qwen3:8b** (5.2 GB) - Chinese/English multilingual model, good for general tasks
- **gemma3:12b** (8.1 GB) - Google's Gemma model, strong reasoning capabilities
- **llama3.2:3b-instruct-fp16** (6.4 GB) - Meta's Llama optimized for instruction following
- **mxbai-embed-large** (669 MB) - Embedding model for semantic search/similarity

### Access Methods
```bash
# Start Ollama API server (runs on http://localhost:11434)
ollama serve

# Run models directly
ollama run qwen3:8b
ollama run gemma3:12b
ollama run llama3.2:3b-instruct-fp16

# API usage
curl -X POST http://localhost:11434/api/generate \
  -d '{"model": "qwen3:8b", "prompt": "Your prompt here"}'
```

## Usage
The main.py file demonstrates structured chat interaction:
```python
from main import generate_general_output, models

# Generate structured response
response = generate_general_output(
    model=models["qwen"],
    model_temperature=0.7,
    prompt="Your question here",
    system_prompt="You are a helpful assistant."
)
print(response.content)
```

## Development Setup
1. Ensure Ollama is running on host machine (`ollama serve`)
2. Open project in VS Code with Dev Containers extension
3. Container will automatically configure to use host Ollama instance
4. Install dependencies: `pip install ollama pydantic`

## Model Configuration
Available models are configured in `main.py`:
- **qwen**: qwen3:8b - General purpose multilingual model
- **gemma**: gemma3:12b - Strong reasoning capabilities  
- **llama**: llama3.2:3b-instruct-fp16 - Instruction-following optimized
- **embed**: mxbai-embed-large - Text embedding model