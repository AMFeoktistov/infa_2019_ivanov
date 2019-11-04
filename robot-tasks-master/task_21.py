#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    move_right()
    move_down()
    fill_cell()
    x = 1
    for i in range(13):
        for i in range(x):
            fill_cell()
            move_right()
        move_left(x)
        move_down()
        x += 1


if __name__ == '__main__':
    run_tasks()
