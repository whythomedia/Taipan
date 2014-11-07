import sys
import math
import random
import Tkinter as tk
from buy import *
from sell import *

def proper_name(item):
	first = item[0].upper()
	output = first + item[1:len(item)]
	return output

def test(event):
    action = str(self.entry.get())
    print action
    main.absolute_truth

def play(self):
    self.TKupdate()

    self.TKresponse.set('What do you want to do?')
    def value_in(event):
        return move(self)
    self.entry.bind("<Return>", value_in)
    self.entry.pack()


def move(self):
    action_item = ""
    action = str(self.entry.get())
    self.entry.delete(0,tk.END)

    if self.boat_fill() == 0 and self.boat['money'] == 0:
        print "You have no money and no goods, you lose!"
        self.TKresponse.set("You have no money and no goods, you lose!")
#        elif action == 'help':
#        need to build a new help function for TK frame
    elif action == 'buy':
        self.TKresponse.set("What would you like to buy?")
        def get_user_city_number(event):
            s = self.entry.get()
            buy(self,s)
        self.entry.bind("<Return>", get_user_city_number)
        self.entry.pack()
        self.entry.delete(0,tk.END)
    elif action == 'sell':
        self.TKresponse.set("What would you like to sell?")
        def get_user_city_number(event):
            s = self.entry.get()
            sell(self,s)
        self.entry.bind("<Return>", get_user_city_number)
        self.entry.pack()
        self.entry.delete(0,tk.END)
    elif action == 'sail':
        self.TKresponse.set("Ah, the open sea!\n Where to Captain?")
        def get_user_city_number(event):
            s = self.entry.get()
            try:
                return  self.sail(int(s) - 1)
                self.entry.delete(0,tk.END)
                self.entry.unbind("<Return>", get_user_city_number)
            except:
                self.TKresponse.set("Come again?")
                self.entry.delete(0,tk.END)
                return
        self.entry.bind("<Return>", get_user_city_number)
        self.entry.pack()
        self.entry.delete(0,tk.END)
    elif action == 'quit' or action =='q':
        text = "I knew you weren't fit for sailing %s!\n" % (self.player_name)
        self.TKresponse.set(text)
    else:
        self.TKresponse.set("It is not lawful to do that here:\nIf you don't know ask for help")
    return
