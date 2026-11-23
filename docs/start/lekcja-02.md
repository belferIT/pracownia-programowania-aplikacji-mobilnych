# Lekcja 2. Pierwsza aplikacja .NET MAUI

<p class="lekcja-meta">Dział: Start · 45 min · Efekty: INF.04.6 (1), (2) · <span class="zakres zakres-p">INF.04</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- utworzyć projekt z szablonu **Aplikacja .NET MAUI**,
- wskazać najważniejsze pliki i foldery projektu,
- uruchomić aplikację na komputerze z Windows,
- zmienić tekst i kolor na stronie głównej.

## Wprowadzenie

### Struktura projektu

| Plik / folder | Zawartość |
|---|---|
| `MauiProgram.cs` | punkt startowy: konfiguracja aplikacji, czcionki, biblioteki |
| `App.xaml`, `App.xaml.cs` | klasa aplikacji, zasoby wspólne, tworzenie okna (`CreateWindow`) |
| `AppShell.xaml` | „rama” aplikacji: nawigacja, menu, zakładki |
| `MainPage.xaml` | wygląd strony głównej (XAML) |
| `MainPage.xaml.cs` | kod strony głównej (C#), tzw. *code-behind* |
| `Platforms/` | kod specyficzny dla Androida, iOS, Windows, macOS (np. `AndroidManifest.xml`) |
| `Resources/` | ikona (`AppIcon`), ekran startowy (`Splash`), obrazy (`Images`), czcionki (`Fonts`), style (`Styles`), pliki (`Raw`) |

```csharp
// App.xaml.cs – aplikacja tworzy okno, w którym jest AppShell
public partial class App : Application
{
    public App()
    {
        InitializeComponent();
    }

    protected override Window CreateWindow(IActivationState? activationState)
    {
        return new Window(new AppShell());
    }
}
```

!!! info "XAML i C# razem"
    Plik `MainPage.xaml` opisuje **wygląd** strony, a `MainPage.xaml.cs` jej **działanie**. Oba pliki tworzą jedną klasę `MainPage` (słowo `partial`). Nazwę klasy wskazuje atrybut `x:Class` w XAML.

!!! tip "Cel uruchomienia"
    Na pasku narzędzi obok zielonej strzałki wybierasz, gdzie uruchomić aplikację: **Windows Machine** albo emulator Androida. Na Windows aplikacja startuje najszybciej, dlatego w trakcie pracy często sprawdzasz wygląd właśnie tam.

## Zadanie główne (25 min)

1. W Visual Studio wybierz **Utwórz nowy projekt**. W wyszukiwarce wpisz `MAUI` i wybierz szablon **Aplikacja .NET MAUI** (*.NET MAUI App*), język C#.
2. Nazwa projektu: `PierwszaAplikacja`, lokalizacja: `C:\Projekty\Nazwisko_Imie`. Zaznacz **Umieść rozwiązanie i projekt w tym samym katalogu**.
3. Platforma: **.NET 10.0 (obsługa długoterminowa)**. Jeśli pojawi się opcja przykładowej zawartości (*sample content*), nie zaznaczaj jej.
4. Wybierz cel **Windows Machine** i uruchom aplikację klawiszem ++f5++. Kliknij kilka razy przycisk. Zamknij aplikację.
5. Otwórz `MainPage.xaml`. Znajdź etykietę `Label` z tekstem `Hello, World!` i zmień tekst na **Cześć, tu Twoje Imię!**.
6. Etykiecie dodaj atrybut `TextColor="#4527A0"`.
7. Otwórz `MainPage.xaml.cs` i znajdź metodę obsługującą kliknięcie przycisku. Zmień teksty tak, aby przycisk pokazywał **Kliknięto 1 raz** i **Kliknięto N razy**.
8. Uruchom aplikację ponownie i sprawdź zmiany.
9. Uzupełnij w zeszycie lub w pliku `notatki.txt` tabelę: plik → co w nim zmieniłeś.

??? question "Podpowiedź: błąd przy uruchamianiu na Windows"
    Jeśli Visual Studio prosi o włączenie **trybu dewelopera**, otwórz Ustawienia Windows → System → Dla deweloperów i włącz tryb dewelopera (w pracowni zrób to z nauczycielem).

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Otwórz `AppShell.xaml` i zmień wartość `Title` strony głównej na nazwę swojej aplikacji. Potem otwórz plik projektu (dwuklik na nazwie projektu w Eksploratorze rozwiązań) i znajdź znaczniki `ApplicationTitle` i `ApplicationId`. Zmień tytuł aplikacji na `Moja pierwsza`.

## Czy potrafię…?

- [ ] utworzyć projekt .NET MAUI z szablonu
- [ ] wyjaśnić, do czego służą `MainPage.xaml` i `MainPage.xaml.cs`
- [ ] wskazać folder z obrazami i folder z kodem dla Androida
- [ ] uruchomić aplikację na Windows Machine
