#!/usr/bin/python -tt
import sys
import math
import random
import Tkinter as tk

app = tk.Tk()
app.title("Taipan")


#The Game Begins
wares = ['gold','silk','arms','general']
boat = {'gold':0,'silk':0,'arms':0,'general':0,'money':100,'capacity':10,'city':0}
original_prices = {'gold':800,'silk':200,'arms':50,'general':10}
prices = {'gold':1,'silk':1,'arms':1,'general':1}
actions = ['buy','sell','inventory','run']
cities = ['Hong Kong','Shanghai','Nagasaki','Saigon','Manila','Singapore','Batavia']
turn = 1
player_name = ''

def main():
    global player_name
    if turn == 1:
        pname = raw_input("What is your name sailor. ")
        player_name = pname
        TKplayer_name.set(pname)
    print "\n***** Welcome to Hong Kong! *****"
    current_prices(boat['city'])
    play()

def play():
    global boat
    working = True
    while working:
        TKturn.set(turn)
        print "\nYou have $%s" % (boat['money'])

        for i in wares:
            print "$%s for %s" % (prices[i],proper_name(i))

        toDo = raw_input('What do you want to do? ')
        action = toDo.partition(' ')[0]
        action_item = toDo.partition(' ')[2]

        if boat_fill() == 0 and boat['money'] == 0:
            print "You have no money and no goods, you lose!"
            working = False
        elif action == 'help':
            print "You can:"
            for i in actions:
              print i
        elif action == 'buy':
            buy(action_item)
        elif action == 'sell':
            sell(action_item)
        elif action == 'inventory':
            print "\n---- %s's Master Inventory ----" % (player_name)
            for i in wares:
                print "You have %s of %s." % (boat[i],i)
            print "You have %s dollars on hand." % (boat['money'])
        elif action == 'market':
            for i in wares:
                print "$%s for %s" % (prices[i],proper_name(i))
        elif action == 'sail':
            print 'Ah, the open sea!'
            sail()
        elif action == 'quit' or action =='q':
            print "I knew you weren't fit for sailing %s!\n" % (player_name)
            working = False
        else:
            print "It is not lawful to do that here:"
            print "If you don't know ask for help"


def buy(action_item):
    if action_item.lower() in wares:
        item = action_item
    else:
        item = raw_input('What do you want to buy? ')
        item = item.lower()
    if boat["money"] == 0:
        print 'You have no money!'
        return
    elif item in wares and boat["money"] < prices[item]:
        print "You are too poor!"
        return
    elif item in wares:
        print "\nYou have $%s, %s is $%s per unit" % (boat["money"],item,prices[item])
        max_volume = int(math.floor(boat["money"] / prices[item]))
        print "You have money to buy up to %s %s" % (max_volume,item)
        print "Your ship can hold %s more units." % (boat['capacity']-boat_fill())
        count = get_user_number('buy')
        transaction("buy", item, count)
        return
    elif item == 'help':
        for i in wares:
            print i
        buy(action_item)
    elif item == 'nothing':
        return
    else:
        print "We have no %s" % (item)
        print "If you don't know ask for help"
        buy(action_item)

def sell(action_item):
    if action_item.lower() in wares:
        item = action_item
    else:
        item = raw_input('What do you want to sell? ')
        item = item.lower()
    if item not in wares:
        print "You have no %s" % (item)
        return
    elif boat[item] <= 0:
        print "You don't have any of those to sell"
        return
    elif item in wares:
        print "You have %s units of %s, it is worth $%s per unit" % (boat[item],item,prices[item])
        count = get_user_number('sell')
        if count > boat[item]:
            print "You don't have that many to sell, you only have %s units of %s." % (boat[item], item)
            sell(item)
        else:
            boat[item] -= count
            transaction("sell", item, count)
            return
    elif item == 'help':
        for i in wares:
            print "You have %s units of %s" % (boat[i], i)
        sell()
    elif item == 'nothing':
        return
    else:
        print "If you don't know ask for help"
        sell()

def transaction(direction,item,volume):
    cost = int(prices[item]) * int(volume)
    global turn
    global boat
    if direction == "buy":
        if cost > boat["money"]:
            print "You don't have that much money."
        elif volume == 0:
            print "Buy low, sell high!"
        elif volume > boat['capacity']-boat_fill():
            volume = boat['capacity']-boat_fill()
            print "You only have capacity for more %s units." % (volume)
        else:
            boat[item] += volume
            boat["money"] -= cost
            boat["capacity"] -= volume
            print "\nSUCCESS"
            print "That costs you %s dollars." % (cost)
            print "We loaded %s units of %s for you." % (volume, item)
            print "You now have %s units of %s in storage and $%s left." % (boat[item], item, boat["money"])
            TKmoney.set(boat['money'])
            TKcapacity.set(boat['capacity'])
    else:
        boat["money"] += cost
        boat["capacity"] += volume
        print "\nSUCCESS"
        print "That earns you %s dollars." % (cost)
        print "We unloaded %s units of %s for you." % (volume, item)
        print "You now have %s units of %s in storage and $%s." % (boat[item], item, boat["money"])
        TKmoney.set(boat['money'])
        TKcapacity.set(boat['capacity'])


def current_prices(city):
        global original_prices
        global prices
        for i in prices:
                prices[i] = original_prices[i] * random.randrange(1,6)

def proper_name(item):
    first = item[0].upper()
    output = first + item[1:len(item)]
    return output

def get_user_number(transaction):
    i = raw_input("How many do you want to %s.\n" % (transaction))
    #if i == 'all':
    #    return 'all'
    #else:
    try:
        return int(i)
    except:
        print("I didn't recognize {0} as a number".format(i))
        return get_user_number(transaction)

def get_user_city_number():
    s = raw_input("Where do you want to go? ")
    try:
        return  int(s) - 1
    except:
        print("I didn't recognize {0} as a number".format(s))
        return get_user_city_number()

def boat_fill():
    fill = 0
    for i in wares:
        fill += boat[i]
    return fill

def sail():
    global prices
    global turn
    global cities
    global boat
    print " "
    loop = 0
    for i in cities:
        print "%s: %s" % (loop+1,i)
        loop += 1
    sail_to = get_user_city_number()
    if sail_to == boat['city']:
        print "\nYou're already there, pick somewhere else"
        sail()
    elif sail_to > 6 or 0 > sail_to:
        print "\nNo go Captain, thar be sea snakes!"
        sail()
    else:
        if 1 == random.randrange(1,21):
            print "You got robbed! Your ship was emptied while you were asleep."
            for i in wares:
                boat[i] = 0
        boat['city'] = sail_to
        TKcity.set(cities[sail_to])
        turn +=1
        print "\n***** Welcome to %s, turn %s *****" % (cities[sail_to],turn)
        current_prices(sail_to)



# Interface

TKplayer_name = tk.StringVar()
TKplayer_name.set(player_name)
TKturn = tk.IntVar()
TKturn.set(turn)
TKcity = tk.StringVar()
TKcity.set(cities[boat['city']])
TKcapacity = tk.IntVar()
TKcapacity.set(boat['capacity'])
TKmoney = tk.IntVar()
TKmoney.set(boat['money'])
TKgold = tk.IntVar()
TKgold.set(boat['gold'])
TKsilk = tk.IntVar()
TKsilk.set(boat['silk'])
TKgeneral = tk.IntVar()
TKgeneral.set(boat['general'])
TKarms = tk.IntVar()
TKarms.set(boat['arms'])

tk.Label(app, text="Player Name: ").grid(row=0, column=0)
tk.Label(app, textvariable=TKplayer_name).grid(row=0, column=1)
tk.Label(app, text='Turn: ').grid(column=0, row=1, sticky=tk.E)
tk.Label(app, textvariable=TKturn).grid(column=1, row=1, sticky=tk.W)
tk.Label(app, text='City: ').grid(column=0, row=2, sticky=tk.E)
tk.Label(app, textvariable=TKcity).grid(column=1, row=2, sticky=tk.W)
tk.Label(app, text='Money: ').grid(column=0, row=3, sticky=tk.E)
tk.Label(app, textvariable=TKmoney).grid(column=1, row=3, sticky=tk.W)
tk.Label(app, text='Capacity: ').grid(column=0, row=4, sticky=tk.E)
tk.Label(app, textvariable=TKcapacity).grid(column=1, row=4, sticky=tk.W)
#tk.Label(app, text='Money: ').grid(column=0, row=5, sticky=tk.E)
#tk.Label(app, textvariable=TKmoney).grid(column=1, row=5, sticky=tk.W)




# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
