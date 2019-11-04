#!/usr/bin/python3

from pyrob.api import *




@task(delay=0.01)

def task_9_3():
    x = -1
    while not wall_is_on_the_right():
        move_right()
        x += 1
        if not wall_is_on_the_right():
            fill_cell()
    y = 0
    z = x + 1
    move_down()
    while x>=0:
        x -= 2
        y += 1
        for i in range(y):
            fill_cell()
            move_left()
        if x>0:
            move_left()
        for i in range(x):
            fill_cell()
            move_left()
        for i in range(y):
            move_left()
            fill_cell()
        move_right(z)
        move_down()
    while not (wall_is_on_the_left() and wall_is_beneath()):
        x += 2
        y -= 1
        for i in range(y):
            fill_cell()
            move_left()
        if x>0:
            move_left()
        for i in range(x):
            fill_cell()
            move_left()
        for i in range(y):
            move_left()
            fill_cell()
        if not (wall_is_on_the_left() and wall_is_beneath()):
            move_right(z)
            move_down()




if __name__ == '__main__':
    run_tasks()
