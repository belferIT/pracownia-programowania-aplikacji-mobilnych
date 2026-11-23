# Lekcja 34. Preferencje użytkownika

<p class="lekcja-meta">Dział: Dane, sieć i usługi urządzenia · 45 min · Efekty: INF.04.6 (2) kryt. 3 · <span class="zakres zakres-p">INF.04</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- zapisać ustawienie aplikacji tak, aby przetrwało jej zamknięcie,
- odczytać ustawienie z wartością domyślną,
- usunąć jedno ustawienie lub wszystkie.

## Wprowadzenie

`Preferences` przechowuje małe dane w parach **klucz → wartość** (na Androidzie w *SharedPreferences*). Nadaje się do ustawień: imię, rozmiar czcionki, wybrany motyw, licznik uruchomień.

```csharp
// zapis
Preferences.Default.Set("imie", "Ola");
Preferences.Default.Set("rozmiar", 18);
Preferences.Default.Set("dzwiek", true);

// odczyt: drugi parametr to wartość domyślna (gdy klucza nie ma)
string imie = Preferences.Default.Get("imie", "Gość");
int rozmiar = Preferences.Default.Get("rozmiar", 16);
bool dzwiek = Preferences.Default.Get("dzwiek", true);

// inne operacje
bool jest = Preferences.Default.ContainsKey("imie");
Preferences.Default.Remove("imie");
Preferences.Default.Clear();
```

| Obsługiwane typy | `string`, `int`, `long`, `double`, `float`, `bool`, `DateTime` |
|---|---|
| Nie nadaje się do | list, dużych tekstów, zdjęć (użyj plików lub bazy) |
| Dane wrażliwe (hasła, tokeny) | `SecureStorage` – szyfrowane |

!!! tip "Stałe zamiast tekstów"
    Literówka w kluczu (`"imie"` / `"imię"`) to trudny do znalezienia błąd. Zapisz klucze jako stałe: `private const string KluczImie = "imie";`.

!!! info "Gdzie odczytywać"
    Ustawienia odczytuj w konstruktorze strony lub w `OnAppearing()`. Zapisuj od razu po zmianie (np. w `Toggled`, `ValueChanged`) – użytkownik może zamknąć aplikację w każdej chwili.

## Zadanie główne (25 min)

Utwórz projekt `Ustawienia`.

1. Strona zawiera:
    1. etykietę powitania `lblPowitanie`,
    2. pole **Imię** (`entImie`) i przycisk **Zapisz imię**,
    3. `Slider` **Rozmiar tekstu** 12–30 (zmienia `FontSize` powitania),
    4. `Switch` **Tryb ciemny** (zmienia `UserAppTheme`),
    5. `Picker` **Ulubiony kolor** (czerwony, zielony, niebieski) – zmienia kolor powitania,
    6. etykietę **Aplikację uruchomiono N razy**,
    7. przycisk **Przywróć domyślne**.
2. Powitanie: **Cześć, Ola!**, a gdy imienia nie zapisano – **Cześć, Gościu!**.
3. Każde ustawienie zapisuj w `Preferences` od razu po zmianie. Przy starcie odczytaj wszystkie i ustaw kontrolki.
4. Licznik uruchomień zwiększaj o 1 w konstruktorze strony.
5. **Przywróć domyślne** pyta o potwierdzenie, czyści ustawienia (poza licznikiem uruchomień) i ustawia kontrolki na wartości domyślne.
6. Sprawdź: zapisz ustawienia, **zamknij aplikację w emulatorze** (przeciągnij ją z listy ostatnich aplikacji) i uruchom ponownie z ikony.

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Dodaj pole **PIN** (4 cyfry) zapisywane w `SecureStorage` (`await SecureStorage.Default.SetAsync("pin", pin);`). Przy kolejnym uruchomieniu aplikacja pyta o PIN (`DisplayPromptAsync`) i pokazuje ustawienia dopiero po podaniu poprawnego.

## Czy potrafię…?

- [ ] zapisać i odczytać ustawienie z wartością domyślną
- [ ] wybrać, gdzie w kodzie odczytać i zapisać ustawienia
- [ ] usunąć jedno ustawienie i wszystkie ustawienia
- [ ] wyjaśnić, kiedy zamiast `Preferences` użyć `SecureStorage`
