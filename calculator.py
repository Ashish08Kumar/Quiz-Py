import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create the display for the calculator
display = tk.Entry(window, font=("Helvetica", 24))
display.grid(row=0, column=0, columnspan=5)

# Define the functions for the calculator buttons
def button_press(value):
    display.insert(tk.END, value)

def clear_display():
    display.delete(0, tk.END)

def calculate():
    try:
        result = eval(display.get())
        clear_display()
        display.insert(tk.END, result)
    except:
        clear_display()
        display.insert(tk.END, "Error")

# Create the buttons for the calculator
button1 = tk.Button(window, text="1", font=("Helvetica", 24), command=lambda: button_press("1"))
button2 = tk.Button(window, text="2", font=("Helvetica", 24), command=lambda: button_press("2"))
button3 = tk.Button(window, text="3", font=("Helvetica", 24), command=lambda: button_press("3"))
button4 = tk.Button(window, text="4", font=("Helvetica", 24), command=lambda: button_press("4"))
button5 = tk.Button(window, text="5", font=("Helvetica", 24), command=lambda: button_press("5"))
button6 = tk.Button(window, text="6", font=("Helvetica", 24), command=lambda: button_press("6"))
button7 = tk.Button(window, text="7", font=("Helvetica", 24), command=lambda: button_press("7"))
button8 = tk.Button(window, text="8", font=("Helvetica", 24), command=lambda: button_press("8"))
button9 = tk.Button(window, text="9", font=("Helvetica", 24), command=lambda: button_press("9"))
button0 = tk.Button(window, text="0", font=("Helvetica", 24), command=lambda: button_press("0"))
button_add = tk.Button(window, text="+", font=("Helvetica", 24), command=lambda: button_press("+"))
button_subtract = tk.Button(window, text="-", font=("Helvetica", 24), command=lambda: button_press("-"))
button_multiply = tk.Button(window, text="", font=("Helvetica", 24), command=lambda: button_press(""))
button_divide = tk.Button(window, text="/", font=("Helvetica", 24), command=lambda: button_press("/"))
button_equal = tk.Button(window, text="=", font=("Helvetica", 24), command=calculate)
button_clear = tk.Button(window, text="Clear", font=("Helvetica", 24))