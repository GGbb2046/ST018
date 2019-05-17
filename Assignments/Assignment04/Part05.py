import turtle
def draw_monogram(gal):
    start_x = gal.xcor()
    start_y = gal.ycor()
    start_heading = gal.heading()

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

    gal.setx(start_x)
    gal.sety(start_y)
    gal.setheading(start_heading)
    return

sandbox = turtle.Screen()
sandbox.bgcolor('black')
marker = turtle.Turtle()
marker.pensize(2)
marker.speed(100)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
for i in range(18):
        marker.pencolor(colors[i % 6])
        draw_monogram(marker)
        marker.left(20)
        marker.forward(10)
marker.hideturtle()
sandbox.mainloop()




window = turtle.Screen()
window.mainloop()
