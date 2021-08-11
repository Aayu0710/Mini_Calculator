from tkinter import *
root = Tk()
root.geometry("500x700")
root.title("My first calculator")
#root.colormapwindows()
def click(event):
    global scval
    text = event.widget.cget("text")
    # Above is for capture the value of button clicked
    print(text)
    if text=="=":
        if scval.get().isdigit():
            value = int(scval.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                value = "Error"


        scval.set(value)
        screen.update()
    elif text=="c":
        scval.set("")# It will blank the screen
        screen.update()
    else:
        scval.set(scval.get()+text)# This will display the clicked text in on the screen
        screen.update()# It will update the screen



scval = StringVar()
scval.set("")
# First we will make a screen where user can write the entry
screen = Entry(root, textvar=scval, font="lucida 40", bg='white')
screen.pack(padx=30, pady=10)
# Inside the root we create a frame
f = Frame(root, bg="light green")
# Inside the frame we will create a button
# This is for top 3 button
b = Button(f, text="9", font="lucida 30 italic",bg="yellow", relief=GROOVE, borderwidth=5)
# I will bind this button with an event
b.pack(side=LEFT, padx=40, pady=10)
b.bind("<Button-1>", click)
b = Button(f, text="8", font="lucida 30 italic", bg="yellow", relief=GROOVE, borderwidth=5)
b.pack(side=LEFT, padx=40)
b.bind("<Button-1>", click)
b = Button(f, text="7", font="lucida 30 italic", bg="yellow", relief=GROOVE, borderwidth=5)
b.pack(side=LEFT, padx=40)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="green")
# Inside the frame we will create a button
# This is for top 3 button
b = Button(f, text="6", font="lucida 30 italic", bg="yellow", relief=GROOVE, borderwidth=5)
# I will bind this button with an event
b.pack(side=LEFT, padx=40, pady=10)
b.bind("<Button-1>", click)
b = Button(f, text="5", font="lucida 30 italic", bg="yellow", relief=GROOVE, borderwidth=5)
b.pack(side=LEFT, padx=40)
b.bind("<Button-1>", click)
b = Button(f, text="4", font="lucida 30 italic", bg="yellow", relief=GROOVE, borderwidth=5)
b.pack(side=LEFT, padx=40)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="light green")
# Inside the frame we will create a button
# This is for top 3 button
b = Button(f, text="3", font="lucida 30 italic", bg="yellow", relief=GROOVE, borderwidth=5)
# I will bind this button with an event
b.pack(side=LEFT, padx=40, pady=10)
b.bind("<Button-1>", click)
b = Button(f, text="2", font="lucida 30 italic", bg="yellow", relief=GROOVE, borderwidth=5)
b.pack(side=LEFT, padx=40)
b.bind("<Button-1>", click)
b = Button(f, text="1", font="lucida 30 italic", bg="yellow", relief=GROOVE, borderwidth=5)
b.pack(side=LEFT, padx=40)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="green")
# Inside the frame we will create a button
# This is for top 3 button
b = Button(f, text="0", font="lucida 30 italic", bg='yellow', relief=GROOVE, borderwidth=5)
# I will bind this button with an event
b.pack(side=LEFT, padx=40.51, pady=10)
b.bind("<Button-1>", click)
b = Button(f, text="-", font="lucida 30 italic", bg='yellow', relief=GROOVE, borderwidth=5)
b.pack(side=LEFT, padx=40.51)
b.bind("<Button-1>", click)
b = Button(f, text="+", font="lucida 30 italic", bg='yellow', relief=GROOVE, borderwidth=5)
b.pack(side=LEFT, padx=40.51)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="light green")
# Inside the frame we will create a button
# This is for top 3 button
b = Button(f, text="*", font="lucida 30 italic", bg="yellow", relief=GROOVE, borderwidth=5)
# I will bind this button with an event
b.pack(side=LEFT, padx=40.5, pady=10)
b.bind("<Button-1>", click)
b = Button(f, text="/", font="lucida 30 italic", bg="yellow", relief=GROOVE, borderwidth=5)
b.pack(side=LEFT, padx=40.2)
b.bind("<Button-1>", click)
b = Button(f, text="%", font="lucida 30 italic", bg="yellow", relief=GROOVE, borderwidth=5)
b.pack(side=LEFT, padx=40.2)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="green")
# Inside the frame we will create a button
# This is for top 3 button
b = Button(f, text="=", font="lucida 30 italic", bg="yellow", relief=GROOVE, borderwidth=5)
# I will bind this button with an event
b.pack(side=LEFT, padx=41.6, pady=10)
b.bind("<Button-1>", click)
b = Button(f, text="c", font="lucida 30 italic", bg="yellow", relief=GROOVE, borderwidth=5)
b.pack(side=LEFT, padx=42)
b.bind("<Button-1>", click)
b = Button(f, text=".", font="lucida 30 italic", bg="yellow", relief=GROOVE, borderwidth=5)
b.pack(side=LEFT, padx=42)
b.bind("<Button-1>", click)
f.pack()
root.mainloop()