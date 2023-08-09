import numpy as np
from matplotlib import pyplot as PLT

class ImageProcessor:
    def load(self, path):
        image = PLT.imread(path, "dtype=float32")
        if len(image[0][0]) == 4:
            tmp = image[:, :, :3]
            image = tmp
        if len(image[0][0]) == 3:
            lon, lar = len(image), len(image[0])
            print(f"Size of the image : {lon} x {lar}")
            return image

    def display(self, array):
        PLT.imshow(array)
        PLT.axis("off")
        PLT.show()

if __name__=='__main__':
    imp = ImageProcessor()
    arr = imp.load("image.png")
    imp.display(arr)
