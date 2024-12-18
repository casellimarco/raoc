from aocd import data
from dataclasses import dataclass, field

# data=\
# """Register A: 729
# Register B: 0
# Register C: 0

# Program: 0,1,5,4,3,0"""

# data=\
# """Register A: 2024
# Register B: 29
# Register C: 0

# Program: 1,7"""


@dataclass
class Computer:
    A: int
    B: int
    C: int
    program: list[int]
    out: list[int] = field(default_factory=list)
    pointer: int = 0

    def combo_operand(self, n):
        if n < 4:
            return n
        elif n == 4:
            return self.A
        elif n == 5:
            return self.B
        elif n == 6:
            return self.C
        raise ValueError(f"Invalid combo operand {n}")

    def run(self):
        while self.pointer < len(self.program):
            instruction, operand = self.program[self.pointer: self.pointer+2]
            getattr(self, f"ins{instruction}")(operand)
        return ",".join(list(map(str,self.out)))

    def ins0(self, operand):
        operand = self.combo_operand(operand)
        self.A = self.A // 2**operand
        self.pointer += 2
    
    def ins1(self, operand):
        self.B = self.B ^ operand
        self.pointer += 2
    
    def ins2(self, operand):
        self.B = self.combo_operand(operand) % 8
        self.pointer += 2
    
    def ins3(self, operand):
        if self.A == 0:
            self.pointer += 2
        else:
            self.pointer = operand

    def ins4(self, operand):
        self.B = self.B | self.C
        self.pointer += 2 
    
    def ins5(self, operand):
        self.out.append(self.combo_operand(operand) % 8)
        self.pointer += 2

    def ins6(self, operand):
        operand = self.combo_operand(operand)
        self.B = self.A // 2**operand
        self.pointer += 2
    
    def ins7(self, operand):
        operand = self.combo_operand(operand)
        self.C = self.A // 2**operand
        self.pointer += 2
    

register, program = data.split("\n\n")
register = [int(line.split(": ")[1]) for line in register.split("\n")]
program = list(map(int, program.split(": ")[1].split(",")))

computer = Computer(*register, program)

output = computer.run()
print(1, output)