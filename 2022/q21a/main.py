f = open("input.txt", "r").read()

f = f.replace(":", "=")

part = "b"

if part == "a":
    done = False
    while not done:
        done = True
        for l in f.splitlines():
            try:
               exec(l) 
            except:
                done = False

    print(int(root))

def all_cases(string):
    cases = [string]
    symbols = set("+-*/")
    if not symbols.intersection(string):
        return cases
    a,bc = string.split("= ")
    b, op, c = bc.split(" ")
    if op == "+":
        cases.extend([
            b + "= " + a + "-" + c,
            c + "= " + a + "-" + b,
        ])
    if op == "-":
        cases.extend([
            b + "= " + a + "+" + c,
            c + "= " + "-" + a + "+" + b,
        ])
    if op == "*":
        cases.extend([
            b + "= " + a + "/" + c,
            c + "= " + a + "/" + b,
        ])
    if op == "/":
        cases.extend([
            b + "= " + a + "*" + c,
            c + "= " + b + "/" + a,
        ])
    return cases



if part == "b":
    f = f.replace("humn= 870", "pass")
    f = f.replace("root= vtsj + tfjf", "tfjf = vtsj\nvtsj = tfjf")

    done = False
    while not done:
        done = True
        for l in f.splitlines():
            for c in all_cases(l):
                try:
                   exec(c) 
                except:
                    done = False

    print(int(humn))

