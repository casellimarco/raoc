fn main() {
    let mut x: i64 = 0;
    let mut y: i64 = 0;
    for l in include_str!("../input.txt")
            .lines() {
        let dir_len: Vec<&str> = l.split(" ").collect();
        let dir = dir_len[0];
        let len: i64 = dir_len[1].parse().unwrap();
        match dir {
            "forward" => x+=len,
            "up" => y-=len,
            "down" => y+=len,
            _ => panic!(),
        }
    }
    println!("{}", x*y);
}
