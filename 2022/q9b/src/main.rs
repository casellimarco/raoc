
use std::collections::HashSet;

fn main() {
    let instructions: Vec<(char, i32)> = include_str!("../input.txt")
        .lines()
        .map(|instruction| instruction.split_once(' ').unwrap())
        .map(|x| (x.0.parse().unwrap(), x.1.parse().unwrap())).collect();
    let T: (i32, i32) = (0,0);
    let mut rope = Vec::new();
    for _ in 0..10 {
        rope.push(T.clone());
    }
    let mut set = HashSet::from([T]);
    
    for (direction, length) in instructions {
        for _ in 0..length {
            match direction {
                'U' => rope[0].1 += 1,
                'D' => rope[0].1 -= 1,
                'R' => rope[0].0 += 1,
                'L' => rope[0].0 -= 1,
                _ => panic!("Invalid direction"),
            }
            for i in 1..10 {
                loop {
                    let diff = (rope[i].0-rope[i-1].0, rope[i].1-rope[i-1].1);
                    if diff.0.abs() < 2 && diff.1.abs() < 2 {
                        break;
                    }
                    rope[i].0 -= diff.0.signum();
                    rope[i].1 -= diff.1.signum();
                    if i == 9 {
                        set.insert(rope[9]);
                    }
                }
            }
        }
    }
    println!("{:?}", set.len());
}

