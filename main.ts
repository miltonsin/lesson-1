music.playMelody("E B G A F C5 - F ", 500)
led.plot(1, 2)
while (false) {
    basic.clearScreen()
}
basic.forever(function () {
    basic.showIcon(IconNames.Ghost)
    basic.showArrow(ArrowNames.NorthEast)
    basic.showString("Hello!")
    basic.clearScreen()
    basic.showLeds(`
        # . # . #
        . . . . .
        # . # . #
        . . . . .
        # . # . #
        `)
    basic.showLeds(`
        # # # # #
        # . . . #
        # . # . #
        # . . . #
        # # # # #
        `)
    basic.showNumber(7)
    if (true) {
        basic.showIcon(IconNames.Heart)
    }
})
