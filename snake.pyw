import pixels as px
import tkinter as tk
from random import randint

class Snake():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("snake")

        self.lines = 15
        self.columns = 15

        self.width = 210
        self.height = 210
        
        self.grid = px.Grid(self.window, self.lines, self.columns, self.width, self.height, "yellow green")

        self.canvas = self.grid.canvas

        self.window.bind("<Up>", self.up)
        self.window.bind("<Down>", self.down)
        self.window.bind("<Right>", self.right)
        self.window.bind("<Left>", self.left)

        self.setup()

        self.window.mainloop()

    def setup(self, key=None):
        self.window.bind("<Return>", self.do_nothing)
        
        self.grid.clear()

        self.points = 0
        
        self.positions = [[2, self.lines//2], [1, self.lines//2], [0, self.lines//2]]
        self.dir_x = 1
        self.dir_y = 0
                
        for pos in range(len(self.positions)):
            self.grid.pixel(self.positions[pos][0], self.positions[pos][1], "blue", "black")
            
        self.start = True
        self.stop = False

        self.apple_pos = []
        self.set_apple()

        self.snake()

    def snake(self):
        if self.start is False:
            nbr_pos = len(self.positions)-1
            self.grid.pixel(self.positions[nbr_pos][0], self.positions[nbr_pos][1], "yellow green") 
            
            for i in range(len(self.positions)-1, -1, -1):
                if i != 0:
                    self.positions[i] = self.positions[i-1][::]

            self.positions[0][0] += self.dir_x
            self.positions[0][1] += self.dir_y

            last_pos = []
            for i, pos in enumerate(self.positions):
                if i != 0:
                    last_pos.append(pos)

            if self.positions[0] == self.apple_pos:
                self.positions.append(self.positions[len(self.positions)-2][::])
                self.set_apple()

            if self.positions[0] in last_pos:
                self.game_over()

            elif self.positions[0][0] >= self.columns or self.positions[0][0] < 0:
                self.game_over()

            elif self.positions[0][1] >= self.lines or self.positions[0][1] < 0:
                self.game_over()
                
            else:            
                for pos in self.positions:
                    self.grid.pixel(pos[0], pos[1], "blue", "black")

        else:
            self.start = False
            
        if self.stop != True:
            self.canvas.after(100, self.snake)

    def up(self, key):
        if self.dir_x != 0 and self.dir_y != -1:
            self.dir_x = 0
            self.dir_y = -1

    def down(self, key):
        if self.dir_x != 0 and self.dir_y != 1:
            self.dir_x = 0
            self.dir_y = 1

    def right(self, key):
        if self.dir_x != 1 and self.dir_y != 0:
            self.dir_x = 1
            self.dir_y = 0
    
    def left(self, key):
        if self.dir_x != -1 and self.dir_y != 0:
            self.dir_x = -1
            self.dir_y = 0
                
    def set_apple(self):
        if self.apple_pos != []:
            self.grid.pixel(self.apple_pos[0], self.apple_pos[1], "yellow green")
            
        x = randint(0, self.columns-1)
        y = randint(0, self.lines-1)

        while [x, y] in self.positions:
            x = randint(0, self.columns-1)
            y = randint(0, self.lines-1)

        self.apple_pos = [x, y]

        self.grid.pixel(x, y, "red", "black")

    def game_over(self):
        self.stop = True
        
        for pos in self.positions:
            self.grid.pixel(pos[0], pos[1], "red", "black")
        
        self.window.bind("<Return>", self.setup)

        self.grid.clear()
        self.canvas.after(1000, self.show_points)

    def show_points(self):
        if self.points < len(self.positions)-3:
            x, y = 0, self.points
            while y >= self.columns:
                x += 1
                y -= self.columns
            self.points += 1
            self.grid.pixel(y, x, "red", "black")
            self.canvas.after(75, self.show_points)

    def do_nothing(self, key=None):
        pass
        

snake = Snake()
