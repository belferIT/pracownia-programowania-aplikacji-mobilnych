# Lekcja 23. Animacje widoków

<p class="lekcja-meta">Dział: Kontrolki i wiązanie danych · 45 min · Efekty: INF.04.6 (2) kryt. 4, 6 · <span class="zakres zakres-p">INF.04</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- przesunąć, obrócić, przeskalować i ukryć kontrolkę z animacją,
- wykonać animacje jedna po drugiej i jednocześnie,
- dobrać funkcję przebiegu animacji (`Easing`).

## Wprowadzenie

Każda kontrolka (`VisualElement`) ma metody animacji. W .NET 10 mają one końcówkę `Async`:

| Metoda | Zmienia | Przykład |
|---|---|---|
| `FadeToAsync(krycie, ms)` | `Opacity` (0–1) | `await img.FadeToAsync(0, 500);` |
| `RotateToAsync(kąt, ms)` | `Rotation` | `await img.RotateToAsync(360, 1000);` |
| `ScaleToAsync(skala, ms)` | `Scale` | `await img.ScaleToAsync(1.5, 300);` |
| `TranslateToAsync(x, y, ms)` | `TranslationX`, `TranslationY` (przesunięcie względem miejsca w układzie) | `await img.TranslateToAsync(0, -300, 2000);` |

```csharp
// jedna po drugiej
await imgRakieta.ScaleToAsync(1.2, 300);
await imgRakieta.ScaleToAsync(1.0, 300);

// jednocześnie
await Task.WhenAll(
    imgRakieta.TranslateToAsync(0, -600, 2000, Easing.CubicIn),
    imgRakieta.FadeToAsync(0, 2000));

// powrót bez animacji
imgRakieta.TranslationY = 0;
imgRakieta.Opacity = 1;
imgRakieta.Rotation = 0;
```

| `Easing` | Przebieg |
|---|---|
| `Linear` | stała prędkość |
| `CubicIn` / `CubicOut` | przyspieszanie / hamowanie |
| `BounceOut` | odbicie na końcu |
| `SpringOut` | sprężynowanie |

!!! info "Wcześniejsze wersje"
    W .NET 8 i 9 metody nazywały się `FadeTo`, `RotateTo`, `ScaleTo`, `TranslateTo`. W .NET 10 są przestarzałe. Przerwanie animacji: `imgRakieta.CancelAnimations();`.

!!! tip "Blokuj przycisk w trakcie animacji"
    Gdy użytkownik kliknie **Start** dwa razy, uruchomią się dwie animacje naraz. Ustaw `btnStart.IsEnabled = false;` na początku i `true` na końcu metody.

## Zadanie główne (25 min)

Pobierz obraz [rakieta.png](../pliki/lekcja-23/rakieta.png){ download } i dodaj go do `Resources/Images`.

Utwórz projekt `StartRakiety`.

1. Strona ma tło `#0D1B2A`. Na środku obraz `imgRakieta` (szerokość `150`), na dole trzy przyciski obok siebie: **Odliczanie**, **Start**, **Reset** (tło `#FF9800`).
2. Nad rakietą duża etykieta `lblOdliczanie` (rozmiar `64`, biała, początkowo pusta).
3. **Odliczanie**: wyświetla kolejno 3, 2, 1 – każda cyfra pojawia się (`FadeToAsync` z 0 do 1 w 300 ms), powiększa (`ScaleToAsync(2, 500)`), wraca do skali 1. Między cyframi animacje czekają na siebie (`await`). Na końcu napis **START!**.
4. **Start**: rakieta jednocześnie:
    - drży – trzy obroty `RotateToAsync(-5, 50)` / `RotateToAsync(5, 50)`, potem `0`,
    - a następnie leci do góry o 700 jednostek w 2 s z `Easing.CubicIn` i jednocześnie znika (`FadeToAsync(0, 2000)`).
5. **Reset**: rakieta wraca na miejsce bez animacji, jest widoczna, napis pusty.
6. W trakcie animacji wszystkie przyciski są nieaktywne.

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Dodaj „gwiazdy”: 20 małych `BoxView` (2×2, białe) w losowych miejscach `AbsoluteLayout`. Podczas startu gwiazdy przesuwają się w dół (`TranslateToAsync`), dając wrażenie lotu. Użyj pętli i `Random.Shared`.

## Czy potrafię…?

- [ ] użyć metod `FadeToAsync`, `RotateToAsync`, `ScaleToAsync`, `TranslateToAsync`
- [ ] wykonać animacje jedna po drugiej i równocześnie (`Task.WhenAll`)
- [ ] dobrać `Easing` do efektu
- [ ] przywrócić kontrolkę do stanu początkowego
