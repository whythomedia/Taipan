import sys
import math
import random

def sell(self,):
	item = self.action_item
	if item == 'nothing':
		self.TKresponse.set("What would you like to do.")
		self.action = ""
		self.action_item = ""
		self.entry.bind("<Return>", self.value_in)
		return
	elif self.boat[item] <= 0:
		self.TKresponse.set("You don't have any of those.\nWhat would you like to sell.")
		self.action_item = ""
		self.entry.bind("<Return>", self.value_in)
		return
	elif item in self.wares:
		if self.volume == -1:
			text = "How many %s would you like to sell?" % (action_item)
			self.TKresponse.set(text)
			self.entry.bind("<Return>", self.get_user_number)
		elif self.volume == 0:
			self.TKresponse.set("What would you like to do.")
			self.action = ""
			self.action_item = ""
			self.volume = -1
			self.entry.bind("<Return>", self.value_in)
		elif self.volume > self.boat[item]:
			self.TKresponse.set("You don't have that many to sell.\nHow many do you want to sell?")
			self.entry.bind("<Return>", self.get_user_number)
		else:
			self.transaction("sell", self.action_item, self.volume)
			return
	else:
		text = "I'm not sure about %s sailor.\nWhat would you like to sell." % (item)
		self.TKresponse.set(text)
		self.action_item = ""
		self.entry.bind("<Return>", self.value_in)

