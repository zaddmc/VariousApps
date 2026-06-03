#[derive(Debug)]
pub struct Cell {
    pub row: usize,
    pub col: usize,
    pub color: CellColor,   // "red", "blue", or "empty"
    pub number: Option<u8>, // Some(n) for blue dots with a number
}

#[derive(Debug, PartialEq)]
pub enum CellColor {
    Blue,
    Red,
    Empty,
}
