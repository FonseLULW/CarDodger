import pygame
import sys
import random
#random for random car obstacles

pygame.init()
# ^^ initialize game

#--variables--
window_size = (500, 500)
#--/variables/--

screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Dodge the Cars")
clock = pygame.time.Clock()
font = pygame.font.SysFont('comicsans', 74, True)
bg_surface = pygame.image.load('purplebg.png').convert()
player_x = 5
player_y = 265
player_size_x = 75
player_size_y = 40
# vv load in pics vv
road = pygame.image.load('ROAD.png').convert()
moon = pygame.image.load('moon.png').convert_alpha()
stars = pygame.image.load('stars.png').convert_alpha()
# road ^ || player v
playercar = pygame.image.load('carplayer.png').convert_alpha()
# vvv cars vvvv
car1 = pygame.image.load('cars/car1_c.png').convert_alpha()
car2 = pygame.image.load('cars/car2_c.png').convert_alpha()
car3 = pygame.image.load('cars/car3_c.png').convert_alpha()
car4 = pygame.image.load('cars/car4_c.png').convert_alpha()
car5 = pygame.image.load('cars/car5_c.png').convert_alpha()
car6 = pygame.image.load('cars/car6_c.png').convert_alpha()
car7 = pygame.image.load('cars/car7_c.png').convert_alpha()
car8 = pygame.image.load('cars/car8_c.png').convert_alpha()
car9 = pygame.image.load('cars/car9_c.png').convert_alpha()
car10 = pygame.image.load('cars/car10_c.png').convert_alpha()
car11 = pygame.image.load('cars/car11_c.png').convert_alpha()
pcar1 = pygame.image.load('cars/policecar1_c.png').convert_alpha()
pcar2 = pygame.image.load('cars/policecar2_c.png').convert_alpha()
van = pygame.image.load('cars/van_c.png').convert_alpha()
taxi = pygame.image.load('cars/taxi_c.png').convert_alpha()
truck1 = pygame.image.load('cars/truck_c.png')
truck2 = pygame.image.load('cars/redtruck_c.png')
# ^^ load in pics ^^ || vv transform pics vv
gameroad = pygame.transform.scale(road, (500, 300))
moon = pygame.transform.scale(moon, (80, 80))
stars = pygame.transform.scale(stars, (100, 70))
# road ^ || player v
player = pygame.transform.scale(playercar, (player_size_x, player_size_y))
# vvv cars vvvv
car1 = pygame.transform.scale(car1, (75, 40))
car2 = pygame.transform.scale(car2, (75, 40))
car3 = pygame.transform.scale(car3, (75, 40))
car4 = pygame.transform.scale(car4, (75, 40))
car5 = pygame.transform.scale(car5, (75, 40))
car6 = pygame.transform.scale(car6, (75, 40))
car7 = pygame.transform.scale(car7, (75, 40))
car8 = pygame.transform.scale(car8, (75, 40))
car9 = pygame.transform.scale(car9, (75, 40))
car10 = pygame.transform.scale(car10, (75, 40))
car11 = pygame.transform.scale(car11, (75, 40))
pcar1 = pygame.transform.scale(pcar1, (75, 40))
pcar2 = pygame.transform.scale(pcar2, (75, 40))
van = pygame.transform.scale(van, (75, 40))
taxi = pygame.transform.scale(taxi, (75, 40))
truck1 = pygame.transform.scale(truck1, (180, 40))
truck2 = pygame.transform.scale(truck2, (180, 40))
# ^^ transform pics ^^ || vv put pics in place vv ||
road_rect = gameroad.get_rect(center=(250, 250))
player_rect = playercar.get_rect(topleft=(player_x, player_y))
# ^^ put pics in place ^^
player_hitbox = [player_x, player_y, 75, 40]


# ^^ set up game | vv functions
class thecars:
    def __init__(self, car_used, x, y, vel):
        self.x = x
        self.y = y
        self.car_used = car_used
        self.vel = vel
        self.to_display = self.car_used
        if self.car_used in trucks:
            self.hitbox = [self.x, self.y, 180, 40]
        else:
            self.hitbox = [self.x, self.y, 75, 40]
        if self.y == 265 or self.y == 340:  #bottom lanes#
            self.to_display = pygame.transform.flip(self.car_used, True, False)

    def draw(self):
        screen.blit(self.to_display, (self.x, self.y))
        if self.x == 250:
            global spawn
            spawn = True

    def move(self):
        global cars, car_num, car_list, car_lanes, cars2nd, veloc, rand_lane, trucks
        if self.x == -190:
            if car.x == -190:
                cars.pop(0)
                car_num = random.randint(1, 3)
                if car_num == 1:
                    cars = [
                        thecars(random.choice(car_list), 501,
                                random.choice(car_lanes), veloc)
                    ]
                elif car_num == 2:
                    rand_lane.append(random.choice(car_lanes))
                    car_lanes.remove(rand_lane[0])
                    cars = [
                        thecars(random.choice(car_list), 501, rand_lane[0],
                                veloc),
                        thecars(random.choice(car_list), 501,
                                random.choice(car_lanes), veloc)
                    ]
                    rand_lane = []
                    car_lanes = [120, 190, 265, 340]
                else:
                    rand_lane.append(random.choice(car_lanes))
                    car_lanes.remove(rand_lane[0])
                    rand_lane.append(random.choice(car_lanes))
                    car_lanes.remove(rand_lane[1])
                    cars = [
                        thecars(random.choice(car_list), 501, rand_lane[0],
                                veloc),
                        thecars(random.choice(car_list), 501, rand_lane[1],
                                veloc),
                        thecars(random.choice(car_list), 501,
                                random.choice(car_lanes), veloc)
                    ]
                    rand_lane = []
                    car_lanes = [120, 190, 265, 340]
            else:
                cars2nd.pop(0)
                car_num = random.randint(1, 3)
                if car_num == 1:
                    cars2nd = [
                        thecars(random.choice(car_list), 501,
                                random.choice(car_lanes), veloc)
                    ]
                elif car_num == 2:
                    rand_lane.append(random.choice(car_lanes))
                    car_lanes.remove(rand_lane[0])
                    cars2nd = [
                        thecars(random.choice(car_list), 501, rand_lane[0],
                                veloc),
                        thecars(random.choice(car_list), 501,
                                random.choice(car_lanes), veloc)
                    ]
                    rand_lane = []
                    car_lanes = [120, 190, 265, 340]
                else:
                    rand_lane.append(random.choice(car_lanes))
                    car_lanes.remove(rand_lane[0])
                    rand_lane.append(random.choice(car_lanes))
                    car_lanes.remove(rand_lane[1])
                    cars2nd = [
                        thecars(random.choice(car_list), 501, rand_lane[0],
                                veloc),
                        thecars(random.choice(car_list), 501, rand_lane[1],
                                veloc),
                        thecars(random.choice(car_list), 501,
                                random.choice(car_lanes), veloc)
                    ]
                    rand_lane = []
                    car_lanes = [120, 190, 265, 340]
        else:
            self.x += veloc
            if self.car_used in trucks:
                self.hitbox = [self.x, self.y, 180, 40]
            else:
                self.hitbox = [self.x, self.y, 75, 40]


spawn = False
car_lanes = [120, 190, 265, 340]
car_list = [
    car1, car2, car3, car4, car5, car6, car7, car8, car9, car10, car11, pcar1,
    pcar2, truck1, truck2, taxi, van
]
trucks = [truck1, truck2]
car_num = random.randint(1, 3)
cars = []
cars2nd = []
veloc = -1
rand_lane = []
if car_num == 1:
    cars = [
        thecars(random.choice(car_list), 501, random.choice(car_lanes), veloc)
    ]
    cars2nd = [
        thecars(random.choice(car_list), 501, random.choice(car_lanes), veloc)
    ]
elif car_num == 2:
    rand_lane.append(random.choice(car_lanes))
    car_lanes.remove(rand_lane[0])
    cars = [
        thecars(random.choice(car_list), 501, rand_lane[0], veloc),
        thecars(random.choice(car_list), 501, random.choice(car_lanes), veloc)
    ]
    rand_lane = []
    car_lanes = [120, 190, 265, 340]
    rand_lane.append(random.choice(car_lanes))
    car_lanes.remove(rand_lane[0])
    cars2nd = [
        thecars(random.choice(car_list), 501, rand_lane[0], veloc),
        thecars(random.choice(car_list), 501, random.choice(car_lanes), veloc)
    ]
    rand_lane = []
    car_lanes = [120, 190, 265, 340]
else:
    rand_lane.append(random.choice(car_lanes))
    car_lanes.remove(rand_lane[0])
    rand_lane.append(random.choice(car_lanes))
    car_lanes.remove(rand_lane[1])
    cars = [
        thecars(random.choice(car_list), 501, rand_lane[0], veloc),
        thecars(random.choice(car_list), 501, rand_lane[1], veloc),
        thecars(random.choice(car_list), 501, random.choice(car_lanes), veloc)
    ]
    rand_lane = []
    car_lanes = [120, 190, 265, 340]

    rand_lane.append(random.choice(car_lanes))
    car_lanes.remove(rand_lane[0])
    rand_lane.append(random.choice(car_lanes))
    car_lanes.remove(rand_lane[1])
    cars2nd = [
        thecars(random.choice(car_list), 501, rand_lane[0], veloc),
        thecars(random.choice(car_list), 501, rand_lane[1], veloc),
        thecars(random.choice(car_list), 501, random.choice(car_lanes), veloc)
    ]
    rand_lane = []
    car_lanes = [120, 190, 265, 340]


def redrawGameWindow():
    global font, score, crash, crash2, cars, road_animate, animate, didspawn, pre_score, player_x, player_y, player_size_x, player_size_y, car_lanes, car_list, trucks, car_num, cars2nd, veloc, rand_lane
    font = pygame.font.SysFont('comicsans', 72, True)
    screen.blit(bg_surface, (0, 0))

    screen.blit(stars, (0, 0))
    screen.blit(stars, (0, 70))
    screen.blit(stars, (100, -30))
    screen.blit(stars, (100, 40))
    screen.blit(stars, (200, -10))
    screen.blit(stars, (200, 60))
    screen.blit(stars, (300, 0))
    screen.blit(stars, (300, 70))
    screen.blit(stars, (400, -24))
    screen.blit(stars, (400, 46))

    screen.blit(moon, (404, 4.8))

    screen.blit(road, road_rect)
    screen.blit(player, player_rect)
    game_score = font.render("Score: " + str(score), True, (250, 250, 250))
    screen.blit(game_score, (3, 420))

    if score > 500:
        font = pygame.font.SysFont('comicsans', 32, True)
        title = font.render("GOOD", True, (250, 250, 250))
        title2 = font.render("JOB!", True, (250, 250, 250))
        text = 420
        screen.blit(title, (303, text))
        screen.blit(title2, (303, text + 35))
    else:
        font = pygame.font.SysFont('comicsans', 32, True)
        title = font.render("Can you get", True, (250, 250, 250))
        title2 = font.render("500 points?", True, (250, 250, 250))
        text = 420
        screen.blit(title, (303, text))
        screen.blit(title2, (303, text + 35))
    font = pygame.font.SysFont('comicsans', 72, True)

    for car in cars:
        car.draw()

    global spawn
    if spawn == True:
        for car2nd in cars2nd:
            car2nd.draw()

    if crash == True:
        font = pygame.font.SysFont('comicsans', 120, False)
        gameover = font.render("GAME", True, (250, 0, 0))
        gameover2 = font.render("OVER!", True, (250, 0, 0))
        screen.blit(gameover, (250 - 120, 250 - 120))
        screen.blit(gameover2, (250 - 120, 320 - 120))
        crash2 = True

    pygame.display.update()
    #^^ display changes

    if crash == True and crash2 == True:
        pygame.time.delay(3000)
        pygame.quit()
        sys.exit()


def animations():
    global animate, road_animate, road_rect
    road_animate += 1

    if road_animate == animate * 0.25:
        road_rect = gameroad.get_rect(center=(225, 250))
    if road_animate == animate * 0.5:
        road_rect = gameroad.get_rect(center=(218.75, 250))
    if road_animate == animate * 0.75:
        road_rect = gameroad.get_rect(center=(212.5, 250))
    if road_animate == animate * 1:
        road_rect = gameroad.get_rect(center=(206.25, 250))
    if road_animate == animate * 1.25:
        road_rect = gameroad.get_rect(center=(250, 250))
    if road_animate == animate * 1.5:
        road_rect = gameroad.get_rect(center=(243.75, 250))
    if road_animate == animate * 1.75:
        road_rect = gameroad.get_rect(center=(237.5, 250))
    if road_animate == animate * 2:
        road_rect = gameroad.get_rect(center=(231.25, 250))
        road_animate = 0


road_animate = 0
animate = 24
didspawn = False

score = 0
pre_score = 0
crash = False
crash2 = False
# ^^ functions | vv game proper
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_y > 110:
        player_y -= 3
        player_hitbox = [player_x, player_y, 75, 40]
    if keys[pygame.K_s] and player_y < 390 - player_size_y:
        player_y += 3
        player_hitbox = [player_x, player_y, 75, 40]
    if keys[pygame.K_a] and player_x > 0:
        player_x -= 3
        player_hitbox = [player_x, player_y, 75, 40]
    if keys[pygame.K_d] and player_x < 500 - player_size_x:
        player_x += 3
        player_hitbox = [player_x, player_y, 75, 40]

    player_rect = playercar.get_rect(topleft=(player_x, player_y))

    for car in cars:
        car.move()

        if car.x <= player_hitbox[
                0] <= car.x + car.hitbox[2] or car.x <= player_hitbox[
                    0] + player_hitbox[2] <= car.x + car.hitbox[2]:
            if car.y <= player_hitbox[
                    1] <= car.y + car.hitbox[3] or car.y <= player_hitbox[
                        1] + player_hitbox[3] <= car.y + car.hitbox[3]:
                crash = True

        if didspawn == True:
            if car2nd.x <= player_hitbox[0] <= car2nd.x + car2nd.hitbox[
                    2] or car2nd.x <= player_hitbox[0] + player_hitbox[
                        2] <= car2nd.x + car2nd.hitbox[2]:

                if car2nd.y <= player_hitbox[1] <= car2nd.y + car2nd.hitbox[
                        3] or car2nd.y <= player_hitbox[1] + player_hitbox[
                            3] <= car2nd.y + car2nd.hitbox[3]:
                    crash = True
    if spawn == True:
        didspawn = True
        for car2nd in cars2nd:
            car2nd.move()

    animations()
    redrawGameWindow()

    pre_score += 1
    if pre_score == 10:
        score += 1
        pre_score = 0

    clock.tick(120)
