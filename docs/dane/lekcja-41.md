# Lekcja 41. Zegar i stoper: timer

<p class="lekcja-meta">Dział: Dane, sieć i usługi urządzenia · 45 min · Efekty: INF.04.6 (2) kryt. 7 · <span class="zakres zakres-p">INF.04</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- wykonywać kod cyklicznie co określony czas (`IDispatcherTimer`),
- mierzyć upływ czasu (`Stopwatch`),
- formatować czas (`TimeSpan`) i godzinę (`DateTime`).

## Wprowadzenie

```csharp
private readonly IDispatcherTimer timer;

public MainPage()
{
    InitializeComponent();
    timer = Dispatcher.CreateTimer();
    timer.Interval = TimeSpan.FromSeconds(1);
    timer.Tick += OnTick;
    timer.Start();
}

private void OnTick(object? sender, EventArgs e)
{
    lblZegar.Text = DateTime.Now.ToString("HH:mm:ss");
}
```

| Element | Znaczenie |
|---|---|
| `Dispatcher.CreateTimer()` | timer działający w wątku interfejsu – można w nim zmieniać kontrolki |
| `Interval` | odstęp między wywołaniami |
| `Tick` | zdarzenie wywoływane co `Interval` |
| `Start()`, `Stop()`, `IsRunning` | sterowanie |
| `IsRepeating = false` | timer wykona się tylko raz |

### Dokładny pomiar czasu

Timer **nie gwarantuje** dokładnych odstępów (może się spóźnić). Do stopera użyj `Stopwatch` i odczytuj zmierzony czas w każdym `Tick`:

```csharp
using System.Diagnostics;

private readonly Stopwatch stoper = new();

stoper.Start();    stoper.Stop();    stoper.Reset();
TimeSpan czas = stoper.Elapsed;
lblStoper.Text = czas.ToString(@"mm\:ss\.ff");   // 01:23.45
```

| Format `TimeSpan` | Wynik |
|---|---|
| `@"hh\:mm\:ss"` | 00:05:07 |
| `@"mm\:ss\.ff"` | 05:07.32 |

!!! warning "Zatrzymaj timer, gdy strona znika"
    Timer działa dalej, gdy przejdziesz na inną stronę. W `OnDisappearing()` zatrzymaj go (`timer.Stop()`), a w `OnAppearing()` uruchom ponownie.

## Zadanie główne (25 min)

Utwórz projekt `Czasomierz` z dolnymi zakładkami (`TabBar`) **Zegar**, **Stoper**, **Minutnik**.

1. **Zegar**: duża godzina `HH:mm:ss` (rozmiar `56`), pod nią data `dddd, d MMMM yyyy`. Odświeżanie co 1 s.
2. **Stoper**: czas w formacie `mm:ss.ff` (rozmiar `56`), odświeżany co 10 ms; przyciski **Start/Pauza** (jeden przycisk zmieniający tekst), **Okrążenie**, **Zeruj**. **Okrążenie** dodaje czas do listy (`CollectionView`) z numerem: **Okrążenie 1: 00:12.34**.
3. **Minutnik**: `Stepper` minut (1–60) i sekund (0–59, krok 5), przycisk **Start**, pozostały czas `mm:ss`, `ProgressBar` pokazujący upływ czasu. Po dojściu do zera timer się zatrzymuje i wyświetla komunikat **Czas minął!**.
4. Na każdej zakładce timer zatrzymuje się w `OnDisappearing`.

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Na zakładce **Stoper** oznacz najszybsze okrążenie kolorem zielonym, a najwolniejsze czerwonym (klasa `Okrazenie` z właściwością `Kolor` i ponowne wyliczanie po każdym okrążeniu). Na zakładce **Minutnik** odtwórz dźwięk z lekcji 24.

## Czy potrafię…?

- [ ] utworzyć i uruchomić timer
- [ ] zmierzyć czas klasą `Stopwatch`
- [ ] sformatować `TimeSpan` i `DateTime`
- [ ] zatrzymać timer, gdy strona znika
