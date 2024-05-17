import turtle as tu

tu.bgcolor('black')
tu.color('white')

tu.pensize(10)
tu.speed(20)

screen = tu.Screen()

tu.penup()
tu.goto(x=-440, y=375)
tu.pendown()

tu.right(90)
tu.forward(200)
tu.right(180)
tu.forward(100)
tu.right(90)
tu.forward(100)
tu.right(90)
tu.forward(100)
tu.right(180)
tu.forward(200)

 #H is finished


tu.penup()
tu.goto(x=-280, y=375)
tu.pendown()

tu.right(180)
tu.forward(200)
tu.right(180)
tu.forward(200)
tu.right(90)
tu.forward(100)
tu.right(180)
tu.forward(100)
tu.left(90)
tu.forward(100)
tu.right(270)
tu.forward(80)
tu.right(180)
tu.forward(80)
tu.left(90)
tu.forward(100)
tu.left(90)
tu.forward(100)

#E is finished

tu.penup()
tu.goto(x=-140, y=375)
tu.pendown()
tu.right(90)
tu.forward(200)
tu.left(90)
tu.forward(120)

#L is finished

tu.penup()
tu.goto(x=20, y=375)
tu.pendown()
tu.right(90)
tu.forward(200)
tu.left(90)
tu.forward(120)

#L is finished

tu.penup()
tu.goto(x=240, y=160)
tu.pendown()

tu.circle(radius=120, extent=360, steps=60)

#O is finished, HELLO is finished

tu.penup()
tu.goto(x=-465, y=75)
tu.pendown()

tu.right(60)
tu.forward(175)
tu.left(140)
tu.forward(165)
tu.right(155)
tu.forward(165)
tu.left(135)
tu.forward(175)

#W is finished

tu.penup()
tu.goto(x=10, y=-50)
tu.pendown()

tu.circle(radius=120, extent=360, steps=60)

#O is finished

tu.penup()
tu.goto(x=60, y=-20)
tu.pendown()


tu.right(150)
tu.forward(100)


tu.right(180)
tu.forward(165)


tu.right(135)
tu.forward(10)


tu.circle(radius=70, extent=350, steps=90)

tu.forward(205)

#R is finished

tu.penup()
tu.goto(x=220, y=115)
tu.pendown()

tu.right(35)
tu.forward(230)

tu.left(90)
tu.forward(110)

#L is finished

tu.penup()
tu.goto(x=355, y=115)
tu.pendown()

tu.right(90)
tu.forward(225)
tu.left(90)
tu.circle(radius=120, extent=90, steps=90)

tu.penup()
tu.goto(x=355, y=115)
tu.pendown()

tu.right(90)
tu.circle(radius=-120, extent=90, steps=90)

#HELLO WORLD is finished
screen.mainloop()
