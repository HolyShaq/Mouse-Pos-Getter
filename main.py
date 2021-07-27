from tkinter import *
import pyperclip


def getMouse(event):
    coord = Label(frmCoords, text=f"X: {event.x_root}\tY: {event.y_root}")
    coordLabels.append(coord)
    coord.pack()


def copy(event):
    latest = coordLabels[-1].cget("text").split("\t")
    latest = ", ".join([c[3:] for c in latest])
    pyperclip.copy(latest)


def clear(event):
    for label in coordLabels:
        label.pack_forget()


root = Tk()
frmControls = Frame(root)
frmCoords = Frame(root)
controlA = Label(frmControls, text="Z - Get Position")
controlB = Label(frmControls, text="C - Copy Coordinates")
controlC = Label(frmControls, text="X - Clear Window")
controlA.pack()
controlB.pack()
controlC.pack()

frmControls.grid(column=0, row=0)
frmCoords.grid(column=1, row=0)

coordLabels = []
root.bind("<z>", getMouse)
root.bind("<c>", copy)
root.bind("<x>", clear)
mainloop()
