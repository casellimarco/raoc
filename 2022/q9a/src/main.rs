use std::collections::HashSet;

fn main() {
    let instructions: Vec<(char, i32)> = include_str!("../input.txt")
        .lines()
        .map(|instruction| instruction.split_once(' ').unwrap())
        .map(|x| (x.0.parse().unwrap(), x.1.parse().unwrap())).collect();
    let mut T: (i32, i32) = (0,0);
    let mut H: (i32, i32) = (0,0);
    let mut set = HashSet::from([T]);
    
    for (direction, length) in instructions {
        match direction {
            'U' => H.1 += length,
            'D' => H.1 -= length,
            'R' => H.0 += length,
            'L' => H.0 -= length,
            _ => panic!("Invalid direction"),
        }
        loop {
            let diff = (T.0-H.0, T.1-H.1);
            if diff.0.abs() < 2 && diff.1.abs() < 2 {
                break;
            }
            T.0 -= diff.0.signum();
            T.1 -= diff.1.signum();
            set.insert(T);
        }
    }
    println!("{:?}", set.len());
}
