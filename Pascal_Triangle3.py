from manim import *

class PascalTriangleWithInfinityAndQuestion(Scene):
    def construct(self):
        # Define el tamaño del texto
        text_size = 40
        
        # Texto inicial
        title = Text("¿Qué es el Triángulo de Pascal?", font_size=text_size).move_to(ORIGIN)
        
        # Animar el texto y moverlo hacia arriba
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        
        # Crear el Triángulo de Pascal correctamente orientado
        pascal_triangle = self.create_pascals_triangle(5)
        
        # Animar el Triángulo de Pascal con FadeIn
        self.play(FadeIn(pascal_triangle))
        self.wait(1)
        
        # Mover el Triángulo de Pascal hacia la izquierda
        self.play(pascal_triangle.animate.shift(LEFT * 2))
        
        # Crear el símbolo de infinito a la derecha, un poco más separado
        infinity_symbol = MathTex(r"\infty", font_size=80).next_to(pascal_triangle, RIGHT, buff=2)
        
        # Animar el símbolo de infinito
        self.play(FadeIn(infinity_symbol))
        self.wait(2)

        # Desvanecer todo (texto, triángulo, infinito)
        self.play(FadeOut(title), FadeOut(pascal_triangle), FadeOut(infinity_symbol))
        
        # Agregar y mostrar el signo de interrogación en el centro
        question_mark = Text("?", font_size=100).move_to(ORIGIN)
        self.play(FadeIn(question_mark))
        self.wait(2)

        # Desvanecer el signo de interrogación
        self.play(FadeOut(question_mark))

    def create_pascals_triangle(self, rows):
        # Crear el triángulo completo como un grupo
        triangle = VGroup()
        for i in range(rows):
            row = VGroup()
            for j in range(i + 1):
                number = self.calculate_pascals_number(i, j)
                num_text = Text(str(number)).scale(0.7)
                # Ajustar posición para orientar correctamente el triángulo
                num_text.move_to((j - i / 2) * RIGHT + i * DOWN * 0.5)
                row.add(num_text)
            triangle.add(row)
        return triangle

    def calculate_pascals_number(self, n, k):
        # Función para calcular el número en el triángulo de Pascal
        if k == 0 or k == n:
            return 1
        return self.calculate_pascals_number(n - 1, k - 1) + self.calculate_pascals_number(n - 1, k)
