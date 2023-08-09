import numpy as np
from ImageProcessor import ImageProcessor
from matplotlib import pyplot as PLT

class ScrapBooker:
    def crop(self, array, dim, position=(0, 0)):
        if not array[position[0]][position[1]]:
            return None
        else:
            end_lon = position[0] + dim[0]
            end_lar = position[1] + dim[1]
            new = array[position[0]:end_lon, position[1]:end_lar]
            return new
    
    def thin(self, array, n, axis):
        new = np.delete(array, np.s_[n -1:: n], 1 - axis)
        return new

    def juxtapose(self, array, n, axis):
        if axis == 1:
            new = np.zeros((len(array), len(array[0])*n))
            for i in range(n):
                start = i * len(array)
                new[:,start:start + len(array)] = array
            return new
        if axis == 0:
            new = np.zeros(((len(array) * n), len(array[0])))
            for i in range(n):
                start = i * len(array)
                new[start:start +len(array),:] = array
            return new
    
    def mosaic(self, array, dim):
        longueur = len(array) * dim[0]
        largeur = len(array) * dim[1]
        new = np.zeros((longueur, largeur))
        i = 0
        while i < dim[0]:
                si = i * len(array)
                j = 0
                while j < dim[1]:
                    sj = j * (len(array[0]))
                    new[si:si+len(array),sj:sj + len(array[0])] = array
                    j = j + 1
                i = i + 1
        return new


if __name__=='__main__':
    spb = ScrapBooker()
    arr1 = np.arange(0, 25).reshape(5, 5)
    print(arr1)
    print(spb.crop(arr1, (3, 1), (1, 0)))
    arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1,9)
    print(arr2)
    print(spb.thin(arr2, 3, 0))
    arr3 = np.array([[1, 2, 3],[1, 2, 3],[1, 2, 3]])
    print(arr3)
    print(spb.juxtapose(arr3, 3, 1))
    print(spb.mosaic(arr3, (3, 3)))
