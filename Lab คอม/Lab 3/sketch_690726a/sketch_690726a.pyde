def setup():
    size(500,500)

x = 50
y = 50

direction = 0
speed = 2

    
def draw():
    global x,y,direction

    background(255)


    rect(x,y,50,50)       
    rect(x,y-50,50,50)      
    rect(x,y+50,50,50)      
    rect(x-50,y,50,50)       
    rect(x+50,y,50,50)      


    if direction == 0:      
        x += speed
        if x >= 300:
            direction = 1

    elif direction == 1:      
        y += speed
        if y >= 300:
            direction = 2

    elif direction == 2:        
        x -= speed
        if x <= 100:
            direction = 3

    elif direction == 3:      
        y -= speed
        if y <= 100:
            direction = 0
            
            
