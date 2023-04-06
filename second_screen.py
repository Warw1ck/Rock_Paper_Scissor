from PIL import ImageTk, Image
from tkinter import Button, PhotoImage
from canvas1 import frame, root
from helprers import clean, paper, scissor, rock
from third_screen import fight


def chose_r_p_s():
    clean()
    rock_button = Button(
        root,
        image=rock(),
        bd=0,
        bg='#DAF5FF',
        activebackground='#DAF5FF',
        command=lambda: fight(1)
    )
    scissor_button = Button(
        root,
        image=scissor(),
        bd=0,
        bg='#DAF5FF',
        activebackground='#DAF5FF',
        command=lambda: fight(3)
    )
    paper_button = Button(
        root,
        image=paper(),
        bd=0,
        bg='#DAF5FF',
        activebackground='#DAF5FF',
        command=lambda: fight(2)
   )
    frame.create_window(120, 270, window=rock_button, tag="screen")
    frame.create_window(340, 270, window=paper_button, tag="screen")
    frame.create_window(560, 270, window=scissor_button, tag="screen")


