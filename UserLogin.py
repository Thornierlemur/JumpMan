import tkinter as tk
import tkinter.font as tkFont

# Define function for getting username and password from entries
def handle_click(event):
  username = userNameEnt.get()
  password = passEnt.get()

  print("Username is: " + username)
  print("Password is: " + password)

# Creating window element and setting the title
logWin = tk.Tk()
logWin.title("Jump Man")

# Setting window dimensions and positioning
width = logWin.winfo_screenwidth()      
height = logWin.winfo_screenheight()
logWin.geometry("600x400+468+132")

# Setting font(s)
fontStyle = tkFont.Font(family = "Lucida Grande", size = 25)




# Creating text labels
logInLabel = tk.Label(text = "JumpMan log in", font = fontStyle)
logInLabel.place(x = 20, y = 10)

labelU = tk.Label(text = "Username:")
labelU.place(x = 20, y = 60)

labelP = tk.Label(text = "Password:")
labelP.place(x = 20, y = 130)



# Creating button to make an account 
acctButton = tk.Button(text = "Create an account", width = 20, bg = "lightblue")
acctButton.place(x = 430, y = 360)

loginButton = tk.Button(text = "Sign in", width = 10, bg = "orange")
loginButton.place(x = 20, y = 200)
loginButton.bind("<Button-1>", handle_click)

# Creating entries for input
userNameEnt = tk.Entry(text = "Username", width = 16, font = fontStyle)
userNameEnt.place(x = 20, y = 80)

passEnt = tk.Entry(width = 10, font = fontStyle)
passEnt.place(x = 20, y = 150)


# running the window (doesn't work without this)
logWin.mainloop()


class UserLogin:
  def __init__(self, name, age):
    self.name = name
    self.age = age
