def setup():
    size(500, 500)
    background(255)

    draw_vertical_lines(100, 250, 400, 250)


def draw_vertical_lines(x1, y1, x2, y2):
    space = abs(x1 - x2) // 5

    while x1 <= x2:
        line(x1, y1 - 50, x1, y1 + 50)
        x1 = x1 + space
