import sys

import pygame


from settings import StaticSettings
from mazeElement import MazeElement
from player import Player



class RayCasterMain:
    "main class"

    def __init__(self) -> None:
        pygame.init()

        self.settings = StaticSettings()

        self.screen_init()
        self.maze_init()
        self.player_init()

        self.running = True

    def screen_init(self):
        self.icon = pygame.image.load('graphics/icon.png')
        pygame.display.set_icon(self.icon)

        self.screen = pygame.display.set_mode((self.settings.screenWidth, self.settings.screenHeight))
        pygame.display.set_caption("RayCaster")

    def maze_init(self):
        self.maze_parts = pygame.sprite.Group()

        self.maze_elements_list = [
            #edge walls
            (0, 0, 25, self.settings.screenHeight),
            (self.settings.screenWidth-25, 0, 25, self.settings.screenHeight),
            (0, 0, self.settings.screenWidth, 25),
            (0, self.settings.screenHeight-25, self.settings.screenWidth, 25),

            (self.settings.screenWidth//2 ,0, 50, self.settings.screenHeight//3)
        ]

        for part in self.maze_elements_list:
            element = MazeElement(part)
            self.maze_parts.add(element)

    def player_init(self):
        self.player = Player()



    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)

    def check_keydown_events(self, event):
        if event.key == pygame.K_ESCAPE:
            sys.exit()
        
        elif event.key == pygame.K_d:
            self.player.moving["right"] = True
        elif event.key == pygame.K_a:
            self.player.moving["left"] = True
        elif event.key == pygame.K_s:
            self.player.moving["down"] = True
        elif event.key == pygame.K_w:
            self.player.moving["up"] = True

        elif event.key == pygame.K_LCTRL:
            self.player.moving["sprinting"] = True
        elif event.key == pygame.K_LSHIFT:
            self.player.moving["sneaking"] = True

    def check_keyup_events(self, event):

        if event.key == pygame.K_d:
            self.player.moving["right"] = False
        elif event.key == pygame.K_a:
            self.player.moving["left"] = False
        elif event.key == pygame.K_s:
            self.player.moving["down"] = False
        elif event.key == pygame.K_w:
            self.player.moving["up"] = False

        elif event.key == pygame.K_LCTRL:
            self.player.moving["sprinting"] = False
        elif event.key == pygame.K_LSHIFT:
            self.player.moving["sneaking"] = False


    def update_screen(self):
        self.screen.fill(self.settings.screenBaseColor)

        self.maze_parts.draw(self.screen)
        self.player.update_player()
        self.player.draw_player(self.screen)

        pygame.display.flip()




    def run_game(self):
        while self.running:
            self.check_events()

            self.update_screen()




if __name__ == '__main__':
    instance = RayCasterMain()
    instance.run_game()
