# Importamos la librería Turtle para diseñar a la serpiente

from turtle import Turtle

# Inicializamos variables que van a guardar las posiciones, distancia de recorrido de la serpiente, y el sistema de movimiento, teniendo en cuenta las medidas dadas 

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 12
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# Instanciamos una clase que tendrá nombre Snake y en ella creamos funciones donde añadiremos atributos a la serpiente, como su color, que figura tendrá, etc

class Snake:

    # Creamos el cuerpo de la serpiente y lo dividimos en segmentos, y esto se encierra en una lista que contiene una tupla, para crear y guardar esos segmentos del cuerpo
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # Definimos en qué posición comenzará a moverse la serpiente, utilizando la variable STARTING_POSITIONS parametrizamos el punto de partida
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    # Añadimos los atributos que tendrá la serpiente, como su forma, color, su posición inicial, y cuando coma se añadirán nuevos segmentos al final del cuerpo, por eso el .append()
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("purple")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    # Se define la posición donde se añadirá el nuevo segmento del cuerpo de la serpiente
    def extend(self):
        self.add_segment(self.segments[-1].position())

    # La definición del cuerpo de la serpiente para que cada segmento se una y se mantenga en la misma posición, teniendo en cuenta la variable MOVE_DISTANCE los segmentos se moveran hacia adelante
    def move(self):
        for seg_num in range(len(self.segments)- 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # Definición de uno de los movimientos del sistema (abajo)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    # Definición de uno de los movimientos del sistema (arriba)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    # Definición de uno de los movimientos del sistema (derecha)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    # Definición de uno de los movimientos del sistema (izquierda)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)