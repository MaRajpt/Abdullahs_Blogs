from tkinter import *
import random
from tkinter import messagebox  # HAVE TO IMPORT SEPERATLY SINCE ITS NOT A CLASS  !!!!
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for letter in range(0, 5)]
    password_symbols = [random.choice(symbols) for symbol in range(0, 3)]
    password_numbers = [random.choice(numbers) for number in range(0, 3)]

    bundle = password_letters + password_symbols + password_numbers
    random.shuffle(bundle)

    password = ''.join(bundle)  # we can also use for loop using empty string "" and assign values

    password_entry.insert(0, password)

    #   AUTOMATICALLY COPIES THE GENERATED PASSWORD ( CAN BE PASTED ANYWHERE )
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_info():

    web_data = web_entry.get()
    email_entry = user_entry.get()
    password_data = password_entry.get()
    new_data = {
        web_data: {
            "email": email_entry,
            "password": password_data
        }
    }

    # MESSAGE BOX
    if len(web_data) == 0 or len(password_data) == 0:
        messagebox.showinfo(title="Oops", message="You left a field empty !")
    else:
        try:
            with open("data.json", 'r') as data_file:  # reading data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", 'w') as data_file:  # ENTERING NEW DATA IN EXISTING DICTIONARY OF DATA ( INSTEAD OF APPENDING) Thnaks to data.update
                json.dump(new_data, data_file, indent=4)
        else:       # if exception does not takes place
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            web_entry.delete(0, END)
            password_entry.delete(0, END)       # deleting zero to end

# ---------------------------- FIND PASSWORD  ------------------------------- #

def search_password():
    search_company = web_entry.get()
    try:
        with open("data.json", 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=" File Not Found !")
    else:
        if search_company in data:
            messagebox.showinfo(title=f"{search_company}", message=f"Email: {data[search_company]['email']} \nPassword: {data[search_company]['password']} ")
        else:
            messagebox.showinfo(title="Error", message="Data no Found !")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.minsize(300, 300)
window.config(padx=20, pady=20)


canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
web = Label(text="Website:")
web.grid(column=0, row=1)

user = Label(text="Email/Username:")
user.grid(column=0, row=2)

password = Label(text="Password:")
password.grid(column=0, row=3)

# Entries

web_entry = Entry(width=35)
web_entry.grid(column=1, row=1)
web_entry.focus()

user_entry = Entry(width=35)
user_entry.grid(column=1, row=2)        # To insert the email when application is launched (by default)
user_entry.insert(0, "Abdullah@email.com")                # 0 is index for cursor starting position ( eg begin) if we want end use "END"

password_entry = Entry(width=35)
password_entry.grid(column=1, row=3)

# Buttons

generate_password_button = Button(text="Generate Password", height=1, command=generate_password)
generate_password_button.grid(column=2, row=3)

search_button = Button(text="Search", height=1, command=search_password, width=15)
search_button.grid(column=2, row=1)

add_button = Button(text="Add", width=29, command=save_info)
add_button.grid(row=4, column=1)


window.mainloop()