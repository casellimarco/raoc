pub fn main() {
    let crabs:Vec<i32> = include_str!("../input.txt")
        .trim()
        .split(",")
        .map(|i| i.parse().unwrap())
        .collect();
    let mean:i32 = crabs.iter().sum::<i32>()/crabs.len() as i32;
    let fuel:i32 = crabs.iter().map(|c| (c-mean).abs()).map(|d| d*(d+1)/2).sum();
    println!("{:?}", fuel );
}

