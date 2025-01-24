# 3Blue1Brown Agent
Convert any problem to animation video

## Agent Pipeline
### Researcher
Given any problem create a detailed research work around it including any illustrations, graphs, etc. to help user understand the problem.

### Sketch Generator
Given a problem and research work around, design a sketch for the video including multiple different scenes.

### Scene Generator
Given a sketch of the video consisting of multiple scenes, it divides each scene into multiple part. For each part, it outputs animation and audio that should be played along.

### Animation Code Generator
Given a complete description of video (divided into multiple animation and audio), it outputs a python code using manim and manim_voiceover library.

### Sample Videos
**Help me Understand Linear Regression**  
<video src="assets/LinearReg.mp4" controls width="600"></video>

**What is the difference b/w SQL and NoSQL databases**  
<video src="assets/sqlvsnosql.mp4" controls width="600"></video>

**Explain all the three laws of motion**  
<video src="assets/laws_of_motion.mp4" controls width="600"></video>

**What is Gaussian distribution**  
<video src="assets/gaussian.mp4" controls width="600"></video>