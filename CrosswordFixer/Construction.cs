using System.Diagnostics;
namespace CrosswordFixer {
    internal class Construction {
        public static string[][] Letters { get; set; } // The first bracket is Row/y while the second is Col/x
        public static string[] PotentielWords { get; set; }


        public static void GridMaker() {

            if (Letters == null)
                throw new ArgumentException("order problem i guess");

            int maxi = 0;
            for (int i = 0; i < Letters.Length; i++) {
                MainPage.CrossGrid.AddRowDefinition(new RowDefinition { Height = new GridLength(1, GridUnitType.Star) });
                if (Letters[i].Length > maxi)
                    maxi = Letters[i].Length;

            }

            for (int i = 0; i < maxi; i++) {
                MainPage.CrossGrid.AddColumnDefinition(new ColumnDefinition { Width = new GridLength(1, GridUnitType.Star) });
            }





            for (int i = 0; i < Letters.Length; i++) {
                for (int j = 0; j < Letters[i].Length; j++) {
                    MainPage.CrossGrid.Add(TileGenerator(j, i), j, i);
                }
            }



        }
        private static Label TileGenerator(int x, int y) {
            Label tile = new Label
            {
                BackgroundColor = MainPage.ColorTheme[0],
                // HeightRequest = 50,
                // WidthRequest = 50,
                Margin = 2,
                Text = Letters[x][y].ToUpper(),
                TextColor = Colors.Black,
                HorizontalTextAlignment = TextAlignment.Center,
                VerticalTextAlignment = TextAlignment.Center
            };

            MainPage.Tiles.Add(new Position(x, y).ToString(), tile);

            return tile;
        }
        public static async Task<bool> GridInput(string inputType) {

            switch (inputType.ToLower()) {
                default:

                    break;
                case "readfile":
                    var result = await FilePicker.Default.PickAsync(PickOptions.Default);

                    if (result != null && result.FileName.EndsWith("csv"))
                        // not final just testing
                        FileReader(result.FullPath);
                    break;
                case "manueltypeing":

                    break;
            }



            return true;
        }
        private static void FileReader(string file) {

            StreamReader sr = new StreamReader(file);

            while (true) {
                Debug.WriteLine("Checking File for next step");
                try {
                    switch (sr.ReadLine().ToLower()) {
                        case "read":
                            Debug.WriteLine("Reading letters");
                            ReadLetters(sr);
                            break;
                        case "words":
                            Debug.WriteLine("Reading potentiel words");
                            ReadWords(sr);
                            break;
                        case "finishedreading":
                            Debug.WriteLine("finished reading the file will now continue");
                            return;
                        default:
                            Debug.WriteLine("Empty Line or unrecognized determing wether to end or continue");
                            if (sr.EndOfStream)
                                return;
                            break;
                    }
                }
                catch (Exception) {
                    Debug.WriteLine("Failed to read from file, may be due to it being empty or non existent");

                    throw;
                }
            }
        }
        private static void ReadWords(StreamReader sr) {
            switch (sr.ReadLine().ToLower()) {
                case "line":
                    Debug.WriteLine("Reading potentiel words as a line");
                    PotentielWords = sr.ReadLine().ToLower().Split(',');
                    if (sr.ReadLine().ToLower() == "endwords")
                        return;
                    else
                        Debug.WriteLine("Eat shit and die"); // can be made better to actually take care of the problem, but then again it is YOUR formatting that fucked up
                    break;
                case "list":
                    Debug.WriteLine("to be done");
                    break;
            }
        }
        private static void ReadLetters(StreamReader sr) {
            List<string[]> listOfLetters = new();

            while (true) {
                string toBeAllocated = sr.ReadLine();

                if (toBeAllocated == "ENDREAD")
                    break;

                listOfLetters.Add(toBeAllocated.ToLower().Split(','));
            }

            Letters = listOfLetters.ToArray();
        }

    }
    public class Position {
        public int x;
        public int y;
        public Position(int x, int y) {
            this.x = x;
            this.y = y;
        }
        public override string ToString() {
            return string.Format("x:{0}, y:{1}", x, y);
        }

    }
}
