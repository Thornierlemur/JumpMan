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
  def sign_in():

    username = userNameEnt.get()
    password = passEnt.get()
    
    # Appends new line character to the end of variables to match structure on file
    username = username + "\n"
    password = password + "\n"

    # Open accounts file for read only
    file1 = open("accounts\Accounts.txt", "r")

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
        global name
        name = userNameEnt.get()
        #time.sleep(3)
        logWin.destroy()
       
      else:
        loginFailureLabel = tk.Label(text = "Incorect Password")
        loginFailureLabel.place(x = 110, y = 205)

  # Setting up font and window including labels, buttons, and entries
  fontStyle = tkFont.Font(family = "Lucida Grande", size = 25)
  logInLabel = tk.Label(text = "JumpMan log in", font = fontStyle); logInLabel.place(x = 20, y = 10)
  labelU = tk.Label(text = "Username:"); labelU.place(x = 20, y = 60)
  labelP = tk.Label(text = "Password:"); labelP.place(x = 20, y = 130)
  acctButton = tk.Button(text = "Create an account", command = create_account_win, width = 20, bg = "lightblue"); acctButton.place(x = 430, y = 230)
  loginButton = tk.Button(text = "Sign in", command = sign_in, width = 10, bg = "orange"); loginButton.place(x = 20, y = 200)
  changePassButton = tk.Button(text = "Change password?", command = change_password_window, width = 20, bg = "lightblue"); changePassButton.place(x = 430, y = 200)
  userNameEnt = tk.Entry(width = 12, font = fontStyle); userNameEnt.place(x = 20, y = 80)
  passEnt = tk.Entry(width = 12, font = fontStyle); passEnt.place(x = 20, y = 150)

  # running the window (doesn't work without this)
  logWin.mainloop()


# Building the appearance of the log in window before it appears. Also contains the function that handles
# how the user creates their account
def create_account_win():

  # Handles writing to the file when a new account is created, also possible input errors that might occur
  def account_creation():

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
  winTitle = tk.Label(newWin, text = "Register an Account", font = fontStyle); acctLabel.place(x = 20, y = 10)
  labelU = tk.Label(newWin, text = "Username:"); labelU.place(x = 20, y = 60)
  labelP = tk.Label(newWin, text = "Password:"); labelP.place(x = 20, y = 130)
  createNameEnt = tk.Entry(newWin, width = 12, font = fontStyle); createNameEnt.place(x = 20, y = 80)
  createPassEnt = tk.Entry(newWin, width = 12, font = fontStyle); createPassEnt.place(x = 20, y = 150)
  makeAcctButton = tk.Button(newWin, text = "Create Account", command = account_creation, width = 14, bg = "orange"); makeAcctButton.place(x = 20, y = 200)
  closeWinButton = tk.Button(newWin, text = "Back to Sign in", width = 20, bg = "lightblue", command = newWin.destroy); closeWinButton.place(x = 430, y = 360)

  newWin.mainloop


def change_password_window():

  def change_pass():
    uName = currentUserEnt.get()
    passw = oldPassEnt.get()
    newPass = newPassEnt.get()
    confirmPass = cnfrmPassEnt.get()

    if(uName == "" or passw == "" or newPass == "" or confirmPass == ""):
      print("Please fill all entries")
      return
    if(len(uName) > 15 or len(passw) > 15 or len(newPass) > 15 or len(confirmPass) > 15):
      print("No entry longer than 15 characters, please.")
      return

    found = False

    file1 = open("accounts\Accounts.txt", "r+")

    while True:
      line = file1.readline()
      if line == (uName + '\n'):
        found = True
        break
      elif not line:
        break
      else:
        file1.readline()

    if found == True:
      storedP = file1.readline()
      if(storedP == (passw + '\n')):
        print("Correct Password")

      else:
        print("Incorrect Password")
    else:
      print("Username not found")




  newPassWin = Toplevel(logWin)
  newPassWin.title("Change password")
  center_window(newPassWin,600,300)

  labelU = tk.Label(newPassWin, text = "Username:"); labelU.place(x = 20, y = 60)
  labelP = tk.Label(newPassWin, text = "Old Password:"); labelP.place(x = 20, y = 130)
  labelNewP = tk.Label(newPassWin, text = "New password:"); labelNewP.place(x = 300, y = 60)
  labelCnfrmP = tk.Label(newPassWin, text = "Comfirm New Password:"); labelCnfrmP.place(x = 300, y = 130)

  fontStyle = tkFont.Font(family = "Lucida Grande", size = 25)
  acctLabel = tk.Label(newPassWin, text = "Change your password", font = fontStyle); acctLabel.place(x = 20, y = 10)
  currentUserEnt = tk.Entry(newPassWin, text = "Username", width = 12, font = fontStyle); currentUserEnt.place(x = 20, y = 80)
  oldPassEnt = tk.Entry(newPassWin, width = 12, font = fontStyle); oldPassEnt.place(x = 20, y = 150)
  newPassEnt = tk.Entry(newPassWin, width = 12, font = fontStyle); newPassEnt.place(x = 300, y = 80)
  cnfrmPassEnt = tk.Entry(newPassWin, width = 12, font = fontStyle); cnfrmPassEnt.place(x = 300, y = 150)

  changeButton = tk.Button(newPassWin, text = "Make Change", width = 10, command = change_pass); changeButton.place(x = 150, y = 200)
  


  newPassWin.mainloop

def get_user_name():
  global name

  if len(name) == 0:
    return ""
  else:
    return name