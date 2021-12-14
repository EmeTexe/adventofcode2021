import numpy as np

# Part 1 and 2 same
def new_step(data):
    data += 1
    flashing = np.transpose(np.where(data > 9))
    flashed = []
    n_flash = 0
    # print(data)
    while len(flashing)>0:
        data[data > 9] = 0
        for f in flashing:
            n_flash += 1
            y,x = f[0], f[1]
            flashed.append((y, x))
            data[y-1 if y>0 else 0:y+2,x-1 if x>0 else 0:x+2] = [[i+1 if i>0 else i for i in j] for j in data[y-1 if y>0 else 0:y+2,x-1 if x>0 else 0:x+2]]
        # print(data)
        flashed.append([i for i in flashing])
        # print(flashed)
        flashing = np.transpose(np.where(data > 9))
    return data, n_flash


data = np.array([[int(i) for i in line.rstrip()] for line in open("input.txt")])
flash_total = 0
step = 0
while len(data)>0:
    step += 1
    # print(step)
    data, n_flash = new_step(data)
    flash_total += n_flash
    # print(data)
    # if step%10 == 0:
    #     print(step)
    #     print(data)
    if step == 100:
        print(flash_total)
    if np.all(data==0):
        print(step)
        break

