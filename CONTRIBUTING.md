# Contributing to PDF Password Remover

🎉 Thank you for your interest in contributing to PDF Password Remover!
We welcome all contributions—bug reports, feature requests, documentation, and code.

## 🛠️ How to Contribute

### 1. Fork the Repository

Click the **Fork** button in the top-right corner of the [GitHub repo](https://github.com/thecasualdev17/pdf-password-remover) and clone your fork locally:

```bash
git clone https://github.com/thecasualdev17/pdf-password-remover.git
cd pdf-password-remover
```

### 2. Set Up Your Environment
Make sure you have Python 3.9+ and install the dependencies using Poetry:

```bash
poetry install
```

### 3. Create a Branch
Use descriptive names like `fix-batch-processing` or `feature-gui-enhancement`.

```bash
git checkout -b feature-your-description
```

### 4. Make your changes

- Follow the existing code style and structure in `src/pdf_password_remover/`.
- Add or update tests in the `tests/` directory if applicable.
- Update documentation (README, docstrings) as needed.

### 5. Test your changes

Run the CLI and tests to ensure everything works:

```bash
poetry run pdf-password-remover remove-password --help
# (run your feature or fix)
# If tests exist:
pytest
```

### 6. Commit and Push

```bash
git add .
git commit -m "Describe your change"
git push origin feature-your-description
```

### 7. Open a Pull Request

Go to your fork on GitHub and open a Pull Request to the `main` branch. Describe your changes and reference any related issues.

---

## Code of Conduct

Please read and follow our [Code of Conduct](CODE_OF_CONDUCT.md).

## Security

If you discover a security vulnerability, please see our [Security Policy](SECURITY.md).

Thank you for helping make PDF Password Remover better!
