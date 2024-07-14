"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.x = window_width/2 - paddle_width/2
        self.paddle.y = window_height - paddle_offset - paddle_height
        self.window.add(self.paddle, x=self.paddle.x, y=self.paddle.y)
        # Center a filled ball in the graphical window
        self.ball = GOval(BALL_RADIUS*2, BALL_RADIUS*2)
        self.ball.filled = True
        self.ball.x = window_width/2 - BALL_RADIUS
        self.ball.y = window_height/2 - BALL_RADIUS
        self.__dx = 0
        self.__dy = 0
        self.window.add(self.ball, x=self.ball.x, y=self.ball.y)

        # Default initial velocity for the ball
        # Initialize our mouse listeners
        onmouseclicked(self.handle_mouse_click)
        onmousemoved(self.handle_mouse_move)

        # Draw bricks
        self.rows = brick_rows
        self.cols = brick_cols
        self.brick_count = 0

        for i in range(brick_rows):
            for j in range(brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.brick.fill_color = self.get_brick_color(i)
                self.window.add(self.brick, x=0+j*(brick_spacing+brick_width),
                                y=0+brick_offset+i*(brick_spacing+brick_height))
                self.brick_count += 1  # to calculate total numbers of bricks

        # Game status
        self.is_ball_in_the_motion = False

    @staticmethod
    def get_brick_color(row):
        colors = ['red', 'orange', 'yellow', 'green', 'blue']
        return colors[(row // 2) % len(colors)]  # to get color of the list

    def set_ball_velocity(self):
        self.__dx = random.randint(0, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx

    # Handles the mouse move event to update the paddle position
    def handle_mouse_move(self, event):
        new_x = event.x - self.paddle.width / 2
        if new_x <= 0:
            new_x = 0
        elif new_x >= self.window.width - self.paddle.width:
            new_x = self.window.width - self.paddle.width
        self.paddle.x = new_x

    # Handles the mouse click event to start the ball motion
    def handle_mouse_click(self, event):
        if not self.is_ball_in_the_motion:
            self.set_ball_velocity()
            self.is_ball_in_the_motion = True

    # Return the ball's x velocity
    def get_dx(self):
        return self.__dx

    # Return the ball's y velocity
    def get_dy(self):
        return self.__dy

    # set ball's x velocity
    def set_dx(self, dx):
        self.__dx = dx

    # set ball's y velocity
    def set_dy(self, dy):
        self.__dy = dy

    # Reset the ball to the starting position and stops its movements
    def reset_ball(self):
        self.ball.x = self.window.width / 2 - BALL_RADIUS
        self.ball.y = self.window.height / 2 - BALL_RADIUS
        self.window.add(self.ball, x=self.ball.x, y=self.ball.y)
        self.is_ball_in_the_motion = False

    # Moves the ball according to its velocity and checking collision conditions
    def move_ball(self):
        if self.is_ball_in_the_motion:
            self.ball.move(self.__dx, self.__dy)
            self.check_for_collisions()

    # check for collision with walls, paddle, and bricks, and update ball directions
    def check_for_collisions(self):

        # Check for collision with left and right walls
        if self.ball.x <= 0 or self.ball.x + self.ball.width >= self.window.width:
            self.__dx = -self.__dx

        # Check for collision with the top wall
        if self.ball.y <= 0:
            self.__dy = -self.__dy

        # Check for collision with the bottom wall
        if self.ball.y + self.ball.height >= self.window.height:
            self.reset_ball()

        # Check for collision with the paddle

        # 這版本會導致球從側邊進入板子後上下震盪
        # if self.ball.y + self.ball.height >= self.paddle.y and \
        #         self.paddle.x <= self.ball.x + self.ball.width / 2 <= self.paddle.x + self.paddle.width:
        #     self.__dy = -self.__dy

        # modified version for fixed lateral collision for paddle
        # self.ball.y + self.ball.height >= self.paddle.y --> 檢查球的底部是否超過板子
        # self.paddle.x <= self.ball.x + self.ball.width / 2 <= self.paddle.x + self.paddle.width
        # -->檢查球的水平中心是否在板子的水平範圍內
        if self.ball.y + self.ball.height >= self.paddle.y and \
                self.paddle.x <= self.ball.x + self.ball.width / 2 <= self.paddle.x + self.paddle.width:

            if self.__dy > 0:  # ensure ball is moving downward to avoid bug of lateran collision
                self.__dy = -self.__dy

        # Check for collision with bricks
        # 將球的4個角座標儲存在一個二維陣列中
        corners = [
            [self.ball.x, self.ball.y],  # 左上角
            [self.ball.x + self.ball.width, self.ball.y],  # 右上角
            [self.ball.x, self.ball.y + self.ball.height],  # 左下角
            [self.ball.x + self.ball.width, self.ball.y + self.ball.height]]  # 右下角

        for corner in corners:
            # 檢查座標上是否有物體
            obj = self.window.get_object_at(corner[0], corner[1])
            if obj is not None and obj != self.paddle:
                self.window.remove(obj)
                self.brick_count -= 1

                # previous code only change y direction without consideration of collision of x direction
                # self.__dy = -self.__dy

                # check collision for y direction(ensure ball y between obj top and bottom--> use "and")
                if self.ball.y <= obj.y + obj.height and self.ball.y + self.ball.height >= obj.y:
                    self.__dy = -self.__dy

                # check collision for x direction(ensure ball y between obj left and right--> use "and")
                elif self.ball.x <= obj.x + obj.width and self.ball.x + self.ball.width >= obj.x:
                    self.__dx = -self.__dx
                break




