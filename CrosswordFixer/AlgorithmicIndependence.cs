
namespace CrosswordFixer {
    public class AlgorithmicIndependence {

        // asbjorn is weak
        private static int number = 0;

        public static void DoButton(string name) {
            Button button = new Button
            {
                ClassId = name,
                Text = "Start: " + name + " Algorithim",
                TextColor = Colors.Black,
            };

            MainPage.StartButtons.Add(button);
        }
        public static void MakeButtons() {
            DoButton("Testing");
            DoButton("Simple");
            DoButton("Zadd");
        }





        public static void JustForTesting() {
            /*
            for (int i = 0; i < Construction.Letters.Length - 5; i++) {
                Worker.UnSelectAll();
                Worker.PickRoot(number, 0);
                for (int j = 0; j < 2; j++) {
                    Worker.AddBranch(i, j);
                }
                string fish= Worker.CWord();
                int lol = 0;
            }
            */

            Worker.PickRoot(1, 5);
            Worker.AddBranch(4, 6);
            Worker.AddBranch(7, 6);
            Worker.AddBranch(12, 0);
            Worker.AddBranch(4, 3);
            Worker.AddBranch(6, 17);
            MainPage.Tiles[new Position(12, number).ToString()].BackgroundColor = Colors.IndianRed;
            Worker.AddBranch(12, 5);
            string fish1 = Worker.CWord();
            //Worker.UnSelectBranch();
            string fish2 = Worker.CWord();
            int lol1 = 69;
            lol1++;

            number++;
        }

        public class SimpleAI {
            public static void Start() {
                List<string> cwords = Construction.PotentielWords.ToList();
                for (int i = 0; i < Construction.Letters.Length; i++) { //i ned af, j er henad
                    for (int j = 0; j < Construction.Letters[i].Length; j++) {
                        if (Worker.PickRoot(i, j) == cwords[0][0].ToString()) {//Checks if the first letter is equel with the first letter of Potentiel words  cwords does not work proberly by channging. yet. 
                                                                               //SimpleAICheckAround(i, j);
                            for (int k = 0; k < 3; k++) {
                                CheckAround(i, j, k, cwords[0]);

                            }
                        }
                        else {
                            return;
                        }

                    }
                }
            }
            public static void CheckAround(int i, int j, int k, string cword) {
                switch (k) {
                    case 0:
                        if (Worker.AddBranch(i+1, j) == cword[0].ToString()) { //------------------------------------------------
                            if (cword==Worker.CWord()) {
                                Worker.MarkAsGreen();
                                Worker.UnSelectAll();
                            }
                            CheckNext(i+1, j, k,cword);
                        }
                        break;
                    case 1:
                        if (Worker.AddBranch(i, j+1) == cword[0].ToString()) { //------------------------------------------------
                            if (cword == Worker.CWord()) {
                                Worker.MarkAsGreen();
                                Worker.UnSelectAll();
                            }
                            CheckNext(i, j, k, cword);
                        }
                            break;
                    case 2:
                        if (Worker.AddBranch(i+1, j+1) == cword[0].ToString()) { //------------------------------------------------
                            if (cword == Worker.CWord()) {
                                Worker.MarkAsGreen();
                                Worker.UnSelectAll();
                            }
                            CheckNext(i, j, k,cword);
                        }
                            break;

                    default:
                        break;
                }

            }
            public static void CheckNext(int i, int j, int k, string cword) {
                switch (k) {
                    case 0:
                        Worker.AddBranch(i + 1, j);
                        if (cword == Worker.CWord()) {
                            Worker.MarkAsGreen();
                            Worker.UnSelectAll();
                        }
                        break;
                    default:
                        break;
                }
            }
            /*public static (bool buh, int idkman) SimpleAICheckAround(int i, int j, List<string> cwords, int listnumber, int charnumber) {
                for (int k = -1; k < 2; k++) {
                    if (Worker.PickRoot(i - 1, j + k) == cwords[listnumber][1].ToString()) { //checker det næste bågstav ved de 3 neder under root, AKA en række ned af,
                        SimpleAICheckNext(i, j, k, cwords, listnumber, charnumber);

                    }


                }

                return (true, 12);
            }
            public static bool SimpleAICheckNext(int i, int j, int k, List<string> cwords, int listnumber, int charnumber) {
                if (Worker.PickRoot(i + k, j) == cwords[listnumber][charnumber].ToString())
                    if (Worker.PickRoot(i, j + k) == cwords[listnumber][cwords[listnumber].Length].ToString())



                      
                        if (i == 0) { }

                return (true);
            }*/
        }//close the code above this text -----

        public class ZaddAI : Worker { // the zaddest ai ever
            public static int minWordLength = int.MaxValue; // fuck asbjron
            public static int maxWordLength = 0;

            public static void Start() {
                MinMaxWordLength();

                // cheks vertical from left to right otherwise known as east
                for (int i = 0; i < Construction.Letters[0].Length; i++) {
                    List<string> listList = new();
                    for (int j = 0; j < Letters[0].Length; j++) {
                        listList.Add(Letters[0][j]);
                    }
                    string listSingle = ListToSingle(listList);

                    SearchForWords(listSingle, i, OrientationTypes.East);
                }

                // cheks horizontol from top to bottom otherwise known as south
                for (int i = 0; i < Construction.Letters.Length; i++) {
                    string listSingle = ArrayToSingle(Construction.Letters[i]);

                    SearchForWords(listSingle, i, OrientationTypes.South);
                }


            }
            private static string ArrayToSingle(string[] array) {
                string single = array[0];
                for (int i = 1; i < array.Length; i++) {
                    single += array[i];
                }
                return single;
            }
            private static string ListToSingle(List<string> list) {
                string single = list[0];
                for (int i = 1; i < list.Count; i++) {
                    single += list[i];
                }
                return single;
            }
            private static void SearchForWords(string listSingle, int index, OrientationTypes orientation) {

                for (int i = 0; i < Construction.PotentielWords.Length; i++) {
                    if (listSingle.Contains(Construction.PotentielWords[i])) {
                        var (succes, from, to) = FindWord(Construction.PotentielWords[i], listSingle);
                        if (succes) {
                            MarkFoundWord(from, to, index, orientation);
                        }
                    }
                }


            }
            private static void MarkFoundWord(int from, int to, int index, OrientationTypes orientation) {
                switch (orientation) {
                    case OrientationTypes.East:
                        for (int i = from; i < to; i++) {
                            AddBranch(i, index);
                        }
                        break;
                    case OrientationTypes.SouthEast:
                        for (int i = from; i < to; i++) {
                            AddBranch(index + i, i);
                        }
                        break;
                    case OrientationTypes.South:
                        for (int i = from; i < to; i++) {
                            AddBranch(index, i);
                        }
                        break;
                    case OrientationTypes.SouthWest:
                        break;
                    case OrientationTypes.West:
                        break;
                    case OrientationTypes.NorthWest:
                        break;
                    case OrientationTypes.North:
                        break;
                    case OrientationTypes.NorthEast:
                        break;
                    default:
                        break;
                }
                MarkAsGreen();
                UnSelectAll();
            }
            private enum OrientationTypes {
                East,
                SouthEast,
                South,
                SouthWest,
                West,
                NorthWest,
                North,
                NorthEast,
            }

            private static (bool succes, int from, int to) FindWord(string wordToFind, string fromWhere) {
                string cutout = fromWhere[0].ToString();
                for (int i = 1; i < wordToFind.Length; i++) {
                    cutout += fromWhere[i].ToString();
                }


                for (int i = 0; i < fromWhere.Length; i++) {
                    if (cutout == wordToFind) {
                        return (true, i, i + wordToFind.Length);
                    }
                    else {
                        cutout = cutout.Remove(0, 1);
                        cutout += fromWhere[i + wordToFind.Length];
                    }
                }

                return (false, 0, 0);
            }
            private static void MinMaxWordLength() {
                List<string> list = Construction.PotentielWords.ToList();
                for (int i = 0; i < list.Count; i++) {
                    if (list[i].Length < minWordLength) {
                        minWordLength = list[i].Length;
                    }
                    if (list[i].Length > maxWordLength) {
                        maxWordLength = list[i].Length;
                    }
                }
            }
            private static bool Compare() {
                if (CWord().Length < minWordLength || CWord().Length > maxWordLength) {
                    return false; // it will return 
                }


                for (int i = 0; i < Construction.PotentielWords.Length; i++) {

                    if (CWord() == Construction.PotentielWords[i]) {
                        MarkAsGreen();
                        return false;
                    }
                }

                return false;
            }
        }
    }
}
