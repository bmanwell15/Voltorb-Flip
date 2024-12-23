import pyglet

class Marker:

    def __init__(self, type, winWidth, pBatch):
        self.hasBeenHovered = False

        self.y = 28
        self.width = 50
        self.height = 50

        if type == "clear":
            self.x = winWidth - 211
            self.sprite = pyglet.sprite.Sprite(pyglet.image.load("Assets/Images/Tile Flipped Down - Marker Hover.png"), x=self.x, y=28, batch=pBatch)
        elif type == "volt":
            self.x = winWidth - 146
            self.sprite = pyglet.sprite.Sprite(pyglet.image.load("Assets/Images/Voltorb Marker.png"), x=self.x, y=28, batch=pBatch)
        elif type == "one":
            self.x = winWidth - 81
            self.sprite = pyglet.sprite.Sprite(pyglet.image.load("Assets/Images/One Marker.png"), x=self.x, y=28, batch=pBatch)
    
    def update(self):
        self.sprite.width = self.width
        self.sprite.height = self.height
        self.sprite.x = self.x
        self.sprite.y = self.y