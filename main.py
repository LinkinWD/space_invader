import pygame, sys
from player import  Player
import obsticle


class Game:
    def __init__(self):
        #player setup
        player_sprite = Player((screen_width / 2, screen_height), 600, 5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        #obsticle setup
        self.shape = obsticle.shape
        self.block_size = 6
        self.blocks = self.blocks = pygame.sprite.Group()
        self.create_obstacle()
    def create_obstacle(self):
         for row_index, row in enumerate(self.shape):
             for col_index, col in enumerate(row):
                 if col == 'x':
                    x = col_index * self.block_size
                    y = row_index * self.block_size
                    block = obsticle.Block(self.block_size,(241,79,80),x,y)
                    self.blocks.add(block)

    def run(self):
        self.player.update()

        self.player.sprite.lasers.draw(screen)

        self.player.draw(screen)
        self.blocks.draw(screen)

if __name__ == '__main__':
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width,screen_height))
    clock = pygame.time.Clock()
    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((30,30,30))
        game.run()

        pygame.display.flip()
        clock.tick(60)