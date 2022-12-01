fn main() {
    let elfs: Vec<Vec<usize>> = include_str!("../input.txt")
        .split("\n\n")
        .map(|elf| elf.lines().map(|i| i.parse().unwrap()).collect())
        .collect();
    let mut food: Vec<usize> = elfs.iter().map(|elf| elf.iter().sum()).collect();
    food.sort();
    let tot: usize = food.iter().rev().take(3).sum();
    println!("{}", tot);
}
