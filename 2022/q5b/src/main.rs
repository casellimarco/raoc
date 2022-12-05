use std::collections::HashMap;
use regex::Regex;


fn main() {
    let crates_and_ins: Vec<&str> = include_str!("../input.txt").split("\n\n").collect();
    let [crates_str, instructions] = <[&str; 2]>::try_from(crates_and_ins).ok().unwrap();
    let mut crates: HashMap<usize, Vec<char>> = HashMap::new();
    for line in crates_str.lines() {
        if line.chars().nth(1).unwrap().is_numeric() {
            break;
        }
        for (i, char) in line.chars().enumerate().filter(|&(i, c)| i % 4 == 1 && c != ' ') {
            let index = (i-1)/4+1;
            crates.entry(index).or_insert(vec![]).push(char);
        }
    }
    for index in 1..(crates.len()+1) {
        crates.get_mut(&index).unwrap().reverse();
    }
    let re = Regex::new(r"move (\d.*) from (\d.*) to (\d.*)").unwrap();
    for instruction in instructions.lines() {
        let cap = re.captures(instruction).unwrap();
        let size: usize = cap[1].parse().unwrap();
        let from: usize = cap[2].parse().unwrap();
        let to: usize = cap[3].parse().unwrap();
        let mut to_move: Vec<char> = vec![];
        for _ in 0..size {
            to_move.push(crates.get_mut(&from).unwrap().pop().unwrap());
        }
        crates.get_mut(&to).unwrap().extend(to_move.iter().rev());  
    }
    let mut sol: Vec<&char> = vec![];
    for index in 1..(crates.len()+1) {
        sol.push(&crates.get(&index).unwrap().last().unwrap()); 
    }
    println!("{:?}", &sol.into_iter().collect::<String>());
}
