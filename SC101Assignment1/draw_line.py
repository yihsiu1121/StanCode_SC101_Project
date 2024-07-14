"""
File: 
Name: YI HSIU
-------------------------
TODO: draw lines
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# define size of hollow circle
SIZE = 30
# a window created for common used
window = GWindow()
# create a object called hole that can be seen by all functions
hole = GOval(SIZE, SIZE)
# initial condition for mouse click times
n = 1


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(create_line)
    # n = n + 1  # n不能寫在這做計數，他只會被執行一次要寫在onmouseclick的functioin中才會每次被看到


def create_line(mouse):
    global n, hole

    if n % 2 == 1:  # when n is odd-->draw hollow circle
        hole.filled = False
        hole.color = 'black'
        window.add(hole, x=mouse.x-SIZE/2, y=mouse.y-SIZE/2)

    else:  # draw line and remove hollow circle
        line = GLine(hole.x, hole.y, mouse.x, mouse.y)
        window.remove(hole)
        window.add(line)

    n += 1  # to count mouse click times


if __name__ == "__main__":
    main()
