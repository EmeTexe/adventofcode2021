with open("input.txt", "r") as f:
    poly = f.readline().rstrip()
    map_insert = {line.split(" -> ")[0]:line.split(" -> ")[1].rstrip() for line in f if " -> " in line}
    pairs = {i:0 for i in map_insert}
    for i in range(len(poly) - 1):
        pairs[poly[i] + poly[i + 1]] += 1
    print(pairs)
    print(poly)

# count = {i:poly.count(i) for i in poly}
for n in range(40):
    new_pairs = {i:0 for i in pairs}
    for p in pairs:
        new_pairs[p[0] + map_insert[p]] += pairs[p]
        new_pairs[map_insert[p] + p[1]] += pairs[p]
        # count[map_insert[p]] = pairs[p] if map_insert[p] not in count else count[map_insert[p]] + pairs[p]
    pairs = new_pairs

    if n == 9 or n == 39:
        count = {i: 0 for i in ''.join(pairs.keys())}
        for p in pairs:
            count[p[0]] += pairs[p]
        count[poly[-1]] += 1
        print(count)
        print(max(count.values()) - min(count.values()))







