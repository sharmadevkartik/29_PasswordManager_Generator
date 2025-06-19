from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generatepassword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters= [random.choice(letters) for _ in range(random.randint(8,10))]
    password_numbers= [random.choice(numbers) for _ in range(random.randint(2,4))]
    password_symbols= [random.choice(symbols) for _ in range(random.randint(2,4))]

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
    new_data={
        website_text: {
            "email":email_username_text,
            "password": password_text
        }
    }

    if len(website_text) ==0 or len(password_text)==0:
        messagebox.showerror(title='Oops, Data Missing!', message="Website and Password fields can't be empty")
    else:
        try:
            with open('credentials_ledger.json', 'r') as f:
                # Reading old data
                data = json.load(f)
        except:
            with open('credentials_ledger.json', 'w') as f:
                json.dump(new_data,f,indent=4)
        else:
            data.update(new_data)
            with open('credentials_ledger.json', 'w') as f:
                json.dump(data,f,indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# -------------------------- FIND PASSWORD ---------------------------- #

def find_password():
    website_text=website_entry.get()
    try:
        with open('credentials_ledger.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title='Oops, File missing', message='No Data File Found')
    except:
        messagebox.showinfo(title='Oops, File missing', message='There is nothing here, start saving some credentials first')
    else:
        try:
            foundemail = data[f'{website_text}']['email']
            foundpassword=data[f'{website_text}']['password']
        except KeyError:
            messagebox.showinfo(title='Oops, Data Missing!', message=f"No details for {website_text} exists")
        else:
            messagebox.showinfo(title=website_text, message=f'Email: {foundemail}\nPassword: {foundpassword}')



# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title('Password Manager')
window.config(padx=50,pady=50)

canvas=Canvas(width=200, height=200)
lock_img=PhotoImage(file='logo.png')
canvas.create_image(100,100,image=lock_img)
canvas.grid(column=1,row=0)

#Entries
website_entry = Entry(width=20)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_username_entry = Entry(width=38)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0,'dksharma94@gmail.com')

password_entry = Entry(width=20)
password_entry.grid(column=1, row=3)

#labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#Buttons
gen_pswd_button=Button(text='Generate Password', width=15, command=generatepassword)
gen_pswd_button.grid(column=2, row=3)

add_button=Button(text='Add', width=34, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button=Button(text='Search',width=15, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()