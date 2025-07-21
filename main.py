import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    time = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()
    Asteroid.containers = (asteroid_group, updatable_group, drawable_group)
    Player.containers = (updatable_group, drawable_group)
    AsteroidField.containers = updatable_group
    Shot.containers = (shot_group, updatable_group, drawable_group)
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill([0, 0, 0])
        updatable_group.update(dt)
        for asteroid in asteroid_group:
            if asteroid.checkCollision(player):
                print("Game over!")
                return
            for bullet in shot_group:
                if asteroid.checkCollision(bullet):
                    bullet.kill()
                    asteroid.kill()
        for object in drawable_group:
            object.draw(screen)
        pygame.display.flip()
        dt = time.tick(60) / 1000
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
