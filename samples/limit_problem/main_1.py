
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