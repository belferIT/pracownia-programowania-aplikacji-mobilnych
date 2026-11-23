# Lekcja 17. Okna dialogowe i async/await

<p class="lekcja-meta">Dział: Kontrolki i wiązanie danych · 45 min · Efekty: INF.04.6 (2) kryt. 4, 6 · <span class="zakres zakres-p">INF.04</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- wyświetlić komunikat i pytanie Tak/Nie,
- dać użytkownikowi wybór z listy opcji,
- pobrać tekst w oknie dialogowym,
- wyjaśnić, po co jest `async` i `await`.

## Wprowadzenie

Okna dialogowe w MAUI są **asynchroniczne**: metoda zwraca wynik dopiero, gdy użytkownik kliknie przycisk. Dlatego metoda obsługi zdarzenia ma słowo `async`, a wywołanie – `await`.

```csharp
private async void OnUsunClicked(object? sender, EventArgs e)
{
    // 1. komunikat
    await DisplayAlertAsync("Informacja", "Zapisano zmiany", "OK");

    // 2. pytanie: true = Tak, false = Nie
    bool usun = await DisplayAlertAsync("Uwaga", "Usunąć notatkę?", "Tak", "Nie");
    if (!usun) return;

    // 3. wybór z listy: zwraca tekst klikniętej opcji
    string? wybor = await DisplayActionSheetAsync("Poziom trudności", "Anuluj", null,
                                                  "Łatwy", "Średni", "Trudny");

    // 4. pobranie tekstu: null, gdy anulowano
    string? imie = await DisplayPromptAsync("Gracz", "Jak masz na imię?",
                                            "OK", "Anuluj", "np. Ola", maxLength: 20);

    string? liczba = await DisplayPromptAsync("Zgadnij", "Podaj liczbę",
                                              keyboard: Keyboard.Numeric);
}
```

| Metoda (.NET 10) | Zwraca |
|---|---|
| `DisplayAlertAsync(tytuł, treść, przycisk)` | nic (`Task`) |
| `DisplayAlertAsync(tytuł, treść, tak, nie)` | `bool` |
| `DisplayActionSheetAsync(tytuł, anuluj, usuń, opcje…)` | `string?` – tekst wybranej opcji |
| `DisplayPromptAsync(tytuł, treść, …)` | `string?` – wpisany tekst lub `null` |

!!! info "Starsze wersje"
    W .NET 8 i 9 metody nazywały się `DisplayAlert` i `DisplayActionSheet`. W .NET 10 nadal działają, ale są oznaczone jako przestarzałe (ostrzeżenie kompilatora). W starszych przykładach z internetu spotkasz obie wersje.

!!! warning "async void"
    `async void` stosuj **tylko** w metodach obsługi zdarzeń. Własne metody asynchroniczne zwracają `Task` (np. `private async Task ZapiszAsync()`).

## Zadanie główne (25 min)

Utwórz projekt `ZgadnijLiczbe`.

1. Ekran zawiera: nagłówek **Zgadnij liczbę**, etykietę `lblZakres` (**Liczba od 1 do 100**), etykietę `lblProby` (**Próby: 0**) i trzy przyciski: **Zgaduj**, **Poziom**, **Nowa gra**.
2. Przy starcie aplikacja losuje liczbę: `Random.Shared.Next(1, max + 1)`, gdzie `max` = 100.
3. **Zgaduj** otwiera `DisplayPromptAsync` z klawiaturą numeryczną. Po wpisaniu liczby:
    1. anulowanie lub tekst, który nie jest liczbą – nic się nie dzieje,
    2. za mała – komunikat **Za mało!**, za duża – **Za dużo!**,
    3. trafiona – komunikat **Brawo! Zgadłeś w N próbach.** i nowe losowanie.
    Każda poprawna próba zwiększa licznik prób.
4. **Poziom** otwiera `DisplayActionSheetAsync` z opcjami **Łatwy (1–10)**, **Średni (1–100)**, **Trudny (1–1000)**. Wybór zmienia `max`, napis `lblZakres` i rozpoczyna nową grę.
5. **Nowa gra** pyta: **Czy na pewno zacząć od nowa?** (Tak/Nie). Po odpowiedzi Tak – nowe losowanie i zerowanie prób.

??? question "Podpowiedź: sprawdzanie, czy liczba jest poprawna"
    ```csharp
    string? tekst = await DisplayPromptAsync("Zgadnij", $"Podaj liczbę od 1 do {max}",
                                             keyboard: Keyboard.Numeric);
    if (!int.TryParse(tekst, out int strzal)) return;
    ```

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Zapamiętuj najlepszy wynik (najmniej prób) dla każdego poziomu w słowniku `Dictionary<int, int>` i pokazuj go w etykiecie **Rekord: N**. Po pobiciu rekordu wyświetl dodatkowy komunikat.

## Czy potrafię…?

- [ ] wyświetlić komunikat i pytanie Tak/Nie
- [ ] odczytać wybór z `DisplayActionSheetAsync`
- [ ] pobrać liczbę przez `DisplayPromptAsync` i sprawdzić ją
- [ ] wyjaśnić, kiedy piszę `async` i `await`
