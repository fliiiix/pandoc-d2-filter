#!/usr/bin/env python

import os
import sys
import subprocess

from pandocfilters import toJSONFilter, Para, Image
from pandocfilters import get_filename4code, get_value, get_caption, get_extension

D2_BIN = os.environ.get("D2_BIN", "d2")

def d2(key, value, format, meta):
    if key == "CodeBlock":
        [[ident, classes, keyvals], code] = value

        if "d2" in classes:
            caption, typef, keyvals = get_caption(keyvals)

            filename = get_filename4code("d2", code)
            filetype = "png"

            theme = get_value(keyvals, "theme", 0)[0]
            src = filename + ".d2"
            dest = filename + "." + filetype

            #sys.stderr.write(f"{keyvals=}")

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
