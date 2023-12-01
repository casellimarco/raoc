str_to_int = {"one":1, "two":2, "three":3, "four":4, "five":5,
              "six":6, "seven":7, "eight":8, "nine": 9}

total = 0
with open("input.txt", "r") as f:
    for r in f:
        for c in r:
            if c.isdigit():
                total += int(c)*10
                break
        for c in r[::-1]:
            if c.isdigit():
                total += int(c)
                break
print(1, total)

total = 0
with open("input.txt", "r") as f:
    for r in f:
        for i, c in enumerate(r):
            if c.isdigit():
                total += int(c)*10
                break
            found = False
            for k, v in str_to_int.items():
                if r[i:i+len(k)] == k:
                    total += v*10
                    found = True
                    break
            if found:
                break

        for i, c in enumerate(r[::-1]):
            if c.isdigit():
                total += int(c)
                break
            found = False
            for k, v in str_to_int.items():
                if r[len(r)-i-len(k):len(r)-i] == k:
                    total += v
                    found = True
                    break
            if found:
                break
print(2, total)