with open("input.txt", "r") as f:
    input = [l.strip() for l in f]


p5_to_c5 = {0:"0", 1:"1", 2:"2", 3:"=", 4:"-"}
c5_to_p5 = {"0":0, "1":1, "2":2, "=":-2, "-":-1}

def dec_to_c5(dec):
    out = ""
    while dec != 0:
        dec, r = divmod(dec, 5)
        out += str(p5_to_c5[r])
        if r in [3,4]:
            dec += 1
    return out[::-1]

def c5_to_dec(c5):
    out = 0
    for c in c5:
        out *= 5
        out += c5_to_p5[c]
    return out

print(dec_to_c5(sum(map(c5_to_dec, input))))