#!/usr/bin/env python3
class Shoe:
    def __init__(self, brand, condition = 'Used', size = 0 ):
        self.brand = brand
        self.size = size
        self.condition = condition

    def get_size(self):
        return self._size
    
    def set_size(self,size):
        if type(size) != int:
            print('size must be an integer')
            return False
        self._size  = size
    
    def cobble(self):
        self.condition = 'New'
        print('Your shoe is as good as new!')

    size = property(get_size, set_size)        