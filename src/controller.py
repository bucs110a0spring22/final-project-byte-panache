import sys
import time
import pygame
import random
import src.models as model 
from src.utility import Utility as Consts
from threading import Thread


class Controller:

  def setUpHoles(self):
    '''
    sets up the holes through determining the distance between the screen. makes an index of all the hole possible positions
    arg= none
    return= holeList= index of hole possible positions    
    '''
    # Placing and making holes
    holeList = []
    startX = (self.SCREENWIDTH/4)
    startY = (self.SCREENHEIGHT/4)
    xCord = 0
    yCord = 0

    for hole in range(9):
      if hole % 3 == 0:
        xCord = (startX)
        yCord += (startY)
      else:
        xCord += startX
        
      holeList.append(model.Hole((xCord,yCord)))
    return holeList


  
  def __init__(self,SCREENWIDTH = Consts.SCREENWIDTH, SCREENHEIGHT = Consts.SCREENHEIGHT):
    '''
    initializes the screen, variables, scorekeep, etc
    arg= none
    return= none
    
    '''

    #Setting up screen
    pygame.font.init()
    self.state = "gameplay"
    self.SCREENWIDTH = SCREENWIDTH
    self.SCREENHEIGHT = SCREENHEIGHT
    self.screen = pygame.display.set_mode((self.SCREENWIDTH,self.SCREENHEIGHT), pygame.FULLSCREEN)
    # Color in RGB format
    color = (43, 92, 44)
    self.screen.fill(color)
    self.clock = pygame.time.Clock()
    self.FPS = 30
    self.font = pygame.font.SysFont("Monospace",15)

      
    # Setting up holes
    holeArray = self.setUpHoles()
    self.holeList = pygame.sprite.Group()
    for hole in holeArray:
      self.holeList.add(hole)
    
    # Setting up mole and clock
    index = random.randint(0,8)
    self.mole = model.Mole(holeArray[index].moleAbove(), Consts.MOLE,Consts.IMAGEMOLE,holeArray)


    self.clock = pygame.time.Clock()
    self.time = 0

    self.all_sprites = pygame.sprite.Group(tuple(self.holeList,) + (self.mole,))
    
    # Death Screen setup
    self.img_death = pygame.image.load((Consts.IMAGEDEATHSCREEN)).convert_alpha()

    # Game logic setup
    self.alive = True
    self.lives = 3
    self.score = 0

    #color of the score
    self.black= (0, 0, 0)
    self.white = (255, 255, 255)

    #create timer for stunned mole
    self.timestunned = 0

    # Update screen with the background we just added
    pygame.display.flip()
  

  

  def menuloop(self):
    '''
    description: determines which loop the game is gonna run --> gameplay, death, exit
    arg= none
    return= none
    
    '''
    while self.alive:
      if self.state == "gameplay":
        self.gameloop()
      elif self.state == "death":
        self.deathScreen()
      elif self.state == "exit":
        self.exitloop()

  def gameloop(self):
    '''
    main loop of the function, player hit the moles/bombs. Accounts for if either the mole or the bomb was hit, determines the lives of the player and the point per mole. Makes the clock tick, mole updates depending on time clicked. 
    arg= none
    return= none
    
    '''
  
    # make cursor
    cursor= pygame.image.load(Consts.IMAGEHAMMER)

    while self.state == "gameplay":
      
      #Make clock tick so that mole only moves after a certain amount of time

      #makes cursor and finds cursor position
      pygame.mouse.set_visible(False)
      x,y=pygame.mouse.get_pos()
      x -= cursor.get_width()/2
      y-= cursor.get_height()/2
      self.screen.blit(cursor,(x,y))
      pygame.display.update()

      #mole updates when hit.missed
      
      dt = self.clock.tick()
      self.time += dt
      self.timestunned += dt
      color= (43, 92, 44)
      if self.time >= Consts.MOLEWAIT:
          self.time = 0
          self.mole.updateMiss()
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
          pos = pygame.mouse.get_pos()
          if self.checkClick(pos):
            if self.timestunned >= 200:
              self.time = 0
              self.mole.updateHit()
              self.mole.state = Consts.MOLE

      if self.lives == 0:
        self.state= "death"
        self.menuloop()
            
      
    
      #fix the moles duplicating by filling screen green after each position
      self.screen.fill(color)
      
      # make the score show up at the top of the screen
      myfont= pygame.font.SysFont('Monospace', 20)
      message = myfont.render('Score: '+ str(self.score), False, (self.white))
      self.screen.blit(message, [200, 60])

      message2= myfont.render('Lives: ' + str(self.lives), False, (self.white))
      self.screen.blit(message2, [450, 60])

      Title= myfont.render('Whack-A-Digett', False, (self.white))
      self.screen.blit(Title, [300,10])

      self.all_sprites.draw(self.screen)
      pygame.display.flip()

  
  
  def checkClick(self,mousePos):
    '''
    checks if the click was in the rect of the mole or the bomb, adds a point or removes a life depending
    arg= mousePos= mouse position
    return = true or false depending if the mole/bomb is clicked
    
    '''
    if self.mole.rect.collidepoint(mousePos):
      if self.mole.state == Consts.MOLE:
        def task(self):
          time.sleep(1)
          self.mole.image = pygame.image.load(Consts.IMAGEMOLE)
          self.mole.state = Consts.MOLE
        imgchange = Thread(target=task, args=(self,))
        self.mole.image = pygame.image.load(Consts.IMAGEMOLEHIT)
        self.score += Consts.SCOREGAP
        self.mole.state = Consts.MOLE_HIT
        
        imgchange.start()
        

      if self.mole.state == Consts.BOMB:
        self.lives += -1
        self.mole.image = pygame.image.load(Consts.IMAGEBOMB)
        self.mole.state = Consts.BOMB_HIT

      elif self.mole.state == Consts.BOMB_HIT:
        self.mole.image = pygame.image.load(Consts.IMAGEBOMBHIT)
        self.mole.state = Consts.MOLE
        
      return True
    return False

    
  def deathScreen(self):
    '''
    displays the losing screen, and writes their score
    arg= none
    return= none
    
    '''
    DS_size= self.screen.get_size()
    DS_rect= self.img_death.get_rect()
    DS_screen= pygame.display.set_mode(DS_size)
    DS_screen.blit(self.img_death, DS_rect)
  
    my_font= pygame.font.SysFont("Impact", 100)
    your_score= my_font.render( str(self.score), False, self.black)
    DS_screen.blit(your_score, (360, 200)) #center of screen of DS (from 704 x 392)
    pygame.display.flip()
    
    while self.state == "death":
      for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
          self.state = "exit"
      

  def exitloop(self):
    '''
    exits the screen 
    arg= none
    return= none
    '''
    pygame.quit()
    exit()




  