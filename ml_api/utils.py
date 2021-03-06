from PIL import Image, ImageOps
import numpy as np
from io import StringIO

def read_digit(data: bytes, encoding: str) -> np.array:
    im = Image.frombytes(encoding, (28, 28), data)
    im = ImageOps.invert(im)
    arr = np.array(im)
    arr = arr / 255.0
    return np.array([arr])