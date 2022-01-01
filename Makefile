FILES=keymap.c config.h rules.mk

KM=jat
KB=splitkb/kyria

compile: $(FILES)
	qmk compile -kb $(KB) -km $(KM)

flash: $(FILES)
	qmk flash -kb $(KB) -km $(KM)

lint: $(FILES)
	qmk lint -kb $(KB) -km $(KM)

$(FILES): main.org
	./org-tangle main.org

tangle: main.org
	./org-tangle main.org

clean:
	rm -rf $(FILES)
