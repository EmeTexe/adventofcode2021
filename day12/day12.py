from copy import copy

inp = [line.rstrip().split("-") for line in open("input.txt", "r")]
mapping = {}
for i in inp:
    mapping[i[0]] = [i[1]] if i[0] not in mapping else mapping[i[0]] + [i[1]]
    mapping[i[1]] = [i[0]] if i[1] not in mapping else mapping[i[1]] + [i[0]]

print(mapping)


# Part 1
def find_all_paths(cave:str, cave_list, current_path=[], visited=[]):
    # print(f"cave: {cave}")
    if cave.islower() and cave in current_path:
        return visited
    current_path.append(cave)
    if cave == "end":
        # print(current_path)
        path = copy(current_path)
        visited.append(path)
        del current_path[-1]
        return visited
    for i in cave_list[cave]:
        # print(current_path)
        # print(f"{cave}:{i}")
        visited = find_all_paths(i, cave_list, current_path, visited)
    del current_path[-1]
    return visited


paths = find_all_paths("start", mapping)
# print(paths)
# for p in paths:
#     print('-'.join(p))

print(len(paths))


# Part 2
def find_all_paths2(cave:str, cave_list, current_path=[], visited=[]):
    # print(f"cave: {cave}")
    lower_path = [l for l in current_path if l.islower()]
    # print(lower_path)
    if (cave == "start" and cave in lower_path) or (cave in lower_path and any(lower_path.count(e)>1 for e in lower_path)):
        return visited
    current_path.append(cave)
    if cave == "end":
        # print(current_path)
        path = copy(current_path)
        visited.append(path)
        del current_path[-1]
        return visited
    for i in cave_list[cave]:
        # print(current_path)
        # print(f"{cave}:{i}")
        visited = find_all_paths2(i, cave_list, current_path, visited)
    del current_path[-1]
    return visited


paths2 = find_all_paths2("start", mapping)
# print(paths)
# for p in paths2:
#     print('-'.join(p))

print(len(paths2))
