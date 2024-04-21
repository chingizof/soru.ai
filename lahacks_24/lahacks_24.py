"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config
# from mama import create_flashcard_prompt
import reflex as rx


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

docs_url = "https://reflex.dev/docs/getting-started/introduction/"
filename = f"{config.app_name}/{config.app_name}.py"

class State(rx.State):
    img: list = []  # If this holds multiple image filenames
    cards_list: list[tuple[str, str]] = []  # Explicitly define the type as a list of tuples
    flash_text: str = ""
    processing: bool = False
    complete: bool = False
    test_card: list[tuple[str, str]] = [("Front: What is the capital of France?", "Back: Paris")]

    async def split_flashcards_list(self, data: list[str]):
        # Remove any empty entries and extra whitespace
        cleaned_data = [line.strip() for line in data if line.strip()]

        # Check if the number of elements in the list is even after cleaning
        if len(cleaned_data) % 2 != 0:
            raise ValueError("The number of flashcard elements must be even (each front should have a corresponding back).")

        # Create pairs of (front, back)
        flashcards = []
        for i in range(0, len(cleaned_data), 2):
            front = cleaned_data[i]
            back = cleaned_data[i+1]
            flashcards.append((front, back))
        
        self.cards_list = flashcards


    async def create_flashcard_prompt(self, files: list[rx.UploadFile]):
        self.processing = True

        # Handle the upload of file(s).
        for file in files:
            upload_data = await file.read()
            outfile = rx.get_upload_dir() / file.filename

            # Save the file.
            with outfile.open("wb") as file_object:
                file_object.write(upload_data)

            # Update the img var.
            # self.img = file.filename
            self.img.append(file.filename)

        print("Creating flashcard prompt")
        print(self.img)
        # Text recognition from image
        with open(file.filename, "rb") as f:
            image_data = f.read()

        print("read image data")
        ocr_response = requests.post(API_URL, headers=HEADERS, data=image_data)
        generated_text = ocr_response.json()[0]["generated_text"]
        print("generated text", generated_text)

        # Generate flashcards based on OCR result
        prompt = f"""I want you to create a flashcards for a given topic. Each flashcard consists of the front and back side. 
        Front of the Flashcard: This side should have a question or a key concept that triggers your memory. Think of it as the prompt for your brain. For example, if you are learning Spanish, you might write, 'How do you say ‘apple’ in Spanish?' Make sure it's clear and concise.
        Back of the Flashcard: This side should answer the question or explain the concept from the front. Continuing our example, you would write 'Manzana', which is the Spanish word for 'apple'. Here, you can include additional details to help clarify the answer if necessary, like an image of an apple or a sentence using the word.
        Limit both front and back side to 100 characters.
        
        Write them in the following format, without spaces: 
        Front: text for front of the Flashcard
        Back: back for back of the Flashcard
        Front: text for front of the Flashcard
        Back: back for back of the Flashcard
        Create at least 5 of flashcards on the topic in provided text: {generated_text}"""
        
        # Get response from Gemini model
        response = model.generate_content(prompt)
        self.flash_text = response.text
        print(self.flash_text)
        self.processing = False
        self.complete = True
        await self.split_flashcards_list(self.flash_text.split('\n'))  # Assuming flash_text contains data in a format splitable into flashcards


    



        


color = "rgb(107,99,246)"

def fb(card: tuple[str, str]):
    return rx.box(
        rx.box(card[0]),  # Front of card
        rx.box(card[1]),  # Back of card
        margin_bottom="10px",
    )



def index():
    """The main view."""
    return rx.vstack(
        rx.heading("Welcome to Suraq!"),
        rx.upload(
            rx.vstack(
                rx.button("Select File", color=color, bg="white", border=f"1px solid {color}"),
                rx.text("Drag and drop files here or click to select files"),
            ),
            id="upload1",
            border=f"1px dotted {color}",
            padding="5em",
        ),
        rx.hstack(rx.foreach(rx.selected_files("upload1"), rx.text)),
        rx.button(
            "Upload",
            on_click= State.create_flashcard_prompt(rx.upload_files(upload_id="upload1"), State.img),
        ),
        rx.button(
            "Clear",
            on_click=rx.clear_selected_files("upload1"),
        ),

        rx.cond(
            State.processing,
            rx.chakra.circular_progress(is_indeterminate=True),
            rx.cond(
                State.complete,
                # rx.box(State.flash_text)
                rx.box(
                    rx.foreach(State.cards_list, fb)
                ),
            )
        ),

        rx.foreach(State.img, lambda img: rx.image(src=rx.get_upload_url(State.img), 
                                                   width="50vw",
                                                   height="auto",
                                                   border="5px solid #555")),
        # rx.foreach(
        #     State.img,
        #     lambda img: rx.box(create_flashcard_prompt(img)),
        # ),
        padding="5em",
    )



app = rx.App()
app.add_page(index)
