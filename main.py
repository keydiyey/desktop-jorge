import random
import animations
import pet
import tkinter as tk
import time

class Game:
    def __init__(self):
        # Create the Window
        self.window = tk.Tk()
        
        # right click menu
        self.right_menu = tk.Menu(self.window, tearoff=0)
        self.right_menu.add_command(label="exit", command = self.quit)
        self.window.bind("<Button-3>", self.popup)
        
        # enabe dragging
        self.window.bind("<ButtonPress-1>", self.start_drag)
        self.window.bind("<ButtonRelease-1>", self.stop_drag)
        self.window.bind("<B1-Motion>", self.drag)
        
        # to make window borderless and transparent
        self.window.wm_attributes("-transparentcolor", "white")
        self.window.overrideredirect(True)
        self.window.attributes('-topmost', True)
            
        # for states
        self.state = "idle"
        self.ID = 0
        self.pet = pet.Pet(self.window)
        self.current_frame = 0

    def start_main_loop(self):
        self.window.after(0, self.check_state)   
        self.window.mainloop()
        

    def check_state(self):
        if self.state == "idle":
            self.ID = 0
          
        elif self.state == "walk":
            self.ID = 1
            
        elif self.state == "sniff":
            self.ID = 2
            
        elif self.state == "jump":
            self.ID = 3
        
        elif self.state == "drag":
            self.ID = 4

        self.state, self.current_frame = self.pet.run(self.ID, self.current_frame)
        self.window.after(250, self.check_state)
        
    def popup(self, event):
        try:
            self.right_menu.tk_popup(event.x_root, event.y_root, 0)
        finally:
            self.right_menu.grab_release()
    
    def start_drag(self, event):
        self.x = event.x
        self.y = event.y

    def stop_drag(self, event):
        self.x = event.x
        self.y = event.y

    def drag(self, event):
        #self.state == "drag"
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.window.winfo_x() + deltax
        y = self.window.winfo_y() + deltay
        self.window.geometry(f"+{x}+{y}")
    
    def quit(self):
        self.window.destroy()
        
# initiating game starting variables

game = Game()


# starting game loop
game.start_main_loop()

