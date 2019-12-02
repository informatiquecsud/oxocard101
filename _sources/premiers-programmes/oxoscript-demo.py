def main():
    disableAutoUpdate()
    for n in [1,2,3]:
        x =random(0,3)
        y =random(0,3)
        setColor(0, 0, random(1,10)*25)

        drawPixel(x, y)
        drawPixel(x, 7 - y)
        drawPixel(7 - x, y)
        drawPixel(7 - x, 7 - y)
        
        update()
        
        delay(50)
