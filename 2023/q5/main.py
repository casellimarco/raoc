with open("input.txt", "r") as f:
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

print(1, min(all_entries(seed, entries) for seed in seeds))

def glue_intervals(intervals):
    if len(intervals) == 0:
        return intervals
    intervals = [tuple(i) for i in intervals]
    intervals.sort()
    new_intervals = [list(intervals.pop(0))]
    for interval in intervals:
        if interval[0] <= new_intervals[-1][1]:
            new_intervals[-1][1] = max(interval[1], intervals[-1][1])
        else:
            new_intervals.append(list(interval))
    return new_intervals
    

def intervals_to_intervals(intervals, entry):
    return_intervals = []
    for to, from_, range in entry:
        new_intervals = []
        for interval in intervals:
            i_from, i_to = interval
            # tot 6 cases
            if i_to<from_: # 1 case, all interval out
                new_intervals.append(interval)
            elif i_from>=from_+range: # 1 case, all interval out 
                new_intervals.append(interval)
            elif from_<=i_to<from_+range:
                if i_from>=from_: # 1 case, all interval in
                    return_intervals.append((to + i_from - from_, to + i_to - from_))
                else: # i_from<from_ # 1 case, first half out, second in
                    new_intervals.append((i_from, from_ -1))
                    return_intervals.append((to, to + i_to - from_))
            elif i_to>=from_+range:
                new_intervals.append((from_+range, i_to)) # last part out
                if i_from<from_: # 1 case first part out, second in
                    new_intervals.append((i_from, from_ -1))
                    return_intervals.append((to, to + range -1))
                else: # from_+range>i_from>=from_ # 1 case, first part in
                    return_intervals.append((to + i_from - from_, to + range -1))
        intervals = glue_intervals(new_intervals)
    return glue_intervals(new_intervals + return_intervals)

intervals = []
for i in range(len(seeds)//2):
    intervals.append((seeds[2*i], seeds[2*i+1]+seeds[2*i]-1))

for i, entry in enumerate(entries):
    intervals = intervals_to_intervals(intervals, entry)
print(2, min(i[0] for i in intervals))
