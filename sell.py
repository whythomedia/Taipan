import sys
import math
import random

def sell(self,action_item):
	if action_item.lower() in self.wares:
		item = action_item
	else:
		item = raw_input('What do you want to sell? ')
		item = item.lower()
	if item == 'help':
		for i in self.wares:
			print "You have %s units of %s" % (self.boat[i], i)
	elif item == 'nothing':
		return
	elif item not in self.wares:
		print "You have no %s" % (item)
		return
	elif self.boat[item] <= 0:
		print "You don't have any of those to sell"
		return
	elif item in self.wares:
		print "You have %s units of %s, it is worth $%s per unit" % (self.boat[item],item,self.prices[item])
		count = self.get_user_number('sell')
		if count > self.boat[item]:
			print "You don't have that many to sell, you only have %s units of %s." % (self.boat[item], item)
			sell(self,item)
		else:
			self.boat[item] -= count
			self.transaction("sell", item, count)
			return
	else:
		print "If you don't know ask for help"
