using System.Diagnostics;
namespace CrosswordFixer {
    internal class Construction {
        private static string[][] Letters { get; set; } // The first bracket is Row/y while the second is Col/x
        private static string[] PotentielWords { get; set; }


        public static void GridMaker() {

            // not final just testing
            FileReader("\\Resources\\Crosswords\\test1.csv");

            
            
            MainPage.CrossGrid.AddRowDefinition(new RowDefinition { Height = new GridLength(1, GridUnitType.Star) });

            MainPage.CrossGrid.AddColumnDefinition(new ColumnDefinition { Width = new GridLength(1, GridUnitType.Star) });

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
}
