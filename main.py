import tkinter
from tkinter import *
from tkinter import messagebox
from random import randint

root = Tk()
root.title('Password Gen')
# root.iconbitmap()
root.geometry("800x400")


def rand_pass():
    entry2.delete(0, END)
    pass_len = int(entry.get())
    generated_pass = ''

    for i in range(pass_len):
        generated_pass += chr(randint(33, 126))

    entry2.insert(0, generated_pass)

    if entry2 == '':
        messagebox.showerror("Uh oh...", "You need to enter a length for the password")
    else:
        pass


def copy_pass():
    root.clipboard_clear()
    root.clipboard_append(entry2.get())

    messagebox.showinfo("Copied!", "The password you generated\nhas been saved to your clipboard")


frame = LabelFrame(root, text="Choose the length of the password")
frame.pack(padx=40, pady=40, side=RIGHT)

entry = Entry(frame, font=("Roboto", 24))
entry.pack(pady=20, padx=20)

entry2 = Entry(frame, text='', font=("Roboto", 24))
entry2.pack(padx=20, pady=20, side=RIGHT)

btn_frame = Frame(root)
btn_frame.pack(padx=20, side=tkinter.LEFT)

btn_gen = Button(btn_frame, text="Generate password", command=rand_pass)
btn_gen.grid(row=0, column=0, pady=40)

btn_copy = Button(btn_frame, text="Copy To Clipboard", command=copy_pass)
btn_copy.grid(row=1, column=0)

root.mainloop()
