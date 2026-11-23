# Lekcja 18. Wiązanie danych między kontrolkami

<p class="lekcja-meta">Dział: Kontrolki i wiązanie danych · 45 min · Efekty: INF.04.6 (2) kryt. 5, 6 · <span class="zakres zakres-p">INF.04</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- połączyć właściwość jednej kontrolki z właściwością innej bez pisania kodu C#,
- sformatować wartość w wiązaniu (`StringFormat`),
- wyjaśnić, czym jest źródło i cel wiązania.

## Wprowadzenie

**Wiązanie danych** (*Data Binding*) łączy właściwość **celu** (np. `Label.Text`) z właściwością **źródła** (np. `Slider.Value`). Gdy zmienia się źródło, cel aktualizuje się sam.

```xml
<Slider x:Name="sldKat" Maximum="360" Value="0" />

<Label Text="{Binding Source={x:Reference sldKat}, Path=Value, StringFormat='Kąt: {0:F0}°'}" />

<Image Source="logo.png" WidthRequest="120"
       Rotation="{Binding Source={x:Reference sldKat}, Path=Value}" />
```

| Część wiązania | Znaczenie |
|---|---|
| `Source={x:Reference sldKat}` | źródło: kontrolka o nazwie `sldKat` |
| `Path=Value` | właściwość źródła |
| `StringFormat='Kąt: {0:F0}°'` | format tekstu; `{0}` to wartość, `F0` – bez miejsc po przecinku |
| `Mode=TwoWay` | zmiana działa w obie strony (cel → źródło też) |

!!! info "To samo na egzaminie"
    W informatorze CKE jest przykład: `<Label Text="{Binding Source={x:Reference slider2}, Path=Value}" />`. Wiązanie łączy **właściwość elementu interfejsu z danymi lub z właściwością innego obiektu**. W założeniach aplikacji pojawia się zdanie: „działanie kontrolek obsłużone za pomocą zdarzeń **lub techniką Data Binding**”.

### Typowe połączenia

| Źródło | Cel | Efekt |
|---|---|---|
| `Switch.IsToggled` | `Label.IsVisible` | przełącznik pokazuje i ukrywa etykietę |
| `Entry.Text` | `Label.Text` | podgląd wpisywanego tekstu |
| `Slider.Value` | `Label.FontSize`, `BoxView.Opacity` | zmiana rozmiaru, przezroczystości |
| `Stepper.Value` | `Label.Text` | licznik bez kodu |
| `CheckBox.IsChecked` | `Button.IsEnabled` | przycisk aktywny po zaznaczeniu zgody |

## Zadanie główne (25 min)

Utwórz projekt `PodgladNapisu`. **Nie pisz żadnego kodu w `MainPage.xaml.cs`** – wszystko zrób wiązaniami w XAML.

1. Pole `Entry` `entTekst` z podpowiedzią **Wpisz napis**.
2. Etykieta `lblPodglad` na środku obszaru o wysokości `200`, której tekst jest powiązany z `entTekst.Text`.
3. Suwak `sldRozmiar` (10–80, start 30) i etykieta **Rozmiar: 30** (z `StringFormat`, bez miejsc po przecinku). Rozmiar czcionki podglądu jest powiązany z suwakiem.
4. Suwak `sldObrot` (0–360) i etykieta **Obrót: 0°**. Obrót podglądu (`Rotation`) jest powiązany z suwakiem.
5. `Stepper` `stpPrzezroczystosc` (0–1, krok 0.1, start 1) i etykieta **Krycie: 1,0**. `Opacity` podglądu jest powiązane ze stepperem.
6. `Switch` `swWidoczny` (włączony) z napisem **Pokaż podgląd**, powiązany z `IsVisible` podglądu.
7. `CheckBox` z napisem **Akceptuję regulamin** i przycisk **Zapisz**, który jest aktywny tylko po zaznaczeniu pola (wiązanie `IsEnabled`).

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Dodaj drugi suwak obrotu powiązany z pierwszym w trybie `Mode=TwoWay` (np. `Value="{Binding Source={x:Reference sldObrot}, Path=Value, Mode=TwoWay}"`). Sprawdź, że przesunięcie dowolnego z nich przesuwa oba.

## Czy potrafię…?

- [ ] zapisać wiązanie z `x:Reference` i `Path`
- [ ] sformatować wartość w wiązaniu przez `StringFormat`
- [ ] wskazać źródło i cel wiązania
- [ ] wyjaśnić, co oznacza `Mode=TwoWay`
