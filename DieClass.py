# Class for a die with a default of six sides and a roll method
class Die :

    # Constructer
    def __init__( self, sidenum = 6 ) :
        import random
        self.sides = sidenum

    # returns the number of sides in a string
    def __str__( self ) :
        return "Number of sides: " + str( self.sides)

    # randomly selects one of the sides
    def roll( self ) :
        return random.randint(1, self.sides)
    
