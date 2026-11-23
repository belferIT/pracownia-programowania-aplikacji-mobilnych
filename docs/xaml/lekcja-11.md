# Lekcja 11. Pola edycyjne: Entry i Editor

<p class="lekcja-meta">Dział: XAML i układy · 45 min · Efekty: INF.04.6 (2) kryt. 4, 6 · <span class="zakres zakres-p">INF.04</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- pobrać tekst od użytkownika polem `Entry` i `Editor`,
- ograniczyć klawiaturę do liczb,
- bezpiecznie zamienić tekst na liczbę (`TryParse`),
- reagować na zmianę tekstu (`TextChanged`).

## Wprowadzenie

| Właściwość `Entry` | Działanie |
|---|---|
| `Placeholder="Podaj wagę"` | szary tekst podpowiedzi w pustym polu |
| `Keyboard="Numeric"` | klawiatura numeryczna (`Text`, `Email`, `Telephone`, `Url`, `Chat`) |
| `IsPassword="True"` | ukrywa wpisywane znaki |
| `MaxLength="3"` | maksymalna liczba znaków |
| `IsReadOnly="True"` | tylko do odczytu |
| `ClearButtonVisibility="WhileEditing"` | przycisk czyszczenia pola |

`Editor` to pole wielowierszowe (np. na notatkę); `AutoSize="TextChanges"` powiększa je w miarę pisania.

### Tekst → liczba

`entWaga.Text` to zawsze **tekst** (może być `null` lub pusty). `int.Parse` przy błędnym tekście wyrzuca wyjątek i aplikacja się zamyka. Używaj `TryParse`:

```csharp
if (int.TryParse(entWiek.Text, out int wiek))
{
    lblWynik.Text = $"Za rok będziesz mieć {wiek + 1} lat";
}
else
{
    lblWynik.Text = "Wpisz liczbę całkowitą";
}
```

!!! warning "Przecinek czy kropka?"
    `double.TryParse` czyta liczbę według ustawień regionalnych urządzenia: na polskim Windows separatorem jest przecinek, a w emulatorze z angielskim systemem – kropka. Bezpieczny sposób, który akceptuje oba zapisy:

    ```csharp
    using System.Globalization;

    private static bool CzytajLiczbe(string? tekst, out double liczba)
    {
        string t = (tekst ?? "").Replace(',', '.');
        return double.TryParse(t, NumberStyles.Float, CultureInfo.InvariantCulture, out liczba);
    }
    ```

### Zdarzenia pól

| Zdarzenie | Kiedy |
|---|---|
| `TextChanged` | po każdej zmianie znaku; `e.NewTextValue`, `e.OldTextValue` |
| `Completed` | użytkownik nacisnął Enter / „Gotowe” na klawiaturze |
| `Focused`, `Unfocused` | pole dostało lub straciło fokus |

!!! info "Na egzaminie"
    Typowe wymaganie: „Do pola edycyjnego można wpisać jedynie liczby” – ustaw `Keyboard="Numeric"`. Drugie: „Wpisanie dowolnego innego znaku jest ignorowane – aplikacja nie wywołuje błędu działania” – sprawdzaj dane przez `TryParse`.

## Zadanie główne (25 min)

Utwórz projekt `Rejestracja`.

1. Ekran zawiera kolejno (z etykietami nad polami):
    1. **Imię**: `Entry` `entImie`, podpowiedź *np. Anna*,
    2. **Wiek**: `Entry` `entWiek`, klawiatura numeryczna, maks. 3 znaki,
    3. **Hasło**: `Entry` `entHaslo`, znaki ukryte,
    4. etykieta `lblSila` pod hasłem,
    5. **O sobie**: `Editor` `edtOpis`, wysokość `100`, podpowiedź *Napisz kilka słów*,
    6. przycisk **Zarejestruj**,
    7. etykieta `lblWynik`.
2. Obsłuż `TextChanged` pola hasła. W `lblSila` wypisuj: **Hasło za krótkie** (mniej niż 8 znaków, kolor `#D32F2F`) albo **Hasło poprawne** (8 i więcej, kolor `#2E7D32`).
3. Po kliknięciu **Zarejestruj** sprawdź dane w tej kolejności i wypisz w `lblWynik` **pierwszy** napotkany błąd:
    1. imię puste (`string.IsNullOrWhiteSpace`) → **Podaj imię**,
    2. wiek nie jest liczbą lub jest spoza zakresu 13–120 → **Podaj poprawny wiek**,
    3. hasło krótsze niż 8 znaków → **Hasło musi mieć co najmniej 8 znaków**.
4. Jeśli dane są poprawne, wypisz: **Witaj, Anna! Liczba znaków opisu: N**.

| Imię | Wiek | Hasło | Wynik |
|---|---|---|---|
| (puste) | 17 | abcdefgh | Podaj imię |
| Anna | 1a | abcdefgh | Podaj poprawny wiek |
| Anna | 9 | abcdefgh | Podaj poprawny wiek |
| Anna | 17 | abc | Hasło musi mieć co najmniej 8 znaków |
| Anna | 17 | abcdefgh | Witaj, Anna! Liczba znaków opisu: … |

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Oceniaj siłę hasła w trzech stopniach: **słabe** (mniej niż 8 znaków), **średnie** (8+ znaków), **silne** (8+ znaków, zawiera cyfrę i wielką literę – użyj `char.IsDigit` i `char.IsUpper` w pętli lub `Any`). Zmieniaj kolor etykiety odpowiednio na czerwony, pomarańczowy i zielony.

## Czy potrafię…?

- [ ] ustawić klawiaturę numeryczną i ukrywanie znaków
- [ ] zamienić tekst na liczbę bez ryzyka wyjątku
- [ ] obsłużyć liczby z przecinkiem i z kropką
- [ ] reagować na każdą zmianę tekstu w polu
