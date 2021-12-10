use std::collections::HashMap;

pub fn main() {
    let bra = HashMap::from([(')', '('), (']', '['), ('}', '{'), ('>', '<')]);
    let mut scores: Vec<i64> = vec![];
    let value = HashMap::from([('(', 1 as i64), ('[', 2 as i64), ('{', 3 as i64), ('<', 4 as i64)]);
    for line in include_str!("../input.txt").lines(){
        let mut stack:Vec<char> = vec![];
        let mut incomplete = true;
        for c in line.chars(){
            let compl = bra.get(&c);
            if compl.is_some(){
                if stack.last() == compl{
                    stack.pop();
                }else{
                    incomplete = false;
                    break;
                }
            }else{
                stack.push(c);
            }
        }
        if incomplete{
            let mut score: i64 = 0;
            while stack.len() > 0{
                let c = stack.pop().unwrap();
                score = 5*score + value[&c];
            }
            scores.push(score);
        }
    }
    let median_index = scores.len()/2;
    scores.select_nth_unstable(median_index);
    println!("{:?}", scores[median_index]);
}
