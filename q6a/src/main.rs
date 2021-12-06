fn main() {
    let max_day:usize = 9;
    let mut counter = vec![0;max_day];
    for fish in include_str!("../input.txt")
        .trim()
        .split(",")
        .map(|i| i.parse::<usize>().unwrap()){
        counter[fish]+=1;
    }
    let days:usize = 256;
    for d in 0..days {
        counter[(7+d)%max_day] += counter[d%max_day];
    }
    println!("{:?}", counter.iter().sum::<usize>());
}
