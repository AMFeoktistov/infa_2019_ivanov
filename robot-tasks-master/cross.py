#!/usr/bin/python3

from pyrob.api import *

def x():
    fill_cell()
    move_right()
    move_down()
    fill_cell()
    move_down()
    move_left()
    fill_cell()
    move_up()
    fill_cell()
    move_left()
    fill_cell()
    move_up()
if __name__ == '__main__':
    run_tasks()
