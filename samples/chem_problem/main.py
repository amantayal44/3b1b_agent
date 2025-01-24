
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
        # Implementation: Display "Problem:" in white text on a dark background, centered at the top of the screen.
        problem_title = Text("Problem:", font_size=48)
        problem_title.to_edge(UP)

        # Implementation: Below the title, display the problem statement: "The ratio of mass percent of C and H of an organic compound (CxHyOz) is 6 : 1. If one molecule of the above compound ( CxHyOZ ) contains half as much oxygen as required to burn one molecule of compound CXHY completely to CO2 and H2O. The empirical formula of compound CxHyOz is :".
        # Implementation: Center the text and scale down to ensure it fits within the frame.
        problem_statement_text = """
            The ratio of mass percent of C and H of an organic compound (CxHyOz) is 6 : 1.
            If one molecule of the above compound ( CxHyOZ ) contains half as much
            oxygen as required to burn one molecule of compound CXHY completely to
            CO2 and H2O. The empirical formula of compound CxHyOz is :
        """
        problem_statement = Text(problem_statement_text, font_size=24, line_spacing=1.5)
        # Calculating: Center the text and scale down to ensure it fits within the frame.
        problem_statement.next_to(problem_title, DOWN, buff=0.5)

        with self.voiceover(text="Let's tackle this chemistry problem. We're given an organic compound with the general formula CxHyOz. The mass ratio of carbon to hydrogen is 6 to 1. And, the oxygen in this molecule is half of what would be needed to completely burn CxHy into carbon dioxide and water. Our task is to find the empirical formula of this compound.") as tracker:
            # Implementation: Animate the display of the problem title and statement.
            self.play(Write(problem_title))
            self.play(Write(problem_statement))
        # Cleaning: No need to remove objects as they are used in the next scene.

    def play_scene_2(self):
        # Implementation: Display the title "Mass Ratio to Mole Ratio" in white text on a dark background, centered at the top.
        title = Text("Mass Ratio to Mole Ratio", font_size=48)
        title.to_edge(UP)

        # Implementation: Below, display "Assume 100g of the compound."
        assumption = Text("Assume 100g of the compound", font_size=36)
        assumption.next_to(title, DOWN, buff=0.5)

        # Implementation: Then show calculations in a list format: "Mass of C = 60g, Moles of C = 60g / 12 g/mol = 5 mol".
        # Calculating: Calculate mass of C from the ratio 6:1 in 100g. Mass of C = (6 / (6+1)) * 100 = 60g
        mass_c = Text("Mass of C = 60g", font_size=36)
        # Calculating: Position mass_c below assumption.
        mass_c.next_to(assumption, DOWN, buff=0.5)
        # Calculating: Calculate moles of C. Moles = Mass / Molar Mass = 60g / 12 g/mol = 5 mol
        moles_c = Text("Moles of C = 60g / 12 g/mol = 5 mol", font_size=36)
        # Calculating: Position moles_c below mass_c.
        moles_c.next_to(mass_c, DOWN, buff=0.5)

        # Implementation: Below that, display "Mass of H = 10g, Moles of H = 10g / 1 g/mol = 10 mol".
        # Calculating: Calculate mass of H from the ratio 6:1 in 100g. Mass of H = (1 / (6+1)) * 100 = 10g
        mass_h = Text("Mass of H = 10g", font_size=36)
        # Calculating: Position mass_h below moles_c.
        mass_h.next_to(moles_c, DOWN, buff=0.5)
        # Calculating: Calculate moles of H. Moles = Mass / Molar Mass = 10g / 1 g/mol = 10 mol
        moles_h = Text("Moles of H = 10g / 1 g/mol = 10 mol", font_size=36)
        # Calculating: Position moles_h below mass_h.
        moles_h.next_to(mass_h, DOWN, buff=0.5)

        # Implementation: Finally, display "Mole Ratio C:H = 5:10 = 1:2". Represent this as "CxH2x".
        mole_ratio = Text("Mole Ratio C:H = 5:10 = 1:2", font_size=36)
        # Calculating: Position mole_ratio below moles_h.
        mole_ratio.next_to(moles_h, DOWN, buff=0.5)
        representation = Text("CxH2x", font_size=36)
        # Calculating: Position representation below mole_ratio.
        representation.next_to(mole_ratio, DOWN, buff=0.5)

        with self.voiceover(text="First, let's convert the mass ratio of carbon and hydrogen to a mole ratio. If we assume we have 100 grams of the compound, then according to the mass ratio, we have 60 grams of carbon and 10 grams of hydrogen.") as tracker:
            # Implementation: Animate the display of the title and assumption.
            self.play(Write(title))
            self.play(Write(assumption))
            # Implementation: Animate the display of mass of C.
            self.play(Write(mass_c))

        with self.voiceover(text="To find the moles, we divide the mass by the atomic mass. For carbon, 60 grams divided by 12 grams per mole gives us 5 moles. For hydrogen, 10 grams divided by 1 gram per mole gives us 10 moles.") as tracker:
            # Implementation: Animate the display of moles of C and mass of H.
            self.play(Write(moles_c))
            self.play(Write(mass_h))
            # Implementation: Animate the display of moles of H.
            self.play(Write(moles_h))

        with self.voiceover(text="So, the mole ratio of carbon to hydrogen is 5 to 10, which simplifies to 1 to 2. This means we can represent the compound as CxH2x.") as tracker:
            # Implementation: Animate the display of mole ratio and representation.
            self.play(Write(mole_ratio))
            self.play(Write(representation))
        # Cleaning: Remove all objects except representation.
        self.clear()
        self.add(representation)

    def play_scene_3(self):
        # Implementation: Display the general combustion reaction: "CxHy + (x + y/4)O2 --> xCO2 + (y/2)H2O" in white text on a dark background, centered on the top-half of the screen.
        combustion_reaction = MathTex("C_xH_y + (x + \\frac{y}{4})O_2 \\rightarrow xCO_2 + \\frac{y}{2}H_2O", font_size=36)
        # Calculating: Position combustion_reaction on the top-half of the screen.
        combustion_reaction.to_edge(UP)

        # Implementation: Below this, substitute x=1 and y=2 to get "CH2 + (1+2/4)O2 --> 1CO2 + 1H2O", simplifying to "CH2 + (3/2)O2 --> CO2 + H2O".
        # Implementation: Each equation should be centered.
        example_reaction = MathTex("CH_2 + (1+\\frac{2}{4})O_2 \\rightarrow 1CO_2 + 1H_2O", font_size=36)
        # Calculating: Position example_reaction below combustion_reaction.
        example_reaction.next_to(combustion_reaction, DOWN, buff=0.5)
        simplified_reaction = MathTex("CH_2 + \\frac{3}{2}O_2 \\rightarrow CO_2 + H_2O", font_size=36)
        # Calculating: Position simplified_reaction below example_reaction.
        simplified_reaction.next_to(example_reaction, DOWN, buff=0.5)

        with self.voiceover(text="Now, let's look at the combustion reaction. The general equation for burning CxHy is CxHy plus (x plus y over 4) O2 yields xCO2 plus (y over 2) H2O. Using our C to H ratio of 1 to 2, let's use CH2 as an example. Substituting into the equation, we get CH2 plus (1 plus 2 over 4) O2, which simplifies to CH2 plus 3 over 2 O2, yielding CO2 and H2O. This tells us that one molecule of CH2 needs 1.5 molecules of O2 for complete combustion.") as tracker:
            # Implementation: Animate the display of the combustion reaction.
            self.play(Write(combustion_reaction))
            # Implementation: Animate the display of the example reaction and its simplification.
            self.play(Write(example_reaction))
            self.play(TransformMatchingTex(example_reaction.copy(), simplified_reaction))
        # Cleaning: Remove all objects.
        self.clear()

    def play_scene_4(self):
        # Implementation: Display "Oxygen in CxHyOz = 1/2 * Oxygen needed for CxHy" in white text on a dark background, centered.
        oxygen_statement = Text("Oxygen in CxHyOz = 1/2 * Oxygen needed for CxHy", font_size=36)
        oxygen_statement.to_edge(UP)

        # Implementation: Below this, show "Oxygen needed for CH2 = 1.5 O2".
        oxygen_needed = Text("Oxygen needed for CH2 = 1.5 O2", font_size=36)
        # Calculating: Position oxygen_needed below oxygen_statement.
        oxygen_needed.next_to(oxygen_statement, DOWN, buff=0.5)

        # Implementation: Then calculate "Oxygen in CxHyOz = 1/2 * 1.5 O2 = 0.75 O2".
        oxygen_calculation = MathTex("Oxygen \\ in \\ C_xH_yO_z = \\frac{1}{2} * 1.5 \\ O_2 = 0.75 \\ O_2", font_size=36)
        # Calculating: Position oxygen_calculation below oxygen_needed.
        oxygen_calculation.next_to(oxygen_needed, DOWN, buff=0.5)

        # Implementation: Finally, show "0.75 O2 = 1.5 O atoms".
        oxygen_atoms = Text("0.75 O2 = 1.5 O atoms", font_size=36)
        # Calculating: Position oxygen_atoms below oxygen_calculation.
        oxygen_atoms.next_to(oxygen_calculation, DOWN, buff=0.5)

        with self.voiceover(text="The problem states that our compound, CxHyOz, contains half the oxygen needed for the complete combustion of CxHy. We found that CH2 needs 1.5 molecules of O2. Therefore, CxHyOz contains half of this, which is 0.75 molecules of O2. Since O2 is diatomic, this corresponds to 1.5 atoms of oxygen.") as tracker:
            # Implementation: Animate the display of the oxygen statement.
            self.play(Write(oxygen_statement))
            # Implementation: Animate the display of the oxygen needed for CH2.
            self.play(Write(oxygen_needed))
            # Implementation: Animate the display of the oxygen calculation.
            self.play(Write(oxygen_calculation))
            # Implementation: Animate the display of the oxygen atoms.
            self.play(Write(oxygen_atoms))
        # Cleaning: Remove all objects.
        self.clear()

    def play_scene_5(self):
        # Implementation: Display "Initial Formula: C1H2O1.5" in white text on a dark background, centered on the screen.
        initial_formula = Text("Initial Formula: C1H2O1.5", font_size=48)
        # Calculating: Center initial_formula on the screen.
        initial_formula.move_to(ORIGIN)

        with self.voiceover(text="Based on our findings, we can now write the initial formula of the compound as C1H2O1.5.") as tracker:
            # Implementation: Animate the display of the initial formula.
            self.play(Write(initial_formula))
        # Cleaning: Remove all objects.
        self.clear()

    def play_scene_6(self):
        # Implementation: Show "Multiply by 2 to get whole numbers" in white text on a dark background, centered.
        multiply_text = Text("Multiply by 2 to get whole numbers", font_size=36)
        multiply_text.to_edge(UP)

        # Implementation: Then display the conversion: "C1 * 2 = C2", "H2 * 2 = H4", "O1.5 * 2 = O3".
        c_conversion = MathTex("C_1 * 2 = C_2", font_size=36)
        # Calculating: Position c_conversion below multiply_text.
        c_conversion.next_to(multiply_text, DOWN, buff=0.5)
        h_conversion = MathTex("H_2 * 2 = H_4", font_size=36)
        # Calculating: Position h_conversion below c_conversion.
        h_conversion.next_to(c_conversion, DOWN, buff=0.5)
        o_conversion = MathTex("O_{1.5} * 2 = O_3", font_size=36)
        # Calculating: Position o_conversion below h_conversion.
        o_conversion.next_to(h_conversion, DOWN, buff=0.5)

        # Implementation: Finally, show "Empirical Formula: C2H4O3".
        empirical_formula = Text("Empirical Formula: C2H4O3", font_size=48)
        # Calculating: Position empirical_formula below o_conversion.
        empirical_formula.next_to(o_conversion, DOWN, buff=1)

        with self.voiceover(text="To get the empirical formula, we need whole number subscripts. We multiply each subscript by 2. This gives us C2, H4, and O3. Thus, the empirical formula of the compound is C2H4O3.") as tracker:
            # Implementation: Animate the display of the multiply instruction.
            self.play(Write(multiply_text))
            # Implementation: Animate the display of the conversions.
            self.play(Write(c_conversion))
            self.play(Write(h_conversion))
            self.play(Write(o_conversion))
            # Implementation: Animate the display of the empirical formula.
            self.play(Write(empirical_formula))
        # Cleaning: Remove all objects except empirical_formula.
        self.clear()
        self.add(empirical_formula)

    def play_scene_7(self):
        # Implementation: Display "Summary:" in white text on a dark background, centered at the top.
        summary_title = Text("Summary:", font_size=48)
        summary_title.to_edge(UP)

        # Implementation: List the main steps below it: "1. Mass Ratio to Mole Ratio", "2. Combustion Reaction", "3. Oxygen Content", "4. Empirical Formula".
        step1 = Text("1. Mass Ratio to Mole Ratio", font_size=36)
        # Calculating: Position step1 below summary_title.
        step1.next_to(summary_title, DOWN, buff=0.5)
        step2 = Text("2. Combustion Reaction", font_size=36)
        # Calculating: Position step2 below step1.
        step2.next_to(step1, DOWN, buff=0.5)
        step3 = Text("3. Oxygen Content", font_size=36)
        # Calculating: Position step3 below step2.
        step3.next_to(step2, DOWN, buff=0.5)
        step4 = Text("4. Empirical Formula", font_size=36)
        # Calculating: Position step4 below step3.
        step4.next_to(step3, DOWN, buff=0.5)

        # Implementation: Then show "Final Answer: C2H4O3".
        final_answer = Text("Final Answer: C2H4O3", font_size=48)
        # Calculating: Position final_answer below step4.
        final_answer.next_to(step4, DOWN, buff=1)

        with self.voiceover(text="Let's summarize what we did. We converted the mass ratio to a mole ratio, analyzed the combustion reaction, determined the oxygen content, and finally arrived at the empirical formula. So, the empirical formula of the organic compound is C2H4O3. Understanding empirical formulas is crucial in chemistry as it helps us identify unknown compounds and predict their behavior.") as tracker:
            # Implementation: Animate the display of the summary title.
            self.play(Write(summary_title))
            # Implementation: Animate the display of the summary steps.
            self.play(Write(step1))
            self.play(Write(step2))
            self.play(Write(step3))
            self.play(Write(step4))
            # Implementation: Animate the display of the final answer.
            self.play(Write(final_answer))
        # Cleaning: Remove all objects.
        self.clear()