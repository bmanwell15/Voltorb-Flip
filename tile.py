import pyglet

class Tile:

  def __init__(self, pi, pk, windowWidth, windowHeight, pBatch):
    self.hasBeenHovered = False
    self.hasBeenClicked = False
    self.mark = "clear"
    self.i = pi
    self.k = pk
    self.height = (60 / 500) * windowHeight
    self.width = self.height
    self.x = 25 + ((self.width + 20)*self.i + windowWidth/3 - ((self.width + 20) * 6)/2)
    self.y = ((self.height + 20)*self.k + windowHeight/2 - ((self.height + 20) * 6)/3)
    self.sprite = pyglet.sprite.Sprite(pyglet.image.load("Assets/Images/Tile Flipped Down.png"), x=self.x, y=self.y, batch=pBatch)

  def update(self):
    self.sprite.width = self.width
    self.sprite.height = self.height
    self.sprite.x = self.x
    self.sprite.y = self.y
  
  def getHoverImage(self, mStatus):

      if mStatus == "clear":
        if self.mark == "clear":
          return pyglet.image.load("Assets/Images/Tile Flipped Down - Hover.png")
        elif self.mark == "volt":
          return pyglet.image.load("Assets/Images/Voltorb Marker - Hover.png")
        elif self.mark == "one":
          return pyglet.image.load("Assets/Images/One Marker - Hover.png")
        
      if mStatus == "volt": return pyglet.image.load("Assets/Images/Voltorb Marker - Marker Hover.png")
      if mStatus == "one": return pyglet.image.load("Assets/Images/One Marker - Marker Hover.png")
  
  def getOffHoverImage(self):
    if self.mark == "clear": return pyglet.image.load("Assets/Images/Tile Flipped Down.png")
    if self.mark == "volt": return pyglet.image.load("Assets/Images/Voltorb Marker.png")
    if self.mark == "one": return pyglet.image.load("Assets/Images/One Marker.png")


  def toString(self):
    return "Tile " + str(5*self.k + self.i)
