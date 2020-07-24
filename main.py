def on_button_pressed_a():
    led.plot_brightness(2, 3, 152)
    led.set_brightness(255)
input.on_button_pressed(Button.A, on_button_pressed_a)

music.play_melody("E B G A F C5 - F ", 500)
led.plot(1, 2)
while False:
    basic.clear_screen()

def on_forever():
    basic.show_icon(IconNames.GHOST)
    basic.show_arrow(ArrowNames.NORTH_EAST)
    basic.show_string("Hello!")
    basic.clear_screen()
    basic.show_leds("""
        # . . . #
        . . . . .
        # . # . #
        . . . . .
        # . # . #
        """)
basic.forever(on_forever)
def on_forever2():
    pass
basic.forever(on_forever2)