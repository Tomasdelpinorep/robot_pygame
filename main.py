import pygame

from models.robot import Robot

pygame.init()
bg = pygame.image.load("assets/background.png")
robot_sprite = pygame.image.load("assets/megaman.png")
robot_sprite = pygame.transform.scale(robot_sprite, (50, 50))
heartIcon = pygame.image.load("assets/megaman.png")
robot = Robot(robot_sprite)
screen_width = 800
screen_height = 600
lifeBar = pygame.Surface((screen_width, 50))
lifeBar.fill((0, 0, 0))

screen = pygame.display.set_mode((screen_width, screen_height))
screen.blit(bg, (0, 0))

game_running = True
while game_running:
    for event in pygame.event.get():

        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_RIGHT:
        #         robot.move_right()
        #     if event.key == pygame.K_LEFT:
        #         robot.move_left()
        #     if event.key == pygame.K_UP:
        #         robot.move_up()
        #     if event.key == pygame.K_DOWN:
        #         robot.move_down()

        if event.type == pygame.QUIT:
            game_running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        robot.move_right()
    if keys[pygame.K_LEFT]:
        robot.move_left()
    if keys[pygame.K_UP]:
        robot.move_up()
    if keys[pygame.K_DOWN]:
        robot.move_down()

    screen.blit(bg, (0, 0))
    screen.blit(robot.sprite, (robot.position[0], robot.position[1]))
    screen.blit(lifeBar, (0, screen_height - 50))
    lifeBar.blit(heartIcon, (100, 100))
    pygame.display.flip()

pygame.quit()
