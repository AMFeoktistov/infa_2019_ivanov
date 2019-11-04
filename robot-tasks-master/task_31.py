#!/usr/bin/python3

from pyrob.api import *


            
@task(delay=0.01)
def task_8_30():
    lenght_of_raw = 1
    while not wall_is_on_the_left():
         move_left()
         lenght_of_raw += 1
    x = 1
    while x < lenght_of_raw:
        while not wall_is_on_the_right():
            if wall_is_beneath():
                move_right()
                x += 1
            elif not wall_is_beneath():
                move_down()
                x = 0
        while not wall_is_on_the_left():
            if wall_is_beneath():
                move_left()
                x += 1
            elif not wall_is_beneath():
                move_down()
                x = 0  
    while not wall_is_on_the_left():
         move_left()

if __name__ == '__main__':
    run_tasks()
