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

            "turning": {
                "right": False,
                "left": False
            },

            "sprinting": False,
            "sneaking": False
        }

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.angle = pygame.math.Vector2(0, -1)

    
    def reset_player(self):
        self.rect.center = (self.settings.screenWidth//2, self.settings.screenHeight//2)

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update_player(self):

        self.movingX = self.moving["right"] - self.moving["left"]
        self.movingY = self.moving["down"] - self.moving["up"]
        self.rotation = self.moving["turning"]["right"] - self.moving["turning"]["left"]

        if self.rotation != 0:
            self.angle.rotate_ip(self.rotation * self.settings.playerRotateSpeed)

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
        

