import pygame


def background_image_menu(name, size, screen):
    image = pygame.image.load(f"Backgrounds_Menu/{name}")
    image = pygame.transform.scale(image, size)
    screen.blit(image, (0, 0))


def background_image_levels(name, size, screen):
    image = pygame.image.load(f"Levels_Back/{name}")
    image = pygame.transform.scale(image, size)
    screen.blit(image, (0, 0))
