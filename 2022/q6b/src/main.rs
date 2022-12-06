use std::collections::HashSet;
use std::iter::FromIterator;

fn main() {
    let messages: Vec<usize> = include_str!("../input.txt").lines()
        .map(|m| m.as_bytes().windows(14).enumerate().filter(
            |&(_, window)| 
            HashSet::<&u8>::from_iter(window.iter().clone()).len() == 14
        ).map(|(i, _)| i+14)).next().unwrap().collect();
    println!("{:?}", messages[0]);
}
