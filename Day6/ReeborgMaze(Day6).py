#Sticks to the right wall and moves to goal
#All commands are defined in reeborg's keyboard!
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()