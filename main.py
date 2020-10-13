from tkinter import *
window = Tk()
window.title('Temperature Convector')
window.minsize(width=500, height=500)


l1=LabelFrame(window,text='Celcius To Fahrenheit',padx=20, pady=20)
l1.grid(row=2, column=0)
E1=Entry(l1,state='disable')
E1.grid(row=4, column=0)

def Cel_Active():
    E1.configure(state='normal')
btn_active=Button(window,text='Activate -Celcius to Fahrenheit', command=Cel_Active)
btn_active.grid(row=6, column=0)

l2=LabelFrame(window, text='Fahrenheit to Celcius',padx=20, pady=20)
l2.grid(row=2, column=5)
E2=Entry(l2,state='disable')
E2.grid(row=4, column=5)

def Far_Active():
    E2.configure(state='normal')
btn_active1=Button(window,text='Activate -Fahrenheit to Celcius', command=Far_Active)
btn_active1.grid(row=6, column=5)



def exit():
    window.destroy()
exit_btn = Button(text = "Quit", command=exit)
exit_btn.grid(row=9, column=6)



def convert():
    if E1:
        fahrenheit = float(E1.get())
        celcius = (fahrenheit-32)*5/9
        result_entry.config(text=round(celcius,2))
        result_entry.insert(0, celcius)
    if E2:
        celcius = float(E2.get())
        fahrenheit = (celcius*9/5)+32
        result_entry.config(text=round(fahrenheit,2))

result_bnt=Button(window, text='Calculate Conversion',command=convert)
result_bnt.grid(row=6, column=3)
result_entry=Entry(window, bg='light green')
result_entry.grid(row=7, column=3)


def Clear():
    E1.delete(0, END)
    E2.delete(0, END)
    result_entry.delete(0,END)
Clear_btn=Button(window, text='Clear',command=Clear)
Clear_btn.grid(row=8, column=6)

window.mainloop()
