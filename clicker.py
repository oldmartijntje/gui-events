import tkinter
window = tkinter.Tk()
string = tkinter.StringVar(value='0')
amount = 0
window.configure(bg = 'grey')
touching = False

def changeColor():
    if touching == True:
        pass
    elif amount > 0:
        window.configure(bg = 'green')
    elif amount < 0:
        window.configure(bg = 'red')
    else:
        window.configure(bg = 'grey')

def change(change):
    global amount
    amount = change
    string.set(amount)
    changeColor()

def enter(event):
    global touching
    touching = True
    window.configure(bg = 'yellow')

def leave(event):
    global touching
    touching = False
    changeColor()

button1 = tkinter.Button(window)
button1.configure(text='Up', command= lambda: change(amount + 1))
button1.pack(ipady=10, fill = 'x', padx = 10, pady = 10)

button2 = tkinter.Button(window)
button2.configure(textvariable=string,command = lambda: change(amount * -1))
button2.pack(ipady=10, ipadx=200, fill = 'x', padx = 10, pady = 10)
button2.bind('<Enter>',enter)
button2.bind('<Leave>',leave)



button3 = tkinter.Button(window)
button3.configure(text='Down', command= lambda: change(amount -1))
button3.pack(ipady=10, ipadx=200, fill = 'x', padx = 10, pady = 10)



window.mainloop()