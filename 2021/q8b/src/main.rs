use itertools::Itertools;
use std::collections::HashMap;

pub fn main() {
    let mut counter:usize = 0;
    let cha = vec!['a','b','c','d','e','f','g'];
    let ctd:HashMap<&char, usize> = HashMap::from_iter(cha.iter().enumerate().map(|(d,c)| (c,d)));
    let digits:HashMap<&str, usize> = HashMap::from([
        ("abcefg",0), ("cf",1), ("acdeg",2), ("acdfg",3),("bcdf",4),
        ("abdfg",5), ("abdefg",6), ("acf", 7), ("abcdefg",8), ("abcdfg", 9)]);
    for l in include_str!("../input.txt").lines(){
        let v:Vec<&str> = l.split(" | ").collect();
        let mut inputs:Vec<&str> = v[0].split_whitespace().collect();
        let outputs:Vec<&str> = v[1].split_whitespace().collect();
        inputs.sort_by(|a,b| a.len().cmp(&b.len()));
        let mut cha_map:Vec<&char> = Vec::new();
        for dtc in cha.iter().permutations(cha.len()){
            let mut pass:usize = 0;
            for entry in &inputs{
                 let mut mapped_entry = entry.chars().map(|c| dtc[ctd[&c]]).collect::<Vec<&char>>();
                 mapped_entry.sort();
                 let mapped_string: String = mapped_entry.into_iter().collect();
                 if digits.get(&mapped_string.as_str()).is_none(){
                     break;
                 }else{
                     pass += 1;
                 }
            }
            if pass == 10{
                cha_map = dtc;
                break;
            }
        }
        for (i, entry) in outputs.iter().enumerate(){
             let mut mapped_entry = entry.chars().map(|c| cha_map[ctd[&c]]).collect::<Vec<&char>>();
             mapped_entry.sort();
             let mapped_string: String = mapped_entry.into_iter().collect();
             let p = (outputs.len() - i - 1) as u32;
             counter += digits.get(&mapped_string.as_str()).unwrap()*usize::pow(10,p);
        }
    }
    println!("{:?}", counter);
}
