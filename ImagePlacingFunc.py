import pygame
from Image_to_list_loader import Size,CellImages
def Coordinate(x,y):
    m,n = 250,250
    m += (x - 2) * Size
    n += (y - 2) * Size
    return m, n

def DrawCell(a, b, c, win):
    x, y = Coordinate(b, c)
    if a > 0 and a < 17:
        win.blit(CellImages[a - 1], (x, y))
    else:
        pygame.draw.rect(win, (255, 255, 255), (x, y, Size, Size))


def DrawBackground(win):
    pygame.draw.rect(win, (0, 0, 0), (250, 250 - 2 * Size, 3, 4 * Size))
    pygame.draw.rect(win, (0, 0, 0), (250 - Size, 250 - 2 * Size, 3, 4 * Size))
    pygame.draw.rect(win, (0, 0, 0), (250 + Size, 250 - 2 * Size, 3, 4 * Size))
    pygame.draw.rect(win, (0, 0, 0), (250 - 2 * Size, 250, 4 * Size, 3))
    pygame.draw.rect(win, (0, 0, 0), (250 - 2 * Size, 250 - Size, 4 * Size, 3))
    pygame.draw.rect(win, (0, 0, 0), (250 - 2 * Size, 250 + Size, 4 * Size, 3))


def CoordIntoNumber(x, y):
    return x * 4 + y + 1


def NumberIntoCoord(x):
    x -= 1
    a = x // 4
    b = x % 4
    return a, b

