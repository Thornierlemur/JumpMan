import tkinter as tk
import tkinter.font as tkFont
from tkinter.ttk import *
from tkinter import *
import time

name = ""

# Intent: Function to center Tkinter window in center of the currently focused screen
# Preconditions: Parameters root = window, w = width, h = hieght 
# Postcondition: Display a window in the center of screen
# Example center_window(root,500,500) , displays the specified window at center with 
# a width and heigh of 500
def center_window(root, w, h):
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))

# Creating window element and setting the title
logWin = tk.Tk()
logWin.title("Jump Man")
center_window(logWin,600,300)

# Intent: Building the appearance of the log in window before it appears. 
# Also contains the function that handles how the user signs in
def log_in_win():

  # Intent: Define function for getting username and password from entries and handling errors that may occur
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
        # Used to skip over line in file that contains the password and question
        file1.readline(); file1.readline()

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
        loginFailureLabel = tk.Label(text = "Incorect Password"); loginFailureLabel.place(x = 110, y = 205)

  # Setting up font and window including labels, buttons, and entries
  fontStyle = tkFont.Font(family = "Lucida Grande", size = 25)
  logInLabel = tk.Label(text = "JumpMan log in", font = fontStyle); logInLabel.place(x = 20, y = 10)
  labelU = tk.Label(text = "Username:"); labelU.place(x = 20, y = 60)
  labelP = tk.Label(text = "Password:"); labelP.place(x = 20, y = 130)
  acctButton = tk.Button(text = "Create an account", command = create_account_win, width = 20, bg = "lightblue"); acctButton.place(x = 430, y = 230)
  loginButton = tk.Button(text = "Sign in", command = sign_in, width = 10, bg = "orange"); loginButton.place(x = 20, y = 200)
  changePassButton = tk.Button(text = "Change password?", command = change_password_window, width = 20, bg = "lightblue"); changePassButton.place(x = 430, y = 200)
  userNameEnt = tk.Entry(width = 12, font = fontStyle); userNameEnt.place(x = 20, y = 80)
  passEnt = tk.Entry(width = 12, font = fontStyle, show = '*'); passEnt.place(x = 20, y = 150)

  # running the window (doesn't work without this)
  logWin.mainloop()

# Intent: Building the appearance of the log in window before it appears. 
# Also contains the function that handles how the user creates their account.
def create_account_win():

  # Intent: Handles writing to the file when a new account is created, also possible input errors that might occur
  def account_creation():
    # Open the accounts file to append username and password to the end
    
    name = createNameEnt.get()
    passw = createPassEnt.get()
    question = securityQuestionEnt.get()


    file1 = open("accounts\Accounts.txt", "r")
    while True:
      fileUname = file1.readline()
      if(fileUname == (name + '\n')):
        tooLongLabel.place_forget()
        entryEmpty.place_forget()
        uNameExistsLabel.place(x = 240, y = 90)
        return
      elif not fileUname:
        break
      else:
        file1.readline()
        file1.readline()

    file1.close()
    if len(name) > 15 or len(passw) > 15 or len(question) > 15:
      entryEmpty.place_forget()
      tooLongLabel.place(x = 240, y = 90)

    # Condition for if create account is clicked with one or both entries empty
    elif(name == "" or passw == "" or question == ""):
      tooLongLabel.place_forget()
      entryEmpty.place(x = 240, y = 90)

    
    # Creation Success Condition
    else:
      file1 = open("accounts\Accounts.txt", "a")
      file1.write(name + "\n")
      file1.write(passw + "\n")
      file1.write(question + "\n")
      file1.close()

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
  winTitle = tk.Label(newWin, text = "Register an Account", font = fontStyle); winTitle.place(x = 20, y = 10)
  labelU = tk.Label(newWin, text = "Username:"); labelU.place(x = 20, y = 60)
  labelP = tk.Label(newWin, text = "Password:"); labelP.place(x = 20, y = 130)
  labelQ = tk.Label(newWin, text = "Security Question: What is your favorite song?"); labelQ.place(x = 20, y = 200)
  tooLongLabel = tk.Label(newWin, text = "No entry longer than 15 characters, please")
  uNameExistsLabel = tk.Label(newWin, text = "Username already exists")
  entryEmpty = tk.Label(newWin, text = "Please fill all entries")

  createNameEnt = tk.Entry(newWin, width = 12, font = fontStyle); createNameEnt.place(x = 20, y = 80)
  createPassEnt = tk.Entry(newWin, width = 12, font = fontStyle, show = '*'); createPassEnt.place(x = 20, y = 150)
  securityQuestionEnt = tk.Entry(newWin, width = 15, font = fontStyle); securityQuestionEnt.place(x = 20, y = 220)
  makeAcctButton = tk.Button(newWin, text = "Create Account", command = account_creation, width = 14, bg = "orange"); makeAcctButton.place(x = 460, y = 220)
  closeWinButton = tk.Button(newWin, text = "Back to Sign in", width = 14, bg = "lightblue", command = newWin.destroy); closeWinButton.place(x = 460, y = 250)

  newWin.mainloop


# Intent: Window that shows up when a user clicks "Change Password" allows users to change a forgetten password.
def change_password_window():

  # Intent: Hide labels from view to avoid clutter 
  def hideAllLabels():
    labelINCP.place_forget()
    labelINCQ.place_forget()
    labelNOU.place_forget()
    labelTooLong.place_forget()
    labelDifPass.place_forget()
    labelEmptyEntry.place_forget()
  
  # Intent: Main fuction to grab user infomation such as username, password, new password, and security question.
  def change_pass():
    # Get all data from entries
    uName = currentUserEnt.get()
    passw = oldPassEnt.get()
    newPass = newPassEnt.get()
    confirmPass = cnfrmPassEnt.get()
    answ = questionEnt.get()

    # Check for empty entries
    if(uName == "" or passw == "" or newPass == "" or confirmPass == "" or answ == ""):
      hideAllLabels()
      labelEmptyEntry.place(x = 360, y = 40)
      return
    # Check for entries exceeding char limit
    if(len(uName) > 15 or len(passw) > 15 or len(newPass) > 15 or len(confirmPass) > 15 or len(answ) > 15):
      hideAllLabels()
      labelTooLong.place(x = 360, y = 40)
      return
    # Check if new and confirmation password match
    if(newPass != confirmPass):
      hideAllLabels()
      labelDifPass.place(x = 360, y = 40)
      return

    found = False # Bool for if account name is found
    count = 0 # Holds index where password will be overwritten

    file1 = open("accounts\Accounts.txt", "r+")

    while True:
      line = file1.readline()
      if line == (uName + '\n'):
        found = True
        break
      # Reached end of file
      elif not line:
        break
      else:
        # Skip over password and question to get to next account name
        file1.readline(); file1.readline()
        count += 3

    if found == True:
      # Get current pass and security answer for account
      storedP = file1.readline()
      securityAnswer = file1.readline()

      # If both match data from entries, overwrite with new password
      if(storedP == (passw + '\n') and securityAnswer == (answ + '\n')):
       file2 = open("accounts\Accounts.txt", "r")
       fullList = file2.readlines()
       fullList[count + 1] = newPass + '\n'

       file2 = open("accounts\Accounts.txt", "w")
       file2.writelines(fullList)
       file2.close()
       changeButton.destroy()

      # Incorrect entry
      else:
        
        if(storedP != (passw + '\n')):
          hideAllLabels()
          labelINCP.place(x = 360, y = 40)
        elif(securityAnswer != (answ + '\n')):
          hideAllLabels()
          labelINCQ.place(x = 360, y = 40)
    else:
      hideAllLabels()
      labelNOU.place(x = 360, y = 40)



  # Window appearance and geometry
  newPassWin = Toplevel(logWin)
  newPassWin.title("Change password")
  center_window(newPassWin,600,300)

  labelU = tk.Label(newPassWin, text = "Username:"); labelU.place(x = 20, y = 60)
  labelP = tk.Label(newPassWin, text = "Old Password:"); labelP.place(x = 20, y = 130)
  labelQ = tk.Label(newPassWin, text = "Security Question: What is your favorite song?"); labelQ.place(x = 20, y = 200)
  labelNewP = tk.Label(newPassWin, text = "New password:"); labelNewP.place(x = 300, y = 60)
  labelCnfrmP = tk.Label(newPassWin, text = "Comfirm New Password:"); labelCnfrmP.place(x = 300, y = 130)
  labelINCP = tk.Label(newPassWin, text = "Old password is incorrect") 
  labelINCQ = tk.Label(newPassWin, text = "Secuirty question is incorrect") 
  labelNOU = tk.Label(newPassWin, text = "Username not found")
  labelTooLong = tk.Label(newPassWin, text = "No entry longer than 15 characters, please")
  labelDifPass = tk.Label(newPassWin, text = "New/confirmation password don't match")
  labelEmptyEntry = tk.Label(newPassWin, text = "Please fill all entries")

  fontStyle = tkFont.Font(family = "Lucida Grande", size = 25)
  acctLabel = tk.Label(newPassWin, text = "Change your password", font = fontStyle); acctLabel.place(x = 20, y = 10)
  currentUserEnt = tk.Entry(newPassWin, text = "Username", width = 12, font = fontStyle); currentUserEnt.place(x = 20, y = 80)
  oldPassEnt = tk.Entry(newPassWin, width = 12, font = fontStyle, show = '*'); oldPassEnt.place(x = 20, y = 150)
  newPassEnt = tk.Entry(newPassWin, width = 12, font = fontStyle, show = '*'); newPassEnt.place(x = 300, y = 80)
  cnfrmPassEnt = tk.Entry(newPassWin, width = 12, font = fontStyle, show = '*'); cnfrmPassEnt.place(x = 300, y = 150)
  questionEnt = tk.Entry(newPassWin, width = 15, font = fontStyle); questionEnt.place(x = 20, y = 220)

  changeButton = tk.Button(newPassWin, text = "Make Change", width = 10, bg = "orange", command = change_pass); changeButton.place(x = 510, y = 260)
  


  newPassWin.mainloop

# Intent: Function that grab the users username and return it if succesful or blank if not.
def get_user_name():
  global name

  if len(name) == 0:
    return ""
  else:
    return name