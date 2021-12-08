use itertools::Itertools;
use std::collections::HashMap;
use std::collections::HashSet;

pub fn main() {
    let mut counter:usize = 0;
    let cha = vec!['a','b','c','d','e','f','g'];
    let ctd:HashMap<&char, usize> = HashMap::from_iter(cha.iter().enumerate().map(|(d,c)| (c,d)));
    let digits:HashMap<&str, usize> = HashMap::from([
        ("abcefg",0), ("cf",1), ("acdeg",2), ("acdfg",3),("bcdf",4),
        ("abdfg",5), ("abdefg",6), ("acf", 7), ("abcdefg",8), ("abcdfg", 9)]);
    for l in include_str!("../input2.txt").lines(){
        let v:Vec<&str> = l.split(" | ").collect();
        let mut inputs:Vec<&str> = v[0].split_whitespace().collect();
        let outputs:Vec<&str> = v[1].split_whitespace().collect();
        inputs.sort_by(|a,b| a.len().cmp(&b.len()));
        let cf: HashSet<_> = inputs[0].chars().collect();
        let acf: HashSet<_> = inputs[1].chars().collect();
        let bcdf: HashSet<_> = inputs[2].chars().collect();
        let abcdefg: HashSet<_> = inputs[9].chars().collect();
        let a = &acf - &cf;
        let bd = &bcdf - &cf;
        let aeg = &abcdefg - &bcdf;
        let eg = &aeg - &a;
        let m256_0: HashSet<_> = inputs[3].chars().collect();
        let m256_1: HashSet<_> = inputs[4].chars().collect();
        let m256_2: HashSet<_> = inputs[5].chars().collect();
        let adg = m256_0.intersection(&m256_1).cloned().collect::<HashSet<_>>().intersection(&m256_2).cloned().collect::<HashSet<_>>();
        let d = &adg - &aeg;
        let b = &bd - &d;
        let e = &aeg - &adg;
        let g = &eg - &e;
        let mut crazy: usize = 0;
        for i in 6..9 {
            let m: HashSet<_> = inputs[i].chars().collect();
            let maybe_c = &(&(&m - &adg) - &b) - &e;
            if maybe_c.len() == 1{
                crazy = i;
                break;
            }
        }
        let m: HashSet<_> = inputs[crazy].chars().collect();
        let c = &(&(&m - &adg) - &b) - &e;
        let f = &cf - &c;
        let set_map = vec![a,b,c,d,e,f,g];
        let cha_map: Vec<char> = set_map.iter().map(|s| s.iter().next().cloned().unwrap()).collect();
        println!("{:?}", cha_map);
        for (i, entry) in outputs.iter().enumerate(){
             let mut mapped_entry: Vec<char> = entry.chars().map(|c| cha[cha_map.iter().position(|&i| i == c).unwrap()]).collect();
             // let mut mapped_entry: Vec<char> = entry.chars().map(|c| cha_map[ctd[&c]]).collect();
             mapped_entry.sort();
             let mapped_string: String = mapped_entry.into_iter().collect();
             println!("{:?}", entry);
             println!("{:?}", mapped_string);
             let p = (outputs.len() - i - 1) as u32;
             counter += digits.get(&mapped_string.as_str()).unwrap()*usize::pow(10,p);
             println!("{:?}", counter);
        }
    }
    println!("{:?}", counter);
}
