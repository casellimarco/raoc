use std::collections::HashSet;

fn score(rusks: Vec<&str>) -> u32 {
    let mut sets: Vec<HashSet<char>>= vec![];
    for rusk in rusks {
        sets.push(HashSet::<char>::from_iter(rusk.chars()));
    }
    let mut intersection = sets[0].clone();
    for other in sets[1..].iter() {
        intersection.retain(|e| other.contains(e));
    }
    let c = intersection.iter().next().unwrap();
    let a = score_char(*c);
    a
}

fn score_char(c: char) -> u32 {
    let score: u32 = c.to_lowercase().nth(0).unwrap().into();
    score -96 + (c.is_uppercase() as u32)*26
}

fn main() {
    let lines = include_str!("../input.txt").lines();
    let mut elfs: Vec<&str> = vec![];
    let mut tot: u32 = 0;
    for line in lines {
        elfs.push(line);
        if elfs.len() % 3 == 0 {
            tot += score(elfs);
            elfs = vec![];
        }
    }
    println!("{:?}", tot);
    }