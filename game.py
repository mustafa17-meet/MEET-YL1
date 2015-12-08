from meet import *
from random import randint
cells=[]

for x in range(30) :
	cell1={"x":randint(-400,400), "y":randint(-400,400), "radius":30, "dy":2, "dx":2,"color":"red"}
	z=create_cell(cell1)
	cells.append(z)
while True:	
	for cell in cells:
		get_screen_width()
		get_screen_height()
		cell.xcor()
		cell.ycor()
		if (cell.x.cor(get_screen_width())):
			cell.setdx(-1)
		if (cell.y.cor(get_screen_height())):
			cell.setdy(-1)
				move_cells(cells)
