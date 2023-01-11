# coding: utf-8

from PIL import Image, ImageGrab

def load_img_from_file(imgPath):
    """Return the Image object of a given file path.

    Args:
        imgPath (str): File path of the image.

    Returns:
        Image | None: The Image object of the file. If it is not an image or the path does not exist, return None.
    """
    img = Image.open(imgPath)
    if isinstance(img, Image.Image):
        img.save('temp.png')
        return Image.open(imgPath)
    else:
        return None