import numpy as np
from scipy.ndimage.measurements import label

structure = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]])
with open('input.txt', 'r') as f:
    data = np.array([list(line.strip()) for line in f.readlines()]).astype(np.int)
labeled, _ = label(data<9, structure)
_, counts = np.unique(labeled, return_counts=True)
sizes = np.partition(counts[1:], -3)[-3:]
print(np.prod(sizes))