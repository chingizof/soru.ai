# Soru.ai Project Structure Guide

## 📁 Complete Directory Structure

```
soru.ai/
│
├── 📂 lahacks_24/                    # Main application package
│   ├── __init__.py                   # Package initializer
│   ├── lahacks_24.py                 # Main app with UI & state management
│   ├── config.py                     # Configuration & environment management
│   └── 📂 utils/                     # Utility modules
│       ├── __init__.py
│       ├── ocr.py                    # OCR processing (TrOCR)
│       ├── ai.py                     # AI flashcard generation (Gemini)
│       └── youtube.py                # YouTube transcript extraction
│
├── 📂 assets/                        # Static assets
│   ├── favicon.ico                   # Website favicon
│   └── IMG_0328.jpg                  # Sample image
│
├── 📂 uploaded_files/                # Temporary file storage (gitignored)
│   └── [User uploaded files]
│
├── 📂 docs/                          # Documentation
│   ├── API.md                        # API reference documentation
│   ├── SETUP.md                      # Detailed setup guide
│   └── ARCHITECTURE.md               # System architecture docs
│
├── 📂 .github/                       # GitHub configuration
│   ├── 📂 workflows/
│   │   └── ci.yml                    # GitHub Actions CI/CD pipeline
│   ├── 📂 ISSUE_TEMPLATE/
│   │   ├── bug_report.md            # Bug report template
│   │   └── feature_request.md       # Feature request template
│   └── PULL_REQUEST_TEMPLATE.md     # PR template
│
├── 📂 venv/                          # Virtual environment (gitignored)
│   └── [Python packages]
│
├── 📄 .env                           # Environment variables (gitignored)
├── 📄 env.example                    # Environment template (commit this)
├── 📄 .gitignore                     # Git ignore rules
│
├── 📄 requirements.txt               # Python dependencies
├── 📄 rxconfig.py                    # Reflex framework configuration
│
├── 📄 README.md                      # Main project documentation
├── 📄 CONTRIBUTING.md                # Contribution guidelines
├── 📄 CODE_OF_CONDUCT.md             # Community code of conduct
├── 📄 LICENSE                        # MIT License
├── 📄 SECURITY.md                    # Security policy
├── 📄 CHANGELOG.md                   # Version history
└── 📄 PROJECT_STRUCTURE.md           # This file
```

## 🎯 File Purposes

### Core Application Files

| File | Purpose | Key Features |
|------|---------|--------------|
| `lahacks_24/lahacks_24.py` | Main application logic | State management, UI components, routing |
| `lahacks_24/config.py` | Configuration management | Environment vars, validation, API keys |
| `lahacks_24/utils/ocr.py` | OCR processing | Handwriting recognition via TrOCR |
| `lahacks_24/utils/ai.py` | AI generation | Flashcard creation via Gemini |
| `lahacks_24/utils/youtube.py` | Video processing | Transcript extraction |

### Configuration Files

| File | Purpose | Commit to Git? |
|------|---------|----------------|
| `.env` | Actual API keys | ❌ Never |
| `env.example` | Template for .env | ✅ Yes |
| `.gitignore` | Ignore rules | ✅ Yes |
| `rxconfig.py` | Reflex config | ✅ Yes |
| `requirements.txt` | Dependencies | ✅ Yes |

### Documentation Files

| File | Audience | Content |
|------|----------|---------|
| `README.md` | Everyone | Overview, quick start, features |
| `docs/SETUP.md` | New developers | Detailed setup instructions |
| `docs/API.md` | Developers | API reference, functions |
| `docs/ARCHITECTURE.md` | Technical team | System design, data flow |
| `CONTRIBUTING.md` | Contributors | How to contribute |
| `SECURITY.md` | Security researchers | Security policy |

### GitHub Templates

| File | Purpose | When Used |
|------|---------|-----------|
| `.github/workflows/ci.yml` | Automated testing | Every push/PR |
| `.github/ISSUE_TEMPLATE/bug_report.md` | Bug reports | Creating issues |
| `.github/ISSUE_TEMPLATE/feature_request.md` | Feature requests | Creating issues |
| `.github/PULL_REQUEST_TEMPLATE.md` | Pull requests | Creating PRs |

## 🔄 Data Flow Through Files

### Image Upload Flow

```
User Upload
    ↓
lahacks_24.py (State.create_flashcard_prompt)
    ↓
utils/ocr.py (extract_text_from_image)
    ↓
utils/ai.py (create_flashcard_prompt + generate_flashcards)
    ↓
lahacks_24.py (split_flashcards_list)
    ↓
Display in UI
```

### YouTube Video Flow

```
User pastes URL
    ↓
lahacks_24.py (State.create_youtube_prompt)
    ↓
utils/youtube.py (extract_video_id + get_video_transcript)
    ↓
utils/ai.py (create_youtube_flashcard_prompt + generate_flashcards)
    ↓
lahacks_24.py (split_flashcards_list)
    ↓
Display in UI
```

## 🔐 Security Files

### Protected Files (Never Commit)

1. `.env` - Contains actual API keys
2. `uploaded_files/` - User uploaded content
3. `venv/` - Virtual environment
4. `.web/` - Build artifacts
5. `__pycache__/` - Python cache

### Security Best Practices

✅ **DO:**
- Use `env.example` as a template
- Validate all environment variables on startup
- Keep API keys in `.env` only
- Use `.gitignore` properly

❌ **DON'T:**
- Hardcode API keys in code
- Commit `.env` file
- Share API keys publicly
- Skip input validation

## 📦 Dependencies

### Core Dependencies

```
reflex==0.4.8.post1              # Web framework
google-generativeai==0.5.2       # AI generation
transformers==4.37.2             # ML models
requests==2.31.0                 # HTTP client
python-dotenv==1.0.0             # Environment vars
youtube-transcript-api==0.6.2    # YouTube integration
```

### Development Dependencies

```
pytest                           # Testing framework
black                            # Code formatter
flake8                          # Linter
bandit                          # Security scanner
```

## 🚀 Getting Started Checklist

- [ ] Clone repository
- [ ] Create virtual environment
- [ ] Install dependencies
- [ ] Copy `env.example` to `.env`
- [ ] Add API keys to `.env`
- [ ] Run `reflex init`
- [ ] Start application with `reflex run`
- [ ] Open browser to `http://localhost:3000`

## 📚 Documentation Reading Order

For new developers:

1. **Start Here**: `README.md` - Overview and quick start
2. **Setup**: `docs/SETUP.md` - Detailed installation
3. **Architecture**: `docs/ARCHITECTURE.md` - System design
4. **API Reference**: `docs/API.md` - Function documentation
5. **Contributing**: `CONTRIBUTING.md` - How to contribute

## 🛠️ Development Workflow

```
1. Read documentation
2. Set up development environment
3. Create feature branch
4. Make changes
5. Test locally
6. Create pull request
7. CI/CD runs automatically
8. Code review
9. Merge to main
```

## 📝 Code Organization Principles

### 1. Separation of Concerns
- UI logic in `lahacks_24.py`
- Business logic in `utils/`
- Configuration in `config.py`

### 2. Single Responsibility
- Each utility module has one purpose
- OCR, AI, and YouTube are separate

### 3. DRY (Don't Repeat Yourself)
- Shared functions in utils
- Configuration centralized
- Prompt templates reusable

### 4. Security First
- No hardcoded credentials
- Input validation everywhere
- Error handling comprehensive

## 🔍 Finding What You Need

**Want to change UI?**
→ `lahacks_24/lahacks_24.py`

**Want to modify OCR?**
→ `lahacks_24/utils/ocr.py`

**Want to change AI prompts?**
→ `lahacks_24/utils/ai.py`

**Want to add YouTube features?**
→ `lahacks_24/utils/youtube.py`

**Want to add dependencies?**
→ `requirements.txt`

**Want to configure app?**
→ `config.py` and `.env`

## 📊 File Statistics

- **Total Python files**: 7
- **Total documentation files**: 11
- **Total configuration files**: 6
- **Lines of code**: ~1,500+
- **Documentation lines**: ~2,000+

## 🎓 Learning Resources

### Understanding Reflex
- Official Docs: https://reflex.dev/docs
- Component Gallery: https://reflex.dev/docs/library

### Understanding AI APIs
- Google Gemini: https://ai.google.dev/
- Hugging Face: https://huggingface.co/docs

### Python Best Practices
- PEP 8: https://pep8.org/
- Type Hints: https://docs.python.org/3/library/typing.html

## 🤝 Contributing Areas

**Frontend**: Improve UI/UX in `lahacks_24.py`
**Backend**: Enhance utilities in `utils/`
**Documentation**: Update docs in `docs/`
**Testing**: Add tests (create `tests/` directory)
**CI/CD**: Improve `.github/workflows/`

## 📈 Future Structure Plans

Planned additions:

```
soru.ai/
├── 📂 tests/                   # Unit and integration tests
├── 📂 scripts/                 # Utility scripts
├── 📂 migrations/              # Database migrations (future)
├── 📂 static/                  # Additional static files
└── 📂 locales/                 # i18n translations (future)
```

## ✨ Pro Tips

1. **Always activate venv** before working
2. **Read docs/** before making changes
3. **Use env.example** never actual `.env`
4. **Test locally** before pushing
5. **Follow templates** for issues/PRs
6. **Ask questions** in discussions

---

**Last Updated**: November 2024
**Maintained By**: Soru.ai Team

For questions about project structure, see `CONTRIBUTING.md` or open a discussion on GitHub.

