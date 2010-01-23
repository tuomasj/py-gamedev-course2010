# monster.py
import pyglet

class Monster(pyglet.sprite.Sprite):
    pass

class MonsterContainer():
    def __init__(self, cols, rows):
        self.monsters = []
        monster_image = pyglet.image.load('monster.png')

        for y in range(rows):
            for x in range(cols):
                monster = Monster( monster_image,  x * 36, 480 - (y * 36) - 32 )
                self.monsters.append( monster )

        self.width = 36 * cols
        self.height = 36 * rows

    def draw(self):
        for monster in self.monsters:
            monster.draw()

    def update(self, dt):
        for monster in self.monsters:
            monster.x += 5 * dt
    
