# Soru.ai Architecture

## System Overview

Soru.ai is a full-stack web application built with Python, leveraging modern AI technologies to transform educational content into interactive flashcards.

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                        User Interface                        │
│                     (Reflex Frontend)                        │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │ Image Upload │  │ YouTube Form │  │  Flashcards  │     │
│  └──────┬───────┘  └──────┬───────┘  └──────▲───────┘     │
└─────────┼──────────────────┼──────────────────┼────────────┘
          │                  │                  │
          ▼                  ▼                  │
┌─────────────────────────────────────────────────────────────┐
│                    Application Layer                         │
│                  (Reflex Backend / State)                    │
│  ┌──────────────────────────────────────────────────────┐   │
│  │              State Management                         │   │
│  │  • File handling    • Processing status              │   │
│  │  • Card storage     • User interaction               │   │
│  └──────────────────────────────────────────────────────┘   │
└────┬────────────────────┬──────────────────────┬────────────┘
     │                    │                      │
     ▼                    ▼                      ▼
┌─────────────┐    ┌─────────────┐      ┌─────────────┐
│  OCR Utils  │    │  AI Utils   │      │YouTube Utils│
│   (ocr.py)  │    │   (ai.py)   │      │(youtube.py) │
└──────┬──────┘    └──────┬──────┘      └──────┬──────┘
       │                  │                     │
       ▼                  ▼                     ▼
┌─────────────┐    ┌─────────────┐      ┌─────────────┐
│ Hugging Face│    │   Google    │      │  YouTube    │
│   TrOCR API │    │ Gemini API  │      │Transcript API│
└─────────────┘    └─────────────┘      └─────────────┘
```

## Component Architecture

### 1. Frontend Layer (Reflex UI)

**Technologies**: Reflex, React (compiled), JavaScript

**Components**:
- `navbar()`: Navigation bar with branding and links
- `main_banner()`: Hero section with tagline
- `index()`: Main landing page with upload forms
- `quizlet_page()`: Flashcard display and interaction
- `fb()`: Individual flashcard rendering

**Responsibilities**:
- User interface rendering
- File upload handling
- Flashcard display and interaction
- Visual feedback (loading states, animations)

### 2. Application Layer (State Management)

**Technologies**: Reflex State Management, Python

**Key State Variables**:
```python
class State(rx.State):
    img: list                    # Uploaded image filenames
    cards_list: list[tuple]      # (front, back) pairs
    visual_cards_list: list      # Currently visible sides
    flash_text: str              # Raw AI output
    processing: bool             # Processing indicator
    complete: bool               # Completion flag
```

**Responsibilities**:
- Managing application state
- Coordinating between UI and business logic
- Handling async operations
- Error management

### 3. Business Logic Layer (Utilities)

#### OCR Module (`utils/ocr.py`)

**Purpose**: Extract text from images

**Flow**:
```
Image Bytes → HTTP POST → TrOCR API → JSON Response → Extracted Text
```

**Key Function**:
```python
async def extract_text_from_image(image_data: bytes) -> Optional[str]
```

#### AI Module (`utils/ai.py`)

**Purpose**: Generate flashcards using AI

**Flow**:
```
Text Content → Prompt Creation → Gemini API → Flashcard Text
```

**Key Functions**:
```python
def create_flashcard_prompt(text: str) -> str
def create_youtube_flashcard_prompt(transcript: str) -> str
async def generate_flashcards(prompt: str) -> str
```

#### YouTube Module (`utils/youtube.py`)

**Purpose**: Extract video transcripts

**Flow**:
```
YouTube URL → Video ID Extraction → Transcript API → Combined Text
```

**Key Functions**:
```python
def extract_video_id(url: str) -> Optional[str]
async def get_video_transcript(video_id: str) -> Optional[str]
```

### 4. Configuration Layer

**File**: `config.py`

**Purpose**: 
- Environment variable management
- API configuration
- Validation

**Key Features**:
- Centralized configuration
- Automatic validation on import
- Secure credential handling

### 5. External Services

#### Google Gemini Pro
- **Purpose**: AI text generation
- **Model**: gemini-pro
- **Rate Limit**: 60 req/min (free tier)
- **Latency**: 2-5 seconds typical

#### Hugging Face TrOCR
- **Purpose**: Handwriting recognition
- **Model**: microsoft/trocr-base-handwritten
- **Rate Limit**: Varies by tier
- **Latency**: 3-10 seconds typical

#### YouTube Transcript API
- **Purpose**: Video transcript extraction
- **Method**: Scraping (unofficial)
- **Rate Limit**: None official
- **Latency**: 1-3 seconds typical

## Data Flow

### Image Upload Flow

```
1. User uploads image
   ↓
2. File saved to uploaded_files/
   ↓
3. Image data read as bytes
   ↓
4. OCR extraction (TrOCR API)
   ↓
5. Prompt creation with extracted text
   ↓
6. AI generation (Gemini API)
   ↓
7. Parse flashcard text
   ↓
8. Update state with flashcards
   ↓
9. Redirect to flashcard page
   ↓
10. Display interactive flashcards
```

### YouTube Video Flow

```
1. User pastes YouTube URL
   ↓
2. Extract video ID from URL
   ↓
3. Fetch transcript (YouTube API)
   ↓
4. Combine transcript segments
   ↓
5. Prompt creation with transcript
   ↓
6. AI generation (Gemini API)
   ↓
7. Parse flashcard text
   ↓
8. Update state with flashcards
   ↓
9. Display interactive flashcards
```

## File Structure

```
soru.ai/
├── lahacks_24/                 # Main application package
│   ├── __init__.py
│   ├── lahacks_24.py          # Main app logic & UI
│   ├── config.py              # Configuration management
│   └── utils/                 # Utility modules
│       ├── __init__.py
│       ├── ocr.py            # OCR processing
│       ├── ai.py             # AI generation
│       └── youtube.py        # YouTube integration
├── assets/                    # Static assets
│   ├── favicon.ico
│   └── IMG_0328.jpg
├── uploaded_files/           # Temporary uploads (gitignored)
├── .web/                     # Reflex build output (gitignored)
├── docs/                     # Documentation
│   ├── API.md
│   ├── SETUP.md
│   └── ARCHITECTURE.md
├── .github/                  # GitHub templates
│   ├── workflows/
│   │   └── ci.yml
│   ├── ISSUE_TEMPLATE/
│   └── PULL_REQUEST_TEMPLATE.md
├── .env                      # Environment variables (gitignored)
├── env.example              # Environment template
├── .gitignore
├── requirements.txt
├── rxconfig.py              # Reflex configuration
├── README.md
├── CONTRIBUTING.md
├── LICENSE
├── CODE_OF_CONDUCT.md
├── SECURITY.md
└── CHANGELOG.md
```

## Security Architecture

### API Key Management
- Environment variables via `.env`
- Validation on application startup
- Never exposed to frontend
- Separate keys for dev/prod

### File Upload Security
- Type validation (images only)
- Size limits enforced
- Temporary storage
- Automatic cleanup

### Input Sanitization
- URL validation for YouTube links
- File extension checking
- Content-type verification
- Character encoding validation

## Performance Considerations

### Optimization Strategies

1. **Async Operations**: All I/O operations use async/await
2. **Caching**: Browser caching for static assets
3. **Lazy Loading**: Components load on-demand
4. **Compression**: Images compressed before upload

### Bottlenecks

1. **API Latency**: 
   - OCR: 3-10 seconds
   - AI Generation: 2-5 seconds
   - Total: 5-15 seconds per request

2. **Rate Limits**:
   - Gemini: 60 requests/minute
   - TrOCR: Variable based on tier

### Scaling Considerations

**Current Architecture**: Suitable for 100-1000 users

**To Scale Beyond**:
1. Add caching layer (Redis)
2. Queue system for API calls (Celery)
3. Load balancer for multiple instances
4. CDN for static assets
5. Database for user data persistence

## Technology Stack Summary

| Layer | Technology | Version |
|-------|-----------|---------|
| Framework | Reflex | 0.4.8+ |
| Language | Python | 3.11+ |
| AI Model | Google Gemini Pro | Latest |
| OCR Model | TrOCR | microsoft/trocr-base-handwritten |
| Video API | YouTube Transcript API | 0.6.2 |
| Environment | python-dotenv | 1.0.0 |
| HTTP Client | requests | 2.31.0 |

## Future Architecture Improvements

1. **Database Integration**: PostgreSQL for user data
2. **Authentication**: OAuth2 with Google/GitHub
3. **Caching**: Redis for flashcard storage
4. **Queue System**: Celery for background processing
5. **CDN**: CloudFlare for asset delivery
6. **Monitoring**: Prometheus + Grafana
7. **Logging**: ELK stack (Elasticsearch, Logstash, Kibana)
8. **Testing**: Comprehensive unit and integration tests

## Development vs Production

### Development
- Debug mode enabled
- Local file storage
- No caching
- Verbose logging
- Hot reload enabled

### Production
- Debug mode disabled
- Cloud storage (S3/Azure Blob)
- Redis caching
- Error-level logging only
- Optimized builds
- HTTPS enforced
- Rate limiting enabled

## Deployment Architecture

```
┌──────────────┐
│   GitHub     │
│  Repository  │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ GitHub       │
│ Actions CI   │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│   Docker     │
│   Registry   │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  Cloud       │
│  Platform    │
│  (Vercel/    │
│   Railway)   │
└──────────────┘
```

---

**Last Updated**: November 2024
**Maintainer**: Soru.ai Team

