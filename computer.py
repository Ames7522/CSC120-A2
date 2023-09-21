class Computer:

    # What attributes will it need?
    """
    storing information about a specific computer
    initial opperating system to allow updating a computer's OS
    """
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description: str, processor_type:str,hard_drive_capacity: int,
                 memory: int,operating_system: str,year_made: int,price: float):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
        
        #pass # You'll remove this when you fill out your constructor

    # What methods will you need?
