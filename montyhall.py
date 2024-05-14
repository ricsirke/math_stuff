# -*- coding: utf-8 -*-

import numpy as np


num_of_trials = 500000
X = np.random.randint(1, 4, size=num_of_trials) # generating the winning doors

wins_no_switch = 0
wins_switch = 0

choice = 1
for win_door in X:  
    
    ### NO SWITCH ###
    if win_door == choice:
        wins_no_switch += 1
    
    ### SWITCH ###
    # opening a door without the car, nor our choice
    doors = {2, 3}
    doors.discard(win_door) # dropping the winning door
    door_opened = doors.pop() # getting an other door

    doors = {2, 3} # we won't chose the already chosen door
    doors.discard(door_opened) # removing the opened door
    new_door = doors.pop() # getting the new door
    if win_door == new_door:
        wins_switch += 1
    
        
prob_win_no_switch = float(wins_no_switch) / num_of_trials
prob_win_switch    = float(wins_switch) / num_of_trials

print("prob of win without switch:\t", prob_win_no_switch)
print("prob of win with switch:\t", prob_win_switch)