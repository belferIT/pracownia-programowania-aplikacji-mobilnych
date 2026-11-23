# Lekcja 4. Składnia XAML: etykiety i przyciski

<p class="lekcja-meta">Dział: XAML i układy · 45 min · Efekty: INF.04.6 (2) kryt. 5 · <span class="zakres zakres-p">INF.04</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- odczytać budowę pliku XAML: element, atrybut, element właściwości,
- ustawić tekst, kolor, rozmiar i styl czcionki etykiety,
- nadać kontrolce nazwę `x:Name`, żeby odwołać się do niej w C#.

## Wprowadzenie

XAML (*eXtensible Application Markup Language*) to język znaczników oparty na XML. Każdy element XAML to **obiekt** klasy C#, a każdy atrybut to **właściwość** tego obiektu.

```xml
<ContentPage xmlns="http://schemas.microsoft.com/dotnet/2021/maui"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             x:Class="Wizytowka.MainPage"
             BackgroundColor="#EDE7F6">

    <VerticalStackLayout Padding="20" Spacing="10">
        <Label x:Name="lblImie"
               Text="Anna Nowak"
               FontSize="32"
               FontAttributes="Bold"
               TextColor="#4527A0"
               HorizontalOptions="Center" />

        <Button Text="Zadzwoń"
                BackgroundColor="#FF9800"
                TextColor="White"
                CornerRadius="20" />
    </VerticalStackLayout>
</ContentPage>
```

| Zapis | Znaczenie |
|---|---|
| `<Label ... />` | utwórz obiekt klasy `Label` |
| `Text="Anna Nowak"` | ustaw właściwość `Text` |
| `x:Name="lblImie"` | nazwa pola w C# (`lblImie.Text = "..."`) |
| `x:Class` | klasa C#, z którą połączony jest plik (przestrzeń nazw = nazwa projektu) |
| `FontAttributes="Bold,Italic"` | pogrubienie i kursywa jednocześnie |

Najważniejsze właściwości etykiety `Label`: `Text`, `FontSize`, `FontAttributes`, `FontFamily`, `TextColor`, `BackgroundColor`, `HorizontalTextAlignment`, `TextDecorations` (`Underline`, `Strikethrough`), `LineBreakMode`, `MaxLines`.

!!! info "Element właściwości"
    Złożoną wartość wpisujesz jako element zagnieżdżony `<Klasa.Właściwość>`. Przykład: etykieta z fragmentami w różnych kolorach:

    ```xml
    <Label FontSize="18">
        <Label.FormattedText>
            <FormattedString>
                <Span Text="Telefon: " />
                <Span Text="600 100 200" TextColor="#FF9800" FontAttributes="Bold" />
            </FormattedString>
        </Label.FormattedText>
    </Label>
    ```

!!! tip "Konwencja nazw"
    Kontrolkom nadawaj nazwy z przedrostkiem typu: `lblWynik` (Label), `btnOblicz` (Button), `entWaga` (Entry), `imgZdjecie` (Image). Na egzaminie liczy się czytelność kodu i znaczące nazwy.

## Zadanie główne (25 min)

Utwórz projekt `Wizytowka` (szablon **Aplikacja .NET MAUI**). W `MainPage.xaml` usuń całą zawartość `ScrollView` i wykonaj wizytówkę:

1. Tło strony: `#EDE7F6`.
2. Kontener `VerticalStackLayout` z odstępem wewnętrznym `30` i odstępem między elementami `12`.
3. Etykieta z Twoim imieniem i nazwiskiem: rozmiar `32`, pogrubiona, kolor `#4527A0`, wyśrodkowana.
4. Etykieta **Technik programista**: rozmiar `20`, kursywa, kolor `#616161`, wyśrodkowana.
5. Etykieta z adresem e-mail (wymyślonym), podkreślona (`TextDecorations="Underline"`), kolor `#1565C0`.
6. Etykieta z tekstem z `FormattedText`: **Zainteresowania:** (pogrubione) i dalej trzy Twoje zainteresowania zwykłą czcionką.
7. Przycisk **Kontakt**: tło `#FF9800`, tekst biały, zaokrąglenie `20`, szerokość `200` (`WidthRequest`), wyśrodkowany.
8. W pliku `MainPage.xaml.cs` usuń metodę `OnCounterClicked` i pole `count`, a w XAML nie zostawiaj odwołania `Clicked`. Uruchom aplikację w emulatorze.

??? question "Podpowiedź: błąd XFC0000 / nie znaleziono metody"
    Jeśli w XAML został atrybut `Clicked="OnCounterClicked"`, a w C# nie ma tej metody, projekt się nie skompiluje. Usuń atrybut albo przywróć metodę.

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Dodaj do wizytówki własną czcionkę: pobierz z Google Fonts plik `.ttf` (np. *Pacifico*), skopiuj go do `Resources/Fonts` i zarejestruj w `MauiProgram.cs` w `ConfigureFonts`: `fonts.AddFont("Pacifico-Regular.ttf", "Pacifico");`. Użyj jej w etykiecie z imieniem: `FontFamily="Pacifico"`.

## Czy potrafię…?

- [ ] wyjaśnić, że element XAML to obiekt, a atrybut to właściwość
- [ ] ustawić rozmiar, kolor i styl czcionki etykiety
- [ ] użyć elementu właściwości (`Label.FormattedText`)
- [ ] nadać kontrolce nazwę `x:Name` zgodnie z konwencją
