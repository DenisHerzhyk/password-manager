import tkinter as tk
from tkinter import messagebox


def main():
  global entryName, entryPassword
  app = tk.Tk()
  app.geometry("560x270")
  app.title("Password Manager")

  labelName = tk.Label(app, text="Usename:")
  labelName.grid(row=0, column=0, padx=15, pady=15)
  entryName = tk.Entry(app)
  entryName.grid(row=0, column=1, padx=15, pady=15)

  labelPassword = tk.Label(app, text="Password:")
  labelPassword.grid(row=1, column=0, padx=10, pady=5)
  entryPassword = tk.Entry(app)
  entryPassword.grid(row=1, column=1, padx=10, pady=5)

  buttonAdd = tk.Button(app, text="ADD", command=add)
  buttonAdd.grid(row=2, column=0, padx=15, pady=8, sticky="we")

  buttonGet = tk.Button(app, text="GET", command=get)
  buttonGet.grid(row=2, column=1, padx=15, pady=8, sticky="we")

  buttonList = tk.Button(app, text="LIST", command=getList)
  buttonList.grid(row=3, column=0, padx=15, pady=8, sticky="we")

  buttonDelete = tk.Button(app, text="DELETE", command=delete)
  buttonDelete.grid(row=3, column=1, padx=15, pady=8, sticky="we")

  app.mainloop()


def add():
  username = entryName.get()
  password = entryPassword.get()

  if username and password:
    try:
      with open("passwords.txt", "r") as f:
        if f"{username} {password}\n" in f.readlines():
          messagebox.showinfo("Dublicate", "This username and password pair already in list!")
          return
    except FileNotFoundError:
      print("No passwords in passwords.txt!")
    
    with open("passwords.txt", "a") as f:
      f.write(f"{username} {password}\n")
    messagebox.showinfo("Success", "Password passed!")
  else:
    messagebox.showerror("Error", "Please enter both inputs")


def get():
  username = entryName.get()
  passwords = []

  try:
    with open("passwords.txt", 'r') as f:
      for line in f.readlines():
        data = line.strip().split(" ")
        passwords.append([data[0], data[1]])
  except:
    print("No passwords in passwords.txt!")
    
  if passwords:
    message = ""
    found = False
    for data in passwords:
      if data[0] == username:
        message += f"Username: \"{username}\"\tPassword: \"{data[1]}\"\n-------------------------------------------------------------------------------"
        found = True
    if not found:
      message = "No such username exists"
    messagebox.showinfo("Passwords", message)
  else:
    messagebox.showinfo("Passwords", "EMPTY LIST!")


def getList():
  passwords = set()

  try:
    with open("passwords.txt", 'r') as f:
      for line in f.readlines():
        data = line.strip().split(" ")
        passwords.add((data[0], data[1]))
  except FileNotFoundError:
    print("No passwords in passwords.txt!")
    return

  passwords = list(passwords)
  if passwords:
    message = ""
    for username, password in passwords:
      message += f"Username: \"{username}\"\tPassword: \"{password}\"\n-------------------------------------------------------------------------------"
    messagebox.showinfo("Passwords", message)
  else:
    messagebox.showinfo("Passwords","EMPTY LIST!")


def delete():
  username = entryName.get() 
  password = entryPassword.get()

  temp_passwords = []

  try:
    with open("passwords.txt", 'r') as f:
      for line in f.readlines():
        data = line.strip().split(" ")
        if len(data) == 2 and ((data[0], data[1]) != (username, password)):
          temp_passwords.append([data[0], data[1]])
    with open("passwords.txt", 'w') as f:
      for data in temp_passwords:
        f.write(f"{data[0]} {data[1]}\n")
    messagebox.showinfo("Success", f"User \"{username}\" with password \"{password}\" deleted successfully")
  except Exception as e:
    messagebox.showerror("Error", f"Error while deleting user \"{username}\": {e}")


if __name__ == "__main__":
  main()