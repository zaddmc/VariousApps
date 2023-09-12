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

    }
}
