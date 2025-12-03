from aocd import data


def get_max(values, digits):
    if digits > 1:
        m = max(values[:-(digits-1)])
    else:
        m = max(values)
    return m, values[values.index(m)+1:]


def solve(digits):
    result=0
    for batch in data.splitlines():
        values = list(map(int, batch))
        score = 0
        for d in range(digits, 0, -1):
            m, values = get_max(values, d)
            score = score*10 + m
        result+=score
    return result
        
print(solve(2))
print(solve(12))
