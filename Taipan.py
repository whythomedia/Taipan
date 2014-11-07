#!/usr/bin/python -tt
import sys
import math
import random
import Tkinter as tk
import tkFont
from play import *
#from buy import *
#from sell import *

app = tk.Tk()
app.title("Taipan")

#--- Build the canvas and fields within
font1 = tkFont.Font(size = '18', weight = 'bold')
font2 = tkFont.Font(size = '18', weight = 'bold')

canvas = tk.Canvas(app, width=800, height=600)
canvas.pack()

img = tk.PhotoImage(file="game.gif")
canvas.create_image(0,0, image=img, anchor = "nw")

aFrame = tk.Frame(canvas, bg = "#e8eaeb")
bFrame = tk.Frame(canvas, bg = "#e8eaeb")
cFrame = tk.Frame(canvas, bg = "#e8eaeb")
dFrame = tk.Frame(canvas, bg = "#e8eaeb")
nameFrame = tk.Frame(canvas, bg = "#404040")
turnFrame = tk.Frame(canvas, bg = "#404040")
cityFrame = tk.Frame(canvas, bg = "#404040")
aBox = canvas.create_window(185, 154, height=175, width=60, anchor = "nw")
bBox = canvas.create_window(440, 154, height=200, width=60, anchor = "nw")
cBox = canvas.create_window(70, 460, height=75, width=600, anchor = "nw")
dBox = canvas.create_window(70, 535, height=25, width=600, anchor = "nw")
nameBox = canvas.create_window(120, 87, height=30, width=90, anchor = "nw")
turnBox = canvas.create_window(370, 87, height=30, width=50, anchor = "nw")
cityBox = canvas.create_window(615, 87, height=30, width=130, anchor = "nw")
canvas.itemconfigure (aBox, window=aFrame)
canvas.itemconfigure (bBox, window=bFrame)
canvas.itemconfigure (cBox, window=cFrame)
canvas.itemconfigure (dBox, window=dFrame)
canvas.itemconfigure (nameBox, window=nameFrame)
canvas.itemconfigure (turnBox, window=turnFrame)
canvas.itemconfigure (cityBox, window=cityFrame)


#--- Fill the boxes on the canvas
def tkfield(parent,var,row,initial,font):
	if font == 2:
		tk.Label(parent, textvariable=var, pady = 0, font = font2, bg = "#404040", fg = "#ffdb00").grid(row=row, column=0, sticky=tk.W )
	else:
		tk.Label(parent, textvariable=var, pady = 0, font = font1, bg = "#e8eaeb", fg = "#404040").grid(row=row, column=0, sticky=tk.W )
	var.set(initial)


#--- The main class that holds all of the boat information
class Taipan:
	#The Game Begins
	wares = ['gold','silk','arms','general']
	boat = {'gold':0,'silk':0,'arms':0,'general':0,'money':100,'capacity':10,'city':0,'health':100}
	original_prices = {'gold':800,'silk':200,'arms':50,'general':10}
	prices = {'gold':1,'silk':1,'arms':1,'general':1}
	actions = ['buy','sell','inventory','run']
	cities = ['Hong Kong','Shanghai','Nagasaki','Saigon','Manila','Singapore','Batavia']
	turn = 1
	player_name = 'Sailor'
	absolute_truth = True


	def transaction(self,direction,item,volume):
		cost = int(self.prices[item]) * int(volume)
		if direction == "buy":
			if cost > self.boat["money"]:
				print "You don't have that much money."
			elif volume == 0:
				print "Buy low, sell high!"
			elif volume > self.boat['capacity']-self.boat_fill():
				volume = self.boat['capacity']-self.boat_fill()
				print "You only have capacity for more %s units." % (volume)
			else:
				self.boat[item] += int(volume)
				self.boat["money"] -= cost
				self.boat["capacity"] -= int(volume)
				print "\nSUCCESS"
				print "That costs you %s dollars." % (cost)
				print "We loaded %s units of %s for you." % (volume, item)
				print "You now have %s units of %s in storage and $%s left." % (self.boat[item], item, self.boat["money"])
				self.TKmoney.set(self.boat['money'])
				self.TKcapacity.set(self.boat['capacity'])
		else:
			self.boat["money"] += int(cost)
			self.boat["capacity"] += int(volume)
			print "\nSUCCESS"
			print "That earns you %s dollars." % (cost)
			print "We unloaded %s units of %s for you." % (volume, item)
			print "You now have %s units of %s in storage and $%s." % (self.boat[item], item, self.boat["money"])
			self.TKmoney.set(self.boat['money'])
			self.TKcapacity.set(self.boat['capacity'])

	def current_prices(self,city):
			for i in self.prices:
					self.prices[i] = self.original_prices[i] * random.randrange(1,6)

	def proper_name(item):
		first = item[0].upper()
		output = first + item[1:len(item)]
		return output

	def get_user_number(self,transaction):
		i = raw_input("How many do you want to %s.\n" % (transaction))
		#if i == 'all':
		#    return 'all'
		#else:
		try:
			return int(i)
		except:
			print("I didn't recognize {0} as a number".format(i))
			return get_user_number(transaction)

	def get_user_city_number(self):
		s = self.entry.get()
		try:
			return  int(s) - 1
		except:
			print("I didn't recognize {0} as a number".format(s))
		#	return self.get_user_city_number()

	def boat_fill(self):
		fill = 0
		for i in self.wares:
			fill += self.boat[i]
		return fill

	def sail(self, number):

		loop = 0
		sail_to = number
		if sail_to == self.boat['city']:
			self.TKresponse.set("\nYou're already there")
			return
		elif sail_to > 6 or 0 > sail_to:
			self.TKresponse.set("No go Captain, thar be sea snakes!")
			return
		else:
			if 1 == random.randrange(1,21):
				print "You got robbed! Your ship was looted while you were asleep."
				for i in self.wares:
					self.boat[i] = int(math.floor(self.boat[i]/2))
			self.boat['city'] = sail_to
			self.TKcity.set(self.cities[sail_to])
			self.turn +=1
			self.TKresponse.set("***** Welcome to %s, turn %s *****\nWhat now Captain?" % (self.cities[sail_to],self.turn))
			self.current_prices(sail_to)

	#--- update the display variables, at least each time through play()
	def TKupdate(self):
		self.TKgold.set(self.boat['gold'])
		self.TKsilk.set(self.boat['silk'])
		self.TKarms.set(self.boat['arms'])
		self.TKgeneral.set(self.boat['general'])
		self.TKMgold.set(self.prices['gold'])
		self.TKMsilk.set(self.prices['silk'])
		self.TKMarms.set(self.prices['arms'])
		self.TKMgeneral.set(self.prices['general'])
		self.TKturn.set(self.turn)


	#--- declare and set all of the variables for display
	def __init__(self):
		self.TKplayer_name = tk.StringVar()
		self.TKturn = tk.IntVar()
		self.TKcity = tk.StringVar()
		self.TKhealth = tk.IntVar()
		self.TKmoney = tk.IntVar()
		self.TKcapacity = tk.IntVar()
		self.TKgold = tk.IntVar()
		self.TKsilk = tk.IntVar()
		self.TKgeneral = tk.IntVar()
		self.TKarms = tk.IntVar()
		self.TKMgold = tk.IntVar()
		self.TKMsilk = tk.IntVar()
		self.TKMgeneral = tk.IntVar()
		self.TKMarms = tk.IntVar()

		self.TKresponse = tk.StringVar()
		self.TKresponse.set("Welcome")

		self.TKgold.set(self.boat['gold'])
		self.TKsilk.set(self.boat['silk'])
		self.TKgeneral.set(self.boat['general'])
		self.TKarms.set(self.boat['arms'])

		tkfield(aFrame,self.TKhealth,0,self.boat['health'],1)
		tkfield(aFrame,self.TKmoney,1,self.boat['money'],1)
		tkfield(aFrame,self.TKcapacity,2,self.boat['capacity'],1)
		tkfield(aFrame,self.TKgold,3,self.boat['gold'],1)
		tkfield(aFrame,self.TKsilk,4,self.boat['silk'],1)
		tkfield(aFrame,self.TKarms,5,self.boat['arms'],1)
		tkfield(aFrame,self.TKgeneral,6,self.boat['general'],1)

		tkfield(bFrame,self.TKMgold,0,0,1)
		tkfield(bFrame,self.TKMsilk,1,0,1)
		tkfield(bFrame,self.TKMarms,2,0,1)
		tkfield(bFrame,self.TKMgeneral,3,0,1)

		tkfield(cFrame,self.TKresponse, 0, self.TKresponse,1)

		self.user = tk.StringVar()
		self.entry = tk.Entry(dFrame, textvariable=self.user, font = font1, bg = "#e8eaeb", fg = "#404040")


		tkfield(nameFrame,self.TKplayer_name,0,self.player_name,2)
		tkfield(turnFrame,self.TKturn,0,self.turn,2)
		tkfield(cityFrame,self.TKcity,0,self.cities[self.boat['city']],2)
#		canvas.create_text(650, 98, textvariable=self.TKcity, fill = "#ffdb00", font = font2)



		Taipan.current_prices(self,self.boat['city'])


		rc = play(self)
		while rc:
			rc = play(self)

# This is the standard boilerplate that calls the main() function.
#if __name__ == '__main__':
Taipan()
app.mainloop()
