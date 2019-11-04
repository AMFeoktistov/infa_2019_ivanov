#!/usr/bin/python3

from pyrob.api import *
from cross import x

@task(delay=0.02)
def task_2_4():
    for i in range (5):
        move_right(2)
        while not wall_is_on_the_right():
            move_left()
            x()
            move_right(6)
        move_left()
        x()
        move_left(36)
        if i == 4:
            break
        move_down(4)
    
    
if __name__ == '__main__':
    run_tasks()
