# Lekcja 21. Listy: CollectionView

<p class="lekcja-meta">Dział: Kontrolki i wiązanie danych · 45 min · Efekty: INF.04.6 (2) kryt. 4, 6 · <span class="zakres zakres-p">INF.04</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- wyświetlić listę obiektów w `CollectionView`,
- zaprojektować wygląd jednego elementu listy (`ItemTemplate`),
- użyć `ObservableCollection`, aby lista odświeżała się sama,
- zareagować na wybór elementu.

## Wprowadzenie

```csharp
public class Miasto
{
    public string Nazwa { get; set; } = "";
    public string Wojewodztwo { get; set; } = "";
    public int Ludnosc { get; set; }
}
```

```xml
<CollectionView x:Name="cvMiasta" SelectionMode="Single"
                SelectionChanged="OnMiastoWybrane">
    <CollectionView.ItemTemplate>
        <DataTemplate x:DataType="local:Miasto">
            <Grid Padding="10" ColumnDefinitions="*,Auto">
                <VerticalStackLayout>
                    <Label Text="{Binding Nazwa}" FontSize="20" FontAttributes="Bold" />
                    <Label Text="{Binding Wojewodztwo}" TextColor="Gray" />
                </VerticalStackLayout>
                <Label Grid.Column="1" Text="{Binding Ludnosc, StringFormat='{0:N0}'}"
                       VerticalOptions="Center" />
            </Grid>
        </DataTemplate>
    </CollectionView.ItemTemplate>
</CollectionView>
```

```csharp
using System.Collections.ObjectModel;

private readonly ObservableCollection<Miasto> miasta = new()
{
    new Miasto { Nazwa = "Szczecin", Wojewodztwo = "zachodniopomorskie", Ludnosc = 391566 },
    new Miasto { Nazwa = "Goleniów", Wojewodztwo = "zachodniopomorskie", Ludnosc = 22104 },
};

public MainPage()
{
    InitializeComponent();
    cvMiasta.ItemsSource = miasta;
}

private async void OnMiastoWybrane(object? sender, SelectionChangedEventArgs e)
{
    if (e.CurrentSelection.FirstOrDefault() is Miasto m)
    {
        await DisplayAlertAsync(m.Nazwa, $"Ludność: {m.Ludnosc:N0}", "OK");
        cvMiasta.SelectedItem = null;   // odznacz
    }
}
```

| Element | Znaczenie |
|---|---|
| `ItemsSource` | kolekcja danych |
| `ItemTemplate` / `DataTemplate` | wygląd **jednego** elementu; `{Binding Nazwa}` odnosi się do właściwości obiektu |
| `SelectionMode` | `None`, `Single`, `Multiple` |
| `EmptyView="Brak danych"` | tekst, gdy lista jest pusta |
| `ObservableCollection<T>` | lista, która powiadamia widok o dodaniu i usunięciu elementów |

!!! warning "ListView jest przestarzały"
    W .NET 10 kontrolka `ListView` i komórki (`TextCell`, `ViewCell`…) są oznaczone jako przestarzałe. W starszych materiałach i arkuszach możesz je spotkać – w nowych projektach używaj `CollectionView`.

!!! info "Liczby w danych"
    Liczby ludności w zadaniu są przykładowe (zaokrąglone). Nie traktuj ich jako danych statystycznych.

## Zadanie główne (25 min)

Utwórz projekt `Miasta` (przestrzeń nazw `Miasta`, w XAML `xmlns:local="clr-namespace:Miasta"`).

1. Dodaj klasę `Miasto` z właściwościami: `Nazwa`, `Wojewodztwo`, `Ludnosc`, `Powierzchnia` (km², `double`).
2. W `MainPage.xaml.cs` utwórz `ObservableCollection<Miasto>` z danymi:

| Nazwa | Województwo | Ludność | Powierzchnia |
|---|---|---|---|
| Warszawa | mazowieckie | 1 860 000 | 517,2 |
| Kraków | małopolskie | 805 000 | 326,8 |
| Gdańsk | pomorskie | 487 000 | 262,0 |
| Szczecin | zachodniopomorskie | 390 000 | 300,6 |
| Goleniów | zachodniopomorskie | 22 000 | 63,8 |

3. Wyświetl listę: nazwa (20, pogrubiona), województwo (szary), ludność po prawej z separatorem tysięcy. Elementy oddziel `BoxView` o wysokości 1 lub umieść w `Border`.
4. Nad listą nagłówek **Miasta Polski** i etykieta `lblLiczba` z tekstem **Liczba miast: 5**.
5. Po wybraniu miasta wyświetl `DisplayAlertAsync` z gęstością zaludnienia: **Gęstość: N os./km²** (bez miejsc po przecinku) i odznacz wybór.
6. Dodaj przycisk **Sortuj wg ludności**, który ustawia nową kolekcję posortowaną malejąco: `cvMiasta.ItemsSource = new ObservableCollection<Miasto>(miasta.OrderByDescending(m => m.Ludnosc));`.

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Dodaj `SearchBar` nad listą. Przy każdej zmianie tekstu (`TextChanged`) pokazuj tylko miasta, których nazwa zawiera wpisany tekst bez względu na wielkość liter: `m.Nazwa.Contains(tekst, StringComparison.OrdinalIgnoreCase)`. Ustaw `EmptyView`.

## Czy potrafię…?

- [ ] wyświetlić listę obiektów w `CollectionView`
- [ ] zaprojektować szablon elementu z wiązaniami
- [ ] obsłużyć wybór elementu i odznaczyć go
- [ ] wyjaśnić, czym `ObservableCollection` różni się od `List`
