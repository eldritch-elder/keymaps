FILES=keymap.c config.h rules.mk


tangle:
	org-tangle main.org

clean:
	rm -rf $(FILES)
