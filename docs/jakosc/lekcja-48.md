# Lekcja 48. Wzorzec MVVM: model, widok, ViewModel, Command

<p class="lekcja-meta">Dział: Jakość, testy i publikacja · 45 min · Efekty: INF.04.3 (8), INF.04.6 (2) kryt. 5 · <span class="zakres zakres-p">INF.04</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- wyjaśnić, za co odpowiada model, widok i ViewModel,
- przenieść logikę strony z pliku `.xaml.cs` do klasy ViewModel,
- obsłużyć przycisk przez `Command` i `CommandParameter` zamiast zdarzenia `Clicked`.

## Wprowadzenie

**MVVM** (Model – View – ViewModel) to wzorzec projektowy, który rozdziela wygląd od logiki. Wiązania i `INotifyPropertyChanged` znasz już z lekcji 19. MVVM porządkuje je w trzy warstwy.

| Warstwa | Co zawiera | Przykład |
|---|---|---|
| **Model** | dane i reguły, bez wiedzy o ekranie | klasa `Rachunek`, tabela SQLite |
| **View** (widok) | XAML; w `.xaml.cs` tylko `InitializeComponent()` i `BindingContext` | `MainPage.xaml` |
| **ViewModel** | właściwości do wiązania, obliczenia, polecenia (`ICommand`) | `NapiwekViewModel` |

Przycisk nie musi mieć zdarzenia `Clicked`. Ma właściwość `Command`, którą wiążesz z poleceniem w ViewModelu. `CommandParameter` przekazuje do polecenia wartość.

=== "NapiwekViewModel.cs"

    ```csharp
    using System.ComponentModel;
    using System.Runtime.CompilerServices;
    using System.Windows.Input;

    namespace Napiwek;

    public class NapiwekViewModel : INotifyPropertyChanged
    {
        private int procent = 10;

        public int Procent
        {
            get => procent;
            set
            {
                if (procent == value) return;
                procent = value;
                OnPropertyChanged();
                OnPropertyChanged(nameof(Napiwek));
            }
        }

        public decimal Napiwek => 100m * Procent / 100;   // na razie stały rachunek 100 zł

        public ICommand UstawProcentCommand { get; }

        public NapiwekViewModel()
        {
            // parametr z XAML przychodzi jako tekst
            UstawProcentCommand = new Command<string>(p => Procent = int.Parse(p));
        }

        public event PropertyChangedEventHandler? PropertyChanged;

        protected void OnPropertyChanged([CallerMemberName] string? nazwa = null)
            => PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(nazwa));
    }
    ```

=== "MainPage.xaml"

    ```xml
    <ContentPage ...
                 xmlns:vm="clr-namespace:Napiwek"
                 x:DataType="vm:NapiwekViewModel">

        <VerticalStackLayout Padding="20" Spacing="10">
            <Label Text="{Binding Procent, StringFormat='Napiwek: {0} %'}" />
            <HorizontalStackLayout Spacing="8">
                <Button Text="10%" Command="{Binding UstawProcentCommand}" CommandParameter="10" />
                <Button Text="15%" Command="{Binding UstawProcentCommand}" CommandParameter="15" />
            </HorizontalStackLayout>
            <Label Text="{Binding Napiwek, StringFormat='{0:F2} zł'}" FontSize="24" />
        </VerticalStackLayout>
    </ContentPage>
    ```

=== "MainPage.xaml.cs"

    ```csharp
    public MainPage()
    {
        InitializeComponent();
        BindingContext = new NapiwekViewModel();   // i nic więcej!
    }
    ```

!!! info "Po co to wszystko?"
    ViewModel nie zna kontrolek (`lblWynik`, `entKwota`), więc możesz go **przetestować** bez uruchamiania aplikacji (lekcja 51) i podłączyć do innego widoku, np. wersji na tablet. Na egzaminie INF.04 wystarczy obsługa zdarzeń, ale MVVM to standard w firmach.

## Zadanie główne (25 min)

Utwórz projekt `Napiwek`. Plik `MainPage.xaml.cs` ma zawierać **tylko** konstruktor z `InitializeComponent()` i ustawieniem `BindingContext`.

```text
+-------------------------------------+
|  Kalkulator napiwku                 |  <- #00695C, tekst biały, 24
+-------------------------------------+
|  Rachunek (zł): [ 150          ]    |
|  Napiwek: 15 %                      |
|  [ 10% ] [ 15% ] [ 20% ]            |  <- CommandParameter
|  Liczba osób: 3          [ - | + ]  |
|                                     |
|  Napiwek:      22,50 zł             |
|  Do zapłaty:  172,50 zł             |
|  Na osobę:     57,50 zł             |  <- 28, pogrubiony
|  [            WYCZYŚĆ             ] |
+-------------------------------------+
```

1. Dodaj klasę `NapiwekViewModel` z właściwościami `Rachunek` (`string`, wiązana z `Entry`), `Procent` (`int`, start 10), `LiczbaOsob` (`int`, start 1) i właściwościami wyliczanymi `Napiwek`, `DoZaplaty`, `NaOsobe` (`decimal`).
2. Zmiana `Rachunek`, `Procent` lub `LiczbaOsob` powiadamia o zmianie wszystkich trzech właściwości wyliczanych. Gdy rachunek nie jest poprawną liczbą, wyniki wynoszą 0.
3. Trzy przyciski procentu korzystają z **jednego** polecenia `UstawProcentCommand` z różnym `CommandParameter`.
4. `Stepper` liczby osób 1–10 wiązany z `LiczbaOsob`.
5. Przycisk **WYCZYŚĆ** wywołuje `WyczyscCommand`: rachunek pusty, procent 10, jedna osoba.
6. Wyniki z dwoma miejscami po przecinku (`StringFormat`). Sprawdź:

| Rachunek | Procent | Osoby | Napiwek | Do zapłaty | Na osobę |
|---|---|---|---|---|---|
| 200 | 10 | 1 | 20,00 | 220,00 | 220,00 |
| 150 | 15 | 3 | 22,50 | 172,50 | 57,50 |
| 87,40 | 20 | 2 | 17,48 | 104,88 | 52,44 |
| 99 | 15 | 4 | 14,85 | 113,85 | 28,46 |
| abc | 15 | 2 | 0,00 | 0,00 | 0,00 |

??? question "Podpowiedź: przecinek czy kropka?"
    Emulator ma zwykle ustawiony język angielski, w którym separatorem jest kropka. Przyjmij oba zapisy:
    ```csharp
    private decimal Kwota =>
        decimal.TryParse(Rachunek?.Replace(',', '.'), NumberStyles.Number,
                         CultureInfo.InvariantCulture, out decimal k) && k > 0 ? k : 0;
    ```
    Potrzebujesz `using System.Globalization;`.

??? question "Podpowiedź: polecenie bez parametru"
    ```csharp
    WyczyscCommand = new Command(() =>
    {
        Rachunek = "";
        Procent = 10;
        LiczbaOsob = 1;
    });
    ```

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Dodaj model `Rachunek` (kwota, procent, osoby, data) i listę **Historia** (`CollectionView` wiązana z `ObservableCollection<Rachunek>` w ViewModelu). Przycisk **ZAPISZ** dodaje bieżący rachunek do historii i jest nieaktywny, gdy kwota wynosi 0. Użyj drugiego argumentu konstruktora `Command` (`canExecute`) i metody `ChangeCanExecute()`.

## Czy potrafię…?

- [ ] wymienić trzy warstwy MVVM i powiedzieć, co należy do każdej z nich
- [ ] napisać ViewModel z właściwościami i właściwościami wyliczanymi
- [ ] podłączyć przycisk do polecenia przez `Command`
- [ ] przekazać wartość do polecenia przez `CommandParameter`
