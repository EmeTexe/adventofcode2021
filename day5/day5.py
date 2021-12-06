import numpy as np

all_points = []
maxx, maxy = 0,0
with open("input.txt", "r") as f:
    for line in f:
        all_points.append([tuple(int(i) for i in line.rstrip().split(" -> ")[0].split(",")), tuple(int(i) for i in line.rstrip().split(" -> ")[1].split(","))])
        maxx, maxy = max(maxx, all_points[-1][0][0], all_points[-1][1][0]), max(maxx, all_points[-1][0][1], all_points[-1][1][1])

# Part 1
vents = np.zeros((maxx+1, maxy+1))
for seg in all_points:
    x1,x2,y1,y2 = seg[0][0], seg[1][0], seg[0][1], seg[1][1]
    if x1 == x2:
        vents[x1,range(min(y1, y2), max(y1,y2)+1)] += 1
    elif y1 == y2:
        vents[range(min(x1, x2), max(x1,x2)+1), y1] += 1

print((vents>1).sum())

# Part 2
vents = np.zeros((maxx+1, maxy+1))
for seg in all_points:
    x1,x2,y1,y2 = seg[0][0], seg[1][0], seg[0][1], seg[1][1]
    if x1 == x2:
        vents[x1,range(min(y1, y2), max(y1,y2)+1)] += 1
    elif y1 == y2:
        vents[range(min(x1, x2), max(x1,x2)+1), y1] += 1
    else:
        # print(f"{x1}, {y1}, {x2}, {y2}")
        for i in range(max(x1, x2)-min(x1,x2)+1):
            x,y = x1+i if x1<x2 else x1-i, y1+i if y1<y2 else y1-i
            # print((x,y))
            vents[x,y] += 1

# print(vents)
print((vents>1).sum())





