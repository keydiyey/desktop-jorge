import pygame
import pyautogui
import time
import spritesheet
import random
import pet


#initializing pygame
pygame.init()

#setting up variables
FPS = 6
BG = (50,50,50)
clock = pygame.time.Clock()

# bg
background = pygame.Surface([64,64], pygame.SRCALPHA, 32)


#creating pygame window
screen = pygame.display.set_mode([120, 120])


running = True



   
class Game():
    
    def __init__(self):
        self.state = "idle" # setting starting state which is idle
        self.current_frame = 0
        
    def state_manager(self):
        if self.state == "idle":
            print("wo")
            print("current frame state manager:" + str(self.current_frame))
            self.state, self.current_frame = jorge.idle(self.current_frame)
            print("current frame after run:" + str(self.current_frame))
            
        if self.state == "walk":
            print("wo")
            print("current frame state manager:" + str(self.current_frame))
            self.state, self.current_frame = jorge.walk(self.current_frame)
            print("current frame after run:" + str(self.current_frame))

# creating pet        
jorge = pet.Pet(screen, 100, 100)        
  
# init game class outside loop to avoid resetting current_frames
game = Game()  


while running:
    print("back to game loop")
    screen.blit(background, (0,0))
    game.state_manager()
    pygame.display.update()
    clock.tick(4)
    
    
pygame.quit()