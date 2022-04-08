"""A module to help creating and managing a grid with pixels."""

import tkinter as tk

class Pixel():
    def __init__(self, canvas, line:int, column:int, width_line:int, width_column:int, colour:str="black", outline:str="black"):
        self.canvas = canvas
        
        self.line = line
        self.column = column

        self.width_line = width_line
        self.width_column = width_column

        self.colour = colour
        self.outline = outline

        self.create()

    def create(self):
        y1 = self.column*self.width_column
        x1 = self.line*self.width_line
        
        y2 = self.column*self.width_column+self.width_column
        x2 = self.line*self.width_line+self.width_line
        
        self.pixel = self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.colour, outline=self.outline)

    def delete(self):
        self.canvas.delete(self.pixel)

class Grid():
    """Grid(window, lines:int, columns:int, width:int, height:int, colour:str="white")
Creates a grid."""
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

    def pixel(self, line:int, column:int, colour:str="black", outline:str=""):
        """Grid.pixel(line:int, column:int, colour:str="black", outline:str="")
Changes a specific pixel's colour."""
        if outline == "":
            outline = colour
        if self.pixels != []:
            for i, px in enumerate(self.pixels):
                if px.line == line and px.column == column:
                    px.delete()
                    self.pixels.pop(i)
                    break
            if colour != self.colour:
                self.pixels.append(Pixel(self.canvas, line, column, self.width_line, self.width_column, colour, outline))
        else:
            if colour != self.colour:
                self.pixels.append(Pixel(self.canvas, line, column, self.width_line, self.width_column, colour, outline))

    def clear(self):
        """Clears the entire grid."""
        if self.pixels != []:
            for px in self.pixels:
                px.delete()
            self.pixels = []
            

if __name__ == "__main__":

    window = tk.Tk()

    lines = 15
    columns = 15

    height = 600
    width = 600

    my_grid = Grid(window, lines, columns, width, height)

    my_grid.pixel(7, 7, "red")
    my_grid.pixel(7, 5, "blue")

    my_grid.canvas.after(1000, my_grid.clear)
    
    window.mainloop()
