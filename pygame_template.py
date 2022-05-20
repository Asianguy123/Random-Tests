# Basic Pygame Template

# contains filler values

# ---------------------------------------------------------------------------------------------------------------------
# Imports

import sys
import pygame

# ---------------------------------------------------------------------------------------------------------------------
# Main Function

def main():
    click = False
    while True:
        
        mx, my = pygame.mouse.get_pos() 
       
        # event loop
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # window update
        pygame.display.flip()
        clock.tick(60)
        SCREEN.fill(bg_colour)
    

# ---------------------------------------------------------------------------------------------------------------------
# Constants

pygame.init()
CLOCK = pygame.time.Clock()
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000 
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Application Name | Asianguy_123')
bg_colour = pygame.Color('#FFFFFF')

# ---------------------------------------------------------------------------------------------------------------------
# Runs Code

if __name__ == '__main__':
  main()
