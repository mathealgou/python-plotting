import random
from re import X
import pygame

BACKGROUND_COLOR = (20, 20, 20)
WHITE = (255, 255, 255)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TOP_PADDING = 50
LIST_SIZE = 50
CLOCK = 10


def generate_random_list(size: int, max_value: int) -> list:

    list = []

    for i in range(size):
        bar = {}
        bar['value'] = random.randint(0, max_value)
        bar['color'] = (random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255))
        bar['width'] = SCREEN_WIDTH / size
        list.append(bar)

    return list


def draw_list(list, screen):
    max_value = max(list, key=lambda x: x['value'])
    block_height = (SCREEN_HEIGHT - TOP_PADDING) / max_value['value']
    for i in range(len(list)):
        value = list[i]['value']
        color = list[i]['color']
        width = list[i]['width']
        height = block_height * value
        x = i * width
        y = TOP_PADDING + (max_value['value'] - value) * block_height

        pygame.draw.rect(surface=screen, color=color, rect=(
            x, y, width, height))


def draw_label(text, x, y, color, screen):
    font = pygame.font.SysFont('Arial', 20)
    label = font.render(text, 1, color)
    screen.blit(label, (x, y))


def bubble_sort(i, max_value, list):
    if i == max_value:
        return list
    for j in range(max_value):
        if list[j]["value"] > list[j+1]["value"]:
            list[j], list[j+1] = list[j+1], list[j]
    return list


def main():
    running = True
    sorting = False

    # pygame bullshittery
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Sorting Visualizer")
    clock = pygame.time.Clock()
    list = generate_random_list(LIST_SIZE, 100)

    n = 0

    while running:
        screen.fill(BACKGROUND_COLOR)
        if sorting:
            draw_label("Sorting", SCREEN_WIDTH/2,
                       35, WHITE, screen)
            list = bubble_sort(n, len(list)-1, list)
            n += 1
        if n >= len(list)-1:
            sorting = False

        draw_list(list, screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type != pygame.KEYDOWN:
                continue
            if event.key == pygame.K_r:
                list = generate_random_list(LIST_SIZE, 100)
                n = 0
            if event.key == pygame.K_SPACE:
                sorting = True
        pygame.display.flip()
        clock.tick(CLOCK)
    pygame.quit()


if __name__ == "__main__":
    main()
