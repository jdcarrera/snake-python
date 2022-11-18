#TRABAJO EN CLASE REALIZADO POR : Juan Diego Carrera Laverde y Kevin José Cáceres Hernández por falta de equipos funcionales.

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen() #La función screen sebe usarse como herramienta al hacer graficos en la libreria turtle.
screen.setup(width=600, height=600)  #De la linea 8 hasta la 11 asignamos un color, nombre y tamaño al cuadro gráfico
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()       #Asignamos los nombres a los objetos que irán dentro del cuadro grafico
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")      #En está parte asignamos el sistema de movimientos de la serpiente los cuales seran hacia arriba, abajo, derecha e izquierda. 
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True  #Esta función aplica para que cuando el juego se inicie

while game_is_on:       # Cuando el juego se active,  
    screen.update()     # La ventaja se abrira
    time.sleep(0.1)     # Y la velocidad con la que la serpiente inicie será con 0.1 mili segundos
    snake.move()        # En esta parte se asigna el movimiento a la serpiente

    #Detect collision with food.
    
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()              # Llama la instancia "snake" para que cuando colisione con la comida el score incremente
        scoreboard.increase_score()


    #Detect collision with wall.

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor()> 280 or snake.head.ycor() < -280:
        game_is_on = False          # Esta función se utiliza para devolver la coordenada x de la serpiente de la posición actual de la serpiente.  requiere los argumentos expuestos en la linea 40.
        scoreboard.game_over()      

    #Detect collision with tail.
    for segment in snake.segments:
        if segment == snake.head:        # Está parte ayuda a que la serpiente crezca cada vez que el score incremente
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()     #Esta parte ayuda a poder salir de el juego al cerrar la ventana.