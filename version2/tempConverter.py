from tkinter import *

root = Tk()
root.title("Temperature Converter")
root.geometry("1200x500")
root.config(bg="#000000")

def plus():
    c = cel.cget("text")
    c1 = c.strip('°C')
    c2 = float(c1) + 0.5
    c3 = str(c2) +'°C'
    cel.config(text=c3)
    
    f = (c2*1.8) + 32
    f3 = str(round(f,2)) +'°F'
    far.config(text=f3)
    print(f3)
    
def minus():
    c = cel.cget("text")
    c1 = c.strip('°C')
    c2 = float(c1) - 0.5
    c3 = str(c2) +'°C'
    cel.config(text=c3)
    
    f = (c2*1.8) + 32
    f3 = str(round(f,2)) + '°F'
    far.config(text=f3)
    print(f3)



window = Label(root, bg="#1b263b")
window.place(x=50, y=50, width=1100, height=400)

cel = Label(root, text='37.0 °C', font=("Arial", 70, 'bold'), bg="#00dbfd", fg="#ffffff")
cel.place(x=440, y=60, width=340, height=110)

far = Label(root, text='98.6 °F', font=("Arial", 70, 'bold'), bg="#00dbfd", fg="#ffffff")
far.place(x=440, y=330, width=340, height=110)


p_button = Button(root, text='+', font=("Arial", 250, 'bold'), bg="#00dbfd", fg="#1b263b", borderwidth=5, command=plus)
p_button.place(x=50, y=50, width=220, height=400)

m_button = Button(root, text='−', font=("Arial", 200, 'bold'), bg="#00dbfd", fg="#1b263b", borderwidth=5, command=minus)
m_button.place(x=950, y=50, width=220, height=400)

root.mainloop()