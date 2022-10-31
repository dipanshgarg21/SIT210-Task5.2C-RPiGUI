#Libraries
from tkinter import *
import tkinter.font
import RPi.GPIO as GPIO
from gpiozero import LED

#Initializing the GPIO pins
GPIO.setmode(GPIO.BCM)
led1 = LED(14)
led2 = LED(15)
led3 = LED(18)

#Creating an instance of tkinter
master = Tk()

#Initial setup of the window
master.title("MENU")
myFont = tkinter.font.Font(family = 'Arial' , size = 12, weight = "bold")
master.eval('tk::PlaceWindow . center')

#Restricting the size of the window
master.minsize(600,300)
master.maxsize(600,300)

v = StringVar()

#Creating the functions for the functionality behind the radio buttons
def ledBlink1():
    if led1.is_lit:
        led1.off()
    else:
        led1.on()
        led2.off()
        led3.off()
    print("led1")
    myLabel.config(text = v.get())
        
def ledBlink2():
    if led2.is_lit:
        led2.off()
    else:
        led1.off()
        led2.on()
        led3.off()
    print("led2")
    myLabel.config(text = v.get())

def ledBlink3():        
    if led3.is_lit:
        led3.off()
    else:
        led1.off()
        led2.off()
        led3.on()
    print("led3")
    myLabel.config(text = v.get())

#A function to quit
def close():
    GPIO.cleanup()
    master.destroy()
    print("cleanup")

#Widgets
Label(master, text = "** CHOOSE A LED **", font = myFont, padx = 14).pack()
Radiobutton(master, text = "RED", font = myFont, command = ledBlink1, bg="red", bd = 3, variable = v, value = "LED: Red", cursor = "dot").pack(fill=X, ipady = 10, pady = 5)
Radiobutton(master, text = "GREEN",font = myFont, command = ledBlink2, bg="green", bd = 3, variable = v, value = "LED: Green", cursor = "dot").pack(fill=X, ipady = 10, pady = 5)
Radiobutton(master, text = "BLUE", font = myFont, command = ledBlink3, bg="blue", bd = 3, variable = v, value = "LED: Blue", cursor = "dot").pack(fill=X, ipady = 10, pady = 5)
myLabel = Label(master, text = "LED: NONE", font = myFont)
myLabel.pack(pady = 10)
Button(master, text = 'QUIT', font = myFont, command = close, bg = 'purple', height = 2, width = 15, cursor = "target").pack(anchor = NE, pady = 5, padx = 20)

#Enabling cross protocol to do the same function as the quit button
master.protocol("WM_DELETE_WINDOW", close)

#So as to put the window's functionality in a loop
master.mainloop()
