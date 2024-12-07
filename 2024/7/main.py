import re

from aocd import data
from dataclasses import dataclass


@dataclass
class Calibration:
    target: int
    values: list[int]
    part2: bool = False

    def check(self):
        if len(self.values) == 1:
            return self.target == self.values[0]
        if self.values[0] > self.target:
            return False
        a, b, *tail = self.values
        cal_sum = Calibration(self.target, [a+b, *tail], self.part2)
        cal_prod = Calibration(self.target, [a*b, *tail], self.part2)
        output = cal_sum.check() or cal_prod.check() 
        if self.part2:
            cal_con = Calibration(self.target, [int(str(a)+str(b)), *tail], self.part2)
            output |= cal_con.check()
        return output

    
part1 = 0
part2 = 0

for calibration_str in data.splitlines():
    target, *values = list(map(int, re.split(": | ", calibration_str)))
    calibration = Calibration(target, values)
    if calibration.check():
        part1 += calibration.target
    calibration.part2 = True
    if calibration.check():
        part2 += calibration.target
        
print(1, part1)
print(2, part2)
    