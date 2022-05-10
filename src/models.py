import pygame
import random
import src.constants as consts

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
    self.frame = state
    self.state = state

    self.holeList = holeList

  def updateMiss(self):
    '''
    if the mole is not hit, the mole/bomb randomly respawns in another hole
    arg= none
    return= none
    '''
    index = random.randint(0,8)
    (self.rect.x,self.rect.y) = self.holeList[index].getPosition()
    
  def updateHit(self):

    '''
    determines what happens if the mole/bomb is hit, if state is 1, then the bomb looks like the exlode img, 3, then mole looks injured png. 
    arg= none
    return=none
    '''
    
    if self.state == 1:
      self.image = pygame.image.load(consts.BOMB_HIT)
    if self.state == 3:
      self.image = pygame.image.load(consts.MOLE_HIT)
      self.image = pygame.transform.scale(consts.MOLEWIDTH, consts.MOLEHEIGHT)


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

    
  def getPosition(self):
    '''
    returns the x and y positions of the rectangle
    arg= none
    return= self.rect.x, self.rect.y
    
    '''
    return (self.rect.x,self.rect.y)


