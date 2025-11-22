"""
OCR (Optical Character Recognition) utilities for processing handwritten notes.
"""

import requests
from typing import Optional
from ..config import Config


async def extract_text_from_image(image_data: bytes) -> Optional[str]:
    """
    Extract text from an image using Microsoft's TrOCR model.
    
    Args:
        image_data: Binary image data to process
        
    Returns:
        Extracted text if successful, None otherwise
        
    Raises:
        requests.RequestException: If the API request fails
    """
    try:
        response = requests.post(
            Config.HUGGINGFACE_API_URL,
            headers=Config.get_headers(),
            data=image_data
        )
        response.raise_for_status()
        
        result = response.json()
        if isinstance(result, list) and len(result) > 0:
            return result[0].get("generated_text", "")
        
        return None
        
    except requests.RequestException as e:
        print(f"❌ OCR request failed: {e}")
        raise
    except (KeyError, IndexError) as e:
        print(f"❌ Error processing OCR response: {e}")
        return None

