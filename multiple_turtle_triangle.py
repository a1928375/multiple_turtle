import turtle

def detail_1(name):
    name.forward(30)
    name.left(60)

def detail_2(name,n):
    name.left(120)
    name.forward(60)
    name.left(60)
    name.forward(60*n)
    name.right(180)    

def draw_small(name):
    
    for i in range(0,3):
        name.forward(60)
        name.left(120)
    
    detail_1(name)

    for j in range(0,2):
        name.forward(30)
        name.left(120)
    
    detail_1(name)
    name.forward(30)

def draw_medium(name):

    for i in range(0,2):
        draw_small(name)

    detail_2(name,1)
    draw_small(name)

def draw_big():
    window=turtle.Screen()
    window.bgcolor("red")

    brad=turtle.Turtle()
    brad.shape("classic")
    brad.color("blue")
    brad.speed(5)

    draw_medium(brad)
    brad.right(60)
    brad.forward(60)
    brad.left(60)

    draw_medium(brad)
    detail_2(brad,2)

    draw_medium(brad)  

    window.exitonclick()

draw_big()

