# Lekcja 54. Nazwa, ikona, ekran startowy, wersja; licencje zasobów

<p class="lekcja-meta">Dział: Jakość, testy i publikacja · 45 min · Efekty: INF.04.6 (2) kryt. 10, 12, INF.04.3 (9) · <span class="zakres zakres-p">INF.04</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- zmienić nazwę wyświetlaną, identyfikator i wersję aplikacji,
- przygotować ikonę aplikacji z tła i pierwszego planu w SVG,
- zmienić ekran startowy (*splash screen*),
- dobrać zasoby (obrazy, dźwięki, czcionki) zgodnie z licencją.

## Wprowadzenie

Ustawienia aplikacji są w pliku projektu `.csproj` (dwuklik na nazwie projektu w **Eksploratorze rozwiązań**).

```xml
<PropertyGroup>
    <ApplicationTitle>Moja Aplikacja</ApplicationTitle>          <!-- nazwa pod ikoną -->
    <ApplicationId>pl.szkola.mojaaplikacja</ApplicationId>       <!-- unikalny identyfikator -->
    <ApplicationDisplayVersion>1.0</ApplicationDisplayVersion>   <!-- wersja dla ludzi -->
    <ApplicationVersion>1</ApplicationVersion>                   <!-- numer kolejny, tylko rośnie -->
</PropertyGroup>

<ItemGroup>
    <MauiIcon Include="Resources\AppIcon\appicon.svg"
              ForegroundFile="Resources\AppIcon\appiconfg.svg" Color="#4527A0" />
    <MauiSplashScreen Include="Resources\Splash\splash.svg"
                      Color="#4527A0" BaseSize="128,128" />
</ItemGroup>
```

| Ustawienie | Uwagi |
|---|---|
| `ApplicationId` | odwrócona domena, małe litery, bez polskich znaków i spacji; po publikacji w sklepie nie można go zmienić |
| `ApplicationDisplayVersion` | np. `1.0`, `1.1`, `2.0`: widzi ją użytkownik |
| `ApplicationVersion` | liczba całkowita; każda nowa wersja w sklepie musi mieć większą |
| ikona | MAUI sam tworzy wszystkie rozmiary ikony z jednego pliku SVG; tło wypełnia cały kwadrat, pierwszy plan mieści się w środkowym obszarze (Android przycina ikonę do koła lub zaokrąglonego kwadratu) |
| ekran startowy | jeden obraz SVG na środku i kolor tła `Color` |

!!! warning "Stara ikona w emulatorze"
    Android przechowuje ikonę w pamięci podręcznej. Po zmianie ikony odinstaluj aplikację z emulatora (przytrzymaj ikonę → **Odinstaluj**) i wybierz **Kompilacja → Wyczyść rozwiązanie** przed ponownym uruchomieniem.

**Licencje zasobów.** Obraz z internetu nie jest „darmowy” tylko dlatego, że można go pobrać. Zasoby w aplikacji muszą mieć licencję pozwalającą na takie użycie.

| Licencja | Co możesz | Obowiązek |
|---|---|---|
| własne dzieło | wszystko | – |
| CC0 (domena publiczna) | wszystko, także komercyjnie | brak |
| CC BY | używać i zmieniać, także komercyjnie | podać autora i licencję |
| CC BY-NC | używać i zmieniać, tylko niekomercyjnie | autor, licencja, brak zarobku |
| CC BY-ND | używać bez zmian | autor, licencja, bez przeróbek |
| MIT, Apache 2.0 (biblioteki, czcionki) | używać w aplikacji, także płatnej | dołączyć tekst licencji |
| „wszelkie prawa zastrzeżone” | nic bez zgody autora | – |

## Zadanie główne (25 min)

Plik startowy: [ikona.zip](../pliki/lekcja-54/ikona.zip){ download } (`appicon.svg` – tło, `appiconfg.svg` – pierwszy plan).

Pracujesz na swoim projekcie `Napiwek` z lekcji 48 (albo innym własnym projekcie).

1. Ustaw nazwę wyświetlaną **Napiwek**, identyfikator `pl.<twojeinicjaly>.napiwek`, wersję `1.0` i numer `1`.
2. Zastąp pliki w `Resources/AppIcon` plikami z archiwum. Otwórz `appiconfg.svg` w Notatniku lub Inkscape i zaprojektuj własny pierwszy plan: zmień literę **A** na **%** albo narysuj symbol. Usuń przerywaną ramkę pomocniczą. Zmień kolor tła w `appicon.svg` na kolor paska Twojej aplikacji.
3. W `Resources/Splash/splash.svg` zmień rysunek (może to być ten sam symbol co na ikonie) i ustaw `Color` ekranu startowego.
4. Odinstaluj starą wersję z emulatora, wyczyść rozwiązanie i uruchom aplikację. Wykonaj zrzuty: ikona na ekranie głównym emulatora i ekran startowy.
5. Dodaj w aplikacji stronę lub etykietę **O aplikacji**: wersja (odczytaj ją w kodzie: `AppInfo.Current.VersionString`), autor, licencje użytych zasobów.
6. Zmień wersję na `1.1` i numer na `2`, uruchom ponownie i sprawdź, że **O aplikacji** pokazuje nową wersję.

??? question "Podpowiedź: ekran startowy znika za szybko"
    Na emulatorze aplikacja startuje szybko, a ekran startowy widać przez ułamek sekundy. Zrzut zrobisz, zamykając aplikację przyciskiem **Wstecz** i uruchamiając ją ponownie z ikony. Pierwsze uruchomienie po instalacji trwa dłużej.

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Dodaj do aplikacji własną czcionkę z licencją SIL Open Font License (np. z katalogu czcionek systemu Linux lub pobraną przez nauczyciela). Skopiuj plik `.ttf` do `Resources/Fonts`, zarejestruj ją w `MauiProgram.cs` (`fonts.AddFont("plik.ttf", "MojaCzcionka")`) i użyj w nagłówku. Dopisz czcionkę z licencją na stronie **O aplikacji**.

## Czy potrafię…?

- [ ] zmienić nazwę, identyfikator i wersję aplikacji w pliku `.csproj`
- [ ] wyjaśnić różnicę między `ApplicationDisplayVersion` a `ApplicationVersion`
- [ ] przygotować ikonę z tła i pierwszego planu
- [ ] zmienić ekran startowy
- [ ] sprawdzić, czy mogę użyć zasobu, i podać jego licencję
