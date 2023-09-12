//using Construction;
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
        public static void SimpleAI() {
            List<string> cwords = Construction.PotentielWords.ToList();
            for (int i = 0; i < Construction.Letters.Length; i++) {
                for (int j = 0; j < Construction.Letters[i].Length; j++) {
                    if (Worker.PickRoot(i, j) == cwords[0][0].ToString()) {//cwords does not work proberly by channging
                        Position korrekt = new Position(i, j);
                        

                    }
                    else
                }



                //Den checker første bogstav. hvis det ikke er det samme går den videre til den næste. Hvis det er det rigtige bogstav,
                //så checker den de 3 felter over én, så til venstre, højre og 3 under. hvis der ikke er noget så går den videre til den næste.
                //Hvis den er rigtig går til den næste



            }
        }
    }
