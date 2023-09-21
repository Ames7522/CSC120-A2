class ResaleShop:

    # What attributes will it need?
    """
storing the inventory for the store
updating a computer's price
updating a computer's OS
buying a computer (add to inventory)
selling a computer (remove from inventory)
refurbishing a computer
    """
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, inventory: int, itemID: int ):
        self.inventory = inventory
        self.itemID = itemID
        
        #pass # You'll remove this when you fill out your constructor

    # What methods will you need?
