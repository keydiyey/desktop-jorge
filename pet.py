import animations
import ast
import random


import tkinter as tk



class Pet:
    def __init__(self, window):
        # pet variables
        self.x = 0
        self.y = 0
        self.cycle = 0
        self.state = "idle"
        self.sprites = animations.Animations()
        self._x_is_reversed = False
        self._y_is_reversed = False
        '''
        
        Properties of window (change when changing gui)
        
        '''        
        self.window = window
        self.screen_W = window.winfo_screenwidth() 
        self.screen_H = window.winfo_screenheight()

        
        # initiating canvas
        self.canvas = tk.Canvas(self.window, width = 64, height = 64, bg = 'white', highlightthickness=0)
        self.img = tk.PhotoImage(file='./animations/1.png')
        self.canvas.create_image((32, 32), image = self.img)
        self.canvas.pack()
        
        # window position
        self.size = "64x64"
        self.window.geometry(f'{self.size}+50+50')
    
    ''' change these two functions according to ur gui '''
    
    def update_position(self, x, y):
        position = self.window.geometry(f'{self.size}+{str(50+x)}+{str(50+y)}')
        return 
    
    def update_image(self, image):
        self.canvas.create_image((32, 32),image = image)
        self.canvas.pack()
        return
    
    ''' collision checking '''

    def check_collision(self, x, y):
        if 64 + x >= self.screen_W or x < 0:
            if self._x_is_reversed == False:
                self._x_is_reversed = True
            else:    
                self._x_is_reversed = False
           
        if 64 + y >= self.screen_H or x < 0:
            if self._y_is_reversed == False:
                self._y_is_reversed = True
            else:    
                self._y_is_reversed = False
        else:
            return

    
    ''' code below is made so it is not indepent of gui (maybe) '''
    
    def next_state(self):
        next_state = random.choice(["idle", "walk", "sniff", "jump"])
 
        return next_state
    
    def run(self, ID, current_frame):
        
        # for checking collisions on the side of the window
        self.check_collision(self.window.winfo_x(),self.window.winfo_y())
        y_vel = self.sprites.getValue(ID, "y_vel")
        x_vel = self.sprites.getValue(ID, "x_vel")
        
        acceleration = 2
        time = 0
        
        if self._x_is_reversed == True:
            self.img = self.sprites.flip(ID, current_frame)
            self.x -= x_vel + (3*time)
            
        else:
            self.img = self.sprites.getImage(ID, current_frame)
            self.x += x_vel + (3*time)
      
        if self._y_is_reversed == True:
            self.y -= random.randint(0,y_vel)          
        else:
            
            self.y += random.randint(0,y_vel)
            

        # updating image and position
        self.update_image(self.img)
        self.update_position(self.x, self.y)
        
        current_frame += 1
        time += 1
        
        # adding count to cycle if all frames passed
        if current_frame >= len(self.sprites.fetchSequence(ID)):
            self.cycle += 1
            current_frame = 0
            
            # if cycle is finished set a new state
            if self.cycle >= self.sprites.getValue(ID, "max_cycles"):
                self.cycle = 0
                time = 0
                self.state = self.next_state()
                return self.state, current_frame
             
        return self.state, current_frame
 
    def get_note(self):
        os.startfile('./src/notes/1.txt')
        win = pyautogui.getWindow(str_title_or_int_id)
        win.move(x, y)
        
        pass