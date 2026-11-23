# Lekcja 6. Układ siatki Grid

<p class="lekcja-meta">Dział: XAML i układy · 45 min · Efekty: INF.04.6 (2) kryt. 5, 6 · <span class="zakres zakres-p">INF.04</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- podzielić ekran na wiersze i kolumny,
- dobrać rozmiar wiersza lub kolumny: stały, `Auto`, `*`,
- umieścić kontrolkę w komórce i rozciągnąć ją na kilka komórek.

## Wprowadzenie

`Grid` dzieli obszar na wiersze (`RowDefinitions`) i kolumny (`ColumnDefinitions`). Kontrolkę umieszczasz w komórce właściwościami dołączonymi `Grid.Row` i `Grid.Column` (numeracja **od 0**).

| Rozmiar | Znaczenie |
|---|---|
| `100` | stały rozmiar 100 jednostek |
| `Auto` | tyle, ile potrzebuje zawartość |
| `*` | cała pozostała przestrzeń |
| `2*` | dwa razy więcej niż `*` |

```xml
<Grid RowDefinitions="Auto,*,60"
      ColumnDefinitions="*,*"
      RowSpacing="10" ColumnSpacing="10" Padding="10">

    <Label Text="Nagłówek" Grid.Row="0" Grid.ColumnSpan="2"
           HorizontalOptions="Center" FontSize="24" />

    <BoxView Color="#B39DDB" Grid.Row="1" Grid.Column="0" />
    <BoxView Color="#FFCC80" Grid.Row="1" Grid.Column="1" />

    <Button Text="OK" Grid.Row="2" Grid.Column="0" />
    <Button Text="Anuluj" Grid.Row="2" Grid.Column="1" />
</Grid>
```

```text
+--------------------------------+
|          Nagłówek              |  Auto
+---------------+----------------+
|               |                |
|   #B39DDB     |    #FFCC80     |  *
|               |                |
+---------------+----------------+
|      OK       |     Anuluj     |  60
+---------------+----------------+
       *                *
```

!!! tip "Pominięte Grid.Row i Grid.Column"
    Jeśli nie podasz `Grid.Row` lub `Grid.Column`, kontrolka trafia do wiersza 0 i kolumny 0. Dwie kontrolki w tej samej komórce **nakładają się** – na egzaminie to błąd.

## Zadanie główne (25 min)

Utwórz projekt `Klawiatura` i wykonaj ekran kalkulatora (bez działania) zgodnie z rysunkiem 1.

```text
Rysunek 1. Ekran kalkulatora

+---------------------------------------+
|                                    0  |   <- Label, wiersz Auto, 48, do prawej
+---------+---------+---------+---------+
|    7    |    8    |    9    |    ÷    |
+---------+---------+---------+---------+
|    4    |    5    |    6    |    ×    |
+---------+---------+---------+---------+
|    1    |    2    |    3    |    −    |
+---------+---------+---------+---------+
|    0              |    ,    |    +    |   <- "0" zajmuje 2 kolumny
+-------------------+---------+---------+
|                   =                   |   <- zajmuje 4 kolumny
+---------------------------------------+
```

1. `Grid` z 6 wierszami: pierwszy `Auto`, pozostałe `*`. 4 kolumny `*`. Odstępy `RowSpacing` i `ColumnSpacing` po `8`, `Padding="12"`.
2. Wyświetlacz: `Label` z nazwą `lblWyswietlacz`, tekst `0`, rozmiar `48`, wyrównany do prawej, rozciągnięty na 4 kolumny.
3. Przyciski cyfr: tło `#EDE7F6`, tekst `#311B92`, rozmiar czcionki `24`.
4. Przyciski działań (`÷ × − +`): tło `#FF9800`, tekst biały, rozmiar `24`.
5. Przycisk `0` zajmuje 2 kolumny, przycisk `=` zajmuje 4 kolumny i ma tło `#4527A0`.
6. Przyciski wypełniają komórki (domyślnie tak jest). Uruchom aplikację i obróć emulator do poziomu. Sprawdź, czy układ się dopasowuje.

??? question "Podpowiedź: znaki ÷ × −"
    Wpisz je bezpośrednio w XAML (plik jest w UTF-8) albo jako encje: `&#247;` (÷), `&#215;` (×), `&#8722;` (−).

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Dodaj nad przyciskiem `7` wiersz z przyciskami `C`, `±`, `%` i `⌫`. Zmień wysokość wyświetlacza tak, aby zajmował zawsze 25% wysokości ekranu (podpowiedź: wiersze `*` i `3*`… policz proporcje).

## Czy potrafię…?

- [ ] zdefiniować wiersze i kolumny siatki skróconym zapisem
- [ ] odróżnić rozmiary `Auto`, `*` i stały
- [ ] umieścić kontrolkę w wybranej komórce
- [ ] rozciągnąć kontrolkę na kilka kolumn lub wierszy
