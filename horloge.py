from tkinter import * 
from time import *

def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    days_string = strftime("%A")
    days_label.config(text=days_string)

    date_string = strftime("%B %d,%Y")
    date_label.config(text=date_string)

    time_label.after(1000, update)

    user= str(input("Veuillez entre sleep pour mettre en pause l'horloge"))
    if user == "sleep":
        time.sleep(5)
        

window = Tk()

time_label = Label(window, font=("Arial",50), fg="#00FF00",bg="black")
time_label.pack()

days_label = Label(window, font=("Ink Free",25,"bold"))
days_label.pack()

date_label = Label(window, font=("Ink Free",30))
date_label.pack()

update()

window.mainloop()