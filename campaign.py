from states import *
import gui
import random
import pygame
import pxl
from pygame.constants import *
import done
from pxls import *
	
class GameState(GuiState):
 
    def __init__(self,driver,screen,level=0):
        GuiState.__init__(self,driver,screen)
        pygame.event.set_grab(True)
        pygame.mouse.set_visible(False)
        random.seed(pygame.time.get_ticks())
        self.player1 = Pxl([50,50], [0,0,255])
        self.add(self.player1)
        self.player2 = Pxl([580,580], [255,0,0], K_w, K_d, K_s, K_a)
        self.add(self.player2)
        
    def update(self,delay):
        GuiState.update(self,delay)

    def paint(self, screen):        
        GuiState.paint(self,screen)
    
    def keyEvent(self, key, unicode, value):
        GuiState.keyEvent(self, key, unicode, value)
        if key == K_q:
            title = pxl.TitleScreen(self._driver, self.screen)
            self._driver.replace(title)
