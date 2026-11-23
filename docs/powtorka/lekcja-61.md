# Lekcje 61–64. Projekt końcowy: własna aplikacja mobilna

<p class="lekcja-meta">Dział: Podsumowanie · 4 × 45 min · Efekty: INF.04.3 (6), INF.04.6 (2), INF.04.8 (3) · <span class="zakres zakres-gw">★ poza egzaminem</span></p>

## Cel projektu

Przez cztery lekcje projektujesz, programujesz, testujesz i prezentujesz **własną** aplikację mobilną. Łączysz w niej to, czego nauczyłeś się w całym roku: układy XAML, kontrolki, nawigację, zapis danych, testy i dokumentację.

Pracujesz samodzielnie albo w parze (wtedy wymagania z kolumny **para**).

## Wymagania

| Wymaganie | Samodzielnie | Para |
|---|---|---|
| strony (`Shell` lub `PushAsync`) | co najmniej 2 | co najmniej 3 |
| lista `CollectionView` z własnym szablonem elementu | ✔ | ✔ |
| trwały zapis danych: SQLite, plik JSON lub `Preferences` | ✔ | SQLite |
| walidacja danych wpisywanych przez użytkownika | ✔ | ✔ |
| własna ikona, nazwa i wersja aplikacji | ✔ | ✔ |
| testy jednostkowe xUnit logiki aplikacji | co najmniej 3 | co najmniej 6 |
| scenariusz testów ręcznych | co najmniej 5 przypadków | co najmniej 8 przypadków |
| funkcja urządzenia lub sieci (lokalizacja, aparat, czujnik, `HttpClient`, powiadomienie) | dla chętnych | co najmniej 1 |
| repozytorium Git z regularnymi commitami | zalecane | wymagane, commity obu osób |

!!! tip "Przykładowe tematy"
    - dziennik nauki: przedmioty, sesje z czasem (stoper), statystyki tygodnia,
    - domowa spiżarnia: produkty z datą ważności, lista „kończy się termin”,
    - planer treningów z historią i wykresem postępu z kontrolek `BoxView`,
    - budżet kieszonkowego: wpływy, wydatki, kategorie, saldo,
    - quiz z pytaniami z pliku JSON i tabelą najlepszych wyników,
    - kolekcja (płyty, gry, książki) ze zdjęciami z aparatu,
    - własny pomysł zatwierdzony przez nauczyciela.

    Wybierz temat, który zrobisz w trzy lekcje. Lepsza mała aplikacja, która działa, niż duża, która się nie kompiluje.

## Lekcja 61. Projekt

1. Wybierz temat i wypełnij **kartę projektu** (dokument tekstowy `projekt`):
    - nazwa aplikacji i jedno zdanie: dla kogo jest i jaki problem rozwiązuje,
    - **historyjki użytkownika** (co najmniej 5) w postaci: *Jako użytkownik chcę dodać produkt z datą ważności, aby wiedzieć, co zjeść najpierw*,
    - podział historyjek na **konieczne** (muszą działać na prezentacji) i **dodatkowe**,
    - **rysunki ekranów** w ASCII albo na kartce (zdjęcie), jak w poleceniach z lekcji: wszystkie strony i przejścia między nimi,
    - **model danych**: klasy, pola i ich typy (np. `Produkt`: `Id` int, `Nazwa` string, `DataWaznosci` DateTime),
    - kolory (HEX) i czcionki aplikacji.
2. Pokaż kartę nauczycielowi do akceptacji.
3. Utwórz projekt, repozytorium Git (lekcja 56), pustą nawigację między stronami. Pierwszy commit: **Szkielet aplikacji**.

## Lekcja 62. Wykonanie

1. Zaprogramuj historyjki **konieczne**: interfejs, model, zapis i odczyt danych.
2. Logikę (obliczenia, walidację, filtrowanie) umieszczaj w osobnych klasach, nie w plikach `.xaml.cs`. Przetestujesz ją w lekcji 63.
3. Po każdej działającej historyjce zrób commit.
4. Na koniec lekcji zapisz w karcie projektu, co działa, a czego jeszcze brakuje.

## Lekcja 63. Wykonanie i testy

1. Dokończ historyjki konieczne. Dodatkowe – jeśli masz czas.
2. Ustaw ikonę, nazwę i wersję `1.0` (lekcja 54).
3. Dodaj projekt testowy xUnit i napisz testy logiki (lekcja 51). Jeśli logika jest w projekcie MAUI, przenieś ją do biblioteki klas.
4. Napisz scenariusz testów ręcznych (lekcja 52). Zamień się miejscem z inną osobą: ona testuje Twoją aplikację według Twojego scenariusza, Ty – jej.
5. Popraw zgłoszone błędy.

## Lekcja 64. Prezentacja

Prezentacja trwa **3–4 minuty** na osobę (parę) w emulatorze wyświetlanym na projektorze:

1. Problem i dla kogo jest aplikacja (30 s).
2. Pokaz działania: typowy scenariusz od początku do końca, zapis danych po ponownym uruchomieniu (2 min).
3. Jeden fragment kodu, z którego jesteś dumny, albo problem, który rozwiązałeś (1 min).
4. Wyniki testów: Eksplorator testów i liczba przypadków ręcznych (30 s).

Oddajesz folder `Nazwisko_Imie_projekt` z projektem (bez `bin` i `obj`), kartą projektu, scenariuszem testów i trzema zrzutami ekranu albo adres repozytorium na GitHub.

## Kryteria oceny (30 pkt)

| Kryterium | Punkty |
|---|---|
| karta projektu: historyjki, rysunki ekranów, model danych | 4 |
| aplikacja kompiluje się i uruchamia, działają historyjki konieczne | 6 |
| interfejs: czytelny, zgodny z projektem, bez nachodzenia elementów | 4 |
| nawigacja i lista `CollectionView` | 3 |
| trwały zapis danych i walidacja | 4 |
| testy jednostkowe i scenariusz testów ręcznych | 4 |
| ikona, nazwa, wersja; kod czytelny, logika poza `.xaml.cs` | 3 |
| prezentacja | 2 |

Progi ocen ustala nauczyciel zgodnie z WSO.

## Czy potrafię…?

- [ ] zaplanować aplikację: historyjki, rysunki ekranów, model danych
- [ ] podzielić pracę na etapy i dokończyć to, co najważniejsze
- [ ] połączyć w jednej aplikacji nawigację, listę, zapis danych i walidację
- [ ] przetestować aplikację testami jednostkowymi i ręcznymi
- [ ] zaprezentować swoją aplikację w kilka minut
