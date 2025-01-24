
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
        # Implementation: Animate the word "Probability" at the top center
        probability_text = Text("Probability", font_size=48, weight=BOLD)
        # Thinking: Position the text at the top center of the screen
        probability_text.to_edge(UP)

        # Implementation: Animate the formula for probability below it
        formula_text = Text("Probability (Event) = ", font_size=36)
        # Thinking: Position the formula text below "Probability"
        formula_text.next_to(probability_text, DOWN, buff=0.5)

        # Implementation: Create the fraction animation
        numerator = Text("Number of favorable outcomes", font_size=30)
        denominator = Text("Total number of possible outcomes", font_size=30)
        fraction_line = Line(LEFT, RIGHT, stroke_width=2)
        # Thinking: Position the fraction line below the formula text
        fraction_line.next_to(formula_text, DOWN, buff=0.5)
        fraction_line.width = max(numerator.width, denominator.width) + 0.5
        # Thinking: Position the numerator above the fraction line
        numerator.next_to(fraction_line, UP, buff=0.3)
        # Thinking: Position the denominator below the fraction line
        denominator.next_to(fraction_line, DOWN, buff=0.3)

        # Implementation: Group the fraction components
        fraction_group = VGroup(numerator, fraction_line, denominator)

        # Implementation: Add voiceover for the first part
        with self.voiceover(text="Probability is a measure of the likelihood of an event occurring. It's expressed as a number between 0 and 1, where 0 means the event is impossible, and 1 means the event is certain.") as tracker:
            # Implementation: Show "Probability" text
            self.play(Write(probability_text))
            self.wait(0.5)
            # Implementation: Show "Probability (Event) = " text
            self.play(Write(formula_text))
            self.wait(0.5)
            # Implementation: Animate the fraction appearing
            self.play(Write(numerator))
            self.wait(0.5)
            self.play(Create(fraction_line))
            self.wait(0.5)
            self.play(Write(denominator))
            self.wait(tracker.duration - 1)

        # Implementation: Add voiceover for the second part
        with self.voiceover(text="The basic formula for probability is: Probability of an Event equals the Number of favorable outcomes divided by the Total number of possible outcomes.") as tracker:
            # Implementation: Keep fraction on screen and add explaining text
            explain_text = Text("The basic formula for probability is: Probability of an Event\n"
                                "equals the Number of favorable outcomes divided by the\n"
                                "Total number of possible outcomes.", font_size=24).next_to(fraction_group, DOWN, buff=1)
            self.play(Write(explain_text))
            self.wait(tracker.duration)

        # Cleaning: Clear all objects for the next scene
        self.clear()

    def play_scene_2(self):
        # Implementation: Display the problem statement text
        problem_statement = Text("Cards numbered 1 to 30 are put in a bag.\nA card is drawn at random from this bag.", font_size=36)
        # Thinking: Position the problem statement at the top of the screen
        problem_statement.to_edge(UP)

        # Implementation: Animate a bag appearing in the center
        bag = Rectangle(width=3, height=4, color=WHITE, fill_opacity=0.5)
        # Thinking: Position the bag in the center of the screen
        bag.move_to(ORIGIN)

        # Implementation: Create cards numbered 1 to 30
        cards = [Text(str(i), font_size=24) for i in range(1, 31)]
        # Thinking: Scale down cards to fit in frame
        for card in cards:
            card.scale(0.5)
        # Implementation: Position cards initially outside the bag
        for i, card in enumerate(cards):
            card.move_to(bag.get_center() + LEFT * 4 + UP * 2 - i * 0.2 * RIGHT)

        # Implementation: Add voiceover for the first part
        with self.voiceover(text="Let's consider a scenario where cards numbered 1 to 30 are put in a bag. A card is drawn at random from this bag.") as tracker:
            self.play(Write(problem_statement))
            self.wait(0.5)
            self.play(Create(bag))
            self.wait(0.5)
            # Implementation: Animate cards moving into the bag
            for card in cards:
                self.play(card.animate.move_to(bag.get_center()), run_time=0.2)
            self.wait(tracker.duration - 1)

        # Implementation: Add voiceover for the second part
        with self.voiceover(text="Now, we need to find the probability that the number on the drawn card satisfies certain conditions.") as tracker:
            # Implementation: Keep bag on the screen and add explaining text
            explain_text = Text("Now, we need to find the probability that the\nnumber on the drawn card satisfies certain conditions.", font_size=30).next_to(bag, DOWN, buff=1)
            self.play(Write(explain_text))
            self.wait(tracker.duration)

        # Cleaning: Clear all objects except the bag for the next scene
        self.remove(problem_statement, explain_text, *cards)

    def play_scene_3(self):
        # Implementation: Display the condition text
        condition_text = Text("(i) not divisible by 3", font_size=36)
        # Thinking: Position the condition text at the top left
        condition_text.to_edge(UP).to_edge(LEFT)

        # Implementation: List numbers divisible by 3
        divisible_by_3 = [Text(str(i), font_size=30) for i in range(3, 31, 3)]
        # Thinking: Position the list on the left side of the screen
        for i, num in enumerate(divisible_by_3):
            num.next_to(condition_text, DOWN, buff=0.5).shift(i * DOWN * 0.8 + RIGHT * 2)

        # Implementation: Add voiceover for the first part
        with self.voiceover(text="First, let's find the probability that the drawn card is not divisible by 3. There are 10 numbers between 1 and 30 that are divisible by 3.") as tracker:
            self.play(Write(condition_text))
            self.wait(0.5)
            # Implementation: Highlight each number as it appears
            for num in divisible_by_3:
                self.play(Write(num))
                self.play(num.animate.set_color(YELLOW))
            self.wait(tracker.duration - 1)

        # Implementation: Calculate numbers not divisible by 3
        calculation_text = Text("30 - 10 = 20", font_size=30)
        # Thinking: Position the calculation text below the list
        calculation_text.next_to(divisible_by_3[-1], DOWN, buff=0.8)

        # Implementation: Display the probability calculation
        probability_text = Text("So, there are 20 numbers not divisible by 3.\n20/30 = 2/3", font_size=30)
        # Thinking: Position the probability text below the calculation
        probability_text.next_to(calculation_text, DOWN, buff=0.8)

        # Implementation: Add voiceover for the second part
        with self.voiceover(text="These are 3, 6, 9, 12, 15, 18, 21, 24, 27, and 30. So, there are 30 minus 10, which is 20 numbers not divisible by 3. Therefore, the probability of drawing a card not divisible by 3 is 20 divided by 30, which simplifies to 2 over 3.") as tracker:
            self.play(Write(calculation_text))
            self.wait(0.5)
            self.play(Write(probability_text))
            self.wait(tracker.duration - 1)

        # Cleaning: Clear all objects for the next scene
        self.clear()

    def play_scene_4(self):
        # Implementation: Display the condition text
        condition_text = Text("(ii) a prime number greater than 7", font_size=36)
        # Thinking: Position the condition text at the top left
        condition_text.to_edge(UP).to_edge(LEFT)

        # Implementation: Define prime numbers
        prime_definition = Text("A prime number is a whole number greater than 1 that has\nonly two divisors: 1 and itself.", font_size=24)
        # Thinking: Position the definition below the condition text
        prime_definition.next_to(condition_text, DOWN, buff=0.5).align_to(condition_text, LEFT)

        # Implementation: List all prime numbers between 1 and 30
        prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        prime_numbers_text = [Text(str(num), font_size=30) for num in prime_numbers]
        # Thinking: Position the list on the left side of the screen
        for i, num_text in enumerate(prime_numbers_text):
            num_text.next_to(prime_definition, DOWN, buff=0.5).shift(i * DOWN * 0.8 + RIGHT)

        # Implementation: Add voiceover for the first part
        with self.voiceover(text="Next, let's find the probability of drawing a prime number greater than 7. A prime number is a whole number greater than 1 that has only two divisors: 1 and itself. The prime numbers between 1 and 30 are: 2, 3, 5, 7, 11, 13, 17, 19, 23, and 29.") as tracker:
            self.play(Write(condition_text))
            self.wait(0.5)
            self.play(Write(prime_definition))
            self.wait(0.5)
            for num_text in prime_numbers_text:
                self.play(Write(num_text))
            self.wait(tracker.duration - 1)

        # Implementation: Highlight prime numbers greater than 7
        highlighted_primes = [11, 13, 17, 19, 23, 29]
        highlighted_primes_text = [Text(str(num), font_size=30, color=YELLOW) for num in highlighted_primes]
        # Thinking: Position the highlighted list below the original list
        for i, num_text in enumerate(highlighted_primes_text):
            num_text.move_to(prime_numbers_text[prime_numbers.index(highlighted_primes[i])])

        # Implementation: Show the calculation for the probability
        calculation_text = Text("6/30 = 1/5", font_size=30)
        # Thinking: Position the calculation text below the list
        calculation_text.next_to(prime_numbers_text[-1], DOWN, buff=0.8)

        # Implementation: Add voiceover for the second part
        with self.voiceover(text="Among these, the prime numbers greater than 7 are: 11, 13, 17, 19, 23, and 29. There are 6 such numbers. So, the probability is 6 divided by 30, which simplifies to 1 over 5.") as tracker:
            for num_text in highlighted_primes_text:
                self.play(Transform(prime_numbers_text[prime_numbers.index(int(num_text.text))], num_text))
            self.wait(0.5)
            self.play(Write(calculation_text))
            self.wait(tracker.duration - 1)

        # Cleaning: Clear all objects for the next scene
        self.clear()

    def play_scene_5(self):
        # Implementation: Display the condition text
        condition_text = Text("(iii) not a perfect square number", font_size=36)
        # Thinking: Position the condition text at the top left
        condition_text.to_edge(UP).to_edge(LEFT)

        # Implementation: Define perfect square numbers
        perfect_square_definition = Text("A perfect square number is a number that can be\nobtained by squaring a whole number.", font_size=24)
        # Thinking: Position the definition below the condition text
        perfect_square_definition.next_to(condition_text, DOWN, buff=0.5).align_to(condition_text, LEFT)

        # Implementation: List perfect square numbers between 1 and 30
        perfect_squares = [1, 4, 9, 16, 25]
        perfect_squares_text = [Text(str(num), font_size=30) for num in perfect_squares]
        # Thinking: Position the list on the left side of the screen
        for i, num_text in enumerate(perfect_squares_text):
            num_text.next_to(perfect_square_definition, DOWN, buff=0.5).shift(i * DOWN * 0.8 + RIGHT)

        # Implementation: Add voiceover for the first part
        with self.voiceover(text="Finally, let's find the probability that the drawn card is not a perfect square number. A perfect square number is a number that can be obtained by squaring a whole number.") as tracker:
            self.play(Write(condition_text))
            self.wait(0.5)
            self.play(Write(perfect_square_definition))
            self.wait(0.5)
            for num_text in perfect_squares_text:
                self.play(Write(num_text))
            self.wait(tracker.duration - 1)

        # Implementation: Calculate numbers not perfect squares
        calculation_text = Text("30 - 5 = 25", font_size=30)
        # Thinking: Position the calculation text below the list
        calculation_text.next_to(perfect_squares_text[-1], DOWN, buff=0.8)

        # Implementation: Display the probability calculation
        probability_text = Text("So, there are 25 numbers that are not perfect squares.\n25/30 = 5/6", font_size=30)
        # Thinking: Position the probability text below the calculation
        probability_text.next_to(calculation_text, DOWN, buff=0.8)

        # Implementation: Add voiceover for the second part
        with self.voiceover(text="The perfect square numbers between 1 and 30 are: 1, 4, 9, 16, and 25. There are 5 such numbers. So, there are 30 minus 5, which is 25 numbers that are not perfect squares. Therefore, the probability of drawing a card that is not a perfect square is 25 divided by 30, which simplifies to 5 over 6.") as tracker:
            self.play(Write(calculation_text))
            self.wait(0.5)
            self.play(Write(probability_text))
            self.wait(tracker.duration - 1)

        # Cleaning: Clear all objects for the next scene
        self.clear()

    def play_scene_6(self):
        # Implementation: Display the text "Real-life scenario" at the top
        scenario_text = Text("Real-life scenario", font_size=48, weight=BOLD)
        # Thinking: Position the text at the top center of the screen
        scenario_text.to_edge(UP)

        # Implementation: Show a simple graphic of a bag and cards
        bag = Rectangle(width=3, height=4, color=WHITE, fill_opacity=0.5)
        # Thinking: Position the bag in the center of the screen
        bag.move_to(ORIGIN)
        cards = [Text(str(i), font_size=24) for i in range(1, 31)]
        # Thinking: Scale down cards to fit in frame
        for card in cards:
            card.scale(0.5)
        # Implementation: Position cards initially inside the bag
        for i, card in enumerate(cards):
            card.move_to(bag.get_center())

        # Implementation: Add voiceover for the first part
        with self.voiceover(text="Let's put this into a real-life scenario. Imagine you are playing a game where you draw a card from this bag. If you win whenever the number you draw is not divisible by 3, then on average, you will win 2 out of 3 times.") as tracker:
            self.play(Write(scenario_text))
            self.wait(0.5)
            self.play(Create(bag))
            for card in cards:
                self.add(card)
            self.wait(0.5)
            # Implementation: Display the text explaining the win rate for the first scenario
            win_rate_1 = Text("Imagine you are playing a game where you draw a card from this bag.\n"
                              "If you win whenever the number you draw is not divisible by 3,\n"
                              "then on average, you will win 2 out of 3 times.", font_size=24)
            # Thinking: Position the text below the bag
            win_rate_1.next_to(bag, DOWN, buff=0.5)
            self.play(Write(win_rate_1))
            self.wait(tracker.duration - 1)

        # Implementation: Add voiceover for the second part
        with self.voiceover(text="If you only win when a prime number greater than 7 is drawn, you will win 1 out of 5 times.") as tracker:
            # Implementation: Display the text explaining the win rate for the second scenario
            win_rate_2 = Text("If you only win when a prime number greater than 7 is drawn,\nyou will win 1 out of 5 times.", font_size=24)
            # Thinking: Replace the first win rate text with the second one
            self.play(ReplacementTransform(win_rate_1, win_rate_2))
            self.wait(tracker.duration)

        # Implementation: Add voiceover for the third part
        with self.voiceover(text="And if you win when the card drawn is not a perfect square, you will win 5 out of 6 times. This shows how probability can be applied to everyday situations.") as tracker:
            # Implementation: Display the text explaining the win rate for the third scenario
            win_rate_3 = Text("And if you win when the card drawn is not a perfect square,\nyou will win 5 out of 6 times.\n"
                              "This shows how probability can be applied to everyday situations.", font_size=24)
            # Thinking: Replace the second win rate text with the third one
            self.play(ReplacementTransform(win_rate_2, win_rate_3))
            self.wait(tracker.duration)

        # Cleaning: Clear all objects
        self.clear()