# Lekcja 31. Dostosowanie do platformy i urządzenia

<p class="lekcja-meta">Dział: Nawigacja i platformy · 45 min · Efekty: INF.04.6 (2) kryt. 10, INF.04.3 (6) kryt. 5 · <span class="zakres zakres-p">INF.04</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- ustawić różne wartości dla Androida, iOS i Windows (`OnPlatform`),
- dopasować wygląd do telefonu, tabletu i komputera (`OnIdiom`),
- odczytać informacje o urządzeniu i ekranie (`DeviceInfo`, `DeviceDisplay`),
- zareagować na obrót ekranu.

## Wprowadzenie

### OnPlatform i OnIdiom w XAML

```xml
<!-- skrócony zapis -->
<Label Text="Witaj"
       FontSize="{OnIdiom Phone=18, Tablet=28, Desktop=24}"
       Padding="{OnPlatform iOS='0,20,0,0', Android='0', WinUI='10'}" />

<!-- pełny zapis (jak w informatorze CKE) -->
<ContentPage.Padding>
    <OnPlatform x:TypeArguments="Thickness">
        <On Platform="iOS" Value="0,20,0,0" />
        <On Platform="Android" Value="0,0,0,0" />
    </OnPlatform>
</ContentPage.Padding>
```

### W C#

```csharp
if (DeviceInfo.Platform == DevicePlatform.Android) { ... }
if (DeviceInfo.Idiom == DeviceIdiom.Tablet) { ... }

lblModel.Text = $"{DeviceInfo.Manufacturer} {DeviceInfo.Model}";
lblSystem.Text = $"{DeviceInfo.Platform} {DeviceInfo.VersionString}";

DisplayInfo ekran = DeviceDisplay.Current.MainDisplayInfo;
lblEkran.Text = $"{ekran.Width} × {ekran.Height} px, gęstość {ekran.Density}";
lblOrientacja.Text = ekran.Orientation.ToString();   // Portrait / Landscape
```

```csharp
// reakcja na obrót ekranu
DeviceDisplay.Current.MainDisplayInfoChanged += (s, e) =>
{
    bool poziomo = e.DisplayInfo.Orientation == DisplayOrientation.Landscape;
    gridGlowny.ColumnDefinitions = poziomo
        ? new ColumnDefinitionCollection(new ColumnDefinition(GridLength.Star), new ColumnDefinition(GridLength.Star))
        : new ColumnDefinitionCollection(new ColumnDefinition(GridLength.Star));
};
```

| Wartość | Znaczenie |
|---|---|
| `DevicePlatform.Android`, `iOS`, `WinUI`, `MacCatalyst` | system |
| `DeviceIdiom.Phone`, `Tablet`, `Desktop`, `TV`, `Watch` | rodzaj urządzenia |
| `Width`, `Height` | rozmiar ekranu w **pikselach fizycznych**; w jednostkach MAUI: podziel przez `Density` |

!!! info "Egzamin: platforma mobilna"
    Kryterium „tworzy aplikacje dostosowane do danej platformy mobilnej (np. Android smartfon, Android tablet, iPad, iPhone)” jest sprawdzane pytaniami o `OnPlatform` i `OnIdiom` w części pisemnej (przykład w informatorze: margines górny tylko dla iOS).

## Zadanie główne (25 min)

Utwórz projekt `MojeUrzadzenie`.

1. Strona pokazuje w `Grid` (dwie kolumny: opis i wartość) informacje: producent, model, nazwa urządzenia (`DeviceInfo.Name`), system i wersja, rodzaj urządzenia, typ (fizyczne / wirtualne: `DeviceInfo.DeviceType`), rozdzielczość w pikselach, rozdzielczość w jednostkach MAUI (bez miejsc po przecinku), gęstość, orientacja.
2. Rozmiar czcionki nagłówka: telefon `24`, tablet `36`, komputer `30` (`OnIdiom`).
3. Kolor tła strony: Android `#E8F5E9`, Windows `#E3F2FD`, inne `#FFFFFF` (`OnPlatform`).
4. Etykieta orientacji aktualizuje się po obróceniu emulatora (zdarzenie `MainDisplayInfoChanged`). Pamiętaj, aby w `OnDisappearing` odłączyć obsługę zdarzenia (`-=`).
5. Uruchom aplikację na telefonie (emulator), na tablecie (jeśli masz emulator tabletu) i na Windows. Wykonaj zrzut z każdej platformy i wklej do dokumentu `urzadzenia` z podpisami.

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Zrób układ zależny od orientacji: w pionie dane i duża ikona telefonu (📱 w etykiecie o rozmiarze 120) są jedno pod drugim, w poziomie – obok siebie. Zamiast kodu w zdarzeniu możesz użyć `VisualStateManager` z `OrientationStateTrigger`.

## Czy potrafię…?

- [ ] ustawić wartość zależną od systemu (`OnPlatform`)
- [ ] ustawić wartość zależną od rodzaju urządzenia (`OnIdiom`)
- [ ] odczytać model, system i rozdzielczość ekranu
- [ ] zareagować na zmianę orientacji ekranu
