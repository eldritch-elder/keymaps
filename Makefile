FILES=keymap.c config.h rules.mk

KM=jat
KB=splitkb/kyria/rev1

compile:
	qmk compile -kb $(KB) -km $(KM)

flash: compile
	nix run github:eldritch-elder/hid-bootloader-cli.nix# -- --mcu=atmega32u4 -wv ../../../../../splitkb_kyria_rev1_jat.hex

tangle: main.org
	./org-tangle main.org

clean:
	rm -rf $(FILES)
	qmk clean
