use std::ops::AddAssign;

struct CRT {
    register: i32,
    cycle: i32,
    out: Vec<char>,
}

impl CRT {
    fn new() -> CRT {
        CRT{ register:1, cycle:0, out:vec![]}
    }   
}
impl AddAssign<i32> for CRT {
    fn add_assign(&mut self, update: i32) {
        let frequency = 40;
        if (self.cycle - self.register).abs() < 2 {
            self.out.push('#');
        }
        else{
            self.out.push(' ');
        }
        self.cycle += 1;
        self.cycle %= frequency;
        self.register += update;
    }
}

fn main() {
    let mut p = CRT::new();
    for line in include_str!("../input.txt").lines() {
        p+=0;
        if line.starts_with("addx") {
            p+=line[5..].parse().unwrap();
        }
    }
    for i in 0..6{
        println!("{:?}", &p.out[40*i..40*(i+1)].into_iter().collect::<String>());
    }
}
