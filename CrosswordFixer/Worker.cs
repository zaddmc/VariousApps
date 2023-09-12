namespace CrosswordFixer {
    public class Worker {
        static private List<Label> selectedTiles = new();
        static public List<String> selectedString= new();

        public static string CWord() {
            string theWord = selectedString[0];

            for (int i = 1; i < selectedString.Count(); i++) {
                theWord = theWord + selectedString[i];
            }

            return theWord;
        }
        public static string PickRoot(int col, int row) {
            Label chosenTile = MainPage.Tiles[new Position(col, row).ToString()];

            chosenTile.BackgroundColor = Colors.IndianRed;

            selectedTiles.Add(chosenTile);
            selectedString.Add(chosenTile.Text);
            return chosenTile.Text;
        }
        public static string AddBranch(int col, int row) {
            Label chosenTile = MainPage.Tiles[new Position(col, row).ToString()];

            chosenTile.BackgroundColor = Colors.YellowGreen;

            selectedTiles.Add(chosenTile);
            selectedString.Add(chosenTile.Text);

            return chosenTile.Text;
        }
        public static void UnSelectAll() {
            while (selectedTiles.Count > 0) {
                selectedTiles.First().BackgroundColor = MainPage.ColorTheme[0];
                selectedTiles.Remove(selectedTiles.First());
                selectedString.Remove(selectedString.First());
            }
        }
        public static void UnSelectBranch() {

            while (selectedTiles.Count > 1) {
                selectedTiles.Last().BackgroundColor = MainPage.ColorTheme[0];
                selectedTiles.Remove(selectedTiles.Last());
                selectedString.Remove(selectedString.Last());
            }
        }
    }
}
