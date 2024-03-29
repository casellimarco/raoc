pub fn main() {
    let crabs:Vec<f32> = include_str!("../input.txt")
        .trim()
        .split(",")
        .map(|i| i.parse().unwrap())
        .collect();
    let len = crabs.len() as f32;
    let mean = crabs.iter().sum::<f32>()/len;
    let mean_index = crabs.iter().map(|c| (c<&mean) as i32).sum::<i32>() as f32;
    let target = (mean + (len - mean_index*2.0)/(2.0*len)).round();
    let fuel:i32 = crabs.iter().map(|c| (c-target).abs() as i32).map(|d| d*(d+1)/2).sum();
    println!("{:?}", fuel );
}

