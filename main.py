import pygame

from models.robot import Robot

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 1920
screen_height = 1006
bg = pygame.image.load("assets/background.jpg")
bg = pygame.transform.scale(bg, (screen_width, screen_height))
robot_sprite = pygame.image.load("assets/player.png")
robot_sprite = pygame.transform.scale(robot_sprite, (100, 100))
heart_sprite = pygame.image.load("assets/heart.png")
heart_sprite = pygame.transform.scale(heart_sprite, (50, 25))

player_sprite_sheet = pygame.image.load("assets/player/player_sprite_sheet.png")
frame_width, frame_height = 32, 48
num_frames = 4
frames = [player_sprite_sheet.subsurface((i * frame_width, 0, frame_width, frame_height)) for i in range(num_frames)]


robot = Robot(robot_sprite)
lifeBar = pygame.Surface((screen_width, 30))
lifeBar.fill((255, 255, 255))


def render_hearts():
    heart_y = (screen_height - lifeBar.get_height() + ((lifeBar.get_height() - heart_sprite.get_height()) / 2))
    heart_x = -40

    for heart in range(robot.hearts):
        heart_x += heart_sprite.get_width() - 20
        screen.blit(heart_sprite, (heart_x, heart_y))


screen = pygame.display.set_mode((screen_width, screen_height))

screen_rect = screen.get_rect()

game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and robot.position[0] < screen_width - robot.size[1]:
        robot.move_right()

    if keys[pygame.K_LEFT] and robot.position[0] > -0:
        robot.move_left()

    if keys[pygame.K_UP] and robot.position[1] > 0:
        robot.move_up()

    if keys[pygame.K_DOWN] and robot.position[1] < screen_height - lifeBar.get_height() - robot.size[1]:
        robot.move_down()

    screen.blit(bg, (0, 0))
    screen.blit(lifeBar, (0, screen_height - 30))
    screen.blit(robot.sprite, (robot.position[0], robot.position[1]))

    render_hearts()

    pygame.display.flip()

    clock.tick(fps)

pygame.quit()
