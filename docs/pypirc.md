# Using `.pypirc` with Test PyPI

## Overview

The `.pypirc` file is a configuration file used by Python packaging tools (like `twine`) to store PyPI repository credentials and settings. It's typically located at `$HOME/.pypirc` on Unix-like systems or `%USERPROFILE%\. pypirc` on Windows.

## Configuration Format

Create or edit `$HOME/.pypirc` with the following structure:

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-YOUR-PRODUCTION-TOKEN-HERE

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-YOUR-TEST-TOKEN-HERE
```

## Getting Your API Token

1. Register at [test.pypi.org](https://test.pypi.org/account/register/)
2. Navigate to Account Settings → API tokens
3. Click "Add API token" and set an appropriate scope
4. Copy the generated token (starts with `pypi-`)

## Uploading to Test PyPI

Once configured, upload your package using `twine`:

```bash
# Build your package first
python -m build

# Upload to Test PyPI
twine upload --repository testpypi dist/*
```

## Installing from Test PyPI

To install and test your package:

```bash
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ your-package-name
```

The `--extra-index-url` ensures dependencies are pulled from the main PyPI if not available on Test PyPI.

## Security Best Practices

- **Set proper permissions**: `chmod 600 ~/.pypirc` (Unix-like systems only)
- Use API tokens instead of passwords
- Never commit `.pypirc` to version control
- Use different tokens for Test PyPI and production PyPI
- Consider using keyring for credential storage as an alternative

## Troubleshooting

- **Authentication fails**:  Verify your token is correctly copied with no extra spaces
- **Wrong repository**:  Ensure the repository URL uses `https://test.pypi.org/legacy/`
- **File not found**: Check the file is at `~/.pypirc` and properly formatted
