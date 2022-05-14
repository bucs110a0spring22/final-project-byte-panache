import pygame
from src import controller


def main():
  pygame.init()
  main_window = controller.Controller(600,600)
  main_window.menuloop()
  
main()    
  