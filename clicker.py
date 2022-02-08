import tkinter
window = tkinter.Tk()
string = tkinter.StringVar(value='0')
amount = 0
window.configure(bg = 'grey')
touching = False
lastClicked = 'None'

def changeColor():
    if touching == True:
        pass
    elif amount > 0:
        window.configure(bg = 'green')
    elif amount < 0:
        window.configure(bg = 'red')
    else:
        window.configure(bg = 'grey')

def change(change, button = 'None'):
    global amount
    global lastClicked
    lastClicked = button
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

def doubleClick(event):
    global amount
    match lastClicked:
        case 'Up':
            amount = amount * 3
        case 'Down':
            amount = amount // 3
    string.set(amount)

button1 = tkinter.Button(window)
button1.configure(text='Up', command= lambda: change(amount + 1,'Up'))
button1.pack(ipady=10, fill = 'x', padx = 10, pady = 10)

label = tkinter.Label(window)
label.configure(textvariable=string)
#label.configure(command = lambda: change(amount * -1,'Middle'))
label.pack(ipady=10, ipadx=200, fill = 'x', padx = 10, pady = 10)
label.bind('<Enter>',enter)
label.bind('<Leave>',leave)
label.bind('<Double-Button-1>',doubleClick)



button3 = tkinter.Button(window)
button3.configure(text='Down', command= lambda: change(amount -1,'Down'))
button3.pack(ipady=10, ipadx=200, fill = 'x', padx = 10, pady = 10)



window.mainloop()