import tkinter as tk

class Pixel():
    def __init__(self, canvas, line:int, column:int, width_line:int, width_column:int, colour:str="black"):
        self.canvas = canvas
        
        self.line = line
        self.column = column

        self.width_line = width_line
        self.width_column = width_column

        self.colour = colour

        self.create()

    def create(self):
        x1 = self.column*self.width_column
        y1 = self.line*self.width_line
        
        x2 = self.column*self.width_column+self.width_column
        y2 = self.line*self.width_line+self.width_line
        
        self.pixel = self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.colour, outline=self.colour)

    def delete(self):
        self.canvas.delete(self.pixel)

class Grid():
    def __init__(self, window, lines:int, columns:int, width:int, height:int, colour:str="white"):
        self.lines = lines
        self.columns = columns

        self.width = width
        self.width_line = width//lines
        
        self.height = height
        self.width_column = height//columns

        self.colour = colour

        self.canvas = tk.Canvas(window, height=self.height, width=self.width, bg=self.colour)
        self.canvas.pack()

        self.pixels = []

    def pixel(self, line:int, column:int, colour:str="black"):
        if self.pixels != []:
            for i, px in enumerate(self.pixels):
                if px.line == line and px.column == column:
                    px.delete()
                    self.pixels.pop(i)
                    break
            self.pixels.append(Pixel(self.canvas, line, column, self.width_line, self.width_column, colour))
        else:
            if colour != self.colour:
                self.pixels.append(Pixel(self.canvas, line, column, self.width_line, self.width_column, colour))
            

if __name__ == "__main__":

    window = tk.Tk()

    lines = 15
    columns = 15

    height = 600
    width = 600

    my_grid = Grid(window, lines, columns, width, height)

    my_grid.pixel(0, 1, "red")
    
    window.mainloop()
