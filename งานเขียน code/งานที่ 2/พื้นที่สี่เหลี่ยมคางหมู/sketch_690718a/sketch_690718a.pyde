size(500,500)

def draw_trapezoid(x,y):
    x = 100
    y = 100

    line(x,y,x,y+300)
    line(x,y,x+200,y)
    line(x+200,y,x+300,y+300)
    line(x,y+300,x+300,y+300)
    
draw_trapezoid(100,100)
