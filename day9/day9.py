# Part 1 (un enfer)
print([sum([sum([n + 1 for j,n in enumerate(a) if not((m[i-1][j] <= n if i>0 else False) or (m[i+1][j] <= n if i<len(m)-1 else False) or (a[j-1] <= n if j>0 else False) or (a[j+1] <= n if j<len(a)-1 else False))]) for i,a in enumerate(m)]) for m in [[[int(n) for n in line.rstrip()] for line in open("input.txt")]]])
# for i,a in enumerate(m):
#     for j,n in enumerate(a):
#         if

def find_basin()



