use ndarray::prelude::*;
pub fn main() {
    let mut vec:Vec<Vec<i32>> = vec![];
    for line in include_str!("../input.txt").lines(){
        vec.push(line.chars()
        .map(|i| i.to_digit(10).unwrap() as i32)
        .collect());
        
    }
    let mut area = Array::<i32, _>::zeros((vec.len(),vec[0].len()));
    for r in vec.iter().enumerate(){
        for c in r.1.iter().enumerate(){
            area[[r.0,c.0]] = *c.1;
        }
    }
    let max_row = area.shape()[0] as i32;
    let max_col = area.shape()[1] as i32;
    let mut counter: usize = 0;
    for (r, c, v) in area.indexed_iter().map(|((r, c), v)| (r as i32, c as i32, v)) {
        let mut is_min = true;
        for add in vec![(1,0),(-1,0),(0,1),(0,-1)][..].iter(){
            if r+add.0< max_row &&
               c+add.1< max_col &&
               r+add.0>= 0 && c+add.1>= 0{
                if area[[(r+add.0) as usize,(c+add.1) as usize]] <= *v{
                    is_min = false;
                    break;
                }
            }
        }
        counter += (*v as usize +1)*(is_min as usize);
    }
    println!("{}", counter);
}
