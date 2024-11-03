from manim import *

class PascalTriangle(Scene):
    def construct(self):
        # Función para generar una fila del triángulo de Pascal
        def pascal_row(n):
            row = [1]
            for k in range(1, n + 1):
                row.append(row[-1] * (n - k + 1) // k)
            return row

        # Crear filas del triángulo de Pascal
        rows = 8  # Cambia este valor para el número de filas que deseas mostrar
        triangle = VGroup()
        for i in range(rows):
            row_values = pascal_row(i)
            row_group = VGroup(*[MathTex(str(num)).scale(0.6) for num in row_values])  # Aumentar tamaño de los números
            row_group.arrange(RIGHT, buff=0.3).shift(DOWN * i * 0.5)  # Disminuye el espaciado entre filas
            triangle.add(row_group)

        # Posicionar triángulo en el centro
        triangle.move_to(ORIGIN)

        # Mostrar filas del triángulo de Pascal con FadeIn
        for row in triangle:
            self.play(FadeIn(row), run_time=0.5)

        # Agregar índices sobre cada fila, alineados a la derecha del último número
        indices = []
        for i, row in enumerate(triangle):
            index = MathTex(str(i), color=YELLOW).scale(0.3)
            index.next_to(row, UP + RIGHT * 0.1, buff=0.1)  # Ajuste de posición relativo al último número
            indices.append(index)  # Guardar índices en una lista
            self.play(FadeIn(index))

        # Animar el FadeOut de todos los índices al mismo tiempo
        self.play(*[FadeOut(index) for index in indices], run_time=1)

        # Esperar 10 segundos antes de mover el triángulo
        self.wait(10)

        # Mover el triángulo hacia la izquierda
        self.play(triangle.animate.shift(LEFT * 2), run_time=1)

        # Añadir la suma de los elementos a cada fila a la derecha
        for row in triangle:
            # Calcular la suma de la fila
            row_values = [int(num.get_tex_string()) for num in row]  # Obtener el texto de cada número
            suma = sum(row_values)  # Calcular la suma
            suma_tex = MathTex("=", str(suma)).scale(0.6)  # El signo igual y la suma
            suma_tex.next_to(row, RIGHT, buff=0.3)  # Colocar a la derecha de la fila
            self.play(FadeIn(suma_tex))  # Mostrar la suma

        self.wait(2)  # Esperar un momento antes de finalizar

