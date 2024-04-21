"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import reflex as rx
import copy
from .results import results
from typing import Any, List

question_style = {
    "bg": "white",
    "padding": "2em",
    "border_radius": "25px",
    "width": "100%",
    "align_items": "start",
}


class State(rx.State):
    """The app state."""

    default_answers = [None, None, [False, False, False, False, False]]
    answers: List[Any]
    answer_key = ["False", "[10, 20, 30, 40]", [False, False, True, True, True]]
    score: int

    def onload(self):
        self.answers = copy.deepcopy(self.default_answers)

    def set_answers(self, answer, index, sub_index=None):
        if sub_index is None:
            self.answers[index] = answer
        else:
            self.answers[index][sub_index] = answer

    def submit(self):
        total, correct = 0, 0
        for i in range(len(self.answers)):
            if self.answers[i] == self.answer_key[i]:
                correct += 1
            total += 1
        self.score = int(correct / total * 100)
        return rx.redirect("/result")

    @rx.var
    def percent_score(self):
        return f"{self.score}%"



def main_banner():
    """Creates a main banner similar to the KyoHealth example."""
    return rx.box(
        rx.text(
            "Your AI-powered Copilot for Education",
            style={
                "font_size": "3rem",  # Large font size for main heading
                "color": "#333",  # Dark text for contrast
                "text_align": "center",  # Centered text
                "margin": "1rem 0",  # Margin top and bottom
            }
        ),
        style = {
            "padding": "4rem 1rem",              # Padding around the text
            "border_radius": "0.75rem",           # Slight rounding of the corners
            "background": "rgba(255, 255, 255, 0.05)",  # Transparent white background
            "color": "white",                    # White text
            "width": "100%",                     # Full width of the banner
            "box_shadow": "0 4px 10px 0 rgba(0, 0, 0, 0.15)"  # Subtle shadow for depth
        }

    )


def navbar():
    """The navbar for the top of the page with 'Soru.ai' positioned more to the left."""
    return rx.box(
        rx.hstack(
            rx.link(
                rx.hstack(
                    rx.heading("Soru.ai", size="6", style={"margin-left": "0.5rem"}),  # Minimal left margin
                    align="center",
                ),
                href="/",
            ),
            rx.spacer(width="auto"),  # This automatically spaces the logo to the left
            rx.link("Contacts", href="/contacts", style={"margin-right": "20px"}), # Contacts Link
            rx.button("Sign Up", size="3", href="/signup", style={"background-color": "#635BFF", "color": "white"}), # Sign Up Button
        ),
        align="center",
        justify="start",  # Elements are aligned to start, minimizing space before 'Soru.ai'
        padding_x="0.5rem",  # Reduced padding on the left to bring 'Soru.ai' closer to the screen edge
        padding_y="0.5rem",
        bg="rgba(255,255,255, 0)",
        position="fixed",
        width="100%",
        top="0px",
        z_index="1000",
        shadow="0 1px 3px rgb(0 0 0 / 10%)",
    )



def question1():
    """The first question view with added top margin."""
    question1_style = copy.deepcopy(question_style)
    question1_style.update({"margin_top": "2em"})  # Adding top margin to the first question only

    return rx.vstack(
        rx.heading("Question #1"),
        rx.text(
            "In Python 3, the maximum value for an integer is 2",
            rx.text("63", as_="sup"),
            " - 1.",
        ),
        rx.divider(),
        rx.radio(
            items=["True", "False"],
            default_value=State.default_answers[0],
            on_change=lambda answer: State.set_answers(answer, 0),
        ),
        style=question1_style,
    )


def index():
    """The main view, including the banner."""
    return rx.center(
        rx.vstack(
            navbar(),
            main_banner(),  # Include the main banner here
            question1(),
            rx.button(
                "Submit",
                bg="black",
                color="white",
                width="6em",
                padding="1em",
                on_click=State.submit,
            ),
            spacing="2",
        ),
        padding_y="2em",
        height="100vh",
        align_items="top",
        bg="linear-gradient(to right, #614385, #516395)",  # Set gradient background here
        overflow="auto",
    )



def result():
    return results(State)


app = rx.App(
theme=rx.theme(
        has_background=True, radius="none", accent_color="gray", appearance="light",
    ),
)
app.add_page(index, title="Reflex Quiz", on_load=State.onload)
app.add_page(result, title="Quiz Results")