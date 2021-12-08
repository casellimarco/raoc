pub fn main() {
    let mut c:usize = 0;
    let sizes:Vec<usize> = vec![2,3,4,7];
    for l in include_str!("../input.txt").lines(){
        let v:Vec<&str> = l.split(" | ").collect();
        for output in v[1].split_whitespace(){
            if sizes.contains(&output.len()) {
                c+=1;
            }
        }
    }
    println!("{:?}", c);
}
