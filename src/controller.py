import sys
import pygame
import random
import src.models as model 
import src.constants as Consts



class Controller:

  def setUpHoles(self):
    '''
    sets up the holes through determining the distance between the screen. makes an index of all the hole possible positions
    arg= none
    return= holeList= index of hole possible positions
    
    
    '''
    # Placing and making holes
    holeList = []
    startX = (Consts.SCREENWIDTH/5) * 2
    startY = (Consts.SCREENHEIGHT/5) * 4
    xCord = 0
    yCord = 0

    for hole in range(9):
      if hole % 3 == 0:
        xCord = startX
        yCord += -(startY)
      else:
        xCord += startX
      holeList.append(model.Hole((xCord,yCord)))
    return holeList
  
  def __init__(self):
    '''
    initializes the screen, variables, scorekeep, etc
    arg= none
    return= none
    
    '''

    #Setting up screen
    pygame.font.init()
    self.state = "gameplay"
    self.screen = pygame.display.set_mode((Consts.SCREENWIDTH,Consts.SCREENHEIGHT))
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
    self.mole = model.Mole(holeArray[index].getPosition(), Consts.MOLE,Consts.IMAGEMOLE,holeArray)

    self.clock = pygame.time.Clock()
    self.time = 0

    self.all_sprites = pygame.sprite.Group((self.mole,) + tuple(self.holeList))
    
    # Death Screen setup
    self.img_death = pygame.image.load((Consts.IMAGEDEATHSCREEN))
    self.img_death = pygame.transform.scale(self.img_death, (Consts.DSWIDTH, Consts.DSHEIGHT))

    # Game logic setup
    self.alive = True
    self.lives = 3
    self.score = 0

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
    if self.lives == 0:
            self.state == "death"
    while self.state == "gameplay":
      # Make clock tick so that mole only moves after a certain amount of time
      dt = self.clock.tick()
      self.time += dt
      
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
            self.time = 0
            self.mole.updateHit()

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
        self.mole.frame = Consts.IMAGEMOLEHIT
        self.score += Consts.SCOREGAP
      if self.mole.state == Consts.BOMB:
        self.lives += -1
        self.mole.frame = Consts.IMAGEBOMBHIT
      return True
    return False
  
  def deathScreen(self):
    '''
    displays the losing screen, and writes their score
    arg= none
    return= none
    
    '''
    while self.state == "death":
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.state = "exit"
      self.display.fill(164, 209, 159)
      self.display.blit(self.img_death, (0,0))
 
      my_font= pygame.font.SysFont("Impact", 30)
      your_score= my_font.render("Your Score: " + str(self.score), False)
      self.display.blit(your_score, (100, 50))
      

  def exitloop(self):
    '''
    exits the screen 
    arg= none
    return= none
    '''
    pygame.quit()
    exit()


  def spawnMole(self):
    '''
    spawns the mole according to a random number from 1-9, the number will correlate to the order of coordinates in the index
    arg= none
    return= none
    
    '''
    index = random.randint(0,8)
    self.mole = model.Mole(self.holeList[index].getPosition(), Consts.MOLE,Consts.IMAGEMOLE)    

    self.screen.blit(self.mole, (self.mole.rect.x,self.mole.rect.y))