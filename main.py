import os
import google.generativeai as genai
import prompt
import helpers
import argparse
import json
import time
import config

# Configure the Generative AI API
genai.configure(api_key=config.API_KEY)
gemini_flash = "gemini-2.0-flash-exp"
gemini_exp = "gemini-exp-1206"

# Create the model configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Initialize the models
researcher = genai.GenerativeModel(
    model_name=gemini_flash,
    generation_config=generation_config,
    system_instruction=prompt.research_prompt
)

sketch_generator = genai.GenerativeModel(
    model_name=gemini_exp,
    generation_config=generation_config,
    system_instruction=prompt.sketch_generator_prompt
)

scene_generator = genai.GenerativeModel(
    model_name=gemini_exp,
    generation_config=generation_config,
    system_instruction=prompt.scene_generator_prompt
)

code_generator = genai.GenerativeModel(
    model_name=gemini_exp,
    generation_config=generation_config,
    system_instruction=prompt.code_generator_prompt
)

# Parse command line arguments
parser = argparse.ArgumentParser(description="Generate content based on a problem statement.")
parser.add_argument("problem", type=str, help="The problem statement to generate content for.")
parser.add_argument("--dir", type=str, help="Directory for storing intermediate files and output code", default="sample")
parser.add_argument("--resume", action="store_true", help="Resume from last checkpoint if available")
args = parser.parse_args()

problem = args.problem
dir = args.dir


def ensure_directory(directory):
    """Ensure the specified directory exists."""
    if not os.path.exists(directory):
        os.makedirs(directory)


def save_checkpoint(filename, content):
    """Save content to a checkpoint file."""
    filepath = os.path.join(dir, filename)
    with open(filepath, "w") as file:
        file.write(content)


def load_checkpoint(filename):
    """Load content from a checkpoint file if it exists."""
    filepath = os.path.join(dir, filename)
    if os.path.exists(filepath):
        with open(filepath, "r") as file:
            return file.read()
    return None


# Ensure tmp directory exists
ensure_directory(dir)

# Step 1: Generate Research Work
research_work = None
if args.resume:
    research_work = load_checkpoint("research_work.txt")

if research_work is None:
    try:
        print("Generating research work...")
        st_time = time.time()
        research_work_response = researcher.generate_content(f"problem: {problem}")
        research_work = research_work_response.text
        print(f"Time taken to generate research work: {time.time() - st_time:.2f} seconds")
        save_checkpoint("research_work.txt", research_work)
    except Exception as e:
        print(f"Error generating research work: {e}")
        exit(1)
else:
    print("Loaded research work from checkpoint")

# Step 2: Generate Sketch
sketch = None
if args.resume:
    sketch = load_checkpoint("sketch.json")

if sketch is None:
    try:
        print("Generating sketch...")
        st_time = time.time()
        sketch_response = sketch_generator.generate_content(f"problem:\n{problem}\nresearch:\n{research_work}")
        sketch_response = sketch_response.text
        print(f"Time taken to generate sketch: {time.time() - st_time:.2f} seconds")
        save_checkpoint("sketch_response.txt", sketch_response)

        # Capture only scenes
        sketch_response = helpers.remove_json(sketch_response).strip()
        sketch_response = sketch_response[sketch_response.find('"scenes":'):sketch_response.rfind("]")+1]
        sketch_response = '{' + sketch_response + '}'

        sketch_json = json.loads(sketch_response)
        sketch_json.pop("reasoning", None)  # Remove reasoning from sketch
        sketch = json.dumps(sketch_json)
        save_checkpoint("sketch.json", json.dumps(sketch_json, indent=2))

    except Exception as e:
        print(f"Error generating sketch: {e}")
        exit(1)
else:
    print("Loaded sketch from checkpoint")

# Step 3: Generate Scene
scene = None
if args.resume:
    scene = load_checkpoint("scene.json")

if scene is None:
    try:
        print("Generating scene...")
        st_time = time.time()
        scene_response = scene_generator.generate_content(sketch)
        scene_response = scene_response.text
        print(f"Time taken to generate scene: {time.time() - st_time:.2f} seconds")
        save_checkpoint("scene_response.txt", scene_response)

        scene_json = json.loads(helpers.remove_json(scene_response))
        # Remove animation planning from parts
        for scene in scene_json.get("scenes", []):
            scene.pop("planning", None)
            for part in scene.get("scene_parts", []):
                part.pop("animation_planning", None)

                # Add audio estimation time to each part.
                part["estimated_audio_duration_s"] = helpers.estimate_duration(part["audio_text"])

        scene = json.dumps(scene_json)
        save_checkpoint("scene.json", json.dumps(scene_json, indent=2))

    except Exception as e:
        print(f"Error generating scene: {e}")
        exit(1)
else:
    print("Loaded scene from checkpoint")

# Step 4: Generate Code
try:
    print("Generating code...")
    st_time = time.time()
    code_response = code_generator.generate_content(scene)
    print(f"Time taken to generate code: {time.time() - st_time:.2f} seconds")
    # Save raw code response
    save_checkpoint("code_response.txt", code_response.text)
    code = helpers.remove_python(code_response.text)
    save_checkpoint("main.py", code)
except Exception as e:
    print(f"Error generating code: {e}")
    exit(1)

print(f"Code successfully saved to {dir}/main.py")
