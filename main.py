from tkinter import *

# importing Mycolors class from mycolors module
from mycolors import Mycolor

# making object of Mycolor Class so that we can access all the variables and methods of Mycolor
obj = Mycolor()

root = Tk()
root.geometry("1200x500")
root.title("Temperature Convertor")
root.config(bg='#ADE4DB')


colordict = {round(35.0 + i/10, 1): obj.colorlist[i] for i in range(len(obj.colorlist))}


def myplus():
    c = cel.cget("text")
    c = c + 0.1
    c1 = round(c,1)
    cel.config(text=c1)
    print(f"{c1} =", end=" ")
    #c.after(200,myplus)
    
    thiscolor = colordict[c1]
    label1.config(bg=thiscolor)
    #print(thiscolor)
    
    f = c1 *1.8+32
    f1 = round(f,1)
    far.config(text=f1)
    print(f1)


def myminus():
    cm = cel.cget('text')
    cm1 = round((cm - 0.1), 2)
    cel.config(text=cm1)
    print(f'{cm1} =',end=" ")
    
     
    thiscolor = colordict[cm1]
    label1.config(bg=thiscolor)
   
    
    fm = cm1 *1.8+32
    fm1 = round(fm,3)
    far.config(text=fm1)
    print(fm1)

    
label1 = Label(root, bg ='#ffe6e6' )
label1.place(x="20", y="40", height=400, width=1160)

cel = Label(root, text=37.0, bg="#03071e", fg="#8ecae6", font=("verdana", 60, 'bold'),)
cel.place(x=60, y=110, height=250, width=250)

far = Label(root, text=98.6, bg="#03071e", fg="#8ecae6", font=("verdana", 50, 'bold'),)
far.place(x=840, y=110, height=240, width=300)

plus = Button(root, text="+", bg="#5F0F40", fg="#8ecae6", font=("verdana", 40, 'bold'), command=myplus)
plus.place(x=460, y=210, height=80, width=100)

minus = Button(root, text="-", bg="#9A031E", fg="#8ecae6", font=("verdana", 50, 'bold'), command=myminus)
minus.place(x=600, y=210, height=80, width=100)



root.mainloop()