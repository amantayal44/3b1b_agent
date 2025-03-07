
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
        self.set_speech_service(GTTSService())
        # scene_style: Dark background. White text, arrows, and RNN block. Use a simple, clean font like Arial or Helvetica. Text size should be large enough to read comfortably (e.g., 48pt for titles, 24pt for body text). Maintain consistent spacing between elements.
        self.camera.background_color = BLACK

        # Part 1
        # animation_details: Show the text "Transformers in ML" at the top-center of the screen in a large, bold, white font, using a sans-serif font like Arial, size 48pt. After a brief pause, start moving the text smoothly towards the left side of the screen, taking about 2 seconds for the transition. Once the text has moved to the left, display a simple rectangular block representing an RNN in the center of the screen. Add a labeled arrow marked "Input" entering the RNN block from the left. Add another labeled arrow exiting the block to the right marked as "Output". Animate a small circle moving along the input arrow, through the RNN block, and out along the output arrow, taking about 2 seconds to complete the path, depicting sequential processing.
        # audio_text: Let's explore the fascinating world of Transformers in machine learning.
        with self.voiceover(text="Let's explore the fascinating world of Transformers in machine learning.") as tracker:
            # Implementation: Create title text
            title_text = Text("Transformers in ML", font="Arial", font_size=48, weight=BOLD).to_edge(UP)

            # Implementation: Display title text
            self.play(Write(title_text))
            self.wait(0.5)

            # Implementation: Move title text to the left
            self.play(title_text.animate.to_edge(LEFT), run_time=2)

            # Implementation: Create RNN block
            # Thinking: Center of the screen is ORIGIN, so we don't need to shift the RNN block
            rnn_block = Rectangle(width=2, height=1.5, color=WHITE)

            # Implementation: Create input arrow
            # Thinking: Left of the screen is LEFT * 7, so we start the arrow from there and end it at the left edge of the RNN block
            input_arrow = Arrow(LEFT * 7, rnn_block.get_left(), buff=0, color=WHITE).set_stroke(width=5)
            input_label = Text("Input", font="Arial", font_size=24).next_to(input_arrow, UP)

            # Implementation: Create output arrow
            # Thinking: Right of the screen is RIGHT * 7, so we start the arrow from the right edge of the RNN block and end it there
            output_arrow = Arrow(rnn_block.get_right(), RIGHT * 7, buff=0, color=WHITE).set_stroke(width=5)
            output_label = Text("Output", font="Arial", font_size=24).next_to(output_arrow, UP)

            # Implementation: Create a circle for animation
            circle = Circle(radius=0.1, color=WHITE, fill_opacity=1)
            circle.move_to(input_arrow.get_start())

            # Implementation: Display RNN block, arrows, and labels
            self.play(
                Create(rnn_block),
                Create(input_arrow),
                Write(input_label),
                Create(output_arrow),
                Write(output_label),
            )

            # Implementation: Animate circle through the RNN block
            self.play(
                MoveAlongPath(circle, input_arrow),
                MoveAlongPath(circle, rnn_block),
                MoveAlongPath(circle, output_arrow),
                run_time=2,
            )
            self.wait(0.5)

        # Cleaning: Keep all objects for the next part

        # Part 2
        # animation_details: Keep the RNN block from the previous part in the center. Add a label "Recurrent Neural Network" below the RNN block using white, Arial font, size 24pt. Ensure the label is horizontally centered with the RNN block and there's enough space between them so they don't overlap.
        # audio_text: Before Transformers, models like Recurrent Neural Networks or RNNs processed data sequentially, one element at a time.
        with self.voiceover(text="Before Transformers, models like Recurrent Neural Networks or RNNs processed data sequentially, one element at a time.") as tracker:
            # Implementation: Create RNN label
            # Thinking: RNN block is at ORIGIN, so we place the label below it with a buffer of 0.5
            rnn_label = Text("Recurrent Neural Network", font="Arial", font_size=24).next_to(rnn_block, DOWN, buff=0.5)

            # Implementation: Display RNN label
            self.play(Write(rnn_label))
            self.wait(tracker.duration - estimated_audio_duration_s + 1)

        # Cleaning: Clear all objects
        self.clear()

    def play_scene_2(self):
        self.set_speech_service(GTTSService())
        # scene_style: Maintain the same dark background, white text and arrows. Use a color gradient from dark red to light pink for the vanishing gradient visualization. Keep the font and text sizes consistent with the previous scene.
        self.camera.background_color = BLACK

        # Part 1
        # animation_details: Display the sentence "This is a long sentence" at the top-left of the screen, with each word spaced apart by about 20 pixels, using white Arial font, size 24pt. Move the entire sentence towards the RNN block, which is positioned in the center of the screen. Animate each word entering the RNN block sequentially, one after the other, with a 0.5-second delay between each word. As each word is processed, show a corresponding output on the right side of the RNN block, represented by small grey rectangles. For each new word processed, reduce the size of the output rectangles from previously processed words by 10% and decrease their opacity by 20%, making them less prominent.
        # audio_text: This sequential nature made RNNs slow, especially for long sequences.
        with self.voiceover(text="This sequential nature made RNNs slow, especially for long sequences.") as tracker:
            # Implementation: Create sentence
            # Thinking: Top-left of the screen is UP * 3.5 + LEFT * 6, so we start the sentence there
            sentence = Text("This is a long sentence", font="Arial", font_size=24, t2c={"This": WHITE, "is": WHITE, "a": WHITE, "long": WHITE, "sentence": WHITE}).arrange(RIGHT, buff=0.25).to_edge(UP).to_edge(LEFT)

            # Implementation: Create RNN block
            # Thinking: Center of the screen is ORIGIN, so we don't need to shift the RNN block
            rnn_block = Rectangle(width=2, height=1.5, color=WHITE)

            # Implementation: Display sentence and RNN block
            self.play(Write(sentence), Create(rnn_block))

            # Implementation: Animate each word entering the RNN block
            output_rects = []
            for i, word in enumerate(sentence):
                # Implementation: Move word to RNN block
                self.play(
                    word.animate.move_to(rnn_block.get_center()),
                    run_time=0.5,
                )

                # Implementation: Create output rectangle
                output_rect = Rectangle(width=0.5, height=0.3, color=GRAY, fill_opacity=1).move_to(rnn_block.get_right()).shift(RIGHT * (i + 1) * 0.6)
                self.play(Create(output_rect))

                # Implementation: Add output rectangle to list
                output_rects.append(output_rect)

                # Implementation: Reduce size and opacity of previous output rectangles
                for j, rect in enumerate(output_rects[:-1]):
                    self.play(
                        rect.animate.scale(0.9).set_opacity(rect.opacity - 0.2),
                        run_time=0.1,
                    )

                # Implementation: Remove word from screen
                self.remove(word)

            self.wait(0.5)

        # Cleaning: Keep sentence and RNN block for the next part

        # Part 2
        # animation_details: Move the sentence and RNN block diagram towards the right side of the screen over a duration of 1 second, creating space on the left. Display the text "Vanishing Gradient Problem" at the top-center in large, bold, white Arial font, size 48pt. Below this text, draw a horizontal chain of five connected rectangular blocks, each 50 pixels wide and 30 pixels high, representing the steps in backpropagation. The blocks should be spaced 20 pixels apart. Apply a color gradient to these blocks, starting with dark red (#8B0000) for the first block on the right and transitioning to light pink (#FFB6C1) for the last block on the left, illustrating the diminishing strength of the gradient signal during backpropagation. Ensure the transition is smooth, using linear interpolation between colors.
        # audio_text: They also suffered from issues like vanishing or exploding gradients, making it hard to learn long-range dependencies in the data.
        with self.voiceover(text="They also suffered from issues like vanishing or exploding gradients, making it hard to learn long-range dependencies in the data.") as tracker:
            # Implementation: Move sentence and RNN block to the right
            self.play(
                sentence.animate.to_edge(RIGHT),
                rnn_block.animate.to_edge(RIGHT),
                run_time=1,
            )

            # Implementation: Create title text
            # Thinking: Top-center of the screen is UP * 3.5, so we place the title there
            title_text = Text("Vanishing Gradient Problem", font="Arial", font_size=48, weight=BOLD).to_edge(UP)

            # Implementation: Display title text
            self.play(Write(title_text))

            # Implementation: Create chain of blocks
            # Thinking: We want the chain to be centered horizontally, so we start from the center and place the blocks to the left and right
            blocks = []
            colors = color_gradient([RED, PINK], 5)
            for i in range(5):
                block = Rectangle(width=1, height=0.6, color=colors[i], fill_opacity=1)
                if i == 0:
                    block.move_to(LEFT * 2)
                else:
                    block.next_to(blocks[i - 1], RIGHT, buff=0.4)
                blocks.append(block)

            # Implementation: Display blocks
            self.play(*[Create(block) for block in blocks])
            self.wait(tracker.duration - estimated_audio_duration_s + 1)

        # Cleaning: Clear all objects
        self.clear()

    def play_scene_3(self):
        self.set_speech_service(GTTSService())
        # scene_style: Continue with the dark background. Use white text for general text and bright, distinct lines for attention connections. Maintain the same font style and size for consistency.
        self.camera.background_color = BLACK

        # Part 1
        # animation_details: Clear the screen of all previous elements. Display the text "Attention" prominently at the top-center of the screen in a large, bold, white Arial font, size 48pt. Below this, add a brief explanation: "Attention allows a model to focus on relevant parts of the input sequence." in white Arial font, size 24pt. The explanation text should be horizontally centered and placed about 30 pixels below the "Attention" text.
        # audio_text: The game-changer was the concept of 'Attention'.
        with self.voiceover(text="The game-changer was the concept of 'Attention'.") as tracker:
            # Implementation: Create title text
            # Thinking: Top-center of the screen is UP * 3.5, so we place the title there
            title_text = Text("Attention", font="Arial", font_size=48, weight=BOLD).to_edge(UP)

            # Implementation: Create explanation text
            # Thinking: We want the explanation to be centered horizontally and placed 30 pixels (0.3 in Manim units) below the title text
            explanation_text = Text("Attention allows a model to focus on relevant parts of the input sequence.", font="Arial", font_size=24).next_to(title_text, DOWN, buff=0.3)

            # Implementation: Display title and explanation text
            self.play(Write(title_text), Write(explanation_text))
            self.wait(tracker.duration - estimated_audio_duration_s + 1)

        # Cleaning: Clear all objects

        # Part 2
        # animation_details: Move the "Attention" text to the top-left corner of the screen, taking 1 second for the transition. Reintroduce the sentence "This is a long sentence" near the top of the screen, slightly below and to the right of the "Attention" text, with each word spaced 20 pixels apart. Draw a new rectangular block labeled "Attention" below the sentence, centered horizontally. Connect all words of the sentence to this block simultaneously with lines, indicating parallel processing. For each word in the sentence, draw lines connecting it to other words, representing attention weights. Use brighter lines (#FFFFE0) for stronger connections and dimmer lines (white with 50% opacity) for weaker connections. For instance, when focusing on the word "sentence", use a bright line to connect it to "long", indicating a strong relationship. The lines should be animated to appear in sync with the audio explanation.
        # audio_text: Instead of processing word by word, attention allows the model to look at all words at once and determine their relationships, avoiding the bottlenecks of RNNs.
        with self.voiceover(text="Instead of processing word by word, attention allows the model to look at all words at once and determine their relationships, avoiding the bottlenecks of RNNs.") as tracker:
            # Implementation: Move title text to the top-left corner
            self.play(
                title_text.animate.to_edge(LEFT).to_edge(UP),
                run_time=1,
            )
            self.remove(explanation_text)

            # Implementation: Create sentence
            # Thinking: We want the sentence to be near the top of the screen, slightly below and to the right of the "Attention" text
            sentence = Text("This is a long sentence", font="Arial", font_size=24).arrange(RIGHT, buff=0.25).next_to(title_text, DOWN).shift(RIGHT * 2)

            # Implementation: Create attention block
            # Thinking: We want the attention block to be below the sentence, centered horizontally
            attention_block = Rectangle(width=3, height=1.5, color=WHITE).next_to(sentence, DOWN, buff=1)
            attention_label = Text("Attention", font="Arial", font_size=24).move_to(attention_block)

            # Implementation: Display sentence and attention block
            self.play(Write(sentence), Create(attention_block), Write(attention_label))

            # Implementation: Connect all words to the attention block
            lines_to_block = []
            for word in sentence:
                line = Line(word.get_bottom(), attention_block.get_top(), color=WHITE)
                lines_to_block.append(line)
            self.play(*[Create(line) for line in lines_to_block])

            # Implementation: Connect words to each other
            lines_between_words = []
            for i, word1 in enumerate(sentence):
                for j, word2 in enumerate(sentence):
                    if i != j:
                        # Implementation: Use brighter lines for stronger connections (e.g., "sentence" and "long")
                        if (word1.text == "sentence" and word2.text == "long") or \
                           (word1.text == "long" and word2.text == "sentence"):
                            line = Line(word1.get_center(), word2.get_center(), color="#FFFFE0")
                        else:
                            line = Line(word1.get_center(), word2.get_center(), color=WHITE, opacity=0.5)
                        lines_between_words.append(line)

            # Implementation: Animate lines between words
            self.play(*[Create(line) for line in lines_between_words])
            self.wait(tracker.duration - estimated_audio_duration_s + 1)

        # Cleaning: Clear all objects
        self.clear()

    def play_scene_4(self):
        self.set_speech_service(GTTSService())
        # scene_style: Dark background. Use distinct colors for the "Encoder" and "Decoder" blocks. Within the "Encoder", use different colors for the "Multi-Head Attention" and "Feed-Forward Network" layers. Use white text for labels and descriptions. Maintain a consistent font style and size.
        self.camera.background_color = BLACK

        # Part 1
        # animation_details: Draw two large rectangular blocks side-by-side in the center of the screen, each about 200 pixels wide and 100 pixels high, spaced 40 pixels apart. Label the left block "Encoder" and the right block "Decoder" in white Arial font, size 36pt, centered within each block. Add a brief text description below each block in white Arial font, size 24pt: "Encoder: Processes the input sequence." and "Decoder: Generates the output sequence." These descriptions should be horizontally centered with their respective blocks and placed about 20 pixels below.
        # audio_text: A Transformer has two main parts: an Encoder and a Decoder.
        with self.voiceover(text="A Transformer has two main parts: an Encoder and a Decoder.") as tracker:
            # Implementation: Create Encoder and Decoder blocks
            # Thinking: We want the blocks to be side-by-side in the center of the screen, each about 200 pixels wide (2 in Manim units) and 100 pixels high (1 in Manim units), spaced 40 pixels (0.4 in Manim units) apart.
            encoder_block = Rectangle(width=2, height=1, color=WHITE)
            decoder_block = Rectangle(width=2, height=1, color=WHITE)
            encoder_block.to_edge(LEFT, buff=2)
            decoder_block.next_to(encoder_block, RIGHT, buff=1)

            # Implementation: Label the blocks
            encoder_label = Text("Encoder", font="Arial", font_size=36).move_to(encoder_block)
            decoder_label = Text("Decoder", font="Arial", font_size=36).move_to(decoder_block)

            # Implementation: Add descriptions below the blocks
            # Thinking: We want the descriptions to be horizontally centered with their respective blocks and placed about 20 pixels (0.2 in Manim units) below.
            encoder_description = Text("Encoder: Processes the input sequence.", font="Arial", font_size=24).next_to(encoder_block, DOWN, buff=0.2)
            decoder_description = Text("Decoder: Generates the output sequence.", font="Arial", font_size=24).next_to(decoder_block, DOWN, buff=0.2)

            # Implementation: Display blocks, labels, and descriptions
            self.play(
                Create(encoder_block),
                Create(decoder_block),
                Write(encoder_label),
                Write(decoder_label),
                Write(encoder_description),
                Write(decoder_description),
            )
            self.wait(tracker.duration - estimated_audio_duration_s + 1)

        # Cleaning: Keep all objects for the next part

        # Part 2
        # animation_details: Emphasize the "Encoder" block by increasing its size by 10% and changing its border color to a brighter white. Divide the "Encoder" block into two distinct horizontal layers. Label the top layer "Multi-Head Attention" and the bottom layer "Feed-Forward Network" in white Arial font, size 24pt, centered within each layer. Use different background colors to distinguish the layers: light grey (#D3D3D3) for "Multi-Head Attention" and slightly darker grey (#A9A9A9) for "Feed-Forward Network". Add a brief text description below each layer, outside the block: "Multi-Head Attention: Computes attention scores between words." and "Feed-Forward Network: Processes each word's representation." in white Arial font, size 20pt. These descriptions should be horizontally centered with their respective layers.
        # audio_text: The Encoder processes the input sequence. Each Encoder layer has two sub-layers: Multi-Head Self-Attention and a Feed-Forward Network.
        with self.voiceover(text="The Encoder processes the input sequence. Each Encoder layer has two sub-layers: Multi-Head Self-Attention and a Feed-Forward Network.") as tracker:
            # Implementation: Emphasize the Encoder block
            self.play(
                encoder_block.animate.scale(1.1).set_stroke(color=WHITE, width=6),
            )

            # Implementation: Divide the Encoder block into two layers
            layer_divider = Line(encoder_block.get_left(), encoder_block.get_right(), color=WHITE)
            layer_divider.move_to(encoder_block.get_center())

            # Implementation: Label the layers
            multi_head_attention_label = Text("Multi-Head Attention", font="Arial", font_size=24, color=BLACK).move_to(encoder_block.get_top()).shift(DOWN * 0.25)
            feed_forward_label = Text("Feed-Forward Network", font="Arial", font_size=24, color=BLACK).move_to(encoder_block.get_bottom()).shift(UP * 0.25)

            # Implementation: Set background colors for the layers
            multi_head_attention_layer = SurroundingRectangle(multi_head_attention_label, color=LIGHT_GRAY, fill_opacity=1, buff=0.1)
            feed_forward_layer = SurroundingRectangle(feed_forward_label, color=DARK_GRAY, fill_opacity=1, buff=0.1)

            # Implementation: Add descriptions below each layer
            # Thinking: We want the descriptions to be horizontally centered with their respective layers and placed outside the block.
            multi_head_attention_description = Text("Multi-Head Attention: Computes attention scores between words.", font="Arial", font_size=20).next_to(encoder_block, DOWN, buff=0.5).align_to(multi_head_attention_label, LEFT)
            feed_forward_description = Text("Feed-Forward Network: Processes each word's representation.", font="Arial", font_size=20).next_to(multi_head_attention_description, DOWN, buff=0.2).align_to(feed_forward_label, LEFT)

            # Implementation: Display layers, labels, and descriptions
            self.play(
                Create(layer_divider),
                Create(multi_head_attention_layer),
                Write(multi_head_attention_label),
                Create(feed_forward_layer),
                Write(feed_forward_label),
                Write(multi_head_attention_description),
                Write(feed_forward_description),
            )
            self.wait(tracker.duration - estimated_audio_duration_s + 1)

        # Cleaning: Clear all objects
        self.clear()

    def play_scene_5(self):
        self.set_speech_service(GTTSService())
        # scene_style: Maintain the dark background. Use distinct colors for Q, K, and V vectors (e.g., red, blue, green). Use white text for labels and explanations. Use a clear and consistent font. For matrix multiplications, use a standard notation with clear brackets and labels.
        self.camera.background_color = BLACK

        # Part 1
        # animation_details: Display the sentence "I love learning" at the top-left of the screen, using white Arial font, size 24pt, with words spaced 20 pixels apart. Below each word, draw a vertical array of numbers enclosed in brackets to represent its word embedding. For example:
        # [0.2, 0.8, -0.1] for "I",
        # [0.5, -0.3, 0.7] for "love",
        # [-0.2, 0.6, 0.4] for "learning". Each number should be in white Arial font, size 18pt. Label this group of vectors as "Word Embeddings" on the right, using white Arial font, size 24pt, positioned vertically centered with the embeddings.
        # audio_text: In Multi-Head Attention, words are first converted into embeddings.
        with self.voiceover(text="In Multi-Head Attention, words are first converted into embeddings.") as tracker:
            # Implementation: Create sentence
            # Thinking: Top-left of the screen is UP * 3.5 + LEFT * 6, so we start the sentence there
            sentence = Text("I love learning", font="Arial", font_size=24).arrange(RIGHT, buff=0.25).to_edge(UP).to_edge(LEFT)

            # Implementation: Create word embeddings
            # Thinking: We want the embeddings to be below each word, so we use the get_bottom() method of each word and shift it DOWN
            embeddings = []
            embedding_values = [[0.2, 0.8, -0.1], [0.5, -0.3, 0.7], [-0.2, 0.6, 0.4]]
            for i, word in enumerate(sentence):
                embedding = MathTex(str(embedding_values[i]), font_size=24).next_to(word, DOWN)
                embeddings.append(embedding)

            # Implementation: Label the group of vectors as "Word Embeddings"
            # Thinking: We want the label to be on the right of the embeddings, vertically centered
            word_embeddings_label = Text("Word Embeddings", font="Arial", font_size=24).next_to(embeddings, RIGHT, buff=1).align_to(embeddings[1], UP)

            # Implementation: Display sentence, embeddings, and label
            self.play(Write(sentence), *[Write(embedding) for embedding in embeddings], Write(word_embeddings_label))
            self.wait(tracker.duration - estimated_audio_duration_s + 1)

        # Cleaning: Keep all objects for the next part

        # Part 2
        # animation_details: For each word embedding, draw three arrows pointing to three new sets of vectors. Each arrow should be 50 pixels long. Label these new vectors as "Query (Q)", "Key (K)", and "Value (V)" using white Arial font, size 20pt, positioned above each vector. Use different colors for these vectors and their labels: red (#FF0000) for Q, blue (#0000FF) for K, and green (#00FF00) for V. Represent the linear transformations as matrix multiplications. Show a matrix labeled Wq (in red) multiplying the word embedding to get Q, Wk (in blue) to get K, and Wv (in green) to get V. Each matrix should be represented by a 2x3 grid of numbers in their respective colors, using Arial font, size 18pt. These labels should be clearly placed beside each transformation arrow.
        # audio_text: Then, for each word, we create Query, Key, and Value vectors using different learned weight matrices.
        with self.voiceover(text="Then, for each word, we create Query, Key, and Value vectors using different learned weight matrices.") as tracker:
            # Implementation: Create Q, K, and V vectors and labels
            # Thinking: We want the vectors to be to the right of the embeddings, with arrows pointing from the embeddings to the vectors
            qkv_vectors = []
            qkv_labels = []
            qkv_matrices = []
            arrows = []
            colors = [RED, BLUE, GREEN]
            labels = ["Query (Q)", "Key (K)", "Value (V)"]
            matrix_values = [[[0.1, 0.2, -0.3], [-0.2, 0.4, 0.1]], [[0.3, -0.1, 0.2], [0.1, 0.4, -0.2]], [[-0.1, 0.3, 0.2], [0.2, -0.1, 0.4]]]

            for i, embedding in enumerate(embeddings):
                for j in range(3):
                    vector = MathTex(str([round(val, 1) for val in np.random.rand(3)]), font_size=24, color=colors[j]).next_to(embedding, RIGHT, buff=1.5).shift(UP * (j - 1))
                    label = Text(labels[j], font="Arial", font_size=20, color=colors[j]).next_to(vector, UP)
                    arrow = Arrow(embedding.get_right(), vector.get_left(), color=WHITE, buff=0.1)
                    matrix = MathTex(str(matrix_values[j]), font_size=24, color=colors[j]).next_to(arrow, UP, buff=0)

                    qkv_vectors.append(vector)
                    qkv_labels.append(label)
                    arrows.append(arrow)
                    qkv_matrices.append(matrix)

            # Implementation: Display arrows, vectors, labels, and matrices
            self.play(
                *[Create(arrow) for arrow in arrows],
                *[Write(vector) for vector in qkv_vectors],
                *[Write(label) for label in qkv_labels],
                *[Write(matrix) for matrix in qkv_matrices],
            )
            self.wait(tracker.duration - estimated_audio_duration_s + 1)

        # Cleaning: Keep all objects for the next part

        # Part 3
        # animation_details: Illustrate the Scaled Dot-Product Attention process step-by-step. First, show the matrix multiplication of Q (red) and the transpose of K (blue) for a given word, resulting in a 3x3 matrix of attention scores. Use red and blue Arial font, size 18pt for the numbers in the matrices. Next, show this matrix being divided by the square root of the dimension of K (e.g., \u221a3), with the result displayed below. Then, apply the softmax function to this result, normalizing the scores, and display the final 3x3 matrix with normalized values. Finally, show the multiplication of these normalized scores with the V (green) vectors to get the weighted Value vectors. Use clear labels and arrows, each 50 pixels long, to indicate each operation and the flow of calculations. All text should be in white Arial font, size 20pt.
        # audio_text: We calculate the attention scores using scaled dot product of Q and K, normalize them using softmax, and then weight the Value vectors by these scores.
        with self.voiceover(text="We calculate the attention scores using scaled dot product of Q and K, normalize them using softmax, and then weight the Value vectors by these scores.") as tracker:
            # Implementation: Select Q, K, and V vectors for the first word
            q_vector = qkv_vectors[0]
            k_vector = qkv_vectors[1]
            v_vector = qkv_vectors[2]

            # Implementation: Calculate attention scores (Q * K^T)
            attention_scores_matrix = MathTex(r"\begin{bmatrix} 0.8 & 0.2 & 0.5 \\ 0.3 & 0.7 & 0.1 \\ 0.6 & 0.4 & 0.9 \end{bmatrix}", font_size=24).next_to(q_vector, RIGHT, buff=2)
            attention_scores_label = Text("Attention Scores", font="Arial", font_size=20).next_to(attention_scores_matrix, UP)
            q_k_arrow = Arrow(q_vector.get_right(), attention_scores_matrix.get_left(), color=WHITE, buff=0.1)

            # Implementation: Display attention scores matrix and label
            self.play(Create(q_k_arrow), Write(attention_scores_matrix), Write(attention_scores_label))

            # Implementation: Scale attention scores (divide by sqrt(dimension of K))
            scaled_attention_scores_matrix = MathTex(r"\begin{bmatrix} 0.46 & 0.12 & 0.29 \\ 0.17 & 0.40 & 0.06 \\ 0.35 & 0.23 & 0.52 \end{bmatrix}", font_size=24).next_to(attention_scores_matrix, DOWN, buff=0.5)
            scaled_attention_scores_label = Text("Scaled Scores", font="Arial", font_size=20).next_to(scaled_attention_scores_matrix, UP)
            scale_arrow = Arrow(attention_scores_matrix.get_bottom(), scaled_attention_scores_matrix.get_top(), color=WHITE, buff=0.1)

            # Implementation: Display scaled attention scores matrix and label
            self.play(Create(scale_arrow), Write(scaled_attention_scores_matrix), Write(scaled_attention_scores_label))

            # Implementation: Apply softmax to scaled attention scores
            softmax_matrix = MathTex(r"\begin{bmatrix} 0.51 & 0.15 & 0.34 \\ 0.18 & 0.74 & 0.08 \\ 0.26 & 0.17 & 0.57 \end{bmatrix}", font_size=24).next_to(scaled_attention_scores_matrix, DOWN, buff=0.5)
            softmax_label = Text("Softmax", font="Arial", font_size=20).next_to(softmax_matrix, UP)
            softmax_arrow = Arrow(scaled_attention_scores_matrix.get_bottom(), softmax_matrix.get_top(), color=WHITE, buff=0.1)

            # Implementation: Display softmax matrix and label
            self.play(Create(softmax_arrow), Write(softmax_matrix), Write(softmax_label))

            # Implementation: Multiply softmax matrix by V vectors
            weighted_v_vectors = []
            weighted_v_labels = []
            v_multiply_arrows = []
            result_vectors = []
            result_labels = []
            result_arrows = []

            for i in range(3):
                weighted_v_vector = MathTex(str([round(val, 1) for val in np.
