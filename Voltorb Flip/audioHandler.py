import pyglet

class AUDIO:
  backgroundAudioPlayer = pyglet.media.player.Player()
  for i in range(999): backgroundAudioPlayer.queue(pyglet.media.load("Assets/Sounds/Background Music.wav"))

  onePoint = pyglet.media.load("Assets/Sounds/x1 Point.wav", streaming=False)
  twoPoint = pyglet.media.load("Assets/Sounds/x2 Point.wav", streaming=False)
  threePoint = pyglet.media.load("Assets/Sounds/x3 Point.wav", streaming=False)
  hitVoltorb = pyglet.media.load("Assets/Sounds/Hit Voltorb.wav", streaming=False)
  loseSong = pyglet.media.load("Assets/Sounds/Lose Song.wav")
  winSong = pyglet.media.load("Assets/Sounds/Win Song.wav")
  passLevel = pyglet.media.load("Assets/Sounds/Pass Level.wav", streaming=False)