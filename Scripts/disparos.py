# Miguel Ángel Jiménez 23-EISN-2-010
import pygame, Scripts.spritesheet as spritesheet
from Scripts.constantes import *
from Scripts.animateobj import *

# Clase Bullet, representa una bala en el juego
class Bullet(AnimateObj):
    bulletcnt = BULLETS_MAX
    bulletcolor = WHITE

    # Controla la creación de balas según el límite máximo
    def __new__(cls, *args):
        if Bullet.bulletcnt == 0:
            return None
        elif args[1] == 'still':
            return None
        else:
            Bullet.bulletcnt -= 1
            return super(Bullet, cls).__new__(cls)

    def __init__(self, color, direction, x, y, filename, speed=16, count=1, colorkey=BLACK, scale=2):
        # Inicializa la bala y su sprite
        super(Bullet, self).__init__()
        ss = spritesheet.spritesheet(filename)

        # Diccionario de imágenes para cada dirección de disparo
        IMG_DICT = {"W": (0, 0 ,6, 1), "E": (0, 0, 6, 1), "N": (24, 0, 1, 6), "S": (24, 0, 1, 6),
                    "NE": (16, 0, 6, 6), "SE": (8, 0, 6, 6), "NW": (8, 0, 6, 6), "SW": (16, 0, 6, 6)}

        if direction in IMG_DICT:
            self.images.append(ss.image_at(IMG_DICT[direction]))

        self.direction = direction
        self.speed = speed

        # Escala la imagen de la bala
        image = self.images[0]
        w, h = image.get_size()
        cropped_image = image.subsurface(0, 0, w, h)
        scale_image = pygame.transform.scale(cropped_image, (scale*w, scale*h))
        self.images[0] = scale_image

        self.image = self.images[0]
        self.rect = self.image.get_rect()

        self.setcolor(color)

        self.rect.x = x
        self.rect.y = y
        self.addpattern('bullet', [0])
        self.setpattern('bullet')

    # Libera una bala cuando es destruida
    def kill(self):
        Bullet.bulletcnt += 1
        super(Bullet, self).kill()

    # Actualiza la posición de la bala y la elimina si sale de la pantalla
    def update(self):
        super(Bullet, self).update()

        x, y  = {"W": (-1, 0), "E": (1, 0,), "N": (0, -1), "S": (0, 1,),
                 "NE": (1, -1), "NW": (-1, -1), "SE": (1, 1), "SW": (-1, 1),
                 "still": (0, 0)}[self.direction]

        self.rect.x += x*self.speed
        self.rect.y += y*self.speed

        # Elimina la bala si sale de los límites de la pantalla
        if (self.rect.x < 10) or (self.rect.x > (SCREEN_WIDTH - 16)):
            self.kill()
        if (self.rect.y < 10) or (self.rect.y > (SCREEN_HEIGHT - 16)):
            self.kill()

    def draw(self):
        # Método de dibujo (no implementado)
        pass

