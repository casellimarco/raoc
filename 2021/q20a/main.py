import numpy as np
from scipy.signal import convolve2d

c_to_b = {"#":1, ".":0}
cb = lambda x: c_to_b[x]
image = []
with open("input.txt") as f:
    for i, line in enumerate(f):
        if i == 0:
            enhance = np.array(list(map(cb, line.strip())))
        elif i>1:
            image.append(list(map(cb, line.strip())))


image = np.array(image)

kernel = np.array([[2**0, 2**1, 2**2],
                   [2**3, 2**4, 2**5],
                   [2**6, 2**7, 2**8]])

fillvalue = 0
for i in range(50):
    grad = convolve2d(image, kernel, boundary='fill', mode='full', fillvalue=fillvalue)
    fillvalue = enhance[np.sum(fillvalue*kernel)]
    image = enhance[grad]

print(np.sum(image))