from computer import *

item_nmb = int

class ResaleShop:

    # What attributes will it need?
    inventory = [] # Computer objects will go in here
    item_nmb = 0 # Sets number in inventory to 0

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        pass # You'll remove this when you fill out your constructor

    # What methods will you need?
    def buy(self, inventory: list, computer):
        item_nmb += 1
        inventory[item_nmb] = computer
        return item_nmb
    


        # 1. call Computer(...) constructor to create a new Computer instance

        # 2. call inventory.append(...) to add the new Computer instance to the inventory