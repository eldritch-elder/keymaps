# keymap

this is the firmware for the splaytoraid40 rev3 with a helios rp2040 on zmk.

## how to use

this repo is made for local building, grab the zmk repo at first before proceeding to initialize and update `west`
``` sh
git submodule update --init
cd zmk/app
west init
west update 
```

a `flake.nix` with the environment declared is provided, just do `direnv allow` when you have in your system

## limitations

- rgb doesn't work yet on helios
- gotta test and add the overlays for the nice!nanos (don't have the hardware)
