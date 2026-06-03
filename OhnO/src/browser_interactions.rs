use std::os::raw;

use chromiumoxide::browser::{Browser, BrowserConfig};
use chromiumoxide::cdp::js_protocol::runtime::EvaluateParams;
use chromiumoxide::js::EvaluationResult;
use chromiumoxide::page::Page;
use futures::StreamExt;
use tokio::task::JoinHandle;

use crate::types::{Cell, CellColor};

pub struct BrowserSession {
    pub browser: Browser,
    pub page: Page,
    handle: JoinHandle<()>,
}
impl BrowserSession {
    pub async fn new(url: &str) -> Result<Self, Box<dyn std::error::Error>> {
        let (browser, mut handler) = Browser::launch(
            BrowserConfig::builder()
                .with_head() // use .headless() for no window
                .build()?,
        )
        .await?;

        // The handler drives the browser event loop — run it in the background
        let handle = tokio::spawn(async move {
            loop {
                let _event = handler.next().await.unwrap();
            }
        });

        let page = browser.new_page(url).await?;
        tokio::time::sleep(std::time::Duration::from_secs(1)).await;
        println!("Opened {}", url);

        Ok(Self { browser, page, handle })
    }

    pub async fn gather(&self) -> Result<(Vec<Cell>), Box<dyn std::error::Error>> {
        self.page.evaluate("Game.startGame(9)").await?;
        println!("Called Game.startGame(9)");

        // Give the game a moment to render the grid
        tokio::time::sleep(std::time::Duration::from_secs(1)).await;

        let grid_js = r#"
            (() => {
                const cells = document.querySelectorAll('#grid td');
                return Array.from(cells).map(cell => {
                    const tile = cell.querySelector('.tile');
                    const classes = tile ? Array.from(tile.classList) : [];
                    const color = classes.includes('tile-2') ? 'blue'
                                : classes.includes('tile-1') ? 'red'
                                : 'empty';
                    const inner = cell.querySelector('.inner');
                    const text = inner ? inner.textContent.trim() : '';
                    const number = (text !== '') ? parseInt(text, 10) : null;
                    const col = parseInt(cell.dataset.x, 10);
                    const row = parseInt(cell.dataset.y, 10);
                    return { row, col, color, number };
                });
            })()
        "#;

        let result = self
            .page
            .evaluate(
                EvaluateParams::builder()
                    .expression(grid_js)
                    .return_by_value(true)
                    .build()?,
            )
            .await?;

        #[derive(Debug, serde::Deserialize)]
        struct RawCell {
            row: usize,
            col: usize,
            color: String,
            number: Option<u8>,
        }

        let raw: Vec<RawCell> = result.into_value()?;
        let cells: Vec<Cell> = raw
            .into_iter()
            .map(|c| Cell {
                row: c.row,
                col: c.col,
                color: match c.color.as_str() {
                    "blue" => CellColor::Blue,
                    "red" => CellColor::Red,
                    _ => CellColor::Empty,
                },
                number: c.number,
            })
            .collect();

        println!("\nParsed {} cells:", cells.len());
        for cell in &cells {
            println!("  ({}, {}) {:?} {:?}", cell.row, cell.col, cell.color, cell.number);
        }

        Ok(cells)
    }

    pub async fn click(&self, cells: Vec<Cell>) -> Result<bool, Box<dyn std::error::Error>> {
        for cell in &cells {
            let elm = self
                .page
                .find_element(format!("#tile-{}-{}", cell.row, cell.col))
                .await?;
            elm.click().await?;
        }

        // TODO: Wait and check if the ojoo comes around
        Ok(false)
    }

    // pub async fn close(mut self) -> Result<(), Box<dyn std::error::Error>> {
    //     self.browser.close().await?;
    //     self.handle.await?;
    //     Ok(())
    // }
}
