#!/usr/bin/python -tt
import sys
import math
import random

wares = ['opium','silk','arms','general']
inventory = {'opium':0,'silk':0,'arms':0,'general':0,'money':100}
original_prices = {'opium':800,'silk':200,'arms':50,'general':10}
prices = {'opium':1,'silk':1,'arms':1,'general':1}
actions = ['buy','sell','inventory','run']
turn = [1,0]
player_name = ''

def main():
    global player_name
    if player_name == '':
        player_name = raw_input("What is your name sailor. ")
    # randomize pricing
    print "\n***** Turn %s *****" % (turn[0])
    if turn[0] != turn[1]:
        global prices
        current_prices()
        turn[1] +=1
    print "\nYou have $%s" % (inventory['money'])

    for i in wares:
        print "$%s for %s" % (prices[i],proper_name(i))

    action = raw_input('What do you want to do? ')


    if action == 'help':
        print "You can:"
        for i in actions:
          print i
    elif action == 'buy':
        buy()
    elif action == 'sell':
        sell()
    elif action == 'inventory':
        print "\n---- %s's Master Inventory ----" % (player_name)
        for i in wares:
            print "You have %s of %s." % (inventory[i],i)
        print "You have %s dollars on hand." % (inventory['money'])
        main()
    elif action == 'market':
        for i in wares:
            print "$%s for %s" % (prices[i],proper_name(i))
        main()
    elif action == 'run':
        print 'Coward, you lose a turn!'
        turn[0] += 1
        main()
    elif action == 'quit' or action =='q':
        print "I knew you weren't fit for sailing %s!\n" % (player_name)
    else:
        print "It is not lawful to do that here:"
        print "If you don't know ask for help"
        main()


def buy():
    item = raw_input('What do you want to buy? ')
    item = item.lower()
    if inventory["money"] == 0:
        print 'You have no money!'
        main()
    elif item in wares and inventory["money"] < prices[item]:
        print "You are too poor!"
        main()
    elif item in wares:
        print "You have $%s, %s is $%s per unit" % (inventory["money"],item,prices[item])
        max_volume = int(math.floor(inventory["money"] / prices[item]))
        print "You can buy up to %s %s" % (max_volume,item)
        count = get_user_number('buy')
        if count == 'all':
            count = max_volume
        inventory[item] += count
        transaction("buy", item, count)
        main()
    elif item == 'help':
        for i in wares:
            print i
        buy()
    elif item == 'nothing':
        main()
    else:
        print "We have no %s" % (item)
        print "If you don't know ask for help"
        buy()

def sell():
    item = raw_input('What do you want to sell? ')
    item = item.lower()
    if item not in wares:
        print "You have no %s" % (item)
        main()
    elif inventory[item] <= 0:
        print "You don't have any of those to sell"
        main()
    elif item in wares:
        print "You have %s units of %s, it is worth $%s per unit" % (inventory[item],item,prices[item])
        count = get_user_number('sell')
        if count =='all':
            count = inventory[item]
        elif count > inventory[item]:
            print "You don't have that many to sell, you only have %s units of %s." % (inventory[item], item)
            sell()
        else:
            inventory[item] -= count
            transaction("sell", item, count)
            main()
    elif item == 'help':
        for i in wares:
            print "You have %s units of %s" % (inventory[i], i)
        sell()
    elif item == 'nothing':
        main()
    else:
        print "If you don't know ask for help"
        sell()

def transaction(direction,item,volume):
    cost = int(prices[item]) * int(volume)
    global turn
    if direction == "buy":
        if cost > inventory["money"]:
            print "You don't have that much money."
        else:
            inventory["money"] -= cost
            print "\nSUCCESS"
            print "That costs you %s dollars." % (cost)
            print "We loaded %s units of %s for you." % (volume, item)
            print "You now have %s units of %s in storage and $%s left." % (inventory[item], item, inventory["money"])
            turn[0] += 1
    else:
        inventory["money"] += cost
        print "\nSUCCESS"
        print "That earns you %s dollars." % (cost)
        print "We unloaded %s units of %s for you." % (volume, item)
        print "You now have %s units of %s in storage and $%s." % (inventory[item], item, inventory["money"])
        turn[0] += 1

def current_prices():
        global original_prices
        global prices
        for i in prices:
                prices[i] = original_prices[i] * random.randrange(1,5)

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

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
