from tkinter import *
from tkinter import ttk
import random
import string
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.title('Password Generator')
root.geometry('380x330')
root.maxsize(380, 330)
root.minsize(380, 330)
root.iconbitmap('G:/C/Py/pwd.ico')


def generate_pw():
    pw = type_box.get()
    pw_len = length.get(1.0, 'end-1c')
    alpha_lower = string.ascii_lowercase
    alpha_upper = string.ascii_uppercase
    digits = string.digits
    punctuations = string.punctuation
    if pw_len == '':
        messagebox.showerror('Error', 'Please enter password length !')
    elif int(pw_len) > 12:
        messagebox.showerror('Error', 'Max Password Length: 12')
    elif pw == type_box['values'][0]:
        strong = alpha_lower + alpha_upper + digits + punctuations
        pwd = "".join(random.sample(strong, int(pw_len)))
        password_text.insert('end', pwd)
    elif pw == type_box['values'][1]:
        normal = alpha_lower + digits
        pwd = "".join(random.sample(normal, int(pw_len)))
        password_text.insert('end', pwd)
    elif pw == type_box['values'][2]:
        weak = digits
        pwd = "".join(random.sample(weak, int(pw_len)))
        password_text.insert('end', pwd)


def clear():
    password_text.delete(1.0, END)
    length.delete(1.0, END)


password = Label(root, text='Password Generator', font=('Century Gothic', 20, 'bold'))
password.place(x=60, y=10)

pw_image = ImageTk.PhotoImage(Image.open('G:/C/Py/pwd1.ico'))
pw_image_label = Label(root, image=pw_image)
pw_image_label.place(x=50, y=50)

type_ = StringVar()
type_box = ttk.Combobox(root, textvariable=type_, state='readonly', width=22, font=('Comic Sans', 12, 'bold'))
type_box['values'] = (
    'Strong password', 'Normal password', 'Weak password'
)
type_box.current(2)
type_box.place(x=80, y=80)

password_text = Text(root, width=15, height=1, borderwidth=5, relief=GROOVE, font=('Times New Roman', 20))
password_text.place(x=80, y=200)

length_label = Label(root, text='Length: ', font=('Century Gothic', 15))
length_label.place(x=80, y=160)

length = Text(root, width=15, height=1, borderwidth=2, relief=GROOVE)
length.place(x=175, y=165)

generate = Button(root, text='Generate', font=('Century Gothic', 10), command=generate_pw)
generate.place(x=90, y=275)

clear = Button(root, text='Clear', font=('Century Gothic', 10), command=clear)
clear.place(x=250, y=275)

exit_root = Button(root, text='Exit', font=('Century Gothic', 10), command=root.quit)
exit_root.place(x=190, y=275)

root.mainloop()
