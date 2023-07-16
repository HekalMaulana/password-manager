from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

FONT_NAME = "Arial"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    random_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_list += random_letters
    random_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_list += random_symbols
    random_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list += random_numbers

    shuffle(password_list)

    password = "".join(password_list)

    password_textinput.delete(0, END)
    password_textinput.insert(0, f"{password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
    website_input = website_textinput.get()
    username_input = username_textinput.get()
    password_input = password_textinput.get()

    new_data = {
        website_input: {
            "email": username_input,
            "password": password_input,
        },
    }

    if len(website_input) == 0 or len(password_input) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title="Save to data.txt",
                                       message=f"These are the details entered: \nEmail: {username_input}"
                                               f"\nPassword: {password_input} \nits ok to save ?")

        if is_ok:
            try:
                # Read Data
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                # Create new data if data.json doesn't exist
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating the data
                data.update(new_data)

                # Write new data
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                # Delete user input and set the cursor focus back to website input
                website_textinput.delete(0, END)
                website_textinput.focus()
                password_textinput.delete(0, END)


# --------------------------- Find Password ---------------------------- #
def find_password():
    pass


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas Widget
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Website label
website_label = Label(text="Website:", font=(FONT_NAME, 12, "bold"))
website_label.grid(column=0, row=1)

# Username label
username_label = Label(text="Email/Username:", font=(FONT_NAME, 12, "bold"))
username_label.grid(column=0, row=2)

# Password label
password_label = Label(text="Password:", font=(FONT_NAME, 12, "bold"))
password_label.grid(column=0, row=3)

# Website textinput
website_textinput = Entry(width=33)
website_textinput.grid(column=1, row=1, sticky="w")
website_textinput.focus()

# username textinput
username_textinput = Entry(width=40)
username_textinput.grid(column=1, row=2, columnspan=2, sticky="w")
username_textinput.insert(0, "example@gmail.com")

# password textinput
password_textinput = Entry(width=33)
password_textinput.grid(column=1, row=3, sticky="w")

# Find password button
find_password_button = Button(text="Search", font=FONT_NAME, command=find_password)
find_password_button.grid(column=2, row=1)

# generate password button
generate_password_button = Button(text="Generate Password", font=FONT_NAME, command=generate_password)
generate_password_button.grid(column=2, row=3)

# Add button
add_button = Button(text="Add", width=36, font=FONT_NAME, command=add_data)
add_button.grid(column=1, row=4, columnspan=2, sticky="w", pady=10)

window.mainloop()
