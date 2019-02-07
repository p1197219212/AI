from flask import Flask, make_response
from enum import Enum
from flask_restful import reqparse, Api, Resource, abort
import random

#Create webserver

bot = Flask(__name__)

#API
api = Api(bot)

#API Arguments
parser = reqparse.RequestParser()
parser.add_argument('lastOpponentMove')
parser.add_argument('opponentName')
parser.add_argument('pointsToWin', type=int)
parser.add_argument('maxRounds', type=int)
parser.add_argument('dynamiteCount',type=int)
'''
count = 0
result = []
'''
#Game state
class GameState():
    oppPreviousMoves = list()
    turnCount = 0
    opponentName = ""
    pointsToWin = 0
    maxRounds = 0
    dynamiteCount = 0
#Available moves
class Actions(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    DYNAMITE = 4
    WATERBOMB = 5
    '''
class NumberCheck():
    numberrock = 0
    numberscissors = 0
    numberpaper = 0
    numberdynamite = 0
    numberwaterbomb = 0
    prock = 0
    pscissors = 0
    ppaper = 0
    pdynamite = 0
    pwaterbomb = 0
'''

class Move(Resource):
    game_state = None
    '''
    number_check = None
'''
    def __init__(self,**kwargs):
        self.game_state = kwargs['game_state']
        '''
        self.number_check = kwargs['number_check']
        '''
    #Return bot's move for next round
    #Make changes here
    
    def get(self):

        #Increment turn count
        self.game_state.turnCount = self.game_state.turnCount + 1

        #Respond randomly
        '''
        b = len(self.game_state.oppPreviousMoves)
        if b > 0:
            
            if self.game_state.oppPreviousMoves[-1] == "ROCK":
                self.number_check.numberrock += 1
            if self.game_state.oppPreviousMoves[-1] == "PAPER":
                self.number_check.numberpaper += 1
            if self.game_state.oppPreciousMoves[-1] == "SCISSORS":
                self.number_check.numberscissors += 1
            if self.game_state.oppPreciousMoves[-1] == "DYNAMITE":
                self.number_check.numberdynamite += 1
            if self.game_state.oppPreciousMoves[-1] == "WATERBOMB":
                self.number_check.numberwaterbomb += 1
            self.number_check.prock = self.number_check.numberrock // self.game_state.turnCount
            self.number_check.ppaper = self.number_check.numberpaper // self.game_state.turnCount
            self.number_check.pscissors = self.number_check.numberscissors // self.game_state.turnCount
            self.number_check.pdynamite = self.number_check.numberdynamite // self.game_state.turnCount
            self.number_check.pwaterbomb = self.number_check.numberwaterbomb // self.game_state.turnCount
            if b%9 == 0:
                return make_response(Actions(4).name,200)
            count = random.randint(0,1)+random.randint(1,2)
            return make_response(Actions(count).name,200)
        if b == 0:
            count = random.randint(0,1)+random.randint(1,2)
            return make_response(Actions(count).name,200)
        '''
        return make_response(Actions(random.randint(1,5)).name,200)

    #Recieving opponent's last move
    def post(self):

        #Parse data from post
        args = parser.parse_args()
        print('Opponent used: ' + args['lastOpponentMoveStore last move in the game state'])
        self.game_state.oppPreviousMoves.append(args['lastOpponentMove'])


class Start(Resource):

    game_state = None

    def __init__(self,**kwargs):
        self.game_state = kwargs['game_state']
    
    #Start game
    def post(self):

        #Parse data from post
        args = parser.parse_args()

        #Set game state
        self.game_state.opponentName = args['opponentName']
        self.game_state.pointsToWin = args['pointsToWin']
        self.game_state.maxRounds = args['maxRounds']
        self.game_state.dynamiteCount = args['dynamiteCount']

        #Clear from previous game
        self.game_state.oppPreviousMoves = list()
        self.game_state.turnCount = 0

        print('###### Start Game #######')
        print('Opponent Name: ' + self.game_state.opponentName)
        print('Points to win: ' + str(self.game_state.pointsToWin))
        print('Max rounds: ' + str(self.game_state.maxRounds))
        print('Dynamite Count: ' + str(self.game_state.dynamiteCount))

#Init game state
state = GameState()
'''
numberCheck = NumberCheck()
'''
#Bind API resources
api.add_resource(Move , '/move', resource_class_kwargs={ 'game_state': state })
'''
                                                        , 'number_check': numberCheck })
                                                        '''
api.add_resource(Start , '/start', resource_class_kwargs={ 'game_state': state })

if __name__ == '__main__':
    #Listen externally on port 80
    bot.run(host='0.0.0.0',port=80)
    
