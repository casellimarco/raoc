use std::ops::AddAssign;

struct Power {
    register: i32,
    cycle: i32,
    power: i32,
}

impl Power {
    fn new() -> Power {
        Power{ register:1, cycle:0, power:0}
    }   
}
impl AddAssign<i32> for Power {
    fn add_assign(&mut self, update: i32) {
        let frequency = 40;
        self.cycle += 1;
        if self.cycle % frequency == 20 {
            self.power += self.cycle * self.register;
        }
        self.register += update;
    }
}

fn main() {
    let mut p = Power::new();
    for line in include_str!("../input.txt").lines() {
        p+=0;
        if line.starts_with("addx") {
            p+=line[5..].parse().unwrap();
        }
    }
    println!("{}", p.power);
}
