import sys

import pygame


from settings import Settings
from mazeElement import MazeElement



class RayCasterMain:
    "main class"

    def __init__(self) -> None:
        pygame.init()

        self.settings = Settings()

        self.screen_init()
        self.maze_init()

        self.running = True

    def screen_init(self):

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("RayCaster")

    def maze_init(self):
        self.maze_parts = pygame.sprite.Group()

        self.maze_elements_list = [
            #edge walls
            (0, 0, 25, self.settings.screen_height),
            (self.settings.screen_width-25, 0, 25, self.settings.screen_height),
            (0, 0, self.settings.screen_width, 25),
            (0, self.settings.screen_height-25, self.settings.screen_width, 25)
        ]

        for part in self.maze_elements_list:
            element = MazeElement(self, part)
            self.maze_parts.add(element)




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

    def check_keyup_events(self, event):
        pass


    def update_screen(self):

        self.maze_parts.draw(self.screen)

        pygame.display.flip()




    def run_game(self):
        while self.running:
            self.check_events()

            self.update_screen()




if __name__ == '__main__':
    instance = RayCasterMain()
    instance.run_game()
