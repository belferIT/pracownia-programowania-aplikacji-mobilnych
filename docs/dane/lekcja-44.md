# Lekcja 44. Powiadomienia

<p class="lekcja-meta">Dział: Dane, sieć i usługi urządzenia · 45 min · Efekty: INF.04.6 (2) kryt. 7 · <span class="zakres zakres-p">INF.04</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- wyświetlić krótkie powiadomienie w aplikacji (`Toast`, `Snackbar`),
- zaplanować powiadomienie systemowe, które pojawi się, nawet gdy aplikacja jest zamknięta,
- poprosić o zgodę na powiadomienia (Android 13+).

## Wprowadzenie

| Rodzaj | Gdzie widać | Narzędzie |
|---|---|---|
| **Toast** | krótki dymek na dole ekranu, znika sam | `CommunityToolkit.Maui` |
| **Snackbar** | pasek na dole z przyciskiem akcji (np. **Cofnij**) | `CommunityToolkit.Maui` |
| **Powiadomienie lokalne** | w obszarze powiadomień systemu, także po zamknięciu aplikacji | pakiet `Plugin.LocalNotification` |

### CommunityToolkit.Maui

Zainstaluj pakiet `CommunityToolkit.Maui` i dodaj w `MauiProgram.cs`:

```csharp
using CommunityToolkit.Maui;

builder
    .UseMauiApp<App>()
    .UseMauiCommunityToolkit();
```

```csharp
using CommunityToolkit.Maui.Alerts;
using CommunityToolkit.Maui.Core;

await Toast.Make("Zapisano notatkę", ToastDuration.Short).Show();

var snackbar = Snackbar.Make("Usunięto notatkę",
                             action: () => PrzywrocNotatke(),
                             actionButtonText: "Cofnij",
                             duration: TimeSpan.FromSeconds(4));
await snackbar.Show();
```

### Powiadomienie lokalne

Zainstaluj pakiet `Plugin.LocalNotification`, dodaj w `MauiProgram.cs` `.UseLocalNotification()` (przestrzeń nazw `Plugin.LocalNotification`), a w `AndroidManifest.xml` uprawnienie:

```xml
<uses-permission android:name="android.permission.POST_NOTIFICATIONS" />
```

```csharp
using Plugin.LocalNotification;

if (!await LocalNotificationCenter.Current.AreNotificationsEnabled())
{
    await LocalNotificationCenter.Current.RequestNotificationPermission();
}

var powiadomienie = new NotificationRequest
{
    NotificationId = 100,
    Title = "Czas na przerwę",
    Description = "Odejdź od ekranu na 5 minut",
    Schedule = new NotificationRequestSchedule { NotifyTime = DateTime.Now.AddSeconds(30) }
};
await LocalNotificationCenter.Current.Show(powiadomienie);
```

!!! warning "Wersje pakietów"
    Pakiety spoza MAUI zmieniają się szybciej niż sam MAUI. Jeśli kod z lekcji się nie kompiluje, otwórz stronę pakietu w NuGet (zakładka **README**) i sprawdź aktualny sposób konfiguracji. To normalna praca programisty.

!!! info "Snackbar na Windows"
    Na Windows `Snackbar` wymaga dodatkowej konfiguracji w `UseMauiCommunityToolkit(...)`. W tej lekcji testuj go w emulatorze Androida.

## Zadanie główne (25 min)

Utwórz projekt `Przypominajka`.

1. Zainstaluj i skonfiguruj `CommunityToolkit.Maui` i `Plugin.LocalNotification`. Dodaj uprawnienie do manifestu.
2. Formularz: **Treść przypomnienia** (`Entry`), `Stepper` **Za ile minut** (1–60), przycisk **Zaplanuj**, lista zaplanowanych przypomnień (`CollectionView`: treść i godzina `HH:mm`).
3. **Zaplanuj**: prosi o zgodę na powiadomienia (jeśli trzeba), planuje powiadomienie lokalne za wybraną liczbę minut, dodaje przypomnienie do listy i pokazuje `Toast` **Przypomnienie o 14:35**. Każde powiadomienie ma inny `NotificationId` (licznik).
4. Pusta treść – `Toast` **Wpisz treść przypomnienia**.
5. Wybranie przypomnienia na liście usuwa je (`LocalNotificationCenter.Current.Cancel(id)`) i pokazuje `Snackbar` **Usunięto** z akcją **Cofnij**, która przywraca przypomnienie (i planuje je ponownie).
6. Sprawdź: zaplanuj powiadomienie za 1 minutę, zamknij aplikację i poczekaj.

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Dodaj powtarzanie: `Switch` **Codziennie** – ustaw w `Schedule` `RepeatType = NotificationRepeat.Daily`. Po dotknięciu powiadomienia aplikacja otwiera się i wyświetla jego treść (zdarzenie `LocalNotificationCenter.Current.NotificationActionTapped`).

## Czy potrafię…?

- [ ] skonfigurować `CommunityToolkit.Maui` w `MauiProgram.cs`
- [ ] wyświetlić `Toast` i `Snackbar` z akcją
- [ ] zaplanować powiadomienie lokalne i je anulować
- [ ] poprosić o zgodę na powiadomienia
