use std::collections::HashSet;
use regex::Regex;
use std::cmp::min;
use std::cmp::max;


struct Sensor {
    pos: (i32, i32),
    distance: i32
}

impl Sensor {
    fn new(line: &str) -> Sensor {
        let re_line = r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)";
        let re = Regex::new(re_line).unwrap();
        let cap = re.captures(line).unwrap();
        let pos: (i32, i32) = (cap[1].parse().unwrap(), cap[2].parse().unwrap());
        let beacon: (i32, i32) = (cap[3].parse().unwrap(), cap[4].parse().unwrap());
        let distance = (pos.0-beacon.0).abs() + (pos.1-beacon.1).abs();
        Sensor{pos, distance}
    }   
    fn is_close(&self, point: (i32, i32)) -> bool {
        let d = (self.pos.0-point.0).abs() + (self.pos.1-point.1).abs();
        d <= self.distance
    }
    fn border(&self, area: &mut HashSet<(i32, i32)>) {
        let max_value = 4000000;
        let distance = self.distance + 1;
        let min_x = max(0,self.pos.0-distance);
        let max_x = min(max_value, self.pos.0+distance);
        for i in min_x..=max_x{
            let d = distance - (self.pos.0-i).abs();
            if self.pos.1-d >=0 {
                area.insert((i,self.pos.1-d));
            }
            if self.pos.1+d <=max_value {
                area.insert((i,self.pos.1+d));
            }
        }
    }
}



fn main() {
    let sensors: Vec<Sensor> = include_str!("../input.txt").lines()
        .map(|line| Sensor::new(line)).collect();
    let mut area: HashSet<(i32, i32)> = HashSet::new();
    for sensor in &sensors{
        sensor.border(&mut area);
    }
    let num_sensors = sensors.len();
    let mut closest: usize = 0;
    let mut found;
    for point in area {
        found = true;
        for k in 0..num_sensors {
            let index = (closest + k) % num_sensors;
            if sensors[index].is_close(point) {
                closest = index;
                found = false;
                break;
            }
        }
        if found {
            let answer = (point.0 as i64)*4000000+(point.1 as i64);
            println!("{:?}",answer);
            break;
        }
    }
}
