import pygame
import random

pygame.init()
WIDTH, HEIGHT = 800, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Koşu Oyunu")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GROUND = HEIGHT - 60

FONT = pygame.font.SysFont("Arial", 24)

class Runner:
    def __init__(self):
        self.x = 100
        self.y = GROUND
        self.width = 40
        self.height = 60
        self.jump = False
        self.vel_y = 0

    def draw(self):
        pygame.draw.rect(WIN, BLACK, (self.x, self.y, self.width, self.height))

    def update(self):
        if self.jump:
            self.vel_y = -15
            self.jump = False
        self.y += self.vel_y
        self.vel_y += 1
        if self.y >= GROUND:
            self.y = GROUND
            self.vel_y = 0

class Obstacle:
    def __init__(self):
        self.x = WIDTH
        self.y = GROUND + 20
        self.width = 30
        self.height = 40

    def draw(self):
        pygame.draw.rect(WIN, (200, 0, 0), (self.x, self.y, self.width, self.height))

    def update(self):
        self.x -= 7

def main():
    run = True
    clock = pygame.time.Clock()
    player = Runner()
    obstacles = []
    score = 0

    while run:
        clock.tick(60)
        WIN.fill(WHITE)
        pygame.draw.line(WIN, BLACK, (0, GROUND + 60), (WIDTH, GROUND + 60), 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player.y == GROUND:
                    player.jump = True

        if random.randint(1, 60) == 1:
            obstacles.append(Obstacle())

        player.update()
        player.draw()

        for obs in obstacles[:]:
            obs.update()
            obs.draw()
            if obs.x + obs.width < 0:
                obstacles.remove(obs)
                score += 1
            if player.x + player.width > obs.x and player.x < obs.x + obs.width:
                if player.y + player.height > obs.y:
                    run = False

        score_text = FONT.render(f"Skor: {score}", True, BLACK)
        WIN.blit(score_text, (10, 10))
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()