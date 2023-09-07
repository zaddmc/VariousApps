using System.Diagnostics;

namespace CrosswordFixer;

public partial class MainPage : ContentPage {
	public static Grid CrossGrid { get; private set; }
	public static Grid MainGrid { get; private set; }
    static public Color[] ColorTheme { get; private set; }

    public MainPage() {
		InitializeComponent();

		CrossGrid = crossGrid;
		MainGrid = maingrid;

        ColorTheme = new Color[] { Color.FromArgb("ffffff"), Color.FromArgb("2b2d31"), Color.FromArgb("1e1f22"), Colors.Green }; // Brightmode 


    }

    private async void Button_Clicked(object sender, EventArgs e) {
		string action = await DisplayActionSheet("Choose method to insert values", null, null, "ReadFile", "ManuelInput");
		
		if (action != null) {
			await Construction.GridInput(action);
			Construction.GridMaker();
		}
	}
}

