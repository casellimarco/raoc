pub fn main() {
    let mut items: Vec<usize> = include_str!("../input.txt")
        .trim()
        .split(",")
        .map(|i| i.parse().unwrap())
        .collect();

    items[1] = 12;
    items[2] = 2;
    for index in 0..items.len() {
        if index % 4 == 0 {
            match items[index] {
                99 => {
                    println!("{}", items[0]);
                    return
                }
                1 => {
                let i = items[index+3];
                items[i] = items[items[index+1]] + items[items[index+2]];
                }
                2 => {
                let i = items[index+3];
                items[i] = items[items[index+1]] * items[items[index+2]];
                }
                _ => panic!(),
            }
        }
    }
}

