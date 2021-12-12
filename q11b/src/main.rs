use std::cmp::*;
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
    let mut counter: i32 = 0;
    loop{
        area += 1;
        counter += 1;
        let mut flashed = Array::<i32, _>::zeros((vec.len(),vec[0].len()));
        let mut check = area.mapv(|a| (a>=10) as i32)*(1-&flashed);
        while check.iter().any(|a| a>&0){
            for r in 0..max_row{
                for c in 0..max_col{
                    let index = [r as usize,c as usize];
                    if area[index] >= 10 && flashed[index] == 0{
                        flashed[index] = 1;
                        let mut slice = area.slice_mut(s![max(0,r-1)..min(max_row,r+2), max(0,c-1)..min(max_col,c+2)]);
                        slice += 1;
                    }
                }
            }
            check = area.mapv(|a| (a>=10) as i32)*(1-&flashed);
        }
        if flashed.sum() == max_row * max_col{
            break
        }
        area = area*(1-flashed);
    }
    println!("{:?}", counter);
}
