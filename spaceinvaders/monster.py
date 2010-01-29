# monster.py
import pyglet

RIGHT = 0
LEFT = 1
DOWN = 2

MONSTER_SPEED = 20

class Monster(pyglet.sprite.Sprite):
    def __init__(self, image, x, y):
        pyglet.sprite.Sprite.__init__(self, image, x, y)
        self.active = True

    def deactivate(self):
        self.active = False

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
        self.movement_distance = 0
        self.x = 0
        self.y = 0
        self.direction = RIGHT
        self.next_direction = RIGHT

    def draw(self):
        for monster in self.monsters:
            # if monster is alive, draw it
            if monster.active:
                monster.draw()

    def move(self, dir_x, dir_y):
        self.x += dir_x
        self.y += dir_y
        for monster in self.monsters:
            monster.x += dir_x
            monster.y += dir_y

    def update(self, dt):
        if self.direction == RIGHT:
            # change only x-coordinate
            self.move(MONSTER_SPEED * dt, 0)
            # if container hits right border
            if self.x > (640 - self.width):
                self.direction = DOWN
                self.movement_distance = self.y - 50
                self.next_direction = LEFT
                return
        if self.direction == DOWN:
            # change only y-coordinate
            self.move(0, -MONSTER_SPEED * dt)
            if self.y < self.movement_distance:
                self.direction = self.next_direction
                return
        if self.direction == LEFT:
            # change only x-coordinate
            self.move(-MONSTER_SPEED * dt, 0)
            # if container hits left border
            if self.x < 0:
                self.direction = DOWN
                self.movement_distance = self.y - 50
                self.next_direction = RIGHT
                return
