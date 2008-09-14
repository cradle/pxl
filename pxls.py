from states import *
import gui
 
import random, math
 
import pygame
from pygame.constants import *


class MoveKey(object):
  def __init__(self, key, update_method):
    self.key = key
    self.pressed = False
    self.update_method = update_method
    
  def update(self, delay):
    if self.pressed:
      self.update_method(delay)
      
class Position(list):
  def __init__(self, xy):
    list.__init__(self, xy)
  
  def x(self):
    return self[0]
  def set_x(self, x):
    self[0] = x
  x = property(x, set_x)

  def y(self):
    return self[1]
  def set_y(self, y):
    self[1] = y
  y = property(y, set_y)

  def dup(self):
    return Position(self)

class Pxl(gui.Paintable, gui.Keyable, gui.Updateable):
    def __init__(self,
                  loc,
                  colour = [255,255,255],
                  up = K_UP, right = K_RIGHT, down = K_DOWN, left = K_LEFT,
                  ):
        gui.Keyable.__init__(self,[up, right, down, left])
        gui.Paintable.__init__(self,Position(loc))
        
        self.lines = [[self.loc.dup() for x in range(10)] for y in range(10)]
        
        self.colour = colour
        
        self.acc = [0,0]
        
        self.keys = {
          up:     MoveKey(up, self._up),
          right:  MoveKey(right, self._right),
          left:   MoveKey(left, self._left),
          down:   MoveKey(down, self._down)
        }
        
        self.acceleration = 50

    def _up(self, delay):
      self.acc[1] -= delay * self.acceleration
      
    def _down(self, delay):
      self.acc[1] += delay * self.acceleration
      
    def _left(self, delay):
      self.acc[0] -= delay * self.acceleration
      
    def _right(self, delay):
      self.acc[0] += delay * self.acceleration
        
    def update(self,delay):            
      for key in self.keys.values():
        key.update(delay)
      
      self.loc[0] += delay * self.acc[0]
      self.loc[1] += delay * self.acc[1]
      
      if self.loc[0] % 640 != self.loc[0] or self.loc[1] % 640 != self.loc[1] :
        self.loc[0] = self.loc[0] % 640
        self.loc[1] = self.loc[1] % 640
        self.lines.append([self.loc.dup()]*10)
      else:
        self.lines[0].pop(0)
        self.lines[-1].append(self.loc.dup())
        
      if len(self.lines[0]) < 2:
        self.lines.pop(0)
    
    def keyEvent(self, key, unicode, pressed):
      if key not in self.keys:
        return
      
      self.keys[key].pressed = pressed
            
    def paint(self,screen):
      for line in self.lines:
        pygame.draw.lines(screen, self.colour, False, line)