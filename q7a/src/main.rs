pub fn main() {
    let mut crabs:Vec<i32> = include_str!("../input.txt")
        .trim()
        .split(",")
        .map(|i| i.parse().unwrap())
        .collect();
    let median_index = crabs.len()/2;
    crabs.select_nth_unstable(median_index);
    let median = crabs[median_index];
    let fuel:i32 = crabs.iter().map(|c| (c-median).abs()).sum();
    println!("{:?}", fuel );
}
