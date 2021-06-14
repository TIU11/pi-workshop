# Rock Paper Scissors Game

from guizero import *
import random

possible_answers = ['rock','paper','scissors']

def rock():
    comp_answer = random.choice(possible_answers)
    if comp_answer == 'rock' :
        result.value = "Tie"
    elif comp_answer == 'paper':
        result.value = 'You lose, sorry!'
    else:
        result.value = 'You win. Yay!'
    comp_result.value = "Computer picked " + comp_answer

app = App()

title_label = Text(app, text = "What is your choice?")
layout = Box(app, layout = 'grid', grid=[2,1])

rock_btn = PushButton(layout, text = "Rock", command = rock, grid = [1,2])
paper_btn = PushButton(layout, text = "Paper", grid = [2,2])
scissors_btn = PushButton(layout, text = "Scissors", grid = [3,2])

result = Text(app)
comp_result = Text(app)
app.display()
