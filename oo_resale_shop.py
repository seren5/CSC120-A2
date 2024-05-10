from computer import *



class ResaleShop:

    # What attributes will it need?
    # inventory = {} # Computer objects will go in here
    # itemNumber = 0 # Sets number in inventory to 0

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory = []
        self.itemNumber = 0
        


    # What methods will you need?
    def printInventory(self):
        '''Prints inventory'''
        if self.itemNumber == 0:
            print("No inventory to show.")
        else:
            return self.inventory
            for i in range(len(self.inventory)):
                print(self.inventory[i])

    def buy(self, computer):
        '''Buys computer'''
        self.inventory.append(computer)
        self.itemNumber = len(self.inventory)
        return self.itemNumber
    
    def sell(self, computer_id):
        '''Sells computer'''
        if computer_id in self.inventory:
            self.inventory.remove[computer_id]
            print("Done! ", computer_id, "is now sold.")
        else:
            print(computer_id, " not found. Please choose another item to sell.")
    
    def refurbish(self, itemNumber: int, new_os: str):
        '''Refurbishes computer'''
        if self.itemNumber in self.inventory:
            computer = self.inventory[itemNumber]
            if int(computer["year made"]) < 2000:
                computer["price"] = 0
            elif int(computer["year made"]) < 2014:
                computer["price"] = 250
            elif int(computer["price"]) < 2020:
                computer["price"] = 500
            else:
                computer["price"] = 1000

            if self.new_os:
                self.computer.update_os(new_os)
        else:
            print("Item", itemNumber, "not found. Please select another item to refurbish.")
        # 1. call Computer(...) constructor to create a new Computer instance

        # 2. call inventory.append(...) to add the new Computer instance to the inventory

def main():
    # First, let's make a computer
    computer = Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )
    shop = ResaleShop()
    print(shop.buy(computer))
    print(shop.buy(computer))
    # print(shop.printInventory)
    # print(shop.sell(computer))
    # print(shop.refurbish(2, "Sonoma"))


if __name__ == "__main__": main()