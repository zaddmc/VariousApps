namespace CrosswordFixer;

public partial class MainPage : ContentPage {
	public static Grid CrossGrid { get; private set; }
	public static Grid MainGrid { get; private set; }

	public MainPage() {
		InitializeComponent();

		CrossGrid = crossGrid;
		MainGrid = maingrid;



	}

	private void Button_Clicked(object sender, EventArgs e) {

		var action = DisplayActionSheet("Choose method to insert values", null, null, "ReadFile", "ManuelInput");
		if (action != null) {
			Construction.GridInput(action.Result);
			Construction.GridMaker();
		}
	}
}

