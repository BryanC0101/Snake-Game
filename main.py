import tkinter
import random

ROWS = 25
COLS = 25
TITLE_SIZE = 25

WINDOW_WIDTH = TITLE_SIZE * ROWS
WINDOW_HEIGHT = TITLE_SIZE * COLS

# Criar a janela
window = tkinter.Tk()
window.title("Snake")
window.resizable(False, False)

# Aqui é onde o jogo será desenhado
canvas = tkinter.Canvas(window, bg = "black", width=WINDOW_WIDTH, height=WINDOW_HEIGHT, borderwidth=0, highlightthickness=0)
canvas.pack()
window.update()


window.mainloop()
