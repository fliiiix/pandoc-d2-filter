#!/usr/bin/env python

import os
import subprocess
import sys

from pandocfilters import Image, Para, get_caption, get_filename4code, get_value, toJSONFilter

D2_BIN = os.environ.get("D2_BIN", "d2")

d2_theme = {
    "Neutral default": 0,
    "Neutral Grey": 1,
    "Flagship Terrastruct": 3,
    "Cool classics": 4,
    "Mixed berry blue": 5,
    "Grape soda": 6,
    "Aubergine": 7,
    "Colorblind clear": 8,
    "Vanilla nitro cola": 100,
    "Orange creamsicle": 101,
    "Shirley temple": 102,
    "Earth tones": 103,
    "Everglade green": 104,
    "Buttered toast": 105,
    "Terminal": 300,
    "Terminal Grayscale": 301,
    "Origami": 302,
    "Dark Mauve": 200,
    "Dark Flagship Terrastruct": 201,
}


def extract_theme_id(theme: str) -> int:
    try:
        # Value is just theme id
        theme = int(theme)
        if theme not in d2_theme.values():
            sys.stderr.write(
                "Theme {theme} not found make sure its a valid theme with `d2 themes`! Using default from d2."
            )
    except ValueError:
        try:
            # Value is theme name
            return d2_theme[theme]
        except KeyError:
            sys.stderr.write(f"Theme {theme} not found make sure its a valid theme with `d2 themes`! Using default 0.")
            pass
    return 0


def d2(key, value, format, meta):  # noqa: ARG001
    if key == "CodeBlock":
        [[ident, classes, keyvals], code] = value

        if "d2" in classes:
            caption, typef, keyvals = get_caption(keyvals)

            filename = get_filename4code("d2", code)
            filetype = "png"

            theme = extract_theme_id(get_value(keyvals, "theme", 0)[0])

            src = filename + ".d2"
            dest = filename + "." + filetype

            # sys.stderr.write(f"{keyvals=}")

            txt = code.encode(sys.getfilesystemencoding())
            with open(src, "wb") as f:
                f.write(txt)

            subprocess.check_call([D2_BIN, f"--theme={theme}", src, dest])
            sys.stderr.write("Created image " + dest + "\n")

            return Para([Image([ident, [], keyvals], caption, [dest, typef])])


def main():
    toJSONFilter(d2)


if __name__ == "__main__":
    main()
