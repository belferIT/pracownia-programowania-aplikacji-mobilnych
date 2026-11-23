# Lekcja 52. Scenariusze testów i raport błędów

<p class="lekcja-meta">Dział: Jakość, testy i publikacja · 45 min · Efekty: INF.04.8 (3) kryt. 7, 10, 11, 12 · <span class="zakres zakres-p">INF.04</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- napisać scenariusz testu i przypadki testowe dla aplikacji mobilnej,
- przeprowadzić test ręczny i zapisać wynik,
- zgłosić błąd w raporcie tak, aby inna osoba mogła go powtórzyć,
- sprawdzić interfejs na różnych urządzeniach i w różnych ustawieniach.

## Wprowadzenie

Testy jednostkowe sprawdzają kod. **Testy ręczne** (funkcjonalne) sprawdzają aplikację tak, jak używa jej człowiek. Na egzaminie INF.04 część zadania może polegać na przygotowaniu dokumentacji testów.

**Przypadek testowy** zapisujesz w tabeli:

| ID | Warunki wstępne | Kroki | Dane | Oczekiwany wynik | Wynik rzeczywisty | Status |
|---|---|---|---|---|---|---|
| T01 | aplikacja uruchomiona, lista pusta | 1. wpisz klienta 2. wybierz rower 3. ustaw godziny 4. dotknij **WYPOŻYCZ** | Jan Kowalski, górski, 3 h, kask | na liście: Jan Kowalski, górski, 3 h, 50,00 zł | jak oczekiwano | ✅ zaliczony |
| T02 | aplikacja uruchomiona | dotknij **WYPOŻYCZ** bez wpisania klienta | – | komunikat **Uzupełnij dane wypożyczenia** | aplikacja się zamyka | ❌ błąd B01 |

Gdy test nie przechodzi, piszesz **raport błędu**:

| Pole | Przykład |
|---|---|
| ID i tytuł | B01: zamknięcie aplikacji po dotknięciu WYPOŻYCZ bez klienta |
| Środowisko | emulator Pixel 7, Android 15, wersja aplikacji 1.0 |
| Kroki do powtórzenia | 1. uruchom aplikację 2. nie wpisuj klienta 3. dotknij **WYPOŻYCZ** |
| Oczekiwany wynik | komunikat **Uzupełnij dane wypożyczenia** |
| Rzeczywisty wynik | aplikacja się zamyka |
| Priorytet | wysoki (utrata danych, awaria) / średni / niski (wygląd) |
| Załącznik | zrzut ekranu `B01.png` |

!!! tip "Co testować oprócz „szczęśliwej ścieżki”"
    - puste pola, same spacje, bardzo długi tekst, litery w polu liczbowym,
    - wartości graniczne (0, minimum, maksimum, minimum − 1),
    - ponowne uruchomienie aplikacji (czy dane zostały zapisane?),
    - obrót ekranu, tryb ciemny, powiększona czcionka systemowa,
    - brak internetu (tryb samolotowy w emulatorze), jeśli aplikacja korzysta z sieci.

!!! info "Testy na różnych urządzeniach"
    W **Android Device Manager** utwórz drugi emulator: mały telefon (np. 5″) albo tablet. Uruchom na nim aplikację i na Windows. Sprawdź, czy elementy nie nachodzą na siebie i czy tekst się mieści. Czcionkę systemową zmienisz w emulatorze: **Ustawienia → Wyświetlacz → Rozmiar czcionki**.

## Zadanie główne (25 min)

Pracujesz w parach. Testujesz aplikację kolegi lub koleżanki ze sprawdzianu (lekcja 47, **Dwa Kółka**) albo z lekcji 38 (**Dziennik treningów**). Dokument `testy` przygotuj w edytorze tekstu.

1. Przeczytaj jeszcze raz polecenie zadania. To jest specyfikacja: z niej bierzesz oczekiwane wyniki, a nie z działania aplikacji.
2. Napisz co najmniej **8 przypadków testowych** w tabeli jak we wprowadzeniu, w tym:
    - 3 testy poprawnych danych (z tabeli danych testowych w poleceniu),
    - 3 testy błędnych lub granicznych danych,
    - 1 test zapisu danych po ponownym uruchomieniu,
    - 1 test interfejsu: obrót ekranu albo inne urządzenie.
3. Wykonaj testy i uzupełnij kolumny **Wynik rzeczywisty** i **Status**.
4. Dla każdego niezaliczonego testu napisz raport błędu ze zrzutem ekranu.
5. Na koniec dokumentu dopisz podsumowanie: liczba testów, zaliczone, niezaliczone. Oddaj dokument autorowi aplikacji.

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Popraw błędy zgłoszone w Twojej aplikacji. Przy każdym błędzie dopisz w raporcie kolumnę **Poprawka** (co zmieniłeś) i powtórz test. Ponowne wykonanie testów po poprawkach to **test regresji**.

## Czy potrafię…?

- [ ] napisać przypadek testowy z warunkami wstępnymi, krokami i oczekiwanym wynikiem
- [ ] dobrać testy poprawnych, błędnych i granicznych danych
- [ ] napisać raport błędu, który pozwala powtórzyć błąd
- [ ] sprawdzić aplikację na innym urządzeniu i po obróceniu ekranu
