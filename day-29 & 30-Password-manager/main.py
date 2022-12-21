import json
from tkinter import *
from tkinter import messagebox
import random
from random import shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]
    shuffle(password_list)
    password = ""
    for char in password_list:
        password += char

    pass_entry.insert(END, string=password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = web_entry.get()
    mail = user_entry.get()
    password = pass_entry.get()
    new_data = {
        web: {
            "email": mail,
            "user_password": password
        }
    }

    if web == "" or password == "":
        messagebox.showerror(title='Oops', message="Don't leave any field empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            web_entry.delete(0, END)
            pass_entry.delete(0, END)

def search():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message = "No Data file found")
    else:
        website = web_entry.get()
        if website in data:
            dict = data[website]
            email = dict.get("email")
            password = dict.get("user_password")
            user_entry.delete(0, END)
            user_entry.insert(END, email)
            pass_entry.insert(END, password)
        else:
            messagebox.showinfo(title="Error", message=f"No such {website} website data found")
# ---------------------------- UI SETUP ------------------------------- #


windows = Tk()
windows.title('Password Manager')
windows.configure(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

web_label = Label(text='Website:')
web_label.grid(column=0, row=1)

user_label = Label(text='Email/Username:')
user_label.grid(column=0, row=2)

pass_label = Label(text='Password:')
pass_label.grid(column=0, row=3)

web_entry = Entry(width=33)
web_entry.grid(column=1, row=1)
web_entry.focus()

user_entry = Entry(width=43)
user_entry.grid(column=1, row=2, columnspan=2)
user_entry.insert(END, 'yogeshs15101999@gmail.com')

pass_entry = Entry(width=33)
pass_entry.grid(column=1, row=3)

search_button = Button(text="Search", command=search)
search_button.grid(column=2, row=1)

gen_button = Button(text='Generate', command=generate_password)
gen_button.grid(column=2, row=3)

add_button = Button(width=36, text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2)

windows.mainloop()
