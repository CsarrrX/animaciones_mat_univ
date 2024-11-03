from manim import *

class FibonacciSequence(Scene):
    def construct(self):
        # Lista para almacenar los números de Fibonacci
        fibonacci_numbers = [0, 1]
        number_mobjects = VGroup(
            MathTex("0").scale(0.8), MathTex("1").scale(0.8)
        )
        # Alinear el primer grupo de números hacia la izquierda de la pantalla
        number_mobjects.arrange(RIGHT, buff=0.8).to_edge(LEFT)

        # Mostrar los primeros dos números de Fibonacci
        self.play(FadeIn(number_mobjects[0]), FadeIn(number_mobjects[1]), run_time=0.3)

        # Calcular y mostrar el resto de la secuencia de Fibonacci
        for i in range(8):
            # Calcular el siguiente número de Fibonacci
            next_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]
            fibonacci_numbers.append(next_number)

            # Crear el Tex para el nuevo número
            next_number_mobject = MathTex(str(next_number), color=YELLOW).scale(0.8)
            next_number_mobject.next_to(number_mobjects, RIGHT, buff=0.8)
            number_mobjects.add(next_number_mobject)

            # Crear el Tex para la suma que da el nuevo número
            sum_formula = MathTex(
                f"{fibonacci_numbers[-3]} + {fibonacci_numbers[-2]} = {next_number}"
            ).scale(0.6).next_to(number_mobjects, UP)

            # Animar el cálculo y la aparición del nuevo número
            self.play(Write(sum_formula), run_time=0.3)
            self.play(FadeIn(next_number_mobject, shift=UP), run_time=0.3)
            self.wait(0.2)
            self.play(FadeOut(sum_formula), run_time=0.2)

            # Desplazar todo el grupo hacia la izquierda si se acerca al borde derecho
            if number_mobjects.get_right()[0] > config.frame_width / 2:
                self.play(number_mobjects.animate.shift(LEFT * 0.8), run_time=0.3)

        self.wait(1)
