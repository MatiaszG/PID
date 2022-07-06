from tkinter import *
import tkinter as Tk
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = Tk.Tk()
root.title("PID regulator parameters")
root.geometry("750x750+800+100")
fig = plt.Figure()

ax = fig.add_subplot()

realValues = []
timeStamps = []
requiredValues = []


def animate(i):
    ax.cla()
    requiredValue = input.get()
    if(requiredValue == ''):
        requiredValue = 0
    realValues.append(realValue)
    timeStamps.append(len(realValues)*iterationTime)
    requiredValues.append(int(requiredValue))
    ax.plot(timeStamps, requiredValues)
    ax.plot(timeStamps, realValues)
    ax.set_xlabel('Time [s]')
    ax.set_ylabel('Value [-]')
    ax.legend(['Setpoint', 'Measured value'], loc = 2)
    return


root2 = Tk.Tk()
root2.title("PID regulator visualization")
root2.geometry("750x750+0+100")
root2.configure(background='white')
canvas = FigureCanvasTkAgg(fig, master=root2)
canvas.get_tk_widget().grid(column=0, row=1)
ani = animation.FuncAnimation(fig, animate, interval=300)

label1 = StringVar()
label1.set("Setpoint")
labelDir = Label(root, textvariable=label1, height=2)
labelDir.pack()
input = Entry(root)
input.pack()

label2 = StringVar()
label2.set("P")
labelDir = Label(root, textvariable=label2, height=2)
labelDir.pack()
p = Entry(root)
p.pack()

label3 = StringVar()
label3.set("I")
labelDir = Label(root, textvariable=label3, height=2)
labelDir.pack()
i = Entry(root)
i.pack()

label4 = StringVar()
label4.set("D")
labelDir = Label(root, textvariable=label4, height=2)
labelDir.pack()
d = Entry(root)
d.pack()

run = False
realValue = 0.0
iterationTime = 0.3
errorPrior = 0.0
integralPrior = 0.0
entryValue = 0.0


def onClick():
    global run
    if(run == False):
        run = True
    else:
        run = False
    controllerPid()


def controllerPid():
    global run
    if(run):
        global realValue
        global iterationTime
        global errorPrior
        global integralPrior
        entryValue = input.get()
        gains = {
            "Kp": p.get().replace(',', '.'),
            "Ki": i.get().replace(',', '.'),
            "Kd": d.get().replace(',', '.')
        }
        for gain in gains:
            if(gains[gain] == ''):
                gains[gain] = 0.0
        if entryValue == '':
            entryValue = 0.0
        err = float(entryValue) - realValue
        integral = integralPrior + err * iterationTime
        derivative = (err - errorPrior) / iterationTime
        output = float(gains['Kp'])*err + float(gains['Ki']) * \
            integral + float(gains['Kd'])*derivative
        errorPrior = err
        integralPrior = integral
        realValue += output
        root.after(int(1000*iterationTime), controllerPid)
    else:
        return


startButton = Button(root, text="Start\Stop", command=onClick)
startButton.pack()

Tk.mainloop()
