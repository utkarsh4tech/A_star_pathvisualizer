"""
Project Name: A* Path Finder Visualizer
Author: Utkarsh Sahu
Email: sahuuutkarhs03@gamil.com
Twitter: @Utkarsh4tech ( https://twitter.com/Utkarsh4tech )

Project Description: This is a Visualization tool for helping learners understand 
                    about the A* algorithm. The tech Stack used in Project is 
                    - Pygame and Python.

File Descreption: This file has the Node class and all its member functions.
"""

import pygame as pg
from colors import RED,GREEN,WHITE,BLACK,PURPLE,ORANGE,TURQUOISE

class Node:
    
    def __init__(self,row,col,width,total_rows) -> None:
        self.row=row
        self.col=col
        self.x=row*width
        self.y=col*width
        self.color=WHITE
        self.neighbors=[]
        self.width=width
        self.total_rows=total_rows

    def get_pos(self):
        return self.row,self.col

    def is_open(self):
        return self.color == GREEN

    def is_barrier(self):
        return self.color == BLACK 
    
    def is_start(self):
        return self.color == ORANGE
    
    def is_end(self):
        return self.color == TURQUOISE
    
    def is_closed(self):
        return self.color == RED

    def make_open(self):
        self.color = GREEN

    def make_barrier(self):
        self.color = BLACK 
    
    def make_start(self):
        self.color = ORANGE
    
    def make_end(self):
        self.color = TURQUOISE
    
    def make_closed(self):
        self.color = RED

    def reset(self):
        self.color=WHITE

    def make_path(self):
        self.color=PURPLE

    def draw(self,win):
        pg.draw.rect(win,self.color,(self.x,self.y,self.width,self.width))
    
    def update_neighbors(self,grid):
        self.neighbors=[]

        if self.row < self.total_rows -1 and not grid[self.row+1][self.col].is_barrier():
            self.neighbors.append(grid[self.row+1][self.col])

        if self.col < self.total_rows -1 and not grid[self.row][self.col+1].is_barrier():
            self.neighbors.append(grid[self.row][self.col+1])

        if self.col >0 and not grid[self.row][self.col-1].is_barrier():
            self.neighbors.append(grid[self.row][self.col-1])

        if self.row >0 and not grid[self.row-1][self.col].is_barrier():
            self.neighbors.append(grid[self.row-1][self.col])

    def __lt__(self,width):
        return False
