
# Table of Contents

1.  [The keymap](#orgbbea0a5)
    1.  [The layout](#orga9ac10d)
        1.  [Base layer](#org86844d7)
        2.  [g\*ming layout](#org61b0ab4)
        3.  [lower layer](#org1ae2841)
        4.  [raise layer](#org15f5315)
        5.  [adjusting shit](#orgf1e83e1)
    2.  [combos](#org4ff362a)
    3.  [encoder](#orgf604857)
    4.  [one shot one kill](#orgd74dfa6)
        1.  [canceling oneshotkeys](#orgab08faf)
        2.  [ignoring keys](#org04b92cd)
2.  [Abandon all hope, ye who enter here](#org3357124)
    1.  [generators and parser](#org2e6aad8)
        1.  [keycodes](#org2c8c8c0)
        2.  [layers](#orgbd07a55)
        3.  [combos](#orga4caaaa)
        4.  [osm](#org6fae501)
    2.  [stuff](#orgc3fc6f1)
        1.  [header](#org09cdec4)
        2.  [matrix stuff](#org41eb2c1)
        3.  [combo stuff](#orgcddd337)
        4.  [fixing osm stuff](#org2b742f4)
    3.  [putting it all together](#orgdab8939)
        1.  [keymap.c](#org8e7dfca)
        2.  [config.h](#org7f8149c)
        3.  [rules.mk](#org20c553b)



<a id="orgbbea0a5"></a>

# The keymap


<a id="orga9ac10d"></a>

## The layout

I primarily type in German, English and Swedish so the keyboard should be cabable or outputing the used characters like `ü` or `å`.
For that I am using [EurKey](https://eurkey.steffen.bruentjen.eu/) - but US Intl should be fine too - on my system.  These are QWERTY layouts but they are able to output letters used in different languages using Alt Gr aka Right Alt.


<a id="org86844d7"></a>

### Base layer

On the keyboard however I will use a modified version of [hands down gold](https://sites.google.com/alanreiser.com/handsdown/home?authuser=0#h.rt23wndkh65l), until something better comes up.

<table id="org035675f" border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<tbody>
<tr>
<td class="org-left">xxx</td>
<td class="org-left">&amp;kp a</td>
<td class="org-left">&amp;kp f</td>
<td class="org-left">&amp;kp m</td>
<td class="org-left">&amp;kp p</td>
<td class="org-left">&amp;kp v</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&amp;kp semi</td>
<td class="org-left">&amp;kp dot</td>
<td class="org-left">&amp;kp fslh</td>
<td class="org-left">&amp;kp sqt</td>
<td class="org-left">&amp;kp equal</td>
<td class="org-left">xxx</td>
</tr>


<tr>
<td class="org-left">xxx</td>
<td class="org-left">&amp;kp r</td>
<td class="org-left">&amp;kp s</td>
<td class="org-left">&amp;kp n</td>
<td class="org-left">&amp;kp d</td>
<td class="org-left">&amp;kp w</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&amp;kp comma</td>
<td class="org-left">&amp;kp a</td>
<td class="org-left">&amp;kp e</td>
<td class="org-left">&amp;kp i</td>
<td class="org-left">&amp;kp o</td>
<td class="org-left">xxx</td>
</tr>


<tr>
<td class="org-left">xxx</td>
<td class="org-left">&amp;kp x</td>
<td class="org-left">&amp;kp g</td>
<td class="org-left">&amp;kp l</td>
<td class="org-left">&amp;kp c</td>
<td class="org-left">&amp;kp b</td>
<td class="org-left">&amp;mo _adj</td>
<td class="org-left">xxx</td>
<td class="org-left">xxx</td>
<td class="org-left">xxx</td>
<td class="org-left">&amp;kp minus</td>
<td class="org-left">&amp;kp h</td>
<td class="org-left">&amp;kp u</td>
<td class="org-left">&amp;kp y</td>
<td class="org-left">&amp;kp k</td>
<td class="org-left">xxx</td>
</tr>


<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&amp;kp lgui</td>
<td class="org-left">xxx</td>
<td class="org-left">&amp;mo _low</td>
<td class="org-left">&amp;kp t</td>
<td class="org-left">&amp;kp ret</td>
<td class="org-left">&amp;kp bspc</td>
<td class="org-left">&amp;kp space</td>
<td class="org-left">&amp;mo _high</td>
<td class="org-left">&amp;kp ralt</td>
<td class="org-left">&amp;kp mute</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>
</tbody>
</table>


<a id="org61b0ab4"></a>

### g\*ming layout

Too lazy to config shit in every game I use a keyboard with.

<table id="org3d51a10" border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<tbody>
<tr>
<td class="org-left">xxx</td>
<td class="org-left">&amp;kp a</td>
<td class="org-left">&amp;kp w</td>
<td class="org-left">&amp;kp e</td>
<td class="org-left">&amp;kp r</td>
<td class="org-left">&amp;kp t</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">xxx</td>
<td class="org-left">xxx</td>
<td class="org-left">&amp;kp n3</td>
<td class="org-left">&amp;kp n4</td>
<td class="org-left">xxx</td>
<td class="org-left">xxx</td>
</tr>


<tr>
<td class="org-left">xxx</td>
<td class="org-left">&amp;kp q</td>
<td class="org-left">&amp;kp s</td>
<td class="org-left">&amp;kp d</td>
<td class="org-left">&amp;kp f</td>
<td class="org-left">&amp;kp g</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&amp;kp n7</td>
<td class="org-left">&amp;kp n1</td>
<td class="org-left">&amp;kp n2</td>
<td class="org-left">&amp;kp n5</td>
<td class="org-left">&amp;kp n6</td>
<td class="org-left">xxx</td>
</tr>


<tr>
<td class="org-left">xxx</td>
<td class="org-left">&amp;kp z</td>
<td class="org-left">&amp;kp x</td>
<td class="org-left">&amp;kp c</td>
<td class="org-left">&amp;kp v</td>
<td class="org-left">&amp;kp b</td>
<td class="org-left">---</td>
<td class="org-left">&amp;kp gesc</td>
<td class="org-left">---</td>
<td class="org-left">---</td>
<td class="org-left">xxx</td>
<td class="org-left">xxx</td>
<td class="org-left">xxx</td>
<td class="org-left">xxx</td>
<td class="org-left">xxx</td>
<td class="org-left">xxx</td>
</tr>


<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&amp;kp lgui</td>
<td class="org-left">&amp;kp tab</td>
<td class="org-left">&amp;kp lalt</td>
<td class="org-left">&amp;kp space</td>
<td class="org-left">&amp;lt _low ret</td>
<td class="org-left">xxx</td>
<td class="org-left">xxx</td>
<td class="org-left">xxx</td>
<td class="org-left">xxx</td>
<td class="org-left">&amp;kp mute</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>
</tbody>
</table>


<a id="org1ae2841"></a>

### lower layer

<table id="orgc3a5944" border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<tbody>
<tr>
<td class="org-left">xxx</td>
<td class="org-left">&amp;kp n1</td>
<td class="org-left">&amp;kp n2</td>
<td class="org-left">&amp;kp n3</td>
<td class="org-left">&amp;kp n4</td>
<td class="org-left">&amp;kp n5</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&amp;kps n1</td>
<td class="org-left">&amp;kps n2</td>
<td class="org-left">&amp;kps n3</td>
<td class="org-left">&amp;kps n4</td>
<td class="org-left">&amp;kps n5</td>
<td class="org-left">xxx</td>
</tr>


<tr>
<td class="org-left">xxx</td>
<td class="org-left">&amp;kp n6</td>
<td class="org-left">&amp;kp n7</td>
<td class="org-left">&amp;kp n8</td>
<td class="org-left">&amp;kp n9</td>
<td class="org-left">&amp;kp n0</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&amp;kps n6</td>
<td class="org-left">&amp;kps n7</td>
<td class="org-left">&amp;kps n8</td>
<td class="org-left">&amp;kps n9</td>
<td class="org-left">&amp;kps n0</td>
<td class="org-left">xxx</td>
</tr>


<tr>
<td class="org-left">xxx</td>
<td class="org-left">---</td>
<td class="org-left">---</td>
<td class="org-left">&amp;kp lbrc</td>
<td class="org-left">&amp;kp rbrc</td>
<td class="org-left">---</td>
<td class="org-left">---</td>
<td class="org-left">---</td>
<td class="org-left">---</td>
<td class="org-left">---</td>
<td class="org-left">---</td>
<td class="org-left">&amp;kps lbrc</td>
<td class="org-left">&amp;kps rbrc</td>
<td class="org-left">&amp;kps bslh</td>
<td class="org-left">---</td>
<td class="org-left">xxx</td>
</tr>


<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">---</td>
<td class="org-left">---</td>
<td class="org-left">---</td>
<td class="org-left">---</td>
<td class="org-left">---</td>
<td class="org-left">---</td>
<td class="org-left">---</td>
<td class="org-left">---</td>
<td class="org-left">---</td>
<td class="org-left">---</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>
</tbody>
</table>


<a id="org15f5315"></a>

### raise layer

<table id="orgd80d624" border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<tbody>
<tr>
<td class="org-left">xxx</td>
<td class="org-left">&amp;kp print</td>
<td class="org-left">&amp;kp volu</td>
<td class="org-left">---</td>
<td class="org-left">---</td>
<td class="org-left">---</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">---</td>
<td class="org-left">---</td>
<td class="org-left">---</td>
<td class="org-left">---</td>
<td class="org-left">---</td>
<td class="org-left">xxx</td>
</tr>


<tr>
<td class="org-left">xxx</td>
<td class="org-left">---</td>
<td class="org-left">&amp;kp vold</td>
<td class="org-left">&amp;kp prev</td>
<td class="org-left">&amp;kp pause</td>
<td class="org-left">&amp;kp next</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&amp;kp left</td>
<td class="org-left">&amp;kp down</td>
<td class="org-left">&amp;kp up</td>
<td class="org-left">&amp;kp right</td>
<td class="org-left">---</td>
<td class="org-left">xxx</td>
</tr>


<tr>
<td class="org-left">xxx</td>
<td class="org-left">&amp;kp undo</td>
<td class="org-left">&amp;kp cut</td>
<td class="org-left">&amp;kp copy</td>
<td class="org-left">&amp;kp paste</td>
<td class="org-left">---</td>
<td class="org-left">---</td>
<td class="org-left">---</td>
<td class="org-left">---</td>
<td class="org-left">---</td>
<td class="org-left">---</td>
<td class="org-left">---</td>
<td class="org-left">---</td>
<td class="org-left">---</td>
<td class="org-left">---</td>
<td class="org-left">xxx</td>
</tr>


<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">---</td>
<td class="org-left">---</td>
<td class="org-left">---</td>
<td class="org-left">---</td>
<td class="org-left">---</td>
<td class="org-left">---</td>
<td class="org-left">---</td>
<td class="org-left">---</td>
<td class="org-left">---</td>
<td class="org-left">---</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>
</tbody>
</table>


<a id="orgf1e83e1"></a>

### adjusting shit

This layer contains stuff for adjusting, be it `EE_HANDS` or rgb stuff.

<table id="org748c133" border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<tbody>
<tr>
<td class="org-left">xxx</td>
<td class="org-left">&amp;kp eelh</td>
<td class="org-left">&amp;kp eerh</td>
<td class="org-left">xxx</td>
<td class="org-left">xxx</td>
<td class="org-left">xxx</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">xxx</td>
<td class="org-left">&amp;kp rgbhu</td>
<td class="org-left">&amp;kp rgbsu</td>
<td class="org-left">&amp;kp rgbvu</td>
<td class="org-left">&amp;kp rgbmu</td>
<td class="org-left">xxx</td>
</tr>


<tr>
<td class="org-left">xxx</td>
<td class="org-left">xxx</td>
<td class="org-left">xxx</td>
<td class="org-left">xxx</td>
<td class="org-left">xxx</td>
<td class="org-left">xxx</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">xxx</td>
<td class="org-left">&amp;kp rgbhd</td>
<td class="org-left">&amp;kp rgbsd</td>
<td class="org-left">&amp;kp rgbvd</td>
<td class="org-left">&amp;kp rgbmd</td>
<td class="org-left">xxx</td>
</tr>


<tr>
<td class="org-left">xxx</td>
<td class="org-left">&amp;kp reset</td>
<td class="org-left">&amp;kp eeprt</td>
<td class="org-left">xxx</td>
<td class="org-left">xxx</td>
<td class="org-left">xxx</td>
<td class="org-left">xxx</td>
<td class="org-left">xxx</td>
<td class="org-left">xxx</td>
<td class="org-left">&amp;tg _game</td>
<td class="org-left">xxx</td>
<td class="org-left">xxx</td>
<td class="org-left">xxx</td>
<td class="org-left">xxx</td>
<td class="org-left">xxx</td>
<td class="org-left">xxx</td>
</tr>


<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">xxx</td>
<td class="org-left">xxx</td>
<td class="org-left">xxx</td>
<td class="org-left">xxx</td>
<td class="org-left">xxx</td>
<td class="org-left">xxx</td>
<td class="org-left">xxx</td>
<td class="org-left">xxx</td>
<td class="org-left">xxx</td>
<td class="org-left">xxx</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>
</tbody>
</table>


<a id="org4ff362a"></a>

## combos

Here, combos are a nice feature allowing to add keys at places where they don&rsquo;t impare your typing yet are comfortable to use.
It expects a table with each row taking one combo, the first cell is the result you want to have and all the following cells contain the keys you want to press to, to the key in the first cell.
Leave an empty table to disable this feature.  Leaving the first cell empty will do the trick too.

<table id="org8045717" border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<tbody>
<tr>
<td class="org-left">&amp;osm lsft</td>
<td class="org-left">&amp;kp f</td>
<td class="org-left">&amp;kp m</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">&amp;osm lctl</td>
<td class="org-left">&amp;kp g</td>
<td class="org-left">&amp;kp l</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">&amp;osm lgui</td>
<td class="org-left">&amp;kp fslh</td>
<td class="org-left">&amp;kp sqt</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">&amp;osm lalt</td>
<td class="org-left">&amp;kp u</td>
<td class="org-left">&amp;kp y</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">&amp;kp q</td>
<td class="org-left">&amp;kp z</td>
<td class="org-left">&amp;kp f</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">&amp;kp j</td>
<td class="org-left">&amp;kp m</td>
<td class="org-left">&amp;kp p</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">&amp;kp tab</td>
<td class="org-left">&amp;kp x</td>
<td class="org-left">&amp;kp c</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">&amp;kp esc</td>
<td class="org-left">&amp;kp z</td>
<td class="org-left">&amp;kp p</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">&amp;kp bspc</td>
<td class="org-left">&amp;kp minus</td>
<td class="org-left">&amp;kp h</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">&amp;kps n9</td>
<td class="org-left">&amp;kp f</td>
<td class="org-left">&amp;kp d</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">&amp;kps n0</td>
<td class="org-left">&amp;kp a</td>
<td class="org-left">&amp;kp sqt</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">&amp;kp lbrc</td>
<td class="org-left">&amp;kp f</td>
<td class="org-left">&amp;kp p</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">&amp;kp rbrc</td>
<td class="org-left">&amp;kp dot</td>
<td class="org-left">&amp;kp sqt</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">&amp;kps lbrc</td>
<td class="org-left">&amp;kp f</td>
<td class="org-left">&amp;kp n</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">&amp;kps rbrc</td>
<td class="org-left">&amp;kp e</td>
<td class="org-left">&amp;kp sqt</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">&amp;kp grave</td>
<td class="org-left">&amp;kp sqt</td>
<td class="org-left">&amp;kp equal</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">&amp;kps n1</td>
<td class="org-left">&amp;kp f</td>
<td class="org-left">&amp;kp m</td>
<td class="org-left">&amp;kp e</td>
<td class="org-left">&amp;kp i</td>
</tr>


<tr>
<td class="org-left">&amp;kps fslh</td>
<td class="org-left">&amp;kp s</td>
<td class="org-left">&amp;kp n</td>
<td class="org-left">&amp;kp fslh</td>
<td class="org-left">&amp;kp sqt</td>
</tr>


<tr>
<td class="org-left">&amp;kpag a</td>
<td class="org-left">&amp;kp g</td>
<td class="org-left">&amp;kp c</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">&amp;kpag w</td>
<td class="org-left">&amp;kp dot</td>
<td class="org-left">&amp;kp o</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">&amp;kpag o</td>
<td class="org-left">&amp;kp a</td>
<td class="org-left">&amp;kp o</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">&amp;kpag u</td>
<td class="org-left">&amp;kp h</td>
<td class="org-left">&amp;kp y</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>
</tbody>
</table>


<a id="orgf604857"></a>

## encoder

Rotary encoders add a lot of features and functionality, they are extremly useful.
For me, I like to have volume control on one side and window control on the other.

Simple structure is the function `encoder_update_user(index, clockwise)`, this runs a simple *this encoder does this when turned clockwise, this then otherwise*.

    bool is_alt_tab = false;
    uint16_t alt_tab_timer = 0;
    
    bool encoder_update_user(uint8_t index, bool clockwise) {
        if (index == 1) {
            if (clockwise) {
                tap_code(KC_VOLU);
            } else {
                tap_code(KC_VOLD);
            }
        } else if (index == 0) {
            if (clockwise) {
                if (!is_alt_tab) {
                    is_alt_tab = true;
                    register_code(KC_LALT);
                }
                alt_tab_timer = timer_read();
                tap_code16(KC_TAB);
            } else {
                if (!is_alt_tab) {
                    is_alt_tab = true;
                    register_code(KC_LALT);
                }
                alt_tab_timer = timer_read();
                tap_code16(S(KC_TAB));
            }
        }
    
        return false;
    }
    
    void matrix_scan_user(void) {
        if (is_alt_tab) {
            if (timer_elapsed(alt_tab_timer) > 800) {
                unregister_code(KC_LALT);
                is_alt_tab = false;
            }
        }
    }


<a id="orgd74dfa6"></a>

## one shot one kill

I use callums implementation for oneshot mods.  For more information check callums userspace and the joinked stuff down in [the building section](#org2b742f4).
I&rsquo;m gonna take over the `OSM()` keycodes since this is basically osm except better.


<a id="orgab08faf"></a>

### canceling oneshotkeys

Since they don&rsquo;t use a timer and queue up indefinetly you need some way to cancel the keys when you missclicked or something.

<table id="org759caf7" border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />
</colgroup>
<tbody>
<tr>
<td class="org-left">&amp;mo _high</td>
</tr>
</tbody>
</table>


<a id="org04b92cd"></a>

### ignoring keys

Sometimes you don&rsquo;t want to activate the mods on some keys, e.g. to stack mods or use them across layers.

<table id="org686071b" border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />
</colgroup>
<tbody>
<tr>
<td class="org-left">&amp;osm lsft</td>
</tr>


<tr>
<td class="org-left">&amp;osm rsft</td>
</tr>


<tr>
<td class="org-left">&amp;osm lctl</td>
</tr>


<tr>
<td class="org-left">&amp;osm rctl</td>
</tr>


<tr>
<td class="org-left">&amp;osm lalt</td>
</tr>


<tr>
<td class="org-left">&amp;osm ralt</td>
</tr>


<tr>
<td class="org-left">&amp;osm lgui</td>
</tr>


<tr>
<td class="org-left">&amp;osm rgui</td>
</tr>


<tr>
<td class="org-left">&amp;mo _low</td>
</tr>
</tbody>
</table>


<a id="org3357124"></a>

# Abandon all hope, ye who enter here

This section is the build section. from this point on it&rsquo;s code and code only, be it elisp or c.
I would not recommend altering anything down there, escpecially the generator code, unless you know what you are doing.

I try to write it fairly pessimistic, but if anything faulty goes through, qmk will complain about it.


<a id="org2e6aad8"></a>

## generators and parser

This section contains stuff used for parsing the key definitions.


<a id="org2c8c8c0"></a>

### keycodes

    (defun get-keycode (name)
      "Returns the keycode if it exists."
      (let ((code (nth 1 (assoc name keycode))))
        (if (not code)
            (error "The key %s does't exist - yet." name)
            code)))
    
    (defun get-mod (name)
      "Returns the mod if it exists."
      (let ((code (nth 1 (assoc name modcode))))
        (if (not code)
            (error "The mod %s does't exist." name)
            code)))
    
    (defun parse-key (word)
      "Parses the expression and returns the keycode.  It takes a string as input and ignores empty expressions"
      (unless (eq word "")
        (pcase word
          ((or "&nop" "xxx")                                                                          "KC_NO, ")
          ((or "&trns" "___" "---")                                                                   "KC_TRNS, ")
          ;; FIXME the `rx` shit does not work when tangling with a script/in batch mode
          ((rx bos "&kp" (+ space) (let head (+ word)) (* space) eos)                                 (concat (get-keycode head) ", "))
          ((rx bos "&kps" (+ space) (let head (+ word)) (* space) eos)                                (format "S(%s), " (get-keycode head)))
          ((rx bos "&kpc" (+ space) (let head (+ word)) (* space) eos)                                (format "C(%s), " (get-keycode head)))
          ((rx bos "&kpa" (+ space) (let head (+ word)) (* space) eos)                                (format "A(%s), " (get-keycode head)))
          ((rx bos "&kpag" (+ space) (let head (+ word)) (* space) eos)                               (format "RALT(%s), " (get-keycode head)))
          ((rx bos "&kpg" (+ space) (let head (+ word)) (* space) eos)                                (format "G(%s), " (get-keycode head)))
          ((rx bos "&tg" (+ space) (let head (+ word)) (* space) eos)                                 (format "TG(%s), " head))
          ((rx bos "&lt" (+ space) (let arg (+ word)) (+ space) (let head (+ word)) (* space) eos)    (format "LT(%s, %s), " arg (get-keycode head)))
          ((rx bos "&mo" (+ space) (let head (+ word)) (* space) eos)                                 (format "MO(%s), " head))
          ((rx bos "&mt" (+ space) (let arg (+ word)) (+ space) (let head (+ word)) (* space) eos)    (format "MT(%s, %s), " (get-mod arg) (get-keycode head)))
          ((rx bos "&osm" (+ space) (let head (+ word)) (* space) eos)                                (format "OSM(%s), " (get-mod head)))
          (-                                                                                          (error "unknown expr `%s`" word)))))

1.  tables n shit

    A not so complete list of keycodes
    
    <table id="org94bbb9f" border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">
    
    
    <colgroup>
    <col  class="org-left" />
    
    <col  class="org-left" />
    </colgroup>
    <tbody>
    <tr>
    <td class="org-left">a</td>
    <td class="org-left">KC<sub>A</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">b</td>
    <td class="org-left">KC<sub>B</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">c</td>
    <td class="org-left">KC<sub>C</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">d</td>
    <td class="org-left">KC<sub>D</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">e</td>
    <td class="org-left">KC<sub>E</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">f</td>
    <td class="org-left">KC<sub>F</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">g</td>
    <td class="org-left">KC<sub>G</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">h</td>
    <td class="org-left">KC<sub>H</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">i</td>
    <td class="org-left">KC<sub>I</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">j</td>
    <td class="org-left">KC<sub>J</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">k</td>
    <td class="org-left">KC<sub>K</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">l</td>
    <td class="org-left">KC<sub>L</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">m</td>
    <td class="org-left">KC<sub>M</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">n</td>
    <td class="org-left">KC<sub>N</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">o</td>
    <td class="org-left">KC<sub>O</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">p</td>
    <td class="org-left">KC<sub>P</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">q</td>
    <td class="org-left">KC<sub>Q</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">r</td>
    <td class="org-left">KC<sub>R</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">s</td>
    <td class="org-left">KC<sub>S</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">t</td>
    <td class="org-left">KC<sub>T</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">u</td>
    <td class="org-left">KC<sub>U</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">v</td>
    <td class="org-left">KC<sub>V</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">w</td>
    <td class="org-left">KC<sub>W</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">x</td>
    <td class="org-left">KC<sub>X</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">y</td>
    <td class="org-left">KC<sub>Y</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">z</td>
    <td class="org-left">KC<sub>Z</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">n1</td>
    <td class="org-left">KC<sub>1</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">n2</td>
    <td class="org-left">KC<sub>2</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">n3</td>
    <td class="org-left">KC<sub>3</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">n4</td>
    <td class="org-left">KC<sub>4</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">n5</td>
    <td class="org-left">KC<sub>5</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">n6</td>
    <td class="org-left">KC<sub>6</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">n7</td>
    <td class="org-left">KC<sub>7</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">n8</td>
    <td class="org-left">KC<sub>8</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">n9</td>
    <td class="org-left">KC<sub>9</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">n0</td>
    <td class="org-left">KC<sub>0</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">ret</td>
    <td class="org-left">KC<sub>ENTER</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">esc</td>
    <td class="org-left">KC<sub>ESC</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">gesc</td>
    <td class="org-left">KC<sub>GESC</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">bspc</td>
    <td class="org-left">KC<sub>BSPACE</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">del</td>
    <td class="org-left">KC<sub>DEL</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">tab</td>
    <td class="org-left">KC<sub>TAB</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">space</td>
    <td class="org-left">KC<sub>SPACE</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">minus</td>
    <td class="org-left">KC<sub>MINUS</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">equal</td>
    <td class="org-left">KC<sub>EQUAL</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">lbrc</td>
    <td class="org-left">KC<sub>LBRC</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">rbrc</td>
    <td class="org-left">KC<sub>RBRC</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">fslh</td>
    <td class="org-left">KC<sub>SLASH</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">bslh</td>
    <td class="org-left">KC<sub>BSLASH</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">semi</td>
    <td class="org-left">KC<sub>SCOLON</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">dot</td>
    <td class="org-left">KC<sub>DOT</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">comma</td>
    <td class="org-left">KC<sub>COMMA</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">sqt</td>
    <td class="org-left">KC<sub>QUOTE</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">grave</td>
    <td class="org-left">KC<sub>GRAVE</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">lsft</td>
    <td class="org-left">KC<sub>LSHIFT</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">rsft</td>
    <td class="org-left">KC<sub>RSHIFT</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">lctl</td>
    <td class="org-left">KC<sub>LCTRL</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">rctl</td>
    <td class="org-left">KC<sub>RCTRL</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">lalt</td>
    <td class="org-left">KC<sub>LALT</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">ralt</td>
    <td class="org-left">KC<sub>RALT</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">lgui</td>
    <td class="org-left">KC<sub>LGUI</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">rgui</td>
    <td class="org-left">KC<sub>RGUI</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">mute</td>
    <td class="org-left">KC<sub>MUTE</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">left</td>
    <td class="org-left">KC<sub>LEFT</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">down</td>
    <td class="org-left">KC<sub>DOWN</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">up</td>
    <td class="org-left">KC<sub>UP</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">right</td>
    <td class="org-left">KC<sub>RIGHT</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">volu</td>
    <td class="org-left">KC<sub>VOLU</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">vold</td>
    <td class="org-left">KC<sub>VOLD</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">pause</td>
    <td class="org-left">KC<sub>MPLY</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">next</td>
    <td class="org-left">KC<sub>MNXT</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">prev</td>
    <td class="org-left">KC<sub>MPRV</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">undo</td>
    <td class="org-left">KC<sub>UNDO</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">cut</td>
    <td class="org-left">KC<sub>CUT</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">copy</td>
    <td class="org-left">KC<sub>COPY</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">print</td>
    <td class="org-left">KC<sub>PSCR</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">paste</td>
    <td class="org-left">KC<sub>PASTE</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">eelh</td>
    <td class="org-left">EH<sub>LEFT</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">eerh</td>
    <td class="org-left">EH<sub>RGHT</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">rgbhu</td>
    <td class="org-left">RGB<sub>HUI</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">rgbhd</td>
    <td class="org-left">RGB<sub>HUD</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">rgbsu</td>
    <td class="org-left">RGB<sub>SAI</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">rgbsd</td>
    <td class="org-left">RGB<sub>SAD</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">rgbvu</td>
    <td class="org-left">RGB<sub>VAI</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">rgbvd</td>
    <td class="org-left">RGB<sub>VAD</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">rgbmu</td>
    <td class="org-left">RGB<sub>MOD</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">rgbmd</td>
    <td class="org-left">RGB<sub>RMOD</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">reset</td>
    <td class="org-left">RESET</td>
    </tr>
    
    
    <tr>
    <td class="org-left">eeprt</td>
    <td class="org-left">EEP<sub>RST</sub></td>
    </tr>
    </tbody>
    </table>
    
    A semi complete list of modifier codes
    
    <table id="org44ee8c8" border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">
    
    
    <colgroup>
    <col  class="org-left" />
    
    <col  class="org-left" />
    </colgroup>
    <tbody>
    <tr>
    <td class="org-left">lsft</td>
    <td class="org-left">MOD<sub>LSFT</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">rsft</td>
    <td class="org-left">MOD<sub>RSFT</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">lctl</td>
    <td class="org-left">MOD<sub>LCTL</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">rctl</td>
    <td class="org-left">MOD<sub>RCTL</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">lalt</td>
    <td class="org-left">MOD<sub>LALT</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">ralt</td>
    <td class="org-left">MOD<sub>RALT</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">lgui</td>
    <td class="org-left">MOD<sub>LGUI</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">rgui</td>
    <td class="org-left">MOD<sub>RGUI</sub></td>
    </tr>
    </tbody>
    </table>


<a id="orgbd07a55"></a>

### layers

For processing the table and generating the layers

    (defun get-keycode (name)
      "Returns the keycode if it exists."
      (let ((code (nth 1 (assoc name keycode))))
        (if (not code)
            (error "The key %s does't exist - yet." name)
            code)))
    
    (defun get-mod (name)
      "Returns the mod if it exists."
      (let ((code (nth 1 (assoc name modcode))))
        (if (not code)
            (error "The mod %s does't exist." name)
            code)))
    
    (defun parse-key (word)
      "Parses the expression and returns the keycode.  It takes a string as input and ignores empty expressions"
      (unless (eq word "")
        (pcase word
          ((or "&nop" "xxx")                                                                          "KC_NO, ")
          ((or "&trns" "___" "---")                                                                   "KC_TRNS, ")
          ;; FIXME the `rx` shit does not work when tangling with a script/in batch mode
          ((rx bos "&kp" (+ space) (let head (+ word)) (* space) eos)                                 (concat (get-keycode head) ", "))
          ((rx bos "&kps" (+ space) (let head (+ word)) (* space) eos)                                (format "S(%s), " (get-keycode head)))
          ((rx bos "&kpc" (+ space) (let head (+ word)) (* space) eos)                                (format "C(%s), " (get-keycode head)))
          ((rx bos "&kpa" (+ space) (let head (+ word)) (* space) eos)                                (format "A(%s), " (get-keycode head)))
          ((rx bos "&kpag" (+ space) (let head (+ word)) (* space) eos)                               (format "RALT(%s), " (get-keycode head)))
          ((rx bos "&kpg" (+ space) (let head (+ word)) (* space) eos)                                (format "G(%s), " (get-keycode head)))
          ((rx bos "&tg" (+ space) (let head (+ word)) (* space) eos)                                 (format "TG(%s), " head))
          ((rx bos "&lt" (+ space) (let arg (+ word)) (+ space) (let head (+ word)) (* space) eos)    (format "LT(%s, %s), " arg (get-keycode head)))
          ((rx bos "&mo" (+ space) (let head (+ word)) (* space) eos)                                 (format "MO(%s), " head))
          ((rx bos "&mt" (+ space) (let arg (+ word)) (+ space) (let head (+ word)) (* space) eos)    (format "MT(%s, %s), " (get-mod arg) (get-keycode head)))
          ((rx bos "&osm" (+ space) (let head (+ word)) (* space) eos)                                (format "OSM(%s), " (get-mod head)))
          (-                                                                                          (error "unknown expr `%s`" word)))))
    
    (setq input (flatten-tree input) ; flat is justice
          result "")
    
    (while input
      (let ((word (pop input)))
        (setq result (concat result (parse-key word)))))
    
    (s-chop-suffix ", " result)  ; <- doesn't work outside emacs


<a id="orga4caaaa"></a>

### combos

Parsing and generating the code for the combos

    (if (equal (caar in) "")
        "no" "yes")

    (length in)

    (defun get-keycode (name)
      "Returns the keycode if it exists."
      (let ((code (nth 1 (assoc name keycode))))
        (if (not code)
            (error "The key %s does't exist - yet." name)
            code)))
    
    (defun get-mod (name)
      "Returns the mod if it exists."
      (let ((code (nth 1 (assoc name modcode))))
        (if (not code)
            (error "The mod %s does't exist." name)
            code)))
    
    (defun parse-key (word)
      "Parses the expression and returns the keycode.  It takes a string as input and ignores empty expressions"
      (unless (eq word "")
        (pcase word
          ((or "&nop" "xxx")                                                                          "KC_NO, ")
          ((or "&trns" "___" "---")                                                                   "KC_TRNS, ")
          ;; FIXME the `rx` shit does not work when tangling with a script/in batch mode
          ((rx bos "&kp" (+ space) (let head (+ word)) (* space) eos)                                 (concat (get-keycode head) ", "))
          ((rx bos "&kps" (+ space) (let head (+ word)) (* space) eos)                                (format "S(%s), " (get-keycode head)))
          ((rx bos "&kpc" (+ space) (let head (+ word)) (* space) eos)                                (format "C(%s), " (get-keycode head)))
          ((rx bos "&kpa" (+ space) (let head (+ word)) (* space) eos)                                (format "A(%s), " (get-keycode head)))
          ((rx bos "&kpag" (+ space) (let head (+ word)) (* space) eos)                               (format "RALT(%s), " (get-keycode head)))
          ((rx bos "&kpg" (+ space) (let head (+ word)) (* space) eos)                                (format "G(%s), " (get-keycode head)))
          ((rx bos "&tg" (+ space) (let head (+ word)) (* space) eos)                                 (format "TG(%s), " head))
          ((rx bos "&lt" (+ space) (let arg (+ word)) (+ space) (let head (+ word)) (* space) eos)    (format "LT(%s, %s), " arg (get-keycode head)))
          ((rx bos "&mo" (+ space) (let head (+ word)) (* space) eos)                                 (format "MO(%s), " head))
          ((rx bos "&mt" (+ space) (let arg (+ word)) (+ space) (let head (+ word)) (* space) eos)    (format "MT(%s, %s), " (get-mod arg) (get-keycode head)))
          ((rx bos "&osm" (+ space) (let head (+ word)) (* space) eos)                                (format "OSM(%s), " (get-mod head)))
          (-                                                                                          (error "unknown expr `%s`" word)))))
    
    (setq result ""
          id 0)  ; too lazy to create names, I just use a running number
    
    (unless (eq (caar in) "")
      (while in
        (setq row (cdr (pop in))
              result (concat result (format "const uint16_t PROGMEM unique_combo%d[] = { " id)))
        (while row
          (setq result (concat result (parse-key (pop row)))))
        (setq result (concat result "COMBO_END, };\n")
              id (1+ id)))
    
        (print result))

    (defun get-keycode (name)
      "Returns the keycode if it exists."
      (let ((code (nth 1 (assoc name keycode))))
        (if (not code)
            (error "The key %s does't exist - yet." name)
            code)))
    
    (defun get-mod (name)
      "Returns the mod if it exists."
      (let ((code (nth 1 (assoc name modcode))))
        (if (not code)
            (error "The mod %s does't exist." name)
            code)))
    
    (defun parse-key (word)
      "Parses the expression and returns the keycode.  It takes a string as input and ignores empty expressions"
      (unless (eq word "")
        (pcase word
          ((or "&nop" "xxx")                                                                          "KC_NO, ")
          ((or "&trns" "___" "---")                                                                   "KC_TRNS, ")
          ;; FIXME the `rx` shit does not work when tangling with a script/in batch mode
          ((rx bos "&kp" (+ space) (let head (+ word)) (* space) eos)                                 (concat (get-keycode head) ", "))
          ((rx bos "&kps" (+ space) (let head (+ word)) (* space) eos)                                (format "S(%s), " (get-keycode head)))
          ((rx bos "&kpc" (+ space) (let head (+ word)) (* space) eos)                                (format "C(%s), " (get-keycode head)))
          ((rx bos "&kpa" (+ space) (let head (+ word)) (* space) eos)                                (format "A(%s), " (get-keycode head)))
          ((rx bos "&kpag" (+ space) (let head (+ word)) (* space) eos)                               (format "RALT(%s), " (get-keycode head)))
          ((rx bos "&kpg" (+ space) (let head (+ word)) (* space) eos)                                (format "G(%s), " (get-keycode head)))
          ((rx bos "&tg" (+ space) (let head (+ word)) (* space) eos)                                 (format "TG(%s), " head))
          ((rx bos "&lt" (+ space) (let arg (+ word)) (+ space) (let head (+ word)) (* space) eos)    (format "LT(%s, %s), " arg (get-keycode head)))
          ((rx bos "&mo" (+ space) (let head (+ word)) (* space) eos)                                 (format "MO(%s), " head))
          ((rx bos "&mt" (+ space) (let arg (+ word)) (+ space) (let head (+ word)) (* space) eos)    (format "MT(%s, %s), " (get-mod arg) (get-keycode head)))
          ((rx bos "&osm" (+ space) (let head (+ word)) (* space) eos)                                (format "OSM(%s), " (get-mod head)))
          (-                                                                                          (error "unknown expr `%s`" word)))))
    
    (setq result "combo_t key_combos[COMBO_COUNT] = { "
          id 0)
    
    (unless (eq (caar in) "")
      (while in
        (setq key (car (pop in))
              result (concat result (format "COMBO(unique_combo%d, %s), " id (s-chop-suffix ", " (parse-key key))))
              id (1+ id)))
      (concat result "};"))


<a id="org6fae501"></a>

### osm

    
    
    (setq result "bool is_oneshot_cancel_key(uint16_t keycode) {\n  switch (keycode) {\n")
    
    (while in
      (unless (eq (parse-key (caar in)) "")
        (setq result (concat result "    case " (s-chop-suffix ", " (parse-key (car (pop in)))) ":\n"))))
    
    (concat result "      return true;\n    default:\n      return false;\n  }\n}")

    
    
    (setq result "bool is_oneshot_ignored_key(uint16_t keycode) {\n  switch (keycode) {\n")
    
    (while in
      (unless (eq (parse-key (caar in)) "")
        (setq result (concat result "    case " (s-chop-suffix ", " (parse-key (car (pop in)))) ":\n"))))
    
    (concat result "      return true;\n    default:\n      return false;\n  }\n}")


<a id="orgc3fc6f1"></a>

## stuff

Here we take everything from the section before and format these accordingly before taking everything together.


<a id="org09cdec4"></a>

### header

    /* vim:ro
     * -*- buffer-read-only: t -*-
     *
     * This is autogenerated using babel DO NOT EDIT.
     * Please refer to main.org in [[https://git.sr.ht/~jat/keymap]]
     *
     *
     * Copyright 2021 Freja
     *
     * This program is free software: you can redistribute it and/or modify
     * it under the terms of the GNU General Public License as published by
     * the Free Software Foundation, either version 2 of the License, or
     * (at your option) any later version.
     *
     * This program is distributed in the hope that it will be useful,
     * but WITHOUT ANY WARRANTY; without even the implied warranty of
     * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
     * GNU General Public License for more details.
     *
     * You should have received a copy of the GNU General Public License
     * along with this program.  If not, see <http://www.gnu.org/licenses/>.
     */


<a id="org41eb2c1"></a>

### matrix stuff

    enum layers { _base = 0, _game, _low, _high, _adj, };
    
    const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
             [_base] = LAYOUT(KC_NO, KC_A, KC_F, KC_M, KC_P, KC_V, KC_SCOLON, KC_DOT, KC_SLASH, KC_QUOTE, KC_EQUAL, KC_NO, KC_NO, KC_R, KC_S, KC_N, KC_D, KC_W, KC_COMMA, KC_A, KC_E, KC_I, KC_O, KC_NO, KC_NO, KC_X, KC_G, KC_L, KC_C, KC_B, MO(_adj), KC_NO, KC_NO, KC_NO, KC_MINUS, KC_H, KC_U, KC_Y, KC_K, KC_NO, KC_LGUI, KC_NO, MO(_low), KC_T, KC_ENTER, KC_BSPACE, KC_SPACE, MO(_high), KC_RALT, KC_MUTE),
             [_game] = LAYOUT(KC_NO, KC_A, KC_W, KC_E, KC_R, KC_T, KC_NO, KC_NO, KC_3, KC_4, KC_NO, KC_NO, KC_NO, KC_Q, KC_S, KC_D, KC_F, KC_G, KC_7, KC_1, KC_2, KC_5, KC_6, KC_NO, KC_NO, KC_Z, KC_X, KC_C, KC_V, KC_B, KC_TRNS, KC_GESC, KC_TRNS, KC_TRNS, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_LGUI, KC_TAB, KC_LALT, KC_SPACE, LT(_low, KC_ENTER), KC_NO, KC_NO, KC_NO, KC_NO, KC_MUTE),
             [_low] = LAYOUT(KC_NO, KC_1, KC_2, KC_3, KC_4, KC_5, S(KC_1), S(KC_2), S(KC_3), S(KC_4), S(KC_5), KC_NO, KC_NO, KC_6, KC_7, KC_8, KC_9, KC_0, S(KC_6), S(KC_7), S(KC_8), S(KC_9), S(KC_0), KC_NO, KC_NO, KC_TRNS, KC_TRNS, KC_LBRC, KC_RBRC, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, S(KC_LBRC), S(KC_RBRC), S(KC_BSLASH), KC_TRNS, KC_NO, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS),
             [_high] = LAYOUT(KC_NO, KC_PSCR, KC_VOLU, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_NO, KC_NO, KC_TRNS, KC_VOLD, KC_MPRV, KC_MPLY, KC_MNXT, KC_LEFT, KC_DOWN, KC_UP, KC_RIGHT, KC_TRNS, KC_NO, KC_NO, KC_UNDO, KC_CUT, KC_COPY, KC_PASTE, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_NO, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS),
             [_adj] = LAYOUT(KC_NO, EH_LEFT, EH_RGHT, KC_NO, KC_NO, KC_NO, KC_NO, RGB_HUI, RGB_SAI, RGB_VAI, RGB_MOD, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, RGB_HUD, RGB_SAD, RGB_VAD, RGB_RMOD, KC_NO, KC_NO, RESET, EEP_RST, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, TG(_game), KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO),
    };


<a id="orgcddd337"></a>

### combo stuff

    const uint16_t PROGMEM unique_combo0[] = { KC_F, KC_M, COMBO_END, };
    const uint16_t PROGMEM unique_combo1[] = { KC_G, KC_L, COMBO_END, };
    const uint16_t PROGMEM unique_combo2[] = { KC_SLASH, KC_QUOTE, COMBO_END, };
    const uint16_t PROGMEM unique_combo3[] = { KC_U, KC_Y, COMBO_END, };
    const uint16_t PROGMEM unique_combo4[] = { KC_Z, KC_F, COMBO_END, };
    const uint16_t PROGMEM unique_combo5[] = { KC_M, KC_P, COMBO_END, };
    const uint16_t PROGMEM unique_combo6[] = { KC_X, KC_C, COMBO_END, };
    const uint16_t PROGMEM unique_combo7[] = { KC_Z, KC_P, COMBO_END, };
    const uint16_t PROGMEM unique_combo8[] = { KC_MINUS, KC_H, COMBO_END, };
    const uint16_t PROGMEM unique_combo9[] = { KC_F, KC_D, COMBO_END, };
    const uint16_t PROGMEM unique_combo10[] = { KC_A, KC_QUOTE, COMBO_END, };
    const uint16_t PROGMEM unique_combo11[] = { KC_F, KC_P, COMBO_END, };
    const uint16_t PROGMEM unique_combo12[] = { KC_DOT, KC_QUOTE, COMBO_END, };
    const uint16_t PROGMEM unique_combo13[] = { KC_F, KC_N, COMBO_END, };
    const uint16_t PROGMEM unique_combo14[] = { KC_E, KC_QUOTE, COMBO_END, };
    const uint16_t PROGMEM unique_combo15[] = { KC_QUOTE, KC_EQUAL, COMBO_END, };
    const uint16_t PROGMEM unique_combo16[] = { KC_F, KC_M, KC_E, KC_I, COMBO_END, };
    const uint16_t PROGMEM unique_combo17[] = { KC_S, KC_N, KC_SLASH, KC_QUOTE, COMBO_END, };
    const uint16_t PROGMEM unique_combo18[] = { KC_G, KC_C, COMBO_END, };
    const uint16_t PROGMEM unique_combo19[] = { KC_DOT, KC_O, COMBO_END, };
    const uint16_t PROGMEM unique_combo20[] = { KC_A, KC_O, COMBO_END, };
    const uint16_t PROGMEM unique_combo21[] = { KC_H, KC_Y, COMBO_END, };
    
    combo_t key_combos[COMBO_COUNT] = { COMBO(unique_combo0, OSM(MOD_LSFT)), COMBO(unique_combo1, OSM(MOD_LCTL)), COMBO(unique_combo2, OSM(MOD_LGUI)), COMBO(unique_combo3, OSM(MOD_LALT)), COMBO(unique_combo4, KC_Q), COMBO(unique_combo5, KC_J), COMBO(unique_combo6, KC_TAB), COMBO(unique_combo7, KC_ESC), COMBO(unique_combo8, KC_BSPACE), COMBO(unique_combo9, S(KC_9)), COMBO(unique_combo10, S(KC_0)), COMBO(unique_combo11, KC_LBRC), COMBO(unique_combo12, KC_RBRC), COMBO(unique_combo13, S(KC_LBRC)), COMBO(unique_combo14, S(KC_RBRC)), COMBO(unique_combo15, KC_GRAVE), COMBO(unique_combo16, S(KC_1)), COMBO(unique_combo17, S(KC_SLASH)), COMBO(unique_combo18, RALT(KC_A)), COMBO(unique_combo19, RALT(KC_W)), COMBO(unique_combo20, RALT(KC_O)), COMBO(unique_combo21, RALT(KC_U)), };


<a id="org2b742f4"></a>

### fixing osm stuff

    bool is_oneshot_cancel_key(uint16_t keycode) {
      switch (keycode) {
        case MO(_high):
          return true;
        default:
          return false;
      }
    };
    
    bool is_oneshot_ignored_key(uint16_t keycode) {
      switch (keycode) {
        case OSM(MOD_LSFT):
        case OSM(MOD_RSFT):
        case OSM(MOD_LCTL):
        case OSM(MOD_RCTL):
        case OSM(MOD_LALT):
        case OSM(MOD_RALT):
        case OSM(MOD_LGUI):
        case OSM(MOD_RGUI):
        case MO(_low):
          return true;
        default:
          return false;
      }
    };
    
    // the different states a oneshot key can be in
    typedef enum {
        os_up_unqueued,
        os_up_queued,
        os_down_unused,
        os_down_used,
    } oneshot_state;
    
    void update_oneshot(oneshot_state *state, uint16_t mod, uint16_t trigger, uint16_t keycode, keyrecord_t *record) {
        if (keycode == trigger) {
            if (record->event.pressed) {
                // Trigger keydown
                if (*state == os_up_unqueued) {
                    register_code(mod);
                }
                *state = os_down_unused;
            } else {
                // Trigger keyup
                switch (*state) {
                    case os_down_unused:
                        // If we didn't use the mod while trigger was held, queue it.
                        *state = os_up_queued;
                        break;
                    case os_down_used:
                        // If we did use the mod while trigger was held, unregister it.
                        *state = os_up_unqueued;
                        unregister_code(mod);
                        break;
                    default:
                        break;
                }
            }
        } else {
            if (record->event.pressed) {
                if (is_oneshot_cancel_key(keycode) && *state != os_up_unqueued) {
                    // Cancel oneshot on designated cancel keydown.
                    *state = os_up_unqueued;
                    unregister_code(mod);
                }
            } else {
                if (!is_oneshot_ignored_key(keycode)) {
                    // On non-ignored keyup, consider the oneshot used.
                    switch (*state) {
                        case os_down_unused:
                            *state = os_down_used;
                            break;
                        case os_up_queued:
                            *state = os_up_unqueued;
                            unregister_code(mod);
                            break;
                        default:
                            break;
                    }
                }
            }
        }
    };
    
    oneshot_state sft_state = os_up_unqueued;
    oneshot_state ctl_state = os_up_unqueued;
    oneshot_state alt_state = os_up_unqueued;
    oneshot_state gui_state = os_up_unqueued;

    update_oneshot(&sft_state, KC_LSHIFT, OSM(MOD_LSFT), keycode, record);
    update_oneshot(&ctl_state, KC_LCTRL, OSM(MOD_LCTL), keycode, record);
    update_oneshot(&alt_state, KC_LALT, OSM(MOD_LALT), keycode, record);
    update_oneshot(&gui_state, KC_LGUI, OSM(MOD_LGUI), keycode, record);

    case OSM(MOD_LSFT):
    case OSM(MOD_RSFT):
    case OSM(MOD_LCTL):
    case OSM(MOD_RCTL):
    case OSM(MOD_LALT):
    case OSM(MOD_RALT):
    case OSM(MOD_LGUI):
    case OSM(MOD_RGUI):
        return false;

1.  the implementation

    I just joinked callums oneshot implementation since I don&rsquo;t want to deal with foreign userspace stuff and depend on those.  Look at callums userspace for more information.
    
        // the different states a oneshot key can be in
        typedef enum {
            os_up_unqueued,
            os_up_queued,
            os_down_unused,
            os_down_used,
        } oneshot_state;
        
        void update_oneshot(oneshot_state *state, uint16_t mod, uint16_t trigger, uint16_t keycode, keyrecord_t *record) {
            if (keycode == trigger) {
                if (record->event.pressed) {
                    // Trigger keydown
                    if (*state == os_up_unqueued) {
                        register_code(mod);
                    }
                    *state = os_down_unused;
                } else {
                    // Trigger keyup
                    switch (*state) {
                        case os_down_unused:
                            // If we didn't use the mod while trigger was held, queue it.
                            *state = os_up_queued;
                            break;
                        case os_down_used:
                            // If we did use the mod while trigger was held, unregister it.
                            *state = os_up_unqueued;
                            unregister_code(mod);
                            break;
                        default:
                            break;
                    }
                }
            } else {
                if (record->event.pressed) {
                    if (is_oneshot_cancel_key(keycode) && *state != os_up_unqueued) {
                        // Cancel oneshot on designated cancel keydown.
                        *state = os_up_unqueued;
                        unregister_code(mod);
                    }
                } else {
                    if (!is_oneshot_ignored_key(keycode)) {
                        // On non-ignored keyup, consider the oneshot used.
                        switch (*state) {
                            case os_down_unused:
                                *state = os_down_used;
                                break;
                            case os_up_queued:
                                *state = os_up_unqueued;
                                unregister_code(mod);
                                break;
                            default:
                                break;
                        }
                    }
                }
            }
        }


<a id="orgdab8939"></a>

## putting it all together


<a id="org8e7dfca"></a>

### keymap.c

    /* vim:ro
     * -*- buffer-read-only: t -*-
     *
     * This is autogenerated using babel DO NOT EDIT.
     * Please refer to main.org in [[https://git.sr.ht/~jat/keymap]]
     *
     *
     * Copyright 2021 Freja
     *
     * This program is free software: you can redistribute it and/or modify
     * it under the terms of the GNU General Public License as published by
     * the Free Software Foundation, either version 2 of the License, or
     * (at your option) any later version.
     *
     * This program is distributed in the hope that it will be useful,
     * but WITHOUT ANY WARRANTY; without even the implied warranty of
     * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
     * GNU General Public License for more details.
     *
     * You should have received a copy of the GNU General Public License
     * along with this program.  If not, see <http://www.gnu.org/licenses/>.
     */
    
    #include QMK_KEYBOARD_H
    
    enum layers { _base = 0, _game, _low, _high, _adj, };
    
    const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
             [_base] = LAYOUT(KC_NO, KC_A, KC_F, KC_M, KC_P, KC_V, KC_SCOLON, KC_DOT, KC_SLASH, KC_QUOTE, KC_EQUAL, KC_NO, KC_NO, KC_R, KC_S, KC_N, KC_D, KC_W, KC_COMMA, KC_A, KC_E, KC_I, KC_O, KC_NO, KC_NO, KC_X, KC_G, KC_L, KC_C, KC_B, MO(_adj), KC_NO, KC_NO, KC_NO, KC_MINUS, KC_H, KC_U, KC_Y, KC_K, KC_NO, KC_LGUI, KC_NO, MO(_low), KC_T, KC_ENTER, KC_BSPACE, KC_SPACE, MO(_high), KC_RALT, KC_MUTE),
             [_game] = LAYOUT(KC_NO, KC_A, KC_W, KC_E, KC_R, KC_T, KC_NO, KC_NO, KC_3, KC_4, KC_NO, KC_NO, KC_NO, KC_Q, KC_S, KC_D, KC_F, KC_G, KC_7, KC_1, KC_2, KC_5, KC_6, KC_NO, KC_NO, KC_Z, KC_X, KC_C, KC_V, KC_B, KC_TRNS, KC_GESC, KC_TRNS, KC_TRNS, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_LGUI, KC_TAB, KC_LALT, KC_SPACE, LT(_low, KC_ENTER), KC_NO, KC_NO, KC_NO, KC_NO, KC_MUTE),
             [_low] = LAYOUT(KC_NO, KC_1, KC_2, KC_3, KC_4, KC_5, S(KC_1), S(KC_2), S(KC_3), S(KC_4), S(KC_5), KC_NO, KC_NO, KC_6, KC_7, KC_8, KC_9, KC_0, S(KC_6), S(KC_7), S(KC_8), S(KC_9), S(KC_0), KC_NO, KC_NO, KC_TRNS, KC_TRNS, KC_LBRC, KC_RBRC, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, S(KC_LBRC), S(KC_RBRC), S(KC_BSLASH), KC_TRNS, KC_NO, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS),
             [_high] = LAYOUT(KC_NO, KC_PSCR, KC_VOLU, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_NO, KC_NO, KC_TRNS, KC_VOLD, KC_MPRV, KC_MPLY, KC_MNXT, KC_LEFT, KC_DOWN, KC_UP, KC_RIGHT, KC_TRNS, KC_NO, KC_NO, KC_UNDO, KC_CUT, KC_COPY, KC_PASTE, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_NO, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS),
             [_adj] = LAYOUT(KC_NO, EH_LEFT, EH_RGHT, KC_NO, KC_NO, KC_NO, KC_NO, RGB_HUI, RGB_SAI, RGB_VAI, RGB_MOD, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, RGB_HUD, RGB_SAD, RGB_VAD, RGB_RMOD, KC_NO, KC_NO, RESET, EEP_RST, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, TG(_game), KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO),
    };
    
    #ifdef ENCODER_ENABLE
    bool is_alt_tab = false;
    uint16_t alt_tab_timer = 0;
    
    bool encoder_update_user(uint8_t index, bool clockwise) {
        if (index == 1) {
            if (clockwise) {
                tap_code(KC_VOLU);
            } else {
                tap_code(KC_VOLD);
            }
        } else if (index == 0) {
            if (clockwise) {
                if (!is_alt_tab) {
                    is_alt_tab = true;
                    register_code(KC_LALT);
                }
                alt_tab_timer = timer_read();
                tap_code16(KC_TAB);
            } else {
                if (!is_alt_tab) {
                    is_alt_tab = true;
                    register_code(KC_LALT);
                }
                alt_tab_timer = timer_read();
                tap_code16(S(KC_TAB));
            }
        }
    
        return false;
    }
    
    void matrix_scan_user(void) {
        if (is_alt_tab) {
            if (timer_elapsed(alt_tab_timer) > 800) {
                unregister_code(KC_LALT);
                is_alt_tab = false;
            }
        }
    }
    #endif
    
    const uint16_t PROGMEM unique_combo0[] = { KC_F, KC_M, COMBO_END, };
    const uint16_t PROGMEM unique_combo1[] = { KC_G, KC_L, COMBO_END, };
    const uint16_t PROGMEM unique_combo2[] = { KC_SLASH, KC_QUOTE, COMBO_END, };
    const uint16_t PROGMEM unique_combo3[] = { KC_U, KC_Y, COMBO_END, };
    const uint16_t PROGMEM unique_combo4[] = { KC_Z, KC_F, COMBO_END, };
    const uint16_t PROGMEM unique_combo5[] = { KC_M, KC_P, COMBO_END, };
    const uint16_t PROGMEM unique_combo6[] = { KC_X, KC_C, COMBO_END, };
    const uint16_t PROGMEM unique_combo7[] = { KC_Z, KC_P, COMBO_END, };
    const uint16_t PROGMEM unique_combo8[] = { KC_MINUS, KC_H, COMBO_END, };
    const uint16_t PROGMEM unique_combo9[] = { KC_F, KC_D, COMBO_END, };
    const uint16_t PROGMEM unique_combo10[] = { KC_A, KC_QUOTE, COMBO_END, };
    const uint16_t PROGMEM unique_combo11[] = { KC_F, KC_P, COMBO_END, };
    const uint16_t PROGMEM unique_combo12[] = { KC_DOT, KC_QUOTE, COMBO_END, };
    const uint16_t PROGMEM unique_combo13[] = { KC_F, KC_N, COMBO_END, };
    const uint16_t PROGMEM unique_combo14[] = { KC_E, KC_QUOTE, COMBO_END, };
    const uint16_t PROGMEM unique_combo15[] = { KC_QUOTE, KC_EQUAL, COMBO_END, };
    const uint16_t PROGMEM unique_combo16[] = { KC_F, KC_M, KC_E, KC_I, COMBO_END, };
    const uint16_t PROGMEM unique_combo17[] = { KC_S, KC_N, KC_SLASH, KC_QUOTE, COMBO_END, };
    const uint16_t PROGMEM unique_combo18[] = { KC_G, KC_C, COMBO_END, };
    const uint16_t PROGMEM unique_combo19[] = { KC_DOT, KC_O, COMBO_END, };
    const uint16_t PROGMEM unique_combo20[] = { KC_A, KC_O, COMBO_END, };
    const uint16_t PROGMEM unique_combo21[] = { KC_H, KC_Y, COMBO_END, };
    
    combo_t key_combos[COMBO_COUNT] = { COMBO(unique_combo0, OSM(MOD_LSFT)), COMBO(unique_combo1, OSM(MOD_LCTL)), COMBO(unique_combo2, OSM(MOD_LGUI)), COMBO(unique_combo3, OSM(MOD_LALT)), COMBO(unique_combo4, KC_Q), COMBO(unique_combo5, KC_J), COMBO(unique_combo6, KC_TAB), COMBO(unique_combo7, KC_ESC), COMBO(unique_combo8, KC_BSPACE), COMBO(unique_combo9, S(KC_9)), COMBO(unique_combo10, S(KC_0)), COMBO(unique_combo11, KC_LBRC), COMBO(unique_combo12, KC_RBRC), COMBO(unique_combo13, S(KC_LBRC)), COMBO(unique_combo14, S(KC_RBRC)), COMBO(unique_combo15, KC_GRAVE), COMBO(unique_combo16, S(KC_1)), COMBO(unique_combo17, S(KC_SLASH)), COMBO(unique_combo18, RALT(KC_A)), COMBO(unique_combo19, RALT(KC_W)), COMBO(unique_combo20, RALT(KC_O)), COMBO(unique_combo21, RALT(KC_U)), };
    
    bool is_oneshot_cancel_key(uint16_t keycode) {
      switch (keycode) {
        case MO(_high):
          return true;
        default:
          return false;
      }
    };
    
    bool is_oneshot_ignored_key(uint16_t keycode) {
      switch (keycode) {
        case OSM(MOD_LSFT):
        case OSM(MOD_RSFT):
        case OSM(MOD_LCTL):
        case OSM(MOD_RCTL):
        case OSM(MOD_LALT):
        case OSM(MOD_RALT):
        case OSM(MOD_LGUI):
        case OSM(MOD_RGUI):
        case MO(_low):
          return true;
        default:
          return false;
      }
    };
    
    // the different states a oneshot key can be in
    typedef enum {
        os_up_unqueued,
        os_up_queued,
        os_down_unused,
        os_down_used,
    } oneshot_state;
    
    void update_oneshot(oneshot_state *state, uint16_t mod, uint16_t trigger, uint16_t keycode, keyrecord_t *record) {
        if (keycode == trigger) {
            if (record->event.pressed) {
                // Trigger keydown
                if (*state == os_up_unqueued) {
                    register_code(mod);
                }
                *state = os_down_unused;
            } else {
                // Trigger keyup
                switch (*state) {
                    case os_down_unused:
                        // If we didn't use the mod while trigger was held, queue it.
                        *state = os_up_queued;
                        break;
                    case os_down_used:
                        // If we did use the mod while trigger was held, unregister it.
                        *state = os_up_unqueued;
                        unregister_code(mod);
                        break;
                    default:
                        break;
                }
            }
        } else {
            if (record->event.pressed) {
                if (is_oneshot_cancel_key(keycode) && *state != os_up_unqueued) {
                    // Cancel oneshot on designated cancel keydown.
                    *state = os_up_unqueued;
                    unregister_code(mod);
                }
            } else {
                if (!is_oneshot_ignored_key(keycode)) {
                    // On non-ignored keyup, consider the oneshot used.
                    switch (*state) {
                        case os_down_unused:
                            *state = os_down_used;
                            break;
                        case os_up_queued:
                            *state = os_up_unqueued;
                            unregister_code(mod);
                            break;
                        default:
                            break;
                    }
                }
            }
        }
    };
    
    oneshot_state sft_state = os_up_unqueued;
    oneshot_state ctl_state = os_up_unqueued;
    oneshot_state alt_state = os_up_unqueued;
    oneshot_state gui_state = os_up_unqueued;
    
    bool process_record_user(uint16_t keycode, keyrecord_t *record) {
        update_oneshot(&sft_state, KC_LSHIFT, OSM(MOD_LSFT), keycode, record);
        update_oneshot(&ctl_state, KC_LCTRL, OSM(MOD_LCTL), keycode, record);
        update_oneshot(&alt_state, KC_LALT, OSM(MOD_LALT), keycode, record);
        update_oneshot(&gui_state, KC_LGUI, OSM(MOD_LGUI), keycode, record);
    
        switch (keycode) {
            case OSM(MOD_LSFT):
            case OSM(MOD_RSFT):
            case OSM(MOD_LCTL):
            case OSM(MOD_RCTL):
            case OSM(MOD_LALT):
            case OSM(MOD_RALT):
            case OSM(MOD_LGUI):
            case OSM(MOD_RGUI):
                return false;
            default: return true;
        }
    }
    
    void matrix_init_user(void) {
    #ifdef RGB_MATRIX_ENABLE
        g_led_config = (led_config_t){
            {
                {NO_LED, NO_LED, 3, 4, 4, 5, 5},
                {NO_LED, NO_LED, 3, 4, 4, 5, 6},
                {0, 0, 1, 2, 2, 7, 6},
                {0, 0, 1, 2, 7, NO_LED, NO_LED},
                {NO_LED, NO_LED, 11, 12, 12, 13, 13},
                {NO_LED, NO_LED, 11, 12, 12, 13, 14},
                {8, 8, 9, 10, 10, 15, 14},
                {8, 8, 9, 10, 15, NO_LED, NO_LED},
            },
            {
                {91,40}, {77,56}, {63,56}, {77,24}, {63,8}, {21,8}, {21,40}, {35,40}, {133,40}, {147,56}, {161,56}, {147,24}, {161,8}, {203,8}, {203,40}, {189,40}
            },
            {
                255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255
            }
        };
    #endif
    }
    
    
    /* layer_state_t layer_state_set_user(layer_state_t state) { */
    /* #ifdef COMBO_ENABLE */
    /*     if (IS_LAYER_ON_STATE(state, _game)) { */
    /*         combo_disable(); */
    /*     } else { */
    /*         combo_enable(); */
    /*     } */
    /* #endif */
    /*     return state; */
    /* } */


<a id="org7f8149c"></a>

### config.h

    /* vim:ro
     * -*- buffer-read-only: t -*-
     *
     * This is autogenerated using babel DO NOT EDIT.
     * Please refer to main.org in [[https://git.sr.ht/~jat/keymap]]
     *
     *
     * Copyright 2021 Freja
     *
     * This program is free software: you can redistribute it and/or modify
     * it under the terms of the GNU General Public License as published by
     * the Free Software Foundation, either version 2 of the License, or
     * (at your option) any later version.
     *
     * This program is distributed in the hope that it will be useful,
     * but WITHOUT ANY WARRANTY; without even the implied warranty of
     * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
     * GNU General Public License for more details.
     *
     * You should have received a copy of the GNU General Public License
     * along with this program.  If not, see <http://www.gnu.org/licenses/>.
     */
    
    #pragma once
    
    #define EE_HANDS
    
    #define LAYER_STATE_8BIT
    
    #define TAPPING_TERM 300
    #define IGNORE_MOD_TAP_INTERRUPT
    
    #ifdef OLED_DRIVER_ENABLE
    #define OLED_DISPLAY_128X64
    #endif
    
    #ifdef NKRO_ENABLE
    #define FORCE_NKRO
    #endif
    
    #ifdef RGBLIGHT_ENABLE
    #define RGBLIGHT_LED_MAP {0,1,2,9,8,7,4,3,5,6,19,18,17,10,11,12,15,16,14,13}
    #define RGBLIGHT_SLEEP
    #define RGBLIGHT_EFFECT_BREATHING
    #define RGBLIGHT_EFFECT_KNIGHT
    
    #define RGBLIGHT_HUE_STEP 8
    #define RGBLIGHT_SAT_STEP 8
    #define RGBLIGHT_VAL_STEP 8
    #define RGBLIGHT_LIMIT_VAL 150
    #endif
    
    #ifdef RGB_MATRIX_ENABLE
    #define ENABLE_LED_MATRIX_SOLID
    /* #define ENABLE_LED_MATRIX_BREATHING */
    /* #define LED_MATRIX_KEYPRESSES */
    /* #define ENABLE_LED_MATRIX_SOLID_REACTIVE_SIMPLE */
    #endif
    
    #ifdef ENCODER_ENABLE
    #define ENCODER_RESOLUTION 2
    #define ENCODER_DIRECTION_FLIP
    #endif
    
    #ifdef COMBO_ENABLE
    #define COMBO_COUNT 22
    #define EXTRA_SHORT_COMBOS
    #define COMBO_TERM 70
    /* #define COMBO_NO_TIMER */
    #endif
    
    // define USB_POLLING_INTERVAL_MS 5


<a id="org20c553b"></a>

### rules.mk

    OLED_DRIVER_ENABLE = no
    WPM_ENABLE = no
    RGBLIGHT_ENABLE = no
    RGB_MATRIX_ENABLE = yes
    COMBO_ENABLE = yes
    ENCODER_ENABLE = yes
    STENO_ENABLE = no
    NKRO_ENABLE = no
    
    BOOTLOADER=qmk-hid
    BOOTLOADER_SIZE=512

