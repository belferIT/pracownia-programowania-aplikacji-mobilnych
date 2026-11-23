# Lekcja 33. Tryb jasny i ciemny

<p class="lekcja-meta">Dział: Nawigacja i platformy · 45 min · Efekty: INF.04.6 (2) kryt. 5 · <span class="zakres zakres-gw">★ poza egzaminem</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- ustawić różne kolory dla motywu jasnego i ciemnego (`AppThemeBinding`),
- wymusić motyw w aplikacji niezależnie od ustawień systemu,
- zmieniać kolory w trakcie działania aplikacji (`DynamicResource`).

## Wprowadzenie

Android, iOS i Windows mają **tryb ciemny**. Dobra aplikacja dopasowuje do niego swoje kolory.

```xml
<Label Text="Witaj"
       TextColor="{AppThemeBinding Light=#212121, Dark=#FAFAFA}" />

<ContentPage BackgroundColor="{AppThemeBinding Light={StaticResource TloJasne},
                                               Dark={StaticResource TloCiemne}}">
```

```csharp
// odczyt bieżącego motywu
AppTheme motyw = Application.Current!.RequestedTheme;   // Light / Dark / Unspecified

// wymuszenie motywu w aplikacji
Application.Current!.UserAppTheme = AppTheme.Dark;       // Unspecified = jak w systemie

// reakcja na zmianę w systemie
Application.Current!.RequestedThemeChanged += (s, e) => lblMotyw.Text = e.RequestedTheme.ToString();
```

| `StaticResource` | `DynamicResource` |
|---|---|
| wartość pobrana **raz**, przy tworzeniu kontrolki | wartość śledzona: zmiana zasobu w trakcie działania zmienia kontrolki |
| szybsze | potrzebne do przełączania „skórek” |

```csharp
// zmiana zasobu w trakcie działania – kontrolki z DynamicResource zmienią kolor
Application.Current!.Resources["Akcent"] = Color.FromArgb("#00BFA5");
```

!!! info "Szablon już to robi"
    Plik `Resources/Styles/Styles.xaml` z szablonu MAUI używa `AppThemeBinding` dla wszystkich kontrolek. Dlatego aplikacja z szablonu sama zmienia kolory po włączeniu trybu ciemnego w emulatorze (Ustawienia → Wyświetlacz → Ciemny motyw).

## Zadanie główne (25 min)

Rozbuduj projekt `Przewodnik` z lekcji 32 albo `Kino` z lekcji 29–30.

1. W `Colors.xaml` dodaj pary kolorów: `TloJasne` `#FAFAFA` / `TloCiemne` `#121212`, `TekstJasny` `#212121` / `TekstCiemny` `#EEEEEE`, `KartaJasna` `#EDE7F6` / `KartaCiemna` `#311B92`.
2. Ustaw tło stron, kolor tekstu i tło kart listy przez `AppThemeBinding` z tymi kolorami.
3. Na stronie **Ustawienia** dodaj trzy `RadioButton`: **Jak w systemie**, **Jasny**, **Ciemny**. Wybór ustawia `UserAppTheme`.
4. Dodaj etykietę **Bieżący motyw: …** aktualizowaną przy zmianie motywu.
5. Dodaj `Picker` **Kolor akcentu** z trzema kolorami (`#FF9800`, `#00BFA5`, `#E91E63`). Kolor paska tytułu i przycisków ustaw przez `DynamicResource Akcent` i zmieniaj zasób po wyborze.
6. Sprawdź działanie, przełączając też motyw systemowy w emulatorze.

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Zapamiętaj wybrany motyw i kolor akcentu po zamknięciu aplikacji. Przeczytaj wcześniej wprowadzenie do lekcji 34 (`Preferences`) i przywracaj ustawienia w konstruktorze `App`.

## Czy potrafię…?

- [ ] ustawić kolor zależny od motywu (`AppThemeBinding`)
- [ ] wymusić motyw jasny lub ciemny w aplikacji
- [ ] wyjaśnić różnicę między `StaticResource` a `DynamicResource`
- [ ] zmienić zasób w trakcie działania aplikacji
