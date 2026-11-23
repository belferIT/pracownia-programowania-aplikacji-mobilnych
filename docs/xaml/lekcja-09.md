# Lekcja 9. Style i zasoby

<p class="lekcja-meta">Dział: XAML i układy · 45 min · Efekty: INF.04.6 (2) kryt. 5, INF.04.3 (6) kryt. 4 · <span class="zakres zakres-p">INF.04</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- zdefiniować kolor i rozmiar jako zasób i użyć go wiele razy,
- utworzyć styl dla wszystkich kontrolek danego typu oraz styl z nazwą,
- wskazać, gdzie w projekcie są style globalne.

## Wprowadzenie

Gdy ten sam kolor powtarza się w 20 miejscach, jego zmiana jest uciążliwa. Zasoby (`ResourceDictionary`) pozwalają zapisać wartość **raz**.

```xml
<ContentPage.Resources>
    <Color x:Key="Glowny">#4527A0</Color>
    <Color x:Key="Akcent">#FF9800</Color>
    <x:Double x:Key="DuzaCzcionka">24</x:Double>

    <!-- styl jawny (z kluczem) -->
    <Style x:Key="PrzyciskAkcent" TargetType="Button">
        <Setter Property="BackgroundColor" Value="{StaticResource Akcent}" />
        <Setter Property="TextColor" Value="White" />
        <Setter Property="CornerRadius" Value="12" />
    </Style>

    <!-- styl niejawny (bez klucza): działa na WSZYSTKIE Label na stronie -->
    <Style TargetType="Label">
        <Setter Property="TextColor" Value="{StaticResource Glowny}" />
        <Setter Property="FontSize" Value="16" />
    </Style>
</ContentPage.Resources>

<VerticalStackLayout Padding="20" Spacing="10">
    <Label Text="Tytuł" FontSize="{StaticResource DuzaCzcionka}" />
    <Button Text="Zapisz" Style="{StaticResource PrzyciskAkcent}" />
</VerticalStackLayout>
```

| Gdzie zdefiniujesz zasób | Zasięg |
|---|---|
| `<Kontrolka.Resources>` | ta kontrolka i jej dzieci |
| `<ContentPage.Resources>` | jedna strona |
| `App.xaml` → `Application.Resources` | cała aplikacja |
| `Resources/Styles/Colors.xaml` i `Styles.xaml` | cała aplikacja (dołączone w `App.xaml`) |

!!! info "Dziedziczenie stylów"
    `BasedOn` tworzy styl na podstawie innego: `<Style x:Key="PrzyciskUsun" TargetType="Button" BasedOn="{StaticResource PrzyciskAkcent}">` i zmienia tylko kolor tła.

!!! tip "Wartość z atrybutu wygrywa"
    Atrybut wpisany wprost w kontrolce (`TextColor="Red"`) ma pierwszeństwo przed stylem.

## Zadanie główne (25 min)

Utwórz projekt `Menu` z ekranem menu restauracji.

1. Otwórz `Resources/Styles/Colors.xaml`. Zmień wartość koloru `Primary` na `#4527A0`. Dodaj nowe kolory: `Akcent` = `#FF9800`, `TloKarty` = `#EDE7F6`. Uruchom aplikację i zobacz, jak zmienił się kolor domyślnych przycisków.
2. W `MainPage.xaml` w `ContentPage.Resources` utwórz:
    1. styl niejawny dla `Label`: rozmiar `16`, kolor `#212121`,
    2. styl `Naglowek` dla `Label`: rozmiar `26`, pogrubiony, kolor `{StaticResource Primary}`,
    3. styl `Cena` dla `Label`: pogrubiony, kolor `{StaticResource Akcent}`, wyrównany do prawej,
    4. styl `Karta` dla `Border`: tło `{StaticResource TloKarty}`, `Padding` `12`, `StrokeShape` `RoundRectangle 10`, bez obramowania (`StrokeThickness` `0`).
3. Wykonaj ekran: nagłówek **Menu dnia** (styl `Naglowek`), pod nim **4 karty** (styl `Karta`) z daniami. W karcie `Grid` z dwiema kolumnami `*,Auto`: nazwa dania w lewej kolumnie i cena w prawej (styl `Cena`).
4. Na dole przycisk **Zamów** ze stylem `PrzyciskAkcent` z przykładu.
5. Zmień kolor `Akcent` w `Colors.xaml` na `#E65100` i sprawdź, że zmieniły się wszystkie ceny i przycisk.

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Przenieś style `Naglowek`, `Cena` i `Karta` do `Resources/Styles/Styles.xaml`, aby można ich było użyć na każdej stronie. Dodaj styl `PrzyciskUsun` dziedziczący po `PrzyciskAkcent` (tło `#D32F2F`).

## Czy potrafię…?

- [ ] zdefiniować kolor jako zasób i użyć go przez `StaticResource`
- [ ] odróżnić styl jawny (z `x:Key`) od niejawnego
- [ ] wskazać plik z kolorami całej aplikacji
- [ ] utworzyć styl dziedziczący po innym (`BasedOn`)
