import pygame, sys, random

# setup
pygame.init()
clock = pygame.time.Clock()
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('firework particle effect things')

# location, velocity, timer
particles = []
particles1 = []
particles2 = []

while True:
    screen.fill((0, 0, 0))
    mx, my = pygame.mouse.get_pos()

    particles.append([[mx, my], [random.randint(0, 20)/10 - 1.5, -3], random.randint(4, 6)])
    for particle in particles:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 0.035
        particle[1][1] += 0.03
        pygame.draw.circle(screen, pygame.Color('#eb4034'), (int(particle[0][0]), int(particle[0][1])), int(particle[2]))
        if particle[2] <= 0:
            particles.remove(particle)
    
    particles1.append([[mx, my], [random.randint(0, 20)/10 - 1, -3], random.randint(4, 6)])
    for particle in particles1:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 0.035
        particle[1][1] += 0.03
        pygame.draw.circle(screen, pygame.Color('#1ab3eb'), (int(particle[0][0]), int(particle[0][1])), int(particle[2]))
        if particle[2] <= 0:
            particles1.remove(particle)
    
    particles2.append([[mx, my], [random.randint(0, 20)/10 - 0.5, -3], random.randint(4, 6)])
    for particle in particles2:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 0.035
        particle[1][1] += 0.03
        pygame.draw.circle(screen, pygame.Color('#ffffff'), (int(particle[0][0]), int(particle[0][1])), int(particle[2]))
        if particle[2] <= 0:
            particles2.remove(particle)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)