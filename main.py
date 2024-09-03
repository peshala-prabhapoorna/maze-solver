from graphics import Line, Point, Window


def main():
    win = Window(800, 600)
    point1 = Point(50, 50)
    point2 = Point(750, 50)
    line1 = Line(point1, point2)
    win.draw_line(line1, "black")
    win.wait_for_close()


main()
