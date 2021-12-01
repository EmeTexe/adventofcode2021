with open("input.txt", "r") as f:
    depths = [int(line.rstrip()) for line in f]

# part 1
n = 0
for i, d in enumerate(depths[1:]):
    n += d > depths[i]
print(n)

# part 2
n = 0
for i in range(len(depths[1:-2])):
    n += sum(depths[i+1:i+4]) > sum(depths[i:i+3])

print(n)