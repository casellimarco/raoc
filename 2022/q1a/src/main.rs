fn main() {
    let elfs: Vec<Vec<usize>> = include_str!("../input.txt")
        .split("\n\n")
        .map(|elf| elf.lines().map(|i| i.parse().unwrap()).collect())
        .collect();
    let food: Vec<usize> = elfs.iter().map(|elf| elf.iter().sum()).collect();
    println!("{}",food.iter().max().unwrap());
}
