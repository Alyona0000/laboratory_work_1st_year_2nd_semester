from tkinter import *
import random

class Ball:

    def __init__(self, canvas, paddle, color, xpos,ypos):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill = color)
        self.canvas.move(self.id, xpos, ypos)

        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()#висота
        self.canvas_width = self.canvas.winfo_width()#ширина

        self.hit_bottom = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

    def draw(self):
        if self.hit_bottom == False:

            self.canvas.move(self.id, self.x, self.y)

            pos = self.canvas.coords(self.id)

            if pos[1] <= 0:
                self.y = 1
            #if pos[3] >= self.canvas_height:
             #   self.y = -1

            if pos[3] >= self.canvas_height:
                self.hit_bottom = True

            if self.hit_paddle(pos) == True:
                self.y = -2

            if pos[0] <= 0:
                self.x = 2
            if pos[2] >= self.canvas_width:
                self.x = -2

            if self.hit_bottom == False:
                self.canvas.after(10, self.draw)

class Paddle:

    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)

        self.x = 0

        self.canvas_width = self.canvas.winfo_width()

        self.canvas.bind_all("<KeyPress-Left>", self.turn_left)
        self.canvas.bind_all("<KeyPress-Right>", self.turn_right)


    def draw(self):
        if ball.hit_bottom == False:

            self.canvas.move(self.id, self.x, 0)

            pos = self.canvas.coords(self.id)
            if pos[0] <= 0:
                self.x = 0
            if pos[2] >= self.canvas_width:
                self.x = 0

            self.canvas.after(10, self.draw)

    def turn_left(self, event):
        self.pos = self.canvas.coords(self.id)

        if self.pos[0] >= 1:
            self.x = -3

    def turn_right(self, event):
        self.pos = self.canvas.coords(self.id)

        if self.pos[2] <= self.canvas_width-1:
            self.x = 3


def start_game(event):
    ball.draw()


tk = Tk()
tk.title("Paddleball Game")
tk.resizable(0,0) # tk вікно не змінює своїх розмірів  x і y
tk.wm_attributes("-topmost", 1) #робить вікно верхнього рівня

canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0,bg = 'lightblue') #відсутність рамок навколо canvas
canvas.pack()
tk.update() # обробляє всі завдання, які стоять в черзі. Зазвичай ця функція використовується під час "важких" розрахунків,
            #коли необхідно щоб залишити програму чуйним на дії користувача.

paddle = Paddle(canvas, "blue")
ball = Ball(canvas, paddle, "red",245,100)

canvas.bind("<Button-1>", start_game)
paddle.draw()

tk.mainloop()
