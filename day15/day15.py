import numpy as np
cav = np.array([[int(i) for i in line.rstrip()] for line in open("test.txt")])


def find_best_path(cave:np.array):
    current_score, scores = 0,{(0,0):0}
    neighbors = [(-1,0),(0,-1),(1,0),(0,1)]




print(find_best_path(cav))
