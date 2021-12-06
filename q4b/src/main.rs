use std::collections::hash_map::Entry;
use std::collections::HashMap;

use ndarray::prelude::*;

pub fn main() {
    let mut tables_values= Vec::new();
    let mut draws: Vec<usize> = Vec::new();
    let mut table: usize = 0;
    let mut row: usize = 0;
    let mut num_to_coords = HashMap::<usize, Vec<(usize, usize, usize)>>::new();
    let mut table_values = Array::zeros((5,5));
    for (line_index,l) in include_str!("../input.txt")
            .lines().enumerate() {
        if line_index == 0 {
            draws = l.split(",").map(|i| i.parse().unwrap()).collect();
        }else if line_index == 1 {
        }else if l.len() == 0 {
            tables_values.push(table_values);
            table += 1;
            row = 0;
            table_values = Array::zeros((5,5));
        }else {
            for (col, value) in l.split_whitespace().map(|i| i.parse::<usize>().unwrap()).enumerate() {
                table_values[[row, col]] = value;
                match num_to_coords.entry(value) {
                    Entry::Occupied(mut entry)  => { entry.get_mut().push((table, row, col)); },
                    Entry::Vacant(entry)        => { entry.insert(vec![(table, row,col)]); },
                }
            }
            row +=1;
        }
    }
    tables_values.push(table_values);
    let mut winners = Array::ones(table+1);
    let mut tables = Array::ones((table+1,row,row));
    for draw in draws {
        match num_to_coords.get(&draw) {
            None => {},
            Some(coords) => {
                for c in coords {
                    tables[[c.0,c.1,c.2]]=0;
                    tables_values[c.0][[c.1,c.2]]=0;
                    if tables.slice(s![c.0, c.1, ..]).iter().sum::<usize>() == 0 ||
                       tables.slice(s![c.0, .., c.2]).iter().sum::<usize>() == 0 {
                           winners[c.0] = 0;
                           if winners.sum() == 0 {
                               println!("{}", draw*tables_values[c.0].sum());
                               return;
                           }
                    }
                }
            }
        }
    }
}

