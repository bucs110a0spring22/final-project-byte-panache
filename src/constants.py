

#SCREEN

SCREENWIDTH = 500
SCREENHEIGHT = 750 
SCREENFPS = 60

#LEVELS

SCOREGAP = 100
MOLESPEED = 5

#HOLE

HOLEWIDTH = 100
HOLEHEIGHT = int(HOLEWIDTH * (3 /8))
HOLETOTAL = 9
#MOLE AND BOMB

MOLEWIDTH = int(HOLEWIDTH * (2/3))
MOLEHEIGHT = int(MOLEWIDTH)

MOLECOOLDOWN = 500 #millisec
MOLEWAIT = 1000

MOLEHIT= 500 #millisec
MOLEMISS= 250 #millisec


BOMB = 0
BOMB_HIT = 1 
MOLE = 2
MOLE_HIT = 3


#IMAGE

IMAGEBASE = "assets/"
IMAGEBASE2 = IMAGEBASE + "moleAnims/"

IMAGEHOLE = IMAGEBASE + "hole.png"
IMAGEBASEMAGEMALLET = IMAGEBASE + "hammer.png"

IMAGEDEATHSCREEN = IMAGEBASE + "DeathScreen.png"

IMAGEMOLE = IMAGEBASE2 + "mole.png"
IMAGEMOLEHIT = IMAGEBASE2 + "molehurt.png"

IMAGEBOMB = IMAGEBASE2 + "Bomb.png"
IMAGEBOMBHIT = IMAGEBASE2 + "Explode.png"

IMAGELIVES = IMAGEBASE + "lives.png"


#FONT
TITLE = "Whack-A-Mole"


#HAMMER

HAMMERWIDTH = int(HOLEWIDTH)
HAMMERHEIGHT = int(HAMMERWIDTH)

#DEATH SCREEN 

DSWIDTH= 750
DSHEIGHT= 500
