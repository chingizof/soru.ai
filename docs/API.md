# Soru.ai API Documentation

## Overview

This document describes the internal API and key functions used in Soru.ai.

## Configuration Module

### `config.py`

#### `Config` Class

Central configuration management for the application.

**Attributes:**
- `GOOGLE_API_KEY` (str): Google Gemini API key
- `HUGGINGFACE_API_KEY` (str): Hugging Face API token
- `HUGGINGFACE_API_URL` (str): TrOCR model endpoint URL
- `APP_NAME` (str): Application identifier
- `DEBUG` (bool): Debug mode flag

**Methods:**

##### `validate() -> bool`
Validates that all required environment variables are set.

**Returns:** `True` if all required values are present, `False` otherwise

##### `get_headers() -> dict`
Gets HTTP headers for Hugging Face API requests.

**Returns:** Dictionary with authorization headers

---

## Utility Modules

### OCR Module (`utils/ocr.py`)

#### `extract_text_from_image(image_data: bytes) -> Optional[str]`

Extracts text from an image using Microsoft's TrOCR model.

**Parameters:**
- `image_data` (bytes): Binary image data to process

**Returns:** Extracted text string, or `None` if extraction fails

**Raises:** `requests.RequestException` if the API request fails

**Example:**
```python
with open("notes.jpg", "rb") as f:
    image_data = f.read()
    
text = await extract_text_from_image(image_data)
print(f"Extracted: {text}")
```

---

### AI Module (`utils/ai.py`)

#### `create_flashcard_prompt(extracted_text: str) -> str`

Creates a formatted prompt for generating flashcards from extracted text.

**Parameters:**
- `extracted_text` (str): Text extracted from notes or transcripts

**Returns:** Formatted prompt string for the AI model

#### `create_youtube_flashcard_prompt(transcript: str) -> str`

Creates a formatted prompt for generating flashcards from YouTube transcripts.

**Parameters:**
- `transcript` (str): Full transcript of the YouTube video

**Returns:** Formatted prompt string for the AI model

#### `generate_flashcards(prompt: str) -> str`

Generates flashcards using Google Gemini AI model.

**Parameters:**
- `prompt` (str): Formatted prompt containing the learning content

**Returns:** Generated flashcard content in the specified format

**Raises:** `Exception` if AI generation fails

**Example:**
```python
prompt = create_flashcard_prompt("Python is a programming language")
flashcards = await generate_flashcards(prompt)
```

---

### YouTube Module (`utils/youtube.py`)

#### `extract_video_id(url: str) -> Optional[str]`

Extracts video ID from a YouTube URL.

**Parameters:**
- `url` (str): YouTube video URL

**Returns:** Video ID string, or `None` if not found

**Supported URL formats:**
- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`

**Example:**
```python
video_id = extract_video_id("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
# Returns: "dQw4w9WgXcQ"
```

#### `get_video_transcript(video_id: str, languages: list = ['en', 'ru']) -> Optional[str]`

Gets transcript from a YouTube video.

**Parameters:**
- `video_id` (str): YouTube video ID
- `languages` (list): List of language codes to try (default: `['en', 'ru']`)

**Returns:** Combined transcript text, or `None` if retrieval fails

**Example:**
```python
transcript = await get_video_transcript("dQw4w9WgXcQ")
print(f"Transcript: {transcript[:100]}...")
```

---

## State Management

### `State` Class (Main Application)

Reflex state management for the application.

**Attributes:**
- `img` (list): List of uploaded image filenames
- `cards_list` (list[tuple[str, str]]): Flashcard pairs (front, back)
- `visual_cards_list` (list[str]): Currently visible card sides
- `flash_text` (str): Raw AI-generated flashcard text
- `processing` (bool): Processing status indicator
- `complete` (bool): Completion status flag
- `yt_link` (str): YouTube video URL
- `yt_transcript` (str): Extracted YouTube transcript

**Methods:**

#### `split_flashcards_list(data: list[str])`

Parses AI-generated text into structured flashcard pairs.

**Parameters:**
- `data` (list[str]): List of lines from AI output

**Processing:**
1. Removes empty entries and whitespace
2. Strips "Front:" and "Back:" prefixes
3. Creates (front, back) tuples
4. Updates state with flashcard data

#### `create_flashcard_prompt(files: list[rx.UploadFile])`

Processes uploaded images and generates flashcards.

**Parameters:**
- `files` (list): List of uploaded files from Reflex

**Workflow:**
1. Save uploaded files to disk
2. Extract text using OCR
3. Generate AI prompt
4. Create flashcards using Gemini
5. Parse and display results

#### `create_youtube_prompt(link: str)`

Extracts YouTube transcript and generates flashcards.

**Parameters:**
- `link` (str): Dictionary with YouTube URL in `prompt_text` field

**Workflow:**
1. Extract video ID from URL
2. Fetch video transcript
3. Generate AI prompt
4. Create flashcards using Gemini
5. Parse and display results

#### `swap_card(idx: int)`

Toggles between front and back of a flashcard.

**Parameters:**
- `idx` (int): Index of the flashcard to flip

#### `upload(files: list[rx.UploadFile])`

Handles file upload and redirects to flashcard view.

**Parameters:**
- `files` (list): List of uploaded files

**Returns:** Redirect to `/quizlet` page

---

## Response Formats

### Flashcard Format

AI generates flashcards in the following format:

```
Front: What is Python?
Back: A high-level programming language
Front: What is a variable?
Back: A container for storing data values
```

**Rules:**
- Each flashcard has exactly one "Front" and one "Back"
- Maximum 100 characters per side
- Question-answer format preferred
- No empty lines between cards

---

## Error Handling

All async functions include try-catch blocks and log errors:

```python
try:
    result = await some_operation()
except Exception as e:
    print(f"❌ Error: {e}")
    return None
```

**Error Indicators:**
- ❌ - Operation failed
- ⚠️ - Warning message
- ✅ - Success
- 📝 - Text processing
- 🎥 - Video processing
- 📸 - Image processing

---

## Environment Variables

Required environment variables:

| Variable | Description | Required |
|----------|-------------|----------|
| `GOOGLE_API_KEY` | Google Gemini API key | Yes |
| `HUGGINGFACE_API_KEY` | Hugging Face API token | Yes |
| `HUGGINGFACE_API_URL` | TrOCR endpoint URL | No (has default) |
| `APP_NAME` | Application name | No |
| `DEBUG` | Debug mode flag | No |

---

## Rate Limits

Be aware of API rate limits:

- **Google Gemini**: 60 requests per minute (free tier)
- **Hugging Face**: Varies by model and plan
- **YouTube Transcript API**: No official limit, but be respectful

---

## Best Practices

1. **Always validate configuration** before making API calls
2. **Handle errors gracefully** with user-friendly messages
3. **Log operations** for debugging purposes
4. **Sanitize user input** before processing
5. **Use async/await** for I/O operations
6. **Clean up temporary files** after processing

