## This is a comment to see if everything is working correctly
## test commit joe
import UserLogin
import Game

UserLogin.log_in_win()

player = str(UserLogin.get_user_name())

print(player)

if player == "":
    exit()
else:
    Game.main_menu(player)