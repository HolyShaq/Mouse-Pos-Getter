from tkinter import *


def getMouse(event):
    coord = Label(frmCoords, text=f"X: {event.x_root}\tY: {event.y_root}")
    labels.append(coord)
    coord.pack()


def clear(event):
    for label in labels:
        label.pack_forget()


root = Tk()
frmControls = Frame(root)
frmCoords= Frame(root)
controlA = Label(frmControls, text="Q - Get Position")
controlB = Label(frmControls, text="C - Copy Coordinates")
controlC = Label(frmControls, text="X - Clear Window")
controlA.pack()
controlB.pack()
controlC.pack()

frmControls.grid(column=0, row=0)
frmCoords.grid(column=1, row=0)

labels = []
root.bind("<q>", getMouse)
root.bind("<x>", clear)
mainloop()
