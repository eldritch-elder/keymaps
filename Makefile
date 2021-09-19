FOLDERS=qmk_firmware/keyboards/splitkb/kyria/keymaps/jat qmk_firmware/users/jat

setup: submodules
	mkdir $(FOLDERS)
	qmk setup -H ./qmk_firmware

submodules:
	git submodule update --init --recursive

update:
	git pull origin developement
	git submodule update --recursive
