'''
HONOR CODE: I solemnly promise that while taking this test I will only use PyCharm or the Internet,
but I will definitely not ask another person except the instructor. Signed: Alex Randall

Update the code in this chapter to do the following:
Open a 500px by 500px window.
Change the Ball class to a Box class.
Instantiate two 30px by 30px boxes. One red and one blue.
Make the blue box have a speed of 240 pixels/second
Make the red box have a speed of 180 pixels/second
Control the blue box with the arrow keys.
Control the red box with the ASDW keys.
Do not let the boxes go off of the screen.
Incorporate different sounds when either box hits the edge of the screen.
Have two people play this TAG game at the same time.
The red box is always "it" and needs to try to catch the blue box.
When you're done Pull Request this test and comment that it's ready to be checked!
'''

import arcade

SW = 500
SH = 500
RED_SPEED = 3  # 3 x 60 = 180 pixels/second
BLUE_SPEED = 4  # 4 x 60 = 240 px/s


class Box:
    def __init__(self, pos_x, pos_y, dx, dy, size, col, sound):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.size = size
        self.col = col
        self.fart2 = arcade.load_sound(sound)
        self.loop = 0

    def draw(self):
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, self.size, self.size, self.col)

    def update(self):
        self.pos_y += self.dy
        self.pos_x += self.dx
        if self.pos_x+15 >= SW or self.pos_x-15 <= 0:
            self.dx = 0
            arcade.play_sound(self.fart2)
        if self.pos_y+15 >= SH or self.pos_y-15 <= 0:
            self.dy = 0
            self.fart2.play()

    def reset_pos(self):
        pass


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.ASH_GREY)
        self.blue_box = Box(50, 50, 0, 0, 30, arcade.color.BLUE, "Sounds/fart2.mp3")
        self.red_box = Box(50, 50, 0, 0, 30, arcade.color.RED, "Sounds/classic_hurt.mp3")

    def on_draw(self):
        arcade.start_render()
        self.red_box.draw()
        self.blue_box.draw()

    def on_update(self, dt):
        self.blue_box.update()
        self.red_box.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.blue_box.dx = -BLUE_SPEED
        elif key == arcade.key.RIGHT:
            self.blue_box.dx = BLUE_SPEED
        elif key == arcade.key.UP:
            self.blue_box.dy = BLUE_SPEED
        elif key == arcade.key.DOWN:
            self.blue_box.dy = -BLUE_SPEED

        if key == arcade.key.A:
            self.red_box.dx = -RED_SPEED
        elif key == arcade.key.D:
            self.red_box.dx = RED_SPEED
        elif key == arcade.key.W:
            self.red_box.dy = RED_SPEED
        elif key == arcade.key.S:
            self.red_box.dy = -RED_SPEED

        if key == arcade.key.SPACE:
            arcade.play_sound(self.fart2)

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.blue_box.dx = 0

        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.blue_box.dy = 0

        if key == arcade.key.A or key == arcade.key.D:
            self.red_box.dx = 0

        elif key == arcade.key.W or key == arcade.key.S:
            self.red_box.dy = 0




def main():
    window = MyGame(SW, SH, "Key Press Example")
    arcade.run()


main()
