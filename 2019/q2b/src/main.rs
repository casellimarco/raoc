pub fn check(mut items: Vec<usize>) -> usize {
    for index in 0..items.len() {
        if index % 4 == 0 {
            match items[index] {
                99 => return items[0],
                1 => {
                let i = items[index+3];
                items[i] = items[items[index+1]] + items[items[index+2]];
                }
                2 => {
                let i = items[index+3];
                items[i] = items[items[index+1]] * items[items[index+2]];
                }
                _ => panic!("{}", items[index]),
            }
        }
    }
    panic!()
}

pub fn main() {
    let originals: Vec<usize> = include_str!("../input.txt")
        .trim()
        .split(",")
        .map(|i| i.parse().unwrap())
        .collect();

    for verb in 0..100 {
        for noun in 0..100 {
            let mut items = originals.clone();
            items[1] = verb;
            items[2] = noun;
            if check(items) == 19690720 {
                println!("{}", verb*100 + noun);
                return
            }
        }
    }
}

