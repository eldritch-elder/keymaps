KB=splaytoraid40
B=nice_nano

.PHONY: clean
clean:
	rm -rf build/*

build/$(KB)/zephyr/zmk.uf2: config/$(KB).keymap
	 west build -s ../app -d build/$(KB) -b $(B) -p -- -DSHIELD=$(KB) -DZMK_CONFIG=$(shell pwd)/config

compile: build/$(KB)/zephyr/zmk.uf2 # only there to be called by taskrunner for compiling only

flash: build/$(KB)/zephyr/zmk.uf2
	cp build/$(KB)/zephyr/zmk.uf2 /run/media/freja/NICENANO/.
