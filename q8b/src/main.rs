use itertools::Itertools;
use std::collections::HashMap;

pub fn main() {
    let mut counter:usize = 0;
    let cha = vec!['a','b','c','d','e','f','g'];
    let ctd:HashMap<&char, usize> = HashMap::from_iter(cha.iter().enumerate().map(|(d,c)| (c,d)));
    let sizes:Vec<usize> = vec![2,3,4,7];
    for l in include_str!("../input.txt").lines(){
        let v:Vec<&str> = l.split(" | ").collect();
        let mut all:Vec<&str> = v[0].split_whitespace().collect();
        let outputs:Vec<&str> = v[1].split_whitespace().collect();
        all.extend(&outputs);
        all.sort_by(|a,b| a.len().cmp(&b.len()));
        for dtc in cha.iter().permutations(cha.len()){
            for entry in &all{
                 let mut mapped_entry = entry.chars().map(|c| dtc[ctd[&c]]).collect::<Vec<&char>>();
                 mapped_entry.sort();
                 let mapped_string: String = mapped_entry.into_iter().collect();
                 println!("{:?}", mapped_string);
                 // let mapped_entry = entry.chars().map(|c| ctd[dtc[&c]]).collect().sort();
            }
            // println!("{:?}", dtc);
        }
        // println!("{:?}", all);
        for output in v[1].split_whitespace(){
            if sizes.contains(&output.len()) {
                counter+=1;
            }
        }
    }
    println!("{:?}", counter);
}
