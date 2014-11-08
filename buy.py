import sys
import math
import random

def buy(self):
	item = self.action_item
	volume = self.volume
	cost = int(self.prices[item]) * int(volume)
	if item == 'nothing':
		self.TKresponse.set("What would you like to do.")
		self.action = ""
		self.action_item = ""
		self.entry.bind("<Return>", self.value_in)
		return
	elif self.boat["money"] < self.prices[item]:
		self.TKresponse.set("You don't have that much money.")
		self.action_item = ""
		self.entry.bind("<Return>", self.value_in)
		return
	elif item in self.wares:
		if self.volume == -1:
			text = "How many %s would you like to buy?" % (action_item)
			self.TKresponse.set(text)
			self.entry.bind("<Return>", self.get_user_number)
		elif self.volume == 0:
			self.TKresponse.set("What would you like to do.")
			self.action = ""
			self.action_item = ""
			self.volume = -1
			self.entry.bind("<Return>", self.value_in)
		elif self.boat["money"] < cost:
			self.TKresponse.set("You don't have that much money.\nHow many would you like to buy.")
			self.volume = -1
			self.entry.bind("<Return>", self.get_user_number)
			return
		elif volume > self.boat['capacity']-self.boat_fill():
			#volume = self.boat['capacity']-self.boat_fill()
			self.TKresponse.set("You don't have that much room left.\nHow many would you like to buy.")
			self.volume = -1
			self.entry.bind("<Return>", self.get_user_number)
		else:
			self.transaction("buy", self.action_item, self.volume)
			return
	else:
		text = "I'm not sure about %s sailor.\nWhat would you like to sell." % (item)
		self.TKresponse.set(text)
		self.action_item = ""
		self.entry.bind("<Return>", self.value_in)
