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
                monster = Monster( monster_image,  x * 36, y* 36)
                self.monsters.append( monster )

    def draw(self):
        for monster in self.monsters:
            monster.draw()

    
