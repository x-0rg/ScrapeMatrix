# 🤝 Contributing Guidelines

Thank you for your interest in contributing to ScrapeMatrix! This document explains how to contribute.

## 🎯 How to Contribute

### Report Bugs

#### Before Reporting
1. Check existing issues
2. Read TROUBLESHOOTING.md
3. Try to reproduce the issue

#### How to Report
1. Go to GitHub Issues
2. Click "New Issue"
3. Choose "Bug Report"
4. Fill in the template with:
   - **Title:** Clear, descriptive
   - **OS & Version:** Windows/macOS/Linux + Python version
   - **Error Message:** Full traceback
   - **Steps to Reproduce:** Clear steps
   - **Expected Behavior:** What should happen
   - **Actual Behavior:** What actually happened
   - **Screenshots:** If applicable

#### Good Bug Report Example
```
Title: "Autocomplete fails with special characters in ticker"

Environment:
- OS: Windows 10
- Python: 3.10.1
- App Version: 0.1.0

Steps to Reproduce:
1. Open app
2. Click ticker input
3. Type "$AAPL" (with dollar sign)
4. See error

Expected:
- Should filter tickers or ignore $

Actual:
- Application crashes
- Error: "ValueError: invalid literal"

Traceback:
[Full error message here]
```

---

### Request Features

#### Before Requesting
1. Check roadmap
2. Check existing issues
3. Ensure it aligns with project goals

#### How to Request
1. Go to GitHub Issues
2. Click "New Issue"
3. Choose "Feature Request"
4. Describe with:
   - **Title:** Clear feature name
   - **Description:** What and why
   - **Use Case:** When would you use it?
   - **Examples:** How should it work?
   - **Mockups:** Optional sketches

---

### Contribute Code

#### Getting Started
1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR-USERNAME/ScrapeMatrix.git`
3. Create virtual environment
4. Install dev dependencies
5. Create feature branch

#### Code Style
- Follow PEP 8
- Use type hints
- Write docstrings
- Comment complex code
- Run formatters

```bash
# Format code
black src/

# Check style
flake8 src/

# Type checking
mypy src/
```

#### Making Changes
1. Make small, focused changes
2. Test thoroughly
3. Write/update tests
4. Update documentation
5. Commit with clear messages

#### Git Workflow

**Create Feature Branch:**
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b bugfix/issue-description
```

**Make Commits:**
```bash
# Keep commits small and focused
git add specific_file.py
git commit -m "Add description of change"
```

**Push Changes:**
```bash
git push origin feature/your-feature-name
```

**Create Pull Request:**
1. Go to GitHub
2. Click "Create Pull Request"
3. Fill in description
4. Wait for review

---

### Improve Documentation

Documentation improvements are always welcome!

#### Documentation Files
- `/docs/*.md` - User and developer guides
- `src/scrapematrix/**/*.py` - Code docstrings
- `README.md` - Project readme

#### How to Contribute Docs
1. Identify improvement needed
2. Fork repository
3. Edit relevant .md file
4. Create pull request
5. Describe improvements

#### Documentation Standards
```python
def fetch_stock_data(ticker: str, period: str = "1y") -> Optional[pd.DataFrame]:
    """
    Fetch historical stock data from Yahoo Finance.
    
    Args:
        ticker: Stock ticker symbol (e.g., 'AAPL')
        period: Time period for data (default: '1y')
               Options: 1mo, 3mo, 6mo, 1y, 2y, 5y, max
    
    Returns:
        DataFrame with OHLCV data or None if fetch fails
        
    Raises:
        ValueError: If ticker is invalid
        ConnectionError: If API connection fails
        
    Example:
        >>> data = StockDataLoader.fetch_stock_data('AAPL', '1y')
        >>> print(data.head())
    """
```

---

## 📋 Pull Request Process

### Before Submitting
- [ ] Code follows PEP 8
- [ ] Type hints added
- [ ] Docstrings written
- [ ] Tests pass
- [ ] Documentation updated
- [ ] Changelog updated

### PR Checklist
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation
- [ ] Code refactoring
- [ ] Dependency update

## Testing
- [ ] All tests pass
- [ ] Added new tests
- [ ] Manual testing done

## Documentation
- [ ] Code documented
- [ ] User guide updated
- [ ] API docs updated

## Screenshots
(If applicable)

## Related Issues
Fixes #123
```

### Review Process
1. **Automated Checks:**
   - Code style
   - Type checking
   - Tests

2. **Code Review:**
   - Maintainer review
   - Feedback on changes
   - Suggestions for improvement

3. **Merge:**
   - After approval
   - All checks pass
   - Conflicts resolved

---

## 🎓 Development Setup

### Clone and Setup
```bash
# Clone your fork
git clone https://github.com/YOUR-USERNAME/ScrapeMatrix.git
cd ScrapeMatrix

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\Activate.ps1 on Windows

# Install in development mode
pip install -e ".[dev]"

# Install pre-commit hooks (optional)
pre-commit install
```

### Testing
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=scrapematrix

# Run specific test
pytest tests/test_loaders.py

# Run in verbose mode
pytest -v
```

### Code Quality
```bash
# Format code
black src/ tests/

# Check style
flake8 src/ tests/

# Type checking
mypy src/

# Full quality check
./scripts/quality_check.sh  # (once added)
```

---

## 💡 Good First Issues

### Beginner-Friendly
Look for issues labeled:
- `good first issue`
- `help wanted`
- `documentation`
- `easy`

### Examples
- Fix typos in documentation
- Add missing docstrings
- Improve error messages
- Add example code
- Create unit tests

---

## 🏗️ Project Structure for Contributors

Key directories:
```
src/scrapematrix/
├── data/          # Data loading and processing
├── gui/           # User interface components
└── models/        # Data models (future)

tests/             # Test files
docs/              # Documentation
```

---

## 📝 Commit Message Format

### Format
```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types
- **feat:** New feature
- **fix:** Bug fix
- **docs:** Documentation
- **style:** Code style changes
- **refactor:** Code refactoring
- **test:** Adding tests
- **chore:** Maintenance

### Examples
```
feat(ui): Add dark mode support

fix(loaders): Handle rate limit errors gracefully

docs(guide): Add troubleshooting section

refactor(data): Simplify ticker filtering logic
```

---

## 🔄 Collaboration

### Communication
- **GitHub Issues:** Bug reports and features
- **GitHub Discussions:** General questions
- **Pull Requests:** Code review and discussion

### Be Respectful
- Follow Code of Conduct
- Be respectful of others
- Welcome new contributors
- Help newcomers

---

## 🎯 Contribution Areas

### High Priority
- Bug fixes
- Performance improvements
- Documentation
- Testing

### Medium Priority
- New features
- Code refactoring
- UI improvements
- Error handling

### Wanted Contributions
- Unit tests
- Integration tests
- Documentation
- User guides
- Examples

---

## 🚀 Release Process

### Version Numbering
SemVer: MAJOR.MINOR.PATCH (e.g., 0.1.0)

### Release Cycle
- Major: When API changes
- Minor: When features added
- Patch: When bugs fixed

### Your Role
- Submit fixes and features
- Report issues
- Improve documentation
- Test releases

---

## ✨ Code Style Guidelines

### Python Style
```python
# Good
def fetch_data(ticker: str) -> Optional[pd.DataFrame]:
    """Fetch stock data."""
    # Implementation

# Bad
def fetch_data(ticker):
    # Implementation (no types, no docs)
```

### File Organization
```python
# 1. Docstring
"""Module docstring."""

# 2. Imports
import os
from typing import Optional

import pandas as pd

# 3. Constants
DEFAULT_PERIOD = "1y"

# 4. Classes
class DataLoader:
    pass

# 5. Functions
def load_data():
    pass

# 6. Main
if __name__ == "__main__":
    pass
```

---

## 🎁 Recognition

### Contributor Recognition
Contributors are recognized in:
- README.md contributors list
- CHANGELOG.md
- GitHub contributors page
- Release notes

### Ways to Contribute
- Code
- Documentation
- Testing
- Bug reports
- Design
- Marketing
- Community support

---

## 📚 Resources

### Development
- [Python Docs](https://docs.python.org/3/)
- [PyQt6 Docs](https://www.riverbankcomputing.com/static/Docs/PyQt6/)
- [Pandas Docs](https://pandas.pydata.org/docs/)

### Best Practices
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [Git Workflow](https://git-scm.com/doc)
- [Open Source Guide](https://opensource.guide/)

---

## ❓ Questions?

- **Issues:** GitHub Issues
- **Discussions:** GitHub Discussions  
- **Email:** Contact maintainers
- **Documentation:** Read docs/

---

## 🙏 Thank You!

Your contributions, no matter how small, make ScrapeMatrix better. Thank you for being part of the community!

---

**Last Updated:** 2026-03-16  
**Version:** 1.0  
**Status:** ✅ Complete
