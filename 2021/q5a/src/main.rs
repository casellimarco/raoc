use ndarray::prelude::*;
pub fn main() {
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
        }
    }
    println!("{:?}", area.mapv(|area| (area>1) as usize).sum());
}
