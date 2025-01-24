
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
        # Implementation: Setting the voiceover service to GTTSService
        self.set_speech_service(GTTSService())
        # Implementation: Displaying the title "Work Done by a Force"
        title = Text("Work Done by a Force", font_size=48, weight=BOLD).to_edge(UP)
        # Implementation: Displaying the force equation
        force_equation = MathTex("F = 2x^2y \\, i + 3xy \\, j", font_size=36).next_to(title, DOWN, buff=0.5).to_edge(LEFT)

        # Implementation: Adding voiceover for the first part of scene 1
        with self.voiceover(text="In this video, we'll explore how to calculate the work done by a force. Specifically, we'll look at a force given by F equals 2 x squared y i plus 3 x y j.") as tracker:
            # Implementation: Animating the title and force equation
            self.play(Write(title), Write(force_equation))
            self.wait(tracker.duration)

        # Implementation: Creating the coordinate plane
        axes = Axes(
            x_range=[0, 1.5, 0.5],
            y_range=[0, 5, 1],
            x_length=6,
            y_length=4,
            axis_config={"color": WHITE},
            x_axis_config={"numbers_to_include": [0, 1]},
            y_axis_config={"numbers_to_include": [0, 4]},
            tips=False,
        ).set_color(BLUE_E)
        # Implementation: Adding labels to the axes
        x_label = axes.get_x_axis_label("x").set_color(WHITE)
        y_label = axes.get_y_axis_label("y").set_color(WHITE)

        # Implementation: Drawing the curve y = 4x^2
        curve = axes.plot(lambda x: 4 * x**2, x_range=[0, 1], color=YELLOW)
        # Implementation: Adding label for the curve
        curve_label = MathTex("y = 4x^2", font_size=36, color=WHITE).next_to(curve, RIGHT, buff=0.1)

        # Implementation: Creating the red dot
        dot = Dot(color=RED)
        dot.move_to(axes.c2p(0, 0))

        # Implementation: Adding voiceover for the second part of scene 1
        with self.voiceover(text="which displaces a particle in the x y plane from the origin, zero zero, to the point one four, along the curve y equals 4 x squared. Let's see how to solve this.") as tracker:
            # Implementation: Animating the coordinate plane, curve, and dot
            self.play(Create(axes), Create(x_label), Create(y_label))
            self.play(Create(curve), Write(curve_label))
            self.add(dot)
            self.play(dot.animate.move_to(axes.c2p(1, 4)), run_time=3)
            self.wait(tracker.duration - 3)

        # Cleaning: Clearing all objects for the next scene
        self.clear()

    def play_scene_2(self):
        # Implementation: Setting the voiceover service to GTTSService
        self.set_speech_service(GTTSService())
        # Implementation: Displaying the work done equation
        work_equation = MathTex("W = \\int F \\cdot dr", font_size=48)
        # Implementation: Highlighting the integral symbol and dot product
        work_equation.set_color_by_tex("\\int", YELLOW)
        work_equation.set_color_by_tex("\\cdot", YELLOW)

        # Implementation: Adding voiceover for the first part of scene 2
        with self.voiceover(text="Since our force varies along the path, and the path is a curve, we can't use the simple work equals force times distance formula. Instead, we need to use a line integral.") as tracker:
            # Implementation: Animating the work equation
            self.play(Write(work_equation))
            self.wait(tracker.duration)

        # Implementation: Defining F and dr below the equation
        f_definition = MathTex("F: \\text{Force Vector}", font_size=36).next_to(work_equation, DOWN, buff=1).to_edge(LEFT)
        dr_definition = MathTex("dr: \\text{Infinitesimal Displacement Vector}", font_size=36).next_to(f_definition, DOWN, buff=0.5).to_edge(LEFT)

        # Implementation: Adding voiceover for the second part of scene 2
        with self.voiceover(text="The work done is given by the integral of the dot product of the force vector, F, and the infinitesimal displacement vector, d r, along the path.") as tracker:
            # Implementation: Animating the definitions of F and dr
            self.play(Write(f_definition))
            self.play(Write(dr_definition))
            self.wait(tracker.duration)

        # Cleaning: Clearing all objects for the next scene
        self.clear()

    def play_scene_3(self):
        # Implementation: Setting the voiceover service to GTTSService
        self.set_speech_service(GTTSService())
        # Implementation: Displaying the title "Parameterize the Path"
        parameterize_title = Text("Parameterize the Path", font_size=48).to_edge(UP)
        # Implementation: Displaying equations x = t and y = 4x^2
        x_equation = MathTex("x = t", font_size=40).next_to(parameterize_title, DOWN, buff=1)
        y_equation = MathTex("y = 4x^2", font_size=40).next_to(x_equation, DOWN, buff=0.5)

        # Implementation: Adding voiceover for the first part of scene 3
        with self.voiceover(text="To evaluate this line integral, we need to parameterize our path. That means expressing x and y in terms of a single parameter, which we'll call t.") as tracker:
            # Implementation: Animating the title and equations
            self.play(Write(parameterize_title))
            self.play(Write(x_equation), Write(y_equation))
            self.wait(tracker.duration)

        # Implementation: Substituting x = t into y = 4x^2 to get y = 4t^2
        y_substitution = MathTex("y = 4(t)^2 = 4t^2", font_size=40).next_to(y_equation, DOWN, buff=0.5)
        y_substitution.set_color_by_tex("t", YELLOW)

        # Implementation: Adding voiceover for the second part of scene 3
        with self.voiceover(text="Since our path is given by y equals 4 x squared, let's set x equal to t. Then, substituting t for x, we get y equals 4 t squared.") as tracker:
            # Implementation: Animating the substitution
            self.play(TransformMatchingTex(y_equation.copy(), y_substitution))
            self.wait(tracker.duration)

        # Cleaning: Clearing all objects for the next scene
        self.clear()

    def play_scene_4(self):
        # Implementation: Setting the voiceover service to GTTSService
        self.set_speech_service(GTTSService())
        # Implementation: Displaying r(t) = x(t) i + y(t) j = t i + 4t^2 j
        r_equation = MathTex("r(t) = x(t) \\, i + y(t) \\, j = t \\, i + 4t^2 \\, j", font_size=40).to_edge(UP)
        # Implementation: Displaying dr = (dx/dt) i + (dy/dt) j dt
        dr_equation = MathTex("dr = \\frac{dx}{dt} \\, i + \\frac{dy}{dt} \\, j \\, dt", font_size=40).next_to(r_equation, DOWN, buff=1)

        # Implementation: Adding voiceover for the first part of scene 4
        with self.voiceover(text="Now, let's express the position vector r as a function of t. r of t equals t i plus 4 t squared j.") as tracker:
            # Implementation: Animating the r(t) and dr equations
            self.play(Write(r_equation))
            self.play(Write(dr_equation))
            self.wait(tracker.duration)

        # Implementation: Deriving dx/dt = 1 and dy/dt = 8t
        dx_dt = MathTex("\\frac{dx}{dt} = 1", font_size=40).next_to(dr_equation, DOWN, buff=1).to_edge(LEFT)
        dy_dt = MathTex("\\frac{dy}{dt} = 8t", font_size=40).next_to(dx_dt, DOWN, buff=0.5).to_edge(LEFT)
        # Implementation: Highlighting terms in yellow during derivation
        dx_dt.set_color_by_tex("dx", YELLOW)
        dx_dt.set_color_by_tex("dt", YELLOW)
        dy_dt.set_color_by_tex("dy", YELLOW)
        dy_dt.set_color_by_tex("dt", YELLOW)
        dy_dt.set_color_by_tex("8t", YELLOW)

        # Implementation: Concluding with dr = (i + 8t j) dt
        dr_final = MathTex("dr = (i + 8t \\, j) \\, dt", font_size=40).next_to(dy_dt, DOWN, buff=1)

        # Implementation: Adding voiceover for the second part of scene 4
        with self.voiceover(text="To find d r, we differentiate x and y with respect to t. d x d t is 1, and d y d t is 8 t. Therefore, d r equals i plus 8 t j d t.") as tracker:
            # Implementation: Animating the derivation of dx/dt and dy/dt
            self.play(Write(dx_dt))
            self.wait(4)  # Waiting for the part of the audio where dy/dt is mentioned
            self.play(Write(dy_dt))
            self.wait(4)  # Waiting for the part of the audio where dr is concluded
            self.play(Write(dr_final))
            self.wait(tracker.duration - 8)

        # Cleaning: Clearing all objects for the next scene
        self.clear()

    def play_scene_5(self):
        # Implementation: Setting the voiceover service to GTTSService
        self.set_speech_service(GTTSService())
        # Implementation: Displaying F = 2x^2y i + 3xy j
        F_equation = MathTex("F = 2x^2y \\, i + 3xy \\, j", font_size=40).to_edge(UP)
        # Implementation: Substituting x = t and y = 4t^2
        F_substitution = MathTex("F = 2(t^2)(4t^2) \\, i + 3(t)(4t^2) \\, j", font_size=40).next_to(F_equation, DOWN, buff=1)
        # Implementation: Highlighting 't' and '4t^2' in yellow
        F_substitution.set_color_by_tex("t", YELLOW)
        F_substitution.set_color_by_tex("4t^2", YELLOW)

        # Implementation: Adding voiceover for the first part of scene 5
        with self.voiceover(text="Next, we need to express our force F in terms of t. Substituting t for x and 4 t squared for y in our force equation, we get") as tracker:
            # Implementation: Animating the force equation and substitution
            self.play(Write(F_equation))
            self.play(TransformMatchingTex(F_equation.copy(), F_substitution))
            self.wait(tracker.duration)

        # Implementation: Simplifying to F = 8t^4 i + 12t^3 j
        F_simplified = MathTex("F = 8t^4 \\, i + 12t^3 \\, j", font_size=40).next_to(F_substitution, DOWN, buff=1)

        # Implementation: Adding voiceover for the second part of scene 5
        with self.voiceover(text="F equals 2 times t squared times 4 t squared i plus 3 times t times 4 t squared j. Simplifying, we have F equals 8 t to the fourth i plus 12 t cubed j.") as tracker:
            # Implementation: Animating the simplification process
            self.play(TransformMatchingTex(F_substitution.copy(), F_simplified))
            self.wait(tracker.duration)

        # Cleaning: Clearing all objects for the next scene
        self.clear()

    def play_scene_6(self):
        # Implementation: Setting the voiceover service to GTTSService
        self.set_speech_service(GTTSService())
        # Implementation: Displaying F · dr = (8t^4 i + 12t^3 j) · (i + 8t j) dt
        F_dot_dr = MathTex("F \\cdot dr = (8t^4 \\, i + 12t^3 \\, j) \\cdot (i + 8t \\, j) \\, dt", font_size=40).to_edge(UP)

        # Implementation: Adding voiceover for the first part of scene 6
        with self.voiceover(text="Now we can calculate the dot product of F and d r.") as tracker:
            # Implementation: Animating the dot product equation
            self.play(Write(F_dot_dr))
            self.wait(tracker.duration)

        # Implementation: Calculating the dot product step-by-step
        dot_product_calc = MathTex("(8t^4 \\cdot 1) + (12t^3 \\cdot 8t) \\, dt", font_size=40).next_to(F_dot_dr, DOWN, buff=1)
        # Implementation: Highlighting each term in yellow during multiplication
        dot_product_calc.set_color_by_tex("8t^4", YELLOW)
        dot_product_calc.set_color_by_tex("1", YELLOW)
        dot_product_calc.set_color_by_tex("12t^3", YELLOW)
        dot_product_calc.set_color_by_tex("8t", YELLOW)
        # Implementation: Simplifying to 104t^4 dt
        dot_product_simplified = MathTex("= (8t^4 + 96t^4) \\, dt = 104t^4 \\, dt", font_size=40).next_to(dot_product_calc, DOWN, buff=0.5)

        # Implementation: Adding voiceover for the second part of scene 6
        with self.voiceover(text="F dot d r equals 8 t to the fourth i plus 12 t cubed j dot i plus 8 t j d t. This simplifies to 8 t to the fourth plus 96 t to the fourth d t, which is 104 t to the fourth d t.") as tracker:
            # Implementation: Animating the dot product calculation and simplification
            self.play(Write(dot_product_calc))
            self.wait(8)  # Waiting for the part of the audio where simplification starts
            self.play(Write(dot_product_simplified))
            self.wait(tracker.duration - 8)

        # Cleaning: Clearing all objects for the next scene
        self.clear()

    def play_scene_7(self):
        # Implementation: Setting the voiceover service to GTTSService
        self.set_speech_service(GTTSService())
        # Implementation: Displaying "Limits: t = 0 to t = 1"
        limits = MathTex("\\text{Limits: } t = 0 \\text{ to } t = 1", font_size=40).to_edge(UP)

        # Implementation: Adding voiceover for the first part of scene 7
        with self.voiceover(text="Since our particle moves from zero zero to one four, our limits for t are from zero to one.") as tracker:
            # Implementation: Animating the limits
            self.play(Write(limits))
            self.wait(tracker.duration)

        # Implementation: Displaying the integral W = ∫(from 0 to 1) 104t^4 dt
        integral = MathTex("W = \\int_{0}^{1} 104t^4 \\, dt", font_size=40).next_to(limits, DOWN, buff=1)

        # Implementation: Adding voiceover for the second part of scene 7
        with self.voiceover(text="Now we can evaluate the integral: W equals the integral from zero to one of 104 t to the fourth d t.") as tracker:
            # Implementation: Animating the integral
            self.play(Write(integral))
            self.wait(tracker.duration)

        # Implementation: Integrating 104t^4 to get 104[t^5/5] (from 0 to 1)
        integration = MathTex("W = 104 \\left[ \\frac{t^5}{5} \\right]_{0}^{1}", font_size=40).next_to(integral, DOWN, buff=1)
        # Implementation: Highlighting the limits of integration in yellow
        integration.set_color_by_tex("0", YELLOW)
        integration.set_color_by_tex("1", YELLOW)
        # Implementation: Calculating W = 104 * (1/5) = 20.8
        calculation = MathTex("W = 104 \\cdot \\frac{1}{5} = 20.8", font_size=40).next_to(integration, DOWN, buff=0.5)

        # Implementation: Adding voiceover for the third part of scene 7
        with self.voiceover(text="This gives us 104 times t to the fifth over five, evaluated from zero to one. Plugging in the limits, we get 104 times one-fifth, which equals 20.8.") as tracker:
            # Implementation: Animating the integration and calculation
            self.play(Write(integration))
            self.wait(5)  # Waiting for the part of the audio where calculation starts
            self.play(Write(calculation))
            self.wait(tracker.duration - 5)

        # Cleaning: Clearing all objects for the next scene
        self.clear()

    def play_scene_8(self):
        # Implementation: Setting the voiceover service to GTTSService
        self.set_speech_service(GTTSService())
        # Implementation: Displaying text "Conclusion"
        conclusion_text = Text("Conclusion", font_size=48).to_edge(UP)

        # Implementation: Creating the coordinate plane
        axes = Axes(
            x_range=[0, 1.5, 0.5],
            y_range=[0, 5, 1],
            x_length=6,
            y_length=4,
            axis_config={"color": WHITE},
            x_axis_config={"numbers_to_include": [0, 1]},
            y_axis_config={"numbers_to_include": [0, 4]},
            tips=False,
        ).set_color(BLUE_E)
        # Implementation: Drawing the curve y = 4x^2
        curve = axes.plot(lambda x: 4 * x**2, x_range=[0, 1], color=YELLOW)

        # Implementation: Adding voiceover for the first part of scene 8
        with self.voiceover(text="So, to recap, we found that the work done by the force F equals 2 x squared y i plus 3 x y j, in displacing a particle from zero zero to one four along the curve y equals 4 x squared,") as tracker:
            # Implementation: Animating the conclusion text and coordinate plane with the curve
            self.play(Write(conclusion_text))
            self.play(Create(axes), Create(curve))
            self.wait(tracker.duration)

        # Implementation: Displaying text "Work Done = 20.8 units"
        work_done_text = Text("Work Done = 20.8 units", font_size=48, weight=BOLD)

        # Implementation: Adding voiceover for the second part of scene 8
        with self.voiceover(text="is 20.8 units. This result highlights how the work done depends on both the force and the path taken.") as tracker:
            # Implementation: Animating the final result
            self.play(Write(work_done_text))
            self.wait(tracker.duration)

        # Cleaning: Clearing all objects for the next scene
        self.clear()