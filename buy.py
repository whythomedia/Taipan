import sys
import math
import random

def buy(self,action_item):
	if action_item.lower() in self.wares:
		item = action_item
	else:
		item = raw_input('What do you want to buy? ')
		item = item.lower()
	if self.boat["money"] == 0:
		print 'You have no money!'
		return
	elif item in self.wares and self.boat["money"] < self.prices[item]:
		print "You are too poor!"
		return
	elif item in self.wares:
		print "\nYou have $%s, %s is $%s per unit" % (self.boat["money"],item,self.prices[item])
		max_volume = int(math.floor(self.boat["money"] / self.prices[item]))
		print "You have money to buy up to %s %s" % (max_volume,item)
		print "Your ship can hold %s more units." % (self.boat['capacity']-self.boat_fill())
		count = self.get_user_number('buy')
		self.transaction("buy", item, count)
		return
	elif item == 'help':
		for i in self.wares:
			print i
	elif item == 'nothing':
		return
	else:
		print "We have no %s" % (item)
		print "If you don't know ask for help"
