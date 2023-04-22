from tkinter import *

root = Tk()
root.geometry("1200x500")
root.title("Temperature Convertor")
root.config(bg='#ADE4DB')


coolcolors = ['#000000', '#00001a', '#000033', '#00004d', '#000066', '#000080', '#000099', '#0000b3', '#0000cc', '#0000e6', '#0000ff', '#1a1aff', '#3333ff', '#4d4dff', '#6666ff', '#8080ff', '#9999ff', '#b3b3ff', '#ccccff','#c6d9ec']
warmcolors = ['ffc2b3', '#ffcccc','#ffb3b3','#ff9999','#ff8080','#ff6666','#ff4d4d','#ff3333','#ff1a1a', '#ff0000','#e60000','#cc0000','#b30000','#990000','#800000','#660000','#4d0000','#330000','#1a0000','#000000']
colorlist = coolcolors + warmcolors

colordict = {round(35.0 + i/10, 1): colorlist[i] for i in range(len(colorlist))}


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