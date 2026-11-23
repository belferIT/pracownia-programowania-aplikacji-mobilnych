# Lekcja 43. Lokalizacja i uprawnienia

<p class="lekcja-meta">Dział: Dane, sieć i usługi urządzenia · 45 min · Efekty: INF.04.6 (2) kryt. 7 · <span class="zakres zakres-p">INF.04</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- dodać uprawnienia do lokalizacji w manifeście Androida,
- poprosić użytkownika o zgodę w trakcie działania aplikacji,
- pobrać bieżącą pozycję z GPS i obliczyć odległość do punktu,
- ustawić pozycję w emulatorze.

## Wprowadzenie

### Uprawnienia

Dostęp do lokalizacji wymaga **dwóch kroków**:

1. Deklaracji w `Platforms/Android/AndroidManifest.xml` (wewnątrz `<manifest>`):

    ```xml
    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
    <uses-feature android:name="android.hardware.location" android:required="false" />
    <uses-feature android:name="android.hardware.location.gps" android:required="false" />
    ```

2. Zgody użytkownika w trakcie działania (okno systemowe):

    ```csharp
    PermissionStatus status = await Permissions.CheckStatusAsync<Permissions.LocationWhenInUse>();
    if (status != PermissionStatus.Granted)
    {
        status = await Permissions.RequestAsync<Permissions.LocationWhenInUse>();
    }
    if (status != PermissionStatus.Granted)
    {
        await DisplayAlertAsync("Brak zgody", "Aplikacja potrzebuje dostępu do lokalizacji", "OK");
        return;
    }
    ```

### Pobranie pozycji

```csharp
var zadanie = new GeolocationRequest(GeolocationAccuracy.Medium, TimeSpan.FromSeconds(10));
Location? pozycja = await Geolocation.Default.GetLocationAsync(zadanie);

if (pozycja != null)
{
    lblPozycja.Text = $"{pozycja.Latitude:F5}, {pozycja.Longitude:F5}";

    var rynek = new Location(53.5640, 14.8280);   // Goleniów, okolice rynku (w przybliżeniu)
    double km = Location.CalculateDistance(pozycja, rynek, DistanceUnits.Kilometers);
    lblOdleglosc.Text = $"Do rynku w Goleniowie: {km:F1} km";
}
```

| Element | Znaczenie |
|---|---|
| `Latitude` | szerokość geograficzna (N +, S −) |
| `Longitude` | długość geograficzna (E +, W −) |
| `Accuracy` | dokładność w metrach |
| `GetLastKnownLocationAsync()` | ostatnia znana pozycja – szybko, ale może być stara lub `null` |
| `Map.Default.OpenAsync(pozycja)` | otwiera pozycję w aplikacji map |

!!! tip "Pozycja w emulatorze"
    Na pasku emulatora kliknij **⋯ (Extended controls) → Location**. Wpisz współrzędne lub wybierz punkt na mapie i kliknij **Set location**. Emulator nie ma prawdziwego GPS – bez tego `GetLocationAsync` może zwrócić `null`.

!!! warning "Wyjątki"
    `GetLocationAsync` może wyrzucić `FeatureNotEnabledException` (wyłączona lokalizacja w telefonie) lub `PermissionException`. Umieść wywołanie w `try`/`catch`.

## Zadanie główne (25 min)

Utwórz projekt `GdzieJestem`.

1. Dodaj uprawnienia do manifestu.
2. Przycisk **Pobierz pozycję**: sprawdza i prosi o zgodę, pobiera pozycję i wyświetla szerokość i długość (5 miejsc po przecinku) oraz dokładność w metrach.
3. `Picker` **Cel** z miastami i ich współrzędnymi (klasa `Miejsce`): Goleniów (53,5640; 14,8280), Szczecin (53,4285; 14,5528), Gdańsk (54,3520; 18,6466), Warszawa (52,2297; 21,0122).
4. Po pobraniu pozycji i wybraniu celu wyświetl odległość: **Do celu: 23,6 km**.
5. Przycisk **Pokaż na mapie** otwiera bieżącą pozycję w aplikacji map (`Map.Default.OpenAsync`).
6. Obsłuż: brak zgody, wyłączoną lokalizację, brak pozycji.

Sprawdź: ustaw w emulatorze pozycję rynku w Goleniowie (53,5640; 14,8280).

| Cel | Odległość (ok.) |
|---|---|
| Goleniów | 0,0 km |
| Szczecin | 23,6 km |
| Gdańsk | 264,7 km |
| Warszawa | 440,4 km |

Wynik może różnić się o 0,1–0,5 km, bo MAUI liczy odległość na kuli o nieco innym promieniu.

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Dodaj **śledzenie trasy**: włącz nasłuch zmian pozycji (`Geolocation.Default.StartListeningForegroundAsync(...)` i zdarzenie `LocationChanged`), dodawaj kolejne punkty do listy i sumuj przebyty dystans. W emulatorze odtwórz trasę z pliku GPX/KML (**Extended controls → Location → Routes**).

## Czy potrafię…?

- [ ] dodać uprawnienia do manifestu Androida
- [ ] poprosić o zgodę w trakcie działania aplikacji
- [ ] pobrać pozycję i obliczyć odległość do punktu
- [ ] ustawić pozycję w emulatorze
