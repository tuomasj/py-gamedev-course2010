# monster.py
import pyglet

RIGHT = 0
LEFT = 1
DOWN = 2

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
        self.x = 0
        self.y = 0
        self.direction = RIGHT

    def draw(self):
        for monster in self.monsters:
            monster.draw()

    def move(self, dir_x, dir_y):
        self.x += dir_x
        self.y += dir_y
        for monster in self.monsters:
            monster.x += dir_x
            monster.y += dir_y
            

    def update(self, dt):
        if self.direction == RIGHT:
            self.move(10 * dt, 0)
            # if container hits right border
            if self.x > (640 - self.width):
                self.direction = DOWN
                return
        
    
