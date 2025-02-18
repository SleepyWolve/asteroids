import pygame
from sys import exit
from constants import *
from player import *
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
   
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()  

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        
        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")
                exit("You lose")
            for shot in shots:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()


        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000
    
    pygame.quit()

if __name__ == "__main__":
    main()
