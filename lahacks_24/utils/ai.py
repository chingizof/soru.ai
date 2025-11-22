"""
AI utilities for generating flashcards using Google Gemini.
"""

import google.generativeai as genai
from ..config import Config

# Configure Google Gemini API
genai.configure(api_key=Config.GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')


def create_flashcard_prompt(extracted_text: str) -> str:
    """
    Create a prompt for generating flashcards from extracted text.
    
    Args:
        extracted_text: Text extracted from notes or transcripts
        
    Returns:
        Formatted prompt for the AI model
    """
    return f"""I want you to create flashcards for a given topic. Each flashcard consists of the front and back side. 

Front of the Flashcard: This side should have a question or a key concept that triggers your memory. Think of it as the prompt for your brain. For example, if you are learning Spanish, you might write, 'How do you say 'apple' in Spanish?' Make sure it's clear and concise.

Back of the Flashcard: This side should answer the question or explain the concept from the front. Continuing our example, you would write 'Manzana', which is the Spanish word for 'apple'. Here, you can include additional details to help clarify the answer if necessary, like an image of an apple or a sentence using the word.

Limit both front and back side to 100 characters. VERY IMPORTANT - stick strictly to question-answer format.

Write them in the following format, without spaces: 
Front: text for front of the Flashcard
Back: text for back of the Flashcard
Front: text for front of the Flashcard
Back: text for back of the Flashcard

Create at least 5 flashcards on the topic in provided text: {extracted_text}"""


def create_youtube_flashcard_prompt(transcript: str) -> str:
    """
    Create a prompt for generating flashcards from YouTube video transcripts.
    
    Args:
        transcript: Full transcript of the YouTube video
        
    Returns:
        Formatted prompt for the AI model
    """
    return f"""I want you to create flashcards for a given transcript from a YouTube video, act like this is a university lecture. Each flashcard consists of the front and back side. 

Front of the Flashcard: This side should have a question or a key concept that triggers your memory. Think of it as the prompt for your brain. For example, if you are learning Spanish, you might write, 'How do you say 'apple' in Spanish?' Make sure it's clear and concise.

Back of the Flashcard: This side should answer the question or explain the concept from the front. Continuing our example, you would write 'Manzana', which is the Spanish word for 'apple'. Here, you can include additional details to help clarify the answer if necessary, like an image of an apple or a sentence using the word.

Limit both front and back side to 100 characters.

Write them in the following format, without spaces: 
Front: text for front of the Flashcard
Back: text for back of the Flashcard
Front: text for front of the Flashcard
Back: text for back of the Flashcard

Create at least 5 flashcards on the topic in provided transcript: {transcript}"""


async def generate_flashcards(prompt: str) -> str:
    """
    Generate flashcards using Google Gemini AI model.
    
    Args:
        prompt: Formatted prompt containing the learning content
        
    Returns:
        Generated flashcard content in the specified format
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"❌ AI generation failed: {e}")
        raise

