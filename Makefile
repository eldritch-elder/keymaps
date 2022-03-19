FILES=keymap.c config.h rules.mk

KM=jat
KB=splitkb/kyria/rev1

compile:
	qmk compile -kb $(KB) -km $(KM)

flash:
	qmk flash -kb $(KB) -km $(KM)

tangle: main.org
	./org-tangle main.org

clean:
	rm -rf $(FILES)
	qmk clean
