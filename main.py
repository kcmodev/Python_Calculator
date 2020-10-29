import tkinter as tk
import tkinter.ttk as ttk

# def print_hi(name):
#     print(f'Hi, {name}')


win = tk.Tk()
win.title("Calculator")
win.geometry("355x245+600+300")

for i in range(5):
    win.rowconfigure(i, weight=2)

# ttk.Button.tk_setPalette(win, background="gray")

text = tk.StringVar()
expr = ''
solved = False


def press(x):
    global expr, solved

    if solved is False:
        if x == 'c':
            text.set('')
            expr = ''

        elif x == '=':
            try:
                result = eval(expr)
                text.set(result)
                solved = True
            except SyntaxError:
                text.set('')
                expr = ''

        elif x in {'+' or '-' or '*' or '/'}:
            expr += f" {str(x)} "
            text.set(expr)

        else:
            expr += f"{str(x)}"
            text.set(expr)
    else:
        expr = str(x)
        text.set(str(x))
        solved = False


num_row, num_span = 0, 1
# text box for user to enter equation
# first row
entry = ttk.Entry(win, justify="right", textvariable=text, font="Calibri 18")
entry.grid(row=num_row, columnspan=3, sticky="nsew")

button_clear = ttk.Button(win, text='C', command=lambda: press('c'))
button_clear.grid(row=num_row, column=3, sticky="nsew")

# number buttons
# second row
num_row += num_span

button_7 = ttk.Button(win, text='7', command=lambda: press(7))
button_7.grid(row=num_row, column=0, sticky="nsew")

button_8 = ttk.Button(win, text='8', command=lambda: press(8))
button_8.grid(row=num_row, column=1, sticky="nsew")

button_9 = ttk.Button(win, text='9', command=lambda: press(9))
button_9.grid(row=num_row, column=2, sticky="nsew")

button_divide = ttk.Button(win, text='/', command=lambda: press('/'))
button_divide.grid(row=num_row, column=3, sticky="nsew")

# second row
num_row += num_span

button_4 = ttk.Button(win, text='4', command=lambda: press(4))
button_4.grid(row=num_row, column=0, sticky="nsew")

button_5 = ttk.Button(win, text='5', command=lambda: press(5))
button_5.grid(row=num_row, column=1, sticky="nsew")

button_6 = ttk.Button(win, text='6', command=lambda: press(6))
button_6.grid(row=num_row, column=2, sticky="nsew")

button_multiply = ttk.Button(win, text='X', command=lambda: press('*'))
button_multiply.grid(row=num_row, column=3, sticky="nsew")

# third row
num_row += num_span

button_1 = ttk.Button(win, text='1', command=lambda: press(1))
button_1.grid(row=num_row, column=0, sticky="nsew")

button_2 = ttk.Button(win, text='2', command=lambda: press(2))
button_2.grid(row=num_row, column=1, sticky="nsew")

button_3 = ttk.Button(win, text='3', command=lambda: press(3))
button_3.grid(row=num_row, column=2, sticky="nsew")

button_subtract = ttk.Button(win, text='-', command=lambda: press('-'))
button_subtract.grid(row=num_row, column=3, sticky="nsew")

# fourth row
num_row += num_span

button_decimal = ttk.Button(win, text='.', command=lambda: press('.'))
button_decimal.grid(row=num_row, column=0, sticky="nsew")

button_zero = ttk.Button(win, text='0', command=lambda: press(0))
button_zero.grid(row=num_row, column=1, sticky="nsew")

button_equals = ttk.Button(win, text='=', command=lambda: press('='))
button_equals.grid(row=num_row, column=2, sticky="nsew")

button_add = ttk.Button(win, text='+', command=lambda: press('+'))
button_add.grid(row=num_row, column=3, sticky="nsew")

win.resizable(False, False)
win.mainloop()

# if __name__ == '__main__':
#     print_hi('PyCharm')
