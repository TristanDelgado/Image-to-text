#transforms a given image into a text representation
from PIL import Image

def get_rgb(file_location: str):
    """
    Opens an image file and returns its RGB values for every pixel.

    Returns:
    tuple of tuples of every RGB value.
    The pixel values are ordered from left to right from the
    top row to the bottom row.
    """
    file_extension = file_location.split(".")[-1]
    #Debug statement
    print(file_location)
    print(file_extension)
    if(file_extension in ("png", "jpg", "jpeg", "webp")):
        im = Image.open(file_location)
        uniqueColors = set(im.getdata())
    return "Executed"
