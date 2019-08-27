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
            elif( num2 == self.boardList[self.boardPos]) :
                self.boardPos += 1
            elif( num3 == self.boardList[self.boardPos]) :
                self.boardPos += 1
            elif( num1 + num2 == self.boardList[self.boardPos]) :
                self.boardPos += 1
            elif( num1 + num3 == self.boardList[self.boardPos]) :
                self.boardPos += 1
            elif( num2 + num3 == self.boardList[self.boardPos]) :
                self.boardPos += 1
            elif( num1 + num2 + num3 == self.boardList[self.boardPos]) :
                self.boardPos += 1
            if( self.boardPos == 11 or self.boardPos == 23) :
                break
        return self.boardPos

class Player:

    def __init__( self, playerName ) :
        self.gameBoard = Board()
        self.name = playerName

    def __str__( self ) :
        return self.name

    def hasWon( self ) :
        if( self.gameBoard.boardPos == 23):
            return True
        return False
        
            
class Game:

    def __init__ ( self, numPlayers) :
        self.players = []
        for i in range(1, numPlayers + 1) :
            self.players.append(Player(input("What will player " + str(i) + "'s name be? ")))   

    def play( self) :
        space = -1
        die1 = Die()
        die2 = Die()
        die3 = Die()
        self.ended = False
        print ("The game has begun!")
        while( self.ended == False) :
            for player in self.players :
                print ("It's " + player.__str__() + "'s turn")
                space = player.gameBoard.boardPos
                die1.roll()
                die2.roll()
                die3.roll()
                print (player.__str__() + " rolled a " + str(die1.getNum()) + ", " + str(die2.getNum()) + ", and " + str(die3.getNum()))
                player.gameBoard.moveUp(die1.getNum(), die2.getNum(), die3.getNum())
                if space != player.gameBoard.boardPos : 
                    print (player.__str__() + " moved to space " + str(player.gameBoard.boardPos +1))
                if player.hasWon() :
                    print (player.__str__() + " has won!")
                    self.ended = True
                    break
        
