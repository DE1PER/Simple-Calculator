
from tkinter.ttk import Entry
import customtkinter as ctk
from customtkinter import CTkEntry, CTkButton

# main window
root = ctk.CTk()
root.geometry('310x400')
root.resizable(False, False)
root.title('Calculator')

# text pole
txt = CTkEntry(root, 
            width=300, height=50)
txt.place(x=5, y=10)
def add_to_entry(symbol):
    txt.insert("end", symbol)
def clear_entry():
    txt.delete(0, "end")

# Button 1
button = ctk.CTkButton(master=root,
                       text="1",
                       command=lambda: add_to_entry("1"),
                       width=75, height=75,
                       font=("arial", 30))
button.place(x=5, y=87)

# Button 2
button2 = ctk.CTkButton(master=root,
                    text="2",
                    command=lambda: add_to_entry("2"),
                    width=75, height=75,
                    font=("arial", 30))
button2.place(x=81, y=87)

# Button 3
button3 = ctk.CTkButton(master=root,
                    text="3",
                    command=lambda: add_to_entry("3"),
                    width=75, height=75,
                    font=("arial", 30))
button3.place(x=157, y=87)

# Button 4
button4 = ctk.CTkButton(master=root,
                    text="4",
                    command=lambda: add_to_entry("4"),
                    width=75, height=75,
                    font=("arial", 30))
button4.place(x=5, y=163)

# Button 5
button5 = ctk.CTkButton(master=root,
                    text="5",
                    command=lambda: add_to_entry("5"),
                    width=75, height=75,
                    font=("arial", 30))
button5.place(x=81, y=163)

# Button 6
button6 = ctk.CTkButton(master=root,
                    text="6",
                    command=lambda: add_to_entry("6"),
                    width=75, height=75,
                    font=("arial", 30))
button6.place(x=157, y=163)

# Button 7
button7 = ctk.CTkButton(master=root,
                    text="7",
                    command=lambda: add_to_entry("7"),
                    width=75, height=75,
                    font=("arial", 30))
button7.place(x=5, y=239)

# Button 8
button8 = ctk.CTkButton(master=root,
                    text="8",
                    command=lambda: add_to_entry("8"),
                    width=75, height=75,
                    font=("arial", 30))
button8.place(x=81, y=239)

# Button 9
button9 = ctk.CTkButton(master=root,
                    text="9",
                    command=lambda: add_to_entry("9"),
                    width=75, height=75,
                    font=("arial", 30))
button9.place(x=157, y=239)

# Button 10
button0 = ctk.CTkButton(master=root,
                    text="0",
                    command=lambda: add_to_entry("0"),
                    width=75, height=75,
                    font=("arial", 30))
button0.place(x=81, y=315)

# Button 11
button_clear = ctk.CTkButton(master=root,
                            text="C",
                            command=clear_entry,
                            width=75, height=75,
                            font=("arial", 30))
button_clear.place(x=5, y=315)

# Button 12
button_equals = ctk.CTkButton(master=root,
                            text="=",
                            command=lambda: add_to_entry("="),
                            width=75, height=75,
                            font=("arial", 30))
button_equals.place(x=157, y=315)

# Button 13
button_plus = ctk.CTkButton(master=root,
                            text="+",
                            command=lambda: add_to_entry("+"),
                            width=75, height=75,
                            font=("arial", 30))
button_plus.place(x=233, y=87)

# Button 14
button_minus = ctk.CTkButton(master=root,
                            text="-",
                            command=lambda: add_to_entry("-"),
                            width=75, height=75,
                            font=("arial", 30))
button_minus.place(x=233, y=163)

# Button 15

button_multiply = ctk.CTkButton(master=root,
                            text="*",
                            command=lambda: add_to_entry("*"),
                            width=75, height=75,
                            font=("arial", 30))
button_multiply.place(x=233, y=239)

# Button 16
button_divide = ctk.CTkButton(master=root,
                            text="/",
                            command=lambda: add_to_entry("/"),
                            width=75, height=75,
                            font=("arial", 30))
button_divide.place(x=233, y=315)

if button_equals.cget("text") == "=":
    def calculate():
        try:
            result = eval(txt.get())
            txt.delete(0, "end")
            txt.insert("end", str(result))
        except Exception as e:
            txt.delete(0, "end")
            txt.insert("end", "Error")

    button_equals.configure(command=calculate)
    
root.mainloop()