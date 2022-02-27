import pygame

from settings import StaticSettings

class Player:

    def __init__(self):
        super().__init__()

        self.settings = StaticSettings()

        self.image = pygame.image.load('graphics/player.png')
        self.image = pygame.transform.scale(self.image, (self.settings.playerSize, self.settings.playerSize))
        self.rect = self.image.get_rect()

        self.reset_player()

        self.moving = {
            "right": False,
            "left": False,
            "up": False,
            "down": False,

            "sprinting": False,
            "sneaking": False
        }

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    
    def reset_player(self):
        self.rect.center = (self.settings.screenWidth//2, self.settings.screenHeight//2)

    def update_player(self):

        self.movingX = self.moving["right"] - self.moving["left"]
        self.movingY = self.moving["down"] - self.moving["up"]

        if self.moving["sneaking"]:
            self.x += self.movingX*(self.settings.playerSpeed+self.settings.playerSneakAjust)
            self.y += self.movingY*(self.settings.playerSpeed+self.settings.playerSneakAjust)
        elif self.moving["sprinting"]:
            self.x += self.movingX*(self.settings.playerSpeed+self.settings.playerSprintAjust)
            self.y += self.movingY*(self.settings.playerSpeed+self.settings.playerSprintAjust)
        else:
            self.x += self.movingX*self.settings.playerSpeed
            self.y += self.movingY*self.settings.playerSpeed

        self.rect.x = self.x
        self.rect.y = self.y


    def draw_player(self, surface):
        surface.blit(self.image, self.rect)
        

