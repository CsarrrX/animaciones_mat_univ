from manim import *

class PotenciasDe11EnTrianguloDePascal(Scene):
    def construct(self):
        # Primera Parte: Construir el triángulo de Pascal
        pascal_triangle = []
        max_rows = 6  # Para mostrar hasta la fila 5
        
        for i in range(max_rows):
            row = [1]  # Inicia cada fila con 1
            if i > 0:
                last_row = pascal_triangle[-1]
                row += [last_row[j] + last_row[j+1] for j in range(len(last_row) - 1)]
                row.append(1)  # Termina cada fila con 1
            pascal_triangle.append(row)
        
        # Visualización del triángulo de Pascal en la escena y ajustar altura
        pascal_mobs = VGroup()  # Agrupamos las filas para manipularlas
        for i, row in enumerate(pascal_triangle):
            row_mobs = VGroup(*[MathTex(str(num)).scale(0.8) for num in row])
            row_mobs.arrange(RIGHT, buff=0.5).shift(UP * (3 - i) * 0.8)  # Centrar más alto
            pascal_mobs.add(row_mobs)
        
        self.play(FadeIn(pascal_mobs), run_time=2)
        self.wait(1)

        # Segunda Parte: Mostrar equivalencia con potencias de 11 en las primeras 5 filas
        for n, row_mobs in enumerate(pascal_mobs[:5]):
            row_numbers = "".join([str(num) for num in pascal_triangle[n]])
            power_of_11 = MathTex(f"11^{n} = {row_numbers}").next_to(row_mobs, RIGHT, buff=1)
            self.play(FadeIn(power_of_11), row_mobs.animate.set_color(YELLOW), run_time=1.5)
            self.wait(1)
            self.play(FadeOut(power_of_11), row_mobs.animate.set_color(WHITE))

        # Tercera Parte: Continuación del patrón en filas superiores con suma de cifras
        row_5_original = [1, 5, 10, 10, 5, 1]
        row_5_adjusted = [1, 6, 1, 0, 5, 1]  # Aplicando la regla de suma de cifras
        
        # Mostrar los números originales de la fila 5 y la versión ajustada
        row_5_original_mob = VGroup(*[MathTex(str(num)).scale(0.8) for num in row_5_original])
        row_5_original_mob.arrange(RIGHT, buff=0.5).shift(UP * -2.5)
        row_5_adjusted_mob = VGroup(*[MathTex(str(num)).scale(0.8) for num in row_5_adjusted])
        row_5_adjusted_mob.arrange(RIGHT, buff=0.5).next_to(row_5_original_mob, DOWN, buff=0.8)

        # Animar el ajuste de la fila 5
        self.play(FadeIn(row_5_original_mob), run_time=1.5)
        self.wait(1)
        self.play(Transform(row_5_original_mob, row_5_adjusted_mob), run_time=2)
        self.wait(2)

        # Despedida de la animación
        self.play(FadeOut(pascal_mobs, row_5_original_mob))
        self.wait(1)
