# Computer Graphics Assignments

##### This branch contains assignments focused on implementing core computer graphics algorithms using C++ and Qt Creator. These assignments explore line drawing, polygon filling, clipping, transformations, fractals, and basic animations. Key algorithms include DDA (Digital Differential Analyzer), Bresenham's line drawing, scan fill, Cohen-Sutherland line clipping, and various transformations.

## Table of Contents

1. [Assignment List](#assignment-list)
2. [Setting Up in Qt Creator](#setting-up-in-qt-creator)
3. [Assignments in Detail](#assignments-in-detail)
   - [Assignment 1: Pattern Drawing with DDA and Bresenham's Algorithms](#assignment-1-pattern-drawing-with-dda-and-bresenhams-algorithms)
   - [Assignment 2: Concave Polygon Filling](#assignment-2-concave-polygon-filling)
   - [Assignment 3: Line Clipping (Cohen-Sutherland)](#assignment-3-line-clipping-cohen-sutherland)
   - [Assignment 4: 2D Transformations](#assignment-4-2d-transformations)
   - [Assignment 5: Snowflake Generation (Fractals)](#assignment-5-snowflake-generation-fractals)
   - [Assignment 6: Koch Curves (Fractals)](#assignment-6-koch-curves-fractals)
   - [Assignment 7: Sun Rise and Sunset (OpenGL)](#assignment-7-sun-rise-and-sunset-opengl)
   - [Assignment 8: Bouncing Ball Animation](#assignment-8-bouncing-ball-animation)

---

## Assignment List

1. **Pattern Drawing**: Use DDA and Bresenham's algorithms to draw patterns involving lines and circles.
2. **Concave Polygon Filling**: Draw and fill a concave polygon using the scan fill algorithm.
3. **Line Clipping**: Implement the Cohen-Sutherland line clipping algorithm.
4. **2D Transformations**: Draw a 2D object and perform scaling, translation, and rotation transformations using operator overloading.
5. **Fractal Snowflake Generation**: Generate a snowflake fractal pattern using object-oriented principles.
6. **Fractal Koch Curves**: Create fractal patterns using Koch curves.
7. **Sun Rise and Sunset (OpenGL)**: Simulate a sun rise and sunset using OpenGL.
8. **Bouncing Ball Animation**: Implement a bouncing ball animation using a sine waveform.

---

## Setting Up in Qt Creator

Each assignment can be set up and executed in **Qt Creator**, following these steps:

1. **Open the Project**: For each assignment, create a separate project folder in Qt Creator. Use Qt's C++ project template and add the necessary files.
2. **Add Graphics Libraries**: Ensure that `QtWidgets` and any required OpenGL modules are included if OpenGL functions are used (e.g., for Assignment 7).
3. **Configure Build Settings**: For smooth rendering, ensure the project uses the correct compiler settings and target.
4. **Run the Code**: Use Qt Creator's build and run features to compile and execute each program. Adjust the project properties as needed.

---

## Assignments in Detail

### Assignment 1: Pattern Drawing with DDA and Bresenham's Algorithms

**Objective**: Write a C++ program to draw a pattern of two circles and an inscribed triangle using:

- **DDA (Digital Differential Analyzer) Algorithm**: For line drawing.
- **Bresenham's Line Drawing Algorithm**: For more efficient line rendering.

### Assignment 2: Concave Polygon Filling

**Objective**: Create a C++ program to draw a concave polygon and fill it using the scan fill algorithm. This involves:

- Drawing each edge of the polygon.
- Using the scan line fill technique to apply color within the shape boundaries.

### Assignment 3: Line Clipping (Cohen-Sutherland)

**Objective**: Implement the **Cohen-Sutherland Line Clipping Algorithm** in C++ to clip lines based on a predefined rectangular clipping window. This algorithm determines whether lines intersect the window and clips lines accordingly.

### Assignment 4: 2D Transformations

**Objective**: Draw a 2D object and implement transformations including:

- **Scaling**
- **Translation**
- **Rotation**

This assignment also involves operator overloading for transformation operations.

### Assignment 5: Snowflake Generation (Fractals)

**Objective**: Write a C++ program to generate a snowflake fractal using recursive functions and object-oriented principles. This program should use graphical recursion to create symmetrical snowflake patterns.

### Assignment 6: Koch Curves (Fractals)

**Objective**: Implement the generation of **Koch curves**, a type of fractal. This involves recursive line generation where each line segment divides into smaller segments, creating complex geometric patterns.

### Assignment 7: Sun Rise and Sunset (OpenGL)

**Objective**: Using **OpenGL**, create a C++ program to simulate the sun rising and setting. This animation should:

- Show a gradual ascent and descent of the sun.
- Use basic OpenGL functions to control the rendering of shapes and transitions.

### Assignment 8: Bouncing Ball Animation

**Objective**: Implement a bouncing ball animation using the sine wave function to simulate realistic motion. This involves:

- Controlling the ball's vertical position with sine functions.
- Creating a looped animation to display continuous bouncing.

---
