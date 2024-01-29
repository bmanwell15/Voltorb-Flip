VERSION = "Alpha 1.29.24"

import pyglet
import math
import random
import base64

from circumvent import Circumvent as C
from audioHandler import AUDIO as AUD
from tile import Tile
from row_tile import RowTile

# python -m PyInstaller -i "C:\Users\benja\Downloads\Voltorb Icon.ico" core.py --onefile

window = pyglet.window.Window(resizable=False, caption="Voltorb Flip - Level 1", width=750, height=520)
window.set_icon(pyglet.image.load("Assets/Images/Icon.png"))
backgroundImage = pyglet.image.SolidColorImagePattern(color=(27, 173, 92, 0)).create_image(window.width, window.height)
drawSprites = pyglet.graphics.Batch()


# Retrieved Save Data
READSAVEFILE = open("Save Data/save.txt", "rt")
fileContent = READSAVEFILE.read()

fileBytes = base64.b64decode(fileContent.encode("ascii"))
saveData = eval(fileBytes.decode("ascii"))
READSAVEFILE.close()


# startString = """{"collectedPoints": 0,"highScore": 0}"""

# startStringBytes = base64.b64encode(startString.encode("ascii"))
# startStringFinal = startStringBytes.decode("ascii")

# print(startStringFinal)

VERSIONINFO = pyglet.text.Label("V. " + VERSION, x=window.width - 100, y = 15, width = 100, font_size = 10, color = (0,0,0,255), align="right", batch=drawSprites)
UPDATEINFO = pyglet.text.Label("Check for updates at 'https://github.com/bmanwell15/Voltorb-Flip.git'", x=window.width - 300, y = 3, width = 300, font_size = 8, color = (0,0,0,255), align="right", batch=drawSprites)


AUD.backgroundAudioPlayer.play()

pyglet.font.add_file("Assets/Fonts/Aldrich.ttf")

# Gameboard Objects & board setup ############################
tiles = []
colorTiles = []
tileLabels = [] # Vertical Red Points, Vertical Red Volts, ... etc.
pointHolder = {
    "levelPointsBox": pyglet.sprite.Sprite(pyglet.image.load("Assets/Images/White Box.png"), x=window.width - 220, y=window.height - 80, batch=drawSprites),
    "levelPointsLabel": pyglet.text.Label("Level Points", font_name='Aldrich', font_size=19, bold=True, x=window.width - 220, y=window.height - 65, width=200, height=50, align="center", color=(0, 0, 0, 255), batch=drawSprites),
    "levelPointsValueBox": pyglet.sprite.Sprite(pyglet.image.load("Assets/Images/White Box.png"), x=window.width - 220, y=window.height - 135, batch=drawSprites),
    "levelPointsValueLabel": pyglet.text.Label("00000000", font_name='Aldrich', font_size=24, bold=True, x=window.width - 220, y=window.height - 120, width=200, height=70, align="center", color=(0, 0, 0, 255), batch=drawSprites),

    "gamePointsBox": pyglet.sprite.Sprite(pyglet.image.load("Assets/Images/White Box.png"), x=window.width - 220, y=window.height - 225, batch=drawSprites),
    "gamePointsLabel": pyglet.text.Label("Game Points", font_name='Aldrich', font_size=19, bold=True, x=window.width - 220, y=window.height - 210, width=200, height=50, align="center", color=(0, 0, 0, 255), batch=drawSprites),
    "gamePointsValueBox": pyglet.sprite.Sprite(pyglet.image.load("Assets/Images/White Box.png"), x=window.width - 220, y=window.height - 280, batch=drawSprites),
    "gamePointsValueLabel": pyglet.text.Label("00000000", font_name='Aldrich', font_size=24, bold=True, x=window.width - 220, y=window.height - 265, width=200, height=70, align="center", color=(0, 0, 0, 255), batch=drawSprites),


    "collectedPointsBox": pyglet.sprite.Sprite(pyglet.image.load("Assets/Images/White Box.png"), x=window.width - 220, y=window.height - 370, batch=drawSprites),
    "collectedPointsLabel": pyglet.text.Label("Total Points", font_name='Aldrich', font_size=19, bold=True, x=window.width - 220, y=window.height - 355, width=200, height=50, align="center", color=(0, 0, 0, 255), batch=drawSprites),
    "collectedPointsValueBox": pyglet.sprite.Sprite(pyglet.image.load("Assets/Images/White Box.png"), x=window.width - 220, y=window.height - 425, batch=drawSprites),
    "collectedPointsValueLabel": pyglet.text.Label(str(saveData["collectedPoints"]).zfill(8), font_name='Aldrich', font_size=24, bold=True, x=window.width - 220, y=window.height - 410, width=200, height=50, align="center", color=(0, 0, 0, 255), batch=drawSprites),
}

pointHolder["collectedPointsValueLabel"].text = str(saveData["collectedPoints"]).zfill(8)

# Points and Voltorb Tracker
horizontalPoints = [0, 0, 0, 0, 0]
horizontalVolts = [0, 0, 0, 0, 0]
verticalPoints = [0, 0, 0, 0, 0]
verticalVolts = [0, 0, 0, 0, 0]

for i in range(5):
    for k in range(5):
        tiles.append(Tile(i, k, window.width, window.height, drawSprites))

colorTiles.append(RowTile(5, 4, "red", window.width, window.height, drawSprites))
colorTiles.append(RowTile(5, 3, "green", window.width, window.height, drawSprites))
colorTiles.append(RowTile(5, 2, "yellow", window.width, window.height, drawSprites))
colorTiles.append(RowTile(5, 1, "blue", window.width, window.height, drawSprites))
colorTiles.append(RowTile(5, 0, "purple", window.width, window.height, drawSprites))
colorTiles.append(RowTile(0, -1, "red", window.width, window.height, drawSprites))
colorTiles.append(RowTile(1, -1, "green", window.width, window.height, drawSprites))
colorTiles.append(RowTile(2, -1, "yellow", window.width, window.height, drawSprites))
colorTiles.append(RowTile(3, -1, "blue", window.width, window.height, drawSprites))
colorTiles.append(RowTile(4, -1, "purple", window.width, window.height, drawSprites))



# Board Setup
gameboard = [[], [], [], [], []]
points = 1
gamePoints = 1
totalRoundPoints = 1
level = 1
isGameOver = False
for i in range(25): gameboard[math.floor(i/5)].append("NA")

for i in range(5):
    for k in range(5):
        if random.randint(1, 20 - level + 1) <= 5: gameboard[i][k] = "V" # 1 in 4 chance of Voltorb
        if random.randint(1, 50 - level + 1) <= 3: gameboard[i][k] = 3   # 1 in 15 chance of '3'
        if random.randint(1, 30 - level + 1) <= 3: gameboard[i][k] = 2   # 1 in 10 chance of '2'
        if gameboard[i][k] == "NA": gameboard[i][k] = 1     # else, place a '1'

for k in range(5):
    for i in range(5):
        if gameboard[i][k] == "V":
            verticalVolts[k] += 1
            horizontalVolts[i] += 1
        else:
            verticalPoints[k] += gameboard[i][k]
            horizontalPoints[i] += gameboard[i][k]

labelWidth = (60 / 500) * window.height

labels = {
    "horizontalRedPointLabel": pyglet.text.Label(str(horizontalPoints[0]), font_name='Aldrich', font_size=16, x=tiles[24].x + 1.35*tiles[0].width, y=tiles[24].y + tiles[0].height/1.23, color=(0,0,0,240), bold=True, batch=drawSprites, z=2, align="right", width=labelWidth),
    "horizontalGreenPointLabel": pyglet.text.Label(str(horizontalPoints[1]), font_name='Aldrich', font_size=16, x=tiles[24].x + 1.35*tiles[0].width, y=tiles[3].y + tiles[0].height/1.23, color=(0,0,0,240), bold=True, batch=drawSprites, z=2, align="right", width=labelWidth),
    "horizontalYellowPointLabel": pyglet.text.Label(str(horizontalPoints[2]), font_name='Aldrich', font_size=16, x=tiles[24].x + 1.35*tiles[0].width, y=tiles[2].y + tiles[0].height/1.23, color=(0,0,0,240), bold=True, batch=drawSprites, z=2, align="right", width=labelWidth),
    "horizontalBluePointLabel": pyglet.text.Label(str(horizontalPoints[3]), font_name='Aldrich', font_size=16, x=tiles[24].x + 1.35*tiles[0].width, y=tiles[1].y + tiles[0].height/1.23, color=(0,0,0,240), bold=True, batch=drawSprites, z=2, align="right", width=labelWidth),
    "horizontalPurplePointLabel": pyglet.text.Label(str(horizontalPoints[4]), font_name='Aldrich', font_size=16, x=tiles[24].x + 1.35*tiles[0].width, y=tiles[0].y + tiles[0].height/1.23, color=(0,0,0,240), bold=True, batch=drawSprites, z=2, align="right", width=labelWidth),
    ###### Vertical Below
    "verticalRedPointLabel": pyglet.text.Label(str(verticalPoints[0]), font_name='Aldrich', font_size=16, x=tiles[0].x, y=tiles[0].y - tiles[0].height/1.9, color=(0,0,0,240), bold=True, batch=drawSprites, z=2, align="right", width=labelWidth),
    "verticalGreenPointLabel": pyglet.text.Label(str(verticalPoints[1]), font_name='Aldrich', font_size=16, x=tiles[5].x, y=tiles[0].y - tiles[0].height/1.9, color=(0,0,0,240), bold=True, batch=drawSprites, z=2, align="right", width=labelWidth),
    "verticalYellowPointLabel": pyglet.text.Label(str(verticalPoints[2]), font_name='Aldrich', font_size=16, x=tiles[10].x, y=tiles[0].y - tiles[0].height/1.9, color=(0,0,0,240), bold=True, batch=drawSprites, z=2, align="right", width=labelWidth),
    "verticalBluePointLabel": pyglet.text.Label(str(verticalPoints[3]), font_name='Aldrich', font_size=16, x=tiles[15].x, y=tiles[0].y - tiles[0].height/1.9, color=(0,0,0,240), bold=True, batch=drawSprites, z=2, align="right", width=labelWidth),
    "verticalPurplePointLabel": pyglet.text.Label(str(verticalPoints[4]), font_name='Aldrich', font_size=16, x=tiles[20].x, y=tiles[0].y - tiles[0].height/1.9, color=(0,0,0,240), bold=True, batch=drawSprites, z=2, align="right", width=labelWidth),
    ##### Horizontal Volts
    "horizontalRedVoltLabel": pyglet.text.Label(str(horizontalVolts[0]), font_name='Aldrich', font_size=18, x=tiles[24].x + 2.05*tiles[0].width, y=tiles[24].y + 0.2*tiles[0].height, color=(0,0,0,240), bold=True, batch=drawSprites, z=2, align="right"),
    "horizontalGreenVoltLabel": pyglet.text.Label(str(horizontalVolts[1]), font_name='Aldrich', font_size=18, x=tiles[24].x + 2.05*tiles[0].width, y=tiles[18].y + 0.2*tiles[0].height, color=(0,0,0,240), bold=True, batch=drawSprites, z=2, align="right"),
    "horizontalYellowVoltLabel": pyglet.text.Label(str(horizontalVolts[2]), font_name='Aldrich', font_size=18, x=tiles[24].x + 2.05*tiles[0].width, y=tiles[12].y + 0.2*tiles[0].height, color=(0,0,0,240), bold=True, batch=drawSprites, z=2, align="right"),
    "horizontalBlueVoltLabel": pyglet.text.Label(str(horizontalVolts[3]), font_name='Aldrich', font_size=18, x=tiles[24].x + 2.05*tiles[0].width, y=tiles[6].y + 0.2*tiles[0].height, color=(0,0,0,240), bold=True, batch=drawSprites, z=2, align="right"),
    "horizontalPurpleVoltLabel": pyglet.text.Label(str(horizontalVolts[4]), font_name='Aldrich', font_size=18, x=tiles[24].x + 2.05*tiles[0].width, y=tiles[0].y + 0.2*tiles[0].height, color=(0,0,0,240), bold=True, batch=drawSprites, z=2, align="right"),
    ##### Vertical Volts
    "verticalRedVoltLabel": pyglet.text.Label(str(verticalVolts[0]), font_name='Aldrich', font_size=18, x=tiles[0].x + 0.74*tiles[0].width, y=tiles[0].y - 1.1*tiles[0].height, color=(0,0,0,240), bold=True, batch=drawSprites, z=2, align="right"),
    "verticalGreenVoltLabel": pyglet.text.Label(str(verticalVolts[1]), font_name='Aldrich', font_size=18, x=tiles[5].x + 0.74*tiles[0].width, y=tiles[5].y - 1.1*tiles[0].height, color=(0,0,0,240), bold=True, batch=drawSprites, z=2, align="right"),
    "verticalYellowVoltLabel": pyglet.text.Label(str(verticalVolts[2]), font_name='Aldrich', font_size=18, x=tiles[10].x + 0.74*tiles[0].width, y=tiles[10].y - 1.1*tiles[0].height, color=(0,0,0,240), bold=True, batch=drawSprites, z=2, align="right"),
    "verticalBlueVoltLabel": pyglet.text.Label(str(verticalVolts[3]), font_name='Aldrich', font_size=18, x=tiles[15].x + 0.74*tiles[0].width, y=tiles[15].y - 1.1*tiles[0].height, color=(0,0,0,240), bold=True, batch=drawSprites, z=2, align="right"),
    "verticalPurpleVoltLabel": pyglet.text.Label(str(verticalVolts[4]), font_name='Aldrich', font_size=18, x=tiles[20].x + 0.74*tiles[0].width, y=tiles[20].y - 1.1*tiles[0].height, color=(0,0,0,240), bold=True, batch=drawSprites, z=2, align="right"),
}

###################### END BOARD SETUP ##########################

@window.event
def on_draw():
    window.clear()
    backgroundImage.blit(0, 0, 0, window.width, window.height)
    drawSprites.draw()


@window.event
def on_key_press(symbol, modifiers):
    key = pyglet.window.key
    AUD.threePoint.play()


@window.event
def on_mouse_press(x, y, button, modifiers):
    for tile in tiles:
        if C.isMouseOver(x, y, tile.x, tile.y, tile.width, tile.height) and not isGameOver and not tile.hasBeenClicked: tileClicked(tile)
            

@window.event
def on_mouse_motion(x, y, dx, dy):
    for i in range(25):
        if not tiles[i].hasBeenClicked and not isGameOver:
            if C.isMouseOver(x, y, tiles[i].x, tiles[i].y, tiles[i].width, tiles[i].height):
                if not tiles[i].hasBeenHovered:
                    tiles[i].sprite.image = pyglet.image.load("Assets/Images/Tile Flipped Down - Hover.png")
                    C.setCursor(window, window.CURSOR_HAND)
                tiles[i].hasBeenHovered = True
            else:
                if tiles[i].hasBeenHovered:
                    tiles[i].sprite.image = pyglet.image.load("Assets/Images/Tile Flipped Down.png")
                    C.setCursor(window, window.CURSOR_DEFAULT)
                tiles[i].hasBeenHovered = False


def tileClicked(tile, inGame=True):
    global points
    global gamePoints
    global isGameOver
    global level
    tileValue = gameboard[4 - tile.k][tile.i]
    if tileValue == 1 and (not isGameOver or not inGame):
        tile.sprite.image = pyglet.image.load("Assets/Images/1 Tile.png")
        if inGame:
            updatePoints(1)
            AUD.onePoint.play()
    elif tileValue == 2 and (not isGameOver or not inGame):
        tile.sprite.image = pyglet.image.load("Assets/Images/2 Tile.png")
        if inGame:
            updatePoints(2)
            AUD.twoPoint.play()
    elif tileValue == 3 and (not isGameOver or not inGame):
        tile.sprite.image = pyglet.image.load("Assets/Images/3 Tile.png")
        if inGame:
            updatePoints(3)
            AUD.threePoint.play()
    elif tileValue == 'V':
        tile.sprite.image = pyglet.image.load("Assets/Images/Voltorb Tile.png")
        if inGame:
            AUD.hitVoltorb.play()
            isGameOver = True
            AUD.backgroundAudioPlayer.pause()
            AUD.loseSong.play()
            def TEMP(dt):
                for i in range(25): tileClicked(tiles[i], inGame=False)
            def RESET(dt):
                AUD.backgroundAudioPlayer.seek(0)
                AUD.backgroundAudioPlayer.play()
                resetBoard(newLevel=1, win=False)
            
            pyglet.clock.schedule_once(TEMP, 2)
            pyglet.clock.schedule_once(RESET,4.5)
    tile.hasBeenClicked = True


    if not isGameOver:
        tile.hasBeenClicked = True
        isGameOver = checkIfGameOver()

        if isGameOver and inGame:
            AUD.backgroundAudioPlayer.pause()
            AUD.passLevel.play()
            def TEMP(dt):
                for i in range(25): tileClicked(tiles[i], inGame=False)
            def RESUME_MUSIC(dt):
                AUD.backgroundAudioPlayer.seek(0)
                AUD.backgroundAudioPlayer.play()
                resetBoard(newLevel=level+1)
                
            pyglet.clock.schedule_once(TEMP, 2)
            pyglet.clock.schedule_once(RESUME_MUSIC, 4)


def checkIfGameOver():
    global tiles
    for i in range(5):
        for k in range(5):
            f = 24 - 5*k - i
            if (gameboard[i][4 - k] == 2 or gameboard[i][4 - k] == 3) and not tiles[f].hasBeenClicked: return False

    return True


def resetBoard(newLevel = level+1, win=True):
    global horizontalPoints
    global horizontalVolts
    global verticalPoints
    global verticalVolts
    global level
    global isGameOver
    global labels
    global pointHolder
    global points
    global gamePoints
    global window

    horizontalPoints = [0, 0, 0, 0, 0]
    horizontalVolts = [0, 0, 0, 0, 0]
    verticalPoints = [0, 0, 0, 0, 0]
    verticalVolts = [0, 0, 0, 0, 0]

    level = newLevel

    for tile in tiles:
        tile.sprite.image = pyglet.image.load("Assets/Images/Tile Flipped Down.png")
        tile.hasBeenClicked = False
        tile.hasBeenHovered = False
    
    for i in range(5):
        for k in range(5):
            gameboard[i][k] = "NA"
            if random.randint(1, 20 - level) <= 5: gameboard[i][k] = "V" # 1 in 4 chance of Voltorb
            if random.randint(1, 50 - level) <= 3: gameboard[i][k] = 3   # 1 in 15 chance of '3'
            if random.randint(1, 30 - level) <= 3: gameboard[i][k] = 2   # 1 in 10 chance of '2'
            if gameboard[i][k] == "NA": gameboard[i][k] = 1     # else, place a '1'

    for k in range(5):
        for i in range(5):
            if gameboard[i][k] == "V":
                verticalVolts[k] += 1
                horizontalVolts[i] += 1
            else:
                verticalPoints[k] += gameboard[i][k]
                horizontalPoints[i] += gameboard[i][k]
    
    labels["horizontalRedPointLabel"].text = str(horizontalPoints[0])
    labels["horizontalGreenPointLabel"].text = str(horizontalPoints[1])
    labels["horizontalYellowPointLabel"].text = str(horizontalPoints[2])
    labels["horizontalBluePointLabel"].text = str(horizontalPoints[3])
    labels["horizontalPurplePointLabel"].text = str(horizontalPoints[4])
    labels["horizontalRedVoltLabel"].text = str(horizontalVolts[0])
    labels["horizontalGreenVoltLabel"].text = str(horizontalVolts[1])
    labels["horizontalYellowVoltLabel"].text = str(horizontalVolts[2])
    labels["horizontalBlueVoltLabel"].text = str(horizontalVolts[3])
    labels["horizontalPurpleVoltLabel"].text = str(horizontalVolts[4])

    labels["verticalRedPointLabel"].text = str(verticalPoints[0])
    labels["verticalGreenPointLabel"].text = str(verticalPoints[1])
    labels["verticalYellowPointLabel"].text = str(verticalPoints[2])
    labels["verticalBluePointLabel"].text = str(verticalPoints[3])
    labels["verticalPurplePointLabel"].text = str(verticalPoints[4])
    labels["verticalRedVoltLabel"].text = str(verticalVolts[0])
    labels["verticalGreenVoltLabel"].text = str(verticalVolts[1])
    labels["verticalYellowVoltLabel"].text = str(verticalVolts[2])
    labels["verticalBlueVoltLabel"].text = str(verticalVolts[3])
    labels["verticalPurpleVoltLabel"].text = str(verticalVolts[4])

    window.set_caption("Voltorb Flip - Level " + str(level))


    if win:
        saveData["collectedPoints"] = int(saveData["collectedPoints"]) + points
        pointHolder["collectedPointsValueLabel"].text = str(saveData["collectedPoints"]).zfill(8)

        if gamePoints > int(saveData["highScore"]):
            saveData["highScore"] = str(gamePoints)

        savetoFile()

    gamePoints = 1
    points = 1

    pointHolder["levelPointsValueLabel"].text = "00000000"
    pointHolder["gamePointsValueLabel"].text = "00000000"
    isGameOver = False

################################# END RESET BOARD ##########################################
    

def updatePoints(p):
    global points
    global pointHolder
    global gamePoints

    initPoints = points # holder variable to calculate deltaPoints (dp)

    points *= p
    pointHolder["levelPointsValueLabel"].text = str(points).zfill(8)
    gamePoints += points - initPoints
    pointHolder["gamePointsValueLabel"].text = str(gamePoints).zfill(8)


def savetoFile():
    SAVEFILE = open("Save Data/save.txt", "w")
    sillyString = str(saveData)
    saveStringBytes = base64.b64encode(sillyString.encode("ascii"))

    SAVEFILE.write(saveStringBytes.decode("ascii"))
    SAVEFILE.close()

pyglet.app.run()