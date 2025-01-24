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
        # Implementation: Setting scene style as mentioned in prompt
        self.camera.background_color = BLUE_E

        # Implementation: Part 1
        with self.voiceover(text="Before transformers, we had Recurrent Neural Networks, or RNNs. They process sequences one token at a time, which is quite slow. They also struggle with long-range dependencies and gradients.") as tracker:
            # Implementation: Display the text "RNN Limitations"
            # Thinking: Position text at top center and scale down to fit in frame
            rnn_limitations_text = Text("RNN Limitations", color=WHITE).scale(0.8).to_edge(UP)
            self.play(Write(rnn_limitations_text))

            # Implementation: Position a simple RNN diagram below it
            # Thinking: Center the diagram and leave space for text below
            input_node = Text("Input", color=WHITE).scale(0.7).shift(LEFT * 4)
            hidden_node = Text("Hidden", color=WHITE).scale(0.7)
            output_node = Text("Output", color=WHITE).scale(0.7).shift(RIGHT * 4)

            # Implementation: Show input sequence and connect with red arrows
            input_sequence = Text("A B C D", color=WHITE).scale(0.6).next_to(input_node, LEFT, buff=1)
            arrows = [
                Arrow(input_sequence.get_right(), input_node.get_left(), color=RED),
                Arrow(input_node.get_right(), hidden_node.get_left(), color=RED),
                Arrow(hidden_node.get_right(), output_node.get_left(), color=RED),
            ]
            self.play(
                Write(input_node),
                Write(hidden_node),
                Write(output_node),
                Write(input_sequence),
            )
            for arrow in arrows:
                self.play(Create(arrow))

            # Implementation: Animate processing of each token
            for char in input_sequence.text:
                self.play(Indicate(input_sequence.get_part_by_text(char), color=YELLOW))

            # Implementation: Place a grey clock icon
            # Thinking: Position clock icon on the right, below "RNN Limitations"
            clock_icon = Text("⏰", color=GREY).scale(0.5).next_to(rnn_limitations_text, DOWN, aligned_edge=RIGHT)
            self.play(Create(clock_icon))

            # Implementation: Display limitations text below the clock icon
            # Thinking: Position text below clock icon, each on a new line
            limitations_text_1 = Text("Vanishing/Exploding Gradients", color=WHITE).scale(0.6).next_to(clock_icon, DOWN)
            limitations_text_2 = Text("Difficulty with Long-Range Dependencies", color=WHITE).scale(0.6).next_to(limitations_text_1, DOWN)
            self.play(Write(limitations_text_1), Write(limitations_text_2))

        # Cleaning: No objects should be cleared

        # Implementation: Part 2
        with self.voiceover(text="Transformers, introduced in the paper \"Attention is All You Need\", solve these issues with parallel processing and a powerful attention mechanism.") as tracker:
            # Implementation: Fade out RNN diagram and text
            self.play(
                FadeOut(input_node),
                FadeOut(hidden_node),
                FadeOut(output_node),
                FadeOut(input_sequence),
                FadeOut(clock_icon),
                FadeOut(limitations_text_1),
                FadeOut(limitations_text_2),
                *[FadeOut(arrow) for arrow in arrows],
            )

            # Implementation: Display "Introducing Transformers" text
            # Thinking: Position text at top center and scale down to fit in frame
            transformers_text = Text("Introducing Transformers", color=WHITE).scale(0.8).to_edge(UP)
            self.play(
                ReplacementTransform(rnn_limitations_text, transformers_text)
            )

            # Implementation: Show a basic Transformer diagram
            # Thinking: Center the diagram and leave space for text
            input_nodes = VGroup(*[Text("Input", color=WHITE).scale(0.6) for _ in range(3)]).arrange(DOWN, buff=0.5).shift(LEFT * 4)
            output_nodes = VGroup(*[Text("Output", color=WHITE).scale(0.6) for _ in range(3)]).arrange(DOWN, buff=0.5).shift(RIGHT * 4)
            attention_mechanism = Text("Attention Mechanism", color=WHITE).scale(0.7)

            # Implementation: Use green parallel arrows
            parallel_arrows = [
                Arrow(input_nodes.get_right(), attention_mechanism.get_left(), color=GREEN),
                Arrow(attention_mechanism.get_right(), output_nodes.get_left(), color=GREEN),
            ]
            self.play(
                Write(input_nodes),
                Write(output_nodes),
                Write(attention_mechanism),
            )
            for arrow in parallel_arrows:
                self.play(Create(arrow))

        # Cleaning: Clear all objects
        self.clear()

    def play_scene_2(self):
        # Implementation: Setting scene style as mentioned in prompt
        self.camera.background_color = BLUE_E

        # Implementation: Part 1
        with self.voiceover(text="First, we convert words into numerical representations called embeddings.") as tracker:
            # Implementation: Display "Input: The quick brown fox" text
            # Thinking: Position text at top left and scale down to fit in frame
            input_text = Text("Input: The quick brown fox", color=WHITE).scale(0.7).to_edge(UP).to_edge(LEFT)
            self.play(Write(input_text))

            # Implementation: Show word transformations into vectors
            # Thinking: Position vectors below each word and use blue color
            words = ["The", "quick", "brown", "fox"]
            vectors = [
                [0.1, 0.2, 0.3],
                [0.4, 0.5, 0.6],
                [0.2, 0.3, 0.5],
                [0.6, 0.1, 0.4],
            ]
            word_vector_group = VGroup()
            for i, word in enumerate(words):
                word_obj = Text(word, color=WHITE).scale(0.6).next_to(input_text, DOWN, aligned_edge=LEFT).shift(RIGHT * i * 2)
                vector_obj = Text(str(vectors[i]), color=BLUE).scale(0.6).next_to(word_obj, DOWN)
                word_vector_group.add(word_obj, vector_obj)
            self.play(Write(word_vector_group))

            # Implementation: Display "Embeddings" text
            # Thinking: Position text at the middle and scale down to fit in frame
            embeddings_text = Text("Embeddings", color=WHITE).scale(0.8).next_to(word_vector_group, DOWN, buff=1)
            self.play(Write(embeddings_text))

        # Cleaning: No objects should be cleared

        # Implementation: Part 2
        with self.voiceover(text="Since transformers don't process sequentially, we add positional encoding to give the model information about the order of words. This is done using sine and cosine functions, as shown in these equations.") as tracker:
            # Implementation: Fade out previous elements
            self.play(
                FadeOut(input_text),
                FadeOut(word_vector_group),
            )

            # Implementation: Display "Positional Encoding" text
            # Thinking: Position text at top center and scale down to fit in frame
            positional_encoding_text = Text("Positional Encoding", color=WHITE).scale(0.8).to_edge(UP)
            self.play(
                ReplacementTransform(embeddings_text, positional_encoding_text)
            )

            # Implementation: Write positional encoding equations
            # Thinking: Position equations below the text and use yellow color
            pe_equation_1 = MathTex("PE(pos, 2i) = sin(pos / 10000^{(2i/d_{model})})", color=YELLOW).scale(0.6).next_to(positional_encoding_text, DOWN, buff=0.5)
            pe_equation_2 = MathTex("PE(pos, 2i+1) = cos(pos / 10000^{(2i/d_{model})})", color=YELLOW).scale(0.6).next_to(pe_equation_1, DOWN)
            self.play(Write(pe_equation_1), Write(pe_equation_2))

            # Implementation: Show matrix of embeddings
            # Thinking: Position matrix below equations and use blue color
            embeddings_matrix = Matrix([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.2, 0.3, 0.5], [0.6, 0.1, 0.4]], element_color=BLUE).scale(0.7).next_to(pe_equation_2, DOWN, buff=0.5)
            self.play(Create(embeddings_matrix))

            # Implementation: Animate adding positional vectors
            # Thinking: Show matrix addition at the bottom of the screen
            positional_vectors = Matrix([[0.01, 0.02, 0.03], [0.04, 0.05, 0.06], [0.02, 0.03, 0.05], [0.06, 0.01, 0.04]], element_color=YELLOW).scale(0.7)
            plus_sign = Text("+", color=WHITE).scale(0.7)
            result_matrix = Matrix([[0.11, 0.22, 0.33], [0.44, 0.55, 0.66], [0.22, 0.33, 0.55], [0.66, 0.11, 0.44]], element_color=BLUE).scale(0.7)
            
            # Thinking: Position matrix addition below embeddings matrix
            addition_group = VGroup(embeddings_matrix.copy(), plus_sign, positional_vectors, Text("=", color=WHITE).scale(0.7), result_matrix).arrange(RIGHT).next_to(embeddings_matrix, DOWN, buff=0.5)
            self.play(Create(addition_group))

        # Cleaning: Clear all objects
        self.clear()

    def play_scene_3(self):
        # Implementation: Setting scene style as mentioned in prompt
        self.camera.background_color = BLUE_E

        # Implementation: Part 1
        with self.voiceover(text="The core of the transformer is the multi-head self-attention.") as tracker:
            # Implementation: Display "Multi-Head Self-Attention" text
            # Thinking: Position text at top center and scale down to fit in frame
            mhsa_text = Text("Multi-Head Self-Attention", color=WHITE).scale(0.8).to_edge(UP)
            self.play(Write(mhsa_text))

        # Cleaning: No objects should be cleared

        # Implementation: Part 2
        with self.voiceover(text="We derive Query, Key, and Value matrices from the input embeddings.") as tracker:
            # Implementation: Show input embeddings matrix X
            # Thinking: Position matrix on the left and use blue color
            x_matrix = Matrix([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.2, 0.3, 0.5]], element_color=BLUE).scale(0.7).to_edge(LEFT)
            self.play(Create(x_matrix))

            # Implementation: Display linear transformations
            # Thinking: Center equations on the screen and use standard blue
            q_equation = MathTex("Q = X * W_Q", color=BLUE).scale(0.7).shift(UP)
            k_equation = MathTex("K = X * W_K", color=BLUE).scale(0.7)
            v_equation = MathTex("V = X * W_V", color=BLUE).scale(0.7).shift(DOWN)

            # Implementation: Show matrices W_Q, W_K, W_V
            # Thinking: Position matrices next to the equations
            w_q_matrix = Matrix([[0.1, 0.2], [0.3, 0.4], [0.5, 0.6]], element_color=BLUE).scale(0.6).next_to(q_equation, RIGHT)
            w_k_matrix = Matrix([[0.2, 0.3], [0.4, 0.5], [0.6, 0.7]], element_color=BLUE).scale(0.6).next_to(k_equation, RIGHT)
            w_v_matrix = Matrix([[0.3, 0.4], [0.5, 0.6], [0.7, 0.8]], element_color=BLUE).scale(0.6).next_to(v_equation, RIGHT)

            self.play(
                Write(q_equation),
                Write(k_equation),
                Write(v_equation),
                Create(w_q_matrix),
                Create(w_k_matrix),
                Create(w_v_matrix),
            )

        # Cleaning: Clear all objects
        self.clear()

        # Implementation: Part 3
        with self.voiceover(text="Each head calculates attention using the scaled dot-product formula.") as tracker:
            # Implementation: Display the attention formula
            # Thinking: Center formula on the screen and use standard blue
            attention_formula = MathTex("Attention(Q, K, V) = softmax((Q * K^T) / \\sqrt{d_k}) * V", color=BLUE).scale(0.7)
            self.play(Write(attention_formula))

        # Cleaning: Clear all objects
        self.clear()

        # Implementation: Part 4
        with self.voiceover(text="Multiple heads work in parallel, capturing different relationships, and their outputs are concatenated and linearly transformed.") as tracker:
            # Implementation: Show three attention heads
            # Thinking: Position heads at the top with different colors
            head_1 = VGroup(
                Text("Head 1", color=RED).scale(0.6),
                MathTex("Q_1", color=RED).scale(0.6),
                MathTex("K_1", color=RED).scale(0.6),
                MathTex("V_1", color=RED).scale(0.6),
            ).arrange(DOWN).shift(LEFT * 4 + UP * 2)
            head_2 = VGroup(
                Text("Head 2", color=GREEN).scale(0.6),
                MathTex("Q_2", color=GREEN).scale(0.6),
                MathTex("K_2", color=GREEN).scale(0.6),
                MathTex("V_2", color=GREEN).scale(0.6),
            ).arrange(DOWN).shift(UP * 2)
            head_3 = VGroup(
                Text("Head 3", color=YELLOW).scale(0.6),
                MathTex("Q_3", color=YELLOW).scale(0.6),
                MathTex("K_3", color=YELLOW).scale(0.6),
                MathTex("V_3", color=YELLOW).scale(0.6),
            ).arrange(DOWN).shift(RIGHT * 4 + UP * 2)

            self.play(
                Write(head_1),
                Write(head_2),
                Write(head_3),
            )

            # Implementation: Animate outputs being concatenated
            # Thinking: Position concatenation at the bottom
            concat_output = MathTex("Concat(Head_1, Head_2, Head_3)", color=WHITE).scale(0.6).shift(DOWN * 2)
            arrows_to_concat = [
                Arrow(head_1.get_bottom(), concat_output.get_top(), color=WHITE),
                Arrow(head_2.get_bottom(), concat_output.get_top(), color=WHITE),
                Arrow(head_3.get_bottom(), concat_output.get_top(), color=WHITE),
            ]
            self.play(
                Write(concat_output),
                *[Create(arrow) for arrow in arrows_to_concat],
            )

            # Implementation: Show final linear transformation
            # Thinking: Position transformation at the bottom right
            final_linear = MathTex("Linear(Concat)", color=WHITE).scale(0.6).next_to(concat_output, RIGHT, buff=1)
            arrow_to_final = Arrow(concat_output.get_right(), final_linear.get_left(), color=WHITE)
            self.play(
                Write(final_linear),
                Create(arrow_to_final),
            )

        # Cleaning: Clear all objects
        self.clear()

    def play_scene_4(self):
        # Implementation: Setting scene style as mentioned in prompt
        self.camera.background_color = BLUE_E

        # Implementation: Part 1
        with self.voiceover(text="Each encoder and decoder layer contains a feed-forward network, which is a simple two-layer neural network.") as tracker:
            # Implementation: Display "Feed-Forward Network" text
            # Thinking: Position text at top center and scale down to fit in frame
            ffn_text = Text("Feed-Forward Network", color=WHITE).scale(0.8).to_edge(UP)
            self.play(Write(ffn_text))

            # Implementation: Show a simple two-layer neural network diagram
            # Thinking: Center diagram below the text and use blue nodes and green connections
            input_layer = VGroup(*[Circle(radius=0.2, color=BLUE) for _ in range(3)]).arrange(RIGHT, buff=0.5).shift(LEFT * 3 + DOWN)
            hidden_layer = VGroup(*[Circle(radius=0.2, color=BLUE) for _ in range(2)]).arrange(RIGHT, buff=0.5).shift(DOWN)
            output_layer = VGroup(*[Circle(radius=0.2, color=BLUE) for _ in range(3)]).arrange(RIGHT, buff=0.5).shift(RIGHT * 3 + DOWN)

            connections = []
            for node in input_layer:
                for h_node in hidden_layer:
                    connections.append(Arrow(node.get_center(), h_node.get_center(), color=GREEN, buff=0.2))
            for h_node in hidden_layer:
                for o_node in output_layer:
                    connections.append(Arrow(h_node.get_center(), o_node.get_center(), color=GREEN, buff=0.2))

            self.play(
                Create(input_layer),
                Create(hidden_layer),
                Create(output_layer),
                *[Create(connection) for connection in connections],
            )

            # Implementation: Animate data flowing through the network
            # Thinking: Use arrows to show data flow
            data_flow_arrows = []
            for i in range(len(input_layer)):
                data_flow_arrows.append(Arrow(input_layer[i].get_center(), hidden_layer[min(i, len(hidden_layer) - 1)].get_center(), color=YELLOW, buff=0.2))
                if i < len(hidden_layer):
                    data_flow_arrows.append(Arrow(hidden_layer[i].get_center(), output_layer[i].get_center(), color=YELLOW, buff=0.2))

            for arrow in data_flow_arrows:
                self.play(Create(arrow))

        # Cleaning: No objects should be cleared

        # Implementation: Part 2
        with self.voiceover(text="Residual connections add the input of each sub-layer to its output, aiding gradient flow.") as tracker:
            # Implementation: Fade out previous elements
            self.play(
                FadeOut(ffn_text),
                FadeOut(input_layer),
                FadeOut(hidden_layer),
                FadeOut(output_layer),
                *[FadeOut(connection) for connection in connections],
                *[FadeOut(arrow) for arrow in data_flow_arrows],
            )

            # Implementation: Display "Residual Connections" text
            # Thinking: Position text at top center and scale down to fit in frame
            residual_text = Text("Residual Connections", color=WHITE).scale(0.8).to_edge(UP)
            self.play(Write(residual_text))

            # Implementation: Show the addition formula
            # Thinking: Center formula below the text and use standard blue
            addition_formula = MathTex("Layer Input + Sublayer(Layer Input)", color=BLUE).scale(0.7).next_to(residual_text, DOWN)
            plus_sign = addition_formula.get_part_by_tex("+")
            self.play(Write(addition_formula), plus_sign.animate.set_color(RED))

        # Cleaning: Clear all objects
        self.clear()

        # Implementation: Part 3
        with self.voiceover(text="Layer normalization is applied to stabilize training.") as tracker:
            # Implementation: Display "Layer Normalization" text
            # Thinking: Position text at top center and scale down to fit in frame
            layer_norm_text = Text("Layer Normalization", color=WHITE).scale(0.8).to_edge(UP)
            self.play(Write(layer_norm_text))

            # Implementation: Show the layer normalization formula
            # Thinking: Center formula below the text and use yellow color
            layer_norm_formula = MathTex("LayerNorm(x + Sublayer(x))", color=YELLOW).scale(0.7).next_to(layer_norm_text, DOWN)
            self.play(Write(layer_norm_formula))

        # Cleaning: Clear all objects
        self.clear()

    def play_scene_5(self):
        # Implementation: Setting scene style as mentioned in prompt
        self.camera.background_color = BLUE_E

        # Implementation: Part 1
        with self.voiceover(text="Here's the complete transformer structure. Data flows through the encoder, gets transformed, and then passes to the decoder.") as tracker:
            # Implementation: Show the complete transformer diagram
            # Thinking: Center diagram on the screen
            encoder_block = Rectangle(width=3, height=4, color=BLUE).shift(LEFT * 3)
            decoder_block = Rectangle(width=3, height=4, color=GREEN).shift(RIGHT * 3)
            encoder_label = Text("Encoder", color=WHITE).scale(0.6).move_to(encoder_block.get_top())
            decoder_label = Text("Decoder", color=WHITE).scale(0.6).move_to(decoder_block.get_top())

            self.play(
                Create(encoder_block),
                Create(decoder_block),
                Write(encoder_label),
                Write(decoder_label),
            )

            # Implementation: Animate data flow through encoder
            # Thinking: Use white arrows to show data flow
            input_embeddings = Text("Input Embeddings", color=WHITE).scale(0.6).next_to(encoder_block, DOWN, buff=0.5)
            arrow_to_encoder = Arrow(input_embeddings.get_top(), encoder_block.get_bottom(), color=WHITE)
            self.play(
                Write(input_embeddings),
                Create(arrow_to_encoder),
            )

            # Implementation: Show data flow through decoder
            # Thinking: Highlight masked multi-head attention and encoder-decoder attention
            arrow_to_decoder = Arrow(encoder_block.get_right(), decoder_block.get_left(), color=WHITE)
            masked_attention = Text("Masked Multi-Head Attention", color=WHITE).scale(0.5).move_to(decoder_block.get_top() + DOWN)
            encoder_decoder_attention = Text("Encoder-Decoder Attention", color=WHITE).scale(0.5).move_to(decoder_block.get_center())
            self.play(
                Create(arrow_to_decoder),
                Write(masked_attention),
                Write(encoder_decoder_attention),
            )

        # Cleaning: No objects should be cleared

        # Implementation: Part 2
        with self.voiceover(text="The decoder uses multi-head attention and, finally, a linear layer with a softmax function produces output probabilities.") as tracker:
            # Implementation: Show the final linear layer
            # Thinking: Position layer at the bottom right
            final_linear_layer = Rectangle(width=2, height=1, color=YELLOW).next_to(decoder_block, DOWN, aligned_edge=RIGHT)
            linear_label = Text("Linear", color=WHITE).scale(0.5).move_to(final_linear_layer.get_center())
            arrow_to_linear = Arrow(decoder_block.get_bottom(), final_linear_layer.get_top(), color=WHITE)
            self.play(
                Create(final_linear_layer),
                Write(linear_label),
                Create(arrow_to_linear),
            )

            # Implementation: Represent the softmax function
            # Thinking: Position function next to the linear layer
            softmax_func = Text("Softmax", color=RED).scale(0.5).next_to(final_linear_layer, RIGHT)
            arrow_to_softmax = Arrow(final_linear_layer.get_right(), softmax_func.get_left(), color=WHITE)
            self.play(
                Write(softmax_func),
                Create(arrow_to_softmax),
            )

            # Implementation: Display output probabilities
            # Thinking: Position probabilities next to the softmax function
            output_probabilities = Text("Output Probabilities", color=LIGHT_BLUE).scale(0.5).next_to(softmax_func, RIGHT)
            arrow_to_output = Arrow(softmax_func.get_right(), output_probabilities.get_left(), color=WHITE)
            self.play(
                Write(output_probabilities),
                Create(arrow_to_output),
            )

        # Cleaning: Clear all objects
        self.clear()
    
    def play_scene_6(self):
        # Implementation: Setting scene style as mentioned in prompt
        self.camera.background_color = BLUE_E

        # Implementation: Part 1
        with self.voiceover(text="Transformers offer significant advantages, including parallel processing, handling long-range dependencies, and enabling transfer learning.") as tracker:
            # Implementation: Display "Advantages of Transformers" text
            # Thinking: Position text at top center and scale down to fit in frame
            advantages_text = Text("Advantages of Transformers", color=WHITE).scale(0.8).to_edge(UP)
            self.play(Write(advantages_text))

            # Implementation: List advantages in green
            # Thinking: Position list below the text, each on a new line
            parallelization = Text("Parallelization", color=GREEN).scale(0.7).next_to(advantages_text, DOWN, aligned_edge=LEFT).shift(DOWN*0.5)
            long_range = Text("Long-Range Dependencies", color=GREEN).scale(0.7).next_to(parallelization, DOWN, aligned_edge=LEFT)
            transfer_learning = Text("Transfer Learning", color=GREEN).scale(0.7).next_to(long_range, DOWN, aligned_edge=LEFT)
            self.play(
                Write(parallelization),
                Write(long_range),
                Write(transfer_learning),
            )

            # Implementation: Show icons for different fields
            # Thinking: Position icons on the right and use light blue color
            nlp_icon = Text("NLP", color=LIGHT_BLUE).scale(0.5).shift(RIGHT * 3 + UP * 1)
            cv_icon = Text("CV", color=LIGHT_BLUE).scale(0.5).next_to(nlp_icon, DOWN)
            other_icon = Text("Other", color=LIGHT_BLUE).scale(0.5).next_to(cv_icon, DOWN)
            self.play(
                Write(nlp_icon),
                Write(cv_icon),
                Write(other_icon),
            )

        # Cleaning: No objects should be cleared

        # Implementation: Part 2
        with self.voiceover(text="They have revolutionized various fields, including machine translation, text summarization, and image classification. The transformer model has truly transformed machine learning.") as tracker:
            # Implementation: Fade out previous elements
            self.play(
                FadeOut(parallelization),
                FadeOut(long_range),
                FadeOut(transfer_learning),
                FadeOut(nlp_icon),
                FadeOut(cv_icon),
                FadeOut(other_icon),
            )

            # Implementation: Display "Applications" text
            # Thinking: Position text at top center and scale down to fit in frame
            applications_text = Text("Applications", color=WHITE).scale(0.8).to_edge(UP)
            self.play(
                ReplacementTransform(advantages_text, applications_text)
            )

            # Implementation: List application examples in yellow
            # Thinking: Position list below the text, each on a new line
            translation = Text("Machine Translation", color=YELLOW).scale(0.7).next_to(applications_text, DOWN, aligned_edge=LEFT).shift(DOWN*0.5)
            summarization = Text("Text Summarization", color=YELLOW).scale(0.7).next_to(translation, DOWN, aligned_edge=LEFT)
            classification = Text("Image Classification", color=YELLOW).scale(0.7).next_to(summarization, DOWN, aligned_edge=LEFT)
            self.play(
                Write(translation),
                Write(summarization),
                Write(classification),
            )

        # Cleaning: Clear all objects
        self.clear()
