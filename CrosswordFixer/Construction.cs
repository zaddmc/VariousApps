namespace CrosswordFixer {
    internal class Construction {
        private static string[][] Letters { get; set; }
        private static string[] PotentielWords { get; set; }


        public static void GridMaker() {

            // not final just testing
            FileReader(@"C:\Users\david\Source\Repos\zaddmc\CrosswordFixer\CrosswordFixer\Resources\Crosswords\test1.csv");



            MainPage.CrossGrid.AddRowDefinition(new RowDefinition { Height = new GridLength(1, GridUnitType.Star) });

            MainPage.CrossGrid.AddColumnDefinition(new ColumnDefinition { Width = new GridLength(1, GridUnitType.Star) });

        }
        private static void FileReader(string file) {

            StreamReader sr = new StreamReader(file);


            int linesToRead = 0;

            if (!int.TryParse(sr.ReadLine().Split(':')[1], out linesToRead))
                throw new ArgumentException("Paramatar Fucked");

            
            Letters = new string[linesToRead][];

            for (int i = 0; i < linesToRead; i++) {
                string toBeAllocated = sr.ReadLine();

                if (toBeAllocated == "ENDREAD")
                    break;
                
                Letters[i] = toBeAllocated.ToLower().Split(',');
            }

            


        }

    }
}
