import tkinter as tk

def button_functionaly():
    print('Button has been pressed!')
    exit()

root = tk.Tk()

# dimensions
root.geometry('800x800')

# title
root.title('My first GUI')

# label
label = tk.Label(root, text='Hello World', font=('Arial', 20))
label.pack(padx=20, pady=20) # paddings can be inserted

# textbox
textbox = tk.Text(root, height=5, width=50, font=('Arial', 16))
textbox.pack()

# entry - oneline textbox
entry = tk.Entry(root, font=('Arial', 16))
entry.pack(padx=20, pady=20)

# button
button = tk.Button(root, text='Click Me!', command=button_functionaly)
button.pack(padx=20, pady=20)

root.mainloop()