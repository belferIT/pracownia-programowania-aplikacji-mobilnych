# Lekcja 42. Kalendarz i daty

<p class="lekcja-meta">Dział: Dane, sieć i usługi urządzenia · 45 min · Efekty: INF.04.6 (2) kryt. 7 · <span class="zakres zakres-p">INF.04</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- obliczyć liczbę dni między datami,
- dodawać dni i miesiące do daty,
- odczytać dzień tygodnia i sformatować datę po polsku,
- policzyć dni robocze w przedziale dat.

## Wprowadzenie

```csharp
DateTime dzis = DateTime.Today;                     // dzisiaj, godzina 00:00
DateTime egzamin = new DateTime(2027, 1, 12);

TimeSpan roznica = egzamin - dzis;
int dni = roznica.Days;                             // pełne dni

DateTime zaTydzien = dzis.AddDays(7);
DateTime zaMiesiac = dzis.AddMonths(1);

DayOfWeek dzien = egzamin.DayOfWeek;                // Tuesday
bool weekend = dzien == DayOfWeek.Saturday || dzien == DayOfWeek.Sunday;

int dniWMiesiacu = DateTime.DaysInMonth(2027, 2);   // 28
bool przestepny = DateTime.IsLeapYear(2028);        // true
```

| Format | Wynik (język polski) |
|---|---|
| `d` | 12.01.2027 |
| `D` | wtorek, 12 stycznia 2027 |
| `dddd` | wtorek |
| `MMMM yyyy` | styczeń 2027 |

!!! info "Język nazw dni i miesięcy"
    Nazwy zależą od języka systemu. Aby zawsze były po polsku: `data.ToString("dddd", new CultureInfo("pl-PL"))`.

### Pętla po dniach

```csharp
int robocze = 0;
for (DateTime d = od; d <= doDaty; d = d.AddDays(1))
{
    if (d.DayOfWeek != DayOfWeek.Saturday && d.DayOfWeek != DayOfWeek.Sunday)
    {
        robocze++;
    }
}
```

## Zadanie główne (25 min)

Utwórz projekt `Odliczanie`.

1. Dwa `DatePicker`: **Od** (domyślnie dziś) i **Do** (domyślnie za 30 dni), format `dd.MM.yyyy`.
2. Przycisk **Oblicz** i etykiety z wynikami:
    1. **Liczba dni: N**,
    2. **To N tygodni i M dni**,
    3. **Dni robocze (pn–pt): N** – liczone od dnia następującego po dacie **Od** do daty **Do** włącznie,
    4. **Dzień tygodnia daty końcowej: …** (po polsku).
3. Jeśli data **Do** jest wcześniejsza niż **Od**, wyświetl **Data końcowa musi być późniejsza** i nie licz.
4. Trzy przyciski szybkiego wyboru ustawiające datę **Do**: **Święta** (24 grudnia bieżącego roku; jeśli już minął – następnego roku), **Nowy Rok** (1 stycznia następnego roku), **Wakacje** (ostatni piątek czerwca – oblicz pętlą od 30 czerwca w tył).

| Od | Do | Dni | Tygodnie | Robocze | Dzień tygodnia |
|---|---|---|---|---|---|
| 23.11.2026 | 24.12.2026 | 31 | 4 tyg. i 3 dni | 23 | czwartek |
| 23.11.2026 | 01.01.2027 | 39 | 5 tyg. i 4 dni | 29 | piątek |
| 23.11.2026 | 25.06.2027 | 214 | 30 tyg. i 4 dni | 154 | piątek |
| 23.11.2026 | 23.11.2026 | 0 | 0 tyg. i 0 dni | 0 | poniedziałek |

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Dodaj listę własnych wydarzeń (nazwa + data) zapisywaną w `Preferences` jako JSON. Na liście pokazuj, ile dni zostało do każdego wydarzenia, a wydarzenia, które minęły, oznaczaj szarym kolorem.

## Czy potrafię…?

- [ ] obliczyć liczbę dni między datami
- [ ] dodać do daty dni i miesiące
- [ ] wyświetlić dzień tygodnia po polsku
- [ ] przejść pętlą po kolejnych dniach
