import pygame
# import skel

class animation():
    #self.rect: where to place the image
    #self.frames: the images 
    #self.frameTime: the time inbetween frames
    #self.repeat: if the animation repeats
    
    def __init__ (self, frames, frameTime, repeat):
        self.frames = frames
        self.frameTime = frameTime
        self.index = 0
        self.count = 0
        self.repeat = repeat
    
    def update(self, screen, rect):
        screen.blit(self.frames[self.index], rect)

        if self.count == self.frameTime[self.index]:
            if self.repeat == True:
                self.index = (self.index + 1) % len(self.frames) #ensures repeatio
            else:
                self.index = self.index + 1
                if self.index >= len(self.frames):
                    self.index = len(self.frames) - 1
            self.count = 0
        self.count = self.count + 1

