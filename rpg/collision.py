# collision.py

def check_collision(spr1, spr2):
    # y-coordinate is inverted in pyglet
    left1 = spr1.x
    right1 = spr1.x + spr1.width
    bottom1 = spr1.y
    top1 = spr1.y + spr1.height

    left2 = spr2.x
    right2 = spr2.x + spr2.width
    bottom2 = spr2.y
    top2 = spr2.y + spr2.height

    # test x-coordinates
    if left1 > right2 or right1 < left2:
        return False

    # test y-coordinates
    if bottom1 > top2 or top1 < bottom2:
        return False

    return True
