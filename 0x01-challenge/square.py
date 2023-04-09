#!/usr/bin/python3

class square():
    """ Square class """ 
        
    def __init__(self, side_length):
        """ Instantiation of class """
        self.side_length = side_length

    def area_of_my_square(self):
        """ Area of the square """
        return self.side_length ** 2

    def PermiterOfMySquare(self):
        """ Perimeter of my square """
        return (self.side_length * 4)

    def __str__(self):
        """ Print representation """
        return "{}".format(self.side_length)

if __name__ == "__main__":

    s = square(12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
