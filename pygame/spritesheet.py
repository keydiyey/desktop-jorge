import pygame
import random

import json


class Animation:

    def __init__(self):
        pass 

    def getData(self):

        # Opening JSON file
        with open('animations.json', 'r') as animations:

            data = json.load(animations)
        return data
    

    def animation_sequence(self, ID):
        animations = self.getData()["animations"]
        # ID specifies the type of animation to be used
        sequence = animations[ID]["sequence"]
        return sequence

    def get_frame(self, ID, current_frame):
        print(current_frame)
        
        # get animation sequence
        # placeholder id 1 for testing
        current_image = (self.animation_sequence(ID))[current_frame]
        
        # loading the image of a specific frame
        path_to_current_frame = pygame.image.load(f"./animations/{current_image}").convert_alpha()
        
        return path_to_current_frame
    
    
        
    
        
        
             
        
            
            
       
                
            
            



        
  
        
  