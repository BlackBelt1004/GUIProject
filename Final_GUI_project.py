import tkinter
import random
from tkinter import * 
from tkinter import messagebox as mb
main_window = tkinter.Tk()
main_window.geometry('350x500')
guestCount = 0

def call():
    global guestCount    
    global output_field    
    
    res = mb.askquestion('Clear', 'Are you sure you want to clear')
    if res == 'yes':
        guestCount = 0
        output_field.config(text = guestCount)
    else:
        mb.showinfo('return', 'Returning to guest count')  
def count_one_guest():    
    global guestCount    
    global output_field   
    global scal
    
    guestCount += 1    
    output_field.config(text=guestCount)
    my_odds = scal.get()
    n = random.random()
    if n < (1/my_odds):
        pop_up = tkinter.messagebox.showinfo("You have won!","You win a new Car")
def remove_one_guest():
    global guestCount
    global output_field
    
    guestCount-=1
    output_field.config(text=guestCount)
def count_five_guests():    
    global guestCount    
    global output_field    
    
    guestCount +=5    
    output_field.config(text=guestCount)
    
main_window.title("Party Guest Counter")
main_window.geometry('400x300')

frame = tkinter.Frame(main_window)
frame.grid()
    
output_label = tkinter.Label(frame, text="Guest count: ", font=('sans-serif', 18, 'bold'))
output_label.grid(row=0, column=0)
    
output_field = tkinter.Label(frame, text=guestCount, font=('sans-serif', 18, 'bold'))
output_field.grid(row=0, column=1)

plus_one = tkinter.Button(frame, text="+1", command=count_one_guest)
plus_one.grid(row=1,  columnspan=2)

minus_one = tkinter.Button(frame, text = "-1", command=remove_one_guest)
minus_one.grid(row=2, columnspan=2)

plus_five = tkinter.Button(frame, text="+5", command=count_five_guests)
plus_five.grid(row=3, columnspan=2)

clear = tkinter.Button(frame, text="Clear", command=call)
clear.grid(row=6, column=3)

scal = Scale(frame)
scal.grid(row = 2,column = 3 )

def keyPressed(event):    
    event_desc = event.char    
    if event.keysym == "Return":        
        event_desc = "<Return>"    
    elif event.keysym == "space":        
        event_desc = "<space>"    
    print("You pressed ", event_desc)
frame.bind_all("a", keyPressed)
frame.bind_all("b", keyPressed)
frame.bind_all("<Return>", keyPressed)
frame.bind_all("<space>", keyPressed)
frame.mainloop()