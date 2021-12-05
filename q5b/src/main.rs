use ndarray::prelude::*;
use num::signum;
fn main() {
    let mut area = Array::<usize, _>::zeros((1000,1000));

    for l in include_str!("../input.txt").lines()
        {
        let coords: Vec<usize> = l.split(&[',','-','>',' '][..]).filter(|c| c!=&"").map(|c| c.parse().unwrap()).collect();
        if coords[0] == coords[2] || coords[1] == coords[3] {
            let mut x0 = coords[0];
            let mut x1 = coords[2];
            let mut y0 = coords[1];
            let mut y1 = coords[3];
            if coords[0] > coords[2]{
                x0 = coords[2];
                x1 = coords[0];
            }
            if coords[1] > coords[3]{
                y0 = coords[3];
                y1 = coords[1];
            }
            let mut slice = area.slice_mut(s![x0..x1+1, y0..y1+1]);
            slice += 1;
        }else{
            let diffx = coords[2] as i32 - coords[0] as i32;
            let diffy = coords[3] as i32 - coords[1] as i32;
            let steps = diffx.abs() as usize +1;
            let incrementx = signum(diffx);
            let incrementy = signum(diffy);
            let mut x = coords[0] as i32;
            let mut y = coords[1] as i32;
            for _ in 0..steps{
                area[[x as usize,y as usize]]+=1;
                x += incrementx;
                y += incrementy;
            }
        }
    }
    println!("{:?}", area.mapv(|area| (area>1) as usize).sum());
}
