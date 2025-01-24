
%%manim -qm -v ERROR AnimationVideo

from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
import numpy as np
import scipy as sp

LIGHT_GREEN = "#90EE90"  # LightGreen
LIGHT_BLUE = "#ADD8E6"   # LightBlue
LIGHT_YELLOW = "#FFFFE0" # LightYellow
BROWN = "#A52A2A"        # Brown
CYAN = "#00FFFF"         # Cyan

class AnimationVideo(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService())

        # Calling all scene methods
        scene_methods = [
            attr_name for attr_name in dir(self)
            if attr_name.startswith("play_scene_") and callable(getattr(self, attr_name))
        ]
        # Sorting all scene methods by id
        scene_methods.sort(key=lambda name: int(name.split('_')[-1]))

        # Executing methods for all scenes in order.
        for method_name in scene_methods:
            method = getattr(self, method_name)
            method()


    def play_scene_1(self):
        # Implementation: Setting dark blue background
        self.camera.background_color = DARK_BLUE

        # Implementation: Defining bag and card properties
        bag_color = BROWN
        card_color = WHITE
        number_color = BLACK
        text_color = WHITE

        # Implementation: Creating and positioning the bag
        # Thinking: Bag should be slightly below the center
        bag = Rectangle(color=bag_color, width=2, height=3, fill_opacity=0.5).shift(DOWN)

        cards = []
        for i in range(1, 31):
            # Implementation: Creating cards with numbers
            # Thinking: Cards should be positioned at the top-center initially
            number = Text(str(i), color=number_color)
            card = Rectangle(color=card_color, width=1, height=0.8, fill_opacity=1).shift(UP * 3)
            card.add(number)
            cards.append(card)

        # Implementation: Adding the bag to the scene
        self.add(bag)

        # Implementation: Animating the cards entering the bag
        with self.voiceover(text="Imagine you have a bag, and you're putting 30 cards into it, each with a unique number from 1 to 30.") as tracker:
            for i, card in enumerate(cards):
                self.play(Create(card), run_time=0.1)
                self.play(card.animate.move_to(bag.get_center() + UP * 0.5), run_time=tracker.duration / 30)
                self.play(FadeOut(card), run_time=0.1)

        # Cleaning: Keeping bag and fading out cards
        self.wait(0.5)

        # Implementation: Displaying the problem text below the bag
        problem_text = Text("Problem: Cards numbered 1 to 30 are put in a bag. A card is drawn at random.\n"
                            "Find the probability that the number on the drawn card is:\n"
                            "(i) not divisible by 3.\n"
                            "(ii) a prime number greater than 7.\n"
                            "(iii) not a perfect square number.", color=text_color, font_size=28).scale(0.8).next_to(bag, DOWN, buff=0.5)

        # Implementation: Animating the problem text
        with self.voiceover(text="Now, if you were to draw a card at random, what's the probability that the number on that card meets certain conditions? Specifically, we'll look at the probability of it not being divisible by 3, being a prime number greater than 7, and not being a perfect square number.") as tracker:
            self.play(Write(problem_text), run_time=tracker.duration)

        # Cleaning: Clearing all objects
        self.wait(0.5)
        self.clear()

    def play_scene_2(self):
        # Implementation: Setting dark blue background
        self.camera.background_color = DARK_BLUE

        # Implementation: Defining text color
        text_color = WHITE

        # Implementation: Displaying the probability formula
        # Thinking: Formula should be centered and divided into two lines
        probability_formula = Tex("Probability of an event =", "$\\frac{\\text{Number of favorable outcomes}}{\\text{Total number of possible outcomes}}$", color=text_color, font_size=36)
        probability_formula.scale(0.8).shift(UP * 0.5)

        # Implementation: Animating the probability formula
        with self.voiceover(text="Before we dive into the conditions, let's quickly recap what probability is. Simply put, the probability of an event is the number of favorable outcomes divided by the total number of possible outcomes.") as tracker:
            self.play(Write(probability_formula), run_time=tracker.duration)

        # Cleaning: No object should be cleared
        self.wait(0.5)

        # Implementation: Highlighting the denominator and moving the formula
        # Thinking: Formula should move to the top-left
        self.play(probability_formula[1][1].animate.set_color(YELLOW), run_time=0.5)
        self.play(probability_formula.animate.to_edge(UP).to_edge(LEFT), run_time=1)

        # Implementation: Displaying the total number of outcomes
        # Thinking: Text should be centered
        total_outcomes_text = Text("Total number of possible outcomes = 30", color=text_color, font_size=36).scale(0.8)

        # Implementation: Animating the total outcomes text
        with self.voiceover(text="In our case, since there are 30 cards, there are 30 possible outcomes.") as tracker:
            self.play(Write(total_outcomes_text), run_time=tracker.duration)

        # Cleaning: Clearing all objects
        self.wait(0.5)
        self.clear()

    def play_scene_3(self):
        # Implementation: Setting dark blue background
        self.camera.background_color = DARK_BLUE

        # Implementation: Defining text and highlight colors
        text_color = WHITE
        divisible_color = RED
        highlight_color = GREEN

        # Implementation: Displaying numbers divisible by 3
        # Thinking: Text should start at the top-left
        divisible_text = Text("Numbers divisible by 3:", color=text_color, font_size=36).to_edge(UP).to_edge(LEFT)
        divisible_numbers = Text("3, 6, 9, 12, 15, 18, 21, 24, 27, 30", color=divisible_color, font_size=36).next_to(divisible_text, RIGHT)

        # Implementation: Animating the divisible numbers
        with self.voiceover(text="First, let's find the probability of drawing a card with a number not divisible by 3. There are 10 numbers between 1 and 30 that are divisible by 3.") as tracker:
            self.play(Write(divisible_text), run_time=tracker.duration / 3)
            self.play(Write(divisible_numbers), run_time=tracker.duration * 2 / 3)

        # Cleaning: No object should be cleared
        self.wait(0.5)

        # Implementation: Calculating and displaying the probability
        # Thinking: Calculation should be below the list, slightly to the left
        calculation_text = Text("30 - 10 = 20 (numbers not divisible by 3)", color=text_color, font_size=30).next_to(divisible_numbers, DOWN).shift(LEFT * 1.5)
        probability_text = Text("Probability (not divisible by 3) = 20 / 30 = 2/3", color=text_color, font_size=30).next_to(calculation_text, RIGHT).shift(RIGHT * 0.5)
        highlight_prob = probability_text[-3:]

        # Implementation: Animating the calculation and probability
        with self.voiceover(text="That leaves us with 20 numbers that are not. So, the probability of drawing a card not divisible by 3 is 20 out of 30, which simplifies to 2/3.") as tracker:
            self.play(Write(calculation_text), run_time=tracker.duration / 2)
            self.play(Write(probability_text), run_time=tracker.duration / 2)
            self.play(highlight_prob.animate.set_color(highlight_color), run_time=0.5)

        # Cleaning: Clearing all objects
        self.wait(0.5)
        self.clear()

    def play_scene_4(self):
        # Implementation: Setting dark blue background
        self.camera.background_color = DARK_BLUE

        # Implementation: Defining text and highlight colors
        text_color = WHITE
        prime_color = YELLOW
        highlight_color = GREEN

        # Implementation: Displaying the definition of a prime number
        # Thinking: Text should be at the top, divided into two lines
        prime_definition = Text("Prime number: a whole number greater than 1 that has only two divisors: 1 and itself", color=text_color, font_size=30).scale(0.8).to_edge(UP)

        # Implementation: Listing prime numbers
        # Thinking: List should be below the definition
        prime_numbers = Text("2, 3, 5, 7, 11, 13, 17, 19, 23, 29", color=prime_color, font_size=30).scale(0.8).next_to(prime_definition, DOWN)

        # Implementation: Animating the definition and prime numbers
        with self.voiceover(text="Next, what's the probability of drawing a prime number greater than 7? A prime number is a number greater than 1 that has only two divisors: 1 and itself.") as tracker:
            self.play(Write(prime_definition), run_time=tracker.duration * 2 / 3)
            self.play(Write(prime_numbers), run_time=tracker.duration / 3)

        # Cleaning: No object should be cleared
        self.wait(0.5)

        # Implementation: Removing all prime numbers except those greater than 7
        self.remove(prime_numbers)
        prime_numbers_gt7 = Text("11, 13, 17, 19, 23, 29", color=highlight_color, font_size=30).scale(0.8).next_to(prime_definition, DOWN)

        # Implementation: Calculating and displaying the probability
        # Thinking: Calculation should be on the right side of the list
        probability_calculation = Text("Probability (prime > 7) = 6 / 30 = 1/5", color=text_color, font_size=30).scale(0.8).next_to(prime_numbers_gt7, RIGHT).shift(RIGHT * 0.5)
        highlight_prob = probability_calculation[-3:]

        # Implementation: Animating the prime numbers greater than 7 and the probability
        with self.voiceover(text="Between 1 and 30, there are six prime numbers greater than 7. Thus, the probability is 6 out of 30, which simplifies to 1/5.") as tracker:
            self.play(Write(prime_numbers_gt7), run_time=tracker.duration / 2)
            self.play(Write(probability_calculation), run_time=tracker.duration / 2)
            self.play(highlight_prob.animate.set_color(highlight_color), run_time=0.5)

        # Cleaning: Clearing all objects
        self.wait(0.5)
        self.clear()

    def play_scene_5(self):
        # Implementation: Setting dark blue background
        self.camera.background_color = DARK_BLUE

        # Implementation: Defining text and highlight colors
        text_color = WHITE
        perfect_square_color = ORANGE
        highlight_color = GREEN

        # Implementation: Displaying the definition of a perfect square
        # Thinking: Text should be at the top, divided into two lines
        perfect_square_definition = Text("Perfect square: a number that is the result of squaring a whole number", color=text_color, font_size=30).scale(0.8).to_edge(UP)

        # Implementation: Listing perfect squares
        # Thinking: List should be at the center
        perfect_squares = Text("1, 4, 9, 16, 25", color=perfect_square_color, font_size=30).scale(0.8).move_to(ORIGIN)

        # Implementation: Animating the definition and perfect squares
        with self.voiceover(text="Finally, let's consider the probability of drawing a card that is not a perfect square number. A perfect square is a number that results from squaring a whole number.") as tracker:
            self.play(Write(perfect_square_definition), run_time=tracker.duration * 2 / 3)
            self.play(Write(perfect_squares), run_time=tracker.duration / 3)

        # Cleaning: No object should be cleared
        self.wait(0.5)

        # Implementation: Calculating and displaying the probability
        # Thinking: Calculation should be below the list, slightly to the left
        calculation_text = Text("30 - 5 = 25 (numbers not perfect squares)", color=text_color, font_size=30).scale(0.8).next_to(perfect_squares, DOWN).shift(LEFT * 1.5)
        probability_text = Text("Probability (not a perfect square) = 25 / 30 = 5/6", color=text_color, font_size=30).scale(0.8).next_to(calculation_text, RIGHT).shift(RIGHT * 0.5)
        highlight_prob = probability_text[-3:]

        # Implementation: Animating the calculation and probability
        with self.voiceover(text="There are five perfect squares between 1 and 30. Therefore, 25 numbers are not perfect squares. The probability of drawing such a card is 25 out of 30, simplifying to 5/6.") as tracker:
            self.play(Write(calculation_text), run_time=tracker.duration / 2)
            self.play(Write(probability_text), run_time=tracker.duration / 2)
            self.play(highlight_prob.animate.set_color(highlight_color), run_time=0.5)

        # Cleaning: Clearing all objects
        self.wait(0.5)
        self.clear()

    def play_scene_6(self):
        # Implementation: Setting dark blue background
        self.camera.background_color = DARK_BLUE

        # Implementation: Defining text and highlight colors
        text_color = WHITE
        highlight_color = YELLOW

        # Implementation: Displaying the summary heading
        # Thinking: Text should be at the top-center
        summary_heading = Text("Summary:", color=text_color, font_size=48).to_edge(UP)

        # Implementation: Listing probabilities
        # Thinking: List should be below the heading, one below the other
        probability_1 = Text("(i) Probability of not divisible by 3: 2/3", color=text_color, font_size=36).next_to(summary_heading, DOWN, buff=1).align_to(summary_heading, LEFT)
        probability_2 = Text("(ii) Probability of a prime number greater than 7: 1/5", color=text_color, font_size=36).next_to(probability_1, DOWN, buff=0.5).align_to(probability_1, LEFT)
        probability_3 = Text("(iii) Probability of not a perfect square: 5/6", color=text_color, font_size=36).next_to(probability_2, DOWN, buff=0.5).align_to(probability_1, LEFT)

        # Implementation: Highlighting each probability
        highlight_prob_1 = probability_1[-3:]
        highlight_prob_2 = probability_2[-3:]
        highlight_prob_3 = probability_3[-3:]

        # Implementation: Animating the summary and probabilities
        with self.voiceover(text="To recap, the probability of not drawing a number divisible by 3 is 2/3, the probability of drawing a prime number greater than 7 is 1/5, and the probability of not drawing a perfect square number is 5/6.") as tracker:
            self.play(Write(summary_heading), run_time=tracker.duration / 4)
            self.play(Write(probability_1), run_time=tracker.duration / 4)
            self.play(highlight_prob_1.animate.set_color(highlight_color), run_time=0.5)
            self.play(Write(probability_2), run_time=tracker.duration / 4)
            self.play(highlight_prob_2.animate.set_color(highlight_color), run_time=0.5)
            self.play(Write(probability_3), run_time=tracker.duration / 4)
            self.play(highlight_prob_3.animate.set_color(highlight_color), run_time=0.5)

        # Cleaning: Clearing all objects
        self.wait(0.5)
        self.clear()

    def play_scene_7(self):
        # Implementation: Setting dark blue background
        self.camera.background_color = DARK_BLUE

        # Implementation: Defining text color
        text_color = WHITE

        # Implementation: Displaying the key concepts heading
        # Thinking: Text should be at the top-center
        key_concepts_heading = Text("Key Concepts:", color=text_color, font_size=48).to_edge(UP)

        # Implementation: Listing key concepts
        # Thinking: List should be below the heading, one below the other
        concept_1 = Text("Probability", color=text_color, font_size=36).next_to(key_concepts_heading, DOWN, buff=1).align_to(key_concepts_heading, LEFT)
        concept_2 = Text("Favorable Outcomes", color=text_color, font_size=36).next_to(concept_1, DOWN, buff=0.5).align_to(concept_1, LEFT)
        concept_3 = Text("Total Possible Outcomes", color=text_color, font_size=36).next_to(concept_2, DOWN, buff=0.5).align_to(concept_1, LEFT)
        concept_4 = Text("Divisibility", color=text_color, font_size=36).next_to(concept_3, DOWN, buff=0.5).align_to(concept_1, LEFT)
        concept_5 = Text("Prime Numbers", color=text_color, font_size=36).next_to(concept_4, DOWN, buff=0.5).align_to(concept_1, LEFT)
        concept_6 = Text("Perfect Squares", color=text_color, font_size=36).next_to(concept_5, DOWN, buff=0.5).align_to(concept_1, LEFT)

        # Implementation: Animating the key concepts
        with self.voiceover(text="Throughout this video, we've touched upon several key concepts: Probability, favorable outcomes, total possible outcomes, divisibility, prime numbers, and perfect squares. Understanding these concepts is crucial for solving problems like this one.") as tracker:
            self.play(Write(key_concepts_heading), run_time=tracker.duration / 7)
            self.play(Write(concept_1), run_time=tracker.duration / 7)
            self.play(Write(concept_2), run_time=tracker.duration / 7)
            self.play(Write(concept_3), run_time=tracker.duration / 7)
            self.play(Write(concept_4), run_time=tracker.duration / 7)
            self.play(Write(concept_5), run_time=tracker.duration / 7)
            self.play(Write(concept_6), run_time=tracker.duration / 7)

        # Cleaning: Clearing all objects
        self.wait(0.5)
        self.clear()