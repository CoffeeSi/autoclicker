from tkinter import *
root = Tk()

delay = StringVar()
delay.set("100")

def CheckInt():
    try:
        int(tickrate.get())
        StartProcess()
    except ValueError:
        WarnLabel.config(text="Enter the number")

def StartProcess():
    try:
        if StartButton["text"] == "Start":
            tickrate.config(state=DISABLED)
            ActionButton.config(state=DISABLED)
            WarnLabel.config(text="")
            StartButton.config(text="Stop")
        elif StartButton["text"] == "Stop":
            tickrate.config(state=NORMAL)
            ActionButton.config(state=NORMAL)
            WarnLabel.config(text="")
            StartButton.config(text="Start")

    except:
        pass

tickrate = Entry(root,width=15,font=("Arial",16),textvariable=delay)
StartButton = Button(root,text="Start",width=15,height=4,command=CheckInt)
ActionButton = Button(root,text="Press (the Button)",width=25,height=4)
millisec = Label(root,text="ms",font=("Arial",16))
WarnLabel = Label(root,font=("Arial",16))

tickrate.place(relx=0.03,rely=0.05)
StartButton.place(relx=0.65,rely=0.62)
ActionButton.place(relx=0.03,rely=0.22)
millisec.place(relx=0.55,rely=0.04)
WarnLabel.place(relx=0.03,rely=0.6)

if __name__=="__main__":
    root.geometry("350x200")
    root.title("AutoClicker")
    root.resizable(False,False)
    root.mainloop()