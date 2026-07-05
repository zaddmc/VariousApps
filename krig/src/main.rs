use rand::seq::SliceRandom;

fn main() {
    let mut rng = rand::rng();

    let mut cards: Vec<i32> = (2..=15).collect::<Vec<_>>().repeat(4);
    cards.shuffle(&mut rng);

    let mut p1: Vec<i32> = vec![];
    let mut p2: Vec<i32> = vec![];

    while cards.len() != 0 {
        p1.append(&mut cards.split_off(cards.len() / 2));
        p2.append(&mut cards);
    }

    while p1.len() != 0 && p2.len() != 0 {}
}

fn round(p1: Vec<i32>, p2: Vec<i32>) {}
