# Part 1
print(sum(sum(len(i) in [2,3,4,7] for i in line.rstrip().split(" | ")[1].split(" ")) for line in open("input.txt", "r")))

# Part 2
print(sum([int(''.join([str({k[0][0]: 1, k[0][1]: 7, k[0][2]: 4, k[0][-1]: 8, next(x for x in k[0][3:6] if 0 not in [c in x for c in k[0][0]]): 3, next(x for x in k[0][3:6] if sum([c in x for c in k[0][2]]) == 2): 2, next(x for x in k[0][3:6] if (sum([c in x for c in k[0][2]]) == 3 and 0 in [c in x for c in k[0][0]])): 5, next(x for x in k[0][6:9] if 0 not in [c in x for c in k[0][1]] and 0 not in [c in x for c in k[0][2]]): 9, next(x for x in k[0][6:9] if 0 in [c in x for c in k[0][1]]): 6, next(x for x in k[0][6:9] if 0 not in [c in x for c in k[0][1]] and 0 in [c in x for c in k[0][2]]): 0}[l]) for l in k[1]])) for k in [[sorted(["".join(sorted(i)) for i in line.rstrip().split(" | ")[0].split(" ")], key=len), ["".join(sorted(j)) for j in line.rstrip().split(" | ")[1].split(" ")]] for line in open("input.txt", "r")]]))


