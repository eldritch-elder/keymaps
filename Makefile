QMK_REPO=qmk_firmware/readme.md  # to check if submodule is setup or not
FOLDERS=qmk_firmware/keyboards/splitkb/kyria/keymaps/jat qmk_firmware/users/jat

setup: submodules
	mkdir $(FOLDERS)

submodules: $(QMK_REPO)
	git submodule update --init --recursive

update: submodules
	git pull
