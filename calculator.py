from tkinter import *

# To create a window or root widget
root=Tk()
root.title("Simple calculator")
root.configure(bg = "SKYBLUE")

# e = Entry(root)
e = Entry(root, width = 35,bg = "GRAY", fg = "black")
e.grid(row=0, column=0, padx =10, pady=10, columnspan=4 )


# Function to extract numbers from the input field
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0,str(current) + str(number))
    return 


# Function to clear the input field
def button_clear():
    e.delete(0,END)
    return 

# Function to perform summation of numbers
def button_add():
    first_num = e.get()
    global f_num
    global math
    math="add"
    if '.' in first_num:
        f_num = float(first_num)
    else:
        f_num = int(first_num)
        e.Delete(0, END)

    

    return

def button_subtract():
    first_num = e.get()
    global f_num
    global math
    math="subtract"
    f_num = int(first_num)
    e.delete(0,END)
    return

def button_multiply():
    first_num = e.get()
    global f_num
    global math
    math="multiply"
    f_num = int(first_num)
    e.delete(0,END)
    return

def button_divide():
    first_num = e.get()
    global f_num
    global math
    math="divide"
    f_num = int(first_num)
    e.delete(0,END)
    return


def button_equal():
    second_number = e.get()
    e.delete(0,END)
    # e.insert(0, f_num+int(second_number))

    match math:
        case "add":
            e.insert(0, f_num+int(second_number))

        case "subtract":
            e.insert(0, f_num-int(second_number))

        case "multiply":
            e.insert(0, f_num*int(second_number))

        case "divide":
            e.insert(0, f_num/int(second_number))
            
# Button layout
def button_operation(operation):
    global f_num
    global math
    math = operation
    f_num = float(e.get())
    e.delete(0, END)

# Rest of the code remains the same...

buttons = [
    ("7", lambda: button_click(7)), ("8", lambda: button_click(8)), ("9", lambda: button_click(9)), ("+", lambda: button_operation("add")),
    ("4", lambda: button_click(4)), ("5", lambda: button_click(5)), ("6", lambda: button_click(6)), ("-", lambda: button_operation("subtract")),
    ("1", lambda: button_click(1)), ("2", lambda: button_click(2)), ("3", lambda: button_click(3)), ("*", lambda: button_operation("multiply")),
    ("0", lambda: button_click(0)), (".", lambda: button_click(".")), ("=", button_equal), ("/", lambda: button_operation("divide")),
    ("C", button_clear),
]

row, col = 1, 0
for (text, cmd) in buttons:
    Button(root, text=text, padx=20, pady=20, font=("Arial", 16), command=cmd)\
      .grid(row=row, column=col, sticky="nsew")
    col += 1
    if col > 3:
        col = 0
        row += 1

# Expand grid
for i in range(row + 1):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()