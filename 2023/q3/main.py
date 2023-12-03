import numpy as np
import cv2

img = []
with open("input.txt", "r") as f:
    for r in f:
        img.append(list(r.strip()))
img = np.array(img)

non_symbols = list(".0123456789")
symbols = ~np.isin(img, non_symbols)
close_symbols = cv2.dilate(symbols.astype(np.uint8), kernel=np.ones((3, 3))).astype(bool)

def get_close_values(img, close_symbols):
    tot = []
    for i, r in enumerate(img):
        number = ""
        close_to_symbol = False
        for j, v in enumerate(r):
            if v.isdigit():
                close_to_symbol |= close_symbols[i, j] 
                number += v
            else:
                if number and close_to_symbol:
                    tot.append(int(number))
                number = ""
                close_to_symbol = False
        if number and close_to_symbol:
            tot.append(int(number))
    return tot
print(1, sum(get_close_values(img, close_symbols)))

gear_coordinates = np.where(img == "*")

tot = 0
for i,j in np.array(gear_coordinates).T:
    i0, i1 = np.clip([i-1, i+2], 0, img.shape[0])
    j0, j1 = np.clip([j-1, j+2], 0, img.shape[1])
    window = img[i0:i1]   
    close_gear = np.zeros_like(window, dtype=bool)
    close_gear[:, j0:j1] = True
    values = get_close_values(window, close_gear)
    if len(values) == 2:
        tot += values[0] * values[1]

print(2, tot)
    


