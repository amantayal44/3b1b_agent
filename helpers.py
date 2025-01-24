import prompt
import re


def remove_json(text):
    if "```json" in text:
        # Select text after '```json' and before last '```'
        text = text[text.find("```json") + 7 : text.rfind("```")]
    return text


def remove_python(text):
    text = text.replace("```python", "")
    text = text.replace("```", "")
    return text


def estimate_duration(text):
    words_count = len(text.split())
    # 150 words per minute -> 2.5 words per second
    speech_rate_wps = 2.5
    min_seconds = 2
    return max(round(words_count / speech_rate_wps), min_seconds)


def indent_python_code(code, scene_ids=[]):
    code = remove_python(code)
    code_lines = code.split("\n")

    def remove_trailing_empty_lines(lines):
        while lines and not lines[-1].strip():
            lines.pop(-1)

    required_method_names = ["play_scene_{}".format(scene_id) for scene_id in scene_ids]

    def check_required_method(method_name):
        if not method_name.strip().startswith("def play_scene_"):
            return False
        return any(name in method_name for name in required_method_names)

    methods = []
    curr_method = []
    for line in code_lines:
        if line.strip().startswith("def play_scene_"):
            remove_trailing_empty_lines(curr_method)
            if curr_method and check_required_method(curr_method[0]):
                methods.append("\n".join(curr_method))
            curr_method = []
        curr_method.append(line.rstrip())

    remove_trailing_empty_lines(curr_method)
    if curr_method and check_required_method(curr_method[0]):
        methods.append("\n".join(curr_method))

    return "\n\n" + "\n\n".join(methods)


def process_voiceover_code(code_string):
    """
    Process Python code by:
    1. Removing only 'with self.voiceover(text="") as tracker:' statements that have empty text
    2. Preserving voiceover statements with non-empty text
    3. Replacing tracker.duration with 1 in appropriate cases

    Args:
        code_string (str): Input Python code as a string

    Returns:
        str: Processed Python code
    """
    lines = code_string.splitlines()
    processed_lines = []
    in_empty_voiceover = False
    voiceover_indent = 0

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped_line = line.strip()
        current_indent = len(line) - len(line.lstrip())

        # Check specifically for empty voiceover pattern
        empty_voiceover_pattern = r'\s*with\s+self\.voiceover\s*\(text\s*=\s*["\'][\s]*["\']\)\s*as\s+tracker\s*:'
        # Check if it's a voiceover line (for tracking non-empty ones)
        voiceover_pattern = r"\s*with\s+self\.voiceover\s*\(.*?\)\s*as\s+tracker\s*:"

        if re.match(empty_voiceover_pattern, line):
            # Skip empty voiceover lines
            in_empty_voiceover = True
            voiceover_indent = current_indent
            i += 1
            continue
        elif re.match(voiceover_pattern, line):
            # Preserve non-empty voiceover lines
            processed_lines.append(line)
            i += 1
            continue

        # Process line
        if stripped_line:
            processed_line = line

            # Replace tracker.duration with 1 only if we're in an empty voiceover block
            if in_empty_voiceover and current_indent > voiceover_indent:
                processed_line = re.sub(r"tracker\.duration", "1", line)
                # Remove one level of indentation (4 spaces)
                processed_line = " " * (current_indent - 4) + processed_line.lstrip()

            # Check if we're exiting the voiceover block
            if in_empty_voiceover and (
                i + 1 >= len(lines)
                or len(lines[i + 1]) - len(lines[i + 1].lstrip()) <= voiceover_indent
            ):
                in_empty_voiceover = False

            processed_lines.append(processed_line)
        else:
            # Preserve empty lines
            processed_lines.append(line)

        i += 1

    return "\n".join(processed_lines)
