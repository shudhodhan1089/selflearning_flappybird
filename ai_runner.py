import pygame
import sys
import os
import neat
import random

from settings import WIDTH,HEIGHT,pipe_size,pipe_gap,pipe_pair_sizes,ground_space
from bird import Bird
from pipe import Pipe

pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT + ground_space))
pygame.display.set_caption("Self-Learning Flappy Bird(NEAT)")

bg_img = pygame.image.load("assets/terrain/bg.png")
bg_img = pygame.transform.scale(bg_img,(WIDTH,HEIGHT))
ground_img = pygame.image.load("assets/terrain/ground.png")

def eval_genomes(genomes,config):
    nets = []
    ge = []
    birds = []

    for genome_id, genome in genomes:
        genome.fitness = 0
        net = neat.nn.FeedForwardNetwork.create(genome,config)
        nets.append(net)
        birds.append(Bird((WIDTH//2-pipe_size,HEIGHT//2-pipe_size),30))
        ge.append(genome)

    pipes = pygame.sprite.Group()
    pipe_pairs = []

    def add_pipe():
        pipe_pair_size = random.choice(pipe_pair_sizes)
        top_pipe_height , bottom_pipe_height = pipe_pair_size[0] * pipe_size ,pipe_pair_size[1]*pipe_size

        pipe_top = Pipe((WIDTH, 0 - (bottom_pipe_height+pipe_gap)),pipe_size,HEIGHT,True)
        pipe_bottom = Pipe((WIDTH,top_pipe_height+pipe_gap),pipe_size,HEIGHT,False)


        pipes.add(pipe_top,pipe_bottom)
        pipe_pairs.append({'top': pipe_top,'bottom':pipe_bottom,'passed':False})

    add_pipe()

    clock = pygame.time.Clock()
    ground_scroll = 0
    run = True

    while run and len(birds)>0:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

        screen.blit(bg_img,(0,0))

        pipe_ind = 0
        if len(birds)>0 and len(pipe_pairs)>0:
            if birds[0].rect.centerx > pipe_pairs[0]['top'].rect.right:
                if len(pipe_pairs) > 1:
                    pipe_ind = 1
        target_pair = pipe_pairs[pipe_ind] if pipe_pairs else None

        for x, bird in enumerate(birds):
            ge[x].fitness += 0.1

            bird.direction.y += 0.5
            bird.rect.y += bird.direction.y

            if target_pair:
                bird_y = bird.rect.y
                top_pipe_bottom_y = target_pair['top'].rect.bottom
                bottom_pipe_top_y = target_pair['bottom'].rect.top

                output = nets[x].activate((
                    bird_y,
                    abs(bird_y - top_pipe_bottom_y),
                    abs(bird_y - bottom_pipe_top_y)
                ))

                if output[0]>0.5:
                    bird.update(True)
                else:
                    bird.update(False)

        pipes.update(-6)

        ground_scroll += -6
        if abs(ground_scroll) > 35:
            ground_scroll = 0

        if len(pipe_pairs)>0:
            last_top = pipe_pairs[-1]['top']
            if last_top.rect.centerx <= (WIDTH//2) - pipe_size:
                add_pipe()

        for x in range(len(birds)-1,-1,-1):
            bird = birds[x]

            out_of_bounds = bird.rect.bottom >= HEIGHT or bird.rect.top <=0
            hit_pipe = pygame.sprite.spritecollideany(bird,pipes)

            if hit_pipe or out_of_bounds:
                ge[x].fitness -= 1
                birds.pop(x)
                nets.pop(x)
                ge.pop(x)


        if target_pair and not target_pair['passed'] and len(birds)>0:
            if birds[0].rect.centerx >= target_pair['top'].rect.centerx:
                target_pair['passed'] = True
                for g in ge:
                    g.fitness += 5

        if len(pipe_pairs) > 0 and pipe_pairs[0]['top'].rect.right<0:
            pipe_pairs.pop(0)

        pipes.draw(screen)
        for bird in birds:
            screen.blit(bird.image,bird.rect)

        screen.blit(ground_img,(ground_scroll,HEIGHT))
        pygame.display.update()

def run_neat(config_file):
    config = neat.Config(neat.DefaultGenome,neat.DefaultReproduction,
                         neat.DefaultSpeciesSet,neat.DefaultStagnation,
                         config_file)
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    
    # Run simulation for up to 50 generations
    winner = p.run(eval_genomes, 50)

if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    # Ensure this matches the name of the config file you saved earlier
    config_path = os.path.join(local_dir, "config-feedforward.txt") 
    run_neat(config_path)

