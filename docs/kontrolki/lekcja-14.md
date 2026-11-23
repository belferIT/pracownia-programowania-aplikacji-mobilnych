# Lekcja 14. Wartości z zakresu: Slider, Stepper, ProgressBar

<p class="lekcja-meta">Dział: Kontrolki i wiązanie danych · 45 min · Efekty: INF.04.6 (2) kryt. 4, 6 · <span class="zakres zakres-p">INF.04</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- pobrać liczbę z zakresu suwakiem `Slider` i przyciskami `Stepper`,
- pokazać postęp paskiem `ProgressBar`,
- zbudować kolor z wartości RGB i zapisać go szesnastkowo.

## Wprowadzenie

| Kontrolka | Właściwości | Zdarzenie |
|---|---|---|
| `Slider` (suwak) | `Minimum`, `Maximum`, `Value`, `MinimumTrackColor`, `ThumbColor` | `ValueChanged` → `e.NewValue` |
| `Stepper` (− / +) | `Minimum`, `Maximum`, `Increment`, `Value` | `ValueChanged` → `e.NewValue` |
| `ProgressBar` | `Progress` od `0` do `1`, `ProgressColor` | – |

```xml
<Slider x:Name="sldCzerwony" Maximum="255" Minimum="0" Value="128"
        MinimumTrackColor="Red" ValueChanged="OnKolorZmieniony" />

<Stepper x:Name="stpRozmiar" Maximum="60" Minimum="10" Increment="2" Value="20"
         ValueChanged="OnRozmiarZmieniony" />

<ProgressBar x:Name="pbPostep" Progress="0.5" ProgressColor="#FF9800" />
```

!!! warning "Kolejność Maximum i Minimum"
    Domyślnie `Maximum` = 1. Jeśli w XAML ustawisz najpierw `Minimum="10"`, będzie ono większe od `Maximum` i aplikacja zgłosi wyjątek. **Zawsze ustawiaj `Maximum` przed `Minimum`.**

```csharp
private void OnKolorZmieniony(object? sender, ValueChangedEventArgs e)
{
    int r = (int)sldCzerwony.Value;
    int g = (int)sldZielony.Value;
    int b = (int)sldNiebieski.Value;

    bxKolor.Color = Color.FromRgb(r, g, b);
    lblHex.Text = $"#{r:X2}{g:X2}{b:X2}";      // X2 = dwie cyfry szesnastkowe
}
```

!!! tip "Animowany pasek postępu"
    `await pbPostep.ProgressTo(0.75, 500, Easing.Linear);` płynnie przesuwa pasek do 75% w ciągu 500 ms.

## Zadanie główne (25 min)

Utwórz projekt `MieszalnikKolorow`.

1. Na górze `BoxView` o nazwie `bxKolor`: wysokość `150`, zaokrąglenie `CornerRadius="15"`, początkowy kolor `#808080`.
2. Etykieta `lblHex` pod podglądem: rozmiar `28`, pogrubiona, wyśrodkowana, tekst `#808080`.
3. Trzy wiersze (`Grid` z kolumnami `40,*,50`): litera **R**/**G**/**B**, suwak 0–255 (wartość początkowa 128), etykieta z bieżącą wartością liczbową. Suwaki mają kolor ścieżki odpowiednio czerwony, zielony i niebieski.
4. Wszystkie suwaki wywołują jedną metodę, która aktualizuje kolor, napis szesnastkowy i trzy etykiety z wartościami.
5. Pod spodem `Stepper` (10–60, krok 2, start 28) i etykieta **Rozmiar napisu: 28**. Stepper zmienia `FontSize` etykiety `lblHex`.
6. Na dole `ProgressBar` pokazujący jasność koloru: `(r + g + b) / 765.0`.
7. Gdy jasność jest mniejsza niż 0,4, tekst `lblHex` jest biały i ma tło `#212121`; w przeciwnym razie czarny na białym tle.

Sprawdź: R = 255, G = 152, B = 0 → `#FF9800`; R = 69, G = 39, B = 160 → `#4527A0` (tekst biały na ciemnym tle).

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Dodaj pole `Entry`, do którego można wpisać kod koloru `#RRGGBB`. Po naciśnięciu Enter (`Completed`) ustaw suwaki na odpowiednie wartości (`Convert.ToInt32("FF", 16)` zamienia tekst szesnastkowy na liczbę). Błędny kod ignoruj.

## Czy potrafię…?

- [ ] ustawić zakres suwaka i odczytać jego wartość
- [ ] użyć `Stepper` z krokiem większym niż 1
- [ ] zbudować kolor z wartości RGB
- [ ] zapisać liczbę szesnastkowo w formacie `X2`
