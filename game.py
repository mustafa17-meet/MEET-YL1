from meet import *
from random import randint
cells=[]

for x in range(15) :
	cell1={"x":randint(-100,100), "y":randint(-100,100), "radius":30, "dy":2, "dx":2,"color":"red"}
	z=create_cell(cell1)
	cells.append(z)
while True:	
	for cell in cells:
		get_screen_width()
		get_screen_height()
		cell.xcor()
		cell.ycor()
		move_cells(cells)
		if (cell.xcor()>get_screen_width()):
			cell.set_dx(-cell.get_dx())
		if (cell.ycor()>get_screen_height()):
			cell.set_dy(-cell.get_dy())
		if (cell.xcor()<-get_screen_width()):
			cell.set_dx(-cell.get_dx())
		if (cell.ycor()<-get_screen_height()):
			cell.set_dy(-cell.get_dy())


def collide(cells):
	 	for i in cells:
	 		for j in cells:
	 				distance = (o.xcor() - j.xcor())**2 + (i.ycor()- j.ycor())**2)**.5
					if distance <= i.get_radius()+ j.get_radius()):
						i.set_radius(i.get_radius()+1)
						x = meet.get_random_x()
						y = meet.get_random_y()
						j.goto(x,y)
					else
						user_cell.clear()
						user_cells.remove(user_cell)
						write		