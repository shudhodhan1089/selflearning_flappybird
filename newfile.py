def get_index(pipes,birds):
    bird_X = birds[0].x

    list_distance = [pipes.X+pipes.IMG_WIDTH-bird_X for pipe in pipes]
    index = list_distance.index(min(i for i in list_distance if i>=0))

    return index

import neat 

def main(genomes,config):
    global generation, SCREEN
    screen = SCREEN
    generation = generation + 1
    score = 0
    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()

    floor = FLoor(floor_starting_y_position)
    pipes