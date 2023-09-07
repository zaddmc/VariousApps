namespace CrosswordFixer {
    internal class Worker {
        static private List<Label> selectedTiles = new List<Label>();


        public static void PickRoot(int col, int row) {
            Label chosenTile = MainPage.Tiles[new Position(col, row).ToString()];

            chosenTile.BackgroundColor = Colors.IndianRed;

            selectedTiles.Add(chosenTile);

        }
        public static void AddBranch(int col, int row) {
            Label chosenTile = MainPage.Tiles[new Position(col, row).ToString()];

            chosenTile.BackgroundColor = Colors.YellowGreen;

            selectedTiles.Add(chosenTile);

        }
        public static void UnSelectAll() {
            while (selectedTiles.Count > 0) {
                selectedTiles.First().BackgroundColor = MainPage.ColorTheme[0];
                selectedTiles.Remove(selectedTiles.First());
            }
        }
        public static void UnSelectBranch() {

            while (selectedTiles.Count > 1) {
                selectedTiles.Last().BackgroundColor = MainPage.ColorTheme[0];
                selectedTiles.Remove(selectedTiles.Last());
            }
        }
    }
}
