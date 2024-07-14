"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    # Add the animation loop here!

    # wait for users to start the game
    while not graphics.is_ball_in_the_motion:
        pause(FRAME_RATE)

    while lives > 0:

        graphics.move_ball()
        pause(FRAME_RATE)

        if not graphics.is_ball_in_the_motion:
            lives -= 1
            print(lives)  # check status
            if lives > 0:
                graphics.reset_ball()
                # Wait for user to click to start the ball motion again
                while not graphics.is_ball_in_the_motion:
                    pause(FRAME_RATE)

        # conditions for game end
        elif graphics.brick_count == 0:
            print("Game Over! All bricks removed")
            break

    # conditions for game end
    if lives == 0:
        print('Game Over!')


if __name__ == '__main__':
    main()
