# keymaps

This repo is my approach to code my keymaps using literate programming.
Before we can begin, you need the following:

- `git` duh
- Something capable for parsing `org` and the source blocks
  - `emacs` is recommended since I use elisp for scripting
- `qmk`

Afterwards, you need to add it to the qmk firmware

``` sh
qmk setup
cd ~/qmk_firmware
git submodule add https://git.sr.ht/~jat/keymaps keyboards/splitkb/kyria/jat --init
```

---
## License

Yea, legal stuff, I know, annoying, but required and without it, you aren't allowed to even use it.
Yea.

> Copyright 2021 Freja
>
> This program is free software: you can redistribute it and/or modify
> it under the terms of the GNU General Public License as published by
> the Free Software Foundation, either version 2 of the License, or
> (at your option) any later version.
>
> This program is distributed in the hope that it will be useful,
> but WITHOUT ANY WARRANTY; without even the implied warranty of
> MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
> GNU General Public License for more details.
>
> You should have received a copy of the GNU General Public License
> along with this program.  If not, see <http://www.gnu.org/licenses/>.

