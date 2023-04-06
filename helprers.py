from PIL import ImageTk, Image

from canvas1 import frame


def clean():
    frame.delete("screen")


def rock():
    path = 'images/rock.png'
    img = ImageTk.PhotoImage(Image.open(path))
    images_1.append(img)
    return img


def paper():
    path = 'images/paper.png'
    img = ImageTk.PhotoImage(Image.open(path))
    images_1.append(img)
    return img


def scissor():
    path = 'images/scissors.png'
    img = ImageTk.PhotoImage(Image.open(path))
    images_1.append(img)
    return img


images_1 = []