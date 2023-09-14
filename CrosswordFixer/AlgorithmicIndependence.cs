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
            DoButton("testing");
            DoButton("fishing");
        }





        public static void JustForTesting() {
            for (int i = 0; i < Construction.Letters.Length - 5; i++) {
                Worker.UnSelectAll();
                Worker.PickRoot(number, 0);
                for (int j = 0; j < 2; j++) {
                    Worker.AddBranch(i, j);
                }

            }


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
            public static void CheckAround(int i, int j, int k, string cwords) {
                switch (k) {
                    case 0:
                        if (Worker.AddBranch(i, j) == null) { //------------------------------------------------
                        }
                        break;
                    case 1:
                        break;
                    case 2:
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

        public class ZaddAI { // the zaddest ai ever
            public static int minWordLength = int.MaxValue; // fuck asbjron
            public static int maxWordLength = 0;

            public static void Start() {
                MinMaxWordLength();



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
                if (Worker.CWord().Length < minWordLength || Worker.CWord().Length > maxWordLength) {
                    return false;
                }


                for (int i = 0; i < Construction.PotentielWords.Length; i++) {

                    if (Worker.CWord() == Construction.PotentielWords[i]) {
                        Worker.MarkAsGreen();
                        return true;
                    }
                }

                return false;
            }
        }
    }
}
