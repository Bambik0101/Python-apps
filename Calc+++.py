import tkinter as tk
import string

def bereken():
    try:
       
        num1 = float(invoer_num1.get())
        num2 = float(invoer_num2.get())
        
       
        result = num1 + num2
        result_label.config(text=f"Het antwoord is {result}", bg="orange", fg="black")
    except ValueError:
       
        result_label.config(text="Voer geldige getallen in!", bg="red", fg="black")


#  main
root = tk.Tk()
root.title = "Calc+++"
root.geometry("500x350")
root.config(bg='#8a0015')

#titel
title_label = tk.Label(root, text="Calc+++(Made by Bambik)", font=("Comic Sans MS", 18), bg="red")
title_label.pack(pady=10)

# invoer label NIET INVOER POSSIBLE
invoer_label1 = tk.Label(root, text="Wat is je eerste getal? En je tweede?", font=("Comic Sans MS", 10), bg="red")
invoer_label1.pack(pady=5)

# invoer eerste num1
invoer_num1 = tk.Entry(root, width=10, font=("Comic Sans MS", 14))
invoer_num1.pack(pady=5)

#invoer tweede num2
invoer_num2 = tk.Entry(root, width=10, font=("Comic Sans MS", 14))
invoer_num2.pack(pady=5)

# bereken knop
bereken_knop = tk.Button(root, text="Bereken", command=bereken, font=("Comic Sans MS", 14), bg="red", fg="black")
bereken_knop.pack(pady=10)

# result
result_label = tk.Label(root, text="", font=("Comic Sans MS", 12), bg="orange", fg="black")
result_label.pack(pady=10)


#loop
root.mainloop()
