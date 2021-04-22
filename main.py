import UserLogin
#import Game

UserLogin.log_in_win()

player = str(UserLogin.get_user_name())

print(player)

if player == "":
    exit()
else:
    import Game
    Game.main_menu(player)