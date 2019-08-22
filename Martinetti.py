# Class for a die with a default of six sides and a roll method
class Die :
    # Constructer
    def __init__( self, sidenum = 6 ) :
        import random
        self.sides = sidenum
        self.num = 1

    # returns the number of sides in a string
    def __str__( self ) :
        return "Number of sides: " + str( self.sides) + " Side up: " + str(self.num)

    # returns the side that is currently up
    def getNum( self ) :
        return self.num

    # randomly selects one of the sides
    def roll( self ) :
        import random
        self.num = random.randint(1,self.sides)
    
