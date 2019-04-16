import arcade

SW = 640
SH = 480
SPEED = 3    # 3 x 60 = 180 pixels/second



class Ball:
    def __init__(self, pos_x, pos_y, dx, dy, rad, col):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.rad = rad
        self.col = col

    def draw(self):
        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.rad, self.col)

    def update(self):
        self.pos_y += self.dy
        self.pos_x += self.dx

class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.ASH_GREY)
        self.ball = Ball(50, 50, 0, 0, 15, arcade.color.AUBURN)
        self.fart1 = arcade.load_sound("Sounds/fart1.mp3")

    def on_draw(self):
        arcade.start_render()
        self.ball.draw()

    def on_update(self, dt):
        self.ball.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.ball.dx = -SPEED
        elif key == arcade.key.RIGHT:
            self.ball.dx = SPEED
        elif key == arcade.key.UP:
            self.ball.dy = SPEED
        elif key == arcade.key.DOWN:
            self.ball.dy = -SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball.dx = 0
            arcade.play_sound(self.fart1)

        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball.dy = 0

def main():
    window = MyGame(SW, SH, "Key Press Example")
    arcade.run()

main()