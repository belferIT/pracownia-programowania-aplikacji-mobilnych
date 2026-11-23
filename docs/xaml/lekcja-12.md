# Lekcja 12. Kalkulator kosztów przejazdu. Zadanie w stylu egzaminu

<p class="lekcja-meta">Dział: XAML i układy · 45 min · Efekty: INF.04.6 (2) kryt. 5, 6, 11, INF.04.3 (6) kryt. 4 · <span class="zakres zakres-p">INF.04</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- wykonać aplikację mobilną według opisu wyglądu i działania jak w arkuszu INF.04,
- połączyć układ, style, pola edycyjne i obsługę zdarzeń,
- sprawdzić aplikację na danych testowych.

## Wprowadzenie

Część II arkusza INF.04 (aplikacja mobilna) ma stały schemat:

1. **Rysunek** lub zrzut ekranu ze stanem początkowym aplikacji.
2. **Opis wyglądu i działania**: kolejne elementy od góry ekranu.
3. **Założenia aplikacji**: język znaczników (XAML), typ układu, kolory, nazwy, sposób obsługi zdarzeń.
4. Kod przygotowany do skopiowania do folderu `mobilna` oraz zrzut ekranu `mobilna.jpg`.

!!! tip "Kolejność pracy na egzaminie"
    1. Najpierw cały wygląd w XAML (bez działania) i uruchomienie w emulatorze.
    2. Potem działanie: zdarzenie po zdarzeniu, każde od razu sprawdzone.
    3. Na końcu nazwy, wcięcia, komentarze i zrzut ekranu. Zrzut z działającej, nawet niepełnej aplikacji jest lepszy niż brak zrzutu.

## Zadanie główne (25 min)

!!! note "Polecenie (styl arkusza INF.04)"
    Wykonaj aplikację mobilną obliczającą koszt przejazdu samochodem. Projekt nazwij `KosztPrzejazdu`. Uruchom aplikację w emulatorze systemu Android.

```text
Rysunek 1. Stan początkowy aplikacji

+---------------------------------------+
|          Koszt przejazdu              |  <- pasek tytułu, tło #4527A0
+---------------------------------------+
|  Dystans [km]                         |
|  [__________________________]         |
|  Średnie spalanie [l/100 km]          |
|  [__________________________]         |
|  Cena paliwa [zł/l]                   |
|  [__________________________]         |
|  Liczba osób                          |
|  [__________________________]         |
|                                       |
|  [             OBLICZ              ]  |  <- tło #FF9800
|                                       |
|  Zużycie paliwa: 0,00 l               |
|  Koszt przejazdu: 0,00 zł             |
|  Koszt na osobę: 0,00 zł              |
|                                       |
|  Autor: Imię Nazwisko                 |  <- na dole, 12, kursywa
+---------------------------------------+
```

**Opis wyglądu i działania aplikacji**

1. Napis **Koszt przejazdu** na pasku u góry: tło `#4527A0`, tekst biały, rozmiar `24`, wyśrodkowany, odstęp wewnętrzny `15`.
2. Cztery etykiety z polami edycyjnymi jak na rysunku. Pola mają nazwy `entDystans`, `entSpalanie`, `entCena`, `entOsoby` i klawiaturę numeryczną.
3. Przycisk **OBLICZ** rozciągnięty na całą szerokość (z marginesem `20` po bokach), tło `#FF9800`, tekst biały, pogrubiony.
4. Po kliknięciu przycisku aplikacja oblicza:
    - zużycie paliwa = dystans × spalanie / 100,
    - koszt przejazdu = zużycie × cena paliwa,
    - koszt na osobę = koszt przejazdu / liczba osób.
5. Wyniki wypisuje w trzech etykietach z dokładnością do dwóch miejsc po przecinku.
6. Jeśli którekolwiek pole jest puste lub nie zawiera liczby, albo dystans, spalanie, cena lub liczba osób jest mniejsza lub równa 0, w miejscu pierwszego wyniku pojawia się napis **Uzupełnij poprawnie wszystkie pola** w kolorze `#D32F2F`, a pozostałe wyniki są puste. Aplikacja nie może zakończyć działania z błędem.
7. Na dole napis **Autor:** i Twoje imię i nazwisko, rozmiar `12`, kursywa.

**Założenia aplikacji**

- interfejs zapisany w języku XAML,
- układ liniowy (`VerticalStackLayout`) lub siatka (`Grid`), elementy nie nachodzą na siebie,
- kolory `#4527A0`, `#FF9800`, `#D32F2F` zdefiniowane jako zasoby strony i użyte przez `StaticResource`,
- liczby dziesiętne można wpisać z przecinkiem lub z kropką,
- liczba osób jest liczbą całkowitą,
- działanie przycisku obsłużone zdarzeniem `Clicked`, kod czytelny, nazwy znaczące.

**Dane testowe**

| Dystans | Spalanie | Cena | Osoby | Zużycie | Koszt | Na osobę |
|---|---|---|---|---|---|---|
| 250 | 6,5 | 6,20 | 1 | 16,25 l | 100,75 zł | 100,75 zł |
| 120 | 5 | 6.50 | 2 | 6,00 l | 39,00 zł | 19,50 zł |
| 480 | 7,2 | 6,05 | 3 | 34,56 l | 209,09 zł | 69,70 zł |
| 36 | 5.8 | 6,39 | 4 | 2,09 l | 13,34 zł | 3,34 zł |
| (puste) | 6 | 6 | 1 | Uzupełnij poprawnie wszystkie pola | | |
| 100 | 6 | 6 | 0 | Uzupełnij poprawnie wszystkie pola | | |

Separator dziesiętny w wynikach (przecinek lub kropka) zależy od języka systemu urządzenia.

Po zakończeniu wykonaj zrzut ekranu `mobilna.jpg` z wynikiem dla danych z trzeciego wiersza tabeli (cały ekran, widoczny pasek zadań i Visual Studio pod emulatorem).

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Dodaj przełącznik (`Switch`) **Podróż w obie strony**. Gdy jest włączony, dystans jest liczony podwójnie. Wyniki przeliczaj automatycznie przy każdej zmianie pola (`TextChanged` wszystkich pól wywołuje tę samą metodę obliczającą).

## Czy potrafię…?

- [ ] odczytać arkusz egzaminacyjny i ustalić kolejność pracy
- [ ] wykonać wygląd aplikacji zgodnie z rysunkiem i opisem
- [ ] obsłużyć błędne dane bez zamknięcia aplikacji
- [ ] sprawdzić aplikację na danych testowych z tabeli
