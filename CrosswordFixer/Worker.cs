namespace CrosswordFixer {
    public class Worker {
        static private List<Label> selectedTiles = new();

        public static string CWord() {
            string theWord = selectedTiles[0].Text;

            for (int i = 1; i < selectedTiles.Count(); i++) {
                theWord = theWord + selectedTiles[i].Text;
            }

            return theWord;
        }
        public static string PickRoot(int col, int row) {
            Label chosenTile = MainPage.Tiles[new Position(col, row).ToString()];

            chosenTile.BackgroundColor = Colors.IndianRed;

            selectedTiles.Add(chosenTile);
            return chosenTile.Text;
        }
        public static string AddBranch(int col, int row) {
            Label chosenTile = MainPage.Tiles[new Position(col, row).ToString()];

            chosenTile.BackgroundColor = Colors.YellowGreen;

            selectedTiles.Add(chosenTile);

            return chosenTile.Text;
        }
        public static void UnSelectAll() {
            while (selectedTiles.Count > 0) {
                selectedTiles.First().BackgroundColor = Color.FromArgb(selectedTiles.First().StyleId);
                selectedTiles.Remove(selectedTiles.First());
            }
        }
        public static void UnSelectBranch() {

            while (selectedTiles.Count > 1) {
                selectedTiles.Last().BackgroundColor = Color.FromArgb(selectedTiles.Last().StyleId);
                selectedTiles.Remove(selectedTiles.Last());
            }
        }
        public static void MarkAsGreen() {
            for (int i = 0; i < selectedTiles.Count; i++) {
                selectedTiles[i].BackgroundColor = Color.FromArgb("37fd12");
                selectedTiles[i].StyleId = "37fd12";
            }
        }
    }
}
