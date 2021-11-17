input.onButtonPressed(Button.A, function () {
    music.playMelody("C5 G B A F A C5 B ", 200)
    music.playMelody("C D E F G A B C5 ", 200)
})
basic.pause(100)
basic.forever(function () {
    basic.showLeds(`
        # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
        `)
    basic.showLeds(`
        . # # # .
        # . # . #
        # # . # #
        # . # . #
        . # # # .
        `)
})
