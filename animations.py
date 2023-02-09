import random
import json

# change this when changing gui
import tkinter as tk
import PIL
from PIL import ImageTk

class Animations:
    
    # read JSON file
    def getData(self):
        with open('animations.json', 'r') as animations:
            data = json.load(animations)
        return data
    
    # getting the any value
    def getValue(self, ID, variable:str):
        animations = self.getData()["animations"]
        value = animations[ID][variable]
        return value
    
    # getting the sequence list
    def fetchSequence(self, ID):
        animations = self.getData()["animations"]
        sequence = animations[ID]["sequence"]
        return sequence
    
    def image_path(self, ID, current_frame):
        sequence = self.fetchSequence(ID)
        filename = sequence[current_frame]
        imagepath = f'./animations/{filename}'
        
        return imagepath
    
    # fetches image from list
    def getImage(self, ID, current_frame):

        '''
        change only the code below when migrating to new gui 
        '''
        
        img = tk.PhotoImage(file = self.image_path(ID, current_frame))   
        return img

    def flip(self, ID, current_frame):
        #read the image
        image = PIL.Image.open(self.image_path(ID, current_frame))

        #flip image
        flipped_image = image.transpose(PIL.Image.FLIP_LEFT_RIGHT)
        image = ImageTk.PhotoImage(flipped_image)
        return image
 
    
        

    
        
    