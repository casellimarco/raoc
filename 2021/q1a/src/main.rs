pub fn main() {
    let items: Vec<usize> = include_str!("../input.txt")
        .lines()
        .map(|i| i.parse().unwrap())
        .collect();
    let mut counter:usize = 0;
    for i in 0..items.len() - 1 {
        if items[i] < items[i+1] {
            counter += 1;
        }
    }
    println!("{}",counter);
}
