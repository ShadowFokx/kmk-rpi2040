import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.RGB import RGB
from kb import rgb_pixel_pin
from kmk.extensions.RGB import RGB, AnimationModes

print("Starting")
keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP7, board.GP9)  # try D5 on Feather, keeboar
keyboard.row_pins = (board.GP8,)  # try D6 on Feather, keeboar
keyboard.diode_orientation = DiodeOrientation.COL2ROW

print("begin key")
keyboard.keymap = [[KC.A, KC.B]]

print("bgin rgb")
rgb_ext = RGB(
    pixel_pin=board.GP15,
    num_pixels=2,
    animation_mode=AnimationModes.RAINBOW,
)
print("end")
if __name__ == "__main__":
    keyboard.go()
