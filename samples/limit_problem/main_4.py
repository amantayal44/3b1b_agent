
class AnimationVideo(VoiceoverScene):


    def play_scene_1(self):
        # Implementation: Set speech service to GTTSService
        self.set_speech_service(GTTSService())

        # Implementation: Create function and limit text objects
        function_text = MathTex("f(x) = \\frac{\\sin(x)}{x}")
        limit_text = MathTex("\\lim_{x \\to 0} \\frac{\\sin(x)}{x}")
        substitution_text = MathTex("\\frac{\\sin(0)}{0} = \\frac{0}{0}")
        indeterminate_label = Text("Indeterminate", color=RED).scale(0.5)

        # Implementation: Group function and limit text, then position them
        group = VGroup(function_text, limit_text).arrange(DOWN)

        # Implementation: Position substitution text below the group
        substitution_text.next_to(group, DOWN)

        # Implementation: Position indeterminate label next to substitution text
        indeterminate_label.next_to(substitution_text, RIGHT)

        # Implementation: Animate writing function and limit text with voiceover
        with self.voiceover(text="Today, we're going to tackle a classic limit problem: finding the limit of sin(x)/x as x approaches 0. If we try direct substitution, we get sin(0)/0, which is 0/0.") as tracker:
            self.play(Write(group))
            self.wait(0.5)
            self.play(Write(substitution_text))
            self.wait(0.5)
            self.play(Write(indeterminate_label))

        self.wait(tracker.duration-tracker.time_until_bookmark())

        # Implementation: Animate writing "Indeterminate" label with voiceover
        with self.voiceover(text="This is an indeterminate form, meaning we can't determine the limit just by plugging in 0. So, we need a different strategy.") as tracker:
            #self.play(Write(indeterminate_label))
            self.wait(tracker.duration)

        # Cleaning: Remove all objects except indeterminate label
        self.remove(group, substitution_text)

    def play_scene_2(self):
        # Implementation: Set speech service to GTTSService
        self.set_speech_service(GTTSService())

        # Implementation: Create unit circle
        circle = Circle(radius=2, color=BLUE)

        # Implementation: Create origin point
        origin = Dot(ORIGIN)

        # Implementation: Create origin label
        origin_label = MathTex("O").next_to(origin, DOWN).scale(0.7)

        # Implementation: Create x-axis and y-axis
        axes = Axes(x_range=[-1, 7, 1], y_range=[-4, 4, 1], tips=False, axis_config={"include_numbers": True}).scale(0.7).shift(LEFT*2)

        # Implementation: Animate drawing unit circle with voiceover
        with self.voiceover(text="Let's visualize this using the unit circle.") as tracker:
            self.play(
                Create(axes),
                Create(circle),
                Create(origin),
                Create(origin_label)
            )
            self.wait(tracker.duration)

        # Implementation: Create angle x
        angle_x = Angle(axes.x_axis, Line(ORIGIN, circle.point_at_angle(PI/6)), radius=0.7, color=GREEN, other_angle=False)

        # Implementation: Create angle x label
        angle_label = MathTex("x", color=GREEN).next_to(angle_x, RIGHT, buff=0.1).scale(0.7)

        # Implementation: Create point P
        point_P = Dot(circle.point_at_angle(PI/6))

        # Implementation: Create point P label
        point_P_label = MathTex("P(\\cos(x), \\sin(x))", color=WHITE).next_to(point_P, UP).scale(0.7)

        # Implementation: Animate drawing angle x and point P with voiceover
        with self.voiceover(text="We draw an angle x, and mark the point P on the circle. The coordinates of P are (cos(x), sin(x)).") as tracker:
            self.play(
                Create(angle_x),
                Create(angle_label),
                Create(point_P),
                Create(point_P_label)
            )
            self.wait(tracker.duration)

        # Implementation: Create vertical line from P to x-axis
        line_PA = DashedLine(point_P.get_center(), axes.c2p(np.cos(PI/6), 0), color=YELLOW)

        # Implementation: Create point A
        point_A = Dot(axes.c2p(np.cos(PI/6), 0))

        # Implementation: Create point A label
        point_A_label = MathTex("A(\\cos(x), 0)", color=WHITE).next_to(point_A, DOWN).scale(0.7)

        # Implementation: Animate drawing line PA and point A with voiceover
        with self.voiceover(text="We drop a perpendicular to the x-axis, meeting at point A.") as tracker:
            self.play(
                Create(line_PA),
                Create(point_A),
                Create(point_A_label)
            )
            self.wait(tracker.duration)

        # Implementation: Create tangent line at (1,0)
        line_tangent = DashedLine(axes.c2p(1,0), axes.c2p(1, 2*np.tan(PI/6)), color=YELLOW)

        # Implementation: Create line OT
        line_OT = DashedLine(origin.get_center(), axes.c2p(1, 2*np.tan(PI/6)), color=YELLOW)

        # Implementation: Create point T
        point_T = Dot(axes.c2p(1, 2*np.tan(PI/6)))

        # Implementation: Create point T label
        point_T_label = MathTex("T(1, \\tan(x))", color=WHITE).next_to(point_T, RIGHT).scale(0.7)

        # Implementation: Animate drawing tangent line and point T with voiceover
        with self.voiceover(text="We also draw a tangent at (1,0), intersecting the line from the origin at point T, which has coordinates (1, tan(x)).") as tracker:
            self.play(
                Create(line_tangent),
                Create(line_OT),
                Create(point_T),
                Create(point_T_label)
            )
            self.wait(tracker.duration)

        # Cleaning: Keep all objects for the next scene

    def play_scene_3(self):
        # Implementation: Set speech service to GTTSService
        self.set_speech_service(GTTSService())

        # Implementation: Get objects from previous scene
        # Implementation: Get point_P, origin, point_A, angle_x from previous scene
        point_P = self.mobjects[-3]
        origin = self.mobjects[2]
        point_A = self.mobjects[-5]
        angle_x = self.mobjects[4]

        # Implementation: Create triangle OAP
        triangle_OAP = Polygon(origin.get_center(), point_A.get_center(), point_P.get_center(), fill_opacity=0.5, color=RED)

        # Implementation: Create area formula for triangle OAP
        triangle_OAP_area = MathTex("\\frac{1}{2}\\cos(x)\\sin(x)", color=RED).next_to(triangle_OAP, RIGHT).scale(0.7)

        # Implementation: Animate filling triangle OAP with voiceover
        with self.voiceover(text="Now, let's compare some areas. Triangle OAP has area (1/2)cos(x)sin(x).") as tracker:
            self.play(
                Create(triangle_OAP),
                Write(triangle_OAP_area)
            )
            self.wait(tracker.duration)

        # Implementation: Get point_T from previous scene
        point_T = self.mobjects[-2]

        # Implementation: Create sector OAP
        sector_OAP = Sector(outer_radius=2, angle=PI/6, start_angle=0, fill_opacity=0.5, color=GREEN).shift(LEFT*2)

        # Implementation: Create area formula for sector OAP
        sector_OAP_area = MathTex("\\frac{1}{2}x", color=GREEN).scale(0.7).next_to(sector_OAP, LEFT, buff=0.7)

        # Implementation: Animate filling sector OAP with voiceover
        with self.voiceover(text="The circular sector OAP has area (1/2)x, since the radius is 1.") as tracker:
            self.play(
                Create(sector_OAP),
                Write(sector_OAP_area)
            )
            self.wait(tracker.duration)

        # Implementation: Create triangle OAT
        triangle_OAT = Polygon(origin.get_center(), point_A.get_center()+2*RIGHT, point_T.get_center(), fill_opacity=0.5, color=BLUE)

        # Implementation: Create area formula for triangle OAT
        triangle_OAT_area = MathTex("\\frac{1}{2}\\tan(x)", color=BLUE).next_to(triangle_OAT, UP).scale(0.7)

        # Implementation: Animate filling triangle OAT with voiceover
        with self.voiceover(text="And triangle OAT has area (1/2)tan(x).") as tracker:
            self.play(
                Create(triangle_OAT),
                Write(triangle_OAT_area)
            )
            self.wait(tracker.duration)

        # Implementation: Scale down the existing objects to make space for new ones
        self.play(
            *[obj.animate.scale(0.7).shift(UP*1.4+LEFT*0.5) for obj in self.mobjects]
        )

        # Implementation: Create inequality text
        inequality = MathTex(
            "\\frac{1}{2}\\cos(x)\\sin(x)", "<", "\\frac{1}{2}x", "<", "\\frac{1}{2}\\tan(x)", color=WHITE
        ).scale(0.7).move_to(DOWN*2.5)

        # Implementation: Set colors for inequality parts
        inequality[0].set_color(RED)
        inequality[2].set_color(GREEN)
        inequality[4].set_color(BLUE)

        # Implementation: Animate writing inequality with voiceover
        with self.voiceover(text="Visually, we can see that the area of triangle OAP is less than the area of sector OAP, which is less than the area of triangle OAT. So, we have this inequality.") as tracker:
            self.play(Write(inequality))
            self.wait(tracker.duration)

        # Cleaning: Remove filled triangles and sector, keep area formulas and inequality
        self.remove(triangle_OAP, sector_OAP, triangle_OAT)

    def play_scene_4(self):
        # Implementation: Set speech service to GTTSService
        self.set_speech_service(GTTSService())

        # Implementation: Get inequality from the previous scene
        inequality = self.mobjects[-1]

        # Implementation: Rearrange inequality to focus on sin(x)/x
        new_inequality_1 = MathTex("2", "\\cdot", "\\frac{1}{2}", "\\cos(x)\\sin(x)", "<", "2", "\\cdot", "\\frac{1}{2}x", "<", "2", "\\cdot", "\\frac{1}{2}\\tan(x)", color=WHITE).scale(0.7).move_to(inequality.get_center())
        new_inequality_2 = MathTex("\\cos(x)\\sin(x)", "<", "x", "<", "\\tan(x)", color=WHITE).scale(0.7).move_to(inequality.get_center())
        new_inequality_3 = MathTex("\\cos(x)", "<", "\\frac{x}{\\sin(x)}", "<", "\\frac{\\tan(x)}{\\sin(x)}", color=WHITE).scale(0.7).move_to(inequality.get_center())
        new_inequality_4 = MathTex("\\cos(x)", "<", "\\frac{x}{\\sin(x)}", "<", "\\frac{\\sin(x)}{\\cos(x)}", "\\cdot", "\\frac{1}{\\sin(x)}", color=WHITE).scale(0.7).move_to(inequality.get_center())
        new_inequality_5 = MathTex("\\cos(x)", "<", "\\frac{x}{\\sin(x)}", "<", "\\frac{1}{\\cos(x)}", color=WHITE).scale(0.7).move_to(inequality.get_center())
        new_inequality_6 = MathTex("\\frac{1}{\\cos(x)}", ">", "\\frac{\\sin(x)}{x}", ">", "\\cos(x)", color=WHITE).scale(0.7).move_to(inequality.get_center())
        new_inequality_7 = MathTex("\\cos(x)", "<", "\\frac{\\sin(x)}{x}", "<", "\\frac{1}{\\cos(x)}", color=WHITE).scale(0.7).move_to(inequality.get_center())

        # Implementation: Set colors for inequality parts
        new_inequality_1[3].set_color(RED)
        new_inequality_1[7].set_color(GREEN)
        new_inequality_1[11].set_color(BLUE)
        new_inequality_2[0].set_color(RED)
        new_inequality_2[2].set_color(GREEN)
        new_inequality_2[4].set_color(BLUE)

        # Implementation: Highlight "2" in yellow
        new_inequality_1[0].set_color(YELLOW)
        new_inequality_1[5].set_color(YELLOW)
        new_inequality_1[9].set_color(YELLOW)

        # Implementation: Animate multiplying by 2 with voiceover
        with self.voiceover(text="Our goal is to isolate sin(x)/x. First, we multiply everything by 2.") as tracker:
            self.play(
                Transform(inequality, new_inequality_1)
            )
            self.wait(tracker.duration)

        # Implementation: Animate simplifying by cancelling 2 with voiceover
        with self.voiceover(text="") as tracker:
            self.play(
                Transform(inequality, new_inequality_2)
            )
            self.wait(tracker.duration)

        # Implementation: Highlight "/sin(x)" in yellow
        temp_inequality = MathTex("\\frac{\\cos(x)\\sin(x)}{\\sin(x)}", "<", "\\frac{x}{\\sin(x)}", "<", "\\frac{\\tan(x)}{\\sin(x)}", color=WHITE).scale(0.7).move_to(inequality.get_center())
        temp_inequality[0][7:14].set_color(YELLOW)
        temp_inequality[2][1:8].set_color(YELLOW)
        temp_inequality[4][7:14].set_color(YELLOW)

        # Implementation: Animate dividing by sin(x) with voiceover
        with self.voiceover(text="Then, we divide by sin(x).") as tracker:
            self.play(Transform(inequality, temp_inequality))
            self.wait(tracker.duration)

        # Implementation: Animate simplifying by cancelling sin(x) with voiceover
        with self.voiceover(text="") as tracker:
            self.play(
                Transform(inequality, new_inequality_3)
            )
            self.wait(tracker.duration)

        # Implementation: Highlight "sin(x)/cos(x)" in yellow
        new_inequality_4[4].set_color(YELLOW)

        # Implementation: Animate replacing tan(x) with sin(x)/cos(x) with voiceover
        with self.voiceover(text="Next, we replace tan(x) with sin(x)/cos(x).") as tracker:
            self.play(Transform(inequality, new_inequality_4))
            self.wait(tracker.duration)

        # Implementation: Animate simplifying by cancelling sin(x) with voiceover
        with self.voiceover(text="") as tracker:
            self.play(
                Transform(inequality, new_inequality_5)
            )
            self.wait(tracker.duration)

        # Implementation: Highlight inversion and flipped inequality signs in yellow
        new_inequality_6[0].set_color(YELLOW)
        new_inequality_6[1].set_color(YELLOW)
        new_inequality_6[2].set_color(YELLOW)
        new_inequality_6[3].set_color(YELLOW)
        new_inequality_6[4].set_color(YELLOW)

        # Implementation: Animate taking reciprocal and flipping inequality signs with voiceover
        with self.voiceover(text="Now, we take the reciprocal of each part, remembering to flip the inequality signs.") as tracker:
            self.play(Transform(inequality, new_inequality_6))
            self.wait(tracker.duration)

        # Implementation: Animate rearranging inequality with voiceover
        with self.voiceover(text="Finally, we rearrange to get cos(x) < sin(x)/x < 1/cos(x).") as tracker:
            self.play(Transform(inequality, new_inequality_7))
            self.wait(tracker.duration)

        # Cleaning: Keep only the final inequality
        #self.clear()
        #self.add(inequality)

    def play_scene_5(self):
        # Implementation: Set speech service to GTTSService
        self.set_speech_service(GTTSService())

        # Implementation: Get inequality from the previous scene
        inequality = self.mobjects[-1]

        # Implementation: Create limit of cos(x) text
        limit_cos = MathTex("\\lim_{x \\to 0} \\cos(x) = 1", color=WHITE).scale(0.7).next_to(inequality, DOWN, buff=0.5)

        # Implementation: Animate writing limit of cos(x) with voiceover
        with self.voiceover(text="We know that the limit of cos(x) as x approaches 0 is 1.") as tracker:
            self.play(Write(limit_cos))
            self.wait(tracker.duration)

        # Implementation: Create limit of 1/cos(x) text
        limit_inv_cos = MathTex("\\lim_{x \\to 0} \\frac{1}{\\cos(x)} = 1", color=WHITE).scale(0.7).next_to(limit_cos, DOWN, buff=0.5)

        # Implementation: Animate writing limit of 1/cos(x) with voiceover
        with self.voiceover(text="and the limit of 1/cos(x) as x approaches 0 is also 1.") as tracker:
            self.play(Write(limit_inv_cos))
            self.wait(tracker.duration)

        # Implementation: Create squeeze theorem inequality text
        squeeze_inequality = MathTex(
            "\\lim_{x \\to 0} \\cos(x) \\leq \\lim_{x \\to 0} \\frac{\\sin(x)}{x} \\leq \\lim_{x \\to 0} \\frac{1}{\\cos(x)}",
            color=WHITE
        ).scale(0.7).next_to(limit_inv_cos, DOWN, buff=0.5)

        # Implementation: Highlight limits of cos(x) and 1/cos(x) in green
        squeeze_inequality[0][0:13].set_color(GREEN)
        squeeze_inequality[0][39:].set_color(GREEN)

        # Implementation: Animate writing squeeze theorem inequality with voiceover
        with self.voiceover(text="The Squeeze Theorem tells us that if a function is squeezed between two other functions that both approach the same limit, then the squeezed function must also approach that limit.") as tracker:
            self.play(
                #Write(squeeze_inequality)
                Transform(inequality, squeeze_inequality)
            )
            self.wait(tracker.duration)

        # Implementation: Create final conclusion text
        final_conclusion = MathTex("1 \\leq \\lim_{x \\to 0} \\frac{\\sin(x)}{x} \\leq 1", color=WHITE).scale(0.7).next_to(squeeze_inequality, DOWN, buff=0.5)
        boxed_conclusion = MathTex("\\therefore, \\lim_{x \\to 0} \\frac{\\sin(x)}{x} = 1", color=WHITE).scale(0.7).next_to(final_conclusion, DOWN, buff=0.5)
        box = SurroundingRectangle(boxed_conclusion, color=WHITE, buff=0.2)

        # Implementation: Animate writing final conclusion with voiceover
        with self.voiceover(text="So, since sin(x)/x is squeezed between cos(x) and 1/cos(x), and both of those approach 1, the limit of sin(x)/x as x approaches 0 must also be 1.") as tracker:
            self.play(Write(final_conclusion))
            self.wait(0.5)
            self.play(
                Write(boxed_conclusion),
                Create(box)
            )
            self.wait(tracker.duration)

        # Cleaning: Remove all objects except the boxed conclusion
        self.remove(inequality, limit_cos, limit_inv_cos, squeeze_inequality, final_conclusion)

    def play_scene_6(self):
        # Implementation: Set speech service to GTTSService
        self.set_speech_service(GTTSService())

        # Implementation: Create equation for sin(-x)/-x
        sin_neg_x_eq = MathTex("\\frac{\\sin(-x)}{-x} = \\frac{-\\sin(x)}{-x} = \\frac{\\sin(x)}{x}", color=WHITE).scale(0.7).shift(UP)

        # Implementation: Animate writing equation with voiceover
        with self.voiceover(text="So far, we've only considered positive values of x. But what about negative angles? We can use the property that sin(-x) = -sin(x). This means sin(-x)/-x is the same as sin(x)/x.") as tracker:
            self.play(Write(sin_neg_x_eq))
            self.wait(tracker.duration)

        # Implementation: Create equation for limit as x approaches 0 from the negative side
        limit_neg_x = MathTex("\\lim_{x \\to 0^-} \\frac{\\sin(x)}{x} = \\lim_{y \\to 0^+} \\frac{\\sin(-y)}{-y} = \\lim_{y \\to 0^+} \\frac{\\sin(y)}{y} = 1", color=WHITE).scale(0.7).next_to(sin_neg_x_eq, DOWN, buff=0.5)

        # Implementation: Highlight the substitution "y = -x" in yellow
        limit_neg_x[0][24:30].set_color(YELLOW)

        # Implementation: Animate writing limit equation with voiceover
        with self.voiceover(text="If we let y = -x, then as x approaches 0 from the negative side, y approaches 0 from the positive side. So, the limit from the negative side is the same as the limit from the positive side, which is 1.") as tracker:
            self.play(Write(limit_neg_x))
            self.wait(tracker.duration)

        # Cleaning: Remove all objects
        self.clear()
```