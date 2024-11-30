from manim import *
import numpy as np

def circumcenter(A, B, C):
    ax, ay, _ = A
    bx, by, _ = B
    cx, cy, _ = C

    d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
    ux = ((ax * ax + ay * ay) * (by - cy) + (bx * bx + by * by) * (cy - ay) + (cx * cx + cy * cy) * (ay - by)) / d
    uy = ((ax * ax + ay * ay) * (cx - bx) + (bx * bx + by * by) * (ax - cx) + (cx * cx + cy * cy) * (bx - ax)) / d

    return np.array([ux, uy, 0])

def radius(O, A):
    return np.linalg.norm(O - A)


class Geometry(Scene):
    def construct(self):
        const = 2.5
        R = 2.5
        A = LEFT * R
        B = RIGHT * R
        O = ORIGIN
        C = UP * R
        E = UP * (R/3**0.5)

        semicircle = Arc(radius=R, start_angle=PI, angle=-PI, color=TEAL)
        diameter = Line(A, B, color=WHITE)
        radius_OC = Line(O, C, color=WHITE)

        points = {
            'A': A, 'B': B, 'O': O, 'C': C, 'E': E
        }
        point_objects = {
            key: Dot(value, color=WHITE, radius=R/40).set_z_index(3)
            for key, value in points.items()
        }

        labels = {
            key: MathTex(key, font_size=16*R).next_to(point_objects[key], 
                        UP if key in ['C', 'D'] else
                        DOWN if key == 'O' else
                        LEFT if key in ['A', 'E'] else RIGHT
                        ).set_z_index(3)
            for key in points.keys()
        }

        m = (E[1] - A[1]) / (E[0] - A[0])
        b = A[1] - m * A[0]
        
        a = 1 + m**2
        b_coeff = 2 * m * b
        c = b**2 - R**2
        discriminant = b_coeff**2 - 4 * a * c

        if discriminant >= 0:
            x1 = (-b_coeff + discriminant**0.5) / (2 * a)
            y1 = m * x1 + b
            M = np.array([x1, y1, 0])
            
            point_M = Dot(M, color=WHITE, radius=R/40).set_z_index(3)
            label_M = MathTex("M", font_size=16*R).next_to(point_M, RIGHT + UP).set_z_index(3)

        line_AM = Line(A, M, color=WHITE)
        yd = (x1**2 + y1**2)/y1
        D = np.array([0, yd, 0])
        point_D = Dot(D, color=WHITE, radius=R/40).set_z_index(3)
        label_D = MathTex("D", font_size=16*R).next_to(point_D, UP).set_z_index(3)
        line_OD = Line(O, D, color=WHITE)
        line_MD = Line(M, D, color=WHITE)

        yk = R*y1/(R - x1)
        K = np.array([0, yk, 0])
        P = circumcenter(K, D, M)

        group = VGroup(
            semicircle, diameter, radius_OC,
            *point_objects.values(), point_M, point_D,
            *labels.values(), label_M, label_D,
            line_AM, line_OD, line_MD
        )

        self.play(Create(diameter), Write(point_objects['A']), Write(labels['A']), run_time=0.75)
        self.play(Write(point_objects['B']), Write(labels['B']))
        self.play(Write(point_objects['O']), Write(labels['O']))
        self.play(Create(semicircle))
        self.play(Create(radius_OC))
        self.play(Write(point_objects['C']), Write(labels['C']))
        self.play(Write(point_objects['E']), Write(labels['E']))
        self.wait(0.5)
        
        self.play(
            labels['E'].animate.shift(UP*R/24),
            Create(line_AM),
            run_time=1
        )
        self.play(Create(point_M), Write(label_M))
        self.wait(0.5)
        self.play(
            Create(line_MD),
            Create(line_OD),
            labels['C'].animate.shift(LEFT*R/8 + DOWN*R/12),
            run_time=1
        )
        self.play(Write(point_D), Write(label_D))

        self.play(group.animate.shift(DOWN * const), run_time=1)
        
        B_new = B + DOWN*const
        O_new = O + DOWN*const
        K = K + DOWN*const

        point_K = Dot(K, color=WHITE, radius=R/40).set_z_index(3)
        label_K = MathTex("K", font_size=16*R).next_to(point_K, UP).set_z_index(3)
        line_BK = Line(B_new, K, color=WHITE)
        line_OK = Line(O_new, K, color=WHITE)
        
        self.play(
            Create(line_BK),
            Create(line_OK),
            label_D.animate.shift(RIGHT*R/9 + DOWN*R/12),
            run_time=1
        )
        C += DOWN*const
        M += DOWN*const
        E += DOWN*const
        I = circumcenter(C, M, E)
        I_R = radius(I, E)
        Cir_CME = Circle(radius=I_R, color=GREEN).move_to(I)
        E += DOWN*const
        L = circumcenter(O, B, E)
        L_R = ((R**2 + (R/3**0.5)**2)**0.5)/2
        Cir_OBE = Circle(radius=L_R, color=RED).move_to(L)

        self.play(Write(point_K), Write(label_K), Create(Line(C, M, color=WHITE)))
        
        D += DOWN*const
        M += DOWN*const
        P += DOWN*const
        P_R = R/3**0.5
        Cir_DMK = Circle(radius=P_R, color=YELLOW).move_to(P)
        
        self.play(Create(Cir_CME))
        self.play(Create(Cir_OBE))
        self.play(
            Create(Cir_DMK),
            label_M.animate.shift(LEFT*R/15),
            run_time=1
        )
        self.play(Create(Circle(radius=R, color=BLUE_E).move_to(M+UP*const)))
        self.wait(5)