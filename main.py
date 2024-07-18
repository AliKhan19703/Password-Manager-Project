from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- SEARCH INFO ------------------------------- #


def search():
    with open("data.json", "r") as file:
        try:
            data = json.load(file)
            website = website_entry.get()
            email = data[website]["email"]
            password = data[website]["password"]
        except JSONDecodeError:
            messagebox.showinfo(title="Error", message="No data in file.")
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="File not found!")
        except KeyError:
            messagebox.showinfo(title="Error", message=f"{website} info not found!")
        else:
            messagebox.showinfo(title=f"{website}", message=f"Email : {email} \nPassword : {password}")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_letters + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    info_dict = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(password) < 1 or len(website) < 1 or len(email) < 1:
        messagebox.showinfo(title="Error", message="Please don't leave any field empty")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                data.update(info_dict)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(info_dict, file, indent=4)
        except JSONDecodeError:
            with open("data.json", "w") as file:
                json.dump(info_dict, file, indent=4)
        else:
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(first=0, last=END)
            password_entry.delete(first=0, last=END)
            website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

website_label = Label(text="website: ")
website_label.grid(column=0, row=1)

website_entry = Entry(width=33)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)

email_entry = Entry(width=52)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "alikhanofficial81@gmail.com")

password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="        Search        ", command=search)
search_button.grid(column=2, row=1)


window.mainloop()
