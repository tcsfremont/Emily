import pgzrun
player=Actor('ranger')
player.x=400
player.y = 600 - player.height * 0.5
aliens=[]
def add_alien():
    alien=Actor('slimey')
    alien.x = 400
    alien.y = alien.height * 0.5
    aliens.append(alien)
clock.schedule_interval(add_alien,5)# every 5 seconds
lasers = []
def fire_laser():
    laser = Rect((player.x, player.y), (10,50))
    lasers.append(laser)
def update():
    if keyboard.left:
        player.x = max(player.width * 0.5,  player.x - 5)
    if keyboard.right and player.x < 800-player.width * 0.5:
        player.x=min(800 - player.width * 0.5, player.x + 5)
    if keyboard.space:
        fire_laser()
    for laser in lasers:
        laser.y -=10
def draw():
    screen.clear()
    player.draw()
    for laser in lasers:
        screen.draw.filled_rect(laser, (227,115,131 ))
    for alien in aliens:
        alien.draw()
pgzrun.go()