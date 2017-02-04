#!/usr/bin/env python3
import sys

from PIL import Image

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Usage: %s image-path" % sys.argv[0])

    filepath = sys.argv[1]
    try:
        image_base = Image.open(filepath)
    except IOError:
        sys.exit("ERROR: Couldn't open image from %s" % filepath)

    #Convert to 8-bit black and white image mode
    image_bw = image_base.convert("L")
