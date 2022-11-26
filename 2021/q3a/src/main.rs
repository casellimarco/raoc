pub fn main() {
    let mut a: Vec<Vec<u32>> = Vec::new();
    for l in include_str!("../input.txt")
            .lines() {
        a.push(l.chars().map(|i| i.to_digit(10).unwrap()).collect());

    }
    let mut c = vec![0; a[0].len()];
    for v in a.iter(){
        for (i,l) in v.iter().enumerate(){
            c[i] += l;
        }
    }
    let mut gamma=0;
    let mut eps=0;
    let len = a.len() as u32;
    for (p, i) in c.iter().enumerate(){
        let power = (c.len() - p - 1) as u32;
        if 2*i > len{
            gamma += u32::pow(2,power);
        } else {
            eps += u32::pow(2,power);
        }
    }
    println!("{}", eps*gamma);
}
