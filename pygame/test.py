import PySimpleGUI as sg

import random
import json

class Animations:
    def __init__(self):
        pass
    

    def getData(self):
        # Opening JSON file
        with open('animations.json', 'r') as animations:
            data = json.load(animations)
        return data
    
    def fetchAnimation(self, ID):
        animations = self.getData()["animations"]
        return animations[ID]["sequence"]
            

seq = Animations().fetchAnimation(1)
print (seq)
print("ok")
print(len(seq))


            r = random.randrange(0,1)
            
            _is_animating = True
            sequence = jorge.animation_sequence(1)
            
                
            image = jorge.get_frame(sequence, current_frame)
            current_frame += 1
            
            if current_frame >= len(sequence):
                current_frame = 0
        
        
            screen.blit(image, (0,0))
