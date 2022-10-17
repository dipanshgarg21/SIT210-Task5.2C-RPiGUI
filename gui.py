from tkinter import *
import tkinter.font
import RPi.GPIO as GPIO
from gpiozero import LED
GPIO.setmode(GPIO.BCM)

led1 = LED(14)
led2 = LED(15)
led3 = LED(18)

master = Tk()
master.title("MENU")
myFont = tkinter.font.Font(family = 'Arial' , size = 12, weight = "bold")

var = StringVar()
var.set("LED")

def ledBlink1():
    if led1.is_lit:
        led1.off()
    else:
        led1.on()
        
def ledBlink2():
    if led2.is_lit:
        led2.off()
    else:
        led2.on()

def ledBlink3():        
    if led3.is_lit:
        led3.off()
    else:
        led3.on()
        
def close():
    GPIO.cleanup()
    master.destroy()

Label(master, text = "Choose an LED", font = myFont, padx = 14).pack()
ledButton1 = Radiobutton(master, text = "RED", font = myFont, command = ledBlink1, variable = var, var = "Red").pack(side = LEFT)
ledButton2 = Radiobutton(master, text = "GREEN",font = myFont, command = ledBlink2, variable = var, var = "GREEN").pack(side = LEFT)
ledButton3 = Radiobutton(master, text = "BLUE", font = myFont, command = ledBlink3, variable = var, var = "BLUE").pack(side = LEFT)

exitButton = Button(master, text = 'QUIT', font = myFont, command = close, bg = 'purple', height = 1, width = 13).pack(anchor = "w")

master.protocol("WM_DELETE_MASTER", close)
master.mainloop()




