#FILES=keymap.c config.h rules.mk

#KM=jat
KB=splaytoraid40
B=nice_nano

compile:
	$(foreach keeb,$(KB),west build -s ../app -d build/$(keeb) -b $(B) -p -- -DSHIELD=$(keeb) -DZMK_CONFIG=$(shell pwd)/config;)

clean:
	rm -rf build/*
