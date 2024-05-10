class Computer:

    # What attributes will it need?
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description: str,
    processor_type: str, 
    hard_drive_capacity: int,
    memory: int,
    operating_system: str,
    year_made: int,
    price: int):
        '''Defines attributes'''
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    # What methods will you need?
    def updatePrice(self, new_price: int):
        ''' Updates Price of Computer'''
        if (self.inventory.contains(Computer)):
            self.price = new_price
            return self.price # print updating price in main
        else:
            print("You cannot update the price of a computer you don't have!")
        

    def updateOS(self, new_OS:str):
        '''Updates operating system'''
        self.operating_system = new_OS
        return self.operating_system