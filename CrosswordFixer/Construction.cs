namespace CrosswordFixer {
    internal class Construction {
        public static void GridMaker() {

            MainPage.CrossGrid.SetRow(new RowDefinition { Height = new GridLength(2, GridUnitType.Star) }, 0);
            Grid crossGg = new Grid
            {
                RowDefinitions =
                {
                    new RowDefinition {Height = new GridLength(2, GridUnitType.Star)}
                }
            };

        }


    }
}
