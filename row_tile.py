import pyglet

class RowTile:
  def __init__(self, pi, pk, color, windowWidth, windowHeight, pBatch):
    self.height = (60 / 500) * windowHeight
    self.width = self.height
    self.i = pi
    self.k = pk
    self.x = 25 + ((self.width + 20)*self.i + windowWidth/3 - ((self.width + 20) * 6)/2)
    self.y = ((self.height + 20)*self.k + windowHeight/2 - ((self.height + 20) * 6)/3)

    if color == "red":
      self.sprite = pyglet.sprite.Sprite(pyglet.image.load("Assets/Images/Red Row Tile.png"), x=self.x, y=self.y, batch=pBatch)
    elif color == "green":
      self.sprite = pyglet.sprite.Sprite(pyglet.image.load("Assets/Images/Green Row Tile.png"), x=self.x, y=self.y, batch=pBatch)
    elif color == "yellow":
      self.sprite = pyglet.sprite.Sprite(pyglet.image.load("Assets/Images/Yellow Row Tile.png"), x=self.x, y=self.y, batch=pBatch)
    elif color == "blue":
      self.sprite = pyglet.sprite.Sprite(pyglet.image.load("Assets/Images/Blue Row Tile.png"), x=self.x, y=self.y, batch=pBatch)
    elif color == "purple":
      self.sprite = pyglet.sprite.Sprite(pyglet.image.load("Assets/Images/Purple Row Tile.png"), x=self.x, y=self.y, batch=pBatch)


  def update(self):
    self.sprite.width = self.width
    self.sprite.height = self.height
    self.sprite.x = self.x
    self.sprite.y = self.y