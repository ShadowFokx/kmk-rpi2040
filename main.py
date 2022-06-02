import board
from kmk.extensions.RGB import RGB
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC

print("start")


keyboard = KMKKeyboard()

keyboard.debug_enabled = True

keyboard.col_pins = (board.GP7, board.GP9)  # try D5 on Feather, keeboar
keyboard.row_pins = (board.GP8,)  # try D6 on Feather, keeboar
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [[KC.A, KC.B]]


rgb_ext = RGB(pixel_pin=board.GP15, num_pixels=2)
keyboard.extensions.append(rgb_ext)


if __name__ == '__main__':
    keyboard.go()

    
