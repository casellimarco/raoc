fn score(line: &str) -> u32 {
    let v: Vec<u32> = line.split(&['-', ','][..]).map(|c| c.parse().unwrap()).collect();
    let [a_start, a_end, b_start, b_end] = <[u32; 4]>::try_from(v).ok().unwrap();
    !(a_end < b_start || a_start > b_end) as u32
}


fn main() {
    let tot: u32 = include_str!("../input.txt")
        .lines()
        .map(|line| score(line)).sum();
    println!("{:?}", tot);
}
