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
food = Tile(10*TILE_SIZE, 10*TILE_SIZE) # Célula inicial da comida
velocity_x = 0
velocity_y = 0

def change_direction(event):
    # print(event.keysym) #  Mostra as teclas que pressiono
    global velocity_x, velocity_y

    if (event.keysym == "Up"):
        velocity_x = 0
        velocity_y = -1
    elif (event.keysym == "Down"):
        velocity_x = 0
        velocity_y = 1
    elif (event.keysym == "Left"):
        velocity_x = -1
        velocity_y = 0
    elif (event.keysym == "Right"):
        velocity_x = 1
        velocity_y = 0


# Função para mover a cobra
def move():
    global snake

    snake.x += velocity_x * TILE_SIZE
    snake.y += velocity_y * TILE_SIZE


def draw():
    global snake
    move()

    canvas.delete("all")

    # Desenhando a cobra
    canvas.create_rectangle(snake.x, snake.y, snake.x + TILE_SIZE, snake.y + TILE_SIZE, fill="lime green")

    # Desenhando a comida
    canvas.create_rectangle(food.x, food.y, food.x + TILE_SIZE, food.y + TILE_SIZE, fill="red")
    
    window.after(100, draw) # Chama a função draw a cada 100ms

draw()

window.bind("<KeyRelease>", change_direction)
window.mainloop()
