import pygame
import os


def load_image(name, colorkey=None):
    fullname = os.path.join(name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        raise Exception(f"Файл с изображением '{fullname}' не найден")

    image = pygame.image.load(fullname)

    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Car(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = load_image("car2.png", -1)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.speed = 5

    def update(self, width=None):
        self.rect.x += self.speed
        if width:
            if self.rect.x + self.image.get_rect()[2] >= width or self.rect.x <= 0:
                self.speed = -self.speed
                self.image = pygame.transform.flip(self.image, flip_y=False, flip_x=True)


def main():
    pygame.init()
    size = width, height = 600, 95
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Test")

    fps = 60
    running = True

    all_sprite = pygame.sprite.Group()
    car = Car(all_sprite)
    clock = pygame.time.Clock()
    while running:
        screen.fill(pygame.Color("white"))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_sprite.draw(screen)
        all_sprite.update(width)

        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()