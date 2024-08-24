from tkinter import*
import time

WIDTH =500
HEIGHT =500

window = Tk()

canvas= Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

photo=PhotoImage(file="C:\\Users\\abdis\\OneDrive\\Desktop\\UFO.png")

my_image = canvas.create_image(0,0,image=photo, anchor=NW)



window.mainloop()