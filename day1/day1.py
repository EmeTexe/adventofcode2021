with open("input.txt", "r") as f:
    depths = [int(line.rstrip()) for line in f]

n = 0
for i, d in enumerate(depths[1:-2]):
    d1, d2 = sum(depths[i:i+3]), sum(depths[i+1:i+4])
    n += 1 if d2>d1 else 0
    print(f"d1 : {d1}, d2 : {d2}, {n}")

print(n) # don't know why, but it always give an answer 1 below for my input
