with open("input.txt", "r") as f:
    fishs = [int(i) for i in f.readline().rstrip().split(",")]

mapp = [0] * 9
for i in fishs:
    mapp[i] += 1


def fish_evol(time, mapp):
    for _ in range(time):
        mapp2 = []
        for i in range(0,9):
            mapp2.append(mapp[(i+1)%9])
            if i==6:
                mapp2[i] += mapp[0]
        print(mapp)
        mapp = mapp2
    return sum(mapp)


print(fish_evol(80, mapp))
print(fish_evol(256, mapp))
