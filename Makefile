DRIVE=/run/media/$(shell whoami)/CIRCUITPY


flash: code.py
	cp -rv code.py $(DRIVE)
