import tkinter
import random

ROWS = 25
COLS = 25
TILE_SIZE = 25

WINDOW_WIDTH = TILE_SIZE * COLS
WINDOW_HEIGHT = TILE_SIZE * ROWS

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Criar a janela
window = tkinter.Tk()
window.title("Snake")
window.resizable(False, False)

# Aqui é onde o jogo será desenhado
canvas = tkinter.Canvas(window, bg = "black", width=WINDOW_WIDTH, height=WINDOW_HEIGHT, borderwidth=0, highlightthickness=0)
canvas.pack()
window.update_idletasks()

# Centralizando a janela na tela
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int(screen_width // 2) - (window_width // 2)
window_y = int(screen_height // 2) - (window_height // 2)

# Definir a geometria da janela
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

# Iniciar o jogo
snake = Tile(5*TILE_SIZE, 5*TILE_SIZE) # Célula inicial da cobra

def draw():
    global snake

    # Desenhando a cobra
    canvas.create_rectangle(snake.x, snake.y, snake.x + TILE_SIZE, snake.y + TILE_SIZE, fill="lime green")
    
    window.after(100, draw) # Chama a função draw a cada 100ms

draw()
window.mainloop()
