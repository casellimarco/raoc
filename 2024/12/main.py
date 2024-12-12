from aocd import data
import numpy as np
from skimage.measure import label

input = np.array([list(row) for row in data.split()])

part1 = 0
part2 = 0

for char in np.unique(input):
    char_mask = input == char
    labels, n_labels = label((char_mask * 255).astype(np.uint8), connectivity=1, background=0, return_num=True)
    for l in range(1, n_labels+1):
        mask = (labels == l).astype(int)
        area = mask.sum()
        mask = np.pad(mask, 1)
        perimeter = np.abs(np.diff(mask, axis=0)).sum() + np.abs(np.diff(mask, axis=1)).sum()
        perimeter2 = int((np.abs(np.diff(np.diff(mask, axis=0), axis=1)).sum() + np.abs(np.diff(np.diff(mask, axis=1),axis=0)).sum())/2)
        part1 += area * perimeter
        part2 += area * perimeter2
        
print(1, part1)
print(2, part2)