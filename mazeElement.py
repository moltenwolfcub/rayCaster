import pygame
from pygame.sprite import Sprite

class MazeElement(Sprite):
    """A Class to manage the maze"""

    def __init__(self, game, shape):
        """Create the maze"""
        super().__init__()

        self.image = pygame.image.load('graphics/maze_color.png')
        self.image = pygame.transform.scale(self.image, (shape[2], shape[3]))
        self.rect = pygame.Rect(shape)

        self.rect.x = shape[0]
        self.rect.y = shape[1]
