pub fn main() {
    let items: Vec<i32> = include_str!("../input.txt")
        .lines()
        .map(|i| i.parse().unwrap())
        .collect();

    let mut tot = 0;
    for a in &items {
        let mut b = a/3 - 2;
        while b>0 {
            tot += b;
            b = b/3 - 2;
        }
    }
    println!("{}", tot);
    // return;
}
