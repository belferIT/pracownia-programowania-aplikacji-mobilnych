# Lekcje 57–60. Symulacja egzaminu INF.04

<p class="lekcja-meta">Dział: Podsumowanie · 4 × 45 min (180 min) · Efekty: INF.04.4 (2), INF.04.6 (2), INF.04.8 (2) · <span class="zakres zakres-p">INF.04</span></p>

## Zasady

- Czas: **180 minut**, jak na egzaminie. Pracujesz samodzielnie, w kolejności zadań, którą sam wybierzesz.
- Możesz korzystać z [dokumentacji .NET](https://learn.microsoft.com/pl-pl/dotnet/) i [dokumentacji .NET MAUI](https://learn.microsoft.com/pl-pl/dotnet/maui/). Nie możesz korzystać z narzędzi AI, materiałów z lekcji, własnych projektów ani pomocy innych osób.
- Na pulpicie utwórz folder `Nazwisko_Imie` z podfolderami `konsola`, `mobilna` i `dokumentacja`. Do nich zapisujesz projekty i zrzuty ekranu. Po zakończeniu pracy nie zmieniaj plików.
- W polu **autor** komentarzy wpisz numer z dziennika poprzedzony literą klasy, np. `4A07` (na egzaminie: dane z arkusza).

!!! tip "Plan czasu"
    | Minuty | Zadanie |
    |---|---|
    | 0–10 | przeczytaj cały arkusz, utwórz foldery, uruchom emulator (start trwa kilka minut) |
    | 10–55 | aplikacja konsolowa, testy, zrzut `konsola.jpg` |
    | 55–155 | aplikacja mobilna, zrzuty `mobilna1.jpg` i `mobilna2.jpg` |
    | 155–175 | dokumentacja, sprawdzenie nazw plików i folderów |
    | 175–180 | rezerwa |

## Materiały

Pobierz i rozpakuj [wycieczki.zip](../pliki/lekcja-57/wycieczki.zip){ download }: `gory.jpg`, `morze.jpg`, `las.jpg`, `miasto.jpg`.

## Zadanie 1. Aplikacja konsolowa

!!! note "Polecenie"
    Wykonaj aplikację konsolową w C#, która szyfruje i odszyfrowuje tekst **szyfrem Cezara**. Projekt nazwij `Szyfr` i zapisz w folderze `konsola`.

Szyfr Cezara zastępuje każdą literę literą przesuniętą w alfabecie o **klucz** pozycji. Alfabet jest „zawinięty”: po `z` jest znowu `a`. Ujemny klucz przesuwa litery w lewo, czyli odszyfrowuje tekst.

**Założenia**

1. Funkcja `Szyfruj` przyjmuje tekst (`string`) i klucz (`int`), zwraca zaszyfrowany tekst. Funkcja nie wypisuje niczego na ekran.
2. Przesuwane są tylko litery alfabetu łacińskiego `a–z` i `A–Z`, z zachowaniem wielkości liter. Pozostałe znaki (spacje, cyfry, polskie litery, znaki interpunkcyjne) zostają bez zmian.
3. Klucz może być dowolną liczbą całkowitą, także większą od 26 lub ujemną.
4. Program główny pyta o tekst i klucz, wywołuje funkcję i wypisuje wynik w postaci `Wynik: …`. Gdy klucz nie jest liczbą całkowitą, wypisuje `Niepoprawny klucz` i kończy działanie.
5. Funkcję należy napisać samodzielnie, bez gotowych bibliotek szyfrujących.

```text
Rysunek 1. Przykładowe działanie programu

Podaj tekst: ala ma kota
Podaj klucz: 3
Wynik: dod pd nrwd
```

| Tekst | Klucz | Wynik |
|---|---|---|
| `abc` | 3 | `def` |
| `xyz` | 3 | `abc` |
| `egzamin inf04` | 5 | `jlefrns nsk04` |
| `zawodowy` | −1 | `yzvncnvx` |
| `ala ma kota` | 27 | `bmb nb lpub` |
| `dmd pd nrwd` | −3 | `aja ma kota` |
| `Kot` | 1 | `Lpu` |

Wykonaj zrzut `konsola.jpg` z działaniem programu dla danych z wiersza `egzamin inf04`, klucz 5.

??? question "Podpowiedź: reszta z dzielenia liczby ujemnej"
    W C# `-1 % 26` daje `-1`, a nie `25`. Bezpieczny wzór na przesunięcie: `((pozycja + klucz) % 26 + 26) % 26`.

## Zadanie 2. Aplikacja mobilna

!!! note "Polecenie"
    Wykonaj aplikację mobilną biura podróży **Horyzont** do rezerwacji wycieczek. Projekt nazwij `Horyzont` i zapisz w folderze `mobilna`. Uruchom aplikację w emulatorze Androida.

```text
Rysunek 2. Aplikacja po wybraniu wycieczki

+---------------------------------------+
|  Biuro podróży Horyzont               |  <- kolor 1, tekst biały, 24
+---------------------------------------+
|  Imię i nazwisko: [ Jan Kowalski  ]   |
|  ( ) Tatry       (o) Bałtyk           |
|  ( ) Bieszczady  ( ) Kraków           |
|  +---------------------------------+  |
|  |        [ obraz morze.jpg ]      |  |  <- wysokość 160
|  +---------------------------------+  |
|  Cena za osobę: 900 zł                |
|  Termin wyjazdu: [ 12.07.2027 ]       |
|  Liczba osób: 4             [ - | + ] |
|  [x] Ubezpieczenie (49 zł/os.)        |
|  Do zapłaty: 3436,00 zł               |  <- pogrubiony, 20
|  [            REZERWUJ              ] |  <- kolor 2
+---------------------------------------+
```

| Element | Grupa A | Grupa B |
|---|---|---|
| kolor 1 (pasek) | `#00838F` | `#AD1457` |
| kolor 2 (przycisk) | `#FF7043` | `#5C6BC0` |

**Opis wyglądu i działania aplikacji**

1. Interfejs w XAML, układ pionowy bez nachodzenia elementów. Pasek z napisem **Biuro podróży Horyzont**: tło kolor 1, tekst biały, rozmiar `24`.
2. Pole tekstowe `Entry` z podpowiedzią **imię i nazwisko**.
3. Cztery przyciski opcji (`RadioButton`) w układzie 2 × 2. Na starcie żaden nie jest wybrany, obraz jest ukryty, a etykieta ceny ma tekst **Wybierz wycieczkę**.
4. Po wybraniu wycieczki widoczny jest jej obraz (`Aspect="AspectFill"`, wysokość `160`, zaokrąglone rogi `Border`) i cena za osobę:

    | Wycieczka | Obraz | Cena za osobę |
    |---|---|---|
    | Tatry | `gory.jpg` | 1200 zł |
    | Bałtyk | `morze.jpg` | 900 zł |
    | Bieszczady | `las.jpg` | 750 zł |
    | Kraków | `miasto.jpg` | 600 zł |

5. `DatePicker` z terminem wyjazdu: domyślnie dzień za tydzień, nie można wybrać daty wcześniejszej niż jutro.
6. `Stepper` liczby osób 1–10 (start 1) z etykietą **Liczba osób: N**, `CheckBox` **Ubezpieczenie (49 zł/os.)**.
7. Kwota **Do zapłaty** jest przeliczana przy każdej zmianie wycieczki, liczby osób i ubezpieczenia: cena za osobę × liczba osób; dla **4 i więcej osób** rabat **10%** od ceny wycieczki; ubezpieczenie 49 zł za osobę bez rabatu. Format: dwa miejsca po przecinku i **zł**.
8. Przycisk **REZERWUJ** (tło kolor 2, tekst biały):
    - gdy pole imienia jest puste albo nie wybrano wycieczki – komunikat (`DisplayAlert`) o tytule **Błąd** i treści **Uzupełnij imię i nazwisko oraz wybierz wycieczkę**,
    - w przeciwnym razie komunikat o tytule **Rezerwacja przyjęta** i treści w postaci: **Jan Kowalski, Bałtyk, 12.07.2027, 4 os., do zapłaty 3436,00 zł**.

| Wycieczka | Osoby | Ubezpieczenie | Do zapłaty |
|---|---|---|---|
| Tatry | 2 | nie | 2400,00 zł |
| Bałtyk | 4 | tak | 3436,00 zł |
| Bieszczady | 1 | tak | 799,00 zł |
| Kraków | 5 | nie | 2700,00 zł |
| Tatry | 3 | tak | 3747,00 zł |
| Bieszczady | 6 | tak | 4344,00 zł |

**Założenia aplikacji**

- obrazy w zasobach aplikacji (`Resources/Images`),
- nazwy kontrolek znaczące, np. `entImie`, `rbTatry`, `imgWycieczka`, `stpOsoby`, `chkUbezpieczenie`, `lblKwota`,
- obliczenie kwoty w osobnej metodzie `ObliczKwote` (parametry: cena za osobę, liczba osób, ubezpieczenie; zwraca `decimal`),
- kod czytelny, z wcięciami.

Wykonaj zrzuty ekranu (cały ekran z emulatorem i paskiem zadań):

- `mobilna1.jpg` – aplikacja dla danych z drugiego wiersza tabeli (Bałtyk, 4 osoby, ubezpieczenie),
- `mobilna2.jpg` – komunikat **Rezerwacja przyjęta** dla tych samych danych.

## Zadanie 3. Dokumentacja

1. W aplikacji konsolowej przed funkcją `Szyfruj`, a w aplikacji mobilnej przed metodą `ObliczKwote` wstaw komentarz nagłówkowy według wzoru:

    ```csharp
    /********************************************************
     * nazwa funkcji: <tu wstaw nazwę funkcji>
     * opis funkcji: <tu wstaw opis działania funkcji>
     * parametry: <tu wstaw nazwę parametru> - <tu wstaw opis parametru>
     * zwracany typ i opis: <tu wstaw typ zwracany oraz opis>
     * autor: <tu wstaw numer zdającego>
     ********************************************************/
    ```

2. W folderze `dokumentacja` utwórz plik `testy` (edytor tekstu) z tabelą trzech przypadków testowych aplikacji mobilnej (dane, oczekiwany wynik, wynik rzeczywisty), w tym jednym dla błędnych danych, oraz z nazwą systemu operacyjnego, środowiska programistycznego i wersji emulatora Androida.
3. Przenieś zrzuty `konsola.jpg`, `mobilna1.jpg`, `mobilna2.jpg` do folderu `dokumentacja`.

## Kryteria oceny (40 pkt)

| Kryterium | Punkty |
|---|---|
| **Aplikacja konsolowa** | **12** |
| funkcja `Szyfruj` z parametrami i wartością zwracaną, bez wypisywania | 2 |
| przesuwanie małych liter z zawijaniem `z → a` | 3 |
| wielkie litery, inne znaki bez zmian | 2 |
| klucze ujemne i większe od 26 | 2 |
| program główny: wczytanie, sprawdzenie klucza, wypisanie wyniku | 2 |
| zrzut `konsola.jpg` zgodny z poleceniem | 1 |
| **Aplikacja mobilna** | **20** |
| projekt uruchamia się w emulatorze, interfejs w XAML zgodny z rysunkiem, kolory grupy | 4 |
| `RadioButton`: brak wyboru na starcie, obraz ukryty, zmiana obrazu i ceny | 4 |
| `DatePicker` z domyślną i minimalną datą | 2 |
| `Stepper`, `CheckBox`, kwota przeliczana na bieżąco | 3 |
| obliczenia w metodzie `ObliczKwote`, rabat 10% od 4 osób tylko na wycieczkę | 4 |
| przycisk **REZERWUJ**: walidacja i komunikat z danymi rezerwacji | 3 |
| **Dokumentacja** | **8** |
| komentarze nagłówkowe zgodne ze wzorem (2 × 2 pkt) | 4 |
| plik `testy`: trzy przypadki testowe i opis środowiska | 2 |
| zrzuty `mobilna1.jpg` i `mobilna2.jpg` zgodne z poleceniem | 2 |

!!! info "Jak liczy się wynik na egzaminie"
    Część praktyczną egzaminu zdajesz, gdy uzyskasz co najmniej **75%** punktów. Na tej symulacji próg zaliczenia to **30 z 40 pkt**. Ocenę szkolną ustala nauczyciel zgodnie z WSO.

## Po symulacji

Po sprawdzeniu prac nauczyciel omówi rozwiązania. Zapisz, które kryteria straciłeś i dlaczego (brak czasu, nieznajomość kontrolki, błąd w obliczeniach, zła nazwa pliku). To Twoja lista do powtórki przed egzaminem.
