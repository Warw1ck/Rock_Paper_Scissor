from tkinter import Tk, Canvas
from PIL import ImageTk, Image


def create_root():
    root = Tk()

    root.configure(background='black')
    root.title('Rock Paper Scissors')
    root.resizable(False, False)
    root.geometry("700x600")

    return root


def create_frame():
    frame = Canvas(root, width=700, height=700)
    frame.grid(row=0, column=0)
    frame.configure(bg='#DAF5FF')
    return frame


root = create_root()
frame = create_frame()

