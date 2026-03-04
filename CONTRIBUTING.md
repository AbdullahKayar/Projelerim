<div align="center">

# 🤝 Contributing Guidelines | Katkı Rehberi

**Thank you for your interest in contributing to the FIFA 2022 World Cup Data Analysis project!**

**FIFA 2022 Dünya Kupası Veri Analizi projesine katkıda bulunmaya ilgi gösterdiğiniz için teşekkür ederiz!**

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)](http://makeapullrequest.com)
[![Code of Conduct](https://img.shields.io/badge/code%20of-conduct-ff69b4.svg?style=for-the-badge)](CODE_OF_CONDUCT.md)

</div>

---

## 📋 Table of Contents | İçindekiler

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Workflow](#development-workflow)
- [Style Guidelines](#style-guidelines)
- [Commit Messages](#commit-messages)
- [Pull Request Process](#pull-request-process)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Enhancements](#suggesting-enhancements)

---

## 📜 Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

Bu proje ve buna katılan herkes [Davranış Kurallarımız](CODE_OF_CONDUCT.md) tarafından yönetilir. Katılarak bu kurallara uymanız beklenir.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- A GitHub account

### Setting Up Your Development Environment

1. **Fork the repository**
   ```bash
   # Click the 'Fork' button on GitHub
   ```

2. **Clone your fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/fifa2022-analysis.git
   cd fifa2022-analysis
   ```

3. **Add upstream remote**
   ```bash
   git remote add upstream https://github.com/ORIGINAL_OWNER/fifa2022-analysis.git
   ```

4. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

5. **Install development dependencies**
   ```bash
   pip install -r requirements-dev.txt
   ```

---

## 💡 How Can I Contribute?

### 🔍 Reporting Bugs

Before creating bug reports, please check the existing issues to see if the problem has already been reported.

**How to submit a good bug report:**

1. **Use the bug report template** when creating a new issue
2. **Use a clear and descriptive title**
3. **Describe the exact steps to reproduce the problem**
4. **Provide specific examples** (code snippets, commands)
5. **Describe the behavior you observed** and what behavior you expected
6. **Include screenshots** if applicable

### 💡 Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues.

**How to submit a good enhancement suggestion:**

1. **Use a clear and descriptive title**
2. **Provide a step-by-step description** of the suggested enhancement
3. **Provide specific examples** to demonstrate the enhancement
4. **Explain why this enhancement would be useful**

### 📝 Pull Requests

1. **Fill in the required template** (PR template will be provided)
2. **Do not include issue numbers in the PR title**
3. **Include screenshots and animated GIFs** in your pull request whenever possible
4. **Follow our style guidelines** (see below)
5. **Document new code** based on the Documentation Styleguide
6. **End all files with a newline**

---

## 🔄 Development Workflow

### Branch Naming Convention

| Type | Pattern | Example |
|------|---------|---------|
| Feature | `feature/description` | `feature/add-jupyter-notebooks` |
| Bugfix | `bugfix/description` | `bugfix/fix-chart-labels` |
| Documentation | `docs/description` | `docs/update-api-reference` |
| Hotfix | `hotfix/description` | `hotfix/critical-data-bug` |

### Syncing Your Fork

```bash
# Fetch upstream changes
git fetch upstream

# Checkout main branch
git checkout main

# Merge upstream changes
git merge upstream/main

# Push to your fork
git push origin main
```

---

## 🎨 Style Guidelines

### Python Code Style

We follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) with the following preferences:

- **Line length**: 100 characters maximum
- **Indentation**: 4 spaces (no tabs)
- **Quotes**: Double quotes for strings
- **Docstrings**: Google style docstrings

```python
def calculate_efficiency(goals_scored: float, expected_goals: float) -> float:
    """Calculate goal efficiency ratio.
    
    Args:
        goals_scored: The actual number of goals scored.
        expected_goals: The expected goals (xG) metric.
        
    Returns:
        The efficiency ratio as a float.
        
    Raises:
        ZeroDivisionError: If expected_goals is zero.
        
    Example:
        >>> calculate_efficiency(5, 4.2)
        1.19
    """
    if expected_goals == 0:
        raise ZeroDivisionError("Expected goals cannot be zero")
    return goals_scored / expected_goals
```

### Code Quality Tools

We use the following tools to ensure code quality:

```bash
# Format code with Black
black src/ tests/

# Check code style with flake8
flake8 src/ tests/

# Run type checking with mypy
mypy src/

# Run tests with pytest
pytest tests/
```

### Documentation Style

- Use clear, concise language
- Include code examples where appropriate
- Keep line length to 80 characters for documentation
- Use proper Markdown formatting

---

## 📝 Commit Messages

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

### Format

```
<type>(<scope>): <description>

[optional body]

[optional footer(s)]
```

### Types

| Type | Description |
|------|-------------|
| `feat` | A new feature |
| `fix` | A bug fix |
| `docs` | Documentation only changes |
| `style` | Changes that don't affect code meaning (formatting) |
| `refactor` | Code change that neither fixes a bug nor adds a feature |
| `perf` | Code change that improves performance |
| `test` | Adding missing tests or correcting existing tests |
| `chore` | Changes to build process or auxiliary tools |

### Examples

```
feat(visualization): add interactive plotly charts

Add interactive charts using Plotly for better user experience.
Includes:
- Scatter plots with hover tooltips
- Zoom and pan functionality
- Export to HTML option

fix(data): handle missing values in group_stats

Resolves: #123

docs(readme): update installation instructions

Add detailed Windows installation steps and troubleshooting guide.
```

---

## 🔀 Pull Request Process

1. **Update the README.md** with details of changes to the interface, if applicable
2. **Update the CHANGELOG.md** with details of your changes
3. **Ensure all tests pass** before submitting
4. **Link any related issues** in the PR description
5. **Wait for review** - at least one maintainer must approve

### PR Checklist

- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes
- [ ] Any dependent changes have been merged and published

---

## 🌍 Türkçe Katkı Rehberi

### Başlarken

1. **Depoyu forklayın**
2. **Fork'unuzu klonlayın**
3. **Geliştirme ortamını kurun** (yukarıdaki adımları takip edin)
4. **Katkıda bulunun!**

### Hata Bildirimi

Hata bildirimleri için:
1. Açık ve açıklayıcı bir başlık kullanın
2. Problemi yeniden üretmek için tam adımları açıklayın
3. Beklenen ve gözlemlenen davranışı belirtin
4. Ekran görüntüleri ekleyin (varsa)

### Kod Stili

- [PEP 8](https://www.python.org/dev/peps/pep-0008/) standartlarını takip edin
- Satır uzunluğu: maksimum 100 karakter
- Girinti: 4 boşluk (tab kullanmayın)
- Google tarzı docstrings kullanın

---

## ❓ Questions?

If you have any questions, feel free to:
- Open an issue with the `question` label
- Contact the maintainers directly
- Check our [FAQ](docs/FAQ.md) (coming soon)

---

<div align="center">

**Thank you for contributing! Your efforts make this project better for everyone.**

**Katkılarınız için teşekkürler! Çabalarınız bu projeyi herkes için daha iyi hale getiriyor.**

🌟 **Happy Coding!** | **İyi Kodlamalar!** 🌟

</div>
