import sys
import math
import random
from buy import *
from sell import *

def proper_name(item):
	first = item[0].upper()
	output = first + item[1:len(item)]
	return output


def play(self):
    working = True
    while working:
        self.TKturn.set(self.turn)
        print "\nYou have $%s" % (self.boat['money'])

        for i in self.wares:
            print "$%s for %s" % (self.prices[i],proper_name(i))

        toDo = raw_input('What do you want to do? ')
        action = toDo.partition(' ')[0]
        action_item = toDo.partition(' ')[2]
        print action

        if self.boat_fill() == 0 and self.boat['money'] == 0:
            print "You have no money and no goods, you lose!"
            working = False
        elif action == 'help':
            print "You can:"
            for i in self.actions:
              print i
        elif action == 'buy':
            buy(self,action_item)
        elif action == 'sell':
            sell(self,action_item)
        elif action == 'inventory':
            print "\n---- %s's Master Inventory ----" % (self.player_name)
            for i in self.wares:
                print "You have %s of %s." % (self.boat[i],i)
            print "You have %s dollars on hand." % (self.boat['money'])
        elif action == 'market':
            for i in self.wares:
                print "$%s for %s" % (self.prices[i],proper_name(i))
        elif action == 'sail':
            print 'Ah, the open sea!'
            self.sail()
        elif action == 'quit' or action =='q':
            print "I knew you weren't fit for sailing %s!\n" % (self.player_name)
            working = False
        else:
            print "It is not lawful to do that here:"
            print "If you don't know ask for help"
