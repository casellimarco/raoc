pub fn main() {
    println!(
        "{}",
        include_str!("../input.txt")
            .lines()
            .map(|i| i.parse::<usize>().unwrap())
            // .combinations(2)
            // .filter(|i| i.iter().sum::<usize>() == 2020)
            // .next()
            .map(|i| i / 3 - 2)
            .sum::<usize>()
    );
}
