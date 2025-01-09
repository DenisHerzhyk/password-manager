import tkinter as tk
from tkinter import messagebox

def main():
  global entryName, entryPassword, entryPlatform
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

  labelPlatform = tk.Label(app, text="Platform:")
  labelPlatform.grid(row=2, column=0, padx=10, pady=15)
  entryPlatform = tk.Entry(app)
  entryPlatform.grid(row=2, column=1, padx=10, pady=15)

  buttonAdd = tk.Button(app, text="ADD", command=lambda: add(entryName, entryPassword, entryPlatform))
  buttonAdd.grid(row=3, column=0, padx=15, pady=8, sticky="we")

  buttonGet = tk.Button(app, text="GET", command=lambda: get(entryName, entryPlatform))
  buttonGet.grid(row=3, column=1, padx=15, pady=8, sticky="we")

  buttonList = tk.Button(app, text="LIST", command=getList)
  buttonList.grid(row=4, column=0, padx=15, pady=8, sticky="we")

  buttonDelete = tk.Button(app, text="DELETE", command=lambda: delete(entryName, entryPassword, entryPlatform))
  buttonDelete.grid(row=4, column=1, padx=15, pady=8, sticky="we")

  app.mainloop()

#TODO Add also platform name for exact data. 

def add(entryName, entryPassword, entryPlatform):
  username = entryName.get()
  password = entryPassword.get()
  platform = entryPlatform.get()

  if username and password and platform:
    try:
      with open("passwords.txt", "r") as f:
        if f"{username} {password} {platform}\n" in f.readlines():
          messagebox.showinfo("Dublicate", "This pair is already in the list!")
          return
    except FileNotFoundError:
      print("No data in passwords.txt!")
    
    with open("passwords.txt", "a") as f:
      f.write(f"{username} {password} {platform}\n")
    messagebox.showinfo("Success", "Password passed!")
  else:
    messagebox.showerror("Error", "Please enter both inputs")


def get(entryName, entryPlatform):
  username = entryName.get()
  platform = entryPlatform.get()
  passwords = []

  try:
    with open("passwords.txt", 'r') as f:
      for line in f.readlines():
        data = line.strip().split(" ")
        passwords.append([data[0], data[1], data[2]])
  except:
    print("No passwords in passwords.txt!")
    
  if passwords:
    message = ""
    found = False
    for data in passwords:
      if data[0] == username and data[2] == platform:
        message += f"Platform: \"{platform}\"\nUsername: \"{username}\"\nPassword: \"{data[1]}\"\n-------------------------------------------------------------------------------"
        found = True
    if not found:
      message = "No such data exists"
    messagebox.showinfo("Passwords", message)
  else:
    messagebox.showinfo("Passwords", "EMPTY LIST!")


def getList():
  passwords = set()

  try:
    with open("passwords.txt", 'r') as f:
      for line in f.readlines():
        data = line.strip().split(" ")
        passwords.add((data[0], data[1], data[2]))
  except FileNotFoundError:
    print("No passwords in passwords.txt!")
    return

  passwords = list(passwords)
  if passwords:
    message = ""
    for username, password, platform in passwords:
      message += f"Platform: \"{platform}\"\nUsername: \"{username}\"\nPassword: \"{password}\"\n-------------------------------------------------------------------------------"
    messagebox.showinfo("Passwords", message)
  else:
    messagebox.showinfo("Passwords","EMPTY LIST!")


def delete(entryName, entryPassword, entryPlatform):
  username = entryName.get() 
  password = entryPassword.get()
  platform = entryPlatform.get()
  temp_passwords = []
  deleted_data = ""

  try:
    with open("passwords.txt", 'r') as f:
      for line in f.readlines():
        data = line.strip().split(" ")
        if len(data) == 3 and ((data[0], data[1], data[2]) != (username, password, platform)):
          temp_passwords.append([data[0], data[1], data[2]])
        else:
          deleted_data = f"{username} {password} {platform}"

    with open("passwords.txt", 'w') as f:
      for data in temp_passwords:
        f.write(f"{data[0]} {data[1]} {data[2]}\n")
    if deleted_data:
      messagebox.showinfo("Success", f"Platform: \"{platform}\"\nUser \"{username}\" with password \"{password}\" deleted successfully")
    else:
      messagebox.showerror("Error", "There's no such data in list!")
  except Exception as e:
    messagebox.showerror("Error", f"Error while deleting user \"{username}\": {e}")


if __name__ == "__main__":
  main()