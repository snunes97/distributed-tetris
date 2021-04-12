# import tkinter module
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk as ttk

# creating main tkinter window/toplevel
master = tk.Tk()
master.geometry("450x750")
# this wil create a label widget


# grid method to arrange labels in respective
# rows and columns as specified

block = Image.open("imgs/block.png")
blockImg = ImageTk.PhotoImage(block)

wall = Image.open("imgs/wall.png")
wallImg = ImageTk.PhotoImage(wall)

void = Image.open("imgs/void.png")
voidImg = ImageTk.PhotoImage(void)

for col in range(13):
    for row in range(23):

        if col == 0 or col == 12 or row == 0 or row == 22:
            wLabel = tk.Label(master, image=wallImg, pady="0", padx="0", bd=1)
            wLabel.grid(row=row, column=col, sticky=tk.W)

        else:
            vLabel = tk.Label(master, image=voidImg, pady="0", padx="0", bd=1)
            vLabel.grid(row=row, column=col, sticky=tk.W)


# infinite loop which can be terminated by keyboard
# or mouse interrupt
tk.mainloop()