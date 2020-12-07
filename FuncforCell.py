 # from _2048 import Size


Size = 125

    

   


def Coordinate(x,y):
    m,n = 250,250
    m += (x - 2) * Size
    n += (y - 2) * Size
    return m, n

    

    