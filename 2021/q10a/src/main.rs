use std::collections::HashMap;

pub fn main() {
    let bra = HashMap::from([(')', '('), (']', '['), ('}', '{'), ('>', '<')]);
    let mut score:i32 = 0;
    let value = HashMap::from([(')', 3), (']', 57), ('}', 1197), ('>', 25137)]);
    for line in include_str!("../input.txt").lines(){
        let mut stack:Vec<char> = vec![];
        for c in line.chars(){
            let compl = bra.get(&c);
            if compl.is_some(){
                if stack.last() == compl{
                    stack.pop();
                }else{
                    score += value[&c];
                    break;
                }
            }else{
                stack.push(c);
            }
        }
    }
    println!("{}", score);
}
