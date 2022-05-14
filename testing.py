import src.models as models

# to run test file:
# show hidden files on Replit
# go to .replit file and switch to 'run testing.py' line
def main():
   #5 is the state
  object = models.Mole((10,20), 5 , "assets/moleAnims/mole.png", [1,2,3])
  # testing __init__
  assert (object.rect.x == 10), "Error in Mole's init"
  assert (object.rect.y == 20), "Error in Mole's init"
  assert (object.state == 5), "Error in Mole's init"# self.state
  assert (object.image== "assets/moleAnims/mole.png"), "Error in Mole's init"# self.image
  assert (object.holeList == [1,2,3]), "Error in Mole's init"

  # testing updateMiss ??
object = models.Mole((10,20), 5 , "assets/moleAnims/mole.png", [1,2,3])
object.updateMiss()
 assert (object.rect.x == 10), "Error in UpdateMiss init"
  assert (object.rect.y == 20), "Error in UpdateMiss init"

  # put assert statements here
  
  # testing updateHit
  # state of 1
  object = models.Mole((1,1), 1, "assets/moleAnims/mole.png", [1,2,3])
  object.updateHit()
  assert (object.state == 1), "Error in UpdateHit's init"
  # put assert statements here
  
  # state of 3
  object = models.Mole((1,1), 3, "assets/moleAnims/mole.png", [1,2,3])
  object.updateHit()
  assert (object.state == 3), "Error in UpdateHit's init"
  # assert

  object = models.Hole((0,1),"assets/moleAnims/hole.png")
  assert (object.rect.x == 0), "Error in Hole's init"
  assert (object.rect.y == 1), "Error in Hole's 
init"
  assert (object.image== "assets/moleAnims/hole.png"), "Error in Hole's init"


  # test Hole methods
  
  # create the object of the class youre testing(init)
  # test that whatever variables were set are set correclty
  # call other method
  # check that whatever it changed was changed correctly
  # continue for all methods of the class
  print("All tests passed without errors")

main()