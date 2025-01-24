
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
        # Implementation: Set the scene style
        self.set_speech_service(GTTSService(lang="en", tld="com"))
        self.camera.background_color = "#000000"  # Dark background

        # Implementation: Define the Gaussian curve
        def gaussian(x, mu=0, sigma=1):
            # Implementation: Calculate the Gaussian function
            return np.exp(-((x - mu) ** 2) / (2 * sigma**2))

        # Implementation: Create the Gaussian curve
        graph = FunctionGraph(
            gaussian,
            x_range=[-3, 3, 0.01],
            color=BLUE_B,
        )
        # Implementation: Scale the curve to fit the frame
        graph.scale(1.3)

        # Implementation: Create the axes
        axes = Axes(
            x_range=[-3, 3],
            y_range=[0, 1],
            axis_config={"color": WHITE},
            x_length=6,
            y_length=4,
        )
        # Implementation: Scale the axes to fit the frame
        axes.scale(1.3)

        # Implementation: Animate the curve appearing from the left
        with self.voiceover(
            text="Let's explore the Gaussian distribution, also known as the normal distribution."
        ) as tracker:
            # Implementation: Animate the curve appearing from the left
            self.play(
                graph.animate.set_x(-3).set_opacity(0),
                run_time=tracker.duration / 2,
            )
            self.play(
                graph.animate.set_x(0).set_opacity(1),
                run_time=tracker.duration / 2,
            )

        # Implementation: Create the mean line and label
        mean_line = DashedLine(
            start=axes.c2p(0, gaussian(0)),
            end=axes.c2p(0, 0),
            color=WHITE,
        )
        # Implementation: Calculate position for mean label
        mean_label = (
            MathTex(r"\mu", color=WHITE)
            .next_to(mean_line, UP, buff=0.5)
            .shift(0.4 * UP)
        )

        # Implementation: Create the x-axis and y-axis labels
        x_label = (
            Text("Random Variable", color=WHITE)
            .scale(0.6)
            .next_to(axes, DOWN, buff=0.8)
        )
        # Implementation: Calculate position for y-axis label
        y_label = (
            Text("Probability Density", color=WHITE)
            .scale(0.6)
            .rotate(90 * DEGREES)
            .next_to(axes, LEFT, buff=0.8)
        )

        # Implementation: Animate the labels and mean line
        with self.voiceover(
            text="It's a cornerstone of statistics and probability, and you'll find it almost everywhere in the real world."
        ) as tracker:
            self.play(
                Create(mean_line),
                Write(mean_label),
                Write(x_label),
                Write(y_label),
                run_time=tracker.duration,
            )

        # Cleaning: Store objects for next scene
        self.gaussian_curve = graph
        self.mean_label = mean_label
        self.axes = axes

    def play_scene_2(self):
        # Implementation: Set the scene style
        self.set_speech_service(GTTSService(lang="en", tld="com"))
        self.camera.background_color = "#000000"  # Dark background

        # Implementation: Retrieve objects from previous scene
        graph = self.gaussian_curve
        mean_label = self.mean_label
        axes = self.axes

        # Implementation: Define the Gaussian function
        def gaussian(x, mu=0, sigma=1):
            return np.exp(-((x - mu) ** 2) / (2 * sigma**2))

        # Implementation: Create a copy of the graph for highlighting
        left_highlight = graph.copy().set_color(GREEN_B)
        right_highlight = graph.copy().set_color(RED_B)

        # Implementation: Clip the highlights to the left and right of the mean
        left_highlight.add_updater(
            lambda m: m.become(
                FunctionGraph(
                    lambda x: gaussian(x) if x <= 0 else 0,
                    x_range=[-3, 3, 0.01],
                    color=GREEN_B,
                ).scale(1.3)
            )
        )

        right_highlight.add_updater(
            lambda m: m.become(
                FunctionGraph(
                    lambda x: gaussian(x) if x >= 0 else 0,
                    x_range=[-3, 3, 0.01],
                    color=RED_B,
                ).scale(1.3)
            )
        )

        # Implementation: Animate highlighting the left side
        with self.voiceover(
            text="One key feature of the Gaussian distribution is its symmetry."
        ) as tracker:
            self.add(left_highlight)
            self.wait(tracker.duration)
            self.remove(left_highlight)

        # Implementation: Animate highlighting the right side
        with self.voiceover(
            text="The curve is perfectly symmetrical around its mean. In fact, the mean, median, and mode are all equal and lie right at the center."
        ) as tracker:
            self.add(right_highlight)
            self.wait(tracker.duration)
            self.remove(right_highlight)

        # Cleaning: Store objects for next scene
        self.gaussian_curve = graph
        self.mean_label = mean_label
        self.axes = axes

    def play_scene_3(self):
        # Implementation: Set the scene style
        self.set_speech_service(GTTSService(lang="en", tld="com"))
        self.camera.background_color = "#000000"  # Dark background

        # Implementation: Retrieve objects from previous scene
        graph = self.gaussian_curve
        mean_label = self.mean_label
        axes = self.axes

        # Implementation: Define the Gaussian function
        def gaussian(x, mu=0, sigma=1):
            return np.exp(-((x - mu) ** 2) / (2 * sigma**2))

        # Implementation: Create curves with different standard deviations
        # Implementation: Calculate smaller standard deviation curve
        smaller_sigma_curve = FunctionGraph(
            lambda x: gaussian(x, sigma=0.5),
            x_range=[-3, 3, 0.01],
            color=YELLOW_B,
        )
        # Implementation: Calculate larger standard deviation curve
        larger_sigma_curve = FunctionGraph(
            lambda x: gaussian(x, sigma=2),
            x_range=[-3, 3, 0.01],
            color=PURPLE_B,
        )

        # Implementation: Scale the curves to fit the frame
        graph.scale(0.7)
        smaller_sigma_curve.scale(0.7)
        larger_sigma_curve.scale(0.7)

        # Implementation: Create labels for the curves
        # Implementation: Calculate position for smaller sigma label
        smaller_sigma_label = (
            MathTex(r"\text{Smaller } \sigma", color=WHITE)
            .scale(0.6)
            .next_to(smaller_sigma_curve, UP, buff=0.5)
            .shift(0.8 * LEFT)
        )
        # Implementation: Calculate position for larger sigma label
        larger_sigma_label = (
            MathTex(r"\text{Larger } \sigma", color=WHITE)
            .scale(0.6)
            .next_to(larger_sigma_curve, DOWN, buff=0.5)
            .shift(0.5 * RIGHT)
        )

        # Implementation: Animate the standard curve
        with self.voiceover(
            text="The spread of the data is determined by the standard deviation."
        ) as tracker:
            self.play(Create(graph), run_time=tracker.duration)

        # Implementation: Animate the smaller sigma curve
        with self.voiceover(
            text="A smaller standard deviation results in a tall, narrow curve."
        ) as tracker:
            self.play(
                Create(smaller_sigma_curve),
                Write(smaller_sigma_label),
                run_time=tracker.duration,
            )

        # Implementation: Animate the larger sigma curve
        with self.voiceover(
            text="while a larger one gives us a wide, flat curve."
        ) as tracker:
            self.play(
                Create(larger_sigma_curve),
                Write(larger_sigma_label),
                run_time=tracker.duration,
            )

        # Cleaning: Clear all objects for next scene
        self.clear()

    def play_scene_4(self):
        # Implementation: Set the scene style
        self.set_speech_service(GTTSService(lang="en", tld="com"))
        self.camera.background_color = "#000000"  # Dark background

        # Implementation: Define the Gaussian PDF formula
        # Implementation: Create the formula
        formula = MathTex(
            r"f(x | \mu, \sigma) = \frac{1}{\sigma \sqrt{2\pi}} \exp\left(-\frac{(x - \mu)^2}{2\sigma^2}\right)",
            color=WHITE,
        )
        # Implementation: Scale the formula to fit the frame
        formula.scale(0.8)

        # Implementation: Highlight parts of the formula
        # Implementation: Create the scaling factor highlight
        scaling_factor = formula[0][9:18].copy().set_color(GREEN_B)
        # Implementation: Create the exponential part highlight
        exponential_part = formula[0][18:].copy().set_color(ORANGE)

        # Implementation: Animate the formula
        with self.voiceover(
            text="Mathematically, the Gaussian distribution is described by its probability density function, or PDF."
        ) as tracker:
            self.play(Write(formula), run_time=tracker.duration)

        # Implementation: Animate the scaling factor highlight
        with self.voiceover(
            text="This formula has two main parts: a scaling factor"
        ) as tracker:
            self.play(TransformFromCopy(formula[0][9:18], scaling_factor))
            self.wait(tracker.duration - scaling_factor.animate.set_opacity(0).duration)
            self.play(scaling_factor.animate.set_opacity(0))

        # Implementation: Animate the exponential part highlight
        with self.voiceover(
            text="and an exponential part that gives the curve its shape."
        ) as tracker:
            self.play(TransformFromCopy(formula[0][18:], exponential_part))
            self.wait(tracker.duration - exponential_part.animate.set_opacity(0).duration)
            self.play(exponential_part.animate.set_opacity(0))

        # Cleaning: Clear all objects for next scene
        self.clear()

    def play_scene_5(self):
        # Implementation: Set the scene style
        self.set_speech_service(GTTSService(lang="en", tld="com"))
        self.camera.background_color = "#000000"  # Dark background

        # Implementation: Define the Gaussian curve
        def gaussian(x, mu=0, sigma=1):
            return np.exp(-((x - mu) ** 2) / (2 * sigma**2))

        # Implementation: Create the Gaussian curve
        graph = FunctionGraph(
            gaussian,
            x_range=[-3, 3, 0.01],
            color=BLUE_B,
        )
        # Implementation: Scale the curve to fit the frame
        graph.scale(1.3)

        # Implementation: Create the axes
        axes = Axes(
            x_range=[-3, 3],
            y_range=[0, 1],
            axis_config={"color": WHITE},
            x_length=6,
            y_length=4,
        )
        # Implementation: Scale the axes to fit the frame
        axes.scale(1.3)

        # Implementation: Create the shaded areas
        # Implementation: Calculate one standard deviation area
        one_sigma_area = axes.get_area(
            graph,
            x_range=[-1, 1],
            color=BLUE_B,
        )
        # Implementation: Calculate two standard deviations area
        two_sigma_area = axes.get_area(
            graph,
            x_range=[-2, 2],
            color=GREEN_B,
        )
        # Implementation: Calculate three standard deviations area
        three_sigma_area = axes.get_area(
            graph,
            x_range=[-3, 3],
            color=RED_B,
        )

        # Implementation: Create the percentage labels
        # Implementation: Calculate position for 68% label
        one_sigma_label = (
            Text("68%", color=WHITE).scale(0.7).move_to(one_sigma_area).shift(0.3 * UP)
        )
        # Implementation: Calculate position for 95% label
        two_sigma_label = (
            Text("95%", color=WHITE)
            .scale(0.7)
            .move_to(two_sigma_area)
            .shift(0.8 * UP)
        )
        # Implementation: Calculate position for 99.7% label
        three_sigma_label = (
            Text("99.7%", color=WHITE)
            .scale(0.7)
            .move_to(three_sigma_area)
            .shift(1.3 * UP)
        )

        # Implementation: Animate the curve
        with self.voiceover(
            text="The empirical rule tells us that about"
        ) as tracker:
            self.play(Create(axes), Create(graph), run_time=tracker.duration)

        # Implementation: Animate one standard deviation area
        with self.voiceover(
            text="68% of the data falls within one standard deviation of the mean,"
        ) as tracker:
            self.play(
                FadeIn(one_sigma_area), Write(one_sigma_label), run_time=tracker.duration
            )

        # Implementation: Animate two standard deviations area
        with self.voiceover(
            text="95% within two standard deviations,"
        ) as tracker:
            self.play(
                FadeIn(two_sigma_area), Write(two_sigma_label), run_time=tracker.duration
            )

        # Implementation: Animate three standard deviations area
        with self.voiceover(
            text="and 99.7% within three."
        ) as tracker:
            self.play(
                FadeIn(three_sigma_area),
                Write(three_sigma_label),
                run_time=tracker.duration,
            )

        # Cleaning: Clear all objects for next scene
        self.clear()

    def play_scene_6(self):
        # Implementation: Set the scene style
        self.set_speech_service(GTTSService(lang="en", tld="com"))
        self.camera.background_color = "#000000"  # Dark background

        # Implementation: Define a function to create a die graphic
        def create_die(dots, scale=0.5):
            # Implementation: Create a die with given number of dots
            square = Square(side_length=1 * scale, color=WHITE, fill_opacity=0.5)
            dot_positions = {
                1: [(0, 0)],
                2: [(-0.25, 0.25), (0.25, -0.25)],
                3: [(-0.25, 0.25), (0, 0), (0.25, -0.25)],
                4: [(-0.25, 0.25), (0.25, 0.25), (-0.25, -0.25), (0.25, -0.25)],
                5: [
                    (-0.25, 0.25),
                    (0.25, 0.25),
                    (-0.25, -0.25),
                    (0.25, -0.25),
                    (0, 0),
                ],
                6: [
                    (-0.25, 0.25),
                    (0.25, 0.25),
                    (-0.25, -0.25),
                    (0.25, -0.25),
                    (-0.25, 0),
                    (0.25, 0),
                ],
            }
            # Implementation: Create dots for die
            dots_list = [
                Dot(point=np.array(pos) * scale, color=WHITE, radius=0.08 * scale)
                for pos in dot_positions[dots]
            ]
            return VGroup(square, *dots_list)

        # Implementation: Define a function to create a bar graph
        def create_bar_graph(values, x_labels, scale=0.5, bar_width=0.5):
            # Implementation: Create a bar graph with given values and x-labels
            max_value = max(values)
            graph = VGroup()
            x_pos = 0
            for i, value in enumerate(values):
                # Implementation: Calculate bar height
                bar_height = value / max_value * 3 * scale
                bar = Rectangle(
                    width=bar_width * scale,
                    height=bar_height,
                    color=BLUE,
                    fill_opacity=0.8,
                )
                # Implementation: Position the bar
                bar.move_to(np.array([x_pos, bar_height / 2, 0]), aligned_edge=DOWN)
                label = Text(x_labels[i], color=WHITE).scale(0.5 * scale)
                # Implementation: Position the x-label
                label.next_to(bar, DOWN, buff=0.2 * scale)
                graph.add(VGroup(bar, label))
                x_pos += bar_width * scale
            return graph

        # Implementation: Create the initial die and its uniform distribution
        die_1 = create_die(1)
        # Implementation: Calculate position for single die
        die_1.move_to(np.array([-5, 0, 0]))
        uniform_dist = create_bar_graph(
            [1, 1, 1, 1, 1, 1], ["1", "2", "3", "4", "5", "6"]
        )
        # Implementation: Calculate position for uniform distribution graph
        uniform_dist.next_to(die_1, RIGHT, buff=1)

        # Implementation: Animate the first die and its distribution
        with self.voiceover(
            text="The Central Limit Theorem explains why the Gaussian distribution is so common."
        ) as tracker:
            self.play(
                Create(die_1), Create(uniform_dist), run_time=tracker.duration
            )

        # Implementation: Create the second die and its distribution
        die_2 = create_die(2)
        # Implementation: Calculate position for two dice
        die_2.move_to(die_1.get_center() + np.array([1.5, 0, 0]))
        two_dice_dist = create_bar_graph(
            [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1],
            ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
        )
        # Implementation: Calculate position for two dice distribution graph
        two_dice_dist.next_to(die_2, RIGHT, buff=1)

        # Implementation: Animate the second die and its distribution
        with self.voiceover(
            text="It states that the sum of many independent random variables,"
        ) as tracker:
            self.play(
                die_1.animate.shift(LEFT * 2),
                uniform_dist.animate.shift(LEFT * 2),
                Create(die_2),
                Create(two_dice_dist),
                run_time=tracker.duration,
            )

        # Implementation: Create the third die and its distribution
        die_3 = create_die(3)
        # Implementation: Calculate position for three dice
        die_3.move_to(die_2.get_center() + np.array([1.5, 0, 0]))
        three_dice_dist = create_bar_graph(
            [
                1,
                3,
                6,
                10,
                15,
                21,
                25,
                27,
                27,
                25,
                21,
                15,
                10,
                6,
                3,
                1,
            ],
            [str(i) for i in range(3, 19)],
        )
        # Implementation: Calculate position for three dice distribution graph
        three_dice_dist.next_to(die_3, RIGHT, buff=1)

        # Implementation: Animate the third die and its distribution
        with self.voiceover(
            text="like rolling multiple dice,"
        ) as tracker:
            self.play(
                die_1.animate.shift(LEFT * 2),
                uniform_dist.animate.shift(LEFT * 2),
                die_2.animate.shift(LEFT * 2),
                two_dice_dist.animate.shift(LEFT * 2),
                Create(die_3),
                Create(three_dice_dist),
                run_time=tracker.duration,
            )

        # Implementation: Create multiple dice and their distribution
        multiple_dice = VGroup(*[create_die(i) for i in range(1, 6)])
        # Implementation: Arrange multiple dice in a row
        multiple_dice.arrange(RIGHT, buff=0.5)
        # Implementation: Calculate position for multiple dice
        multiple_dice.move_to(np.array([0, -2, 0]))
        many_dice_dist = create_bar_graph(
            [
                1,
                5,
                15,
                35,
                70,
                126,
                205,
                305,
                415,
                525,
                615,
                671,
                671,
                615,
                525,
                415,
                305,
                205,
                126,
                70,
                35,
                15,
                5,
                1,
            ],
            [str(i) for i in range(5, 29)],
            scale=0.8,
        )
        # Implementation: Calculate position for many dice distribution graph
        many_dice_dist.move_to(np.array([0, 1, 0]))

        # Implementation: Animate multiple dice and their distribution
        with self.voiceover(
            text="tends towards a normal distribution as the number of variables increases."
        ) as tracker:
            self.play(
                FadeOut(die_1),
                FadeOut(uniform_dist),
                FadeOut(die_2),
                FadeOut(two_dice_dist),
                FadeOut(die_3),
                FadeOut(three_dice_dist),
                Create(multiple_dice),
                Create(many_dice_dist),
                run_time=tracker.duration,
            )

        # Implementation: Remove the dice and keep only the final distribution
        with self.voiceover(text="") as tracker:
            self.play(
                FadeOut(multiple_dice),
                run_time=tracker.duration,
            )

        # Cleaning: Store final distribution graph for next scene
        self.final_dist_graph = many_dice_dist

    def play_scene_7(self):
        # Implementation: Set the scene style
        self.set_speech_service(GTTSService(lang="en", tld="com"))
        self.camera.background_color = "#000000"  # Dark background

        # Implementation: Retrieve the final distribution graph from the previous scene
        many_dice_dist = self.final_dist_graph

        # Implementation: Define a function to create a simple icon
        def create_icon(icon_type, scale=0.5):
            # Implementation: Create a simple icon based on the given type
            if icon_type == "person":
                # Implementation: Create a stick figure icon
                head = Circle(radius=0.2 * scale, color=WHITE, fill_opacity=0.5)
                body = Line(
                    start=head.get_bottom(),
                    end=head.get_bottom() + np.array([0, -0.8, 0]) * scale,
                    color=WHITE,
                )
                left_arm = Line(
                    start=body.get_top() + np.array([0, -0.2, 0]) * scale,
                    end=body.get_top() + np.array([-0.3, -0.5, 0]) * scale,
                    color=WHITE,
                )
                right_arm = Line(
                    start=body.get_top() + np.array([0, -0.2, 0]) * scale,
                    end=body.get_top() + np.array([0.3, -0.5, 0]) * scale,
                    color=WHITE,
                )
                left_leg = Line(
                    start=body.get_end(),
                    end=body.get_end() + np.array([-0.2, -0.5, 0]) * scale,
                    color=WHITE,
                )
                right_leg = Line(
                    start=body.get_end(),
                    end=body.get_end() + np.array([0.2, -0.5, 0]) * scale,
                    color=WHITE,
                )
                return VGroup(head, body, left_arm, right_arm, left_leg, right_leg)
            elif icon_type == "brain":
                # Implementation: Create a simple brain icon
                brain = SVGMobject("brain.svg", color=WHITE, fill_opacity=0.5).scale(
                    scale
                )
                return brain
            elif icon_type == "error":
                # Implementation: Create an error icon
                circle = Circle(radius=0.5 * scale, color=WHITE)
                exclamation = Text("!", color=WHITE).scale(scale)
                return VGroup(circle, exclamation)
            else:
                return None

        # Implementation: Create the text labels and icons
        heights_label = Text("Heights of People", color=WHITE).scale(0.5)
        # Implementation: Calculate position for heights label
        heights_label.move_to(np.array([-4, 3, 0]))
        heights_icon = create_icon("person")
        # Implementation: Calculate position for heights icon
        heights_icon.next_to(heights_label, LEFT, buff=0.5)

        iq_label = Text("IQ Scores", color=WHITE).scale(0.5)
        # Implementation: Calculate position for IQ label
        iq_label.move_to(np.array([0, 3, 0]))

        errors_label = Text("Measurement Errors", color=WHITE).scale(0.5)
        # Implementation: Calculate position for errors label
        errors_label.move_to(np.array([4, 3, 0]))
        errors_icon = create_icon("error")
        # Implementation: Calculate position for errors icon
        errors_icon.next_to(errors_label, LEFT, buff=0.5)

        # Implementation: Animate the Gaussian curve appearance
        with self.voiceover(
            text="The Gaussian distribution appears in many real-world scenarios,"
        ) as tracker:
            self.play(Create(many_dice_dist), run_time=tracker.duration)

        # Implementation: Animate the first example (Heights of People)
        with self.voiceover(
            text="such as the distribution of people's heights,"
        ) as tracker:
            self.play(
                Write(heights_label), Create(heights_icon), run_time=tracker.duration
            )

        # Implementation: Animate the second example (IQ Scores)
        with self.voiceover(text="IQ scores,") as tracker:
            self.play(Write(iq_label), run_time=tracker.duration)

        # Implementation: Animate the third example (Measurement Errors)
        with self.voiceover(
            text="and even errors in measurements. It's truly a fundamental concept with wide-reaching applications."
        ) as tracker:
            self.play(
                Write(errors_label), Create(errors_icon), run_time=tracker.duration
            )

        # Cleaning: Clear all objects
        self.clear()