import numpy as np
from aocd import data


# Source - https://stackoverflow.com/a
# Posted by omotto, modified by community. See post 'Timeline' for change history
# Retrieved 2025-12-04, License - CC BY-SA 4.0

def convolution2d(image, kernel, bias):
    m, n = kernel.shape
    if (m == n):
        y, x = image.shape
        y = y - m + 1
        x = x - m + 1
        new_image = np.zeros((y,x))
        for i in range(y):
            for j in range(x):
                new_image[i][j] = np.sum(image[i:i+m, j:j+m]*kernel) + bias
    return new_image


a = np.array([list(l) for l in data.splitlines()]) == "@"
k = np.ones((3,3))
k[1,1] = 0
original = a.copy()
new = a.copy()
a = np.zeros_like(a)

first = True
while not np.all(a == new):
    a = new
    c = convolution2d(np.pad(a,1),k, 0)
    cond = (c < 4) & a
    new = a & ~cond
    if first:
        first = False
        print(original.sum() - new.sum())
print(original.sum() - new.sum())


