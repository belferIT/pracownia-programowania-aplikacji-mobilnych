# Lekcja 19. BindingContext i INotifyPropertyChanged

<p class="lekcja-meta">Dział: Kontrolki i wiązanie danych · 45 min · Efekty: INF.04.6 (2) kryt. 5, 6 · <span class="zakres zakres-p">INF.04</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- powiązać kontrolki z właściwościami obiektu klasy C#,
- ustawić `BindingContext` strony,
- zaimplementować interfejs `INotifyPropertyChanged`, aby widok odświeżał się sam.

## Wprowadzenie

Wiązanie bez `Source` szuka danych w **kontekście wiązania** (`BindingContext`). Ustawiasz go raz dla strony, a wszystkie kontrolki „widzą” właściwości tego obiektu.

=== "KalkulatorBmi.cs"

    ```csharp
    using System.ComponentModel;
    using System.Runtime.CompilerServices;

    public class KalkulatorBmi : INotifyPropertyChanged
    {
        private double waga = 70;
        private double wzrost = 175;

        public double Waga
        {
            get => waga;
            set
            {
                if (waga == value) return;
                waga = value;
                OnPropertyChanged();               // zmieniła się Waga
                OnPropertyChanged(nameof(Bmi));    // więc zmieniło się też BMI
            }
        }

        public double Wzrost { /* analogicznie jak Waga */ }

        public double Bmi => Waga / Math.Pow(Wzrost / 100, 2);

        public event PropertyChangedEventHandler? PropertyChanged;

        protected void OnPropertyChanged([CallerMemberName] string? nazwa = null)
        {
            PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(nazwa));
        }
    }
    ```

=== "MainPage.xaml"

    ```xml
    <ContentPage ...
                 xmlns:local="clr-namespace:Bmi"
                 x:DataType="local:KalkulatorBmi">

        <VerticalStackLayout Padding="20" Spacing="10">
            <Label Text="{Binding Waga, StringFormat='Waga: {0:F0} kg'}" />
            <Slider Maximum="150" Minimum="40" Value="{Binding Waga}" />
            <Label Text="{Binding Bmi, StringFormat='BMI: {0:F2}'}" FontSize="28" />
        </VerticalStackLayout>
    </ContentPage>
    ```

=== "MainPage.xaml.cs"

    ```csharp
    public MainPage()
    {
        InitializeComponent();
        BindingContext = new KalkulatorBmi();
    }
    ```

| Pojęcie | Znaczenie |
|---|---|
| `BindingContext` | obiekt, z którego wiązania pobierają dane |
| `INotifyPropertyChanged` | interfejs z zdarzeniem `PropertyChanged`: „zmieniła się właściwość X” |
| `[CallerMemberName]` | kompilator sam wstawia nazwę właściwości, z której wywołano metodę |
| `x:DataType` | typ kontekstu: wiązania są sprawdzane przy kompilacji i działają szybciej |

!!! warning "Bez powiadomienia nie ma odświeżenia"
    Jeśli zmienisz pole `waga` bez wywołania `OnPropertyChanged`, etykiety nie zmienią się, choć wartość w obiekcie jest nowa.

## Zadanie główne (25 min)

Utwórz projekt `Bmi` (przestrzeń nazw `Bmi`).

1. Dodaj klasę `KalkulatorBmi` (prawy przycisk na projekcie → **Dodaj → Klasa**) z właściwościami `Waga` (start 70), `Wzrost` (start 175), `Bmi` i `Kategoria`.
2. `Kategoria` zwraca tekst: **niedowaga** (BMI < 18,5), **waga prawidłowa** (18,5 ≤ BMI < 25), **nadwaga** (25 ≤ BMI < 30), **otyłość** (BMI ≥ 30).
3. Zmiana `Waga` lub `Wzrost` powiadamia o zmianie samej siebie oraz `Bmi` i `Kategoria`.
4. Ekran: etykieta wagi i suwak 40–150 kg, etykieta wzrostu i suwak 140–210 cm, duża etykieta z BMI (2 miejsca po przecinku) i etykieta z kategorią. Wszystko przez wiązania, bez zdarzeń.
5. W konstruktorze strony ustaw `BindingContext`. Dodaj `x:DataType` w XAML.
6. Sprawdź:

| Waga | Wzrost | BMI | Kategoria |
|---|---|---|---|
| 70 | 175 | 22,86 | waga prawidłowa |
| 50 | 170 | 17,30 | niedowaga |
| 90 | 180 | 27,78 | nadwaga |
| 110 | 175 | 35,92 | otyłość |

??? question "Podpowiedź: suwak ustawia wartości ułamkowe"
    Suwak przesuwa się płynnie (np. 70,4). Zaokrąglaj wartość w seterze: `waga = Math.Round(value);`.

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Dodaj właściwość `Wiek` (Stepper 1–100) i właściwość `CzyDorosly`. Dla osób poniżej 18 lat zamiast kategorii wyświetl napis **Dla dzieci i młodzieży BMI ocenia się na siatkach centylowych**.

## Czy potrafię…?

- [ ] ustawić `BindingContext` strony
- [ ] napisać właściwość z powiadomieniem o zmianie
- [ ] powiadomić o zmianie właściwości wyliczanej
- [ ] wyjaśnić, do czego służy `x:DataType`
