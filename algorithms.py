"""
Project Name: A* Path Finder Visualizer
Author: Utkarsh Sahu
Email: sahuuutkarhs03@gamil.com
Twitter: @Utkarsh4tech ( https://twitter.com/Utkarsh4tech )

Project Description: This is a Visualization tool for helping learners understand 
                    about the A* algorithm. The tech Stack used in Project is 
                    - Pygame and Python.

File Descreption: This file has all the Algorithms needed to run the a_star.py file.
                    It has the heuristic function that guides the algorithm and the main algorithm.

A* Mathematical Definition : f (n) = g(n)+h(n),
                        where f(n) = total estimated cost of path through node
                        g(n) is the cost of the path from the start node to n,
                        and h(n) is a heuristic function that estimates the cost of
                        the cheapest path from n to the goal.
"""

from queue import PriorityQueue
import pygame as pg

def heuristic(point1,point2): 
    x1,y1=point1
    x2,y2=point2
    manhattan_distance = abs(x1-x2) + abs(y1-y2)
    return manhattan_distance

def construct_path(came_from,curr,draw):
    while curr in came_from:
        curr=came_from[curr]
        curr.make_path()
        draw()

def a_star_algorithm(draw,grid,start,end):
    count=0
    open_set=PriorityQueue()
    open_set.put((0,count,start))
    came_from={}

    g_score={node: float("inf") for row in grid for node in row}
    g_score[start]=0

    f_score={node: float("inf") for row in grid for node in row}
    f_score[start]= heuristic(start.get_pos(),end.get_pos())

    open_set_hash={start}

    while not open_set.empty():

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

        curr =open_set.get()[2]
        open_set_hash.remove(curr)

        if curr == end:
            construct_path(came_from,curr,draw)
            start.make_start()
            end.make_end()
            return True
        
        for neighbor in curr.neighbors:
            temp_g_score=g_score[curr]+1
            if temp_g_score < g_score[neighbor]:
                came_from[neighbor]=curr
                g_score[neighbor]=temp_g_score
                f_score[neighbor]=temp_g_score + heuristic(neighbor.get_pos(),end.get_pos())

                if neighbor not in open_set_hash:
                    count+=1
                    open_set.put((f_score[neighbor],count,neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()

        draw()

        if curr != start:
             curr.make_closed()

    return False
