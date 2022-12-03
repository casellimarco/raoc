use std::collections::HashMap;

fn main() {

    let elf = HashMap::from([
        ("A X", 4),
        ("A Y", 8),
        ("A Z", 3),
        ("B X", 1),
        ("B Y", 5),
        ("B Z", 9),
        ("C X", 7),
        ("C Y", 2),
        ("C Z", 6),
    ]);
    let games: usize = include_str!("../input.txt")
        .lines()
        .map(|game| elf[game]).sum();
    println!("{:?}", games);
}
