import tkinter as tk
from PIL import Image, ImageTk
import time

import tkinter as tk
from PIL import Image, ImageTk
import time

class AnimatedGIF(tk.Label):
    def __init__(self, master, path, bg_color=None, forever=True):
        self._master = master
        self._loc = 0
        self._forever = forever
        self._is_running = False

        self._image = Image.open(path)
        self._frames = []
        self._delay = int(1000 / self._image.info['duration'])  # GIF frame duration

        try:
            while True:
                self._frames.append(ImageTk.PhotoImage(self._image.copy()))
                self._image.seek(len(self._frames))  # Move to next frame
        except EOFError:
            pass  # We're done reading the frames of the GIF

        if len(self._frames) == 1:
            super().__init__(master, image=self._frames[0], bg=bg_color)
        else:
            super().__init__(master, image=self._frames[0], bg=bg_color)

            self._temp = self._frames[0]  # Save reference to prevent garbage collection
            self.animate()  # Start animation

    def animate(self):
        if self._frames:
            self._loc = (self._loc + 1) % len(self._frames)
            self.config(image=self._frames[self._loc])
            self._master.after(self._delay, self.animate)  # Loop after a delay
            
            
            
#class AnimatedGIF(tk.Label):
    #def __init__(self, master, path, forever=True):
        #self._master = master
        #self._loc = 0
        #self._forever = forever
        #self._is_running = False

        #self._image = Image.open(path)
        #self._frames = []
        #self._delay = int(1000 / self._image.info['duration'])  # GIF frame duration

        #try:
            #while True:
                #self._frames.append(ImageTk.PhotoImage(self._image.copy()))
                #self._image.seek(len(self._frames))  # Move to next frame
        #except EOFError:
            #pass  # We're done reading the frames of the GIF

        #if len(self._frames) == 1:
            #super().__init__(master, image=self._frames[0])
        #else:
            #super().__init__(master, image=self._frames[0])

            #self._temp = self._frames[0]  # Save reference to prevent garbage collection
            #self.animate()  # Start animation

    #def animate(self):
        #if self._frames:
            #self._loc = (self._loc + 1) % len(self._frames)
            #self.config(image=self._frames[self._loc])
            #self._master.after(self._delay, self.animate)  # Loop after a delay
