with open("input.txt", "r") as f:
    inp = [line.rstrip().split(" ") for line in f]

# part 1
d,h = 0,0
for i in inp:
    if i[0] == "forward":
        h += int(i[1])
    else:
        d += int(i[1]) if i[0] == "down" else -int(i[1])
print(h*d)

# part 1
d,h,a = 0,0,0
for i in inp:
    if i[0] == "forward":
        h += int(i[1])
        d += a * int(i[1])
    else:
        a += int(i[1]) if i[0] == "down" else -int(i[1])
print(h*d)
