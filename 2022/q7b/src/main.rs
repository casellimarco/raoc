use std::collections::HashMap;
use std::collections::HashSet;

struct Folder {
    path: String,
    parent: String,
    children: HashSet<String>,
    files: HashMap<String, u64>,
}

impl Folder {
    fn new(path: String) -> Folder {
        let parent = if path.contains("-"){
            path.rsplit_once("-").unwrap().0.to_string()
        } else {
            "".to_string()
        };
        let mut children = HashSet::new();
        let mut files = HashMap::new();
        Folder{ path, parent, children, files}
    }   
    fn size(&self, tree: &HashMap<String, Folder>) -> u64 {
        self.files.values().sum::<u64>() + self.children.iter().map(|c| tree[c].size(tree)).sum::<u64>()
    }
}

fn main() {
    let mut tree: HashMap<String, Folder> = HashMap::new();
    let mut cwd: String = "/".to_string();
    let mut folder = Folder::new(cwd.clone());
    tree.insert(folder.path.clone(), folder);
    for line in include_str!("../input.txt").lines() {
        if line == "$ cd .." {
            cwd = cwd.rsplit_once("-").unwrap().0.to_string();
        }
        else if line == "$ cd /" {
            cwd = "/".to_string();
        }
        else if line.starts_with("$ cd"){
            cwd = cwd.clone() + &"-".to_string() + &line[5..].to_string();
        }
        else if line == "$ ls" {
            continue;
        }  
        else if line.starts_with("dir "){
            let path = cwd.clone() + &"-".to_string() + &line[4..].to_string();
            let folder = Folder::new(path.clone());
            tree.insert(path.clone(), folder);
            tree.get_mut(&cwd).unwrap().children.insert(path.clone());
        }
        else{
            let (size, file_name) = line.split_once(" ").unwrap();
            tree.get_mut(&cwd).unwrap().files.insert(file_name.to_string(), size.parse().unwrap());
        }
    }
    let threshold: u64 = 30000000 - (70000000 - tree["/"].size(&tree));
    let min: u64 = tree.values().map(|f| f.size(&tree)).filter(|s|  s >= &threshold).min().unwrap();
    println!("{:?}", min);
}
