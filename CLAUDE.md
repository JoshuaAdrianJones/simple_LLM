# Claude Code Terminal Environment Context

## System Information
- **Platform**: macOS (Darwin 24.4.0)
- **Architecture**: arm64 (Apple Silicon)
- **Working Directory**: /Users/josh
- **Git Repository**: Not initialized

## Shell Environment
- **Terminal**: iTerm2
- **Shell**: zsh 5.9 (arm64-apple-darwin24.0)
- **Framework**: oh-my-zsh
- **Shell Path**: /bin/zsh

## Package Managers & Tools
- **Homebrew**: 4.5.10 (installed at /opt/homebrew/bin/brew)
- **Ollama**: 0.9.6 (installed at /usr/local/bin/ollama)

## Available Commands
- `brew` - Package management for macOS
- `ollama` - Local LLM inference engine
- Standard Unix/macOS command line tools
- zsh built-ins and oh-my-zsh plugins

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

## Use Cases for Ollama + Claude Code Integration

### 1. Code Review Assistant
Build tools that use local models to review code changes, suggest improvements, and check for patterns without sending code to external services.

### 2. Documentation Generator
Create scripts that use Ollama models to generate documentation from code comments and structure, keeping everything local for sensitive projects.

### 3. Custom Chat Interfaces
Build domain-specific coding assistants using local models fine-tuned for specific frameworks or languages.

### 4. Code Explanation Tools
Develop utilities that explain complex codebases using local LLMs, useful for onboarding or legacy code understanding.

### 5. Automated Testing
Create test generators that use local models to create comprehensive test suites based on code analysis.

### 6. Semantic Code Search
Use embedding models (mxbai-embed-large) to build semantic code search tools that understand context beyond keyword matching.

### 7. Code Translation
Build tools to translate code between programming languages using local models, ensuring code privacy.

### 8. Local AI-Powered Git Hooks
Create git hooks that use local models for commit message generation, code quality checks, or automated changelog updates.

## Notes
- Homebrew prefix: /opt/homebrew (Apple Silicon)
- oh-my-zsh configuration directory: ~/.oh-my-zsh