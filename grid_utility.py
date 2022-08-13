from node import Node
import pygame as pg
from colors import GREY,WHITE

def make_grid(rows,width):
    grid=[]
    gap=width//rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node=Node(i,j,gap,rows)
            grid[i].append(node)

    return grid

def draw_grid(win,rows,width):
    gap=width//rows
    for i in range(rows):
        pg.draw.line(win,GREY,(0,i*gap),(width,i*gap))
        for j in range(rows):
            pg.draw.line(win,GREY,(j*gap,0),(j*gap,width))

def draw(win,grid,rows,width):
    win.fill(WHITE)

    for row in grid:
        for node in row:
            node.draw(win)

    draw_grid(win,rows,width)
    pg.display.update()

def get_clicked_pos(pos,rows,width):
    gap = width // rows
    y,x=pos
    row=y//gap
    col=x//gap

    return row,col
