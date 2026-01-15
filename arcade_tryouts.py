import arcade
from pyglet.event import EVENT_HANDLE_STATE


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        # Call the parent class's init function
        super().__init__(width, height, title)
    def on_draw(self):
        arcade.draw_circle_filled(300,250,100, (0,255,255))
        arcade.draw_triangle_outline(100,100,200,100,150,200,(255,0,0))


def main():

    window = MyGame(640, 480, "japan nega")
    arcade.run()





main()