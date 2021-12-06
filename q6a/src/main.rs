fn main() {
    let fishes: Vec<usize> = include_str!("../input.txt")
        .trim()
        .split(",")
        .map(|i| i.parse().unwrap())
        .collect();
    let mut jf = vec![0;9];
    for fish in fishes {
        jf[fish]+=1;
    }
    let days:usize = 80;
    for d in 0..days {
        jf[(7+d)%9] += jf[d%9];
    }
    println!("{:?}", jf.iter().sum::<usize>());

}
