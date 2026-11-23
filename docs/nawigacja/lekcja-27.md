# Lekcja 27. Wiele stron: nawigacja stosowa

<p class="lekcja-meta">Dział: Nawigacja i platformy · 45 min · Efekty: INF.04.6 (2) kryt. 4, 6 · <span class="zakres zakres-p">INF.04</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- dodać do projektu nową stronę XAML,
- przejść na nową stronę i wrócić (`PushAsync`, `PopAsync`),
- otworzyć stronę modalną,
- ustawić tytuł strony widoczny na pasku nawigacji.

## Wprowadzenie

Strony w aplikacji mobilnej układają się w **stos**: nowa strona kładzie się na wierzchu, przycisk „wstecz” zdejmuje ją ze stosu.

```text
PushAsync(B)          PushAsync(C)          PopAsync()
+---+                 +---+                 +---+
| B |                 | C |                 | B |
| A |      →          | B |       →         | A |
+---+                 | A |                 +---+
                      +---+
```

| Metoda (`Navigation.`) | Działanie |
|---|---|
| `PushAsync(new StronaPage())` | przejście na nową stronę (ze strzałką „wstecz”) |
| `PopAsync()` | powrót do poprzedniej strony |
| `PopToRootAsync()` | powrót do pierwszej strony |
| `PushModalAsync(...)` / `PopModalAsync()` | strona modalna: zasłania wszystko, bez paska nawigacji |

```csharp
private async void OnOAplikacjiClicked(object? sender, EventArgs e)
{
    await Navigation.PushAsync(new OAplikacjiPage());
}
```

!!! info "Nowa strona"
    Prawy przycisk na projekcie → **Dodaj → Nowy element → .NET MAUI → .NET MAUI ContentPage (XAML)**. Nazwę kończ słowem `Page`, np. `OAplikacjiPage.xaml`. Powstają dwa pliki: `.xaml` i `.xaml.cs`.

!!! tip "Tytuł na pasku"
    Ustaw `Title="O aplikacji"` w znaczniku `ContentPage`. W aplikacji z szablonu (z `AppShell`) pasek nawigacji i strzałka „wstecz” pojawiają się automatycznie.

## Zadanie główne (25 min)

Utwórz projekt `Przepisy`.

1. Strona główna (`MainPage`, tytuł **Przepisy**): nagłówek **Książka kucharska** i trzy przyciski: **Naleśniki**, **Pierogi**, **Sernik**, a na dole przycisk **O aplikacji**.
2. Dodaj strony `NalesnikiPage`, `PierogiPage`, `SernikPage`. Każda ma tytuł z nazwą dania, listę składników (etykiety lub `FormattedText`) i krótki opis przygotowania (3–4 zdania). Na dole przycisk **Wróć**, który wywołuje `PopAsync()`.
3. Przyciski na stronie głównej otwierają odpowiednie strony (`PushAsync`).
4. Dodaj stronę `OAplikacjiPage` otwieraną **modalnie** (`PushModalAsync`). Zawiera nazwę aplikacji, wersję **1.0** i autora oraz przycisk **Zamknij** (`PopModalAsync`).
5. Na stronie `SernikPage` dodaj przycisk **Strona główna**, który wraca od razu do początku (`PopToRootAsync`).
6. Sprawdź w emulatorze działanie systemowego przycisku „wstecz” Androida na każdej stronie.

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Przechwyć przycisk „wstecz” na stronie `OAplikacjiPage`: nadpisz metodę `OnBackButtonPressed()` tak, aby pytała **Zamknąć informacje?**. Uwaga: metoda nie może być `async`, więc pytanie wyświetl w `Dispatcher.Dispatch(async () => { ... })` i zwróć `true` (zatrzymanie domyślnej akcji).

## Czy potrafię…?

- [ ] dodać nową stronę `ContentPage (XAML)`
- [ ] przejść na stronę i wrócić
- [ ] odróżnić stronę zwykłą od modalnej
- [ ] wrócić od razu do strony głównej
