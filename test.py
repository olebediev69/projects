import tkinter as tk
import customtkinter as ctk

root = tk.Tk()
root.geometry('500x500')

text_var = ctk.StringVar(value=None)
text = ctk.CTkEntry(root, placeholder_text='Something')
text.pack()
root.mainloop()