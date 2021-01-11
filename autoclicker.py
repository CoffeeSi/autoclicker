from tkinter import *
import win32gui
root = Tk()

tickrate = Entry(root,width=15,font=("Segoe",16))
StartButton = Button(root,text="Start",width=20,height=5)

tickrate.pack(padx=15, pady=10, expand=1,anchor=NW)
StartButton.pack(padx=15, pady=10, expand=1,anchor=SE)

if __name__=="__main__":
    root.geometry("500x250")
    root.title("AutoClicker")
    root.mainloop()