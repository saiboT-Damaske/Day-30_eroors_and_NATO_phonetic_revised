import json
from tkinter import messagebox
import random
from tkinter import *
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
               'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
               'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_numbers + password_letters + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)

    print(f"Your password is: {password}")
    entry_pw.insert(0, password)
    pyperclip.copy(password)
    return password


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # text = f"{entry_website.get()} | {entry_mail.get()} | {entry_pw.get()}\n"
    new_data = {
        entry_website.get(): {
            "email": entry_mail.get(),
            "password": entry_pw.get(),
        }
    }

    if len(entry_website.get()) == 0 or len(entry_pw.get()) == 0 or len(entry_mail.get()) == 0:
        messagebox.showinfo(title="Error", message="please dont leave any fields empty")

    else:
        try:
            with open("./passwords.json", "r") as data_file:
                # read the file and update the data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("./passwords.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        except json.decoder.JSONDecodeError:
            with open("./passwords.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("./passwords.json", "w") as data_file:
                # write the new updated json file
                json.dump(data, data_file, indent=4)
        finally:
            entry_pw.delete(0, END)
            entry_mail.delete(0, END)
            entry_website.delete(0, END)


# ---------------------------- SEARCH ENTRY ------------------------------- #


def find_password():
    user_search = entry_website.get().lower()
    try:
        with open("./passwords.json", "r") as data_file:
            # read the file and update the data
            data = json.load(data_file)
            website = data[user_search]
    except json.decoder.JSONDecodeError:
        messagebox.showinfo(title="Error", message="You have not saved any passwords yet.")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.\nYou have not saved any passwords yet.")
    except KeyError:    # this could rather be done with an if/else check which is simply easier
        messagebox.showinfo(title="Error", message="Your search finds no match")
    else:
        messagebox.showinfo(title="Search Result", message=f"Username: {website['email']}\n"
                                                           f"Password: {website['password']}")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50, bg="white")

canvas = Canvas(height=200, width=200, bg="white", highlightthickness=0)
photo = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)

label_web = Label(text="Website:", highlightthickness=0, bg="white")
label_web.grid(column=0, row=1)

label_email = Label(text="Email/Username::", highlightthickness=0, bg="white")
label_email.grid(column=0, row=2)

label_pw = Label(text="Password:", highlightthickness=0, bg="white")
label_pw.grid(column=0, row=3)

entry_website = Entry(width=21)
entry_website.grid(column=1, row=1)
entry_website.focus()

entry_mail = Entry(width=40)
entry_mail.grid(column=1, row=2, columnspan=2)
entry_mail.insert(0, "@gmail.com")

entry_pw = Entry(width=21)
entry_pw.grid(column=1, row=3)

button_generate_pw = Button(text="Generate Password", command=generate_password, width=15)
button_generate_pw.grid(column=2, row=3)

button_add = Button(text="Add", width=36, command=save)
button_add.grid(column=1, row=4, columnspan=2)

button_search = Button(text="Search", command=find_password, width=15)
button_search.grid(column=2, row=1)

window.mainloop()
