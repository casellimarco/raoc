from collections import Counter

data = {}
with open('input.txt', 'r') as f:
    for i, line in enumerate(f):
        if i == 0:
            inp = line.strip()
        elif i == 1:
            continue
        else:
            a, b = line.strip().split(" -> ")
            data[a[0],a[1]]=b

pairs = Counter((inp[i], inp[i+1]) for i in range(len(inp)-1))
for _ in range(40):
    new_pairs = Counter()
    for k, v in pairs.items():
        if k not in data:
            new_pairs[k] += v
        else:
            new_element = data[k]
            new_pairs[k[0], new_element] += v
            new_pairs[new_element, k[1]] += v
    pairs = new_pairs

double_letters = Counter()
for k, v in pairs.items():
    double_letters[k[0]] += v
    double_letters[k[1]] += v

double_letters[inp[0]] += 1
double_letters[inp[1]] += 1
double_freq = double_letters.values()
print((max(double_freq) - min(double_freq))//2)
