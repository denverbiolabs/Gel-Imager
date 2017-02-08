#!/usr/bin/env python3
import sys

import numpy as np
from scipy.signal import argrelmin
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

    #find local minima
    hist = image_bw.histogram()
    minima = argrelmin(np.array(hist), order=10)[0]
    threshold = minima[0] #Current assumption: Because of the way argrelmin clips
    #values, the left side of the histogram won't actually count as a local minimum,
    #so the first local minimum will be the center of the valley between the gel color
    #and the band color.
    #I'm not totally sure if this is generally true.

    #Set all shades to black below a given threshold
    image_filtered = image_bw.point(lambda p: 0 if p < threshold else p)
    image_filtered.save("test_out.png")
