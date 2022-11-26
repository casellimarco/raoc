use ndarray::prelude::*;
use std::collections::HashSet;
pub fn main() {
    let mut vec:Vec<Vec<i32>> = vec![];
    for line in include_str!("../input.txt").lines(){
        vec.push(line.chars()
        .map(|i| i.to_digit(10).unwrap() as i32)
        .collect());
        
    }
    let mut area = Array::<i32, _>::ones((vec.len()+2,vec[0].len()+2))*9;
    for r in vec.iter().enumerate(){
        for c in r.1.iter().enumerate(){
            area[[r.0+1,c.0+1]] = *c.1;
        }
    }
    let mut basins: Vec<usize> = vec![];
    for r in 1..=vec.len(){
        for c in 1..=vec[0].len(){
            let v = area[[r,c]];
            let mut is_min = true;
            for add in vec![(1,0),(-1,0),(0,1),(0,-1)][..].iter(){
                if area[[(r as i32+add.0) as usize,(c as i32+add.1) as usize]] <= v{
                    is_min = false;
                    break;
                }
            }
            if is_min {
                // let mut basin = HashSet::from([(r,c)]);
                let mut basin: Vec<(usize,usize)> = vec![(r,c)];
                let mut to_check: Vec<(usize,usize)> = vec![(r,c)];
                while to_check.len() > 0 {
                    let (r0,c0) = to_check.pop().unwrap();
                    for add in vec![(1,0),(-1,0),(0,1),(0,-1)][..].iter(){
                        let new_r = (r0 as i32+add.0) as usize;
                        let new_c = (c0 as i32+add.1) as usize;
                        if !basin.contains(&(new_r, new_c)) && area[[new_r, new_c]] != 9{
                            to_check.push((new_r, new_c));
                            basin.push((new_r, new_c));
                        }
                    }
                }
                basins.push(basin.len())
            }
                    
        }
    }
    let n = basins.len();
    basins.select_nth_unstable(n-3);
    let mut prod:usize = 1;
    for i in n-3..n {
        prod *= basins[i];
    }
    println!("{}", prod);
}

