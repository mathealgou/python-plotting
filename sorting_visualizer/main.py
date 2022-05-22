import random
import pygame

BACKGROUND_COLOR: tuple = (20, 20, 20)


def generate_random_list(size: int, max_value: int) -> list:
    return [random.randint(0, max_value) for _ in range(size)]


def draw_list(list, screen):

    for i in range(len(list)):
        pygame.draw.rect(screen, (127, 127, 127),
                         (i * 10, 600 - list[i], 10, list[i]))


def main():
    running = True
    sorting = False

    # pygame bullshittery
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Sorting Visualizer")
    clock = pygame.time.Clock()
    list = generate_random_list(10, 100)

    n = 0

    while running:
        screen.fill(BACKGROUND_COLOR)
        draw_list(list, screen)
        if sorting:
            if n < len(list):
                for j in range(len(list) - 1):
                    if list[j] > list[j + 1]:
                        list[j], list[j + 1] = list[j + 1], list[j]
                n += 1
            else:
                sorting = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type != pygame.KEYDOWN:
                continue
            if event.key == pygame.K_r:
                list = generate_random_list(10, 100)
                n = 0
            if event.key == pygame.K_SPACE:
                sorting = True
        pygame.display.flip()
        clock.tick(10)
    pygame.quit()


if __name__ == "__main__":
    main()
