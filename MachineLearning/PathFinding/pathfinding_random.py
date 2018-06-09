import matplotlib.pyplot as plt
from matplotlib import interactive
import random
import math
import time

start_time = time.time()

start_point = [80, 10]
target = [10, 90]
box_x = [0, 0, 100, 100, 0]
box_y = [100, 0, 0, 100, 100]
amount_per_generation = 50
timescale = 1
mutation_ratio = 1
updates = 240 * 1/timescale
Players = []
generations = 200
killzones = []


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
    def __init__(self, movement=[Vector(-90, 0) for _ in range(int(updates))]):
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
        self.fitness = 0

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

    def run(self, plot_collisions = False):
        self.collision = False
        for vector in self.movement:
            self.xhistory.append(self.xpos)
            self.yhistory.append(self.ypos)
            self.a_change(vector)
            self.update()
            if self.xpos > sorted(box_x)[-1] or self.xpos < 0 or self.ypos > sorted(box_y)[-1] or self.ypos < 0:
                self.collision = True
                if plot_collisions:
                    plt.scatter(self.xpos, self.ypos, color="red")
                break
        self.fitness = distance(start_point, target)/distance([self.xpos, self.ypos], target)


def distance(loc1, loc2):
    return ((loc2[0] - loc1[0]) ** 2 + (loc2[1] - loc1[1]) ** 2) ** 0.5


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


best = Player()

# while True:
#     Players = born(best)
#     for i in Players:
#         i.run()
#         pass
#     for i in Players:
#         plt.plot(i.xhistory, i.yhistory)
#     best.run()
#     plt.scatter(best.xhistory, best.yhistory)
#     plt.scatter(start_point[0], start_point[1])
#     print("Best fitness", best.fitness)
#     print("Best angles", [i.angle for i in best.movement])
#     print("Best sizes", [i.size for i in best.movement])
#     box(box_x, box_y)
#     plt.axis("equal")
#     plt.scatter(target[0], target[1], color="red")
#     print("Nowbest %s Best %s" % (sorted(Players, key=lambda x: x.fitness)[-1].fitness, best.fitness),
#           "\n ----------------------------------------------------------------------------")
#     plt.show()
#
#     if sorted(Players, key=lambda x: x.fitness)[-1].fitness > best.fitness:
#         best = sorted(Players, key=lambda x: x.fitness)[-1]

attempt = 0
best = Player()
while True:
    attempt += 1
    print(attempt)
    best.run()
    best = Player(movement=best.mutate())
    print(best.fitness)
    print([i.angle for i in best.movement])
    if best.fitness > 50:
        plt.plot(best.xhistory, best.yhistory)
        plt.show()
        break
#
# bests = []
# for i in range(generations):
#     Players = born(best)
#     print("Generation: ", i)
#     for i in Players:
#         i.run()
#     best.run()
#     # print("Best fitness", best.fitness)
#     # print("Best angles", [i.angle for i in best.movement])
#     # print("Best sizes", [i.size for i in best.movement])
#     # box(box_x, box_y)
#     # print("Nowbest %s Best %s" % (sorted(Players, key=lambda x: x.fitness)[-1].fitness, best.fitness),
#     #       "\n ----------------------------------------------------------------------------")
#     if sorted(Players, key=lambda x: x.fitness)[-1].fitness > best.fitness:
#         best = Player(movement=sorted(Players, key=lambda x: x.fitness)[-1].movement)
#
#     if best not in bests:
#         bests.append(best)
#
#
# plt.figure(2)
# solution = Player(movement=bests[-1].movement)
# solution.run()
# plt.scatter(start_point[0], start_point[1])
# plt.scatter(target[0], target[1])
# plt.plot(solution.xhistory, solution.yhistory, color="red")
# box(box_x,box_y)
#
# plt.figure(1)
# for i in bests:
#     i.run(plot_collisions=True)
#     plt.plot(i.xhistory, i.yhistory)
# box(box_x, box_y)
# print(-1*start_time + time.time())
#
#
# plt.figure(3)
# [i.run() for i in bests]
# plt.plot([i.fitness for i in bests])
#
# plt.show()