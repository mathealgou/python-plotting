import random
from re import X
import pygame

BACKGROUND_COLOR = (20, 20, 20)
WHITE = (255, 255, 255)
DARK_GRAY = (50, 50, 50)
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
        y = (TOP_PADDING + (max_value['value'] - value) * block_height) - 15

        pygame.draw.rect(surface=screen, color=color, rect=(
            x, y, width, height + 15))


def draw_label(text, x, y, color, screen):
    font = pygame.font.SysFont('Arial', 20)
    label = font.render(text, 1, color)
    screen.blit(label, (x, y))


def draw_controls(screen):
    font_large = pygame.font.SysFont('Arial', 20)
    font_small = pygame.font.SysFont('Arial', 15)

    pygame.draw.rect(surface=screen, color=DARK_GRAY, rect=(
        0, 0, (SCREEN_WIDTH // 4) + 10, (SCREEN_HEIGHT // 3) + 10))
    pygame.draw.rect(surface=screen, color=WHITE, rect=(
        0, 0, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 3))

    controls = ["r - reset", "space - sort", "c - change sorting algorithm"]
    for i in range(len(controls)):
        x = font_small.render(controls[i], 1, DARK_GRAY)
        screen.blit(x, (10, (i+1) * 20))


def bubble_sort(i, max_value, list):
    if i == max_value:
        return list
    for j in range(max_value):
        if list[j]["value"] > list[j+1]["value"]:
            list[j], list[j+1] = list[j+1], list[j]
    return list


def insetion_sort(i, max_value, list):

    key = list[i]
    j = i - 1
    while j >= 0 and key['value'] < list[j]['value']:
        list[j+1] = list[j]
        j -= 1
    list[j+1] = key
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
    sorted = False
    sorting_algorithm = "Bubble Sort"
    n = 0
    draw_list(list, screen)

    while running:
        screen.fill(BACKGROUND_COLOR)
        draw_list(list, screen)

        if sorting:
            if sorting_algorithm == "Bubble Sort":
                draw_label("Sorting", SCREEN_WIDTH/2,
                           35, WHITE, screen)
                list = bubble_sort(n, len(list)-1, list)
                n += 1
            elif sorting_algorithm == "Insertion Sort":
                draw_label("Sorting", SCREEN_WIDTH/2,
                           35, WHITE, screen)
                list = insetion_sort(n, len(list)-1, list)
                n += 1
        if n >= len(list):
            sorting = False
            sorted = True

        draw_controls(screen)
        draw_label(sorting_algorithm, 0 + SCREEN_WIDTH/2, 0, WHITE, screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type != pygame.KEYDOWN:
                continue
            if event.key == pygame.K_r:
                list = generate_random_list(LIST_SIZE, 100)
                sorted = False
                n = 0
            if event.key == pygame.K_SPACE and not sorted:
                sorting = True
            if event.key == pygame.K_c:
                if not sorting:
                    if sorting_algorithm == "Bubble Sort":
                        sorting_algorithm = "Insertion Sort"
                    else:
                        sorting_algorithm = "Bubble Sort"
        pygame.display.flip()
        clock.tick(CLOCK)
    pygame.quit()


if __name__ == "__main__":
    main()
