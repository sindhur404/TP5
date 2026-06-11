"""
Ce code présente un paysage tropical qui m'aide à comprendre comment dessiner dans Arcade en utilisant toutes les formes de la bibliothèque
RYAN SINDHU 404
"""import arcade

# Window dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "TP5 plage tropicale"


def dessiner_decor_base():
    """Draws the sky, sun, sea, and sand.


    Uses: rectangle, circle, ellipse.
    """
    # Sky (Background)
    arcade.draw_lbwh_rectangle_filled(left=0, bottom=0, width=800, height=600, color=arcade.color.ORANGE_PEEL)

    # Soliel
    arcade.draw_circle_filled(center_x=650, center_y=280, radius=70, color=arcade.color.SUNGLOW)

    # Sea
    arcade.draw_lbwh_rectangle_filled(left=0, bottom=60, width=800, height=200, color=arcade.color.DARK_BLUE)

    # beach
    arcade.draw_ellipse_filled(center_x=200, center_y=-50, width=900, height=350, color=arcade.color.DESERT_SAND)


def dessiner_nuages():
    # Clouds
    arcade.draw_arc_outline(
        center_x=150, center_y=480, width=120, height=60, color=arcade.color.WHITE, start_angle=0, end_angle=180,
        border_width=3)
    arcade.draw_line(start_x=90, start_y=480, end_x=210, end_y=480, color=arcade.color.WHITE, line_width=3)

    arcade.draw_arc_outline(center_x=400, center_y=520, width=160, height=80, color=arcade.color.WHITE, start_angle=0,
                            end_angle=180, border_width=3)
    arcade.draw_line(start_x=320, start_y=520, end_x=480, end_y=520, color=arcade.color.WHITE, line_width=3)

    # stars (Points)
    star_points = [(700, 550), (750, 520), (620, 570), (780, 580)]
    arcade.draw_points(
        point_list=star_points,
        color=arcade.color.WHITE,
        size=4
    )


def dessiner_palmier():
    """Draws a palm tree on the left side of the beach with thickened leaves.


    Uses: polygon.
    """
    #tree
    trunk_points = [(80, 80), (110, 80), (160, 380), (140, 380)]

    arcade.draw_polygon_filled(
        point_list=trunk_points,
        color=arcade.color.BROWN)

    # leaves
    arcade.draw_polygon_filled(
        point_list=[(140, 385), (145, 365), (100, 330), (50, 340)],
        color=arcade.color.FOREST_GREEN
    )

    arcade.draw_polygon_filled(
        point_list=[(160, 385), (155, 365), (200, 340), (260, 340)],
        color=arcade.color.FOREST_GREEN
    )
    arcade.draw_polygon_filled(
        point_list=[(135, 380), (165, 380), (185, 420), (170, 460)],
        color=arcade.color.FOREST_GREEN
    )


def dessiner_crab():
    # Crab
    arcade.draw_lbwh_rectangle_filled(
        left=325, bottom=45,
        width=50, height=30,
        color=(255, 0, 0)
    )
    # crab hands
    arcade.draw_triangle_filled(x1=310, y1=65, x2=325, y2=85, x3=325, y3=50, color=arcade.color.RED)

    arcade.draw_triangle_filled(x1=390, y1=65, x2=375, y2=85, x3=375, y3=50, color=arcade.color.RED)


def my_sign():
    arcade.draw_text(text="Vacances de reve by Ryan SINDHU", x=30, y=30, color=arcade.color.DARK_BROWN, font_size=18,
                     font_name="Arial")


def main():
    """Main program function."""
    # the window
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    arcade.start_render()

    # draw functions
    dessiner_decor_base()
    dessiner_nuages()
    dessiner_palmier()
    dessiner_crab()
    my_sign()

    arcade.finish_render()

    arcade.run()


if __name__ == "__main__":
    main()
