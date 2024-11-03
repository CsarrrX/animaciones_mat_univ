from manim import *

class PascalBinaryTriangle(Scene):
    def construct(self):
        # Función para generar una fila del triángulo de Pascal
        def pascal_row(n):
            row = [1]
            for k in range(1, n + 1):
                row.append(row[-1] * (n - k + 1) // k)
            return row

        # Función para reemplazar números del triángulo de Pascal con 1 y 0
        def replace_with_binary(row):
            return [1 if num % 2 == 0 else 0 for num in row]

        # Crear filas del triángulo de Pascal
        rows = 16  # Número de filas a mostrar
        triangle = VGroup()
        for i in range(rows):
            row_values = pascal_row(i)
            binary_values = replace_with_binary(row_values)
            row_group = VGroup()

            for num in binary_values:
                if num == 1:
                    number_tex = MathTex("1").set_color(GREEN).scale(0.3)  # Color verde para 1
                else:
                    number_tex = MathTex("0").set_color(BLUE).scale(0.3)  # Color azul para 0
                row_group.add(number_tex)

            row_group.arrange(RIGHT, buff=0.3).shift(DOWN * i * 0.5)  # Ajuste vertical de las filas
            triangle.add(row_group)

        # Asegurarse de que la primera fila contenga el cero
        zero_tex = MathTex("0").set_color(BLUE).scale(0.3)  # Primer número como 0
        row_group = VGroup(zero_tex)
        row_group.arrange(RIGHT, buff=0.3).shift(DOWN * 0.5)  # Ajustar posición
        triangle.add(row_group)

        # Posicionar el triángulo en el centro
        triangle.move_to(ORIGIN)

        # Mostrar filas del triángulo de Pascal con FadeIn
        for row in triangle:
            self.play(FadeIn(row), run_time=0.5)

        self.wait(2)  # Esperar un momento al final de la animación

        # Mover el triángulo de Pascal a la izquierda
        self.play(triangle.animate.shift(LEFT * 3))

        # Crear y animar el triángulo de Sierpinski
        sierpinski_triangle = self.create_sierpinski_triangle(5)
        sierpinski_triangle.scale(2)  # Hacer el triángulo de Sierpinski más grande
        sierpinski_triangle.move_to(RIGHT * 3)  # Mover el triángulo de Sierpinski a la derecha
        self.play(FadeIn(sierpinski_triangle), run_time=2)

        self.wait(3)  # Esperar un momento al final de la animación

    def create_sierpinski_triangle(self, n):
        """Crea un triángulo de Sierpinski de n niveles."""
        triangle = Polygon(ORIGIN, 3 * UP + 1.5 * LEFT, 3 * UP + 1.5 * RIGHT, color=WHITE)
        triangle.set_fill(BLACK, opacity=1)
        triangles = [triangle]

        for _ in range(n):
            new_triangles = []
            for tri in triangles:
                # Obtener los vértices del triángulo
                vertices = tri.get_vertices()
                # Crear los 3 subtriángulos
                mid1 = (vertices[0] + vertices[1]) / 2
                mid2 = (vertices[1] + vertices[2]) / 2
                mid3 = (vertices[0] + vertices[2]) / 2

                new_triangles.append(Polygon(vertices[0], mid1, mid3, color=WHITE))
                new_triangles.append(Polygon(mid1, vertices[1], mid2, color=WHITE))
                new_triangles.append(Polygon(mid3, mid2, vertices[2], color=WHITE))

            triangles = new_triangles

        return VGroup(*triangles)

