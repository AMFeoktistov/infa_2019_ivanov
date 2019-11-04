#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
    if not wall_is_on_the_right():
        move_right(9)
    else:
        move_left(9)
    if not wall_is_above():
        move_up(9)
    else:
        move_down(9)

if __name__ == '__main__':
    run_tasks()
