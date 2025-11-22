# Contributing to Soru.ai

First off, thank you for considering contributing to Soru.ai! It's people like you that make Soru.ai such a great tool for students worldwide.

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to conduct@soru.ai.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

* **Use a clear and descriptive title** for the issue
* **Describe the exact steps to reproduce the problem**
* **Provide specific examples** to demonstrate the steps
* **Describe the behavior you observed** and what behavior you expected to see
* **Include screenshots and animated GIFs** if possible
* **Include your environment details** (OS, Python version, browser)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

* **Use a clear and descriptive title**
* **Provide a step-by-step description** of the suggested enhancement
* **Provide specific examples** to demonstrate the steps
* **Describe the current behavior** and explain the behavior you expected to see
* **Explain why this enhancement would be useful** to most Soru.ai users

### Pull Requests

* Fill in the required template
* Do not include issue numbers in the PR title
* Include screenshots and animated GIFs in your pull request whenever possible
* Follow the Python style guides
* Include thoughtfully-worded, well-structured tests
* Document new code
* End all files with a newline

## Development Setup

1. Fork and clone the repository
   ```bash
   git clone https://github.com/your-username/soru.ai.git
   cd soru.ai
   ```

2. Create a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

5. Run the development server
   ```bash
   reflex run
   ```

## Style Guidelines

### Python Style Guide

* Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
* Use type hints where applicable
* Write descriptive docstrings for functions and classes
* Keep functions focused and small
* Use meaningful variable names

Example:
```python
async def process_image(image_path: str) -> str:
    """
    Process an uploaded image using OCR.
    
    Args:
        image_path: Path to the uploaded image file
        
    Returns:
        Extracted text from the image
        
    Raises:
        OCRError: If image processing fails
    """
    # Implementation here
    pass
```

### Commit Messages

* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or less
* Reference issues and pull requests liberally after the first line

Examples:
```
Add YouTube playlist support

- Extract videos from playlist URLs
- Generate combined flashcards from multiple videos
- Add progress tracking for batch processing

Closes #123
```

## Project Structure

```
soru.ai/
├── lahacks_24/           # Main application package
│   ├── __init__.py
│   ├── lahacks_24.py    # Main app logic
│   ├── config.py        # Configuration management
│   └── utils/           # Utility modules
├── assets/              # Static assets
├── tests/              # Test files
├── docs/               # Documentation
└── requirements.txt    # Dependencies
```

## Testing

* Write tests for new features
* Ensure all tests pass before submitting PR
* Aim for high test coverage

```bash
# Run tests
pytest

# Run with coverage
pytest --cov=lahacks_24
```

## Documentation

* Update README.md if you change functionality
* Add docstrings to new functions/classes
* Update API documentation for new endpoints
* Include examples for new features

## Review Process

1. **Automated checks**: CI/CD runs automated tests
2. **Code review**: At least one maintainer reviews the code
3. **Testing**: Reviewers test the changes locally
4. **Approval**: Maintainer approves and merges

## Priority Areas

We're especially interested in contributions in these areas:

1. **Multi-language support**: Expand beyond English/Russian
2. **Mobile optimization**: Improve mobile user experience
3. **Performance**: Optimize AI processing speed
4. **Export features**: Add Anki/Quizlet export
5. **Analytics**: Learning progress tracking
6. **Accessibility**: WCAG compliance improvements

## Getting Help

* Join our [Discord community](https://discord.gg/soruai)
* Check the [documentation](https://docs.soru.ai)
* Ask questions in GitHub Discussions
* Email: dev@soru.ai

## Recognition

Contributors will be:
* Listed in README.md
* Mentioned in release notes
* Given a shoutout on our social media
* Added to our Hall of Fame

Thank you for contributing to Soru.ai! 🎉

