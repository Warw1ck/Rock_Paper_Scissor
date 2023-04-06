from tkinter import Button, font
from PIL import ImageTk, Image
from canvas1 import root, frame
from second_screen import chose_r_p_s


def app_icon():
    path = 'images/4144572.png'
    img = ImageTk.PhotoImage(Image.open(path))
    images.append(img)
    frame.create_image(300, 344, image=img, tag="screen")


def render_start():
    app_icon()
    myfont = font.Font(weight="bold")
    start_button = Button(
        root,
        text='Play',
        bg='#FEFF86',
        fg='#2D2727',
        borderwidth=0,
        width=7,
        height=2,
        command=chose_r_p_s
    )
    start_button['font'] = myfont
    frame.create_window(500, 100, window=start_button, tag="screen")


images = []