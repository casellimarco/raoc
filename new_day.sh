#!/bin/bash
source ~/.secrets

DAY=${1:-$(date +'%-d')}
YEAR=${2:-$(date +'%Y')}

URL=https://adventofcode.com/${YEAR}/day/${DAY}
browse $URL

cargo new q${DAY}a
cargo new q${DAY}b

curl -b session=${AOC_SESSION} $URL/input > q${DAY}a/input.txt
cp q${DAY}a/input.txt q${DAY}b/input.txt

for f in q${DAY}a q${DAY}b; do
    target=$f/Cargo.toml
    echo "" >> $target
    echo "[lib]" >> $target
    echo "path = [\"src/main.rs\"]" >> $target
done
