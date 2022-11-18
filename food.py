from turtle import Turtle
import random

class Food(Turtle):     #Asigna la clase Food

    def __init__(self):          # Define una función
        super().__init__()          
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)   # En esta parte se le asigna un color, tamaño y forma a la comida que saldra en el cuadro grafico
        self.color("white")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)   # En esta parte se asigna en que lugar va a salir la comida, esto por medio de cuadrantes, de esta manera no se va a salir de las medidas dispuestas (-280, 280) 
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)