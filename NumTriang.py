from manim import *

class TriangularNumbers(Scene):
    def construct(self):
        # Título de la escena
        title = Text("Números Triangulares", font_size=48)
        self.play(Write(title))
        self.wait(6)
        self.play(FadeOut(title))

        # Introducir la explicación de los números triangulares
        intro_text = Text("Los primeros números triangulares son:", font_size=36)
        self.play(Write(intro_text))
        self.wait(2)
        self.play(FadeOut(intro_text))

        # Mostrar los primeros números triangulares
        triangular_numbers = VGroup(
            Text("T_1 = 1", font_size=32),
            Text("T_2 = 1 + 2 = 3", font_size=32),
            Text("T_3 = 1 + 2 + 3 = 6", font_size=32),
            Text("T_4 = 1 + 2 + 3 + 4 = 10", font_size=32),
            Text("T_5 = 1 + 2 + 3 + 4 + 5 = 15", font_size=32),
        ).arrange(DOWN, buff=0.5).shift(UP)

        # Animar la aparición de los números triangulares
        self.play(Write(triangular_numbers))
        self.wait(8)
        self.play(FadeOut(triangular_numbers))

        # Añadir el texto "Formula:" en la parte superior
        formula_title = Text("Fórmula:", font_size=36)
        self.play(Write(formula_title))
        self.wait(1)
        self.play(FadeOut(formula_title))

        # Mostrar la fórmula de los números triangulares
        formula = MathTex(r"T_n = \frac{n(n + 1)}{2}", font_size=48)
        self.play(Write(formula))
        self.wait(10)

