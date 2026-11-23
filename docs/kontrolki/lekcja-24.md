# Lekcja 24. Dźwięk w aplikacji

<p class="lekcja-meta">Dział: Kontrolki i wiązanie danych · 45 min · Efekty: INF.04.6 (2) kryt. 4, 6 · <span class="zakres zakres-p">INF.04</span> <span class="zakres zakres-gw">P+</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- dodać pakiet NuGet do projektu,
- umieścić plik dźwiękowy w zasobach aplikacji (`Resources/Raw`),
- odtworzyć dźwięk i zmienić jego głośność.

## Wprowadzenie

### Pakiety NuGet

MAUI nie ma wbudowanego odtwarzacza krótkich dźwięków. Użyjemy pakietu **Plugin.Maui.Audio**. Instalacja: prawy przycisk na projekcie → **Zarządzaj pakietami NuGet** → zakładka **Przeglądaj** → wyszukaj `Plugin.Maui.Audio` → **Zainstaluj** (najnowsza stabilna wersja).

### Pliki surowe

Pliki dźwiękowe kopiujesz do **`Resources/Raw`**. Mają akcję kompilacji **MauiAsset** i są dołączane do aplikacji bez zmian. Odczytujesz je metodą `FileSystem.OpenAppPackageFileAsync("nazwa.wav")`.

```csharp
using Plugin.Maui.Audio;

public partial class MainPage : ContentPage
{
    private IAudioPlayer? odtwarzacz;

    private async void OnDzwonekClicked(object? sender, EventArgs e)
    {
        await OdtworzAsync("dzwonek.wav");
    }

    private async Task OdtworzAsync(string plik)
    {
        odtwarzacz?.Dispose();                     // zwolnij poprzedni dźwięk
        Stream strumien = await FileSystem.OpenAppPackageFileAsync(plik);
        odtwarzacz = AudioManager.Current.CreatePlayer(strumien);
        odtwarzacz.Volume = sldGlosnosc.Value;     // 0.0 – 1.0
        odtwarzacz.Play();
    }
}
```

| Właściwość / metoda `IAudioPlayer` | Działanie |
|---|---|
| `Play()`, `Pause()`, `Stop()` | sterowanie |
| `Volume` | głośność 0–1 |
| `Loop` | odtwarzanie w pętli |
| `IsPlaying`, `Duration`, `CurrentPosition` | stan |
| `PlaybackEnded` | zdarzenie: koniec odtwarzania |

!!! warning "Dźwięk w emulatorze"
    Emulator odtwarza dźwięk przez głośniki komputera. W pracowni używaj słuchawek. Jeśli nic nie słychać, sprawdź głośność emulatora (przyciski boczne na pasku emulatora).

!!! info "Licencje zasobów"
    Dźwięki z archiwum zostały wygenerowane programowo dla tego kursu. Gdy pobierasz dźwięki z internetu, sprawdź licencję (np. CC0, CC BY – trzeba podać autora).

## Zadanie główne (25 min)

Pobierz i rozpakuj [dzwieki.zip](../pliki/lekcja-24/dzwieki.zip){ download }: `dzwonek.wav`, `klik.wav`, `fanfara.wav`, `blad.wav`.

Utwórz projekt `Dzwieki`.

1. Zainstaluj pakiet `Plugin.Maui.Audio`. Skopiuj pliki `.wav` do `Resources/Raw`.
2. Ekran: nagłówek **Panel dźwięków** i siatka 2×2 dużych przycisków (wysokość `120`, różne kolory tła): **Dzwonek**, **Klik**, **Fanfara**, **Błąd**. Każdy odtwarza swój dźwięk przez wspólną metodę `OdtworzAsync`.
3. Pod siatką suwak **Głośność** (0–1, start 0.8) i etykieta z wartością w procentach (**Głośność: 80%**, wiązanie z `StringFormat='{0:P0}'`).
4. `Switch` **Powtarzaj** – gdy jest włączony, następny dźwięk odtwarza się w pętli (`Loop = true`).
5. Przycisk **Stop** zatrzymuje bieżący dźwięk.
6. Etykieta `lblStatus` pokazuje **Odtwarzam: fanfara.wav**, a po zakończeniu (zdarzenie `PlaybackEnded`) – **Gotowe**.

??? question "Podpowiedź: zmiana etykiety po zdarzeniu z odtwarzacza"
    Zdarzenie może przyjść spoza wątku interfejsu. Zmieniaj kontrolki przez `MainThread.BeginInvokeOnMainThread(() => lblStatus.Text = "Gotowe");`.

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Połącz dźwięk z poprzednimi lekcjami: w projekcie `ZgadnijLiczbe` (lekcja 17) odtwarzaj `blad.wav` po nietrafionej próbie i `fanfara.wav` po odgadnięciu liczby.

## Czy potrafię…?

- [ ] zainstalować pakiet NuGet
- [ ] dodać plik do `Resources/Raw` i odczytać go w aplikacji
- [ ] odtworzyć dźwięk i ustawić głośność
- [ ] zmienić kontrolkę z innego wątku przez `MainThread`
