from tkinter import *


def getMouse(event):
    coord = Label(root, text=f"X: {event.x_root}\tY: {event.y_root}")
    labels.append(coord)
    coord.pack()


def clear(event):
    for label in labels:
        label.pack_forget()


root = Tk()
labels = []
root.bind("<q>", getMouse)
root.bind("<c>", clear)
mainloop()
