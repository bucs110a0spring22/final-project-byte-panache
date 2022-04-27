import sys
import pygame
import random
import time
# from src import bombs
# from src import extrapointmole
# from src import fastmole
# from src import moles
from src import posMOLES
from src import fastermole

class Controller: 
  def __init__(self, width= 800, height=400):
    self.screen = pygame.display.set_mode((width, height))
    self.obj_layer = pygame.display.set_mode((width, height))
    self.clock=pygame.time.Clock()
    self.FPS= 30
    self.background=pygame.image.load('assets/Sprites/StartScreen.png').convert_alpha()
    self.game_state= "BEGIN"
    self.width = width
    self.height = height
    
    self.bomb= bomb.Bomb(randrange(400,801,255),255, 'assets/Sprites/Bomb.png')
    self.mole1=mole.Mole1.randrange(400,801,265),255,'assets/Sprites/Mole1.png')
    # self.mole2=mole.Mole2.randrange(400,801,265),255,'assets/Sprites/Mole2.png')
    # self.mole3=mole.Mole3.randrange(400,801,265),255,'assets/Sprites/Mole3.png')
    self.clock= pygame.time.Clock()
    #make self for music later
    self.state= "BEGIN"
  def mainloop(self):
    #select state loop
    while self.alive:
            if self.game_state == "BEGIN":
                self.gameIntroScreen()
            elif self.game_state == "GAME":
                self.gameLoop()
            elif self.game_state == "LOSE":
                self.gameOverScreen()
    
  
  ### below are some sample loop states ###

  def menuloop(self):
    if self.state == "HIT"
      self.mainloop()
    if self.state == "FINISH"
      return
    if self.state =="GAMEOVER"
      self.gameoverloop()


  def gameoverloop(self):
    self.background = pygame.Surface(self.screen.get_size())
    self.gobackground.fill ( (255, 0, 0) )
    self.screen.blit(gobackground, (0,0))
    pygame.display.flip()
