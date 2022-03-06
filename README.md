# Tkinter-grid
---
A grid for Tkinter, Python. You can control every box in the grid (useful for simple graphics in Tkinter).

## Pixels
You can control each "pixel"'s colour with the `Grid()` class.

## Grid
You don't need to create a canvas on your Tkinter window, the `Grid()` class does it for you.

### Initialization
`my_grid = Grid(window, lines:int, columns:int, width:int, height:int, colour:str="white")`
- `lines` : number of lines on your grid
- `columns` : number of columns on your grid
- `width` : your grid's width
- `height` : your grid's height
- `colour` : your grid's colour (default is white)

### Methods
- `Grid.pixel(line:int, column:int, colour:str="black")`
