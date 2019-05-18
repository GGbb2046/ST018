import turtle
def draw_monogram(gal):
    
    #draw a G
    gal.fd(50)
    gal.rt(90)
    gal.fd(50)
    gal.rt(90)
    gal.fd(75)
    gal.rt(45)
    gal.fd((1250)**(1/2))
    gal.rt(45)
    gal.fd(50)
    gal.rt(45)
    gal.fd((1250)**(1/2))
    gal.rt(45)
    gal.fd(75)
    #draw a B
    gal.up()
    gal.fd(50)
    gal.down()
    gal.fd(50)
    gal.rt(45)
    gal.fd((1250)**(1/2))
    gal.rt(45)
    gal.fd(50)
    gal.rt(45)
    gal.fd((1250)**(1/2))
    gal.rt(45)
    gal.fd(50)
    gal.rt(90)
    gal.fd(100)
    gal.up()
    gal.rt(90)
    gal.fd(75)
    gal.rt(90)
    gal.fd(50)
    gal.down()
    gal.rt(90)
    gal.fd(75)

    
    return

sandbox = turtle.Screen()
sandbox.bgcolor('black')
marker = turtle.Turtle()
marker.pensize(2)
marker.speed(0)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
for i in range(200):
        marker.pencolor(colors[i % 6])
        draw_monogram(marker)
        marker.left(1)
        marker.penup()
        marker.fd(50)
        marker.pd()
        marker.forward(50)
        marker.penup()
        marker.fd(150)
        marker.pd()
        marker.forward(40)
marker.hideturtle()
sandbox.mainloop()




window = turtle.Screen()
window.mainloop()
