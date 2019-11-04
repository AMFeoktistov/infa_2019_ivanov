#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_11():
    a = wall_is_above
    b = wall_is_beneath
    if not a():
        move_up()
        fill_cell()
        move_down()
    if a() and b():
        fill_cell()
    if not b():
        move_down()
        fill_cell()
        move_up()
    while not wall_is_on_the_right():
        move_right()
        if not a():
            move_up()
            fill_cell()
            move_down()
        if not b():
            move_down()
            fill_cell()
            move_up()
        if a() and b():
           fill_cell()
        


if __name__ == '__main__':
    run_tasks()
