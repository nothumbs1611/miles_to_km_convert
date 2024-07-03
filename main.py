from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_results_label.config(text=f"{km}")


window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=20, pady=20)

#make an entry block to receive miles

miles_input = Entry(width = 7)
miles_input.grid(row = 0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)


#output line:
is_equal_label = Label(text="Is equal to:")
is_equal_label.grid(row = 1, column = 0)

km_results_label = Label(text="0")
km_results_label.grid(row = 1, column = 1)

km_label = Label(text = "Km")
km_label.grid(row = 1, column = 2)

#calculate button:

button = Button(text = "Calculate", command = miles_to_km)
button.grid(row = 2, column = 1)






window.mainloop()