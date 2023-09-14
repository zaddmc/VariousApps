using System.Diagnostics;

namespace CrosswordFixer;

public partial class MainPage : ContentPage {
    public static Grid CrossGrid { get; private set; }
    public static Grid MainGrid { get; private set; }
    public static VerticalStackLayout InitiazeButtons { get; private set; }
    static public Color[] ColorTheme { get; private set; }
    static public Dictionary<string, Label> Tiles { get; private set; }
    static public List<Button> StartButtons { get; set; }

    static public bool IsEditModeEnabled = false;



    public MainPage() {
        InitializeComponent();

        // initialzation of grid or other layouts to be used in the code
        CrossGrid = crossGrid;
        MainGrid = maingrid;
        InitiazeButtons = initiazeButtons;

        // initialzation of certain all seeing types 
        ColorTheme = new Color[] { Color.FromArgb("ffffff"), Color.FromArgb("2b2d31"), Color.FromArgb("1e1f22"), Colors.Green }; // Brightmode 
        Tiles = new Dictionary<string, Label>();
        StartButtons = new List<Button>();

        // initialzation of the algorithim buttons so that the user can start an algorithim
        AlgorithmicIndependence.MakeButtons();
        SetupAIButtons();
    }
    private static void SetupAIButtons() {

        while (StartButtons.Count > 0) {
            Button button = StartButtons.First();
            StartButtons.Remove(button);
            
            
            button.Clicked += InitiazeButtons_Clicked;



            InitiazeButtons.Children.Add(button);
        }
    }
    private async void Button_Clicked(object sender, EventArgs e) {
        string action = await DisplayActionSheet("Choose method to insert values", null, null, "ReadFile", "ManuelInput");

        if (action != null) {
            await Construction.GridInput(action);
            Construction.GridMaker();
        }
    }

    private void EditMode_Clicked(object sender, EventArgs e) {
        if (IsEditModeEnabled) {
            IsEditModeEnabled = false;
            EditMode.Text = "Editor Mode: disabled";
        }
        else {
            IsEditModeEnabled = true;
            EditMode.Text = "Editor Mode: enabled";
        }
    }

    private static void InitiazeButtons_Clicked(object sender, EventArgs e) {

        var button = sender as Button;
        string identifier = button.ClassId;

        switch (identifier.ToLower()) {
            default:
                Debug.WriteLine("Missing Identifier in the initialzation of AI buttons");
                break;
            case "testing":
                AlgorithmicIndependence.JustForTesting();
                break;
            case "simple":
                AlgorithmicIndependence.SimpleAI();
                break;
            case "zadd":
                AlgorithmicIndependence.ZaddAI.Start();
                break;
        }

    }
}

