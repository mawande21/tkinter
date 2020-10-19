from tkinter import *


window = Tk()
window.title('Temperature Convector')
window.minsize(width=500, height=500)

celcius_var= IntVar
fahrenheit_var =IntVar

l1 = LabelFrame(window,text='Celcius To Fahrenheit',padx=20, pady=20)
l1.grid(row=2, column=0)

E1 = Entry(l1,state='disable')
E1.grid(row=4, column=0)

def cel_active():
    E1.configure(state='normal')

btn_active = Button(window,text='Activate -Celcius to Fahrenheit', command=cel_active)
btn_active.grid(row=6, column=0)

l2 = LabelFrame(window, text='Fahrenheit to Celcius',padx=20, pady=20)
l2.grid(row=2, column=5)

E2 = Entry(l2,state='disable')
E2.grid(row=4, column=5)

def far_active():
    E2.configure(state='normal')

btn_active1 = Button(window,text='Activate -Fahrenheit to Celcius', command=far_active)
btn_active1.grid(row=6, column=5)



def exit():
    window.destroy()
exit_btn = Button(text = "Quit", command=exit)
exit_btn.grid(row=9, column=6)

def convert_C():
    if  not E1.get():
        celcius = float(E1.get())
        fahrenheit = (celcius*9/5)+32
        result_entry.insert(0, str(fahrenheit))

def convert_f():
    if not E2.get():
        fahrenheit = float(E2.get())
        celcius = (fahrenheit-32)*5/9
        result_entry.insert(0, celcius)

result_bnt = Button(window, text='Convert C-F',command=convert_C)
result_bnt.grid(row=7, column=2)


result_bnt2 = Button(window, text='Convert F-C',command=convert_f)
result_bnt2.grid(row=7, column=4)

result_entry = Entry(window, bg='light green')
result_entry.grid(row=8, column=2)


def Clear():
    E1.delete(0, END)
    E2.delete(0, END)
    result_entry.delete(0,END)

Clear_btn = Button(window, text='Clear',command=Clear)
Clear_btn.grid(row=8, column=6)

window.mainloop()
