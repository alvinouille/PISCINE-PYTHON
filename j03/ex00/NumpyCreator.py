import numpy as np

class NumPyCreator:
    def from_list(self, lst):
        return np.array(liste)
    
    def from_tuple(self, tpl):
        return np.array(tpl, dtype=np.int8)
    
    def from_iterable(self, itr):
        return np.array(itr)
    
    def from_shape(self, shape, value = 0):
        return np.full(shape, value)
    
    def random(self, shape):
        return np.random.randn(shape)
    
    def identity(self, n):
        return np.identity(n)



if __name__=='__main__':
    liste = [[34, 56], [23, 45]]
    tuple = ((1, 2, 3,  4, 5),(6, 7, 8, 9, 10))
    itr = "yo mon gros"
    nump = NumPyCreator()
    print(nump.from_list(liste))
    print(nump.from_tuple(tuple))
    print(nump.from_iterable(itr))
    print(nump.from_shape((4, 5), 5))
    print(nump.random(3))
    print(nump.identity(3))
