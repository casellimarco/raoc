use std::collections::HashMap;

fn main() {

    let elf = HashMap::from([
        ("A X", 3),
        ("A Y", 4),
        ("A Z", 8),
        ("B X", 1),
        ("B Y", 5),
        ("B Z", 9),
        ("C X", 2),
        ("C Y", 6),
        ("C Z", 7),
    ]);
    let games: usize = include_str!("../input.txt")
        .lines()
        .map(|game| elf[game]).sum();
    println!("{:?}", games);
}
