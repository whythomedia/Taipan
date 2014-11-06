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
        self.TKupdate()

        toDo = raw_input('What do you want to do? ')
#        self.TKresponse.set('What do you want to do? ')
#        action = self.entry.bind("<Return>", self.get_response(self.player_name,self.TKplayer_name))

        action = toDo.partition(' ')[0]
        action_item = toDo.partition(' ')[2]
        print action

        if self.boat_fill() == 0 and self.boat['money'] == 0:
            print "You have no money and no goods, you lose!"
            self.TKresponse.set("You have no money and no goods, you lose!")
            working = False
#        elif action == 'help':
#        need to build a new help function for TK frame
        elif action == 'buy':
            buy(self,action_item)
        elif action == 'sell':
            sell(self,action_item)
            print "You have %s dollars on hand." % (self.boat['money'])
        elif action == 'sail':
            print 'Ah, the open sea!'
            self.sail()
        elif action == 'quit' or action =='q':
            print "I knew you weren't fit for sailing %s!\n" % (self.player_name)
            working = False
        else:
            print "It is not lawful to do that here:"
            print "If you don't know ask for help"
