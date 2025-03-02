import webbrowser
from game import Game


# Actions when ...
def change_state(new_state):
    Game.CURRENT_STATE = new_state
def redirect(link):
    webbrowser.open(link)