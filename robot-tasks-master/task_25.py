#!/usr/bin/python3

from pyrob.api import *
from cross import x

@task

def task_2_2():
    
    move_right()
    move_down()
    for i in range(4):
        x()
        move_right(5)
    x()
        
        
if __name__ == '__main__':
    run_tasks()
