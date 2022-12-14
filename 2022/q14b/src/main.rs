use std::collections::HashSet;

struct Sand {
    x: i32,
    y: i32,
}

impl Sand {
    fn new() -> Sand {
        let x: i32 = 500;
        let y: i32 = 0;
        Sand{x, y}
    }   
    fn fall(&mut self, rocks: &mut HashSet::<(i32,i32)>, y_max: i32) -> bool {
        if self.y == y_max + 1 {
            rocks.insert((self.x, self.y));
            return false;
        }
        if !rocks.contains(&(self.x, self.y + 1)){
            self.y+=1;
            return true;
        }
        if !rocks.contains(&(self.x - 1, self.y + 1)){
            self.x-=1;
            self.y+=1;
            return true;
        }
        if !rocks.contains(&(self.x + 1, self.y + 1)){
            self.x+=1;
            self.y+=1;
            return true;
        }
        rocks.insert((self.x, self.y));
        return false;
    }
    fn is_stuck(&self) -> bool {
        self.y == 0
    }
}



fn main() {
    let mut rocks = HashSet::new();
    for line in include_str!("../input.txt").lines(){
        let v: Vec<(i32,i32)> = line.split(" -> ")
        .map(|s| {
            let a = s.split_once(",").unwrap();
            (a.0.parse().unwrap(), a.1.parse().unwrap())
        }).collect();
        for i in 0..v.len()-1 {
            if v[i].0 < v[i+1].0 {
                for j in v[i].0..=v[i+1].0 {
                    rocks.insert((j, v[i].1));   
                }
            }
            else if v[i].0 > v[i+1].0 {
                for j in v[i+1].0..=v[i].0 {
                    rocks.insert((j, v[i].1));    
                }
            }
            else if v[i].1 < v[i+1].1 {
                for j in v[i].1..=v[i+1].1 {
                    rocks.insert((v[i].0, j));   
                }
            }
            else if v[i].1 > v[i+1].1 {
                for j in v[i+1].1..=v[i].1 {
                    rocks.insert((v[i].0, j));   
                }
            }
        }
    }
    let y_max = rocks.iter().map(|r| r.1).max().unwrap();
    let mut sand = Sand::new();
    let mut c: usize = 1;
    loop {
        while sand.fall(&mut rocks, y_max){}
        if !sand.is_stuck() {
            sand = Sand::new();
            c+=1;
        }
        else {
            break;
        }
    }
    println!("{:?}", c);
}
