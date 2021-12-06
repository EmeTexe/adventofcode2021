import numpy as np

all_bingo = []
current_bingo = []
with open("input.txt", "r") as f:
    for i, line in enumerate(f):
        if i == 0:
            numbers = [int(i) for i in line.split(",")]
        elif line.rstrip() == "":
            if i>2:
                all_bingo.append(np.array(current_bingo))
                current_bingo = []
        else:
            current_bingo.append([int(i) for i in line.rstrip().split()])

# Part 1
# print(all_bingo)
for n in numbers:
    # print(n)
    current_bingos = []
    for j, bingo in enumerate(all_bingo):
        bingo = np.where(bingo == n, -1, bingo)
        if any(t == -5 for t in bingo.sum(axis=0)) or any(t == -5 for t in bingo.sum(axis=1)):
            bingo = np.where(bingo == -1, 0, bingo)
            print(bingo)
            print(sum(bingo.sum(axis=0)) * n)
            break
        current_bingos.append(bingo)
    else:
        all_bingo = current_bingos
        # print(all_bingo)
        continue
    break

# Part 2
# print(all_bingo)
won = []
for n in numbers:
    # print(n)
    current_bingos = []
    for j, bingo in enumerate(all_bingo):
        bingo = np.where(bingo == n, -1, bingo)
        if any(t == -5 for t in bingo.sum(axis=0)) or any(t == -5 for t in bingo.sum(axis=1)):
            bingo = np.where(bingo == -1, 0, bingo)
            won.append((bingo, n))
            # print(bingo)
            # print(sum(bingo.sum(axis=0)) * n)
            continue
        current_bingos.append(bingo)
    all_bingo = current_bingos
    # print(all_bingo)

print(sum(won[-1][0].sum(axis=0)) * won[-1][1])