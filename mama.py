import requests
import google.generativeai as genai
import os

# Configuration Constants
API_URL = "https://api-inference.huggingface.co/models/microsoft/trocr-base-handwritten"
HEADERS = {"Authorization": "Bearer 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"}
API_KEY = "AIzaSyCoVWDIcVhf7QTYpOzwr2ScYi_qRj40X-U"

# Configuring Google API
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

# response = model.generate_content("What is the meaning of life")
# print(response.text)

def create_flashcard_prompt(image_filename):
    # Text recognition from image
    with open(image_filename, "rb") as f:
        image_data = f.read()
        try:
            ocr_response = requests.post(API_URL, headers=HEADERS, data=image_data)
            ocr_response.raise_for_status()  # Raises an HTTPError for bad responses
            generated_text = ocr_response.json()[0]["generated_text"]
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            return None
        except KeyError:
            print("Error processing JSON response")
            return None

    # Generate flashcards based on OCR result
    prompt = f"""I want you to create a flashcards for a given topic. Each flashcard consists of the front and back side. 
    Front of the Flashcard: This side should have a question or a key concept that triggers your memory. Think of it as the prompt for your brain. For example, if you are learning Spanish, you might write, 'How do you say ‘apple’ in Spanish?' Make sure it's clear and concise.
    Back of the Flashcard: This side should answer the question or explain the concept from the front. Continuing our example, you would write 'Manzana', which is the Spanish word for 'apple'. Here, you can include additional details to help clarify the answer if necessary, like an image of an apple or a sentence using the word.
    Limit both front and back side to 100 characters.
    
    Write them in the following format: 
    1
    Front: text for front of the Flashcard
    Back: back for back of the Flashcard
    2
    Front: text for front of the Flashcard
    Back: back for back of the Flashcard
    Create at least 5 of flashcards on the topic in provided text: {generated_text}"""

    print(prompt)
    
    # Get response from Gemini model
    response = model.generate_content(prompt)
    return response.text


# Example usage
image_file = "IMG_0328.jpg"
output_text = create_flashcard_prompt(image_file)
print(output_text)
