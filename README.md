# Simple LLM

A starter pack for using local LLMs with Ollama, featuring structured chat integration, development containers, and automated CI/CD workflows.

## Features

- 🤖 **Structured Chat Integration**: Pydantic models for type-safe LLM responses
- 🐳 **Development Containers**: VS Code devcontainer with host Ollama integration  
- 🔍 **Code Quality**: Ruff linting and formatting with automated CI checks
- 📦 **Multiple Models**: Support for Qwen, Gemma, and Llama models
- ⚡ **Easy Setup**: One-command installation and configuration

## Quick Start

### Prerequisites
- [Ollama](https://ollama.com) installed and running (`ollama serve`)
- Python 3.11+
- VS Code with Dev Containers extension (optional)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/JoshuaAdrianJones/simple_LLM.git
cd simple_LLM
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the example:
```bash
python main.py
```

### Development with Containers

1. Open project in VS Code
2. Select "Reopen in Container" when prompted
3. Container automatically configures to use host Ollama instance

## Usage

### Basic Chat Integration

```python
from main import generate_general_output, models

# Generate structured response
response = generate_general_output(
    model=models["qwen"],
    model_temperature=0.7,
    prompt="Explain quantum computing",
    system_prompt="You are a helpful technical assistant."
)
print(response.content)
```

### Available Models

| Model | Size | Description |
|-------|------|-------------|
| **qwen** | 5.2 GB | Chinese/English multilingual, general purpose |
| **gemma** | 8.1 GB | Google's model with strong reasoning |  
| **llama** | 6.4 GB | Meta's instruction-following optimized |
| **embed** | 669 MB | Text embedding for semantic search |

## Project Structure

```
simple_LLM/
├── .devcontainer/
│   └── devcontainer.json      # VS Code development container config
├── .github/
│   └── workflows/
│       └── ci.yml             # GitHub Actions CI/CD pipeline
├── main.py                    # Core Ollama chat integration
├── pyproject.toml             # Project configuration and ruff settings
├── requirements.txt           # Python dependencies
├── CLAUDE.md                  # Development context for Claude Code
└── README.md                  # This file
```

## Development

### Code Quality

This project uses [Ruff](https://docs.astral.sh/ruff/) for linting and formatting:

```bash
# Lint code
ruff check .

# Format code  
ruff format .

# Auto-fix issues
ruff check . --fix
```

### CI/CD

GitHub Actions automatically run on push and pull requests:
- **Lint**: Ruff code quality checks
- **Format**: Code formatting verification
- **Test**: Pytest runner (placeholder for future tests)

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run code quality checks (`ruff check . && ruff format .`)
5. Commit your changes (`git commit -m 'feat: add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Ollama](https://ollama.com) for local LLM inference
- [Pydantic](https://pydantic.dev) for data validation
- [Ruff](https://docs.astral.sh/ruff/) for code quality tools
