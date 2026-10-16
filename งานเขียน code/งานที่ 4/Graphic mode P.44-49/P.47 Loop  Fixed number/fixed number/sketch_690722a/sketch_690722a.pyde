def setup():
    size(500, 500)
    background(255)

    draw_rain_drops(100)


def draw_circle(x, y, r):
    ellipse(x, y, r * 2, r * 2)


def draw_rain_drops(n):
    i = 0
    while i < n:       
        x = random(100, 400)
        y = random(150, 350)
        r = random(3, 30)

        draw_circle(x, y, r)

        i = i + 1
