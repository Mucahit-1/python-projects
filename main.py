from tkinter import *
from tkinter import messagebox
from random import choice , randint , shuffle
import pyperclip
import json
#PASSWORD GENERATOR --

def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# SAVE PASSWORD --
def save():

    website_text = website_entry.get()
    email_text = email_entry.get()
    password_text = password_entry.get()
    data_dic = {
        website_text : {
            "email": email_text,
         "password": password_text
        }
    }

    if len(website_text) == 0 or len(password_text) == 0:
        messagebox.showinfo(title="Oops!" , message="Please make sure that you haven't left any field empty.")

    else:
        try:
            with open("data.json", "r") as data_file:
                #reading old data
                data =json.load(data_file)
                #updating old data with new data
                data.update(data_dic)
        except FileNotFoundError:
            with open("data.json" , "w") as data_file:
                #saving updated data
                json.dump(data_dic , data_file , indent=4)
        else:
            with open("data.json", "w") as data_file:
                json.dump(data , data_file , indent=4)

            website_entry.delete(0 , END)
            password_entry.delete(0 , END)
            messagebox.showinfo(title="successful",message="The website and password are successfully saved")
#FIND PASSWORD --

def find_password():
    website = website_entry.get()
    try:
        with open("data.json" , "r") as data_file:
            data = json.load(data_file)
            if website in data:
                email =  data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title="website" , message=f"email : {email}\npassword : {password}")
            else:
                messagebox.showinfo(title="error" , message="website not found")
    except FileNotFoundError:
        messagebox.showinfo(title="error" , message="No data file found")



#UI SETUP --
window = Tk()
window.title("Password Manager")
window.config(padx=20 , pady=20)

canvas = Canvas(width=120, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(60 , 100 , image=logo_image)
canvas.grid(column=1 , row=0)

website = Label(text="website:")
website.grid(column=0 , row=1)

email = Label(text="Email/Username:")
email.grid(column=0 , row=2)

password = Label(text="Password:")
password.grid(column=0 , row=3)

website_entry = Entry(width=21)
website_entry.grid(column=1 , row=1)
website_entry.focus()

email_entry = Entry(width=40)
email_entry.grid(column=1 , row=2 , columnspan=2)
email_entry.insert(0 , "mojahed.da202@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1 , row=3 )

search_button = Button(text="Search" , width=15 , command=find_password)
search_button.grid(column=2 , row=1)

generate_password_button = Button(text="Generate password" , command=generate_password)
generate_password_button.grid(column=2 , row=3)

add_button = Button(text="Add" , width=34 , command=save)
add_button.grid(column=1 , row=4 , columnspan=2)

window.mainloop()