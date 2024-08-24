from tkinter import*
import time

WIDTH =500
HEIGHT =500

xVelocity = 1
yVelocity =1

window = Tk()

canvas= Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

photo=PhotoImage(file="C:\\Users\\abdis\\OneDrive\\Desktop\\UFO.png")

my_image = canvas.create_image(0,0,image=photo, anchor=NW)
while True:
    coordinates = canvas.coords(my_image)
    print(coordinates)
    canvas.move(my_image,xVelocity,0)
    window.update()
    time.sleep(0.01)



window.mainloop()