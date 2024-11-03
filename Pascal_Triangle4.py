from manim import *

class HighlightPascalTriangleEdgesAndSums(Scene):
    def construct(self):
        # Crear el Triángulo de Pascal en el centro
        pascal_triangle = self.create_pascals_triangle(6)
        
        # Aparición del Triángulo de Pascal con FadeIn más lento
        self.play(FadeIn(pascal_triangle, run_time=2))
        
        # Resaltar los unos al inicio y al final de cada fila
        self.highlight_edges(pascal_triangle)

        # Resaltar la suma acumulativa de los números
        self.highlight_sums(pascal_triangle)

    def create_pascals_triangle(self, rows):
        # Crear el triángulo completo como un grupo
        triangle = VGroup()
        for i in range(rows):
            row = VGroup()
            for j in range(i + 1):
                number = self.calculate_pascals_number(i, j)
                num_text = Text(str(number)).scale(0.7)
                # Ajustar posición para orientar correctamente el triángulo
                num_text.move_to((j - i / 2) * RIGHT + i * DOWN * 0.6)
                row.add(num_text)
            triangle.add(row)
        triangle.move_to(ORIGIN)  # Centrar el triángulo en pantalla
        return triangle

    def calculate_pascals_number(self, n, k):
        # Función para calcular el número en el triángulo de Pascal
        if k == 0 or k == n:
            return 1
        return self.calculate_pascals_number(n - 1, k - 1) + self.calculate_pascals_number(n - 1, k)

    def highlight_edges(self, triangle):
        # Resaltar los números "1" al inicio y final de cada fila
        for row in triangle:
            first_one = row[0]
            last_one = row[-1]
            if first_one.text == "1":
                self.play(first_one.animate.set_color(YELLOW), run_time=0.5)
            if last_one.text == "1":
                self.play(last_one.animate.set_color(YELLOW), run_time=0.5)

    def highlight_sums(self, triangle):
        # Resaltar cómo cada número en el triángulo es la suma de los dos números encima de él
        for i in range(2, len(triangle)):  # Empezamos en la tercera fila (índice 2)
            for j in range(1, len(triangle[i]) - 1):  # Evitamos los bordes (solo filas interiores)
                current_num = triangle[i][j]
                above_left = triangle[i - 1][j - 1]
                above_right = triangle[i - 1][j]

                # Resaltar rápidamente los dos números de arriba y el actual
                self.play(Indicate(above_left, color=BLUE, scale_factor=1.2, run_time=0.4))
                self.play(Indicate(above_right, color=BLUE, scale_factor=1.2, run_time=0.4))
                self.play(Indicate(current_num, color=GREEN, scale_factor=1.2, run_time=0.4))
