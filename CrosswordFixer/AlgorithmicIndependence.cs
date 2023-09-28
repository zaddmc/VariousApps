using System.Diagnostics;
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
                            Worker.UnSelectAll();
                        }

                    }
                }
            }
            public static void CheckAround(int i, int j, int k, string cword) {
                switch (k) {
                    case 0:
                        if (Worker.AddBranch(i + 1, j) == cword[0].ToString()) { //------------------------------------------------
                            if (cword == Worker.CWord()) {
                                Worker.MarkAsGreen();
                                Worker.UnSelectAll();
                            }
                            CheckNext(i + 1, j, k, cword, 1);
                        }
                        break;
                    case 1:
                        if (Worker.AddBranch(i, j + 1) == cword[0].ToString()) { //------------------------------------------------
                            if (cword == Worker.CWord()) {
                                Worker.MarkAsGreen();
                                Worker.UnSelectAll();
                            }
                            CheckNext(i, j + 1, k, cword, 1);
                        }
                        break;
                    case 2:
                        if (Worker.AddBranch(i + 1, j + 1) == cword[0].ToString()) { //------------------------------------------------
                            if (cword == Worker.CWord()) {
                                Worker.MarkAsGreen();
                                Worker.UnSelectAll();
                            }
                            CheckNext(i + 1, j + 1, k, cword, 1);
                        }
                        break;

                    default:
                        break;
                }

            }
            public static void CheckNext(int i, int j, int k, string cword, int charnum) {
                switch (k) {
                    case 0:
                        Worker.AddBranch(i + 1, j); //kigger om den næste bogstav giver ordet
                        if (cword == Worker.CWord()) {
                            Worker.MarkAsGreen();
                            Worker.UnSelectAll();
                        }
                        else if (Worker.AddBranch(i + 1, j) == cword[charnum].ToString()) {
                            CheckNext(i + 1, j, k, cword, charnum + 1);
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

            public static async void Start() {
                MinMaxWordLength();


                Task work1 = new Task(Work1);
                Task work2 = new Task(Work2);
                Task work3 = new Task(Work3);
                Task work4 = new Task(Work4);
                Task work5 = new Task(Work5);

                work1.Start();
                work2.Start();
                work3.Start();
                work4.Start();
                work5.Start();

                //await Task.WhenAll(work1, work2, work3, work4, work5);
                Task.WaitAll(work1, work2, work3, work4, work5);
            }
            private static void Work1() {
                // cheks vertical from left to right otherwise known as east and the reverse
                for (int i = 0; i < Letters[0].Length; i++) {
                    List<string> listList = new();
                    for (int j = 0; j < Letters[i].Length; j++) {
                        listList.Add(Letters[j][i]);
                    }
                    string listSingle = ListToSingle(listList);

                    SearchForWords(listSingle, i, OrientationTypes.East, new WorkerThreading());
                    SearchForWords(Reverse(listSingle), i, OrientationTypes.West, new WorkerThreading());

                }
            }
            private static void Work2() {
                // cheks horizontol from top to bottom otherwise known as south and the reverse
                for (int i = 0; i < Letters.Length; i++) {
                    string listSingle = ArrayToSingle(Letters[i]);

                    SearchForWords(listSingle, i, OrientationTypes.South, new WorkerThreading());
                    SearchForWords(Reverse(listSingle), i, OrientationTypes.North, new WorkerThreading());
                }
            }
            private static void Work3() {
                // cheks diagonal from top right to bottom left otherwise known as southeast 
                for (int i = 0; i < Letters.Length; i++) {
                    List<string> listList = new();
                    for (int j = -Letters.Length; j < Letters[i].Length; j++) {
                        if (j < 0 || i + j > Letters.Length - 1)
                            continue;
                        listList.Add(Letters[i + j][j]);
                    }
                    if (listList.Count < minWordLength) {
                        continue;
                    }
                    string listSingle = ListToSingle(listList);

                    SearchForWords(listSingle, i, OrientationTypes.SouthEast, new WorkerThreading());
                }
            }
            private static void Work4() {
                // cheks diagonal from bottom right to top left otherwise known as northwest
                for (int i = -Letters.Length; i < Letters.Length; i++) {
                    List<string> listList = new();
                    for (int j = 0; j < Letters.Length; j++) {

                        if (i + j < 0 || j + i > Letters.Length - 1) {
                            continue;
                        }

                        listList.Add(Letters[j][j + i]);

                    }
                    if (listList.Count < minWordLength) {
                        continue;
                    }
                    string listSingle = ListToSingle(listList);

                    SearchForWords(Reverse(listSingle), i, OrientationTypes.NorthWest, new WorkerThreading());
                }
            }
            private static void Work5() {
                WorkerThreading worker = new WorkerThreading();
                // cheks diagonal from top left to bottom right otherwise known as southwest
                for (int i = 0; i < Letters.Length * 2; i++) {
                    List<string> listList = new();
                    for (int j = i; j >= 0; j--) {
                        if (j < 0)
                            break;
                        if (i - j >= Letters[0].Length || j >= Letters[0].Length)
                            continue;

                        listList.Add(Letters[i - j][j]);

                    }

                    if (listList.Count < minWordLength) {
                        continue;
                    }
                    string listSingle = ListToSingle(listList);

                    SearchForWords(listSingle, i, OrientationTypes.SouthWest, worker);
                    SearchForWords(Reverse(listSingle), i, OrientationTypes.NorthEast, worker);
                }
                worker.MarkAsGreen();
            }
            private static string Reverse(string strings) {
                string newString = "";
                for (int i = strings.Length - 1; i >= 0; i--) {
                    newString += strings[i];
                }

                return newString;
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
            private static void SearchForWords(string listSingle, int index, OrientationTypes orientation, WorkerThreading workerThreading) {

                for (int i = 0; i < Construction.PotentielWords.Length; i++) {
                    if (listSingle.Contains(Construction.PotentielWords[i])) {
                        var (succes, from, to) = FindWord(Construction.PotentielWords[i], listSingle);
                        if (succes) {
                            Debug.WriteLine("Current word: " + PotentielWords[i]);
                            MarkFoundWord(from, to, index, orientation, workerThreading);
                        }
                    }
                }
            }
            private static void MarkFoundWord(int from, int to, int index, OrientationTypes orientation, WorkerThreading workThread) {
                switch (orientation) {
                    case OrientationTypes.East:
                        for (int i = from; i < to; i++) {
                            workThread.AddBranch(i, index);
                        }
                        break;
                    case OrientationTypes.SouthEast:
                        for (int i = from; i < to; i++) {
                            workThread.AddBranch(index + i, i);
                        }
                        break;
                    case OrientationTypes.South:
                        for (int i = from; i < to; i++) {
                            workThread.AddBranch(index, i);
                        }
                        break;
                    case OrientationTypes.SouthWest:
                        if (index > Letters.Length) {
                            from += index - Letters.Length + 1;
                            to += index - Letters.Length + 1;
                        }
                        for (int i = from; i < to; i++) {
                            workThread.AddBranch(i, index - i);
                        }
                        break;
                    case OrientationTypes.West:
                        for (int i = from; i < to; i++) {
                            workThread.AddBranch(Letters.Length - 1 - i, index);
                        }
                        break;
                    case OrientationTypes.NorthWest: {
                            int save = from, j = 0;
                            from = Letters.Length - to;
                            to = Letters.Length - save;
                            for (int i = from; i < to; i++) {
                                if (index < 0)
                                    workThread.AddBranch(i, j + index + from);
                                else
                                    workThread.AddBranch(i - index, j + from);

                                j++;
                            }
                        }
                        break;
                    case OrientationTypes.North:
                        for (int i = from; i < to; i++) {
                            workThread.AddBranch(index, Letters.Length - 1 - i);
                        }
                        break;
                    case OrientationTypes.NorthEast:
                        if (index > Letters.Length) {
                            from += index - Letters.Length + 1;
                            to += index - Letters.Length + 1;
                        }
                        for (int i = from; i < to; i++) {
                            workThread.AddBranch(index - i, i);
                        }
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
        }
    }
}
