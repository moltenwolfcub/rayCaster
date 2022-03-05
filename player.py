import math
import pygame

from settings import StaticSettings

class Player:

    def __init__(self):
        super().__init__()

        self.settings = StaticSettings()

        #self.image = pygame.image.load('graphics/player.png')
        #self.image = pygame.transform.scale(self.image, (self.settings.playerSize, self.settings.playerSize))
        self.image = pygame.Surface((self.settings.playerSize, self.settings.playerSize), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, (128, 255, 0), ((self.settings.playerSize//2, 0), (self.settings.playerSize - 5, self.settings.playerSize), (5, self.settings.playerSize)))
        self.original_image = self.image

        self.rect = pygame.Rect(0, 0, self.settings.playerSize, self.settings.playerSize)

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

        self.angle = 0
    
    def reset_player(self):
        self.rect.center = (self.settings.screenWidth//2, self.settings.screenHeight//2)

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update_player(self):

        self.LftRgtMotion = self.moving["right"] - self.moving["left"]
        self.FwdBckMotion = self.moving["down"] - self.moving["up"]
        self.rotation = self.moving["turning"]["right"] - self.moving["turning"]["left"]

        self.angle += self.rotation * self.settings.playerRotateSpeed
        self.angle = self.angle % 360

        
        self.image = pygame.transform.rotate(self.original_image, -self.angle)


        if self.moving["sneaking"]:
            if self.FwdBckMotion != 0:
                self.x += self.settings.playerSpeed + self.settings.playerSneakAjust * math.sin(self.angle) * self.FwdBckMotion
                self.y += self.settings.playerSpeed + self.settings.playerSneakAjust * math.cos(self.angle) * self.FwdBckMotion
            if self.LftRgtMotion != 0:
                self.x += self.settings.playerSpeed + self.settings.playerSneakAjust * math.sin(self.angle + 90 * self.LftRgtMotion)
                self.x += self.settings.playerSpeed + self.settings.playerSneakAjust * math.cos(self.angle + 90 * self.LftRgtMotion)

        elif self.moving["sprinting"]:
            if self.FwdBckMotion != 0:
                self.x += self.settings.playerSpeed + self.settings.playerSprintAjust * math.sin(self.angle) * self.FwdBckMotion
                self.y += self.settings.playerSpeed + self.settings.playerSprintAjust * math.cos(self.angle) * self.FwdBckMotion
            if self.LftRgtMotion != 0:
                self.x += self.settings.playerSpeed + self.settings.playerSprintAjust * math.sin(self.angle + 90 * self.LftRgtMotion)
                self.x += self.settings.playerSpeed + self.settings.playerSprintAjust * math.cos(self.angle + 90 * self.LftRgtMotion)

        else:
            if self.FwdBckMotion != 0:
                self.x += self.settings.playerSpeed * math.sin(self.angle) * self.FwdBckMotion
                self.y += self.settings.playerSpeed * math.cos(self.angle) * self.FwdBckMotion
            if self.LftRgtMotion != 0:
                self.x += self.settings.playerSpeed * math.sin(self.angle + 90 * self.LftRgtMotion)
                self.x += self.settings.playerSpeed * math.cos(self.angle + 90 * self.LftRgtMotion)

        self.rect.x = self.x
        self.rect.y = self.y


    def draw_player(self, surface):
        surface.blit(self.image, self.rect)
        

