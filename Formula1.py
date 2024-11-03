from manim import *

class SumFormulaAnimation(Scene):
    def construct(self):
        # Mostrar el texto explicativo en la parte superior
        formula_text = Text("La suma de todos los elementos de cada fila nos da la siguiente fórmula:", font_size=24)
        formula_text.to_edge(UP)  # Colocar el texto en la parte superior
        self.play(FadeIn(formula_text))

        # Mostrar la fórmula 2^n en el centro de la pantalla
        power_formula = MathTex("2^n").scale(2)  # Aumentar tamaño de la fórmula
        power_formula.move_to(ORIGIN)  # Centrarse en la pantalla
        self.play(FadeIn(power_formula))

        # Mostrar la nota en la parte inferior
        index_note = MathTex("(n \\text{ siendo el índice de la fila})").scale(0.6)
        index_note.next_to(power_formula, DOWN, buff=0.2)  # Colocar debajo de la fórmula
        self.play(FadeIn(index_note))

        self.wait(5)  # Esperar un momento antes de finalizar
