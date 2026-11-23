# Lekcja 51. Testy jednostkowe w xUnit

<p class="lekcja-meta">Dział: Jakość, testy i publikacja · 45 min · Efekty: INF.04.8 (3) kryt. 2, 3, 13 · <span class="zakres zakres-p">INF.04</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- wydzielić logikę aplikacji do biblioteki klas, którą da się testować,
- napisać test jednostkowy `[Fact]` i test z danymi `[Theory]`,
- dobrać dane testowe z wartościami granicznymi,
- uruchomić testy w **Eksploratorze testów** i odczytać wynik.

## Wprowadzenie

**Test jednostkowy** to mała metoda, która wywołuje fragment kodu (zwykle jedną metodę) i sprawdza wynik. Testy uruchamiasz jednym kliknięciem, więc po każdej zmianie wiesz, czy niczego nie zepsułeś.

Testy pisze się według schematu **AAA**:

```csharp
using Kino.Logika;

namespace Kino.Testy;

public class CennikTesty
{
    [Fact]
    public void Dorosly_wPoniedzialek_bezKarty_placi30()
    {
        // Arrange – przygotuj dane
        int wiek = 30;

        // Act – wywołaj testowaną metodę
        decimal cena = Cennik.CenaBiletu(wiek, DayOfWeek.Monday, false);

        // Assert – sprawdź wynik
        Assert.Equal(30m, cena);
    }

    [Theory]
    [InlineData(12, 18.0)]
    [InlineData(13, 22.0)]
    public void CenaZalezyOdWieku(int wiek, double oczekiwana)
    {
        decimal cena = Cennik.CenaBiletu(wiek, DayOfWeek.Monday, false);
        Assert.Equal((decimal)oczekiwana, cena);
    }

    [Fact]
    public void UjemnyWiek_rzucaWyjatek()
    {
        Assert.Throws<ArgumentOutOfRangeException>(
            () => Cennik.CenaBiletu(-1, DayOfWeek.Monday, false));
    }
}
```

| Element | Znaczenie |
|---|---|
| `[Fact]` | test bez parametrów, zawsze z tymi samymi danymi |
| `[Theory]` + `[InlineData(...)]` | ten sam test dla wielu zestawów danych |
| `Assert.Equal(oczekiwana, rzeczywista)` | najpierw wartość oczekiwana, potem wynik |
| `Assert.True`, `Assert.Throws<T>` | warunek prawdziwy, metoda rzuca wyjątek typu `T` |

!!! warning "`decimal` w atrybucie"
    W atrybutach C# nie można zapisać wartości `decimal` (`30m`). Dlatego w `[InlineData]` podajesz `double` i zamieniasz na `decimal` w teście.

!!! info "Wartości graniczne"
    Błędy najczęściej siedzą na granicach przedziałów: `<` zamiast `<=`. Gdy reguła brzmi „od 13 do 25 lat”, testuj 12, 13, 25 i 26, a nie tylko 20.

!!! tip "Dlaczego biblioteka klas?"
    Projekt testowy nie może łatwo odwołać się do projektu MAUI (ten jest budowany dla Androida, Windows i iOS). Logikę umieszczasz w zwykłej bibliotece `.NET`. Odwołują się do niej i aplikacja, i testy.

## Zadanie główne (25 min)

Plik startowy: [Cennik.cs](../pliki/lekcja-51/Cennik.cs){ download }

Kino **Kadr** ustaliło cennik. Programista napisał klasę `Cennik`, ale nie sprawdził jej testami.

| Bilet | Cena |
|---|---|
| dziecięcy: do 12 lat włącznie | 18 zł |
| uczniowski: od 13 do 25 lat włącznie | 22 zł |
| senioralny: od 65 lat | 20 zł |
| normalny: pozostałe osoby | 30 zł |

- „Tani wtorek”: każdy bilet 5 zł taniej.
- Karta stałego klienta: 10% rabatu od ceny po innych rabatach.
- Wiek spoza zakresu 0–120 to wyjątek `ArgumentOutOfRangeException`.

1. Utwórz pustą solucję `Kino`. Dodaj projekt **Biblioteka klas** `Kino.Logika` (.NET 10) i skopiuj do niego `Cennik.cs` (usuń `Class1.cs`).
2. Dodaj projekt **Projekt testowy xUnit** `Kino.Testy`. Kliknij prawym przyciskiem **Zależności → Dodaj odwołanie do projektu** i zaznacz `Kino.Logika`.
3. Wklej testy z przykładu i uruchom je: **Test → Eksplorator testów → Uruchom wszystkie** (++ctrl+r++, ++a++).
4. Napisz test `[Theory]` dla wszystkich wierszy tabeli. Uruchom testy.
5. Testy, które nie przechodzą, wskazują błędy w `Cennik.cs`. Popraw kod, aż wszystkie testy będą zielone. **Nie zmieniaj oczekiwanych wartości w testach.**

| Wiek | Dzień | Karta | Oczekiwana cena |
|---|---|---|---|
| 0 | poniedziałek | nie | 18,00 |
| 12 | poniedziałek | nie | 18,00 |
| 13 | poniedziałek | nie | 22,00 |
| 25 | poniedziałek | nie | 22,00 |
| 26 | poniedziałek | nie | 30,00 |
| 64 | poniedziałek | nie | 30,00 |
| 65 | poniedziałek | nie | 20,00 |
| 30 | wtorek | nie | 25,00 |
| 30 | wtorek | tak | 22,50 |
| 13 | wtorek | tak | 15,30 |
| 70 | środa | tak | 18,00 |
| 120 | wtorek | nie | 15,00 |
| −1 i 121 | dowolny | dowolna | wyjątek |

??? question "Podpowiedź: dzień tygodnia w `[InlineData]`"
    Wartości wyliczenia (`enum`) można podawać w atrybutach: `[InlineData(30, DayOfWeek.Tuesday, true, 22.5)]`.

??? question "Podpowiedź: nie widzę testów w Eksploratorze"
    Zbuduj solucję (++ctrl+shift+b++). Metoda testowa musi być `public` i mieć atrybut `[Fact]` lub `[Theory]`.

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Kino wprowadza bilet rodzinny: metoda `CenaRodzinna(int dorosli, int dzieci, DayOfWeek dzien)`, gdzie przy co najmniej 2 dorosłych i 2 dzieciach cała grupa płaci 20% mniej niż za bilety pojedyncze. Najpierw napisz testy (z danymi policzonymi ręcznie), potem metodę. Tak pracuje się w metodzie **TDD** (*Test-Driven Development*).

## Czy potrafię…?

- [ ] utworzyć projekt testowy xUnit i dodać odwołanie do testowanego projektu
- [ ] napisać test według schematu Arrange–Act–Assert
- [ ] użyć `[Theory]` z `[InlineData]`
- [ ] sprawdzić, że metoda rzuca wyjątek
- [ ] dobrać wartości graniczne do danych testowych
