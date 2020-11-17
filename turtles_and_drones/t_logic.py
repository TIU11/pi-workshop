import turtle
t = turtle.Turtle()
t.shape(“turtle”)
problem = int(input(“What is 3 X 4?”))
if problem == 3*4:
	t.write(str(problem) + ‘ is correct!’)
	t.penup()
	t.backwards(30)
else:
t.write(‘You said ‘ + str(problem) + ‘. I got ‘ + str(3*4))
	t.penup()
	t.backwards(30)
