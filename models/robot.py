class Robot():
    def __init__(self, robot_sprite):
        self.position = [0, 0]
        self.speed = 10
        self.sprite = robot_sprite

    def move_right(self):
        self.position[0] += self.speed

    def move_left(self):
        self.position[0] -= self.speed

    def move_up(self):
        self.position[1] -= self.speed

    def move_down(self):
        self.position[1] += self.speed
