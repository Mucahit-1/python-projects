from tkinter import *

window = Tk()
window.title("Mile to Kilometers Converter Project")
window.config(padx=20 , pady=20)

def miles_to_km():
    miles = float(Miles_input.get())
    km = miles*1.609
    kilometer_result_label.config(text=f"{km}")


is_equal_label = Label(text="is equal to")
is_equal_label.grid(column = 0 , row = 1)

Miles_label = Label(text="Miles")
Miles_label.grid(column = 2 , row = 0)

Miles_input = Entry(width=7)
Miles_input.grid(column=1 , row=0)

kilometer_result_label = Label(text = "0" )
kilometer_result_label.grid(column=1 , row=1)

kilometer_label = Label(text = "km")
kilometer_label.grid(column=2 , row=1)

calculate_bottun = Button(text= "calculate" , command=miles_to_km)
calculate_bottun.grid(column=1 , row=2)


window.mainloop()