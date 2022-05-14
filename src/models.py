import pygame
import random
from src.utility import Utility as consts

class Mole(pygame.sprite.Sprite):
  def __init__(self,position,state,img,holeList):
    '''
    initializes the image and the positions 
    arg=position, state, img
    return= none
  
    '''
    super().__init__()
    self.image = pygame.image.load(img)
    self.rect = self.image.get_rect()
    self.rect.x = position[0]
    self.rect.y = position[1]

    self.animation_frame = consts.MOLE
    self.animation_folder = "assets/moleAnims"
    self.state = state

    self.holeList = holeList

  def updateMiss(self):
    '''
    if the mole is not hit, the mole/bomb randomly respawns in another hole
    arg= none
    return= none
    '''

    
    index = random.randint(0,8)

    bombChance = random.randint(0,8)
    chanceList = [7,8]
    #swithc btwn bomb and mole
    if bombChance in chanceList:
      self.state = 0
      self.image = pygame.image.load(consts.IMAGEBOMB) 

    else:
      self.state = 2
      self.image = pygame.image.load(consts.IMAGEMOLE)
    self.rect.x = self.holeList[index].moleAbove()[0]
    self.rect.y = self.holeList[index].moleAbove()[1]
      

    
  def updateHit(self):
    '''
    determines what happens if the mole/bomb is hit, if state is 1, then the bomb looks like the exlode img, 3, then mole looks injured png. 
    arg= none
    return=none
    '''
    bombChance = random.randint(0,8)
    
    #swithc btwn bomb and mole
    index= random.randint(0,8)
    if bombChance == 8:
      self.state = 0
      self.image = pygame.image.load(consts.IMAGEBOMB)
      self.rect.x = self.holeList[index].moleAbove()[0]
      self.rect.y = self.holeList[index].moleAbove()[1]
    #

    if self.state == 1:
      self.image = pygame.image.load(consts.IMAGEBOMBHIT)
    if self.state == 3:
      self.image = pygame.image.load(consts.IMAGEMOLEHIT)


class Hole(pygame.sprite.Sprite):
  def __init__(self,position):
    '''
    initializes the image and the positions
    arg= position
    return= none
    
    '''
    super().__init__()
    self.image = pygame.image.load(consts.IMAGEHOLE)
    self.image = pygame.transform.scale(self.image,(consts.HOLEWIDTH, consts.HOLEHEIGHT))
    
    self.rect = self.image.get_rect()
    self.rect.x = position[0]
    self.rect.y = position[1]

    
  def moleAbove(self):
    '''
    returns the x and y positions of where the mole above should be
    arg= none
    return= self.rect.x, self.rect.y
    
    '''
    return (self.rect.x,self.rect.y - 65 )


