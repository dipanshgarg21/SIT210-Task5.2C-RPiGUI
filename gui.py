from tkinter import *
import tkinter.font
import RPi.GPIO as GPIO
from gpiozero import LED
GPIO.setmode(GPIO.BOARD)

led1 = LED(14)
led2 = LED(15)
led3 = LED(18)

master = Tk()
master.title("MENU")
myFont = tkinter.font.Font(family = 'Helvetica' , size = 12, weight = "bold")

def ledBlink1():
    if led1.is_lit:
        led1.off()
        ledButton1["text"] = "LED: SWITCH ON"
    else:
        led1.on()
        ledButton1["text"] = "LED: SWITCH OFF"
        
def ledBlink2():
    if led2.is_lit:
        led2.off()
        ledButton2["text"] = "LED: SWITCH ON"
    else:
        led2.on()
        ledButton2["text"] = "LED: SWITCH OFF"

def ledBlink3():        
    if led3.is_lit:
        led3.off()
        ledButton3["text"] = "LED: SWITCH ON"
    else:
        led3.on()
        ledButton3["text"] = "LED: SWITCH OFF"

def close():
    GPIO.cleanup()
    master.destroy()

ledButton1 = Button(master, text = 'LED: SWITCH ON', font = myFont, command = ledBlink1, bg = 'blue', height = 2, width = 30)
ledButton1.grid(row=0, column=1)

ledButton2 = Button(master, text = 'LED: SWITCH ON', font = myFont, command = ledBlink2, bg = 'green', height = 2, width = 30)
ledButton2.grid(row=1, column=1)

ledButton3 = Button(master, text = 'LED: SWITCH ON', font = myFont, command = ledBlink3, bg = 'red', height = 2, width = 30)
ledButton3.grid(row=2, column=1)

exitButton = Button(master, text = 'QUIT', font = myFont, command = close, bg = 'purple', height = 1, width = 13)
exitButton.grid(row=3, column=1)

master.protocol("WM_DELETE_WINDOW", close)
master.mainloop()
