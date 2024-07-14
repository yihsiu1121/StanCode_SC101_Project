"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.8
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
is_bouncing = False
n = 1  # to count bouncing times
ball = GOval(SIZE, SIZE)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    # ball = GOval(SIZE, SIZE)
    ball.filled = True
    ball.fill_color = 'black'
    window.add(ball, START_X, START_Y)
    onmouseclicked(bouncing)


def bouncing(mouse):
    global is_bouncing, n, ball

    # is_bouncing = True  # 不能在這邊就讓它變true，這樣每次點擊耍都會變true
    anchor = GOval(SIZE, SIZE)
    window.add(anchor, mouse.x, mouse.y)  # have connection with mouse
    window.remove(anchor)
    vy = 0  # initial y velocity

    # if is_bouncing and n <= 3:  # is_bouncing=true就會進入下面動作和n<=3這寫法不對

    if not is_bouncing and n <= 3:  # 確保開關是在false狀態才能繼續執行併之後把它變true
                                    # 過程中球的開關是true所以mouseclick部會影響球掉下過程

        is_bouncing = True  # 開關從false後讓它變true

        # while True:
        while is_bouncing:  # 當is_bouncing=true執行while loop
            ball.move(VX, vy)
            pause(DELAY)
            vy = vy + GRAVITY
            if ball.y >= window.height - SIZE and ball.x < window.width:
                vy = REDUCE*vy*(-1)
                ball.move(VX, vy)
                pause(DELAY)
            elif ball.x >= window.width:
                n += 1
                ball.x = START_X
                ball.y = START_Y
                break

        is_bouncing = False  # 跑完掉落過程後把開關轉成false


if __name__ == "__main__":
    main()
