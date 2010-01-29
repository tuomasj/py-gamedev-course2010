# bullet.py
import pyglet

class Bullet():

    def __init__(self):
        bullet_image = pyglet.image.load('bullet.png')
        self.sprite = pyglet.sprite.Sprite(bullet_image, 10, 10)

        # bullet has not been shot
        self.active = False

    def update(self, dt):
        if self.active:
            self.sprite.y += dt * 80
            if self.sprite.y > 480:
                self.active = False

    def shoot(self, x, y):
        if not self.active:
            self.sprite.x = x + 16 - (self.sprite.width / 2)
            self.sprite.y = y + 32 + self.sprite.height
            self.active = True

    def draw(self):
        if self.active:
            self.sprite.draw()

    def deactivate(self):
        self.active = False

