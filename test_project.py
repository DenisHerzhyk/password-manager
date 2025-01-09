from project import add, get, getList, delete
import os
from tkinter import messagebox
from unittest.mock import patch, MagicMock


def setup_temp_file():
    with open("passwords.txt", "w") as f:
        f.write("")


@patch("project.messagebox.showinfo")
@patch("project.messagebox.showerror")
def test_add(mock_showerror, mock_showinfo):
  setup_temp_file()
  global entryName, entryPassword, entryPlatform
  entryName, entryPassword, entryPlatform = MagicMock(), MagicMock(), MagicMock()

  entryName.get.return_value = "user"
  entryPassword.get.return_value = "password"
  entryPlatform.get.return_value = "platform"

  add(entryName, entryPassword, entryPlatform)
  mock_showinfo.assert_called_with("Success", "Password passed!")

  add(entryName, entryPassword, entryPlatform)
  mock_showinfo.assert_called_with("Dublicate", "This pair is already in the list!")

  entryName.get.return_value = ""
  entryPassword.get.return_value = ""
  entryPlatform.get.return_value = ""

  add(entryName, entryPassword, entryPlatform)
  mock_showerror.assert_called_with("Error", "Please enter both inputs")


@patch("project.messagebox.showinfo")
def test_get(mock_showinfo):
  setup_temp_file()
  global entryName, entryPassword, entryPlatform
  entryName, entryPassword, entryPlatform = MagicMock(), MagicMock(), MagicMock()

  entryName.get.return_value = "user"
  entryPassword.get.return_value = "password"
  entryPlatform.get.return_value = "platform"

  get(entryName, entryPlatform)
  mock_showinfo.assert_called_with("Passwords", "EMPTY LIST!")

  add(entryName, entryPassword, entryPlatform)
  get(entryName, entryPlatform)
  mock_showinfo.assert_called_with("Passwords", 'Platform: "platform"\nUsername: "user"\nPassword: "password"\n-------------------------------------------------------------------------------')

  entryName.get.return_value = "some"
  entryPlatform.get.return_value = "some"

  get(entryName, entryPlatform)
  mock_showinfo.assert_called_with("Passwords", "No such data exists")


@patch("project.messagebox.showinfo")
def test_getList(mock_showinfo):
  setup_temp_file()
  global entryName, entryPassword, entryPlatform
  entryName, entryPassword, entryPlatform = MagicMock(), MagicMock(), MagicMock()

  entryName.get.return_value = "user"
  entryPassword.get.return_value = "password"
  entryPlatform.get.return_value = "platform"

  getList()
  mock_showinfo.assert_called_with("Passwords", "EMPTY LIST!")

  add(entryName, entryPassword, entryPlatform)

  entryName.get.return_value = "user2"
  entryPassword.get.return_value = "password2"
  entryPlatform.get.return_value = "platform2"

  add(entryName, entryPassword, entryPlatform)
  getList()
  line = 'Platform: "platform"\nUsername: "user"\nPassword: "password"\n-------------------------------------------------------------------------------'
  line += 'Platform: "platform2"\nUsername: "user2"\nPassword: "password2"\n-------------------------------------------------------------------------------'
  mock_showinfo.assert_called_with("Passwords", line)
  with open("passwords.txt", "r") as f:
    print(f.read())

  
@patch("project.messagebox.showinfo")
@patch("project.messagebox.showerror")
def test_delete(mock_showerror, mock_showinfo):
  setup_temp_file()
  global entryName, entryPassword, entryPlatform
  entryName, entryPassword, entryPlatform = MagicMock(), MagicMock(), MagicMock()

  entryName.get.return_value = "user"
  entryPassword.get.return_value = "password"
  entryPlatform.get.return_value = "platform"

  delete(entryName, entryPassword, entryPlatform)
  mock_showerror.assert_called_with("Error", "There's no such data in list!")

  add(entryName, entryPassword, entryPlatform)
  delete(entryName, entryPassword, entryPlatform)
  mock_showinfo.assert_called_with("Success", 'Platform: "platform"\nUser "user" with password "password" deleted successfully')

  