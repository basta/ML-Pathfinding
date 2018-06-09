import matplotlib.pyplot as plt
import random
import math

start_point = [25, 10]
target = [25, 80]
box_x = [0, 0, 50, 50, 0]
box_y = [100, 0, 0, 100, 100]
amount_per_generation = 10
timescale = 1
mutation_ratio = 0.01
time = 30 * 1/timescale
Players = []


class Vector(object):
    def __init__(self, angle, size):
        self.size = size
        self.angle = angle
        self.rad = math.radians(self.angle)
        self.xysize = [math.cos(self.rad) * self.size, math.sin(self.rad) * self.size]

    def move(self, position):
        new_position = position
        new_position[0] += self.size * self.xydirection[0]
        new_position[1] += self.size * self.xydirection[1]
        return new_position

    def mutated(self, mutation_ration):
        pass
        #To Do


class Player(object):
    def __init__(self, movement=[Vector(0, 0) for _ in range(int(time))]):
        self.movement = movement
        self.position = start_point
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 0
        self.xpos = start_point[0]
        self.ypos = start_point[1]
        self.xhistory = []
        self.yhistory = []

    def a_change(self, vector):
        self.ax += vector.size * math.cos(vector.rad)
        self.ay += vector.size * math.sin(vector.rad)

    def mutate(self):
        mutated_movement = []
        for i in self.movement:
            angle_mutate = random.choice(range(-100, 101)) / 100
            size_mutate = random.choice(range(-100, 101)) / 100
            mutated_movement.append(
                Vector(
                    i.angle + angle_mutate * mutation_ratio * 360,
                    i.size + size_mutate * mutation_ratio
                       )
            )
        return mutated_movement

    def update(self):
        self.vx += self.ax * timescale
        self.vy += self.ay * timescale
        self.xpos += self.vx
        self.ypos += self.vy

    def run(self):
        for vector in self.movement:
            self.xhistory.append(self.xpos)
            self.yhistory.append(self.ypos)
            self.a_change(vector)
            self.update()


def distance(loc1, loc2):
    return ((loc2[0] - loc1[0])**2 + (loc2[1] - loc1 [1])**2)**0.5


def box(x, y):
    if sorted(x)[-1] > sorted(y)[-1]:
        scale = sorted(x)[-1]
    else:
        scale = sorted(y)[-1]
    plt.plot(x,y)
    plt.axis("equal")


def fittest(Player_list):
    best = Player()
    best_fitness = distance([Player_list[0].xpos, Player_list[1].ypos], target)

    for player in Player_list:
        if distance([player.xpos, player.ypos], target) < best_fitness:
            # print(distance([player.xpos, player.ypos], target))
            best_fitness = distance([player.xpos, player.ypos], target)
            best = player
    return best

def born(base):
    Players = []
    for _ in range(amount_per_generation):
        Players.append(Player(movement=base.movement))

    for i in Players:   i.movement = i.mutate()
    return Players


def a_change(vector):
    ax = vector.size * math.cos(vector.rad)
    ay = vector.size * math.sin(vector.rad)
    return[ax, ay]


def box(x, y):
    if sorted(x)[-1] > sorted(y)[-1]:
        scale = sorted(x)[-1]
    else:
        scale = sorted(y)[-1]
    plt.plot(x,y)
    plt.axis("equal")


def in_area(xbounds, ybounds):
    pass

plt.plot(range(1,10), color = "#00610f")
plt.plot(range(1,30), color = "#00610f")

plt.show()