use std::collections::HashSet;

fn score(rusk: &str) -> u32 {
    let half = rusk.chars().count()/2;
    let part_1 = HashSet::<char>::from_iter(rusk.chars().take(half));
    let part_2 = HashSet::<char>::from_iter(rusk.chars().rev().take(half));
    let c = part_1.intersection(&part_2).next().unwrap();
    let a = score_char(*c);
    a
}

fn score_char(c: char) -> u32 {
    let score: u32 = c.to_lowercase().nth(0).unwrap().into();
    score -96 + (c.is_uppercase() as u32)*26
}

fn main() {
    let tot: u32 = include_str!("../input.txt")
        .lines()
        .map(|ruck| score(ruck)).sum();
    println!("{:?}", tot);
    }