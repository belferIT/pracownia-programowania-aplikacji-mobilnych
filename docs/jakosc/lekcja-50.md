# Lekcja 50. Debugowanie

<p class="lekcja-meta">Dział: Jakość, testy i publikacja · 45 min · Efekty: INF.04.8 (1) kryt. 3, 4 · <span class="zakres zakres-p">INF.04</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- zatrzymać program w wybranym miejscu punktem przerwania,
- wykonywać kod krok po kroku i podglądać wartości zmiennych,
- odczytać wyjątek i znaleźć jego przyczynę,
- wypisywać komunikaty diagnostyczne do okna **Output**.

## Wprowadzenie

Błąd **kompilacji** widzisz w oknie **Lista błędów** i program się nie uruchomi. Trudniejsze są błędy, przy których program się kompiluje: **wyjątki** (program się wysypuje) i błędy **logiczne** (program działa, ale liczy źle). Do ich szukania służy debuger.

| Czynność | Jak | Klawisz |
|---|---|---|
| punkt przerwania | kliknij szary margines przy numerze wiersza (czerwona kropka) | ++f9++ |
| uruchom z debugowaniem | zielony trójkąt | ++f5++ |
| następny wiersz, bez wchodzenia do metod | **Step Over** | ++f10++ |
| wejdź do wywoływanej metody | **Step Into** | ++f11++ |
| kontynuuj do następnego punktu przerwania | **Continue** | ++f5++ |
| zakończ debugowanie | **Stop** | ++shift+f5++ |

Gdy program stoi na punkcie przerwania:

- najedź myszą na zmienną, aby zobaczyć jej wartość,
- okno **Zmienne lokalne** (*Locals*) pokazuje wszystkie zmienne metody, okno **Czujka** (*Watch*) – wyrażenia, które sam wpiszesz, np. `suma / oceny.Length`,
- **warunkowy punkt przerwania**: prawy przycisk na kropce → **Warunki**, np. `i == 3`.

```csharp
System.Diagnostics.Debug.WriteLine($"i = {i}, suma = {suma}");   // pojawi się w oknie Output
```

!!! tip "Wyjątek w debugerze"
    Gdy pojawi się wyjątek, Visual Studio zatrzyma program na wierszu, który go spowodował, i pokaże typ wyjątku. Najczęstsze: `NullReferenceException` (zmienna jest `null`), `IndexOutOfRangeException` (indeks poza tablicą), `FormatException` (`int.Parse` dostał tekst, który nie jest liczbą), `DivideByZeroException` (dzielenie całkowite przez 0).

## Zadanie główne (25 min)

Plik startowy: [debugowanie.zip](../pliki/lekcja-50/debugowanie.zip){ download }

Utwórz projekt `Debugowanie` i zastąp pliki `MainPage.xaml` oraz `MainPage.xaml.cs` plikami z archiwum. Aplikacja ma liczyć średnią ocen według specyfikacji:

- oceny wpisujesz w jednym polu, oddzielone spacjami,
- poprawna ocena to liczba całkowita 1–6; dla oceny spoza skali komunikat **Ocena 7 jest spoza skali 1–6**, dla tekstu, który nie jest liczbą: **Niepoprawna ocena: x**,
- dla pustego pola komunikat **Wpisz co najmniej jedną ocenę**,
- średnia z dwoma miejscami po przecinku, najwyższa ocena i wyróżnienie **TAK**, gdy średnia wynosi **co najmniej 4,75**.

W kodzie jest **pięć** błędów. Znajdź je debugerem, a nie tylko czytając kod.

1. Uruchom aplikację i wpisz `5 4 3 6`. Program się wysypie. Odczytaj typ wyjątku i wiersz.
2. Postaw punkt przerwania w pierwszym wierszu metody `OnObliczClicked`. Przejdź pętlę ++f10++ i obserwuj `i` w oknie **Zmienne lokalne**. Popraw błąd.
3. Sprawdź wszystkie dane z tabeli. Przy każdym złym wyniku użyj punktów przerwania i okna **Czujka**.
4. Każdy błąd zapisz w tabeli w zeszycie lub pliku: **wiersz – objaw – przyczyna – poprawka**.

| Wejście | Oczekiwany wynik |
|---|---|
| `5 4 3 6` | Średnia: 4,50, Najwyższa: 6, Wyróżnienie: NIE |
| `6 5 5` | Średnia: 5,33, Najwyższa: 6, Wyróżnienie: TAK |
| `4 5 5 5` | Średnia: 4,75, Najwyższa: 5, Wyróżnienie: TAK |
| `5 7` | Ocena 7 jest spoza skali 1–6 |
| `5 x` | Niepoprawna ocena: x |
| *(puste pole)* | Wpisz co najmniej jedną ocenę |

??? question "Podpowiedź: średnia 4,00 zamiast 4,50"
    W oknie **Czujka** wpisz `suma / oceny.Length` i `(double)suma / oceny.Length`. Porównaj typy wyników.

??? question "Podpowiedź: ocena 7 przechodzi"
    Czy liczba może być jednocześnie mniejsza od 1 **i** większa od 6?

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Przenieś obliczenia do osobnej klasy `Statystyka` z metodą `Oblicz(string tekst)` zwracającą wynik (średnia, najwyższa, wyróżnienie albo komunikat błędu). Strona tylko wywołuje metodę i wyświetla wynik. Taką klasę przetestujesz w następnej lekcji.

## Czy potrafię…?

- [ ] postawić punkt przerwania, także warunkowy
- [ ] wykonywać program krok po kroku (++f10++, ++f11++)
- [ ] sprawdzić wartość zmiennej i wyrażenia w czasie działania programu
- [ ] rozpoznać typ wyjątku i wskazać jego przyczynę
- [ ] odróżnić błąd kompilacji, wyjątek i błąd logiczny
