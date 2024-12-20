import tkinter 
import random 

ROWS = 25
COLS = 25
TILE_SIZE = 25

WINDOW_WIDTH = TILE_SIZE * ROWS
WINDOW_HEIGHT = TILE_SIZE * COLS

class Tile:
    def _init_(self, x, y):
        self.x = x
        self.y = y
   

#game window
window = tkinter.Tk()
window.title("Snake")
window.resizable(False, False)

canvas = tkinter.Canvas(window, bg = "black", width = WINDOW_WIDTH, height = WINDOW_HEIGHT, borderwidth = 0, highlightthickness = 0 )
canvas.pack()
window.update()

#center the window
WINDOW_WIDTH = window.winfo_width()
WINDOW_HEIGHT = window.winfo_height()
SCREEN_WIDTH = window.winfo_screenwidth()
SCREEN_HEIGHT = window.winfo_screenheight()

window_x = int((SCREEN_WIDTH/2) - (SCREEN_WIDTH/2))
window_y = int((SCREEN_HEIGHT/2) - (SCREEN_HEIGHT/2))
window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{window_x}+{window_y}")

#initialize game
snake = Tile(5*TILE_SIZE, 5*TILE_SIZE) #sinle tile fot the snakes head
food = Tile(10*TILE_SIZE, 10*TILE_SIZE)

def draw():
    global snake

    #draw snake
    canvas.create_rectangle(snake.x, snake.y, + TILE_SIZE, snake.y + TILE_SIZE, fill= "lime green")

    #draw food
    canvas.create_rectangle(food.x, food.y + TILE_SIZE, food.y + TILE_SIZE, fill = "red")

    window.after(100, draw)

draw()


window.mainloop()