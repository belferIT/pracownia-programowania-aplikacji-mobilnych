# Lekcja 3. Emulator Androida i dokumentowanie uruchomienia

<p class="lekcja-meta">Dział: Start · 45 min · Efekty: INF.04.6 (1), (2), INF.04.8 (2) · <span class="zakres zakres-p">INF.04</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- utworzyć i uruchomić emulator Androida,
- uruchomić aplikację MAUI w emulatorze,
- korzystać z przeładowywania na gorąco (Hot Reload) i listy błędów,
- wykonać zrzuty ekranu wymagane na egzaminie INF.04.

## Wprowadzenie

### Emulator

**Android Device Manager** (menu **Narzędzia → Android**) tworzy wirtualne urządzenia. Każde ma model ekranu i wersję systemu (poziom API).

| Wersja Androida | Poziom API |
|---|---|
| Android 13 | 33 |
| Android 14 | 34 |
| Android 15 | 35 |
| Android 16 | 36 |

!!! warning "Pierwsze uruchomienie trwa długo"
    Pierwsza kompilacja dla Androida i pierwszy start emulatora mogą trwać kilka minut. **Nie zamykaj emulatora** między uruchomieniami. Visual Studio wgra nową wersję aplikacji do działającego emulatora.

### Hot Reload

Gdy aplikacja działa w trybie debugowania (++f5++), zmiany w XAML widzisz od razu, bez ponownego uruchamiania (**XAML Hot Reload**). Zmiany w C# zatwierdzasz przyciskiem z płomieniem 🔥 (**.NET Hot Reload**) albo skrótem ++alt+f10++. Niektóre zmiany (np. nowe pola klasy) wymagają ponownego uruchomienia.

### Zrzuty ekranu na egzaminie

Na egzaminie INF.04 dokumentujesz uruchomienie każdej aplikacji zrzutem ekranu:

- zrzut obejmuje **cały ekran z widocznym paskiem zadań**,
- jeśli aplikacja działa: widać okno aplikacji (emulator) i pod spodem środowisko z projektem,
- jeśli aplikacja się nie kompiluje: widać **Listę błędów** i otwarte środowisko,
- dokument `egzamin` zawiera podpisane zrzuty i informacje: system operacyjny, środowiska, języki programowania, nazwę emulowanego urządzenia.

!!! tip "Skróty"
    ++win+print-screen++ zapisuje zrzut całego ekranu w folderze **Obrazy → Zrzuty ekranu**. ++print-screen++ kopiuje zrzut do schowka. ++win+shift+s++ to narzędzie Wycinanie (na egzaminie nie kadruj zrzutu!).

## Zadanie główne (25 min)

1. Otwórz **Android Device Manager** i utwórz emulator: urządzenie **Pixel 7**, system **Android 15 (API 35)** lub nowszy, procesor **x86_64**. Jeśli emulator już istnieje, użyj go.
2. Otwórz projekt `PierwszaAplikacja` z lekcji 2. Na pasku narzędzi wybierz jako cel utworzony emulator i uruchom aplikację (++f5++).
3. Gdy aplikacja działa, zmień w `MainPage.xaml` rozmiar czcionki etykiety: `FontSize="28"` i zapisz plik. Obserwuj emulator (Hot Reload).
4. Wykonaj zrzut całego ekranu (emulator z aplikacją i Visual Studio pod spodem). Zapisz go jako `C:\Projekty\Nazwisko_Imie\dokumentacja\mobilna.jpg` (utwórz folder `dokumentacja`).
5. Zatrzymaj aplikację (++shift+f5++). W `MainPage.xaml.cs` celowo usuń średnik na końcu dowolnej instrukcji. Skompiluj projekt (++ctrl+shift+b++).
6. Otwórz **Widok → Lista błędów**. Wykonaj zrzut całego ekranu z widoczną listą błędów i zapisz jako `dokumentacja\bledy.jpg`. Popraw błąd.
7. W edytorze tekstu utwórz plik `dokumentacja\egzamin` (format .docx lub .odt) i wpisz:
    - nazwę systemu operacyjnego,
    - nazwę środowiska programistycznego,
    - język programowania (C# i XAML),
    - nazwę emulowanego urządzenia (np. `Pixel 7 – API 35`),
    - oba zrzuty z podpisami **Rysunek 1. Uruchomienie aplikacji w emulatorze** i **Rysunek 2. Lista błędów kompilacji**.

??? question "Podpowiedź: emulator się nie uruchamia"
    Sprawdź w oknie **Dane wyjściowe** komunikat. Najczęstsze przyczyny: brak wirtualizacji, za mało pamięci RAM (zamknij przeglądarkę), uszkodzony obraz systemu (usuń emulator i utwórz nowy). Zgłoś problem nauczycielowi, a w tym czasie pracuj na **Windows Machine**.

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Utwórz drugi emulator z tabletem (np. **Pixel Tablet**) i uruchom na nim tę samą aplikację. Obróć emulator do orientacji poziomej (przycisk obrotu na pasku emulatora). Opisz w dokumencie, czym różni się wygląd aplikacji.

## Czy potrafię…?

- [ ] utworzyć emulator w Android Device Manager
- [ ] uruchomić aplikację MAUI w emulatorze
- [ ] skorzystać z Hot Reload po zmianie XAML
- [ ] wykonać zrzut ekranu zgodny z wymaganiami egzaminu
- [ ] wpisać do dokumentacji nazwę emulowanego urządzenia
