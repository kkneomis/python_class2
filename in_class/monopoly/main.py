from utils import roll_pair, check_doubles

roll_again = True
current_roll = roll_pair()
jail_counter = 0

while roll_again:
    if jail_counter == 3:
        print "Go to jail"
        break

    if check_doubles(current_roll):
       	jail_counter += 1
	if jail_counter == 3:
       	    print "Go to jail"
            break 
        
        print "DOUBLES!"
        print "Move %s spaces" % sum(current_roll)        
        current_roll = roll_pair()
    else:
        print "Move %s spaces" % sum(current_roll)
        roll_again = False


