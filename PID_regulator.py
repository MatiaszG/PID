import re
from tkinter import *
import tkinter as Tk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation

run = False
root = Tk.Tk()
root.title("PID Controller")
root.geometry("750x750")

label1=StringVar()
label1.set("Required value")
labelDir=Label(root, textvariable=label1, height=2)
labelDir.pack()
input = Entry(root)
input.pack()

label2=StringVar()
label2.set("P")
labelDir=Label(root, textvariable=label2, height=2)
labelDir.pack()
p = Entry(root)
p.pack()

label3=StringVar()
label3.set("I")
labelDir=Label(root, textvariable=label3, height=2)
labelDir.pack()
i = Entry(root)
i.pack()

label4=StringVar()
label4.set("D")
labelDir=Label(root, textvariable=label4, height=2)
labelDir.pack()
d = Entry(root)
d.pack()


realValue = 0
iterationTime = 0.2
errorPrior = 0
integral_prior = 0
entryValue = 0
def onClick():
    global run
    print(run)
    if(run == False):
        run = True
    else:
        run = False
    startPid()

def startPid():
    global run
    entryValue = input.get()
    gains = {
        "Kp" : p.get(),
        "Ki" : i.get(),
        "Kd" : d.get()
    }
    for gain in gains:
        if(gains[gain] == ''):
            gains[gain] = 0
    if entryValue == '':
        entryValue = 0
    if run == True:
        controllerPid(int(entryValue), int(gains["Kp"]), int(gains["Ki"]), int(gains["Kd"]))

def controllerPid(entryValue, Kp, Ki, Kd):
    print(Kp)
    global realValue
    global iterationTime
    global errorPrior
    global integral_prior
    if(run):
        err = entryValue - realValue
        integral = integral_prior + err * iterationTime
        derivative = (err - errorPrior ) / iterationTime
        output = Kp*err + Ki*integral + Kd*derivative 
        errorPrior = err
        integral_prior = integral
        realValue += output*0.1
    root.after(int(1000*iterationTime), startPid)
    
startButton = Button(root, text = "Start\Stop", command = onClick)
startButton.pack()
fig = plt.Figure()

axes = [
    fig.add_subplot()]

realValues = []
timeStamps = []
requiredValues = []
def animate(i):
    for ax in axes:
        ax.cla()
    requiredValue = input.get()
    if(requiredValue == ''):
        requiredValue = 0
    print(requiredValue)
    print(realValue)
    realValues.append(realValue)
    timeStamps.append(len(realValues)*iterationTime)
    requiredValues.append(int(requiredValue))
    axes[0].plot(timeStamps, requiredValues)
    axes[0].plot(timeStamps, realValues)
    return 

root2 = Tk.Tk()
label = Tk.Label(root2,text="PID Controller Visualisation").grid(column=0, row=0)   
canvas = FigureCanvasTkAgg(fig, master=root2)
canvas.get_tk_widget().grid(column=0,row=1)
ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), interval=25, blit=False)
Tk.mainloop()
root.mainloop()
