from tkinter import Button
from canvas1 import frame, root
from helprers import clean, rock, paper, scissor
from random import randint
import second_screen


def fight(number):
    clean()
    elements = {1: rock(), 2: paper(), 3: scissor()}
    n = randint(1, 3)

    if number == n:
        text = 'You Tied'
    elif (number == 1 and n == 2) or (number == 2 and n == 3) or (number == 3 and n == 1):
        text = 'You Lose'
    else:
        text = 'You Win'

    play_again = Button(
        root,
        text='Again?',
        bg='#FEFF86',
        fg='#2D2727',
        font=('Helvetica 15', 20, 'bold'),
        borderwidth=0,
        width=7,
        height=2,
        command=second_screen.chose_r_p_s
    )

    frame.create_image(120, 270, image=elements[number], tag="screen")
    frame.create_image(560, 270, image=elements[n], tag="screen")
    frame.create_text(360, 150, text=text, fill="#413543", font=('Helvetica 15', 37,  'bold'), tag="screen")
    frame.create_window(340, 270, window=play_again, tag="screen")


