# AIA - AI Assistant Package

A modern Python package for AI assistance.

## Installation

```bash
pip install aia
```

## Development

This project uses modern Python tooling:

- `hatch` for project management
- `pytest` for testing
- `black` for code formatting
- `isort` for import sorting
- `mypy` for type checking
- `ruff` for linting

### Setup Development Environment

```bash
# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Format code
black .
isort .

# Type checking
mypy .

# Linting
ruff check .
```

## License

MIT License 