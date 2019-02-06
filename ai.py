# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 16:31:37 2019

@author: user
"""

from flask import Flask, make_response
from enum import Enum
from flask_restful import reqparse, Api, Resource, abort
import random

#Create webserver
name = "bo"
bot = Flask(name)

#API
api = Api(bot)

#API Arguments
parser = reqparse.RequestParser()
parser.add_argument('lastOpponentMove')
parser.add_argument('opponentName')
parser.add_argument('pointsToWin', type=int)
parser.add_argument('maxRounds', type=int)
parser.add_argument('dynamiteCount',type=int)


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


class Move(Resource):
    game_state = None
    number_check = None

    def __init__(self,**kwargs):
        self.game_state = kwargs['game_state']

    #Return bot's move for next round
    #Make changes here
    def get(self):

        #Increment turn count
        self.game_state.turnCount = self.game_state.turnCount + 1

        #Respond randomly
        
        if self.game_state.oppPreviousMoves[-1] = "ROCK":
            self.number_check.numberrock += 1
        if self.game_state.oppPreviousMoves[-1] = "PAPER":
            self.number_check.numberpaper += 1
        if self.game_state.oppPreciousMoves[-1] = "SCISSORS":
            self.number_check.numberscissors += 1
        if self.game_state.oppPreciousMoves[-1] = "DYNAMITE":
            self.number_check.numberdynamite += 1
        if self.game_state.oppPreciousMoves[-1] = "WATERBOMB":
            self.number_check.numberwaterbomb += 1
        self.number_check.prock = self.number_check.numberrock // self.game_state.turnCount
        self.number_check.ppaper = self.number_check.numberpaper // self.game_state.tur