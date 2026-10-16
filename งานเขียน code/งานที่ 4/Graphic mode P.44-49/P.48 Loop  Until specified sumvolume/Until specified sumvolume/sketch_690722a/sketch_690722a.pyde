def setup():
    size(500, 500)
    background(255)

    draw_rain_drops_until(300)


def draw_circle(x, y, r):
    ellipse(x, y, r * 2, r * 2)


def draw_rain_drops_until(volume):
    total = 0

    while total < volume:
        x = random(100, 400)
        y = random(150, 350)
        r = random(3, 30)

        draw_circle(x, y, r)

        total = total + r
