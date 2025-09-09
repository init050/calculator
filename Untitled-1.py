import tkinter as tk

def calculate():
    num1 = int(num1_entry.get())
    num2 = int(num2_entry.get())
    if operator.get() == "+":
        result = num1 + num2
    elif operator.get() == "-":
        result = num1 - num2
    elif operator.get() == "*":
        result = num1 * num2
    elif operator.get() == "/":
        result = num1 / num2
    result_label.config(text="Result: " + str(result))

root = tk.Tk()
root.title("Calculator")

num1_label = tk.Label(root, text="Number 1")
num1_label.grid(row=0, column=0)
num1_entry = tk.Entry(root)
num1_entry.grid(row=0, column=1)

num2_label = tk.Label(root, text="Number 2")
num2_label.grid(row=1, column=0)
num2_entry = tk.Entry(root)
num2_entry.grid(row=1, column=1)

operator = tk.StringVar()
operator.set("+")

addition_button = tk.Radiobutton(root, text="+", variable=operator, value="+")
addition_button.grid(row=2, column=0)

subtraction_button = tk.Radiobutton(root, text="-", variable=operator, value="-")
subtraction_button.grid(row=2, column=1)

multiplication_button = tk.Radiobutton(root, text="*", variable=operator, value="*")
multiplication_button.grid(row=3, column=0)

division_button = tk.Radiobutton(root, text="/", variable=operator, value="/")
division_button.grid(row=3, column=1)

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=4, column=0, columnspan=2)

result_label = tk.Label(root, text="Result:")
result_label.grid(row=5, column=0, columnspan=2)

root.mainloop()
