#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    while not wall_is_beneath():
        fill_cell()
        while not wall_is_on_the_right():
            move_right()
            fill_cell()
        move_down()
        fill_cell()
        while not wall_is_on_the_left():
            move_left()
            fill_cell()
        if not wall_is_beneath():
            fill_cell()
            move_down()
        
    if wall_is_beneath() and wall_is_on_the_left():
        while not wall_is_on_the_right():
            move_right()
            fill_cell()
        while not wall_is_on_the_left():
            move_left()
        fill_cell()
    if wall_is_beneath() and wall_is_on_the_right():
        while not wall_is_on_the_left():
            move_left()
            fill_cell()
            
            
if __name__ == '__main__':
    run_tasks()
