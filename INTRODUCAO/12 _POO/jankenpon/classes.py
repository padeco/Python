import os
import time
import random

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

clearConsole()

class Menu:
    def menu(self):
            print('''                                                                                              
                                                                                                    
          `7MMF'                     `7MM                                                            
            MM                         MM                                                            
            MM   ,6"Yb.  `7MMpMMMb.    MM  ,MP' .gP"Ya  `7MMpMMMb.  `7MMpdMAo.  ,pW"Wq.  `7MMpMMMb.  
            MM  8)   MM    MM    MM    MM ;Y   ,M'   Yb   MM    MM    MM   `Wb 6W'   `Wb   MM    MM  
            MM   ,pm9MM    MM    MM    MM;Mm   8M""""""   MM    MM    MM    M8 8M     M8   MM    MM  
       (O)  MM  8M   MM    MM    MM    MM `Mb. YM.    ,   MM    MM    MM   ,AP YA.   ,A9   MM    MM  
        Ymmm9   `Moo9^Yo..JMML  JMML..JMML. YA. `Mbmmd' .JMML  JMML.  MMbmmd'   `Ybmd9'  .JMML  JMML.
                                                                      MM                             
                                                                    .JMML.                           ''')

    
                

class Participant:
  def __init__(self, name):
    self.name = name
    self.points = 0
    self.choice = ""
  def choose(self):
    self.choice = input("{name}, select rock, paper or scissor: ".format(name= self.name))
    print("{name} selects {choice}".format(name=self.name, choice = self.choice))
  def toNumericalChoice(self):
    switcher = {
      "rock": 0,
      "paper": 1,
      "scissor": 2,
    }
    return switcher[self.choice]
  def incrementPoint(self):
    self.points += 1 

class GameRound:
  def __init__(self, p1, p2):
    self.rules = [
 [0, -1, 1],
 [1, 0, -1],
 [-1, 1, 0]
] 

    p1.choose()
    p2.choose()
    result = self.compareChoices(p1,p2)
    print("Round resulted in a {result}".format(result = self.getResultAsString(result) ))
    if result > 0:
      p1.incrementPoint()
    elif result < 0:
      p2.incrementPoint()
    else:
      print("No points for anybody")
    
  def compareChoices(self, p1, p2):
    return self.rules[p1.toNumericalChoice()][p2.toNumericalChoice()]
  def awardPoints(self):
    print("implement")
  def getResultAsString(self, result):
    res = {
      0: "draw",
      1: "win",
      -1: "loss"
    }
    return res[result]

class Game:
  def __init__(self):
    self.endGame = False
    self.participant = Participant("kirk")
    self.secondParticipant = Participant("Spock")
  def start(self):
    while not self.endGame:
      GameRound(self.participant, self.secondParticipant)
      self.checkEndCondition()
      
  def checkEndCondition(self):
     answer = input("Continue game y/n: ")
     if answer == 'y':
        GameRound(self.participant, self.secondParticipant)
        self.checkEndCondition()
     else:
       print("Game ended, {p1name} has {p1points}, and {p2name} has {p2points}".format(p1name = self.participant.name, p1points= self.participant.points, p2name=self.secondParticipant.name, p2points=self.secondParticipant.points))
       self.determineWinner()
       self.endGame = True
  def determineWinner(self):
    resultString = "It's a Draw"
    if self.participant.points > self.secondParticipant.points:
      resultString = "Winner is {name}".format(name=self.participant.name)
    elif self.participant.points < self.secondParticipant.points:
      resultString = "Winner is {name}".format(name=self.secondParticipant.name)
    
    print(resultString)  

