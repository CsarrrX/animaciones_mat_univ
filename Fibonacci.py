from manim import *

class TrianguloDePascalSumaDiagonal(Scene):
    def construct(self):
        # Primera Parte: Construcción del triángulo de Pascal
        pascal_triangle = []
        max_rows = 6  # Hasta la fila 5

        for i in range(max_rows):
            row = [1]  # Inicia cada fila con 1
            if i > 0:
                last_row = pascal_triangle[-1]
                row += [last_row[j] + last_row[j+1] for j in range(len(last_row) - 1)]
                row.append(1)  # Termina cada fila con 1
            pascal_triangle.append(row)
        
        # Visualización inicial del triángulo de Pascal, centrado verticalmente
        pascal_mobs = VGroup()  # Agrupamos las filas para manipularlas
        for i, row in enumerate(pascal_triangle):
            row_mobs = VGroup(*[MathTex(str(num)).scale(0.8) for num in row])
            row_mobs.arrange(RIGHT, buff=0.5).shift(DOWN * i * 0.8)
            pascal_mobs.add(row_mobs)
        
        pascal_mobs.shift(UP * 1.5)  # Centrado vertical
        
        # Animación de aparición del triángulo
        self.play(FadeIn(pascal_mobs), run_time=2)
        self.wait(1)

        # Segunda Parte: Alinear a la izquierda
        aligned_left_mobs = pascal_mobs.copy().arrange(DOWN, aligned_edge=LEFT, buff=0.8).shift(UP * 1)
        self.play(Transform(pascal_mobs, aligned_left_mobs), run_time=2)
        self.wait(1)

        # Tercera Parte: Mostrar las sumas de las diagonales
        diagonal_sums = []
        max_diagonal = max_rows - 1
        for k in range(max_diagonal + 1):
            diagonal_sum = sum(pascal_triangle[i][k - i] for i in range(k + 1) if k - i < len(pascal_triangle[i]))
            diagonal_sums.append(diagonal_sum)

        # Visualización de las sumas diagonales a la izquierda
        diagonal_sums_mobs = VGroup()
        for i, sum_value in enumerate(diagonal_sums):
            sum_mob = MathTex(str(sum_value)).scale(0.8)
            sum_mob.next_to(pascal_mobs[i], LEFT, buff=1)
            diagonal_sums_mobs.add(sum_mob)
        
        # Animación de aparición de las sumas diagonales
        self.play(FadeIn(diagonal_sums_mobs, shift=RIGHT), run_time=2)
        self.wait(2)
