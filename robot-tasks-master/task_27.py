#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    
    move_right()
    fill_cell()
    x = 0
    i = x
    while not wall_is_on_the_right():
        if x < i:
            move_right()
            x += 1
        else:
            fill_cell()
            i += 1
            x = 0     

        
        


if __name__ == '__main__':
    run_tasks()
