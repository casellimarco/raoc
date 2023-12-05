from collections import defaultdict

with open("input2.txt", "r") as f:
    entries = []
    for i, f in enumerate(f):
        if i == 0:
            seeds = list(map(int, f[7:].split()))
        if f == "\n":
            entries.append([])
            continue
        if not f[0].isdigit():
            continue
        entries[-1].append(list(map(int, f.strip().split())))

entries = [sorted(e, key = lambda x: x[1]) for e in entries]
def from_one_to_next(value, entry):
    for to, from_, range in entry:
        if from_<=value<from_+range:
            return to + value - from_
    return value

def all_entries(value, entries):
    for entry in entries:
        value = from_one_to_next(value, entry)
    return value

print(min(all_entries(seed, entries) for seed in seeds))

def glue_intervals(intervals):
    import pdb; pdb.set_trace()
    if len(intervals) == 0:
        return intervals
    intervals = [tuple(i) for i in intervals]
    intervals.sort()
    import pdb; pdb.set_trace()
    new_intervals = [list(intervals.pop(0))]
    for interval in intervals:
        if interval[0] <= new_intervals[-1][1]:
            new_intervals[-1][1] = max(interval[1], intervals[-1][1])
        else:
            new_intervals.append(list(interval))
    return new_intervals
    

def intervals_to_intervals(intervals, entry):
    new_intervals = []
    return_intervals = []
    for interval in intervals:
        for to, from_, range in entry:
            i_from, i_to = interval
            # tot 6 cases
            if i_to<from_: # 1 case
                return_intervals.append(interval)
            elif i_from>=from_+range: # 1 case 
                new_intervals.append(interval)
            elif from_<=i_to<from_+range:
                if i_from>=from_: # 1 case
                    return_intervals.append((to + i_from - from_, to + i_to - from_))
                else: # i_from<from_ # 1 case
                    return_intervals.extend(((i_from, from_ -1), (to, to + i_to - from_)))
            elif i_to>=from_+range:
                new_intervals.append((from_+range, i_to))
                if i_from<from_: # 1 case
                    return_intervals.extend(((i_from, from_ -1),(to, to + range -1)))
                else: # from_+range>i_from>=from_ # 1 case
                    return_intervals.append((to + i_from - from_, to + range -1))
        intervals = glue_intervals(new_intervals)
    return glue_intervals(new_intervals + return_intervals)

intervals = []
for i in range(len(seeds)//2):
    intervals.append((seeds[2*i], seeds[2*i+1]+seeds[2*i]-1))

min_max = []
min_ = int(1e120)
max_ = 0
for entry in entries[::-1]:
    min_ = min(min(e[1] for e in entry), min_)
    max_ = max(min(e[1]+e[2]-1 for e in entry), max_)
    min_max.append([min_, max_])

min_max = min_max[::-1]
# from tqdm import tqdm 
# for entry in tqdm(entries):
def filter_intervals(intervals, min, max):
    results = []
    new_intervals = []
    for i in intervals:
        if i[1] < min:
            results.append(i)
        elif i[0] <= max:
            new_intervals.append(i)
    return new_intervals, results            

results = []
for i, entry in enumerate(entries):
    # import pdb; pdb.set_trace()
    # intervals, new_results = filter_intervals(intervals, *min_max[i])
    # results.extend(new_results)
    intervals = intervals_to_intervals(intervals, entry)
    print(intervals)
    # intervals_to_intervals(intervals, entry)
    print(i, len(intervals))
print(min(i[0] for i in intervals))

# results.extend(intervals)
# print(min(i[0] for i in results))
