import turtle
t = turtle.Turtle()
t.shape("turtle")

your_name = input("What's your name?"")
t.penup()
t.forward(40)
t.write("Oh! Hello, " + your_name + "!")
t.backward(10)
