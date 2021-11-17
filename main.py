def on_button_pressed_a():
    music.play_melody("C5 G B A F A C5 B ", 200)
    music.play_melody("C D E F G A B C5 ", 200)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    basic.show_leds("""
        # . . . #
                . # . # .
                . . # . .
                . # . # .
                # . . . #
    """)
    basic.show_leds("""
        . # # # .
                # . # . #
                # # . # #
                # . # . #
                . # # # .
    """)
basic.forever(on_forever)
