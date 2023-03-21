# These are yous custom keycodes do any needed imports at the top
# then you can reference them in your keymap with for example customkeys.MyKey

from kmk.keys import KC, make_key

MyKey = KC.X


# import storage
# make_key(
#     names=("STORAGE_ON"),
#     on_press=lambda **kwargs: storage.enable_usb_drive(),
# )

# make_key(
#     names=("STORAGE_OFF"),
#     on_press=lambda **kwargs: storage.disable_usb_drive(),
# )