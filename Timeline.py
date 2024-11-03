from manim import *

class TimelineAnimation(Scene):
    def construct(self):
        # Crear puntos para cada siglo desde el XI al XVII
        siglos = ["XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII"]
        
        # Colocación de puntos de los siglos en una línea extendida para cubrir toda la pantalla
        puntos = VGroup(*[Dot() for _ in siglos]).arrange(RIGHT, buff=2)
        puntos.move_to(ORIGIN)  # Centramos en la pantalla

        # Crear línea para conectar los puntos
        linea = Line(start=LEFT * config.frame_width / 2, end=RIGHT * config.frame_width / 2, color=WHITE)
        
        # Añadir etiquetas de números romanos y colocarlas debajo de cada punto
        labels = VGroup(*[Text(s).scale(0.3) for s in siglos])
        for label, punto in zip(labels, puntos):
            label.next_to(punto, DOWN)

        # Añadir elementos a la escena
        self.play(Create(linea), Create(puntos), Write(labels))

        # Crear punto de recorrido y colocarlo inicialmente en el siglo XVII
        punto_recorrido = Dot(color=YELLOW).scale(1.5)
        punto_recorrido.move_to(puntos[-1].get_center())
        self.add(punto_recorrido)

        # Paso 1: Subir
        self.play(punto_recorrido.animate.shift(UP * 0.5), run_time=0.5)

        # Paso 2: Moverse horizontalmente hacia la izquierda
        recorrido = [punto.get_center() + UP * 0.5 for punto in puntos[::-1]]
        self.play(
            *[punto_recorrido.animate.move_to(pos) for pos in recorrido],
            run_time=3, rate_func=smooth
        )

        # Paso 3: Bajar
        self.play(punto_recorrido.animate.shift(DOWN * 0.5), run_time=0.5)

        self.wait(1)
