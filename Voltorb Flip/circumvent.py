import math
import pyglet
import random

class Circumvent:
  version = "Alpha 0.0.1"
  
  
  def touchingRec(x1, y1, w1, h1, x2, y2, w2, h2):
    if x1 <= x2 + w2 and x1 + w1 >= x2 and y1 <= y2 + h2 and y1 + h1 >= y2:
      return True
    return False
  
  def distanceOf(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
  
  def fadeOut(sprite, dur, FPS=(1/60)):
    def INTERNAL_FADEOUT_ANIMATE(dt, sprite, dur):
      sprite.opacity -= ((255 * dt) / dur)
      sprite.opacity = max(0, sprite.opacity)
    pyglet.clock.schedule_interval_for_duration(INTERNAL_FADEOUT_ANIMATE, FPS, dur, sprite, dur)

  def fadeIn(sprite, dur, FPS=(1/60)):
    def INTERNAL_FADEOUT_ANIMATE(dt, sprite, dur):
      sprite.opacity += ((255 * dt) / dur)
      sprite.opacity = min(255, sprite.opacity)
    pyglet.clock.schedule_interval_for_duration(INTERNAL_FADEOUT_ANIMATE, FPS, dur, sprite, dur)
  
  def randomColor():
    return "rgb(" + math.floor(random.randint(0, 255)) + "," + math.floor(random.randint(0, 255)) + "," + math.floor(random.randint(0, 255)) + ")"
  
  def isMouseOver(mx, my, x, y, w, h):
    return mx <= x + w and mx + 1 >= x and my <= y + h and my + 1 >= y
  
  def setCursor(window, cursor):
    window.set_mouse_cursor(window.get_system_mouse_cursor(cursor))

  def print2DArray(arr): 
    for i in range(len(arr)):
      print(arr[i])