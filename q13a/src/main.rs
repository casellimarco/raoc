use std::collections::HashSet;
pub fn main() {
    let mut coordinates_done = false;
    let mut points = HashSet::new();
    let mut folds:Vec<Vec<usize>> = Vec::new();
    for line in include_str!("../input.txt").lines(){
        if line.is_empty() {
            coordinates_done = true;
            continue;
        }
        if !coordinates_done{
            points.insert(line.split(",").map(|x| x.parse().unwrap()).collect::<Vec<usize>>()[..2].to_vec());
        }else{
            let trimmed = line.replace("fold along ", "").replace("x", "0").replace("y", "1");
            folds.push(trimmed.split("=").map(|x| x.parse().unwrap()).collect());
        }
    }
    let fold = &folds[0][..2];
    let axis = fold[0];
    let k = fold[1];
    let mut new_points = HashSet::new();
    for mut p in points{
        if p[axis] > k{
            p[axis] = 2*k - p[axis];
            println!("{:?}", p);
        }
        new_points.insert(p);
    }
    println!("{:?}", new_points.len());
}
