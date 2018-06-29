from imagekit import ImageSpec
from imagekit import processors

class Rename(object):
    def __init__(self, extension):
        self.extension = extension

    def process(self, img):
        original_name = img.name
        splitted_name = original_name.split('.')
        new_name = "".join(splitted_name[0:-1]) + self.extension + "." + "".join(splitted_name[-1])
        img.name = new_name
        return img



names = ['resize', 'res_to_fill', 'res_to_cover', 'res_smart', 'res_canvas', 'res_to_fit']

width = 640
height = 320


class ResizeImg(ImageSpec):
    processors = [processors.Resize(width, height), Rename(names[0])]
    format = 'JPEG'
    options = {'quality': 90}


class ResToFillImg(ImageSpec):
    processors = [processors.ResizeToFill(width, height), Rename(names[1])]
    format = 'JPEG'
    options = {'quality': 90}


class ResToCover(ImageSpec):
    processors = [processors.ResizeToCover(width, height), Rename(names[2])]
    format = 'JPEG'
    options = {'quality': 90}


class ResSmart(ImageSpec):
    processors = [processors.SmartResize(width, height), Rename(names[3])]
    format = 'JPEG'
    options = {'quality': 90}

class ResCanvas(ImageSpec):
    processors = [processors.ResizeCanvas(width, height), Rename(names[4])]
    format = 'JPEG'
    options = {'quality': 90}

class ResToFit(ImageSpec):
    processors = [processors.ResizeToFit(width, height), Rename(names[5])]
    format = 'JPEG'
    options = {'quality': 90}

