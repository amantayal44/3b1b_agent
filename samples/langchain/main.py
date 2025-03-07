
%%manim -qm -v ERROR AnimationVideo

from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
import numpy as np
import scipy as sp

LIGHT_GREEN = "#90EE90"  # LightGreen
LIGHT_BLUE = "#ADD8E6"   # LightBlue
LIGHT_YELLOW = "#FFFFE0" # LightYellow
BROWN = "#A52A2A"	   	 # Brown

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
        # Implementation: Set the speech service to GTTSService for voiceovers.
        self.set_speech_service(GTTSService())
        # Implementation: Create the central "LangChain" text.
        langchain_text = Text("LangChain", font_size=72, weight=BOLD).set_color(WHITE)

        # Implementation: Create the component labels.
        llms_text = Text("LLMs", font_size=36).set_color(LIGHT_BLUE).next_to(langchain_text, UP + LEFT, buff=1)
        prompts_text = Text("Prompts", font_size=36).set_color(LIGHT_BLUE).next_to(langchain_text, UP + RIGHT, buff=1)
        chains_text = Text("Chains", font_size=36).set_color(LIGHT_BLUE).next_to(langchain_text, DOWN + LEFT, buff=1)
        indexes_text = Text("Indexes", font_size=36).set_color(LIGHT_BLUE).next_to(langchain_text, DOWN, buff=1)
        agents_text = Text("Agents", font_size=36).set_color(LIGHT_BLUE).next_to(langchain_text, DOWN + RIGHT, buff=1)

        # Implementation: Create the arrows.
        llms_arrow = Arrow(llms_text.get_bottom(), langchain_text.get_top(), buff=0.1, color=WHITE)
        prompts_arrow = Arrow(prompts_text.get_bottom(), langchain_text.get_top(), buff=0.1, color=WHITE)
        chains_arrow = Arrow(chains_text.get_top(), langchain_text.get_bottom(), buff=0.1, color=WHITE)
        indexes_arrow = Arrow(indexes_text.get_top(), langchain_text.get_bottom(), buff=0.1, color=WHITE)
        agents_arrow = Arrow(agents_text.get_top(), langchain_text.get_bottom(), buff=0.1, color=WHITE)

        # Implementation: Animate the first part of the scene.
        with self.voiceover(text="Imagine you want to build an application using the power of large language models. That's where LangChain comes in.") as tracker:
            # Thinking: Display the "LangChain" text.
            self.play(Write(langchain_text))

        # Implementation: Animate the second part of the scene.
        with self.voiceover(text="It's a powerful framework that helps you connect different components like LLMs, prompts, and more, making it easier to create intelligent applications.") as tracker:
            # Thinking: Display the component labels and connect them with arrows.
            self.play(
                Write(llms_text),
                Create(llms_arrow),
            )
            self.play(
                Write(prompts_text),
                Create(prompts_arrow),
            )
            self.play(
                Write(chains_text),
                Create(chains_arrow),
            )
            self.play(
                Write(indexes_text),
                Create(indexes_arrow),
            )
            self.play(
                Write(agents_text),
                Create(agents_arrow),
            )

        # Cleaning: Remove all objects from the scene.
        self.clear()

    def play_scene_2(self):
        # Implementation: Create the LLM box.
        llm_box = Rectangle(width=4, height=3, color=BLACK, fill_opacity=0.5)
        llm_box.set_fill(BLACK, opacity=0.5)
        llm_label = Text("LLM", font_size=48, color=WHITE).move_to(llm_box)

        # Implementation: Create the input and output text.
        input_text = Text("Input Text", font_size=36, color=WHITE)
        output_text = Text("Output Text", font_size=36, color=WHITE)

        # Implementation: Animate the first part of the scene.
        with self.voiceover(text="At the heart of LangChain are Large Language Models, or LLMs. Think of them as powerful engines that can understand and generate text.") as tracker:
            # Thinking: Display the LLM box and label.
            self.play(Create(llm_box), Write(llm_label))
            # Thinking: Animate the "Input Text" moving into the box.
            self.play(input_text.animate.next_to(llm_box, LEFT, buff=1))
            self.play(input_text.animate.move_to(llm_box))

        # Implementation: Create example input and output.
        example_input = Text("What is the capital of France?", font_size=24, color=WHITE).move_to(llm_box)
        example_output = Text("Paris", font_size=24, color=WHITE).next_to(llm_box, RIGHT, buff=1)

        # Implementation: Animate the second part of the scene.
        with self.voiceover(text="You give them some input text, and they produce a relevant output.") as tracker:
            # Thinking: Show the example input and output.
            self.play(Transform(input_text, example_input))
            self.play(input_text.animate.next_to(llm_box, LEFT, buff=1))
            self.play(Write(example_output))
            # Thinking: Animate the "Output Text" moving out of the box.
            self.play(output_text.animate.next_to(llm_box, RIGHT, buff=1))

        # Cleaning: Keep the LLM box and label for the next scene.
        self.remove(input_text, output_text, example_output)

    def play_scene_3(self):
        # Implementation: Get the LLM box and label from the previous scene.
        llm_box = self.mobjects[0]
        llm_label = self.mobjects[1]

        # Implementation: Create the "Prompt" text.
        prompt_text = Text("Prompt", font_size=48, color=WHITE).to_edge(UP + LEFT)

        # Implementation: Create the arrow from "Prompt" to the LLM box.
        prompt_arrow = Arrow(prompt_text.get_bottom(), llm_box.get_top(), buff=0.1, color=BLUE)

        # Implementation: Animate the first part of the scene.
        with self.voiceover(text="To get the desired output from an LLM, you need to give it instructions. These instructions are called prompts.") as tracker:
            # Thinking: Display the "Prompt" text and the arrow.
            self.play(Write(prompt_text))
            self.play(Create(prompt_arrow))

        # Implementation: Create examples of prompts.
        prompt_examples = VGroup(
            Text("Translate to French: Hello", font_size=24, color=WHITE),
            Text("Summarize this article:", font_size=24, color=WHITE),
            Text("Write a poem about nature", font_size=24, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(prompt_text, DOWN, buff=0.5)

        # Implementation: Animate the second part of the scene.
        with self.voiceover(text="A well-crafted prompt is crucial for getting the results you want.") as tracker:
            # Thinking: Display the prompt examples.
            self.play(Write(prompt_examples))

        # Cleaning: Keep the LLM box and label for the next scene. Remove other objects.
        self.remove(prompt_text, prompt_arrow, prompt_examples)

    def play_scene_4(self):
        # Implementation: Get the LLM box and label from the previous scene.
        llm_box = self.mobjects[0]
        llm_label = self.mobjects[1]

        # Implementation: Create the sequence of boxes for the LLMChain.
        prompt_box = RoundedRectangle(width=2, height=1, corner_radius=0.5, color=LIGHT_BLUE, fill_opacity=0.5).move_to(llm_box).shift(LEFT * 3)
        output_box = RoundedRectangle(width=2, height=1, corner_radius=0.5, color=LIGHT_BLUE, fill_opacity=0.5).move_to(llm_box).shift(RIGHT * 3)
        prompt_label = Text("Prompt", font_size=24, color=WHITE).move_to(prompt_box)
        output_label = Text("Output", font_size=24, color=WHITE).move_to(output_box)

        # Implementation: Create the arrows connecting the boxes.
        arrow1 = Arrow(prompt_box.get_right(), llm_box.get_left(), buff=0.1, color=WHITE)
        arrow2 = Arrow(llm_box.get_right(), output_box.get_left(), buff=0.1, color=WHITE)

        # Implementation: Create the "LLMChain" label.
        llmchain_label = Text("LLMChain", font_size=36, color=WHITE).next_to(prompt_box, UP, buff=1)

        # Implementation: Animate the first part of the scene.
        with self.voiceover(text="Chains allow you to combine multiple steps, including calls to an LLM. A simple example is an LLMChain, where you provide a prompt, the LLM processes it, and you get an output.") as tracker:
            # Thinking: Display the sequence of boxes, labels, and arrows.
            self.play(
                Create(prompt_box),
                Create(output_box),
                Write(prompt_label),
                Write(output_label),
                Create(arrow1),
                Create(arrow2),
                Write(llmchain_label)
            )

        # Implementation: Create the example prompt and output.
        example_prompt = Text("Write a tagline for a coffee shop", font_size=24, color=WHITE).move_to(prompt_box)
        example_output = Text("Your daily dose of happiness", font_size=24, color=WHITE).move_to(output_box)

        # Implementation: Animate the second part of the scene.
        with self.voiceover(text="For example, if the prompt is 'Write a tagline for a coffee shop', the LLM might output 'Your daily dose of happiness'.") as tracker:
            # Thinking: Animate the prompt and output moving through the chain.
            self.play(Transform(prompt_label, example_prompt))
            self.play(prompt_label.animate.move_to(llm_box))
            self.play(Transform(prompt_label, output_label), Transform(output_label, example_output))

        # Cleaning: Remove all objects from the scene.
        self.clear()

    def play_scene_5(self):
        # Implementation: Create the index.
        index_shape = Cylinder(radius=1, height=2, resolution=(8, 8), show_faces=True, fill_opacity=0.5, color=GRAY).to_edge(RIGHT)
        index_label = Text("Index", font_size=36, color=WHITE).move_to(index_shape)

        # Implementation: Create the LLM box.
        llm_box = Rectangle(width=4, height=3, color=BLACK, fill_opacity=0.5)
        llm_box.set_fill(BLACK, opacity=0.5)
        llm_label = Text("LLM", font_size=48, color=WHITE).move_to(llm_box)
        self.add(llm_box, llm_label)

        # Implementation: Create the arrow connecting the LLM box and the index.
        arrow = Arrow(llm_box.get_right(), index_shape.get_left(), buff=0.1, color=WHITE)

        # Implementation: Animate the first part of the scene.
        with self.voiceover(text="Indexes help you store and retrieve information efficiently.") as tracker:
            # Thinking: Display the index and the arrow.
            self.play(DrawBorderThenFill(index_shape), Write(index_label))
            self.play(Create(arrow))

        # Implementation: Create the example query and information.
        example_query = Text("What is the best coffee shop in town?", font_size=24, color=WHITE).move_to(llm_box)
        example_info = Text("List of coffee shops with ratings", font_size=24, color=WHITE).move_to(index_shape)

        # Implementation: Animate the second part of the scene.
        with self.voiceover(text="You can query the index to provide relevant data to the LLM, making your application more powerful.") as tracker:
            # Thinking: Animate the query and information flow.
            self.play(Transform(llm_label, example_query))
            self.play(llm_label.animate.move_to(index_shape))
            self.play(Transform(llm_label, llm_label), Transform(index_label, example_info))
            self.play(index_label.animate.move_to(llm_box))

        # Cleaning: Remove all objects from the scene.
        self.clear()

    def play_scene_6(self):
        # Implementation: Create the "Agent" box.
        agent_box = Rectangle(width=2, height=1, color=WHITE, fill_opacity=0.5)
        agent_label = Text("Agent", font_size=36, color=WHITE).move_to(agent_box)

        # Implementation: Create the tool boxes.
        search_box = Rectangle(width=1.5, height=1, color=YELLOW, fill_opacity=0.5).next_to(agent_box, UP, buff=1)
        search_label = Text("Search", font_size=24, color=WHITE).move_to(search_box)
        calculator_box = Rectangle(width=1.5, height=1, color=GREEN, fill_opacity=0.5).next_to(agent_box, LEFT, buff=1)
        calculator_label = Text("Calculator", font_size=24, color=WHITE).move_to(calculator_box)
        calendar_box = Rectangle(width=1.5, height=1, color=ORANGE, fill_opacity=0.5).next_to(agent_box, RIGHT, buff=1)
        calendar_label = Text("Calendar", font_size=24, color=WHITE).move_to(calendar_box)

        # Implementation: Create the arrows from the "Agent" box to the tool boxes.
        search_arrow = Arrow(agent_box.get_top(), search_box.get_bottom(), buff=0.1, color=WHITE)
        calculator_arrow = Arrow(agent_box.get_left(), calculator_box.get_right(), buff=0.1, color=WHITE)
        calendar_arrow = Arrow(agent_box.get_right(), calendar_box.get_left(), buff=0.1, color=WHITE)

        # Implementation: Animate the first part of the scene.
        with self.voiceover(text="Agents are like decision-makers that can choose the right tool for a given task.") as tracker:
            # Thinking: Display the "Agent" box, tool boxes, and arrows.
            self.play(
                Create(agent_box),
                Write(agent_label),
                Create(search_box),
                Write(search_label),
                Create(calculator_box),
                Write(calculator_label),
                Create(calendar_box),
                Write(calendar_label),
                Create(search_arrow),
                Create(calculator_arrow),
                Create(calendar_arrow)
            )

        # Implementation: Create the example question.
        example_question = Text("What's the weather like tomorrow and find best Italian restaurant near me?", font_size=24, color=WHITE).next_to(agent_box, UP, buff=1)

        # Implementation: Animate the second part of the scene.
        with self.voiceover(text="Based on the user's input, the agent selects the appropriate tools to use, such as searching the web or performing calculations.") as tracker:
            # Thinking: Show the question and highlight the chosen tools.
            self.play(Write(example_question))
            self.play(example_question.animate.move_to(agent_box))
            self.play(
                search_box.animate.set_color(YELLOW_A).set_stroke(width=6),
                calendar_box.animate.set_color(ORANGE_A).set_stroke(width=6)
            )

        # Cleaning: Remove all objects from the scene.
        self.clear()

    def play_scene_7(self):
        # Implementation: Create the components of the diagram.
        user_input = Text("User Input", font_size=36, color=WHITE).to_edge(UP)
        prompt = Text("Prompt", font_size=36, color=WHITE).next_to(user_input, DOWN, buff=1)
        chain = Text("Chain", font_size=36, color=WHITE).next_to(prompt, DOWN, buff=1)
        llm = Text("LLM", font_size=36, color=WHITE).next_to(chain, DOWN, buff=1)
        output = Text("Output", font_size=36, color=WHITE).next_to(llm, DOWN, buff=1)
        indexes = Text("Indexes", font_size=36, color=WHITE).next_to(llm, LEFT, buff=2)
        agents = Text("Agents", font_size=36, color=WHITE).next_to(llm, RIGHT, buff=2)

        # Implementation: Create the arrows for the main flow.
        arrow_up = Arrow(user_input.get_bottom(), prompt.get_top(), buff=0.1, color=WHITE)
        arrow_pc = Arrow(prompt.get_bottom(), chain.get_top(), buff=0.1, color=WHITE)
        arrow_cl = Arrow(chain.get_bottom(), llm.get_top(), buff=0.1, color=WHITE)
        arrow_lo = Arrow(llm.get_bottom(), output.get_top(), buff=0.1, color=WHITE)

        # Implementation: Create the arrows for the side interactions.
        arrow_li = Arrow(llm.get_left(), indexes.get_right(), buff=0.1, color=WHITE)
        arrow_il = Arrow(indexes.get_left(), chain.get_right(), buff=0.1, color=WHITE)
        arrow_la = Arrow(llm.get_right(), agents.get_left(), buff=0.1, color=WHITE)
        arrow_al = Arrow(agents.get_right(), chain.get_left(), buff=0.1, color=WHITE)

        # Implementation: Group objects for easier animation.
        main_flow = VGroup(user_input, prompt, chain, llm, output)
        side_interactions = VGroup(indexes, agents)
        arrows = VGroup(arrow_up, arrow_pc, arrow_cl, arrow_lo, arrow_li, arrow_il, arrow_la, arrow_al)

        # Implementation: Animate the first part of the scene.
        with self.voiceover(text="Let's put it all together. LangChain takes user input, constructs a prompt, and uses a chain to execute a sequence of operations.") as tracker:
            # Thinking: Display the diagram components and arrows.
            self.play(
                Write(main_flow),
                Write(side_interactions),
                Create(arrows)
            )

        # Implementation: Animate the second part of the scene.
        with self.voiceover(text="This often involves calling an LLM and may also include interacting with indexes or using agents to decide the next steps. Finally, an output is produced for the user.") as tracker:
            # Thinking: Highlight each component as it's mentioned.
            self.play(Indicate(user_input))
            self.play(Indicate(prompt))
            self.play(Indicate(chain))
            self.play(Indicate(llm))
            self.play(Indicate(indexes))
            self.play(Indicate(agents))
            self.play(Indicate(output))

        # Cleaning: Remove all objects from the scene.
        self.clear()