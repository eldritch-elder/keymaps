KB=splaytoraid40
B=nice_nano

compile: build/$(KB)/zephyr/zmk.uf2 # only there to be called by taskrunner for compiling only

build/$(KB)/zephyr/zmk.uf2: config/$(KB).keymap config/$(KB).conf
	 west build -s ../app -d build/$(KB) -b $(B) -p -- -DSHIELD=$(KB) -DZMK_CONFIG=$(shell pwd)/config

flash: build/$(KB)/zephyr/zmk.uf2
	sleep 5s
	cp build/$(KB)/zephyr/zmk.uf2 /run/media/$(shell whoami)/NICENANO/.

.PHONY: clean
clean:
	rm -rf build/*
