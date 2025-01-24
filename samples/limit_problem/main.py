
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
        # Implementation: Setting up the voiceover service to GTTSService.
        self.set_speech_service(GTTSService())
        # Implementation: Displaying the initial limit expression.
        limit_text = MathTex(
            r"\lim_{x \to 0} \frac{\sin(x)}{x}",
            font_size=48
        )
        # Implementation: Adding voiceover for the first part of the scene.
        with self.voiceover(text="Today, we're going to tackle the classic limit problem: finding the limit of sin(x) over x as x approaches 0.") as tracker:
            # Implementation: Displaying the limit text on the screen.
            self.play(Write(limit_text))
        # Implementation: Waiting for a brief moment after the first voiceover.
        self.wait(0.5)
        # Implementation: Substituting x = 0 into the expression.
        sin_0_over_0 = MathTex(r"\frac{\sin(0)}{0}", font_size=48)
        zero_over_zero = MathTex(r"\frac{0}{0}", font_size=48)
        # Implementation: Positioning the new expressions below the original.
        sin_0_over_0.next_to(limit_text, DOWN)
        zero_over_zero.next_to(sin_0_over_0, DOWN)
        # Implementation: Adding voiceover for the substitution.
        with self.voiceover(text="If we try to directly substitute 0 for x, we get sin(0) over 0, which simplifies to 0 over 0.") as tracker:
            # Implementation: Animating the substitution.
            self.play(
                Transform(limit_text.copy(), sin_0_over_0),
                Transform(sin_0_over_0.copy(), zero_over_zero)
            )
        # Implementation: Waiting for a brief moment.
        self.wait(0.5)
        # Implementation: Highlighting "0 / 0" and displaying "Indeterminate Form".
        indeterminate_form = Text("Indeterminate Form", color=RED, font_size=36)
        indeterminate_form.next_to(zero_over_zero, DOWN)
        # Implementation: Adding voiceover for the indeterminate form.
        with self.voiceover(text="This is what's known as an indeterminate form, which means we need another way to solve this. That's where the Taylor series comes in.") as tracker:
            # Implementation: Highlighting "0 / 0" in red and showing "Indeterminate Form".
            self.play(
                zero_over_zero.animate.set_color(RED),
                Write(indeterminate_form)
            )
        # Implementation: Waiting for a brief moment.
        self.wait(0.5)
        # Cleaning: Clearing all objects from the scene.
        self.clear()

    def play_scene_2(self):
        # Implementation: Setting up the voiceover service to GTTSService.
        self.set_speech_service(GTTSService())
        # Implementation: Displaying "Taylor Series" text.
        taylor_series_text = Text("Taylor Series", font_size=48)
        taylor_series_text.to_edge(UP)
        # Implementation: Displaying the general formula of the Taylor series.
        taylor_formula = MathTex(
            r"f(x) = f(a) + \frac{f'(a)(x-a)}{1!} + \frac{f''(a)(x-a)^2}{2!} + \frac{f'''(a)(x-a)^3}{3!} + \cdots",
            font_size=36
        )
        taylor_formula.next_to(taylor_series_text, DOWN, buff=0.5)
        # Implementation: Adding voiceover for the Taylor series introduction.
        with self.voiceover(text="The Taylor series is a way to represent a function as an infinite sum of terms calculated from the values of the function's derivatives at a single point. Here's the general formula for the Taylor series of a function around a point 'a'.") as tracker:
            # Implementation: Displaying the Taylor series text and formula.
            self.play(
                Write(taylor_series_text),
                Write(taylor_formula)
            )
        # Implementation: Waiting for a brief moment.
        self.wait(0.5)
        # Cleaning: Clearing all objects from the scene.
        self.clear()

    def play_scene_3(self):
        # Implementation: Setting up the voiceover service to GTTSService.
        self.set_speech_service(GTTSService())
        # Implementation: Displaying "Maclaurin Series (a = 0)" text.
        maclaurin_text = Text("Maclaurin Series (a = 0)", font_size=40)
        maclaurin_text.to_edge(UP)
        # Implementation: Listing the derivatives of sin(x).
        derivatives = VGroup(
            MathTex(r"f(x) = \sin(x)"),
            MathTex(r"f'(x) = \cos(x)"),
            MathTex(r"f''(x) = -\sin(x)"),
            MathTex(r"f'''(x) = -\cos(x)")
        )
        derivatives.arrange(DOWN, aligned_edge=LEFT)
        derivatives.scale(0.7)
        derivatives.next_to(maclaurin_text, DOWN, buff=0.5).shift(LEFT * 2)
        # Implementation: Adding voiceover for the derivatives introduction.
        with self.voiceover(text="For our problem, we'll use the Maclaurin series, which is just a Taylor series centered at 0. Let's find the derivatives of sin(x).") as tracker:
            # Implementation: Displaying the Maclaurin series text and listing the derivatives.
            self.play(Write(maclaurin_text))
            self.play(Write(derivatives))
        # Implementation: Waiting for a brief moment.
        self.wait(0.5)
        # Implementation: Evaluating the derivatives at x=0.
        evaluations = VGroup(
            MathTex(r"f(0) = 0", color=BLUE),
            MathTex(r"f'(0) = 1", color=BLUE),
            MathTex(r"f''(0) = 0", color=BLUE),
            MathTex(r"f'''(0) = -1", color=BLUE)
        )
        # Implementation: Aligning evaluations with their respective derivatives.
        for i, eval_tex in enumerate(evaluations):
            eval_tex.next_to(derivatives[i], RIGHT, buff=1.5)
        # Implementation: Adding voiceover for the evaluations.
        with self.voiceover(text="The first derivative is cos(x), the second is -sin(x), the third is -cos(x), and the fourth is back to sin(x). When we evaluate these at x equals 0, we get a repeating pattern: 0, 1, 0, -1.") as tracker:
            # Implementation: Displaying the evaluations in blue.
            for eval_tex in evaluations:
                self.play(Write(eval_tex))
        # Implementation: Waiting for a brief moment.
        self.wait(0.5)
        # Cleaning: Clearing all objects from the scene.
        self.clear()

    def play_scene_4(self):
        # Implementation: Setting up the voiceover service to GTTSService.
        self.set_speech_service(GTTSService())
        # Implementation: Constructing the Maclaurin series step-by-step.
        series_terms = [
            MathTex(r"0", color=GREEN),
            MathTex(r"+", color=GREEN),
            MathTex(r"\frac{(1)x}{1!}", color=GREEN),
            MathTex(r"+", color=GREEN),
            MathTex(r"\frac{(0)x^2}{2!}", color=GREEN),
            MathTex(r"+", color=GREEN),
            MathTex(r"\frac{(-1)x^3}{3!}", color=GREEN),
            MathTex(r"+", color=GREEN),
            MathTex(r"\frac{(0)x^4}{4!}", color=GREEN),
            MathTex(r"+", color=GREEN),
            MathTex(r"\cdots", color=GREEN)
        ]
        # Implementation: Initial positioning for the series construction.
        series_terms[0].shift(LEFT * 3)
        for i in range(1, len(series_terms)):
            series_terms[i].next_to(series_terms[i - 1], RIGHT, buff=0.2)
        # Implementation: Adding voiceover for the series construction.
        with self.voiceover(text="Now we plug these values into the Maclaurin series formula.") as tracker:
            # Implementation: Displaying the series terms step-by-step.
            for term in series_terms:
                self.play(Write(term))
        # Implementation: Waiting for a brief moment.
        self.wait(0.5)
        # Implementation: Simplifying the series.
        simplified_series = MathTex(
            r"\sin(x) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \cdots",
            font_size=36
        )
        simplified_series.move_to(series_terms[0])
        # Implementation: Adding voiceover for the simplified series.
        with self.voiceover(text="We get sin(x) equals x minus x cubed over 3 factorial plus x to the fifth over 5 factorial minus x to the seventh over 7 factorial, and so on. This is the Maclaurin series expansion for sin(x).") as tracker:
            # Implementation: Transforming the constructed series into the simplified form.
            self.play(
                *[FadeOut(term) for term in series_terms],
                Write(simplified_series)
            )
        # Implementation: Waiting for a brief moment.
        self.wait(0.5)
        # Cleaning: Clearing all objects from the scene.
        self.clear()

    def play_scene_5(self):
        # Implementation: Setting up the voiceover service to GTTSService.
        self.set_speech_service(GTTSService())
        # Implementation: Displaying the original limit expression.
        original_limit = MathTex(r"\lim_{x \to 0} \frac{\sin(x)}{x}", font_size=40)
        original_limit.to_edge(UP)
        # Implementation: Writing the series expansion of sin(x).
        series_expansion = MathTex(
            r"x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \cdots",
            font_size=36
        )
        # Implementation: Positioning the series expansion below the limit.
        series_expansion.next_to(original_limit, DOWN, buff=1)
        # Implementation: Creating the new limit expression with the series expansion.
        new_limit = MathTex(
            r"\lim_{x \to 0} \frac{x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \cdots}{x}",
            font_size=36
        )
        new_limit.move_to(original_limit)
        # Implementation: Adding voiceover for substituting the series expansion.
        with self.voiceover(text="Now, let's substitute the Taylor series expansion of sin(x) into our limit expression. We replace sin(x) with its series: x minus x cubed over 3 factorial plus x to the fifth over 5 factorial, and so on, all over x.") as tracker:
            # Implementation: Displaying the original limit and the series expansion.
            self.play(Write(original_limit))
            self.wait(2)  # Wait for a moment while showing the original limit.
            self.play(Write(series_expansion))
            self.wait(2)  # Wait for a moment while showing the series expansion.
            # Implementation: Transforming the original limit into the new limit with the series expansion.
            self.play(
                Transform(original_limit, new_limit),
                FadeOut(series_expansion)
            )
        # Implementation: Waiting for a brief moment.
        self.wait(0.5)
        # Cleaning: Clearing all objects from the scene.
        self.clear()

    def play_scene_6(self):
        # Implementation: Setting up the voiceover service to GTTSService.
        self.set_speech_service(GTTSService())
        # Implementation: Displaying the limit expression with the series expansion.
        limit_expression = MathTex(
            r"\lim_{x \to 0} \frac{x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \cdots}{x}",
            font_size=36
        )
        limit_expression.to_edge(UP)
        # Implementation: Dividing each term by x.
        divided_terms = MathTex(
            r"\lim_{x \to 0} \left(1 - \frac{x^2}{3!} + \frac{x^4}{5!} - \frac{x^6}{7!} + \cdots\right)",
            font_size=36
        )
        divided_terms.next_to(limit_expression, DOWN, buff=1)
        # Implementation: Adding voiceover for dividing each term by x.
        with self.voiceover(text="We can divide each term in the series by x. This simplifies our limit to 1 minus x squared over 3 factorial plus x to the fourth over 5 factorial minus x to the sixth over 7 factorial, and so on.") as tracker:
            # Implementation: Displaying the limit expression.
            self.play(Write(limit_expression))
            self.wait(2)  # Wait for a moment while showing the limit expression.
            # Implementation: Transforming the limit expression to show the division by x.
            self.play(
                Transform(limit_expression, divided_terms)
            )
        # Implementation: Waiting for a brief moment.
        self.wait(0.5)
        # Cleaning: Clearing all objects from the scene.
        self.clear()

    def play_scene_7(self):
        # Implementation: Setting up the voiceover service to GTTSService.
        self.set_speech_service(GTTSService())
        # Implementation: Displaying the simplified limit expression.
        simplified_limit = MathTex(
            r"\lim_{x \to 0} \left(1 - \frac{x^2}{3!} + \frac{x^4}{5!} - \frac{x^6}{7!} + \cdots\right)",
            font_size=36
        )
        simplified_limit.to_edge(UP)
        # Implementation: Showing the limit as x approaches 0.
        final_result = MathTex(r"1", font_size=48, color=CYAN)
        final_result.move_to(simplified_limit)
        # Implementation: Adding voiceover for the limit approaching 0.
        with self.voiceover(text="As x approaches 0, all terms with x in them will approach 0 as well. This leaves us with just 1. Therefore, the limit of sin(x) over x as x approaches 0 is 1.") as tracker:
            # Implementation: Displaying the simplified limit.
            self.play(Write(simplified_limit))
            self.wait(2)  # Wait for a moment while showing the simplified limit.
            # Implementation: Transforming the limit expression to show the final result.
            self.play(
                Transform(simplified_limit, final_result)
            )
        # Implementation: Waiting for a brief moment.
        self.wait(0.5)
        # Cleaning: Clearing all objects from the scene.
        self.clear()

    def play_scene_8(self):
        # Implementation: Setting up the voiceover service to GTTSService.
        self.set_speech_service(GTTSService())
        # Implementation: Displaying the final result of the limit.
        final_result_text = MathTex(r"\lim_{x \to 0} \frac{\sin(x)}{x} = 1", font_size=48)
        final_result_text.to_edge(UP)
        # Implementation: Displaying text about the applications of this result.
        applications_text = Text(
            "This result is fundamental in calculus, physics (small-angle approximations),\nand engineering (control systems, signal processing)",
            font_size=24
        )
        applications_text.next_to(final_result_text, DOWN, buff=1)
        # Implementation: Adding voiceover for the final result and its applications.
        with self.voiceover(text="So, we've shown that the limit of sin(x) over x as x approaches 0 is 1. This isn't just a neat mathematical trick; it's a fundamental result used in various fields, including calculus, physics, and many branches of engineering. Understanding this limit helps us in many theoretical and practical applications.") as tracker:
            # Implementation: Displaying the final result.
            self.play(Write(final_result_text))
            self.wait(2)  # Wait for a moment while showing the final result.
            # Implementation: Displaying the applications text.
            self.play(Write(applications_text))
        # Implementation: Waiting for a brief moment.
        self.wait(0.5)
        # Cleaning: Clearing all objects from the scene.
        self.clear()