import tkinter as tk
import tkinter.ttk as ttk

# def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


win = tk.Tk()
win.title("Calculator")
win.geometry("350x200+600+300")

# ttk.Button.tk_setPalette(win, background="gray")

text = tk.StringVar()
expr = ''

def press(x):
    global expr

    if x == 'c':
        text.set('')
        expr = ''
    elif x == '=':
        result = eval(expr)
        expr += f" {str(x)} {result}"
        text.set(expr)
    elif x == ('+' or '-' or '*' or '/'):
        expr += f" {str(x)} "
        text.set(expr)
    else:
        expr += f"{str(x)}"
        text.set(expr)


entry = ttk.Entry(win, justify="right", textvariable=text)
entry.grid(row=0, columnspan=3, sticky="nsew")

button_7 = ttk.Button(win, text='7', command=lambda: press(7))
button_7.grid(row=1, column=0)

button_8 = ttk.Button(win, text='8', command=lambda: press(8))
button_8.grid(row=1, column=1)

button_9 = ttk.Button(win, text='9', command=lambda: press(9))
button_9.grid(row=1, column=2)

button_4 = ttk.Button(win, text='4', command=lambda: press(4))
button_4.grid(row=2, column=0)

button_5 = ttk.Button(win, text='5', command=lambda: press(5))
button_5.grid(row=2, column=1)

button_6 = ttk.Button(win, text='6', command=lambda: press(6))
button_6.grid(row=2, column=2)

button_1 = ttk.Button(win, text='1', command=lambda: press(1))
button_1.grid(row=3, column=0)

button_2 = ttk.Button(win, text='2', command=lambda: press(2))
button_2.grid(row=3, column=1)

button_3 = ttk.Button(win, text='3', command=lambda: press(3))
button_3.grid(row=3, column=2)

button_decimal = ttk.Button(win, text='.', command=lambda: press('.'))
button_decimal.grid(row=4, column=0)

button_zero = ttk.Button(win, text='0', command=lambda: press(0))
button_zero.grid(row=4, column=1)

button_equals = ttk.Button(win, text='=', command=lambda: press('='))
button_equals.grid(row=4, column=2)

button_divide = ttk.Button(win, text='/', command=lambda: press('/'))
button_divide.grid(row=1, column=3)

button_multiply = ttk.Button(win, text='x', command=lambda: press('*'))
button_multiply.grid(row=2, column=3)

button_subtract = ttk.Button(win, text='-', command=lambda: press('-'))
button_subtract.grid(row=3, column=3)

button_add = ttk.Button(win, text='+', command=lambda: press('+'))
button_add.grid(row=4, column=3)

button_clear = ttk.Button(win, text='c', command=lambda: press('c'))
button_clear.grid(row=0, column=3)

win.mainloop()
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
