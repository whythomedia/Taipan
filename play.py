import sys
import math
import random
import Tkinter as tk
import tkMessageBox as tkm
from buy import *
from sell import *






def proper_name(item):
	first = item[0].upper()
	output = first + item[1:len(item)]
	return output


def play(self):
    if self.volume == -999:
        self.initialize()
    else:
        self.TKupdate()
        self.TKresponse.set('What do you want to do?')
        self.entry.bind("<Return>", self.value_in)


def move(self):
    action = self.action
    action_item = self.action_item
    self.TKupdate()
    if self.boat_fill() == 0 and self.boat['money'] == 0:
        self.TKresponse.set("You have no money and no goods, you lose!")
#        elif action == 'help':
#        need to build a new help function for TK frame
    elif action == 'sell' or action == 'buy':
        if action_item == "":
            self.TKresponse.set("What would you like to %s?" % (action))
            self.entry.bind("<Return>", self.value_in)
        else:
            text = "How many %s would you like to %s?" % (self.action_item,action)
            self.TKresponse.set(text)
            self.entry.bind("<Return>", self.get_user_number)
        #self.entry.pack()
    elif action == 'sail':
        self.TKresponse.set("Ah, the open sea!\n Where to Captain?")
        self.entry.bind("<Return>", self.get_user_number)

    elif action == 'quit' or action =='q':
        text = "I knew you weren't fit for sailing %s!\n" % (self.player_name)
        self.TKresponse.set(text)
    else:
        self.TKresponse.set("It is not lawful to do that here:\nIf you don't know ask for help")
        self.action = ""
        self.action_item = ""
        self.entry.bind("<Return>", self.value_in)

    return

def new_boat(self):
    if self.boat["money"] > 50:
        cost =  int(math.floor(self.boat["money"]/2))
        capacity = int(math.floor(self.boat["money"]/50))
        text = "Would you like to increase your ship's capacity by %s for %s money?" % (capacity,cost)
        if tkm.askyesno("New Ship",text):
            self.boat["money"] -= cost
            self.boat["capacity"] += capacity
            self.TKupdate()

    return
