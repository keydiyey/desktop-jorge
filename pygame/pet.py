import spritesheet
import pygame
import random
import time

class Pet(pygame.sprite.Sprite):
    
    def __init__(self, screen, x,y):
        # will call laturr
        self.screen = screen
        self._is_animating = False
        self.sprites = spritesheet.Animation()
        
        # starting values of variables
        self.state = "idle"
        self.cycle = 0
        self.current_frame = 0
        
    def update(self, frame):
        # updating screen
        self.screen.blit(frame, (0,0))
        
        


    def run(self, ID, max_cycles, current_frame): # calling animation blitz
    
        print("running animation now")
        
        self.current_frame = current_frame
        
        frame = self.sprites.get_frame(ID, current_frame)
        self.sequence = self.sprites.animation_sequence(ID)
        
        self.update(frame)
        
        self.current_frame += 1
        
        print("current frame running:" + str(self.current_frame))
        print("len seq:" + str(len(self.sequence)))
        
        if self.current_frame >= len(self.sequence):
            # adding count to cycle if all frames passed
            self.cycle += 1
            self.current_frame = 0
            
            if self.cycle >= max_cycles:
                self.state = random.choice(["idle", "walk"])
                return self.state, self.current_frame    
        
        return self.state, self.current_frame
        

    def idle(self, current_frame):
        print("in idle func")
        ID = 0
        max_cycles = 5
        self.state, self.current_frame =  self.run(ID, max_cycles, current_frame)
        return self.state, self.current_frame
        
        
    def walk(self, current_frame):
        print("in walk func")
        ID = 1
        max_cycles = 10
        self.state, self.current_frame =  self.run(ID, max_cycles, current_frame)
        return self.state, self.current_frame