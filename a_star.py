"""
Project Name: A* Path Finder Visualizer
Author: Utkarsh Sahu
Email: sahuuutkarhs03@gamil.com
Twitter: @Utkarsh4tech ( https://twitter.com/Utkarsh4tech )

Project Description: This is a Visualization tool for helping learners understand 
                    about the A* algorithm. The tech Stack used in Project is 
                    - Pygame and Python.

File Descreption: This is the file to be run to start the visualisation.
                    Contains the main function and Pygame Action settings.
 
A* Algorithm: A* Search algorithm is one of the best and popular 
            technique used in path-finding and graph traversals.
            A* is a modification of Dijkstra’s Algorithm that is optimized for a single destination.
            Dijkstra’s Algorithm can find paths to all locations; 
            A* finds paths to one location, or the closest of several locations.
            It prioritizes paths that seem to be leading closer to a goal.

            The secret to its success is that it combines the pieces of information that
            Dijkstra’s Algorithm uses (favoring vertices that are close to the starting point) 
            and information that Greedy Best-First-Search uses (favoring vertices that are close to the goal). 
"""

import pygame as pg
from algorithms import a_star_algorithm
from grid_utility import make_grid,draw,get_clicked_pos

WIDTH = 650
WIN = pg.display.set_mode((WIDTH,WIDTH))
pg.display.set_caption("A* Star PathFinder")

def main(win,width):
    ROWS=50
    grid=make_grid(ROWS,width )

    start,end=None,None
    run=True
    while run:

        draw(win,grid,ROWS,width)

        for event in pg.event.get():

            if event.type == pg.QUIT:
                run=False
                
            if pg.mouse.get_pressed()[0]: #LEFT CLICK
                """
                If the node is clicked by Left Click we calculate the position
                then we get the node corresponding to that position.
                We make the node corresponding to the first node as START,
                node corresponding to the second node as END
                and all the nodes thereafter as Barriers
                """
                pos=pg.mouse.get_pos()
                row,col=get_clicked_pos(pos,ROWS, width)
                node= grid[row][col]

                if not start and node != end:
                    start=node
                    start.make_start()
                
                elif not end and node != start:
                    end=node
                    end.make_end()

                elif node != end and node != start:
                    node.make_barrier()

            elif pg.mouse.get_pressed()[2]: #RIGHT CLICK
                """
                If the node is clicked by right click of mouse
                we use it to reset the position.
                """

                pos=pg.mouse.get_pos()
                row,col=get_clicked_pos(pos,ROWS, width)
                node= grid[row][col]
                node.reset()

                if node == start:
                    start = end
                
                if node == end :
                    end = None

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE and start and end:
                    # If space is pressed we start the algorithm
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)     

                    a_star_algorithm(lambda:draw(win,grid,ROWS,width),grid,start,end)  

                if event.key == pg.K_c:
                    # if 'C' is pressed we clear the screen
                    start=None
                    end=None
                    grid=make_grid(ROWS,width) 

    pg.quit()

if __name__=="__main__":
    main(WIN,WIDTH)