with open("input.txt", "r") as f:
    all_bits = [list(line.rstrip()) for line in f]

# Part 1
n_bits = all_bits[0]
for i in all_bits[1:]:
    n_bits = [int(i[n]) + int(n_bits[n]) for n in range(len(i))]

for n in range(len(n_bits)):
    n_bits[n] = "1" if n_bits[n] > len(all_bits) / 2 else "0"

print(int(''.join(n_bits), 2) * int(''.join([{"1": "0", "0": "1"}[str(i)] for i in n_bits]), 2))


# Part 2
def oxygen(l: list, pos: int = 0):
    if len(l) == 1:
        return l[0]
    l1, l0 = [], []
    for i in l:
        if i[pos] == "1":
            l1.append(i)
        else:
            l0.append(i)
    return oxygen(l0, pos+1) if len(l0) > len(l1) else oxygen(l1, pos+1)


def CO2(l: list, pos: int = 0):
    if len(l) == 1:
        return l[0]
    l1, l0 = [], []
    for i in l:
        if i[pos] == "1":
            l1.append(i)
        else:
            l0.append(i)
    return CO2(l1, pos+1) if len(l1) < len(l0) else CO2(l0, pos+1)


print(int(''.join(oxygen(all_bits)),2) * int(''.join(CO2(all_bits)),2))