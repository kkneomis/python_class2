"""Some helpful functions"""
from dice import Dice
def roll_pair():
    """
    Rolls a pair of dice
    Returns a list with the results
    """
    d1 = Dice()
    roll =  d1.roll()
    print "You rolled a %s and a %s" % (roll[0], roll[1])

    return roll

def check_doubles(pair):
    """
    @params: list with two dice results
    return True or false
    """
    if pair[0] == pair[1]:
        return True
    else:
        return False

