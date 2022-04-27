import pygame
import random
import math
from dataclasses import dataclass


pygame.init()
bg_image = pygame.image.load("Screen.png")
bg_image = pygame.transform.scale(bg_image, (bg_image.get)width() * 3, bg_image.get_height() * 3))
screen = pygame.display.set_mode((bg_image.get_width(), bg_image.get_height()))



score_value = 0
font = pygame.font.sysFont{'timesnewroman', 32)

#scoreboard and font 

textX = 10
textY = 10


mole= []

NUM_COL = 3 
NUM_ROW = 3

possible_mole_pos = [(#find the coordinates later on the screen)]

mole_image = pygame.image.load("mole1.png")
mole_image = pygame.transform.scale(mole_image, (mole_image.getwidth()// 2, mole_image.get_height()//2))

MOLE_RADIUS = min(mole_image.get_width(), mole_image.get_height())// 2.5

GENERATE_MOLE, APPEAR_INTERVAL= pygame.USEREVENT+1, 2*1000
pygame.time.set_timer(GENERATE_MOLE, APPEAR_INTERVAL)

MOLE_LIFE_SPAN = 5* 1000
AGE_MOLE, AGE_INTERVAL= pygame.USERVENT+ 2, MOLE_LIFE_SPAN
pygame.time.set_timer((AGE_MOLE, AGE_INTERVAL))

@dataclass
class Mole:
  x: int
  y: int
  life: int = MOLE_LIFE_SPAN


def check_exist(new_pos):
  for mole in moles:
    if new_pos == (mole.x, mole.y):
      return True
  return False
'''makes sure the mole doesn't randomize to the same hole, arg= new_pos, returns if the mole is in the same spot as another mole '''

  
def generate_next_mole_pos():
  new_pos = ()
  while True:
    grid_index = random.randint(0, NUM_ROW * NUM_COL - 1)
    new_pos = possible_moles_pos[grid_index]
    if not check_exist(new_pos):
      break
  return new_pos
''' creates the next new moles , randomizes the new possition based on the row and column , arg= (), returns random mole position'''


def draw_moles():
  for mole in moles:
    screen.blit(mole_image, (mole.x, mole.y))

''' makes the mole on the screen, arg=(), returns nothing'''

def show_score (x, y):
  global score_value
  score = font.render('Score: ' + str(score_value)), True, () #put coordinates of score board in the parathesis b4 this 
  screen.blit(score, (x,y))

''' writes the scores down, arg= x, y, returns none'''    

def check_mole_collision(clickX, clickY, moleX, moleY)
  moleX, moleY= moleX+MOLE_RADIUS, moleY+MOLE_RADIUS
  distance=math/sprt(math.pow(moleX - clickX, 2)+ (math.pow(moleY-clickY, 2)))
  return distance < MOLE_RADIUS
''' detects if the click was in the radius of the mole, arg= clickX,clickY,moleX,moleY, return= distance is less than the mole radius'''

                     
def check_moles_collision(click_pos,moles):
  for mole in moles:
    if check_mole_collision(click_pos[0],click_pos[1],mole.x, mole.y):
      global score_value
      score_value +=1
      moles.remove(mole)
#when enemy is clicked, mole is removed 
''' when enemy is clicked the mole is removed, arg= click_pos, moles, returns nothing
'''
def age_moles():
  for mole in moles:
    mole.life -+ 1000
''' mole disappears after a while, arg= (), returns nothing'''
def remove_died_moles():
  for mole in moles:
    if mole.life == 0:
      moles.remove(mole)
''' removes the moles that died, arg= (), returns nothing'''
                     
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running= False
    if event.type == pygame.MOUSEBUTTONUP:
      click_pos = pygame.mouse.get.pos()
      check_moles_collision(click_pos, moles)

    if event.type == AGE_MOLE:
      age_mole()
      remove_mole()
     
    if event.type == GENERATE_MOLE:
      if len(moles)< NUM_COL * NUM_ROW:
        new_pos = generate_next_mole_pos()
        moles.append(mole(new_pos.0, new pos[1]))


                     
screen.blit(bg_image, (0,0))
draw_moles()
show_score(textX, textY)
show_score(textX, textY)
pygame.display.update()

