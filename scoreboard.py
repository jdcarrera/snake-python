from turtle import Turtle

# Centrar scoreboard
ALIGNMENT = "center"

# Estilo de letra del scoreboard
FONT = ("Courier", 24, "normal")

# Instanciamos una clase en la cual estarán definidas funciones
class Scoreboard(Turtle):

    # Se añaden atributos al scoreboard
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    # Organizamos la tabla de puntaje, utilizando las variables previamente inicializadas
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    # Colocar el texto GAME OVER en pantalla, propórcionandole atributos de alineación y fuente
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    # El funcionamiento de la tabla de puntaje, como incrementando en uno la cantidad de puntaje, al momento de perder se reinicia el puntaje, y se actualiza
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()