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
![Help me Understand Linear Regression](assets/LinearReg.mp4)

![What is the difference b/w sql and no sql databases](assets/sqlvsnosql.mp4)

![Explain all the threes laws of motion](assets/laws_of_motion.mp4)

![What is gaussian distribution](assets/gaussian.mp4)