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
    let days:usize = 256;
    for _ in 0..days {
        let nb = jf[0];
        for i in 1..9 {
            jf[i-1] = jf[i];
        }
        jf[6] += nb;
        jf[8] = nb;
    }
    println!("{:?}", jf.iter().sum::<usize>());

}
