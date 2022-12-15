use std::collections::HashSet;
use regex::Regex;

struct Sensor {
    pos: (i32, i32),
    beacon: (i32, i32),
}

impl Sensor {
    fn new(line: &str) -> Sensor {
        let re_line = r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)";
        let re = Regex::new(re_line).unwrap();
        let cap = re.captures(line).unwrap();
        let pos: (i32, i32) = (cap[1].parse().unwrap(), cap[2].parse().unwrap());
        let beacon: (i32, i32) = (cap[3].parse().unwrap(), cap[4].parse().unwrap());
        Sensor{pos, beacon}
    }   
    fn empty_area(&self) -> HashSet<(i32, i32)> {
        let distance = (self.pos.0-self.beacon.0).abs() + (self.pos.1-self.beacon.1).abs();
        let mut area = HashSet::new();
        let y = 2000000;
        let target = (self.pos.1-y).abs(); 
        if target <= distance {
            for i in (target-distance)..=(distance-target){
                area.insert((self.pos.0+i, y));
            }
        }
        area
    }
}



fn main() {
    let sensors: Vec<Sensor> = include_str!("../input.txt").lines()
        .map(|line| Sensor::new(line)).collect();
    let mut area: HashSet<(i32, i32)> = HashSet::new();
    let mut beacons: HashSet<(i32, i32)> = HashSet::new();
    
    for sensor in sensors{
        area.extend(&sensor.empty_area());
        beacons.insert(sensor.beacon);
    }
    println!("{:?}", (&area - &beacons).len());
}
