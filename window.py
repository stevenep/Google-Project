from tkinter import *
from settings import *

window = Tk()
window.title("Snake game")
window.resizable(False, False)

window.geometry(f"{GAME_WIDTH}x{GAME_HEIGHT}")

label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()