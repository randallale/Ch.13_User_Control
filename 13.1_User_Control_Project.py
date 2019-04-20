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
OBJECT_AMOUNT = 20


class Rocket(object):
    def __init__(self, start_x, start_y):
        self.rocket_x = start_x
        self.rocket_y = start_y
        self.dx = 0
        self.dy = 0
        self.rocket_color = random_color()

    def draw_rocket(self):
        tip_list = ((self.rocket_x - 15, self.rocket_y + 30), (self.rocket_x, self.rocket_y + 45),
                    (self.rocket_x + 15, self.rocket_y + 30))
        arcade.draw_rectangle_filled(self.rocket_x, self.rocket_y, 30, 60, self.rocket_color)
        arcade.draw_polygon_filled(tip_list, self.rocket_color)

    def reset_pos(self):
        self.rocket_x = SCREEN_WIDTH/2
        self.rocket_y = SCREEN_HEIGHT/4
        self.rocket_color = random_color()
        self.dx = 0
        self.dy = 0

    def update(self):
        self.rocket_y += self.dy
        self.rocket_x += self.dx

        if self.rocket_y+45 >= SCREEN_HEIGHT:
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

    def get_location(self, area):
        if area == "left":
            rocket_left = self.rocket_x - 30
            return rocket_left
        elif area == "right":
            rocket_right = self.rocket_x + 30
            return rocket_right
        elif area == "top":
            rocket_top = self.rocket_y + 30
            return rocket_top
        elif area == "bottom":
            rocket_bottom = self.rocket_y - 30
            return rocket_bottom


class Objects(Rocket):
    def __init__(self, object_x, object_y):
        self.object_x = object_x
        self.object_y = object_y
        self.object_color = random_color()
        self.speed = random.randrange(2, 4)

    def draw_object(self):
        arcade.draw_circle_filled(self.object_x, self.object_y, 8, self.object_color)

    def update(self):
        self.object_y -= self.speed
        if self.object_y <= -10:
            self.object_y = random.randrange(SCREEN_HEIGHT, SCREEN_HEIGHT+100)
            self.object_x = random.randrange(0, SCREEN_WIDTH)
            self.object_color = random_color()
            self.speed = random.randrange(2, 4)

    def get_location(self, area):
        if area == "left":
            object_x_left = self.object_x-8
            return object_x_left
        elif area == "right":
            object_x_right = self.object_x+8
            return object_x_right
        elif area == "top":
            object_y_top = self.object_y+8
            return object_y_top
        elif area == "bottom":
            object_y_bottom = self.object_y-8
            return object_y_bottom

    def stop(self):
        self.speed = 0

    def reset_pos(self):
        self.object_y = random.randrange(SCREEN_HEIGHT, SCREEN_HEIGHT + 100)
        self.object_x = random.randrange(0, SCREEN_WIDTH)
        self.object_color = random_color()
        self.speed = random.randrange(2, 4)


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)

        # If you have sprite lists, you should create them here,
        # and set them to None
        self.object_list = []
        self.object = None
        self.rocket = None
        self.score = 0
        self.end = False
        self.numbers = []
        self.endscore = None
        self.f = 0

    def setup(self):
        # Create your sprites and sprite lists here
        self.f = open("Highscore.txt", "a+")
        self.f.close()
        self.sort_score()
        for i in range(OBJECT_AMOUNT):
            self.object = Objects(random.randrange(0, SCREEN_WIDTH+1),
                                  random.randrange(SCREEN_HEIGHT, SCREEN_HEIGHT+200))
            self.object_list.append(self.object)
        self.rocket = Rocket(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Only hit your color!",
                         SCREEN_WIDTH / 2, SCREEN_HEIGHT - 28, arcade.color.BLACK, 28, width=2000, align="center",
                         anchor_x="center", anchor_y="center")
        self.sort_score()
        arcade.draw_text(f'The highscore is {self.numbers[-1]}!',
                         SCREEN_WIDTH / 10, + 15, arcade.color.BLACK, 15, width=2000, align="center",
                         anchor_x="center", anchor_y="center")

        # Call draw() on all your sprite lists below
        for self.object in self.object_list:
            self.object.draw_object()
        self.rocket.draw_rocket()
        if self.end is True:
            self.endscore = f'Your score is {self.score}'
            arcade.draw_text(self.endscore, SCREEN_WIDTH / 2, 28, arcade.color.BLACK, 28,
                             width=2000, align="center", anchor_x="center", anchor_y="center")
            arcade.draw_text("Press space to reset!", SCREEN_WIDTH / 2, SCREEN_HEIGHT/2, arcade.color.BLACK, 50,
                             width=2000, align="center", anchor_x="center", anchor_y="center")

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        for self.object in self.object_list:
            self.object.update()
            # Checks if object is inside the rocket
            if self.rocket.get_location("left") < self.object.get_location("left") and \
                    self.rocket.get_location("right") > self.object.get_location("right") and \
                    self.rocket.get_location("top") > self.object.get_location("top") and \
                    self.rocket.get_location("bottom") < self.object.get_location("bottom"):
                if self.rocket.rocket_color == self.object.object_color:
                    self.object.reset_pos()
                    self.score += 1
                    self.rocket.rocket_color = random_color()
                elif self.rocket.rocket_color != self.object.object_color:
                    self.object.reset_pos()
                    self.rocket.rocket_color = arcade.color.BLACK
                    for self.object in self.object_list:
                        self.object.stop()
                    self.end = True
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
        if self.end is True:
            if key == arcade.key.SPACE:
                self.end = False
                self.f = open("Highscore.txt", "a+")
                self.f.write(f"{self.score}\r")
                self.f.close()
                self.score = 0
                self.rocket.reset_pos()
                for self.object in self.object_list:
                    self.object.reset_pos()
                self.sort_score()

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

    def sort_score(self):
        with open('Highscore.txt', 'r') as f:
            lines = f.readlines()
        self.numbers = [int(e.strip()) for e in lines]
        self.numbers.sort()
        f.close()


def random_color():
    return random.choice((arcade.color.RED, arcade.color.ORANGE, arcade.color.YELLOW,
                          arcade.color.GREEN, arcade.color.BLUE, arcade.color.VIOLET))


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
