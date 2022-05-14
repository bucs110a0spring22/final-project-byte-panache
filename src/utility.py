

class Utility:  
    #SCREEN
    
    SCREENWIDTH = 0
    SCREENHEIGHT = 0
    
    
    #LEVELS
    
    SCOREGAP = 100
    
    #HOLE
    
    HOLEWIDTH = 125
    HOLEHEIGHT = int(HOLEWIDTH * (3/8))
    HOLETOTAL = 9
    #MOLE AND BOMB
    
    MOLEWIDTH = int(HOLEWIDTH * (2/3))
    MOLEHEIGHT = int(MOLEWIDTH)
    
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
    
    

    IMAGEHAMMER = IMAGEBASE + "hammer.png"
    
  
    
    
    
    #DEATH SCREEN 
    
    DSWIDTH= 750
    DSHEIGHT= 500
