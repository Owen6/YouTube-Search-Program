import pygame, os
from states.state import State

class youtube_window(State):
    def __init__(self, UI):
        State.__init__(self, UI)
        self.bg_color = (0,0,0)

    def update(self,dt,actions):
        pass

    def render(self,display):
        #self.screen.blit(pygame.transform.scale(self.canvas, (self.width,self.height)), (0,0))
        display.blit(pygame.transform.scale(self.window.canvas,(self.window.width, self.window.height)), (0,0))
        self.window.draw_text(display, "YouTube Screen", (0,0,0), self.window.width/2, self.window.width/2,20)
        
        pygame.transform.scale(self.window.canvas, (0,0))