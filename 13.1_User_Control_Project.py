"""
USER CONTROL PROJECT
-----------------
Your choice!!! Have fun and be creative.
Create a background and perhaps animate some objects.
Pick a user control method and navigate an object around your screen.
Make your object more interesting than a ball.
Create your object with a new class.
Perhaps move your object through a maze or move the object to avoid other moving objects.
Incorporate some sound.
Type the directions to this project below:

DIRECTIONS:
----------
Please type directions for this game here.
"""

import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "13.1 User Control Project"
ROCKET_SPEED = 5


class Rocket:
    def __init__(self, start_x, start_y):
        self.rocket_x = start_x
        self.rocket_y = start_y
        self.dx = 0
        self.dy = 0
        self.color = random_color()

    def draw_rocket(self):
        arcade.draw_rectangle_filled(self.rocket_x, self.rocket_y, 30, 60, self.color)

    def reset_pos(self):
        pass

    def update(self):
        self.rocket_y += self.dy
        self.rocket_x += self.dx

        if self.rocket_y+30 >= SCREEN_HEIGHT:
            self.rocket_y -= 1
            self.dy = 0
        elif self.rocket_y-30 <= 0:
            self.rocket_y += 1
            self.dy = 0
        if self.rocket_x+15 >= SCREEN_WIDTH:
            self.rocket_x -= 1
            self.dx = 0
        elif self.rocket_x - 15 <= 0:
            self.rocket_x += 1
            self.dx = 0


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)

        # If you have sprite lists, you should create them here,
        # and set them to None
        self.rocket = None

    def setup(self):
        # Create your sprites and sprite lists here
        self.rocket = Rocket(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    def on_draw(self):
        """
        Render the screen.
        """
        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()
        arcade.draw_text("Don't hit the objects!",
                         SCREEN_WIDTH / 2, SCREEN_HEIGHT - 28, arcade.color.BLACK, 28, width=2000, align="center",
                         anchor_x="center", anchor_y="center")

        self.rocket.draw_rocket()
        # Call draw() on all your sprite lists below

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.rocket.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.rocket.dx -= ROCKET_SPEED
        elif key == arcade.key.RIGHT:
            self.rocket.dx += ROCKET_SPEED
        elif key == arcade.key.UP:
            self.rocket.dy += ROCKET_SPEED
        elif key == arcade.key.DOWN:
            self.rocket.dy -= ROCKET_SPEED

    def on_key_release(self, key, key_modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.rocket.dx = 0
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.rocket.dy = 0

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        pass


def random_color():
    return random.choice((arcade.color.RED, arcade.color.ORANGE, arcade.color.YELLOW,
                          arcade.color.GREEN, arcade.color.BLUE, arcade.color.VIOLET))


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
