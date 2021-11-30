pub fn main() {
    let mut items: Vec<usize> = include_str!("../input.txt")
        .lines()
        .map(|i| i.parse().unwrap())
        .collect();

    for index in 0..items.len() {
        if index % 4 == 0 {
            if items[index] == 99 {
                println!("{}", items[0]);
                return;
            }
            if items[index] == 1 {
                items[items[index+3]] = items[index+1] + items[index+2];
            }
            if items[index] == 2 {
                items[items[index+3]] = items[index+1] * items[index+2];
            }
        }
    }
}

