# Contributing to Proteinstellar

Thank you for your interest in contributing to Proteinstellar! We welcome contributions from the community.

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue on GitHub with:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- System information (OS, Python version, GPU if applicable)
- Error messages or logs

### Suggesting Features

Feature requests are welcome! Please:
- Check existing issues to avoid duplicates
- Clearly describe the feature and its use case
- Explain why it would benefit the project

### Code Contributions

1. **Fork the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/proteinstellar.git
   cd proteinstellar
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Follow existing code style
   - Add comments for complex logic
   - Update documentation if needed

4. **Test your changes**
   - Run existing notebooks to ensure nothing breaks
   - Add test cases if applicable

5. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request**
   - Provide clear description of changes
   - Reference related issues
   - Wait for review

## Coding Standards

### Python Code
- Follow PEP 8 style guide
- Use meaningful variable names
- Add docstrings to functions
- Keep functions focused and concise

### Jupyter Notebooks
- Clear markdown documentation
- Well-commented code cells
- Modular cell structure
- Clean outputs before committing

### Commit Messages
Follow conventional commits:
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `refactor:` - Code refactoring
- `test:` - Adding tests
- `chore:` - Maintenance tasks

## Development Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install black flake8 isort pytest
```

## Testing

```bash
# Run notebooks manually
jupyter notebook

# Check code style
black --check .
flake8 .
isort --check .
```

## Documentation

- Update README.md for user-facing changes
- Update PROJECT_ARCHITECTURE.md for technical changes
- Add inline comments for complex algorithms
- Update requirements.txt for new dependencies

## Code Review Process

1. Maintainers will review your PR
2. Address feedback and requested changes
3. Once approved, your PR will be merged
4. Your contribution will be acknowledged

## Questions?

Feel free to:
- Open a discussion on GitHub
- Comment on existing issues
- Reach out to maintainers

Thank you for contributing! 🎉
