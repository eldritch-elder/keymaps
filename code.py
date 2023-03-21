# Main Keyboard Configuration
# -- some imports
import board
import pog
import supervisor
from kmk.keys import KC


# -- check if we just want to run the coord_mappping finder
if pog.coordMappingAssistant:
    print('running coordmap setup')
    from coordmaphelper import KMKKeyboard
else:
    from kb import KMKKeyboard

keyboard = KMKKeyboard()

keyboard.debug_enabled = False
supervisor.runtime.autoreload = False

# -- Append Modules and Extensions to our Keyboard
from kmk.modules.oneshot import OneShot
keyboard.modules.append(OneShot())


from kmk.extensions.media_keys import MediaKeys
keyboard.extensions.append(MediaKeys())

from kmk.modules.capsword import CapsWord
keyboard.modules.append(CapsWord())

from kmk.modules.layers import Layers
keyboard.modules.append(Layers())

from kmk.extensions.RGB import RGB
from kmk.quickpin.pro_micro.helios import pinout
keyboard.extensions.append(
    RGB(
        pixel_pin=pinout[5],
        num_pixels=18,
        rgb_order=(1, 0, 2),
        val_limit=40,
        hue_default=220,
        hue_step=1,
        sat_default=255,
        sat_step=1,
        val_default=35,
        val_step=5,
    ))

# -- Keymap
if not pog.coordMappingAssistant:
    import keymap
    keyboard.keymap = keymap.keymap
    if pog.hasEncoders:
        from kb import encoder_handler
        encoder_handler.map = keymap.encoderKeymap


# helper function to make things a bit easier to write
def mkchord(behaviour, seq_index, delta=0):
    '''
    takes the index of the keys reqauired to press for the chord and translates them to the right coordinates to do
    layer/key indepentant chording, also makes it easier to do different timeouts for different chords without adding
    too much verbosity by setting  base value the delta gets added to.
    '''
    coordinates = [keyboard.coord_mapping[i] for i in seq_index]
    return Chord(coordinates, behaviour, match_coord=True, timeout=40 + delta)

from kmk.modules.combos import Combos, Chord, Sequence
combos = Combos()
combos.combos = [
    # ; mods 
    mkchord(KC.OS(KC.LCTL), (25, 26)),
    mkchord(KC.OS(KC.LSFT), (8, 9)),
    mkchord(KC.OS(KC.LALT), (31, 32)),
    mkchord(KC.CW, (16, 19)),

    # ; misc
    mkchord(KC.BSPACE, (19, 20)),
    mkchord(KC.LCTL(KC.BSPACE), (19, 20, 21)),
    mkchord(KC.DELETE, (15, 16)),
    mkchord(KC.ESCAPE, (13, 16)),

    # ; 'schland
    mkchord(KC.RALT(KC.A), (25, 27)),
    mkchord(KC.RALT(KC.U), (30, 32)),
    mkchord(KC.RALT(KC.O), (30, 33)),

    # ; symbols
    mkchord(KC.LPRN, (2, 16)),
    mkchord(KC.RPRN, (19, 9)),
    mkchord(KC.LBRC, (14, 16), delta=-5),
    mkchord(KC.RBRC, (19, 21), delta=-5),
    mkchord(KC.LCBR, (3, 16)),
    mkchord(KC.RCBR, (19, 8)),
    mkchord(KC.LABK, (25, 16)),
    mkchord(KC.RABK, (19, 32)),
    mkchord(KC.EXCLAIM, (2, 3, 16), delta=10),
    mkchord(KC.QUESTION, (14, 15, 4), delta=10),
    mkchord(KC.COLON, (6, 7)),
    mkchord(KC.SCOLON, (30, 31)),
    mkchord(KC.EQUAL, (7, 8)),
    mkchord(KC.GRAVE, (9, 10)),
    mkchord(KC.TILDE, (32, 33)),
    mkchord(KC.DQT, (7, 10)),

    # Heres a table with the positions for reference:
    # |  0 |  1 |  2 |  3 |  4 |  5 |    |  6 |  7 |  8 |  9 | 10 | 11 |
    # | 12 | 13 | 14 | 15 | 16 | 17 |    | 18 | 19 | 20 | 21 | 22 | 23 |
    # |    | 24 | 25 | 26 | 27 | 28 |    | 29 | 30 | 31 | 32 | 33 |    |
    # |    |    |    | 34 | 35 | 36 | 37 | 38 | 39 | 40 |    |    |    |
]
keyboard.modules.append(combos)

if __name__ == '__main__':
    keyboard.go()
