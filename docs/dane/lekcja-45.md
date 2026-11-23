# Lekcja 45. Czujniki urządzenia

<p class="lekcja-meta">Dział: Dane, sieć i usługi urządzenia · 45 min · Efekty: INF.04.6 (2) kryt. 7 · <span class="zakres zakres-gw">★ poza egzaminem</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- odczytywać dane z akcelerometru,
- wykryć potrząśnięcie telefonem,
- włączyć wibrację i latarkę,
- sprawdzić, czy urządzenie ma dany czujnik.

## Wprowadzenie

| Czujnik / funkcja | Klasa | Uprawnienie Android |
|---|---|---|
| akcelerometr (przyspieszenie w osiach X, Y, Z) | `Accelerometer.Default` | – |
| żyroskop, magnetometr, kompas, barometr | `Gyroscope`, `Magnetometer`, `Compass`, `Barometer` | – |
| wibracja | `Vibration.Default` | `VIBRATE` |
| latarka | `Flashlight.Default` | `CAMERA`, `FLASHLIGHT` |

```csharp
private void OnStartClicked(object? sender, EventArgs e)
{
    if (!Accelerometer.Default.IsSupported)
    {
        lblInfo.Text = "Brak akcelerometru";
        return;
    }
    Accelerometer.Default.ReadingChanged += OnOdczyt;
    Accelerometer.Default.ShakeDetected += OnPotrzasniecie;
    Accelerometer.Default.Start(SensorSpeed.UI);
}

private void OnOdczyt(object? sender, AccelerometerChangedEventArgs e)
{
    var a = e.Reading.Acceleration;               // wartości w g (1 g ≈ 9,81 m/s²)
    lblXyz.Text = $"X: {a.X:F2}  Y: {a.Y:F2}  Z: {a.Z:F2}";
}

private void OnPotrzasniecie(object? sender, EventArgs e)
{
    Vibration.Default.Vibrate(TimeSpan.FromMilliseconds(300));
}

protected override void OnDisappearing()
{
    base.OnDisappearing();
    Accelerometer.Default.Stop();
    Accelerometer.Default.ReadingChanged -= OnOdczyt;
    Accelerometer.Default.ShakeDetected -= OnPotrzasniecie;
}
```

```csharp
try
{
    await Flashlight.Default.TurnOnAsync();   // TurnOffAsync()
}
catch (FeatureNotSupportedException)
{
    await DisplayAlertAsync("Latarka", "To urządzenie nie ma latarki", "OK");
}
```

!!! tip "Czujniki w emulatorze"
    **Extended controls → Virtual sensors** pozwala obracać wirtualnym telefonem i zmieniać odczyty. Wibracji i latarki emulator nie pokaże – sprawdź je na telefonie (jeśli masz kabel USB i włączone debugowanie USB) albo obsłuż wyjątek.

!!! warning "Bateria"
    Czujniki zużywają energię. Zawsze zatrzymuj je w `OnDisappearing`. `SensorSpeed.UI` wystarcza do interfejsu, `Fastest` jest potrzebne tylko w grach.

## Zadanie główne (25 min)

Utwórz projekt `Kostka`.

1. Dodaj do manifestu uprawnienia `VIBRATE`, `CAMERA`, `FLASHLIGHT`.
2. Ekran: duża etykieta z wynikiem rzutu (rozmiar `120`, np. ⚀ … ⚅ albo cyfra), etykieta **Potrząśnij telefonem, aby rzucić**, etykieta z odczytami X/Y/Z, przycisk **Rzuć** (dla Windows i emulatora).
3. Potrząśnięcie (`ShakeDetected`) lub przycisk losuje liczbę 1–6, animuje etykietę (obrót o 360° w 300 ms) i wibruje 200 ms.
4. Pod spodem historia ostatnich 10 rzutów i średnia.
5. Przycisk **Latarka** włącza i wyłącza latarkę; na urządzeniu bez latarki wyświetla komunikat.
6. Gdy telefon leży ekranem w dół (`Z < -0.8`), tło zmienia się na czarne (tryb „nie przeszkadzać”).

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Wykonaj poziomicę: kółko (`Ellipse` lub `BoxView` z `CornerRadius`) w `AbsoluteLayout` przesuwa się zgodnie z odczytami osi X i Y. Gdy telefon leży poziomo (|X| i |Y| < 0,05), kółko zmienia kolor na zielony.

## Czy potrafię…?

- [ ] uruchomić i zatrzymać odczyt akcelerometru
- [ ] wykryć potrząśnięcie
- [ ] włączyć wibrację i latarkę z obsługą braku funkcji
- [ ] zmieniać odczyty czujników w emulatorze
