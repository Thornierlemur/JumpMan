import tkinter as tk
import tkinter.font as tkFont
from tkinter.ttk import *
from tkinter import *
import time

name = ""

# Function to center Tkinter in center of the currently foucsed screen
# Parameters root = window, w = width, h = hieght 
# Example center_window(root,500,500)
# Display a window in the center with a width and height of 500
def center_window(root, w, h):
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))

# Creating window element and setting the title
logWin = tk.Tk()
logWin.title("Jump Man")
#logWin.geometry("600x400+468+132")
center_window(logWin,600,300)


# Building the appearance of the log in window before it appears. Also contains the function that handles
# how the user signs in
def log_in_win():

  # Define function for getting username and password from entries and handling errors that may occur
  def sign_in(event):

    username = userNameEnt.get()
    password = passEnt.get()
    
    # Appends new line character to the end of variables to match structure on file
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
        #time.sleep(3)
        logWin.destroy()
       

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
  acctButton.place(x = 430, y = 200)
  acctButton.bind("<Button-1>", create_account_win)
  loginButton = tk.Button(text = "Sign in", width = 10, bg = "orange")
  loginButton.place(x = 20, y = 200)
  loginButton.bind("<Button-1>", sign_in)
  userNameEnt = tk.Entry(text = "Username", width = 12, font = fontStyle)
  userNameEnt.place(x = 20, y = 80)
  passEnt = tk.Entry(width = 12, font = fontStyle)
  passEnt.place(x = 20, y = 150)

  # running the window (doesn't work without this)
  logWin.mainloop()


# Building the appearance of the log in window before it appears. Also contains the function that handles
# how the user creates their account
def create_account_win(event):

  # Handles writing to the file when a new account is created, also possible input errors that might occur
  def account_creation(event):

    # Open the accounts file to append username and password to the end
    file1 = open("Accounts.txt", "a")
    name = createNameEnt.get()
    passw = createPassEnt.get()

    if len(name) > 15:
      tooLongLabel = tk.Label(newWin, text = "Username too long. 15 chars max")
      tooLongLabel.place(x = 130, y = 202)

    elif len(passw) > 15:
      tooLongLabel = tk.Label(newWin, text = "Password too long. 15 chars max")
      tooLongLabel.place(x = 130, y = 202)

    # Condition for if create account is clicked with one or both entries empty
    elif(name == "" or passw == ""):
      entryEmpty = tk.Label(newWin, text = "------Please fill both entries------")
      entryEmpty.place(x = 130, y = 202)

    # Creation Success Condition
    else:
      file1.write(name + "\n")
      file1.write(passw + "\n")

      successLabel = tk.Label(newWin, text = "Account Created Successfully")
      successLabel.place(x = 20, y = 230)
      newWin.destroy()
      makeAcctButton.destroy()
    
  #New window for account creation which goes on top of login window
  newWin = Toplevel(logWin)
  newWin.title("Create an Account")
  center_window(newWin,600,300)


  # Setting up font and window including labels, buttons, and entries
  fontStyle = tkFont.Font(family = "Lucida Grande", size = 25)
  acctLabel = tk.Label(newWin, text = "Register an Account", font = fontStyle)
  acctLabel.place(x = 20, y = 10)
  labelU = tk.Label(newWin, text = "Username:")
  labelU.place(x = 20, y = 60)
  labelP = tk.Label(newWin, text = "Password:")
  labelP.place(x = 20, y = 130)
  createNameEnt = tk.Entry(newWin, text = "Username", width = 12, font = fontStyle)
  createNameEnt.place(x = 20, y = 80)
  createPassEnt = tk.Entry(newWin, width = 12, font = fontStyle)
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