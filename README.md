
# My GitHub Page

Welcome to my GitHub page! This page is a showcase of my shitty projects and skills.

---

## Code Section

Here are some examples of my code:

## APMO Problem
[Click Here To Download The Code](APMO.py)
```python
from manim import *
from math import sqrt

def tangent_line(circle, point, length=100):
    center = circle.get_center()
    direction = rotate_vector(point - center, 90 * DEGREES)
    direction = normalize(direction)
    return Line(point - direction * length / 2, point + direction * length / 2)

from sympy import symbols, Eq, solve
import numpy as np

def circle_line_intersections(center, radius, P, Q):
    
    a, b = center[:2]
    
    dx, dy = Q[:2] - P[:2]
    
    t = symbols('t')
    xt = P[0] + t * dx
    yt = P[1] + t * dy

    eq = Eq((xt - a)**2 + (yt - b)**2, radius**2)
    sol_t = solve(eq, t)

    intersections = []
    for sol in sol_t:
        try:
            x_val = float(xt.subs(t, sol))
            y_val = float(yt.subs(t, sol))
            intersections.append(np.array([x_val, y_val, 0]))
        except:
            continue  

    return intersections

class APMO(Scene):
    def construct(self):
        Radius = 2
        a = 1.575/2.5*Radius
        b = 2.28/2.5*Radius
        height = 1
        
        A = np.array([-a, sqrt(Radius*Radius - a*a) + height, 0])
        B = np.array([-b, -sqrt(Radius*Radius - b*b) + height, 0])
        D = np.array([b, -sqrt(Radius*Radius - b*b) + height, 0])
        circle = Circle.from_three_points(A, B, D, color=TEAL)
        tg_B = tangent_line(circle, B, length=100*Radius).get_start_and_end()
        tg_D = tangent_line(circle, D, length=100*Radius).get_start_and_end()
        P = line_intersection(tg_B, tg_D)
        C = circle_line_intersections(circle.get_center(), Radius, A, P)[1]
        tg_C = tangent_line(circle, C, length=100*Radius).get_start_and_end()
        U = line_intersection((A, C), (B, D))
        V = line_intersection(tg_C, (A, B))
        Q = line_intersection(tg_C, (P, D))
        R = line_intersection(tg_C, (A, D))
        T = line_intersection(tg_C, (B, D))
        E = line_intersection((A, Q), (B, R))

        Point_A = Dot(A, color=WHITE, radius=Radius/50)
        Point_B = Dot(B, color=WHITE, radius=Radius/50)
        Point_C = Dot(C, color=WHITE, radius=Radius/50)
        Point_D = Dot(D, color=WHITE, radius=Radius/50)
        Point_P = Dot(P, color=WHITE, radius=Radius/50)
        Point_R = Dot(R, color=WHITE, radius=Radius/50)
        Point_T = Dot(T, color=WHITE, radius=Radius/50)
        Point_U = Dot(U, color=WHITE, radius=Radius/50)
        Point_V = Dot(V, color=WHITE, radius=Radius/50)
        Point_Q = Dot(Q, color=WHITE, radius=Radius/50)
        Point_E = Dot(E, color=WHITE, radius=Radius/50)
        Label_A = MathTex("A", color=WHITE).next_to(Point_A, UP)
        Label_B = MathTex("B", color=WHITE).next_to(Point_B, UP*0.2 + LEFT*0.775)
        Label_C = MathTex("C", color=WHITE).next_to(Point_C, DOWN*0.1 + LEFT*0.15)
        Label_D = MathTex("D", color=WHITE).next_to(Point_D, RIGHT)
        Label_P = MathTex("P", color=WHITE).next_to(Point_P, UP*0.25 + LEFT)
        Label_R = MathTex("R", color=WHITE).next_to(Point_R, RIGHT)
        Label_T = MathTex("T", color=WHITE).next_to(Point_T, LEFT)
        Label_U = MathTex("U", color=WHITE).next_to(Point_U, RIGHT/2 + DOWN/3)
        Label_V = MathTex("V", color=WHITE).next_to(Point_V, DOWN)
        Label_Q = MathTex("Q", color=WHITE).next_to(Point_Q, DOWN + RIGHT/10**2)
        Label_E = MathTex("E", color=WHITE).next_to(Point_E,  UP*0.7 + RIGHT/10**50)

        Quadrilateral_ABCD = Polygon(A, B, C, D, color=WHITE)
        
        Line_AP = Line(A, P, color=WHITE)
        Line_AR = Line(A, R, color=WHITE)
        Line_CR = Line(C, R, color=WHITE)
        Line_BP = Line(B, P, color=WHITE)
        Line_DP = Line(D, P, color=WHITE)
        Line_CT = Line(C, T, color=WHITE)
        Line_DT = Line(D, T, color=WHITE)
        Line_TA = Line(T, A, color=WHITE)
        Line_AQ = Line(A, Q, color=WHITE)
        Line_BR = Line(B, R, color=WHITE)
        Line_BV = Line(B, V, color=WHITE)

        self.play(
            AnimationGroup(
                Create(circle),
                AnimationGroup(
                Create(Quadrilateral_ABCD),
                Write(Point_A), Write(Label_A),
                Write(Point_B), Write(Label_B),
                Write(Point_C), Write(Label_C),
                Write(Point_D), Write(Label_D),
                lag_ratio=0.065
                ),
                lag_ratio=0.25
        ))
        self.play(Create(Line_BP),Create(Line_DP))
        self.play(Create(Line_AP))
        self.play(Write(Point_P), Write(Label_P))
        self.play(
            AnimationGroup(
                Create(Line_CR),
                AnimationGroup(Write(Point_Q), Write(Label_Q),Create(Line_AR)),
                Write(Point_R), Write(Label_R),
                lag_ratio=0.5
            )
        )
        self.play(Create(Line_AQ), Write(Point_E), Write(Label_E))
        self.wait(0.75)
        self.play(Create(Line_BR))
        self.wait(1.5)
        self.play(ReplacementTransform(Line_BR, Point_R))
        self.wait(3)
        self.play(Create(Line_CT), Create(Line_DT), Write(Point_T), Write(Label_T))
        self.wait(0.5)
        self.play(Create(Line_TA))
        self.wait(1.5)
        self.play(Write(Point_U), Write(Label_U))
        self.play(Create(Line_BV), Write(Point_V), Write(Label_V))
        self.wait(3)
```
### Result
<video width="982" controls>
  <source src="APMO.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## Wiggling Graph
[Click Here To Download The Code](Wiggling.py)
```python
import networkx as nx
import numpy as np
from manim import *

class WigglingGraph(Scene):
    def graph_configure(self, graph, **kwargs):
        for submob in graph.vertices.values():
            submob.jiggling_direction = rotate_vector(
                RIGHT, np.random.random() * TAU * 1.5
            )
            submob.jiggling_phase = np.random.random() * TAU * 1.5
        for key, value in kwargs.items():
            setattr(graph, key, value)

    def set_graph_stroke(self, graph, **kwargs):
        for e in graph.edges.values():
            e.set_stroke(**kwargs)

    def construct(self):
        def wiggle_graph_updater(graph, dt):
            for key in graph.edges:
                edge = graph.edges[key]
                edge.start = graph.vertices[key[0]].get_center()
                edge.end = graph.vertices[key[1]].get_center()

            for submob in graph.vertices.values():
                submob.jiggling_phase += dt * graph.jiggles_per_second * TAU
                submob.shift(
                    graph.jiggle_amplitude *
                    submob.jiggling_direction *
                    np.sin(submob.jiggling_phase) * dt
                )

        graph = nx.newman_watts_strogatz_graph(50, 6, 0.1, seed=248)
        graph_mob = Graph.from_networkx(
            graph, layout="kamada_kawai", layout_scale=4, labels=False
        )
        self.graph_configure(graph_mob, jiggle_amplitude=0.3, jiggles_per_second=0.3)
        graph_mob.add_updater(wiggle_graph_updater)
        self.set_graph_stroke(graph_mob, width=0.35)
        self.add(graph_mob)
        self.wait(14)
```
### Result
<video width="982" controls>
  <source src="WigglingGraph.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
