from cmu_112_graphics import *

def appStarted(app):
    app.time = 5
    app.timerDelay = 1000
    app.gameOver = False

def timerFired(app):
    if app.time == 0:
        app.gameOver = True
        return
    app.time -= 1

def redrawAll(app, canvas):
    s = "Time = " + str(app.time)
    canvas.create_text(app.width/2, 20, text=s)
    if app.gameOver:
        canvas.create_text(app.width/2, 50, text="Game Over")

    
runApp(width=400, height=400)