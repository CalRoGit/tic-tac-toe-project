import stddraw

def DrawX(x, y):
    """
    Draw an X on the board
    Args:
    x (int): Top left x cord of X
    y (int): Top left y cord of X
    """
    stddraw.line(x, y, x + 1.5, y - 1.5)
    stddraw.line(x, y - 1.5, x + 1.5, y)

def DrawXAnimation(x, y):
    """
    Animate an X onto the board
    Args:
    x (int): Top left x cord of X
    y (int): Top left y cord of X
    """
    stddraw.line(x, y, (x + (x + 1.5))/2, (y + (y - 1.5))/2)
    stddraw.show(100)
    stddraw.line((x + (x + 1.5))/2, (y + (y - 1.5))/2, x + 1.5, y - 1.5)
    stddraw.show(100)
    stddraw.line(x, y - 1.5, (x + (x + 1.5))/2, (y + (y - 1.5))/2)
    stddraw.show(100)
    stddraw.line((x + (x + 1.5))/2, (y + (y - 1.5))/2, x + 1.5, y)

def DrawO(x, y, r):
    """
    Draw an O on the board
    Args:
    x (int): Middle x cord of O
    y (int): Middle y cord of O
    r (int): Radius of O
    """
    stddraw.circle(x, y, r)

def DrawOAnimation(x, y, r):
    """
    Animate an O onto the board
    Args:
    x (int): Middle x cord of O
    y (int): Middle y cord of O
    r (int): Radius of O
    """
    stddraw.circle(x, y, r)
    stddraw.setPenColor(stddraw.DARK_GRAY)
    stddraw.filledRectangle(x, y - 0.95, r, 1.9)
    stddraw.show(100)
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.circle(x, y, r)