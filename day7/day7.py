import numpy as np
import time
with open("input.txt", "r") as f:
    crabs = np.array([int(i) for i in f.readline().rstrip().split(",")])

# part 1 :
# The best alignment is the median of the crabs, which will allow crabs to spend the least possible fuel
print(sum(abs(crabs - np.median(crabs))))

t1 = time.time()
# Part 2
# Use dichotomic search between leftest and rightest crab, hoping that it only has 1 local minimum
up, down = max(crabs), min(crabs)
value_up, value_down = sum([abs(i-up) * (abs(i-up)+1) / 2 for i in crabs]), sum([abs(i-down) * (abs(i-down)+1) / 2 for i in crabs])
while up-down>1:
    if value_up > value_down:
        up = np.ceil(up-(up-down)/2)
        value_up = sum([abs(i-up) * (abs(i-up)+1) / 2 for i in crabs])
    elif value_down > value_up:
        down = np.floor(down+(up-down)/2)
        value_down = sum([abs(i-down) * (abs(i-down)+1) / 2 for i in crabs])
print(min([value_up, value_down]))

dicho = time.time()-t1
t2 = time.time()
# One line, the least optimized
# find position which minimize fuel consumption
# print(np.argmin([sum([abs(i-j) * abs(i-j+1) / 2 for i in crabs]) for j in range(min(crabs), max(crabs)+1)])+min(crabs))
# Find minimal fuel consumption
print(np.min([sum([abs(i-j) * (abs(i-j)+1) / 2 for i in crabs]) for j in range(min(crabs), max(crabs)+1)]))

full = time.time()-t2
print(f"time for dicho: {dicho}\ntime for full: {full}\ndicho is {round(full/dicho)} times more optimized")

# print(np.mean(crabs))
# print(sum(abs(crabs - np.mean(crabs))))


