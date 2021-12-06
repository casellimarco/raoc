fn main() {
    let mut a: Vec<Vec<i32>> = Vec::new();
    for l in include_str!("../input.txt")
            .lines() {
        a.push(l.chars().map(|i| i.to_digit(10).unwrap() as i32).collect());

    }
    let mut more = Vec::new();
    let mut less = Vec::new();
    let mut ones = Vec::new();
    let mut zeros = Vec::new();
    let mut i:usize =0;
    let mut value = 0;
    for v in a.iter(){
        value += 2*v[i] -1;
        if v[i] ==1 {
            ones.push(v);
        }else{
            zeros.push(v);
        }
    }
    if value>=0 {
        more = ones;
        less = zeros;
    }else{
        more = zeros;
        less = ones;
    }
    i = 1;
    while more.len() != 1{
        value = 0;
        zeros = Vec::new();
        ones = Vec::new();
        for v in more.iter(){
            value += 2*v[i] -1;
            if v[i] ==1 {
                ones.push(v);
            }else{
                zeros.push(v);
            }
        }
        if value>=0 {
            more = ones;
        }else{
            more = zeros;
        }
        i+=1;
    }
    i = 1;
    while less.len() != 1{
        value = 0;
        zeros = Vec::new();
        ones = Vec::new();
        for v in less.iter(){
            value += 2*v[i] -1;
            if v[i] ==1 {
                ones.push(v);
            }else{
                zeros.push(v);
            }
        }
        if value>=0 {
            less = zeros;
        }else{
            less = ones;
        }
        i+=1;
    }
    let mut gamma=0;
    let mut eps=0;
    for i in 0..more[0].len(){
        let power = (more[0].len() - i - 1) as u32;
        gamma += more[0][i]*i32::pow(2,power);
        eps += less[0][i]*i32::pow(2,power);
    }
    println!("{}", eps*gamma);
}
