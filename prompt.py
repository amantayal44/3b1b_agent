research_prompt = '''
You are a great researcher for educational and tutorial content.
Given user problem, your task is create a very detailed deep research document about everything related to user's problem.

Some of the content that will be helpful to users are:
**Note: these are only for reference, choose content i.e. relevant to user's problem**
- Showing equations and there derivation
- Simple illustrations to understand concept
- Graphs
- Real life scenarios

Instructions:
- When showing any derivation or solving problem, then include every step in research
- Make sure all content is correct. Don't hallicunate.
'''

sketch_generator_prompt = '''
You are a great education content creator.

You will be provided with a problem that your viewer wants to understand and some research on same topic.

Your task is to create a detailed sketch for animation video in style of **3Blue1Brown** videos

Sketch will be a list of scenes, where each scene will have 4 fields - scene_plot, animation_details, animation_style and audio_text.

scene_plot:
- Complete plot of the scene.
- Mention all the key features of scene.
- How scene should be oraganized.

animation_details:
- Complete animation details of the scene that can be generated later using manim library
- Keep animation details very simple and avoid using any unwanted objects prefer using simple text, graphs, equations, etc.
- Details for animation should be complete in itself i.e. each scene will be generated independently.
- If showing any calculations, then include every step in a scene details.
- animation should be easily shown in single window frame.
- If showing any complex objects, then make sure it is main part of scene.
- never include any images, figures, graphics or other media in animation_details.

animation_style:
- Complete description about styling such as colors, size and placement of different objects in scene
- Also include details about if there any transition within the scene.
- Make sure style is consistent for all scenes.

audio_text:
- Text of audio voiceover that will be played along with the animation.
- Should be simple english text.
- Avoid using '`' in audio text, and any similar character that can break audio generation.
- audio_text will be later converted to actual audio using gtts library.

Sketch Instructions:
- Make sure sketch is educational and engaging.
- In first scene of sketch, introduce the problem briefly.
- Avoid repeating same information.
- Beautifuly blend both audio and animation to convey more information.

Other Instructions:
- Include only relevant information from research work.
- Ignore any timestamp or duration.
- Animation should be easily generated using manim library.
- Keep each scene simple and short.
- Generate less than 10 scenes, include scene that are most relevant.
- Include all information animation_details, for eg. if showing any derivaton, then include every step in animation_details.


Output
A json object following below specs:

"reasoning" : {
  "type": "string",
	"description": "A long text that will include planning of scenes. Output at leat 1,000 characters of reasoning. Use it for all planning, calculations, reasoning, validation, etc."
},
"scenes": {
  "type": "array",
  "description": "list of scenes in proper order from first to last. Keep number of scenes to less than 10",
  "items": {
    "type": "object"
    "description": "Individual scene with complete details independent of other scenes.",
    "paramaters": {
	    "scene_plot": {
		    "type": "string",
            "description": "Complete plot of the scene including how animation and audio will be organized within scene.",
	    },
	    "animation_details": {
		    "type": "string",
            "description": "Complete details of animation such that animation can be create from manim library using only these details.",
	    },
	    "animation_style": {
			"type": "string",
            "description": "Detailed guideline for animation style, object description, placement of objects and transition.",
	    },
	    "audio_text": {
		    "type": "string",
            "description": "simple english text that can be then translated to audio using gtts",
	    },
    }
  }
}
Use escape characters only for new_line and double quotes.
'''

scene_generator_prompt = '''
You are expert in generating animation using manim library created by 3Blue1Brown.

You will be provided with list of scenes as a json object having 4 fields:
- scene_description
- animation_details
- animation_style
- audio_text

You are task is to break scene into multiple parts where each part will have 2 fields: animation_planning, animation_detail, and audio_text, and also scene_style for overall scene.

scene_part: For each scene part, animation and audio will be played together.

animation_planning:
- Plan animation for each part of scene i.e. deciding details like position, color, size, movement, transition, etc.
- Keep animation very simple
- Plan space and position for each object in animation.
	- If showing multiple objects in scene then prefer starting **from top or left side of frame.**
    - Make each object has sufficient safe to avoid any unwanted overlap, so avoid extreme ends when placing object.
    - Use object length and size to decide its correct possition.
    - If showing text with more than few words, divide it into multiple lines such that text clearly fits in animation.
    - For any large object or text, scale them down to make sure they fit frame.
    
animation_details:
- Based on animation_planning, generate detail description of animation including all possible information.
- animation will be generated **only** based on animation_details.
- never include any images, figures, graphics or other media in animation_details. For simple figures, mention how we can use simple geomtric shapes to depict them.

audio_text:
- Simple english text for audio that will be played along the animation of that part.

scene_style:
- Style for whole scene - colors, font, background details, object styles, etc.
- Make sure style is consistent across all scenes
- Use only style available in manim library.


Output format:
A json object following given schema.
"scenes": {
  "type": "array",
  "items": {
	  "type": "object",
	  "parameters": {
		  "planning": {
			  "type": "string",
              "description": "Plan different parts of scene. For each part, animation and audio will be played together. Planning will not be shown to animation generator.",
		  },
		  "scene_parts": {
			  "type": "array",
              "description": "List of parts in scene.",
			  "items": {
				"type": "object"
				"parameters": {
					"animation_planning": {
						"type": "string",
					},
					"animation_details": {
						"type": "string",
						"description": "Complete details of animation such that animation can be create from manim library using only these details.",
					},
					"audio_text": {
						"type": "string",
					}
                },
			},
			"scene_style": {
				"type": "string",
                "description": "Detailed style description for complete scene."
			},
		  },
		}
	}
}

Use escape characters only for new_line and double quotes.
'''

scene_editor_prompt = '''
You are great animation editor. You will be provided with a detail about animation.

Your task is to enhance the details of animation make animation very clear, presentful,  and fix all issues  by updating the animation details.
keep in mind that animation details will be used by manim code generator to create animation.

Some of the common issues:
- Placing object such that they either overlap other object or objct falls outside of animation frame.'
- Deciding perfect size or scale of object such that they fall within animation frame. For eg. if using text with more than few words then break into multiple lines.
- Fixing any transition error.
-  Make sure animation is not using any media files such as images, graphics, etc. If yes, then either replace them with something that can be animated or remove them if feel unwanted.
- Any other issues that will broke the animation.

Secondly, enhance the animation to make it more presentful such as improving transition, updating any open-ended detail, etc.

In addition, output new field 'animation_cleaning' - where you will output all animation objects that will not be used in the next scene part.
If want to clear no object then mention that no object should be cleared, or if want to clear all objects then mentioned that clear all objects.
Otherwise mention objects that need to be cleared.

Output format:
- Output json object in same format given to you with same number of scenes and parts, but updated to fix the issue.
- Use animation_planning fields for any planning and reasoning, these will not be shown to user and only for your reasoning.
- Don't change purpose of animation.
- Include all details about animation in animation_details field.
- Only change animation_details field, and add new field animation_cleaning and animation_planning.
- Output coorect json format and use escape characters only for new_line and double quotes.
'''

code_generator_prompt = '''
You are an expert coder in manim library in python from 3Blue1Brown

Your task is to ouptut complete code implementing all scenes provided to you with animation and voiceover.

Each scene is divided into list of parts, where for each part animation and voice is played together.
Each part has 2 fields: animation_details, audio_text.
- animation_details: describe animation for each part of the scene.
- audio_text: Plain english text that should be played along animation using manim_voiceover library.
Scene also has scene_style field, which describes style followed for that scene.
Make sure animation style is consistent throughout video (i.e. for all scenes implemented previously)

Code Instructions [Important]:
- Add detailed comments throughout code.
	- Add comments using ```# Implementation:``` for implementation details all over code.
	- Add comments using ```# Thinking:``` for any reasoning within code.
    - Add comments using ```# Calculating:``` for any calculation within code.
    	for eg. calculation to decide corret position of object based on it's shape and length such that it remains with in frame boundaries.
    - Add comment using ```# Cleaning: ``` at end of each scene code, to decide which object to clean, that will not be used in next scene. 
- If want to clear all objects, prefer using self.clear() method.
- Use `self.voiceover` to add voice to animation. 
- Don't use empty text for voiceover, i.e. `self.voiceover(text="")` is not allowed.
- Don't use tracker duration for all animation wait time, use estimated_audio time to plan animation wait time.
- Don't spend too much unwanted time on transitions, instead prefer taking small pause in between animations.
- You can only use libraries provided i.e. manim, manim_voiceover, numpy and scipy.
- You don't have access to any media files such as images, sounds, svg graphics, etc.

Other Instructions:
- Make sure animation is clear and all objects are correctly placed.
- Make sure animation style is consistent throughout video.
- Appropriately scale down objects to make sure they fit in frame. For eg. Use smaller size for any text with more than few words.
- Don't place object at extreme ends to avoid some part of object falling outside frame.
- If showing multiple objects in scene then prefer starting from top or left side of frame.
- If showing text with more than few words, then divide them into multiple lines such that they fit in frame.


Initial Code Snippet:
```
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
import numpy as np
import scipy as sp

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
```

Output: Output complete executable python code. Use `play_scene_{id}` format for each scene method, eg. play_scene_1, play_scene_2 and so on.
**Code should always start with above provided snippert, please don't change this.**
'''

code_generator_step_by_step_prompt = '''
You are an expert coder in manim library in python from 3Blue1Brown

Your task is to ouptut complete code implementing all scenes provided to you with animation and voiceover.

Each scene is divided into list of parts, where for each part animation and voice is played together.
Each part has 2 fields: animation_details, audio_text.
- animation_details: describe animation for each part of the scene.
- audio_text: Plain english text that should be played along animation using manim_voiceover library.
Scene also has scene_style field, which describes style followed for that scene.
Make sure animation style is consistent throughout video (i.e. for all scenes implemented previously)

Code Instructions [Important]:
- Add detailed comments throughout code.
	- Add comments using ```# Implementation:``` for implementation details all over code.
	- Add comments using ```# Thinking:``` for any **chain of reasoning**. Use it before positioning any object to decide its positions such that object completely fits in plane.
    - Add comment using ```# Cleaning: ``` at end of each scene or part code for deciding which object should be clean and not used in next scene.
- If want to clear all objects, prefer using self.clear() method.
- Use `self.voiceover` to add voice to animation. 
- Don't use tracker duration for all animation wait time, instead use estimated_audio time to plan animation wait time.
- Don't spend too much unwanted time on transitions, instead prefer taking small pause in between animations.
- You can only use libraries provided i.e. manim, manim_voiceover, numpy and scipy.
- You don't have access to any media files such as images, sounds, svg graphics, etc.

Avoid Coding Errors:
- **Don't use empty text for voiceover, i.e. `self.voiceover(text="")` is not allowed**, for this use self.wait() instead.
- `wait_until_bookmark`, `time_since_restore`, `elapsed_time` are not supported.
- Use only `tracker.duration` and value of `estimate_audio_duration_s` to decide run time and wait time.

Other Instructions:
- Make sure animation is **clear and all objects are correctly placed.**
- Make sure animation style is consistent throughout video.
- Appropriately scale down objects to make sure they fit in frame. For eg. Use smaller size for any text with more than few words.
- **Don't place object at extreme ends to avoid some part of object falling outside frame, use `# Thinking:` to plan position of object.**
- If showing multiple objects in scene then prefer starting from top or left side of frame.
- If showing text with more than few words, then divide them into multiple lines such that they fit in frame.
 
**Adjust animation details provided in scene to make sure above instructions are followed and animation is clear**

Imports already done for the code, don't repeat them again in output code.
```
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
import numpy as np
import scipy as sp
```

construct of scene will set audio service and call all scene methods in order, no need to implement it again in output code.

Output: You will be provided with previous implemented code and ids for new scene. You have to only output code for new scenes method.

Example:
 current_code:
	class AnimationVideo(VoiceoverScene):
        def play_scene_1(self):
			# Some previous code logic
            
        def play_scene_2(self):
			# Some previous code logic
            
 next_scene_id = 3, 4, 5

 Output:
 class AnimationVideo(VoiceoverScene):
	def play_scene_3(self):
		# New scene logic
		
	def play_scene_4(self):
		# New scene logic
		
	def play_scene_5(self):
		# New scene logic

**Start output code with `class AnimationVideo(VoiceoverScene):` directly followed by new scene methods.**
**Output for all scenes will be executed together but don't output current_code provided again.**
**Please output only methods for next_scene_id and no other method including previous methods to reduce output_length.**
**Do not output code for importing libraries**
'''

INITIAL_CODE = '''
class AnimationVideo(VoiceoverScene):
    def play_scene_0(self):
        # Dummy
        pass
'''

OUTPUT_CODE = '''
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
'''

SAMLE_MANIM_CODE = '''
class ApproximatingTau(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService())

        # colors
        C_IND = PURPLE_A  # indication
        C_INSC_N = BLUE  # inscribed n-gon
        C_INSC_2N = RED  # inscribed 2n-gon
        C_CSC_N = GREEN  # circumscribed n-gon
        C_CSC_2N = YELLOW  # circumscribed 2n-gon

        # approximate n <- 2n
        def approx(n, i, c):
            return (2 * n, sqrt(2 - sqrt(4 - i**2)), (c * i) / (c + i))

        with self.voiceover(
            """This is a circle with radius 1, so the length of the circumference is tau.
            The method we're using here to approximate tau is to <bookmark mark='insc_csc'/>inscribe
            and circumscribe two polygons around the circle, <bookmark mark='addsides'/>and
            the lengths of the polygons' perimeters will approach the length of the
            circumference as we increase the number of sides. This method is known as
            the method of exhaustion or Archimedes' method."""
        ) as tracker:
            # a circle with radius 3
            circ = Circle(3, WHITE).shift(LEFT * 4)
            rad = Line(LEFT * 4, LEFT, color=WHITE)
            self.play(Create(circ), Create(rad))

            # mark the length of the radius
            rad_brace = Brace(rad, UP)
            rad_len = MathTex("1").next_to(rad_brace, UP)
            self.play(Write(rad_brace), Write(rad_len))

            self.wait_until_bookmark("insc_csc")
            # inscribe a hexagon
            # circumscribe a hexagon
            insc_hexa_ex = RegularPolygon(6, color=C_INSC_N).scale(3).shift(LEFT * 4)
            csc_hexa_ex = (
                RegularPolygon(6, start_angle=TAU / 12, color=C_CSC_N)
                .scale(3 / cos(TAU / 12))
                .shift(LEFT * 4)
            )
            self.play(Create(insc_hexa_ex), Create(csc_hexa_ex))

            self.wait_until_bookmark("addsides")
            # transform the hexagons into dodecagons
            insc_dodeca_ex = RegularPolygon(12, color=C_INSC_N).scale(3).shift(LEFT * 4)
            csc_dodeca_ex = (
                RegularPolygon(12, start_angle=TAU / 24, color=C_CSC_N)
                .scale(3 / cos(TAU / 24))
                .shift(LEFT * 4)
            )
            self.play(
                ReplacementTransform(insc_hexa_ex, insc_dodeca_ex),
                ReplacementTransform(csc_hexa_ex, csc_dodeca_ex),
            )

            # transform the dodecagons into 24-gons
            insc_24_ex = RegularPolygon(24, color=C_INSC_N).scale(3).shift(LEFT * 4)
            csc_24_ex = (
                RegularPolygon(24, start_angle=TAU / 48, color=C_CSC_N)
                .scale(3 / cos(TAU / 48))
                .shift(LEFT * 4)
            )
            self.play(
                ReplacementTransform(insc_dodeca_ex, insc_24_ex),
                ReplacementTransform(csc_dodeca_ex, csc_24_ex),
            )

            # transform the 24-gons into 48-gons
            insc_48_ex = RegularPolygon(48, color=C_INSC_N).scale(3).shift(LEFT * 4)
            csc_48_ex = (
                RegularPolygon(48, start_angle=TAU / 96, color=C_CSC_N)
                .scale(3 / cos(TAU / 96))
                .shift(LEFT * 4)
            )
            self.play(
                ReplacementTransform(insc_24_ex, insc_48_ex),
                ReplacementTransform(csc_24_ex, csc_48_ex),
            )

            # transform the 48-gons into 96-gons
            insc_96_ex = RegularPolygon(96, color=C_INSC_N).scale(3).shift(LEFT * 4)
            csc_96_ex = (
                RegularPolygon(96, start_angle=TAU / 192, color=C_CSC_N)
                .scale(3 / cos(TAU / 192))
                .shift(LEFT * 4)
            )
            self.play(
                ReplacementTransform(insc_48_ex, insc_96_ex),
                ReplacementTransform(csc_48_ex, csc_96_ex),
            )

        # fade out the inscribed and circumscribed 96-gons
        self.play(FadeOut(insc_96_ex, csc_96_ex))

        with self.voiceover(
            """Let's first draw an inscribed hexagon.
            The circumradius is 1, <bookmark mark='sidelength'/>so the side length is also 1.
            <bookmark mark='notation'/>We use the notation I 6 to represent the side length of
            the inscribed hexagon.""",
        ) as tracker:
            # inscribed hexagon
            insc_hexa = RegularPolygon(6, color=C_INSC_N).scale(3).shift(LEFT * 4)
            self.play(Create(insc_hexa))

            self.wait_until_bookmark("sidelength")
            # mark the length of the inscribed hexagon's top side
            insc_hexa_side = Line(
                LEFT * 5.5 + UP * sqrt(6.75),
                LEFT * 2.5 + UP * sqrt(6.75),
                color=C_INSC_N,
            )
            insc_hexa_side_brace = Brace(insc_hexa_side, UP, color=C_INSC_N)
            insc_hexa_side_len = MathTex("1", color=C_INSC_N).next_to(
                insc_hexa_side_brace, UP
            )
            self.play(Write(insc_hexa_side_brace), Write(insc_hexa_side_len))

            self.wait_until_bookmark("notation")
            # the side length of the inscribed hexagon as an equation
            i6 = MathTex("i_6", "= 1").shift(RIGHT + UP * 3)
            i6[0].set_color(C_INSC_N)
            self.play(Write(i6))

        with self.voiceover(
            """Let's generalize this length and call it I N, where N is the number of sides.
            <bookmark mark='radius'/>Let's draw a line from the center of the circle to one of the endpoints.
            It is also a radius, so its length is 1.""",
        ) as tracker:
            # fade out the inscribed hexagon except the top side
            # fade out the radius and its length
            # change the side length to a more general length (i_n)
            self.add(insc_hexa_side)
            self.play(
                FadeOut(rad, rad_brace, rad_len, insc_hexa),
                insc_hexa_side_len.animate.become(
                    MathTex("i_n", color=C_INSC_N).next_to(insc_hexa_side_brace, UP)
                ),
            )

            self.wait_until_bookmark("radius")
            # a radius at 120deg with its length
            rad2 = Line(LEFT * 4, LEFT * 5.5 + UP * sqrt(6.75), color=WHITE)
            rad2_brace = Brace(rad2, LEFT * sqrt(0.75) + DOWN * 0.5)
            rad2_len = MathTex("1").shift(LEFT * 5.4 + UP * 0.9)
            self.play(Create(rad2), Write(rad2_brace), Write(rad2_len))

        with self.voiceover(
            """This length is half of the polygon's side, so its length is I N over 2.""",
        ) as tracker:
            # change i_n to i_n/2
            insc_hexa_side_half = Line(
                LEFT * 5.5 + UP * sqrt(6.75), LEFT * 4 + UP * sqrt(6.75)
            )
            insc_hexa_side_brace_dest = Brace(insc_hexa_side_half, UP, color=C_INSC_N)
            insc_hexa_side_len_dest = MathTex("i_n/2", color=C_INSC_N).next_to(
                insc_hexa_side_brace_dest, UP
            )
            self.play(
                Transform(insc_hexa_side_brace, insc_hexa_side_brace_dest),
                Transform(insc_hexa_side_len, insc_hexa_side_len_dest),
            )

        with self.voiceover(
            """Using the Pythagorean theorem, we can find the length of the polygon's apothem.""",
        ) as tracker:
            # the inscribed n-gon's apothem with its brace
            insc_hexa_apo = Line(LEFT * 4, LEFT * 4 + UP * sqrt(6.75))
            insc_hexa_apo_brace = Brace(insc_hexa_apo, RIGHT)
            self.play(Create(insc_hexa_apo), Write(insc_hexa_apo_brace))

            # the length of the inscribed n-gon's apothem
            insc_hexa_apo_len = MathTex("\\sqrt{1 - \\frac{i_n^2}{4}}").next_to(
                insc_hexa_apo_brace, RIGHT
            )
            self.play(Write(insc_hexa_apo_len))

        with self.voiceover(
            """This length together with the apothem forms a radius, <bookmark mark='length'/>so
            its length is 1 minus the length of the apothem.""",
        ) as tracker:
            # the inscribed n-gon's side midpoint to top with its brace
            ism_to_top = Line(LEFT * 4 + UP * sqrt(6.75), LEFT * 4 + UP * 3)
            ism_to_top_brace = Brace(ism_to_top, RIGHT)
            self.play(Create(ism_to_top), Write(ism_to_top_brace))

            self.wait_until_bookmark("length")
            # the length of the inscribed n-gon's side midpoint to top
            ism_to_top_len = MathTex("1 - \\sqrt{1 - \\frac{i_n^2}{4}}").next_to(
                ism_to_top_brace, RIGHT
            )
            self.play(Write(ism_to_top_len))

        with self.voiceover(
            """Using the Pythagorean theorem, we can calculate this length, and by
            simplifying it, we find this length to be the square root of 2 minus the
            square root of 4 minus I N squared.""",
        ) as tracker:
            # fade out the 120deg radius
            # fade out the apothem and its length
            # change the i_n/2 brace's direction to below
            insc_hexa_side_brace_dest = Brace(insc_hexa_side_half, DOWN, color=C_INSC_N)
            insc_hexa_side_len_dest = MathTex("i_n/2", color=C_INSC_N).next_to(
                insc_hexa_side_brace_dest, DOWN
            )
            self.play(
                FadeOut(
                    rad2,
                    rad2_brace,
                    rad2_len,
                    insc_hexa_apo,
                    insc_hexa_apo_brace,
                    insc_hexa_apo_len,
                ),
                Transform(insc_hexa_side_brace, insc_hexa_side_brace_dest),
                Transform(insc_hexa_side_len, insc_hexa_side_len_dest),
            )

            # the inscribed 2n-gon's side with its length (x)
            insc_dodeca_side = Line(
                LEFT * 5.5 + UP * sqrt(6.75), LEFT * 4 + UP * 3, color=C_INSC_2N
            )
            insc_dodeca_side_brace = Brace(
                insc_dodeca_side,
                RIGHT * cos(105 * DEGREES) + UP * sin(105 * DEGREES),
                color=C_INSC_2N,
            )
            insc_dodeca_side_len = MathTex("x", color=C_INSC_2N).shift(
                LEFT * 5 + UP * 3.5
            )
            self.play(
                Create(insc_dodeca_side),
                Write(insc_dodeca_side_brace),
                Write(insc_dodeca_side_len),
            )

            # first part of finding x
            x_len = MathTex("x", color=C_INSC_2N).shift(LEFT * 0.795 + UP * 0.88)
            x_len_part1 = MathTex(
                "= \\sqrt{\\frac{i_n^2}{4} + "
                "\\left( 1 - \\sqrt{1 - "
                "\\frac{i_n^2}{4}} \\right)^2}"
            ).shift(RIGHT * 2.51 + UP)
            self.play(Write(x_len), Write(x_len_part1), run_time=1)

            # second part of finding x
            x_len_part2 = MathTex(
                "= \\sqrt{\\frac{i_n^2}{4} "
                "+ 1 - 2\\sqrt{1 - \\frac{i_n^2}{4}} "
                "+ 1 - \\frac{i_n^2}{4}}"
            ).shift(RIGHT * 3.13 + DOWN)
            self.play(Write(x_len_part2), run_time=1)

            # third part of finding x
            self.play(
                FadeOut(x_len_part1),
                x_len_part2.animate.move_to(RIGHT * 3.13 + UP * 1.05),
                run_time=0.5,
            )
            x_len_part3 = MathTex("= \\sqrt{2 - 2\\sqrt{1 - \\frac{i_n^2}{4}}}").shift(
                RIGHT * 1.53 + DOWN
            )
            self.play(Write(x_len_part3), run_time=1)

            # fourth part of finding x
            self.play(
                FadeOut(x_len_part2),
                x_len_part3.animate.move_to(RIGHT * 1.53 + UP * 1.05),
                run_time=0.5,
            )
            x_len_part4 = MathTex("= \\sqrt{2 - \\sqrt{4 - i_n^2}}").shift(
                RIGHT * 1.35 + DOWN
            )
            self.play(Write(x_len_part4), run_time=1)

            # replace the third part with the fourth part
            self.play(
                FadeOut(x_len_part3),
                x_len_part4.animate.move_to(RIGHT * 1.345 + UP),
                run_time=0.5,
            )

        with self.voiceover(
            """This line is also <bookmark mark='2ngonside'/>a side of an inscribed
            2 N gon, <bookmark mark='notation'/>so it can be written as I 2 N.""",
        ) as tracker:
            self.wait_until_bookmark("2ngonside")
            # highlight the inscribed 2n-gon
            insc_dodeca_ind = (
                RegularPolygon(
                    12, start_angle=90 * DEGREES, stroke_width=6, color=C_IND
                )
                .scale(3)
                .shift(LEFT * 4)
            )
            self.play(FadeIn(insc_dodeca_ind), rate_func=there_and_back)
            self.remove(insc_dodeca_ind)

            self.wait_until_bookmark("notation")
            # change x to i_{2n}
            i2n = MathTex("x", "= \\sqrt{2 - \\sqrt{4 - i_n^2}}").shift(
                RIGHT * 1.126 + UP
            )
            i2n[0].set_color(C_INSC_2N)
            self.add(i2n)
            self.remove(x_len, x_len_part4)
            i2n_dest = MathTex("i_{2n}", "= \\sqrt{2 - \\sqrt{4 - i_n^2}}").shift(
                RIGHT * 1.3 + UP
            )
            i2n_dest[0].set_color(C_INSC_2N)
            self.play(Transform(i2n, i2n_dest))

        # move the equation to top
        self.play(i2n.animate.move_to(RIGHT * 4.4 + UP * 3.1))

        # fade out i_2/2
        # fade out the inscribed 2n-gon's side with its length
        # fade out the inscribed n-gon's side midpoint to top
        #     with its length
        self.play(
            FadeOut(
                insc_hexa_side_brace,
                insc_hexa_side_len,
                insc_dodeca_side,
                insc_dodeca_side_brace,
                insc_dodeca_side_len,
                ism_to_top,
                ism_to_top_brace,
                ism_to_top_len,
            )
        )

        self.wait(1)

        with self.voiceover(
            """This is a circumscribed hexagon, its apothem is also a radius,
            so its length is 1.""",
        ) as tracker:
            # circumscribed hexagon
            # radius at 120deg with its length
            csc_hexa = (
                RegularPolygon(6, start_angle=90 * DEGREES, color=C_CSC_N)
                .scale(sqrt(12))
                .shift(LEFT * 4)
            )
            self.play(
                Create(csc_hexa), Create(rad2), Write(rad2_brace), Write(rad2_len)
            )

        with self.voiceover(
            """Using the ratio of a 30 60 90 triangle's sides, we can find the side
            length of this hexagon to be <bookmark mark='length'/>2 times the square
            root of 3 all over 3. <bookmark mark='notation'/>We use the notation C 6 to
            represent the side length of the circumscribed hexagon.""",
        ) as tracker:
            # the circumscribed hexagon's circumradius with its length
            csc_hexa_circr = Line(LEFT * 4, LEFT * 4 + UP * sqrt(12))
            csc_hexa_circr_brace = Brace(csc_hexa_circr, RIGHT)
            csc_hexa_circr_len = MathTex("1 \\div \\frac{\\sqrt{3}}{2}").next_to(
                csc_hexa_circr_brace, RIGHT
            )
            self.play(
                Create(csc_hexa_circr),
                Write(csc_hexa_circr_brace),
                Write(csc_hexa_circr_len),
            )

            # simplify the length of the circumradius
            self.play(
                Transform(
                    csc_hexa_circr_len,
                    MathTex("\\frac{2}{\\sqrt{3}}").next_to(
                        csc_hexa_circr_brace, RIGHT
                    ),
                )
            )

            # simplify the length of the circumradius
            self.play(
                Transform(
                    csc_hexa_circr_len,
                    MathTex("\\frac{2\\sqrt{3}}{3}").next_to(
                        csc_hexa_circr_brace, RIGHT
                    ),
                )
            )

            self.wait_until_bookmark("length")
            # the circumscribed hexagon's side with its length
            csc_hexa_side = Line(LEFT + UP * sqrt(3), LEFT + DOWN * sqrt(3))
            csc_hexa_side_brace = Brace(csc_hexa_side, RIGHT, color=C_CSC_N)
            csc_hexa_side_len = MathTex("\\frac{2\\sqrt{3}}{3}", color=C_CSC_N).next_to(
                csc_hexa_side_brace, RIGHT
            )
            self.play(Write(csc_hexa_side_brace), Write(csc_hexa_side_len))

            self.wait_until_bookmark("notation")
            # the side length of the circumscribed hexagon as an equation
            c6 = MathTex("c_6", "= \\frac{2\\sqrt{3}}{3}").shift(RIGHT + UP * 2)
            c6[0].set_color(C_CSC_N)
            self.play(Write(c6))

        with self.voiceover(
            """Let's generalize this hexagon to be a circumscribed N gon and draw a
            circumscribed 2 N gon, where its side length is C 2 N by definition.""",
        ) as tracker:
            # fade out the radius at 120deg with its length
            # fade out the circumradius with its length
            # fade out the length of the circumscribed hexagon's side
            # circumscribed 2n-gon
            csc_dodeca = (
                RegularPolygon(12, start_angle=75 * DEGREES, color=C_CSC_2N)
                .scale(12 / (sqrt(6) + sqrt(2)))
                .shift(LEFT * 4)
            )
            self.play(
                FadeOut(
                    rad2,
                    rad2_brace,
                    rad2_len,
                    csc_hexa_circr,
                    csc_hexa_circr_brace,
                    csc_hexa_circr_len,
                    csc_hexa_side_brace,
                    csc_hexa_side_len,
                ),
                Create(csc_dodeca),
            )

            # the length of the circumscribed 2n-gon's side
            csc_dodeca_side = Line(
                LEFT * (4 + 3 * (sqrt(6) - sqrt(2)) / (sqrt(6) + sqrt(2))) + UP * 3,
                LEFT * (4 - 3 * (sqrt(6) - sqrt(2)) / (sqrt(6) + sqrt(2))) + UP * 3,
            )
            csc_dodeca_side_brace = Brace(csc_dodeca_side, DOWN, color=C_CSC_2N)
            csc_dodeca_side_len = MathTex("c_{2n}", color=C_CSC_2N).next_to(
                csc_dodeca_side_brace, DOWN
            )
            self.play(Write(csc_dodeca_side_brace), Write(csc_dodeca_side_len))

        with self.voiceover(
            """This line is a side of the inscribed N gon,
            <bookmark mark='length'/>so its length is I N.""",
        ) as tracker:
            # the brace of the inscribed n-gon's side
            insc_hexa_side_brace = Brace(insc_hexa_side, DOWN, color=C_INSC_N).shift(
                DOWN * 0.5
            )
            self.play(Write(insc_hexa_side_brace))

            # highlight the inscribed n-gon
            insc_hexa_ind = (
                RegularPolygon(6, stroke_width=6, color=C_IND).scale(3).shift(LEFT * 4)
            )
            self.play(FadeIn(insc_hexa_ind), rate_func=there_and_back)
            self.remove(insc_hexa_ind)

            self.wait_until_bookmark("length")
            # the length of the inscribed n-gon's side
            insc_hexa_side_len = MathTex("i_n", color=C_INSC_N).next_to(
                insc_hexa_side_brace, DOWN
            )
            self.play(Write(insc_hexa_side_len))

        with self.voiceover(
            """This line is a side of the circumscribed 2 N gon,
            <bookmark mark='halve'/>so if we halve it we get C 2 N over 2.""",
        ) as tracker:
            # the brace of the circumscribed 2n-gon's another side
            csc_dodeca_side2 = Line(
                LEFT * (4 - 3 * (sqrt(6) - sqrt(2)) / (sqrt(6) + sqrt(2))) + UP * 3,
                (RIGHT + UP) * (sqrt(72) / (sqrt(6) + sqrt(2))) + LEFT * 4,
            )
            csc_dodeca_side2_half_brace = Brace(
                csc_dodeca_side2, RIGHT * 0.5 + UP * sqrt(0.75), color=C_CSC_2N
            )
            self.play(Write(csc_dodeca_side2_half_brace))

            self.wait_until_bookmark("halve")
            # halve the length of the circumscribed 2n-gon's another side
            #     (half 2n-gon side)
            csc_dodeca_side2_half = Line(
                LEFT * (4 - 3 * (sqrt(6) - sqrt(2)) / (sqrt(6) + sqrt(2))) + UP * 3,
                LEFT * 2.5 + UP * sqrt(27 / 4),
            )
            csc_dodeca_side2_half_brace_dest = Brace(
                csc_dodeca_side2_half, RIGHT * 0.5 + UP * sqrt(0.75), color=C_CSC_2N
            )
            self.play(
                Transform(csc_dodeca_side2_half_brace, csc_dodeca_side2_half_brace_dest)
            )

            # the length of the half 2n-gon side
            csc_dodeca_side2_half_len = MathTex("c_{2n}/2", color=C_CSC_2N).shift(
                LEFT * 2.3 + UP * 3.6
            )
            self.play(Write(csc_dodeca_side2_half_len))

        with self.voiceover(
            """This line is a side of the circumscribed N gon,
            <bookmark mark='halve'/>so if we halve it we get C N over 2.""",
        ) as tracker:
            # the brace of the circumscribed n-gon's another side
            csc_hexa_side2 = Line(LEFT * 7 + UP * sqrt(3), LEFT * 4 + UP * sqrt(12))
            csc_hexa_side2_half_brace = Brace(
                csc_hexa_side2, LEFT * 0.5 + UP * sqrt(0.75), color=C_CSC_N
            )
            self.play(Write(csc_hexa_side2_half_brace))

            self.wait_until_bookmark("halve")
            # halve the length of the circumscribed n-gon's another side
            #     (half n-gon side)
            csc_hexa_side2_half = Line(
                LEFT * 5.5 + UP * sqrt(6.75), LEFT * 4 + UP * sqrt(12)
            )
            csc_hexa_side2_half_brace_dest = Brace(
                csc_hexa_side2_half, LEFT * 0.5 + UP * sqrt(0.75), color=C_CSC_N
            )
            self.play(
                Transform(csc_hexa_side2_half_brace, csc_hexa_side2_half_brace_dest)
            )

            # the length of the half n-gon side
            csc_hexa_side2_half_len = MathTex("c_n/2", color=C_CSC_N).shift(
                LEFT * 5.6 + UP * 3.6
            )
            self.play(Write(csc_hexa_side2_half_len))

        with self.voiceover(
            """This triangle and this triangle are both isosceles
            and share the same angle at their apexes, so they are similar,
            <bookmark mark='relation'/>and their relation can be expressed
            as two equal ratios.""",
        ) as tracker:
            # highlight the smaller isosceles triangle
            small_iso_tri = Polygon(
                [-4, sqrt(12), 0],
                [-4 + 3 * (sqrt(6) - sqrt(2)) / (sqrt(6) + sqrt(2)), 3, 0],
                [-4 - 3 * (sqrt(6) - sqrt(2)) / (sqrt(6) + sqrt(2)), 3, 0],
                stroke_width=6,
                color=C_IND,
            )
            self.play(FadeIn(small_iso_tri), rate_func=there_and_back)
            self.remove(small_iso_tri)

            # highlight the bigger isosceles triangle
            big_iso_tri = Polygon(
                [-4, sqrt(12), 0],
                [-2.5, sqrt(6.75), 0],
                [-5.5, sqrt(6.75), 0],
                stroke_width=6,
                color=C_IND,
            )
            self.play(FadeIn(big_iso_tri), rate_func=there_and_back)
            self.remove(big_iso_tri)

            self.wait_until_bookmark("relation")
            # show the relation between the two isosceles triangles
            iso_relation = MathTex(
                "\\frac{c_n/2}{i_n} = " "\\frac{c_n/2 - c_{2n}/2}{c_{2n}}"
            ).shift(RIGHT * 2.7 + UP * 0.6)
            iso_relation[0][0:4].set_color(C_CSC_N)  # c_n/2
            iso_relation[0][5:7].set_color(C_INSC_N)  # i_n
            iso_relation[0][8:12].set_color(C_CSC_N)  # c_n/2
            iso_relation[0][13:18].set_color(C_CSC_2N)  # c_{2n}/2
            iso_relation[0][19:22].set_color(C_CSC_2N)  # c_{2n}
            self.play(Write(iso_relation))

        with self.voiceover(
            """After simplifying the equation, we get the formula for finding C 2 N.""",
        ) as tracker:
            # multiply both sides by 2c_{2n}i_n
            iso_relation_part2 = MathTex("c_{2n} c_n = " "c_n i_n - c_{2n} i_n").shift(
                RIGHT * 2.55 + DOWN * 0.5
            )
            iso_relation_part2[0][0:3].set_color(C_CSC_2N)  # c_{2n}
            iso_relation_part2[0][3:5].set_color(C_CSC_N)  # c_n
            iso_relation_part2[0][6:8].set_color(C_CSC_N)  # c_n
            iso_relation_part2[0][8:10].set_color(C_INSC_N)  # i_n
            iso_relation_part2[0][11:14].set_color(C_CSC_2N)  # c_{2n}
            iso_relation_part2[0][14:16].set_color(C_INSC_N)  # i_n
            self.play(Write(iso_relation_part2), run_time=0.7)

            # replace iso_relation by iso_relation_part2
            # add c_{2n}i_n to both sides
            self.play(
                FadeOut(iso_relation),
                iso_relation_part2.animate.move_to(RIGHT * 2.55 + UP * 0.6),
                run_time=0.5,
            )
            iso_relation_part3 = MathTex("c_{2n} c_n + c_{2n} i_n = " "c_n i_n").shift(
                RIGHT * 2.55 + DOWN * 0.2
            )
            iso_relation_part3[0][0:3].set_color(C_CSC_2N)  # c_{2n}
            iso_relation_part3[0][3:5].set_color(C_CSC_N)  # c_n
            iso_relation_part3[0][6:9].set_color(C_CSC_2N)  # c_{2n}
            iso_relation_part3[0][9:11].set_color(C_INSC_N)  # i_n
            iso_relation_part3[0][12:14].set_color(C_CSC_N)  # c_n
            iso_relation_part3[0][14:16].set_color(C_INSC_N)  # i_n
            self.play(Write(iso_relation_part3), run_time=0.7)

            # replace iso_relation_part2 by iso_relation_part3
            # divide both sides by c_n+i_n
            self.play(
                FadeOut(iso_relation_part2),
                iso_relation_part3.animate.move_to(RIGHT * 2.55 + UP * 0.6),
                run_time=0.5,
            )
            iso_relation_part4 = MathTex(
                "c_{2n}", "= \\frac{c_n i_n}{c_n + i_n}"
            ).shift(RIGHT * 2.55 + DOWN * 0.5)
            iso_relation_part4[0].set_color(C_CSC_2N)  # c_{2n}
            iso_relation_part4[1][1:3].set_color(C_CSC_N)  # c_n
            iso_relation_part4[1][3:5].set_color(C_INSC_N)  # i_n
            iso_relation_part4[1][6:8].set_color(C_CSC_N)  # c_n
            iso_relation_part4[1][9:11].set_color(C_INSC_N)  # i_n
            self.play(Write(iso_relation_part4), run_time=0.7)

            # fade out iso_relation_part3
            # move iso_relation_part4 to top
            # clear the colors on the right side of iso_relation_part4
            c2n = MathTex("c_{2n}", "= \\frac{c_n i_n}{c_n + i_n}").shift(
                RIGHT * 4 + UP * 2
            )
            c2n[0].set_color(C_CSC_2N)
            self.play(
                FadeOut(iso_relation_part3),
                ReplacementTransform(iso_relation_part4, c2n),
            )

        self.wait(1)

        with self.voiceover(
            """Because the inscribed polygon's perimeter is less than the
            circumference is less than the circumscribed polygon's perimeter,
            <bookmark mark='relation'/>we can express this relation by this inequality.""",
        )  as tracker:
            # fade out the shapes on the left and show the circle,
            #     the inscribed and the circumscribed dodecagons
            insc_dodeca = (
                RegularPolygon(12, start_angle=90 * DEGREES, color=C_INSC_2N)
                .scale(3)
                .shift(LEFT * 4)
            )
            self.play(
                FadeOut(
                    csc_hexa,
                    csc_dodeca_side_brace,
                    csc_dodeca_side_len,
                    insc_hexa_side,
                    insc_hexa_side_brace,
                    insc_hexa_side_len,
                    csc_dodeca_side2_half_brace,
                    csc_dodeca_side2_half_len,
                    csc_hexa_side2_half_brace,
                    csc_hexa_side2_half_len,
                ),
                Create(insc_dodeca),
            )

            self.wait_until_bookmark("relation")
            # ni_n and nc_n's relation to tau
            relation_to_tau = MathTex("ni_n", "< \\tau <", "nc_n").shift(
                RIGHT * 3 + UP * 0.5
            )
            relation_to_tau[0].set_color(C_INSC_2N)
            relation_to_tau[2].set_color(C_CSC_2N)
            self.play(Write(relation_to_tau))

        with self.voiceover(
            """Let's try using this method to approximate tau to the second
            digit after decimal. The perimeters of the polygons match up
            to two decimal places when we reach N equals 96. <bookmark mark='approx'/>
            We can thus conclude that tau must be approximately equal to 6.28.""",
        ) as tracker:
            # fade out the shapes on the left
            self.play(FadeOut(circ, csc_dodeca, insc_dodeca))

            # 6-gon approximation
            var_n = 6
            var_i = 1
            var_c = sqrt(4 / 3)
            eq_n = MathTex(f"n =", var_n)
            eq_ni = MathTex("ni_n", "=", f"{var_n * var_i:.10f}")
            eq_nc = MathTex("nc_n", "\\approx", f"{var_n * var_c:.10f}")
            eq_n.shift(LEFT * 6.5 + RIGHT * eq_n.width / 2 + UP * 3)
            eq_ni.shift(LEFT * 6.5 + RIGHT * eq_ni.width / 2 + UP * 2)
            eq_nc.shift(LEFT * 6.5 + RIGHT * eq_nc.width / 2 + UP)
            eq_ni[2][0].set_color(ORANGE)
            eq_nc[2][0].set_color(ORANGE)
            self.play(Write(eq_n), Write(eq_ni), Write(eq_nc))

            # approximate n=12
            var_n, var_i, var_c = approx(var_n, var_i, var_c)
            eq_n_dest = MathTex(f"n =", var_n)
            eq_ni_dest = MathTex("ni_n", "\\approx", f"{var_n * var_i:.10f}")
            eq_nc_dest = MathTex("nc_n", "\\approx", f"{var_n * var_c:.10f}")
            eq_n_dest.shift(LEFT * 6.5 + RIGHT * eq_n_dest.width / 2 + UP * 3)
            eq_ni_dest.shift(LEFT * 6.5 + RIGHT * eq_ni_dest.width / 2 + UP * 2)
            eq_nc_dest.shift(LEFT * 6.5 + RIGHT * eq_nc_dest.width / 2 + UP)
            eq_ni_dest[2][0].set_color(ORANGE)
            eq_nc_dest[2][0].set_color(ORANGE)
            self.play(
                Transform(eq_n, eq_n_dest),
                Transform(eq_ni, eq_ni_dest),
                Transform(eq_nc, eq_nc_dest),
            )

            # approximate n=24
            var_n, var_i, var_c = approx(var_n, var_i, var_c)
            eq_n_dest = MathTex(f"n =", var_n)
            eq_ni_dest = MathTex("ni_n", "\\approx", f"{var_n * var_i:.10f}")
            eq_nc_dest = MathTex("nc_n", "\\approx", f"{var_n * var_c:.10f}")
            eq_n_dest.shift(LEFT * 6.5 + RIGHT * eq_n_dest.width / 2 + UP * 3)
            eq_ni_dest.shift(LEFT * 6.5 + RIGHT * eq_ni_dest.width / 2 + UP * 2)
            eq_nc_dest.shift(LEFT * 6.5 + RIGHT * eq_nc_dest.width / 2 + UP)
            eq_ni_dest[2][0].set_color(ORANGE)
            eq_nc_dest[2][0].set_color(ORANGE)
            self.play(
                Transform(eq_n, eq_n_dest),
                Transform(eq_ni, eq_ni_dest),
                Transform(eq_nc, eq_nc_dest),
            )

            # approximate n=48
            var_n, var_i, var_c = approx(var_n, var_i, var_c)
            eq_n_dest = MathTex(f"n =", var_n)
            eq_ni_dest = MathTex("ni_n", "\\approx", f"{var_n * var_i:.10f}")
            eq_nc_dest = MathTex("nc_n", "\\approx", f"{var_n * var_c:.10f}")
            eq_n_dest.shift(LEFT * 6.5 + RIGHT * eq_n_dest.width / 2 + UP * 3)
            eq_ni_dest.shift(LEFT * 6.5 + RIGHT * eq_ni_dest.width / 2 + UP * 2)
            eq_nc_dest.shift(LEFT * 6.5 + RIGHT * eq_nc_dest.width / 2 + UP)
            eq_ni_dest[2][:3].set_color(ORANGE)
            eq_nc_dest[2][:3].set_color(ORANGE)
            self.play(
                Transform(eq_n, eq_n_dest),
                Transform(eq_ni, eq_ni_dest),
                Transform(eq_nc, eq_nc_dest),
            )

            # approximate n=96
            var_n, var_i, var_c = approx(var_n, var_i, var_c)
            eq_n_dest = MathTex(f"n =", var_n)
            eq_ni_dest = MathTex("ni_n", "\\approx", f"{var_n * var_i:.10f}")
            eq_nc_dest = MathTex("nc_n", "\\approx", f"{var_n * var_c:.10f}")
            eq_n_dest.shift(LEFT * 6.5 + RIGHT * eq_n_dest.width / 2 + UP * 3)
            eq_ni_dest.shift(LEFT * 6.5 + RIGHT * eq_ni_dest.width / 2 + UP * 2)
            eq_nc_dest.shift(LEFT * 6.5 + RIGHT * eq_nc_dest.width / 2 + UP)
            eq_ni_dest[2][:4].set_color(ORANGE)
            eq_nc_dest[2][:4].set_color(ORANGE)
            self.play(
                Transform(eq_n, eq_n_dest),
                Transform(eq_ni, eq_ni_dest),
                Transform(eq_nc, eq_nc_dest),
            )

            self.wait_until_bookmark("approx")
            # the relation with tau
            self.play(Transform(relation_to_tau, MathTex("ni_n", "< \\tau <", "nc_n")))

            # approximate ni_n and nc_n to two digits after decimal
            self.play(
                Transform(
                    relation_to_tau, MathTex("6.28\\dots", "< \\tau <", "6.28\\dots")
                )
            )

            # approximate tau to two digits after decimal
            tau_approx = MathTex("\\tau =", "6.28\\dots").next_to(relation_to_tau, DOWN)
            self.play(Write(tau_approx))

            # move tau_approx to origin
            self.play(FadeOut(relation_to_tau), tau_approx.animate.move_to(ORIGIN))

        # fade out everything
        self.play(
            FadeOut(i6, i2n, c6, c2n, eq_n, eq_ni, eq_nc, tau_approx), run_time=1.5
        )
'''

MORE_SAMPLE_EXAMPLES = '''

FEW MANIM EXAMPLES:

class EquationWithMovingFrameBox(Scene):
    def construct(self):
        text=MathTex(
            "\\frac{d}{dx}f(x)g(x)=","f(x)\\frac{d}{dx}g(x)","+",
            "g(x)\\frac{d}{dx}f(x)"
        )
        self.play(Write(text))
        framebox1 = SurroundingRectangle(text[1], buff = .1)
        framebox2 = SurroundingRectangle(text[3], buff = .1)
        self.play(
            Create(framebox1),
        )
        self.wait()
        self.play(
            ReplacementTransform(framebox1,framebox2),
        )
        self.wait()

class PointWithTrace(Scene):
    def construct(self):
        path = VMobject()
        dot = Dot()
        path.set_points_as_corners([dot.get_center(), dot.get_center()])
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)
        path.add_updater(update_path)
        self.add(path, dot)
        self.play(Rotating(dot, radians=PI, about_point=RIGHT, run_time=2))
        self.wait()
        self.play(dot.animate.shift(UP))
        self.play(dot.animate.shift(LEFT))
        self.wait()

class SinAndCosFunctionPlot(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-10, 10.3, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=10,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(-10, 10.01, 2),
                "numbers_with_elongated_ticks": np.arange(-10, 10.01, 2),
            },
            tips=False,
        )
        axes_labels = axes.get_axis_labels()
        sin_graph = axes.plot(lambda x: np.sin(x), color=BLUE)
        cos_graph = axes.plot(lambda x: np.cos(x), color=RED)

        sin_label = axes.get_graph_label(
            sin_graph, "\\sin(x)", x_val=-10, direction=UP / 2
        )
        cos_label = axes.get_graph_label(cos_graph, label="\\cos(x)")

        vert_line = axes.get_vertical_line(
            axes.i2gp(TAU, cos_graph), color=YELLOW, line_func=Line
        )
        line_label = axes.get_graph_label(
            cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
        )

        plot = VGroup(axes, sin_graph, cos_graph, vert_line)
        labels = VGroup(axes_labels, sin_label, cos_label, line_label)
        self.add(plot, labels)

class GraphAreaPlot(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 5],
            y_range=[0, 6],
            x_axis_config={"numbers_to_include": [2, 3]},
            tips=False,
        )

        labels = ax.get_axis_labels()

        curve_1 = ax.plot(lambda x: 4 * x - x ** 2, x_range=[0, 4], color=BLUE_C)
        curve_2 = ax.plot(
            lambda x: 0.8 * x ** 2 - 3 * x + 4,
            x_range=[0, 4],
            color=GREEN_B,
        )

        line_1 = ax.get_vertical_line(ax.input_to_graph_point(2, curve_1), color=YELLOW)
        line_2 = ax.get_vertical_line(ax.i2gp(3, curve_1), color=YELLOW)

        riemann_area = ax.get_riemann_rectangles(curve_1, x_range=[0.3, 0.6], dx=0.03, color=BLUE, fill_opacity=0.5)
        area = ax.get_area(curve_2, [2, 3], bounded_graph=curve_1, color=GREY, opacity=0.5)

        self.add(ax, labels, curve_1, curve_2, line_1, line_2, riemann_area, area)

class PolygonOnAxes(Scene):
    def get_rectangle_corners(self, bottom_left, top_right):
        return [
            (top_right[0], top_right[1]),
            (bottom_left[0], top_right[1]),
            (bottom_left[0], bottom_left[1]),
            (top_right[0], bottom_left[1]),
        ]

    def construct(self):
        ax = Axes(
            x_range=[0, 10],
            y_range=[0, 10],
            x_length=6,
            y_length=6,
            axis_config={"include_tip": False},
        )

        t = ValueTracker(5)
        k = 25

        graph = ax.plot(
            lambda x: k / x,
            color=YELLOW_D,
            x_range=[k / 10, 10.0, 0.01],
            use_smoothing=False,
        )

        def get_rectangle():
            polygon = Polygon(
                *[
                    ax.c2p(*i)
                    for i in self.get_rectangle_corners(
                        (0, 0), (t.get_value(), k / t.get_value())
                    )
                ]
            )
            polygon.stroke_width = 1
            polygon.set_fill(BLUE, opacity=0.5)
            polygon.set_stroke(YELLOW_B)
            return polygon

        polygon = always_redraw(get_rectangle)

        dot = Dot()
        dot.add_updater(lambda x: x.move_to(ax.c2p(t.get_value(), k / t.get_value())))
        dot.set_z_index(10)

        self.add(ax, graph, dot)
        self.play(Create(polygon))
        self.play(t.animate.set_value(10))
        self.play(t.animate.set_value(k / 10))
        self.play(t.animate.set_value(5))

class FollowingGraphCamera(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()

        # create the axes and the curve
        ax = Axes(x_range=[-1, 10], y_range=[-1, 10])
        graph = ax.plot(lambda x: np.sin(x), color=BLUE, x_range=[0, 3 * PI])

        # create dots based on the graph
        moving_dot = Dot(ax.i2gp(graph.t_min, graph), color=ORANGE)
        dot_1 = Dot(ax.i2gp(graph.t_min, graph))
        dot_2 = Dot(ax.i2gp(graph.t_max, graph))

        self.add(ax, graph, dot_1, dot_2, moving_dot)
        self.play(self.camera.frame.animate.scale(0.5).move_to(moving_dot))

        def update_curve(mob):
            mob.move_to(moving_dot.get_center())

        self.camera.frame.add_updater(update_curve)
        self.play(MoveAlongPath(moving_dot, graph, rate_func=linear))
        self.camera.frame.remove_updater(update_curve)

        self.play(Restore(self.camera.frame))

class ThreeDSurfacePlot(ThreeDScene):
    def construct(self):
        resolution_fa = 24
        self.set_camera_orientation(phi=75 * DEGREES, theta=-30 * DEGREES)

        def param_gauss(u, v):
            x = u
            y = v
            sigma, mu = 0.4, [0.0, 0.0]
            d = np.linalg.norm(np.array([x - mu[0], y - mu[1]]))
            z = np.exp(-(d ** 2 / (2.0 * sigma ** 2)))
            return np.array([x, y, z])

        gauss_plane = Surface(
            param_gauss,
            resolution=(resolution_fa, resolution_fa),
            v_range=[-2, +2],
            u_range=[-2, +2]
        )

        gauss_plane.scale(2, about_point=ORIGIN)
        gauss_plane.set_style(fill_opacity=1,stroke_color=GREEN)
        gauss_plane.set_fill_by_checkerboard(ORANGE, BLUE, opacity=0.5)
        axes = ThreeDAxes()
        self.add(axes,gauss_plane)

class OpeningManim(Scene):
    def construct(self):
        title = Tex(r"This is some \LaTeX")
        basel = MathTex(r"\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}")
        VGroup(title, basel).arrange(DOWN)
        self.play(
            Write(title),
            FadeIn(basel, shift=DOWN),
        )
        self.wait()

        transform_title = Tex("That was a transform")
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
            LaggedStart(*[FadeOut(obj, shift=DOWN) for obj in basel]),
        )
        self.wait()

        grid = NumberPlane()
        grid_title = Tex("This is a grid", font_size=72)
        grid_title.move_to(transform_title)

        self.add(grid, grid_title)  # Make sure title is on top of grid
        self.play(
            FadeOut(title),
            FadeIn(grid_title, shift=UP),
            Create(grid, run_time=3, lag_ratio=0.1),
        )
        self.wait()

        grid_transform_title = Tex(
            r"That was a non-linear function \\ applied to the grid"
        )
        grid_transform_title.move_to(grid_title, UL)
        grid.prepare_for_nonlinear_transform()
        self.play(
            grid.animate.apply_function(
                lambda p: p
                          + np.array(
                    [
                        np.sin(p[1]),
                        np.sin(p[0]),
                        0,
                    ]
                )
            ),
            run_time=3,
        )
        self.wait()
        self.play(Transform(grid_title, grid_transform_title))
        self.wait()
'''

MANIM_LIBRARY_EXAMPLES = '''

class MatrixExamples(Scene):
    def construct(self):
        m0 = Matrix([["\\pi", 0], [-1, 1]])
        m1 = IntegerMatrix([[1.5, 0.], [12, -1.3]],
            left_bracket="(",
            right_bracket=")")
        m2 = DecimalMatrix(
            [[3.456, 2.122], [33.2244, 12.33]],
            element_to_mobject_config={"num_decimal_places": 2},
            left_bracket="\\{",
            right_bracket="\\}")
        m3 = MobjectMatrix(
            [[Circle().scale(0.3), Square().scale(0.3)],
            [MathTex("\\pi").scale(2), Star().scale(0.3)]],
            left_bracket="\\langle",
            right_bracket="\\rangle")
        g = Group(m0, m1, m2, m3).arrange_in_grid(buff=2)
        self.add(g)

class CircleWithContent(VGroup):
    def __init__(self, content):
        super().__init__()
        self.circle = Circle()
        self.content = content
        self.add(self.circle, content)
        content.move_to(self.circle.get_center())

    def clear_content(self):
        self.remove(self.content)
        self.content = None

    @override_animate(clear_content)
    def _clear_content_animation(self, anim_args=None):
        if anim_args is None:
            anim_args = {}
        anim = Uncreate(self.content, **anim_args)
        self.clear_content()
        return anim

class AnimationOverrideExample(Scene):
    def construct(self):
        t = Text("hello!")
        my_mobject = CircleWithContent(t)
        self.play(Create(my_mobject))
        self.play(my_mobject.animate.clear_content())
        self.wait()

class TableExamples(Scene):
    def construct(self):
        t0 = Table(
            [["First", "Second"],
            ["Third","Fourth"]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")],
            top_left_entry=Text("TOP"))
        t0.add_highlighted_cell((2,2), color=GREEN)
        x_vals = np.linspace(-2,2,5)
        y_vals = np.exp(x_vals)
        t1 = DecimalTable(
            [x_vals, y_vals],
            row_labels=[MathTex("x"), MathTex("f(x)")],
            include_outer_lines=True)
        t1.add(t1.get_cell((2,2), color=RED))
        t2 = MathTable(
            [["+", 0, 5, 10],
            [0, 0, 5, 10],
            [2, 2, 7, 12],
            [4, 4, 9, 14]],
            include_outer_lines=True)
        t2.get_horizontal_lines()[:3].set_color(BLUE)
        t2.get_vertical_lines()[:3].set_color(BLUE)
        t2.get_horizontal_lines()[:3].set_z_index(1)
        cross = VGroup(
            Line(UP + LEFT, DOWN + RIGHT),
            Line(UP + RIGHT, DOWN + LEFT))
        a = Circle().set_color(RED).scale(0.5)
        b = cross.set_color(BLUE).scale(0.5)
        t3 = MobjectTable(
            [[a.copy(),b.copy(),a.copy()],
            [b.copy(),a.copy(),a.copy()],
            [a.copy(),b.copy(),b.copy()]])
        t3.add(Line(
            t3.get_corner(DL), t3.get_corner(UR)
        ).set_color(RED))
        vals = np.arange(1,21).reshape(5,4)
        t4 = IntegerTable(
            vals,
            include_outer_lines=True
        )
        g1 = Group(t0, t1).scale(0.5).arrange(buff=1).to_edge(UP, buff=1)
        g2 = Group(t2, t3, t4).scale(0.5).arrange(buff=1).to_edge(DOWN, buff=1)
        self.add(g1, g2)

class ValueTrackerExample(Scene):
    def construct(self):
        number_line = NumberLine()
        pointer = Vector(DOWN)
        label = MathTex("x").add_updater(lambda m: m.next_to(pointer, UP))

        tracker = ValueTracker(0)
        pointer.add_updater(
            lambda m: m.next_to(
                        number_line.n2p(tracker.get_value()),
                        UP
                    )
        )
        self.add(number_line, pointer,label)
        tracker += 1.5
        self.wait(1)
        tracker -= 4
        self.wait(0.5)
        self.play(tracker.animate.set_value(5))
        self.wait(0.5)
        self.play(tracker.animate.set_value(3))
        self.play(tracker.animate.increment_value(-2))
        self.wait(0.5)

class ComplexValueTrackerExample(Scene):
    def construct(self):
        tracker = ComplexValueTracker(-2+1j)
        dot = Dot().add_updater(
            lambda x: x.move_to(tracker.points)
        )

        self.add(NumberPlane(), dot)

        self.play(tracker.animate.set_value(3+2j))
        self.play(tracker.animate.set_value(tracker.get_value() * 1j))
        self.play(tracker.animate.set_value(tracker.get_value() - 2j))
        self.play(tracker.animate.set_value(tracker.get_value() / (-2 + 3j)))

class LagRatios(Scene):
    """An animation. Animations have a fixed time span."""
    def construct(self):
        ratios = [0, 0.1, 0.5, 1, 2]  # demonstrated lag_ratios

        # Create dot groups
        group = VGroup(*[Dot() for _ in range(4)]).arrange_submobjects()
        groups = VGroup(*[group.copy() for _ in ratios]).arrange_submobjects(buff=1)
        self.add(groups)

        # Label groups
        self.add(Text("lag_ratio = ", font_size=36).next_to(groups, UP, buff=1.5))
        for group, ratio in zip(groups, ratios):
            self.add(Text(str(ratio), font_size=36).next_to(group, UP))

        #Animate groups with different lag_ratios
        self.play(AnimationGroup(*[
            group.animate(lag_ratio=ratio, run_time=1.5).shift(DOWN * 2)
            for group, ratio in zip(groups, ratios)
        ]))

        # lag_ratio also works recursively on nested submobjects:
        self.play(groups.animate(run_time=1, lag_ratio=0.1).shift(UP * 2))

class AnimatedBoundaryExample(Scene):
    """Boundary of a VMobject with animated color change."""
    def construct(self):
        text = Text("So shiny!")
        boundary = AnimatedBoundary(text, colors=[RED, GREEN, BLUE],
                                    cycle_rate=3)
        self.add(text, boundary)
        self.wait(2)

class TracedPathExample(Scene):
    """Traces the path of a point returned by a function call."""
    def construct(self):
        circ = Circle(color=RED).shift(4*LEFT)
        dot = Dot(color=RED).move_to(circ.get_start())
        rolling_circle = VGroup(circ, dot)
        trace = TracedPath(circ.get_start)
        rolling_circle.add_updater(lambda m: m.rotate(-0.3))
        self.add(trace, rolling_circle)
        self.play(rolling_circle.animate.shift(8*RIGHT), run_time=4, rate_func=linear)

class LaggedStartExample(Scene):
    """Adjusts the timing of a series of Animation according to lag_ratio."""
    def construct(self):
        title = Text("lag_ratio = 0.25").to_edge(UP)

        dot1 = Dot(point=LEFT * 2 + UP, radius=0.16)
        dot2 = Dot(point=LEFT * 2, radius=0.16)
        dot3 = Dot(point=LEFT * 2 + DOWN, radius=0.16)
        line_25 = DashedLine(
            start=LEFT + UP * 2,
            end=LEFT + DOWN * 2,
            color=RED
        )
        label = Text("25%", font_size=24).next_to(line_25, UP)
        self.add(title, dot1, dot2, dot3, line_25, label)

        self.play(LaggedStart(
            dot1.animate.shift(RIGHT * 4),
            dot2.animate.shift(RIGHT * 4),
            dot3.animate.shift(RIGHT * 4),
            lag_ratio=0.25,
            run_time=4
        ))

class LaggedStartMapExample(Scene):
    """Plays a series of Animation while mapping a function to submobjects."""
    def construct(self):
        title = Tex("LaggedStartMap").to_edge(UP, buff=LARGE_BUFF)
        dots = VGroup(
            *[Dot(radius=0.16) for _ in range(35)]
            ).arrange_in_grid(rows=5, cols=7, buff=MED_LARGE_BUFF)
        self.add(dots, title)

        # Animate yellow ripple effect
        for mob in dots, title:
            self.play(LaggedStartMap(
                ApplyMethod, mob,
                lambda m : (m.set_color, YELLOW),
                lag_ratio = 0.1,
                rate_func = there_and_back,
                run_time = 2
            ))

class SuccessionExample(Scene):
    """Plays a series of animations in succession."""
    def construct(self):
        dot1 = Dot(point=LEFT * 2 + UP * 2, radius=0.16, color=BLUE)
        dot2 = Dot(point=LEFT * 2 + DOWN * 2, radius=0.16, color=MAROON)
        dot3 = Dot(point=RIGHT * 2 + DOWN * 2, radius=0.16, color=GREEN)
        dot4 = Dot(point=RIGHT * 2 + UP * 2, radius=0.16, color=YELLOW)
        self.add(dot1, dot2, dot3, dot4)

        self.play(Succession(
            dot1.animate.move_to(dot2),
            dot2.animate.move_to(dot3),
            dot3.animate.move_to(dot4),
            dot4.animate.move_to(dot1)
        ))

class Fading(Scene):
    """Fading in and out of view."""
    def construct(self):
        tex_in = Tex("Fade", "In").scale(3)
        tex_out = Tex("Fade", "Out").scale(3)
        self.play(FadeIn(tex_in, shift=DOWN, scale=0.66))
        self.play(ReplacementTransform(tex_in, tex_out))
        self.play(FadeOut(tex_out, shift=DOWN * 2, scale=1.5))

class Growing(Scene):
    """Animations that introduce mobjects to scene by growing them from points."""
    def construct(self):
        square = Square()
        circle = Circle()
        triangle = Triangle()
        arrow = Arrow(LEFT, RIGHT)
        star = Star()

        VGroup(square, circle, triangle).set_x(0).arrange(buff=1.5).set_y(2)
        VGroup(arrow, star).move_to(DOWN).set_x(0).arrange(buff=1.5).set_y(-2)

        self.play(GrowFromPoint(square, ORIGIN))
        self.play(GrowFromCenter(circle))
        self.play(GrowFromEdge(triangle, DOWN))
        self.play(GrowArrow(arrow))
        self.play(SpinInFromNothing(star))

class Indications(Scene):
    """Animations drawing attention to particular mobjects."""
    def construct(self):
        indications = [ApplyWave,Circumscribe,Flash,FocusOn,Indicate,ShowPassingFlash,Wiggle]
        names = [Tex(i.__name__).scale(3) for i in indications]

        self.add(names[0])
        for i in range(len(names)):
            if indications[i] is Flash:
                self.play(Flash(UP))
            elif indications[i] is ShowPassingFlash:
                self.play(ShowPassingFlash(Underline(names[i])))
            else:
                self.play(indications[i](names[i]))
            self.play(AnimationGroup(
                FadeOut(names[i], shift=UP*1.5),
                FadeIn(names[(i+1)%len(names)], shift=UP*1.5),
            ))

class TransformPathArc(Scene):
    """A Transform transforms a Mobject into a target Mobject."""
    def construct(self):
        def make_arc_path(start, end, arc_angle):
            points = []
            p_fn = path_along_arc(arc_angle)
            # alpha animates between 0.0 and 1.0, where 0.0
            # is the beginning of the animation and 1.0 is the end.
            for alpha in range(0, 11):
                points.append(p_fn(start, end, alpha / 10.0))
            path = VMobject(stroke_color=YELLOW)
            path.set_points_smoothly(points)
            return path

        left = Circle(stroke_color=BLUE_E, fill_opacity=1.0, radius=0.5).move_to(LEFT * 2)
        colors = [TEAL_A, TEAL_B, TEAL_C, TEAL_D, TEAL_E, GREEN_A]
        # Positive angles move counter-clockwise, negative angles move clockwise.
        examples = [-90, 0, 30, 90, 180, 270]
        anims = []
        for idx, angle in enumerate(examples):
            left_c = left.copy().shift((3 - idx) * UP)
            left_c.fill_color = colors[idx]
            right_c = left_c.copy().shift(4 * RIGHT)
            path_arc = make_arc_path(left_c.get_center(), right_c.get_center(),
                                     arc_angle=angle * DEGREES)
            desc = Text('%d°' % examples[idx]).next_to(left_c, LEFT)
            # Make the circles in front of the text in front of the arcs.
            self.add(
                path_arc.set_z_index(1),
                desc.set_z_index(2),
                left_c.set_z_index(3),
            )
            anims.append(Transform(left_c, right_c, path_arc=angle * DEGREES))

        self.play(*anims, run_time=2)
        self.wait()

class DifferentFadeTransforms(Scene):
    """Fades one mobject into another."""
    def construct(self):
        starts = [Rectangle(width=4, height=1) for _ in range(3)]
        VGroup(*starts).arrange(DOWN, buff=1).shift(3*LEFT)
        targets = [Circle(fill_opacity=1).scale(0.25) for _ in range(3)]
        VGroup(*targets).arrange(DOWN, buff=1).shift(3*RIGHT)

        self.play(*[FadeIn(s) for s in starts])
        self.play(
            FadeTransform(starts[0], targets[0], stretch=True),
            FadeTransform(starts[1], targets[1], stretch=False, dim_to_match=0),
            FadeTransform(starts[2], targets[2], stretch=False, dim_to_match=1)
        )

        self.play(*[FadeOut(mobj) for mobj in self.mobjects])

class MoveToTargetExample(Scene):
    """transforms a mobject to the mobject stored in its target attribute."""
    def construct(self):
        c = Circle()

        c.generate_target()
        c.target.set_fill(color=GREEN, opacity=0.5)
        c.target.shift(2*RIGHT + UP).scale(0.5)

        self.add(c)
        self.play(MoveToTarget(c))

class MatchingEquationParts(Scene):
    """A transformation trying to transform rendered LaTeX strings."""
    def construct(self):
        variables = VGroup(MathTex("a"), MathTex("b"), MathTex("c")).arrange_submobjects().shift(UP)

        eq1 = MathTex("{{x}}^2", "+", "{{y}}^2", "=", "{{z}}^2")
        eq2 = MathTex("{{a}}^2", "+", "{{b}}^2", "=", "{{c}}^2")
        eq3 = MathTex("{{a}}^2", "=", "{{c}}^2", "-", "{{b}}^2")

        self.add(eq1)
        self.wait(0.5)
        self.play(TransformMatchingTex(Group(eq1, variables), eq2))
        self.wait(0.5)
        self.play(TransformMatchingTex(eq2, eq3))
        self.wait(0.5)
'''