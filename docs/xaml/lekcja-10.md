# Lekcja 10. Zdarzenia: obsługa kliknięcia

<p class="lekcja-meta">Dział: XAML i układy · 45 min · Efekty: INF.04.6 (2) kryt. 6 · <span class="zakres zakres-p">INF.04</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- podłączyć metodę do zdarzenia `Clicked` przycisku,
- zmieniać właściwości kontrolek z kodu C#,
- przechowywać stan aplikacji w polu klasy.

## Wprowadzenie

Zdarzenie podłączasz w XAML atrybutem z nazwą metody. Metoda jest w pliku `.xaml.cs`.

=== "XAML"

    ```xml
    <VerticalStackLayout Padding="20" Spacing="15">
        <Label x:Name="lblLicznik" Text="0" FontSize="64"
               HorizontalOptions="Center" />
        <HorizontalStackLayout Spacing="10" HorizontalOptions="Center">
            <Button x:Name="btnMinus" Text="−" Clicked="OnMinusClicked" />
            <Button x:Name="btnPlus" Text="+" Clicked="OnPlusClicked" />
        </HorizontalStackLayout>
    </VerticalStackLayout>
    ```

=== "C#"

    ```csharp
    public partial class MainPage : ContentPage
    {
        private int licznik = 0;   // stan aplikacji: pole klasy

        public MainPage()
        {
            InitializeComponent();
        }

        private void OnPlusClicked(object? sender, EventArgs e)
        {
            licznik++;
            OdswiezWidok();
        }

        private void OnMinusClicked(object? sender, EventArgs e)
        {
            if (licznik > 0)
            {
                licznik--;
            }
            OdswiezWidok();
        }

        private void OdswiezWidok()
        {
            lblLicznik.Text = licznik.ToString();
            lblLicznik.TextColor = licznik >= 10 ? Colors.Red : Colors.Black;
        }
    }
    ```

| Element metody | Znaczenie |
|---|---|
| `object? sender` | kontrolka, która wywołała zdarzenie |
| `EventArgs e` | dodatkowe dane zdarzenia |
| `Colors.Red` | kolor z gotowej palety; własny: `Color.FromArgb("#4527A0")` |
| `IsVisible`, `IsEnabled` | ukrycie lub zablokowanie kontrolki z kodu |

!!! tip "Szybkie tworzenie metody"
    Wpisz w XAML `Clicked="` i wybierz z podpowiedzi **&lt;Nowa procedura obsługi zdarzeń&gt;**. Visual Studio utworzy metodę w `.xaml.cs`. Potem zmień jej nazwę na znaczącą.

!!! info "Jedna metoda dla wielu przycisków"
    ```csharp
    private void OnCyfraClicked(object? sender, EventArgs e)
    {
        Button przycisk = (Button)sender!;
        lblWynik.Text += przycisk.Text;
    }
    ```

## Zadanie główne (25 min)

Utwórz projekt `LicznikWody` – aplikację, która liczy wypite szklanki wody.

1. Na górze etykieta **Dzienny licznik wody**, rozmiar `24`, pogrubiona, kolor `#1565C0`.
2. Etykieta `lblSzklanki` z liczbą szklanek, rozmiar `72`, wyśrodkowana, początkowo `0`.
3. Etykieta `lblLitry` z tekstem **Wypito: 0,00 l** (jedna szklanka = 0,25 l).
4. Trzy przyciski obok siebie: **−1**, **+1**, **Zeruj**.
5. Przycisk **+1** zwiększa licznik o 1, **−1** zmniejsza (ale nie poniżej 0), **Zeruj** ustawia 0.
6. Po każdej zmianie aktualizuj obie etykiety. Litry formatuj z dwoma miejscami po przecinku: `$"Wypito: {litry:F2} l"`.
7. Gdy liczba szklanek osiągnie **8**, pokaż (`IsVisible = true`) ukrytą wcześniej etykietę **Cel dzienny osiągnięty!** w kolorze `#2E7D32`. Poniżej 8 – ukryj ją.
8. Przycisk **−1** jest nieaktywny (`IsEnabled = false`), gdy licznik wynosi 0.

Sprawdź działanie: 3 × **+1** → **Wypito: 0,75 l** (w emulatorze z angielskim systemem: 0.75); 8 × **+1** → widać napis o celu; **−1** → napis znika; **Zeruj** → przycisk **−1** nieaktywny.

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Dodaj pasek postępu `ProgressBar` pokazujący realizację celu (8 szklanek = 100%): `pasek.Progress = szklanki / 8.0;`. Uważaj, aby wartość nie przekroczyła 1.

## Czy potrafię…?

- [ ] podłączyć metodę do zdarzenia `Clicked`
- [ ] zmienić tekst, kolor i widoczność kontrolki z C#
- [ ] przechowywać stan w polu klasy
- [ ] użyć jednej metody dla kilku przycisków
