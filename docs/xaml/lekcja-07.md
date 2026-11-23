# Lekcja 7. FlexLayout, AbsoluteLayout, ScrollView i Border

<p class="lekcja-meta">Dział: XAML i układy · 45 min · Efekty: INF.04.6 (2) kryt. 5, 6 · <span class="zakres zakres-p">INF.04</span> <span class="zakres zakres-gw">P+</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- ułożyć elementy z zawijaniem do kolejnej linii (`FlexLayout`),
- umieścić element w dokładnym miejscu (`AbsoluteLayout`),
- przewijać długą zawartość (`ScrollView`),
- obramować i zaokrąglić grupę kontrolek (`Border`).

## Wprowadzenie

| Układ | Kiedy użyć |
|---|---|
| `FlexLayout` | kafelki, tagi, przyciski, które mają się zawijać (jak flexbox w CSS) |
| `AbsoluteLayout` | elementy nakładane na siebie: plakietka na zdjęciu, przycisk „pływający” |
| `ScrollView` | zawartość dłuższa niż ekran; ma **jedno** dziecko |
| `Border` | ramka, zaokrąglone rogi, cień wokół jednego elementu (zastępuje przestarzały `Frame`) |

```xml
<FlexLayout Wrap="Wrap" JustifyContent="SpaceEvenly" AlignItems="Center">
    <Border WidthRequest="140" HeightRequest="90" Margin="5"
            Stroke="#4527A0" StrokeThickness="2" BackgroundColor="#EDE7F6"
            StrokeShape="RoundRectangle 12">
        <Label Text="C#" HorizontalOptions="Center" VerticalOptions="Center" />
    </Border>
    <!-- kolejne kafelki -->
</FlexLayout>
```

| Właściwość `FlexLayout` | Wartości |
|---|---|
| `Direction` | `Row`, `Column` |
| `Wrap` | `NoWrap`, `Wrap` |
| `JustifyContent` | `Start`, `Center`, `End`, `SpaceBetween`, `SpaceAround`, `SpaceEvenly` |
| `AlignItems` | `Start`, `Center`, `End`, `Stretch` |

### AbsoluteLayout

```xml
<AbsoluteLayout>
    <BoxView Color="#B39DDB" AbsoluteLayout.LayoutBounds="0,0,1,1"
             AbsoluteLayout.LayoutFlags="All" />
    <Button Text="+" CornerRadius="30"
            AbsoluteLayout.LayoutBounds="0.95,0.95,60,60"
            AbsoluteLayout.LayoutFlags="PositionProportional" />
</AbsoluteLayout>
```

`LayoutBounds="x,y,szerokość,wysokość"`. Flaga `PositionProportional` oznacza, że `x` i `y` to ułamki (0–1) wolnego miejsca, a rozmiar jest w jednostkach.

!!! warning "Egzamin"
    Na egzaminie zwykle wymagany jest układ liniowy (Stack) lub siatka. `AbsoluteLayout` stosuj tylko tam, gdzie elementy **mają** się nakładać.

## Zadanie główne (25 min)

Utwórz projekt `Kafelki`.

1. Strona zawiera `ScrollView`, a w nim `VerticalStackLayout` z `Padding="15"` i `Spacing="15"`.
2. Nagłówek **Moje umiejętności**: rozmiar `26`, pogrubiony, kolor `#4527A0`.
3. `FlexLayout` z zawijaniem i `JustifyContent="SpaceEvenly"`, a w nim **10 kafelków** (`Border`): szerokość `140`, wysokość `80`, margines `5`, tło `#EDE7F6`, obramowanie `#4527A0` grubości `2`, zaokrąglenie `RoundRectangle 12`. W każdym kafelku etykieta z nazwą technologii (C#, XAML, SQL, Git, HTML, CSS, JS, Python, Java, Android), wyśrodkowana.
4. Pod kafelkami `Border` z tłem `#FFF3E0`, obramowaniem `#FF9800`, zaokrągleniem `20` i `Padding="15"`, a w nim etykieta z akapitem tekstu o sobie (min. 5 zdań).
5. Uruchom w emulatorze w pionie i w poziomie. Sprawdź, jak zmienia się liczba kafelków w wierszu i czy strona się przewija.

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Zamień `ScrollView` na `AbsoluteLayout` jako główny układ strony: `ScrollView` wypełnia całą stronę (`LayoutBounds="0,0,1,1"`, `LayoutFlags="All"`), a w prawym dolnym rogu znajduje się okrągły „pływający” przycisk **+** (60×60, tło `#FF9800`), który nie przewija się razem z treścią. Kafelkom dodaj cień: `<Border.Shadow><Shadow Brush="Black" Offset="3,3" Opacity="0.3" Radius="6" /></Border.Shadow>`.

## Czy potrafię…?

- [ ] ułożyć kafelki z zawijaniem w `FlexLayout`
- [ ] dodać przewijanie długiej zawartości
- [ ] obramować i zaokrąglić element za pomocą `Border`
- [ ] wyjaśnić, kiedy warto użyć `AbsoluteLayout`
