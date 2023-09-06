namespace CrosswordFixer;

public partial class MainPage : ContentPage {
	public static Grid CrossGrid { get; private set; }
	public static Grid MainGrid { get; private set; }

	public MainPage() {
		InitializeComponent();

		CrossGrid = crossGrid;
		MainGrid = maingrid;

	}







}

