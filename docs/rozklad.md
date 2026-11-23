# Rozkład materiału

**Klasa IV · 64 godziny (45 min) · zajęcia w pracowni**

Przedmiot przygotowuje do kwalifikacji **INF.04** *Projektowanie, programowanie i testowanie aplikacji* (jednostka efektów INF.04.6 *Programowanie aplikacji mobilnych* oraz wybrane efekty z INF.04.3 *Projektowanie oprogramowania* i INF.04.8 *Testowanie i dokumentowanie aplikacji*). Pracujesz w **Visual Studio Community 2026** i **.NET MAUI** (język C#, interfejs w XAML), aplikacje uruchamiasz w emulatorze Androida.

Legenda kolumny „Zakres”:

- **P**: treść z podstawy programowej, wymagana na egzaminie
- **P+**: treść z podstawy rozszerzona poza typowy zakres egzaminu
- **★**: treść spoza podstawy (praktyka zawodowa, nowoczesne techniki)

Kody efektów: `6.1` = INF.04.6 efekt 1 (środowisko dla aplikacji mobilnych), `6.2` = INF.04.6 efekt 2 (programuje aplikacje mobilne), w nawiasie numery kryteriów weryfikacji, np. `6.2 (5)` = interfejs w XAML; `3.5` = INF.04.3 narzędzia do planowania i zarządzania projektem, `3.6` = INF.04.3 projektuje aplikację, `3.8` = wzorce projektowe, `3.9` = prawo autorskie i licencje; `4.2` = INF.04.4 zasady programowania (aplikacja konsolowa); `8.1` = INF.04.8 walidacja kodu, `8.2` = dokumentacja, `8.3` = testy; `1` = BHP (INF.04.1).

## Dział 0. Start (3 h)

| Nr | Temat | Efekty | Zakres |
|---|---|---|---|
| 1 | Zasady BHP i organizacja pracy w pracowni. Visual Studio Community 2026 z obciążeniem .NET MAUI | 1, 6.1 (1, 2) | P |
| 2 | Pierwsza aplikacja .NET MAUI: struktura projektu, `App`, `AppShell`, `MainPage`, uruchomienie na Windows i w emulatorze | 6.1 (2, 3), 6.2 (11) | P |
| 3 | Emulator Androida: Android Device Manager, Hot Reload, lista błędów. Zrzuty ekranu jak na egzaminie | 6.1 (3), 6.2 (11), 8.2 | P |

## Dział 1. XAML i układy (9 h)

| Nr | Temat | Efekty | Zakres |
|---|---|---|---|
| 4 | Składnia XAML: elementy, właściwości, `x:Name`; `Label`, `Button`, kolory i czcionki | 6.2 (5) | P |
| 5 | Układy liniowe: `VerticalStackLayout`, `HorizontalStackLayout`, `Margin`, `Padding`, wyrównanie | 6.2 (5, 6) | P |
| 6 | Układ siatki `Grid`: wiersze, kolumny, rozmiary `Auto`/`*`, scalanie (`ColumnSpan`, `RowSpan`) | 6.2 (5, 6) | P |
| 7 | `FlexLayout`, `AbsoluteLayout`, `ScrollView`, `Border` | 6.2 (5, 6) | P+ |
| 8 | Obrazy: `Image`, zasoby w `Resources/Images`, `Aspect`, `ImageButton` | 6.2 (4, 6) | P |
| 9 | Style i zasoby: `ResourceDictionary`, `Style`, `StaticResource`, plik `Colors.xaml` | 6.2 (5), 3.6 (4) | P |
| 10 | Zdarzenia: `Clicked`, kod w pliku `.xaml.cs`, zmiana właściwości z C# | 6.2 (6) | P |
| 11 | Pola edycyjne `Entry` i `Editor`: `Keyboard="Numeric"`, `Placeholder`, `TextChanged`, `int.TryParse` | 6.2 (4, 6) | P |
| 12 | Aplikacja-kalkulator. Zadanie w stylu egzaminu | 6.2 (5, 6, 11), 3.6 (4) | P |

## Dział 2. Kontrolki i wiązanie danych (14 h)

| Nr | Temat | Efekty | Zakres |
|---|---|---|---|
| 13 | Przełączniki: `Switch`, `CheckBox`, `RadioButton` | 6.2 (4, 6) | P |
| 14 | Wartości z zakresu: `Slider`, `Stepper`, `ProgressBar` | 6.2 (4, 6) | P |
| 15 | Wybór z listy i daty: `Picker`, `DatePicker`, `TimePicker` | 6.2 (6, 7) | P |
| 16 | Galeria obrazów (karuzela, przyciski poprzedni/następny). Zadanie w stylu egzaminu | 6.2 (5, 6, 11) | P |
| 17 | Okna dialogowe: `DisplayAlert`, `DisplayActionSheet`, `DisplayPromptAsync`; `async` i `await` | 6.2 (4, 6) | P |
| 18 | Wiązanie danych między kontrolkami: `{Binding}`, `x:Reference`, `StringFormat` | 6.2 (5, 6) | P |
| 19 | `BindingContext` i klasa z `INotifyPropertyChanged` | 6.2 (5, 6) | P |
| 20 | Konwertery wartości i wyzwalacze (`DataTrigger`) | 6.2 (5) | P+ |
| 21 | Listy: `CollectionView`, `ItemTemplate`, `ObservableCollection` | 6.2 (4, 6) | P |
| 22 | Lista z dodawaniem, usuwaniem i zaznaczaniem elementów. Zadanie w stylu egzaminu | 6.2 (6, 7), 3.6 (9) | P |
| 23 | Animacje widoków: `FadeTo`, `RotateTo`, `ScaleTo`, `TranslateTo` | 6.2 (4, 6) | P |
| 24 | Dźwięk w aplikacji: odtwarzanie plików z zasobów (`Plugin.Maui.Audio`) | 6.2 (4, 6) | P+ |
| 25 | Powtórka: aplikacja z kilkoma kontrolkami według projektu | 6.2 (5, 6), 3.6 (1, 4) | P |
| 26 | Sprawdzian praktyczny: aplikacja mobilna w stylu egzaminu | 6.2 (5, 6, 11), 8.2 | P |

## Dział 3. Nawigacja i platformy (7 h)

| Nr | Temat | Efekty | Zakres |
|---|---|---|---|
| 27 | Wiele stron: `Navigation.PushAsync`, `PopAsync`, pasek nawigacji | 6.2 (4, 6) | P |
| 28 | Przekazywanie danych między stronami | 6.2 (6) | P |
| 29 | `Shell`: zakładki (`TabBar`) i menu wysuwane (`Flyout`) | 6.2 (4, 6) | P |
| 30 | Trasy w `Shell`, parametry `QueryProperty`, menu `ToolbarItem` | 6.2 (4, 6) | P |
| 31 | Dostosowanie do platformy i urządzenia: `OnPlatform`, `OnIdiom`, `DeviceInfo`, orientacja ekranu | 6.2 (10), 3.6 (5) | P |
| 32 | Aplikacja z menu i podstronami. Zadanie w stylu egzaminu | 6.2 (5, 6, 10) | P |
| 33 | Tryb jasny i ciemny: `AppThemeBinding`, `DynamicResource` | 6.2 (5) | ★ |

## Dział 4. Dane, sieć i usługi urządzenia (14 h)

| Nr | Temat | Efekty | Zakres |
|---|---|---|---|
| 34 | Preferencje użytkownika: `Preferences` (zapis ustawień) | 6.2 (3) | P |
| 35 | Pliki w pamięci aplikacji: `FileSystem.AppDataDirectory`, zapis i odczyt, JSON (`System.Text.Json`) | 6.2 (3) | P |
| 36 | Baza SQLite cz. 1: pakiet `sqlite-net-pcl`, model, tworzenie tabeli, dodawanie rekordów | 6.2 (9), 3.6 (8) | P |
| 37 | Baza SQLite cz. 2: odczyt, edycja i usuwanie; lista z bazy w `CollectionView` | 6.2 (9) | P |
| 38 | Aplikacja z bazą danych. Zadanie w stylu egzaminu | 6.2 (3, 9) | P |
| 39 | Dane z internetu: `HttpClient`, pobieranie JSON, uprawnienie `INTERNET` | 6.2 (8), 3.6 (7) | P |
| 40 | Wysyłanie danych (POST) i obsługa błędów sieci: `try`/`catch`, `Connectivity` | 6.2 (8) | P |
| 41 | Zegar i stoper: `IDispatcherTimer` | 6.2 (7) | P |
| 42 | Kalendarz i daty: `DateTime`, `TimeSpan`, odliczanie dni | 6.2 (7) | P |
| 43 | Lokalizacja: `Geolocation`, uprawnienia, pozycja w emulatorze | 6.2 (7) | P |
| 44 | Powiadomienia: lokalne powiadomienie systemowe, `Toast` i `Snackbar` | 6.2 (7) | P |
| 45 | Czujniki urządzenia: akcelerometr, wibracje, latarka | 6.2 (7) | ★ |
| 46 | Aparat i galeria zdjęć: `MediaPicker` | 6.2 (7) | ★ |
| 47 | Sprawdzian praktyczny: aplikacja z danymi | 6.2 (3, 6, 9), 8.2 | P |

## Dział 5. Jakość, testy i publikacja (9 h)

| Nr | Temat | Efekty | Zakres |
|---|---|---|---|
| 48 | Wzorzec MVVM: model, widok, ViewModel, `Command` | 3.8, 6.2 (5) | P+ |
| 49 | MVVM z `CommunityToolkit.Mvvm`: `[ObservableProperty]`, `[RelayCommand]` | 3.8 | ★ |
| 50 | Debugowanie: punkty przerwania, okno zmiennych, wyjątki, okno Output | 8.1 (3, 4) | P |
| 51 | Testy jednostkowe w xUnit dla logiki aplikacji | 8.3 (2, 3, 13) | P |
| 52 | Scenariusze testów i raport błędów; testy interfejsu na różnych urządzeniach | 8.3 (7, 10, 11, 12) | P |
| 53 | Dokumentacja: komentarze nagłówkowe według wzoru z egzaminu, instrukcja użytkownika | 8.2 (1, 2, 4) | P |
| 54 | Nazwa, ikona, ekran startowy, wersja aplikacji; licencje zasobów | 6.2 (10, 12), 3.9 | P |
| 55 | Przygotowanie do publikacji: podpisany plik AAB/APK, sklep Google Play | 6.2 (12) | P |
| 56 | Git i GitHub w projekcie MAUI: repozytorium, `.gitignore`, commity | 3.5 | ★ |

## Dział 6. Podsumowanie (8 h)

| Nr | Temat | Efekty | Zakres |
|---|---|---|---|
| 57–60 | Symulacja egzaminu INF.04 (180 min): aplikacja konsolowa, aplikacja mobilna, dokumentacja | 4.2, 6.2, 8.2 | P |
| 61–64 | Projekt końcowy: własna aplikacja mobilna (projekt, wykonanie, testy, prezentacja) | 3.6, 6.2, 8.3 | ★ |

**Podsumowanie godzin:** P/P+ ≈ 55 h, ★ ≈ 9 h (ok. 14%).

!!! info "Wersje programów"
    Materiały są przygotowane dla Visual Studio Community 2026 i .NET MAUI w wersji .NET 10 (LTS). W nowszych wersjach .NET część okien i szablonów może wyglądać nieco inaczej. Zamiast przestarzałych kontrolek `ListView` i `Frame` używamy `CollectionView` i `Border`.
