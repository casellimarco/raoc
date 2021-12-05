use ndarray::prelude::*;
fn main() {
    let mut area = Array::<usize, _>::zeros((1000,1000));

    for l in include_str!("../input.txt").lines()
        {
        let ch: Vec<usize> = l.split(&[',','-','>',' '][..]).filter(|c| c!=&"").map(|c| c.parse().unwrap()).collect();
        if ch[0] == ch[2] || ch[1] == ch[3] {
            let mut x0 = ch[0];
            let mut x1 = ch[2];
            let mut y0 = ch[1];
            let mut y1 = ch[3];
            if ch[0] > ch[2]{
                x0 = ch[2];
                x1 = ch[0];
            }
            if ch[1] > ch[3]{
                y0 = ch[3];
                y1 = ch[1];
            }
            let mut slice = area.slice_mut(s![x0..x1+1, y0..y1+1]);
            slice += 1;
        }
    }
    println!("{:?}", area.mapv(|area| (area>1) as usize).sum());
}
