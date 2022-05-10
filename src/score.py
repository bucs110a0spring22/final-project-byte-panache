
class Score():
  def __init__ (self, bestScore):
    self.bestTime = bestScore

  def newScore(self, currentScore):
    if currentScore < self.bestTime: 
      self.bestTime= currentScore
  
