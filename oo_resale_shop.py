from computer import *



class ResaleShop:

    # What attributes will it need?
    # inventory = {} # Computer objects will go in here
    # item_nmb = 0 # Sets number in inventory to 0

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory = {}
        self.item_nmb = 0

    # What methods will you need?
    def view_inventory(self):
        if self.item_nmb == 0:
            print("No inventory to show.")
        else:
            print(self.inventory[self.item_nmb])

    def buy(self, computer):
        self.item_nmb += 1
        self.inventory[self.item_nmb] = computer
        return self.item_nmb
    
    def sell(self, computer_id):
        if computer_id in self.inventory:
            self.inventory.remove[computer_id]
            print("Done! ", computer_id, "is now sold.")
        else:
            print(computer_id, " not found. Please choose another item to sell.")
    
    def refurbish(self, item_nmb: int, new_os: str):
        if self.item_nmb in self.inventory:
            computer = self.inventory[item_nmb]
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
            print("Item", item_nmb, "not found. Please select another item to refurbish.")
        # 1. call Computer(...) constructor to create a new Computer instance

        # 2. call inventory.append(...) to add the new Computer instance to the inventory

def main():
    print("hello")
    # First, let's make a computer
    computer = Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )
    shop = ResaleShop()
    # print(shop.buy(computer))
    # print(shop.buy(computer))
    # print(shop.view_inventory)
    # print(shop.sell(computer))
    print(shop.refurbish(new_os))


if __name__ == "__main__": main()