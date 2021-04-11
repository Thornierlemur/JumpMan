import tkinter as tk
import tkinter.font as tkFont
from tkinter.ttk import *
from tkinter import *

name = ""

# Creating window element and setting the title
logWin = tk.Tk()
logWin.title("Jump Man")
logWin.geometry("600x400+468+132")

def log_in_win():

  # Define function for getting username and password from entries
  def sign_in(event):

    username = userNameEnt.get()
    password = passEnt.get()
    
    # For some reason python adds a newline character to the end of a line when you read from a file
    # so I need to add a newline character to the strings obtained from the entry
    username = username + "\n"
    password = password + "\n"

    # Open accounts file for read only
    file1 = open("Accounts.txt", "r")

    # Read through the whole file for the username, if the username is not found readname is set to empty string
    while True:
      readName = file1.readline()
      if(readName == username):
        break
      elif not readName:
        readName = ""
        break
      else:
        # Used to skip over line in file that contains the password
        file1.readline()

    # Username was not found
    if(readName == ""):
        userNameNotFound = tk.Label(text = "No such username")
        userNameNotFound.place(x = 110, y = 205)

    # Username was found 
    else:
      passw = file1.readline()

      if(passw == password):
        loginSuccessLabel = tk.Label(text = "-Login Successful-")
        loginSuccessLabel.place(x = 110, y = 205)
        global name
        name = userNameEnt.get()
        ExitWindowLabel = tk.Label(text = "-Please close the window-")
        ExitWindowLabel.place(x = 110, y = 250)

      else:
        loginFailureLabel = tk.Label(text = "Incorect Password")
        loginFailureLabel.place(x = 110, y = 205)

  # Setting up font and window including labels, buttons, and entries
  fontStyle = tkFont.Font(family = "Lucida Grande", size = 25)
  logInLabel = tk.Label(text = "JumpMan log in", font = fontStyle)
  logInLabel.place(x = 20, y = 10)
  labelU = tk.Label(text = "Username:")
  labelU.place(x = 20, y = 60)
  labelP = tk.Label(text = "Password:")
  labelP.place(x = 20, y = 130)
  acctButton = tk.Button(text = "Create an account", width = 20, bg = "lightblue")
  acctButton.place(x = 430, y = 360)
  acctButton.bind("<Button-1>", create_account_win)
  loginButton = tk.Button(text = "Sign in", width = 10, bg = "orange")
  loginButton.place(x = 20, y = 200)
  loginButton.bind("<Button-1>", sign_in)
  userNameEnt = tk.Entry(text = "Username", width = 16, font = fontStyle)
  userNameEnt.place(x = 20, y = 80)
  passEnt = tk.Entry(width = 10, font = fontStyle)
  passEnt.place(x = 20, y = 150)

  # running the window (doesn't work without this)
  logWin.mainloop()


def create_account_win(event):

  def account_creation(event):

    # Open the accounts file to append username and password to the end
    file1 = open("Accounts.txt", "a")
    name = createNameEnt.get()
    passw = createPassEnt.get()

    # Condition for if create account is clicked with one or both entries empty
    if(name == "" or passw == ""):
      entryEmpty = tk.Label(newWin, text = "Please fill both entries.")
      entryEmpty.place(x = 130, y = 202)

    # Creation Success Condition
    else:
      file1.write(name + "\n")
      file1.write(passw + "\n")

      successLabel = tk.Label(newWin, text = "Account Created Successfully")
      successLabel.place(x = 20, y = 230)
      makeAcctButton.destroy()
    
  #New window for account creation which goes on top of login window
  newWin = Toplevel(logWin)
  newWin.title("Create an Account")
  newWin.geometry("600x400+468+132")

  # Setting up font and window including labels, buttons, and entries
  fontStyle = tkFont.Font(family = "Lucida Grande", size = 25)
  acctLabel = tk.Label(newWin, text = "Register an Account", font = fontStyle)
  acctLabel.place(x = 20, y = 10)
  labelU = tk.Label(newWin, text = "Username:")
  labelU.place(x = 20, y = 60)
  labelP = tk.Label(newWin, text = "Password:")
  labelP.place(x = 20, y = 130)
  createNameEnt = tk.Entry(newWin, text = "Username", width = 16, font = fontStyle)
  createNameEnt.place(x = 20, y = 80)
  createPassEnt = tk.Entry(newWin, width = 10, font = fontStyle)
  createPassEnt.place(x = 20, y = 150)
  makeAcctButton = tk.Button(newWin, text = "Create Account", width = 14, bg = "orange")
  makeAcctButton.place(x = 20, y = 200)
  makeAcctButton.bind("<Button-1>", account_creation)
  closeWinButton = tk.Button(newWin, text = "Back to Sign in", width = 20, bg = "lightblue", command = newWin.destroy)
  closeWinButton.place(x = 430, y = 360)

  newWin.mainloop

def get_user_name():
  global name

  if len(name) == 0:
    return ""
  else:
    return name