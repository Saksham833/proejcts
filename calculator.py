from cmath import exp
from tkinter import *
expr = ""
def updateSreen():
    label.configure(text=expr)
def onclick(n):
    global expr
    expr += str(n)
    updateSreen()
    print(expr)
def evaluate():
    global expr
    expr = str(eval(expr))
    updateSreen()
def clear():
    global expr
    expr = ""
    updateSreen()
def pop():
    global expr
    expr = list(expr)
    expr.pop()
    expr = ''.join(expr)
operators = ["+","-","*","/"]
root = Tk()
screen = Frame(root,)
label = Label(screen,text=expr)
label.grid(column=0,row=0)
screen.grid(column=0,row=0)
c = 1
r = 1
for i in range(0,10):
    if c == 5:
        c = 0
        r += 1
    btn = Button(root,text=f"{i}",command=lambda x=i:onclick(x))
    btn.grid(column = c,row=r,ipadx=5,ipady=5)
    c += 1
    print(f"{c=} {r=}")

btn = Button(root,text=f"=",command=evaluate)
btn.grid(column = 2,row=2,ipadx=5,ipady=5)
for i in operators:
    if c == 5:
        c = 0
        r += 1
    btn = Button(root,text=f"{i}",command=lambda x=i:onclick(x))
    btn.grid(column = c,row=r,ipadx=5,ipady=5)
    c += 1
    print(f"{c=} {r=}")

btn = Button(root,text=f"cls",command=clear)
btn.grid(column = c,row=r,ipadx=5,ipady=5)

btn = Button(root,text=f"del",command=pop)
btn.grid(column = c,row=r,ipadx=5,ipady=5)

root.mainloop()