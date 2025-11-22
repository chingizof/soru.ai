"""
YouTube utilities for extracting video transcripts.
"""

from youtube_transcript_api import YouTubeTranscriptApi
from typing import Optional


def extract_video_id(url: str) -> Optional[str]:
    """
    Extract video ID from a YouTube URL.
    
    Args:
        url: YouTube video URL
        
    Returns:
        Video ID if found, None otherwise
    """
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    return None


async def get_video_transcript(video_id: str, languages: list = ['en', 'ru']) -> Optional[str]:
    """
    Get transcript from a YouTube video.
    
    Args:
        video_id: YouTube video ID
        languages: List of language codes to try (default: ['en', 'ru'])
        
    Returns:
        Combined transcript text if successful, None otherwise
    """
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=languages)
        
        # Combine all transcript segments
        content = " ".join([line['text'] for line in transcript_list])
        return content
        
    except Exception as e:
        print(f"❌ Failed to get YouTube transcript: {e}")
        return None

