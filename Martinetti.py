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
    

# Class that tracks the position of players on the gameboard and moves them
class Board:

    def __init__ ( self ) :
        self.boardList = [1,2,3,4,5,6,7,8,9,10,11,12,11,10,9,8,7,6,5,4,3,2,1]
        self.boardPos = 0

    def __str__ ( self ) :
        return "Board Position: " + str(self.boardPos)
    def moveUp( self, num1, num2, num3) :
        tracker = self.boardPos - 1
        while( tracker < self.boardPos) :
            tracker = self.boardPos
            if( num1 == self.boardList[self.boardPos]) :
                self.boardPos += 1
            else if( num2 == self.boardList[self.boardPos]) :
                self.boardPos += 1
            else if( num3 == self.boardList[self.boardPos]) :
                self.boardPos += 1
            else if( num1 + num2 == self.boardList[self.boardPos]) :
                self.boardPos += 1
            else if( num1 + num3 == self.boardList[self.boardPos]) :
                self.boardPos += 1
            else if( num2 + num3 == self.boardList[self.boardPos]) :
                self.boardPos += 1
            else if( num1 + num2 + num3 == self.boardList[self.boardPos]) :
                self.boardPos += 1
            if( self.boardPos == 11 or self.boardPos == 23) :
                break
        return self.boardPos

class Player:

    def __init__( self, playerName ) :
        gameBoard = Board()
        self.name = playerName

    def __str__( self ) :
        return playerName

    def hasWon( self ) :
        if( self.gameBoard.boardPos == 23):
            return True
        return False
        
            
class Game:
    
