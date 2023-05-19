import pygame, sys, random, time

# setup
pygame.init()
clock = pygame.time.Clock()
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('firework particle effect thing')

# location, velocity, timer
particles = []
particles1 = []
particles2 = []

def particle(particles, colour, angle, size_lower, size_upper, gravity):
    particles.append([[mx, my], [random.randint(0, 20)/10 + angle, -3], random.randint(size_lower, size_upper)])
    for particle in particles:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 0.035
        particle[1][1] += gravity
        pygame.draw.circle(screen, colour, (int(particle[0][0]), int(particle[0][1])), int(particle[2]))
        if particle[2] <= 0:
            particles.remove(particle)

i, j, k = 0, 1, 2 # colours
a_one, a_two, a_three = -1.5, - 1, - 0.5 # angle of emission
sl_one, sl_two, sl_three = 4, 4, 4 # smallest size
su_one, su_two, su_three = 6, 6, 6 # largest size
g_one, g_two, g_three = 0.03, 0.03, 0.03
time.sleep(3)
while True:
    screen.fill((0, 0, 0))
    mx, my = pygame.mouse.get_pos()

    # prime number of colours only
    colours = [pygame.Color('#eb4034'),
                pygame.Color('#1ab3eb'),
                pygame.Color('#ffffff'),
                pygame.Color('#72f7e1'),
                pygame.Color('#ff00cc'),
                pygame.Color('#f3ff05'),
                pygame.Color('#3f05ff'),
                pygame.Color('#ff9305'),
                pygame.Color('#05ff65'), 
                pygame.Color('#d105ff'),
                pygame.Color('#05ffd5')
]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        keys = pygame.key.get_pressed()

        # reset particl settings
        if keys[pygame.K_r]:
            if keys[pygame.K_1]:
                i = 0
                a_one = -1.5
                sl_one = 4
                su_one = 6
                g_one = 0.03
            if keys[pygame.K_2]:
                j = 1
                a_two = -1
                sl_two = 4
                su_two = 6
                g_two = 0.03
            if keys[pygame.K_3]:
                k = 2
                a_three = -0.5
                sl_three = 4
                su_three = 6
                g_three = 0.03

        # colour control
        if keys[pygame.K_c] and keys[pygame.K_1]:
            i += 1
        if keys[pygame.K_c] and keys[pygame.K_2]:
            j += 1
        if keys[pygame.K_c] and keys[pygame.K_3]:
            k += 1
        
        # angle control
        if keys[pygame.K_LSHIFT] and keys[pygame.K_1]:
            if keys[pygame.K_LEFT]:
                a_one -= 0.1
            if keys[pygame.K_RIGHT]:
                a_one += 0.1
        if keys[pygame.K_LSHIFT] and keys[pygame.K_2]:
            if keys[pygame.K_LEFT]:
                a_two -= 0.1
            if keys[pygame.K_RIGHT]:
                a_two += 0.1
        if keys[pygame.K_LSHIFT] and keys[pygame.K_3]:
            if keys[pygame.K_LEFT]:
                a_three -= 0.1
            if keys[pygame.K_RIGHT]:
                a_three += 0.1

        # particle size control
        if keys[pygame.K_d] and keys[pygame.K_1]:
            if keys[pygame.K_UP]:
                su_one += 1
                sl_one += 1
            if keys[pygame.K_DOWN]:
                su_one -= 1
                sl_one -= 1
        if keys[pygame.K_d] and keys[pygame.K_2]:
            if keys[pygame.K_UP]:
                su_two += 1
                sl_two += 1
            if keys[pygame.K_DOWN]:
                su_two -= 1
                sl_two -= 1
        if keys[pygame.K_d] and keys[pygame.K_3]:
            if keys[pygame.K_UP]:
                su_three += 1
                sl_three += 1
            if keys[pygame.K_DOWN]:
                su_three -= 1
                sl_three -= 1
        
        # particle gravity control
        if keys[pygame.K_g] and keys[pygame.K_1]:
            if keys[pygame.K_UP]:
                g_one += 0.01
            if keys[pygame.K_DOWN]:
                g_one -= 0.01
        if keys[pygame.K_g] and keys[pygame.K_2]:
            if keys[pygame.K_UP]:
                g_two += 0.01
            if keys[pygame.K_DOWN]:
                g_two -= 0.01
        if keys[pygame.K_g] and keys[pygame.K_3]:
            if keys[pygame.K_UP]:
                g_three += 0.01
            if keys[pygame.K_DOWN]:
                g_three -= 0.01
                
    particle(particles, colours[i % len(colours)], a_one, sl_one, su_one, g_one)
    particle(particles1, colours[j % len(colours)], a_two, sl_two, su_two, g_two)
    particle(particles2, colours[k % len(colours)], a_three, sl_three, su_three, g_three)
                

    pygame.display.update()
    clock.tick(60)