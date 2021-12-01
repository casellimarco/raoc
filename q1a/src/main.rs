fn main() {
    let items: Vec<usize> = include_str!("../input.txt")
        .lines()
        .map(|i| i.parse().unwrap())
        .collect();
    let mut counter:usize = 0;
    let mut previous = usize::MAX;
    for this in items {
        if this > previous {
            counter += 1;
        }
        previous = this;
    }
    println!("{}",counter);
}
