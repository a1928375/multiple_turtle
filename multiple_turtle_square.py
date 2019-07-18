import turtle

def draw_art():
    window=turtle.Screen()
    window.bgcolor("red")

    brad=turtle.Turtle()
    brad.shape("classic")
    brad.color("yellow")
    brad.speed(25)

    for j in range(0,400):
        for i in range(0,4):
            brad.forward(100)
            brad.right(90)
        brad.right(1)
        print j

    window.exitonclick()

draw_art()
