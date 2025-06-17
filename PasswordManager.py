from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generatepassword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters= [random.choice(letters) for _ in range(random.randint(8,10))]
    password_symbols= [random.choice(numbers) for _ in range(random.randint(2,4))]
    password_numbers= [random.choice(symbols) for _ in range(random.randint(2,4))]

    password_list=password_letters+password_symbols+ password_numbers
    random.shuffle(password_list)

    password="".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website_text=website_entry.get()
    email_username_text=email_username_entry.get()
    password_text=password_entry.get()

    if len(website_text) ==0 or len(password_text)==0:
        messagebox.showerror(title='Oops, Data Missing!', message="Website and Password fields can't be empty")
    else:
        is_ok = messagebox.askokcancel(title=website_text,
                                       message=f"These are the details entered:\nEmail: {email_username_text}\nPassword: {password_text}\nIs it ok to save?")
        if is_ok:
            with open('credentials_ledger.txt', 'a') as f:
                f.write( f"Website: {website_text} | Email/Username: {email_username_text} | Password: {password_text}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title('Password Manager')
window.config(padx=50,pady=50)

canvas=Canvas(width=200, height=200)
lock_img=PhotoImage(file='logo.png')
canvas.create_image(100,100,image=lock_img)
canvas.grid(column=1,row=0)

#Entries
website_entry = Entry(width=39)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_username_entry = Entry(width=39)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0,'dksharma94@gmail.com')

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

#labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#Buttons
gen_pswd_button=Button(text='Generate Password', command=generatepassword)
gen_pswd_button.grid(column=2, row=3)

add_button=Button(text='Add', width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()