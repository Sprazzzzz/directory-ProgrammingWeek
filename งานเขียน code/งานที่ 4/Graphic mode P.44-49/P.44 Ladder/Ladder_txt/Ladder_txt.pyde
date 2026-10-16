def setup():
    size(500,500)
    
x=100
y=200
s=300
    
def draw_ladder(x,y,s):
    line(x,x,x,y+y)
    line(y+y,x,y+y,y+y)
    y=random(150,350)
    line(x,y,x+s,y)


def draw():
    draw_ladder(x,y,s)
