#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    n = 0
    while not wall_is_on_the_right():
        if n < 3:
            move_right()
            if cell_is_filled():
                n += 1
            else:
                n = 0
        else:
            break


if __name__ == '__main__':
    run_tasks()
