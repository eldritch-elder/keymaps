KB=splaytoraid40
B=sparkfun_pro_micro_rp2040
MEDIA=RPI-RP2

compile: zmk/build/$(KB)/zephyr/zmk.uf2

zmk/build/$(KB)/zephyr/zmk.uf2: boards/shields/$(KB)/$(KB).keymap boards/shields/$(KB)/$(KB).conf
	cd zmk; west build -s app -d build/$(KB) -b $(B) -p -- -DSHIELD=$(KB) -DZMK_EXTRA_MODULES="$(shell pwd)"

flash: zmk/build/$(KB)/zephyr/zmk.uf2
	sleep 5s
	cp zmk/build/$(KB)/zephyr/zmk.uf2 /run/media/$(shell whoami)/$(MEDIA)

.PHONY: clean
clean:
	rm -rf build/*
