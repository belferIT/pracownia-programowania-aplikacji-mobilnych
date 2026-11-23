# Lekcja 38. Dziennik treningów. Zadanie w stylu egzaminu

<p class="lekcja-meta">Dział: Dane, sieć i usługi urządzenia · 45 min · Efekty: INF.04.6 (2) kryt. 3, 9 · <span class="zakres zakres-p">INF.04</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- wykonać aplikację mobilną z bazą danych według opisu w stylu arkusza INF.04,
- zaprojektować tabelę dla danych z zadania,
- połączyć bazę danych z preferencjami użytkownika.

## Wprowadzenie

!!! tip "Sprawdzone fragmenty"
    Zanim zaczniesz, otwórz projekt `Biblioteczka` z poprzednich lekcji. Klasę `BazaDanych` możesz skopiować i zmienić typ `Ksiazka` na nowy. Na egzaminie nie masz dostępu do swoich projektów – dlatego warto znać ten kod na pamięć.

| Element | Do zapamiętania |
|---|---|
| pakiety | `sqlite-net-pcl`, `SQLitePCLRaw.bundle_green` |
| ścieżka | `Path.Combine(FileSystem.AppDataDirectory, "plik.db3")` |
| połączenie | `new SQLiteAsyncConnection(sciezka)` + `CreateTableAsync<T>()` |
| klucz | `[PrimaryKey, AutoIncrement] public int Id { get; set; }` |

## Zadanie główne (25 min)

!!! note "Polecenie (styl arkusza INF.04)"
    Wykonaj aplikację mobilną **Dziennik treningów** przechowującą dane w bazie SQLite. Projekt nazwij `Treningi`. Uruchom aplikację w emulatorze.

```text
Rysunek 1. Aplikacja po dodaniu trzech treningów

+---------------------------------------+
|  Dziennik treningów — Ola             |  <- tło #1565C0, tekst biały
+---------------------------------------+
|  Data       [ 23.11.2026 ]            |
|  Rodzaj     [ bieganie         v ]    |
|  Czas [min] [ 30 ]                    |
|  [            DODAJ TRENING         ] |
+---------------------------------------+
| 23.11.2026 bieganie  30 min  300 kcal |
| 22.11.2026 rower     45 min  360 kcal |
| 20.11.2026 pływanie  20 min  180 kcal |
+---------------------------------------+
|  Razem: 95 min, 840 kcal              |
+---------------------------------------+
```

**Opis wyglądu i działania aplikacji**

1. Pasek u góry: **Dziennik treningów — Imię**, tło `#1565C0`, tekst biały. Imię jest pobierane z preferencji. Przy pierwszym uruchomieniu (brak imienia w preferencjach) aplikacja pyta o imię oknem `DisplayPromptAsync` i zapisuje je.
2. Formularz: `DatePicker` (format `dd.MM.yyyy`, najpóźniej dziś), `Picker` z rodzajami **bieganie**, **rower**, **pływanie**, pole czasu w minutach (tylko liczby), przycisk **DODAJ TRENING** (tło `#FF9800`).
3. Po kliknięciu przycisku: jeśli nie wybrano rodzaju albo czas nie jest liczbą całkowitą z przedziału 1–600 – komunikat **Uzupełnij poprawnie dane treningu**. W przeciwnym razie trening jest zapisywany w bazie, a formularz czyszczony (data zostaje).
4. Spalone kalorie: czas × współczynnik: bieganie **10** kcal/min, rower **8** kcal/min, pływanie **9** kcal/min. Kalorie są zapisywane w bazie razem z treningiem.
5. Lista treningów z bazy, posortowana od najnowszej daty: data, rodzaj, czas (**30 min**), kalorie (**300 kcal**).
6. Pod listą podsumowanie: **Razem: X min, Y kcal**.
7. Dotknięcie treningu na liście pyta **Usunąć trening?** i po potwierdzeniu usuwa go z bazy.

**Założenia aplikacji**

- klasa `Trening` (tabela `treningi`): identyfikator (klucz główny, autonumeracja), data, rodzaj (tekst), czas (liczba całkowita), kalorie (liczba całkowita),
- baza w pliku `treningi.db3` w folderze danych aplikacji, dostęp asynchroniczny,
- interfejs w XAML, elementy nie nachodzą na siebie, kod czytelny.

**Dane testowe**

| Data | Rodzaj | Czas | Kalorie |
|---|---|---|---|
| 20.11.2026 | pływanie | 20 | 180 |
| 22.11.2026 | rower | 45 | 360 |
| 23.11.2026 | bieganie | 30 | 300 |
| – | (brak) | 30 | komunikat |
| – | bieganie | 0 | komunikat |

Po dodaniu trzech pierwszych: **Razem: 95 min, 840 kcal**. Po zamknięciu i ponownym uruchomieniu aplikacji dane i imię są zachowane.

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Dodaj `Picker` filtra **Pokaż: wszystkie / bieganie / rower / pływanie**. Podsumowanie dotyczy tylko widocznych treningów. Filtrowanie wykonaj zapytaniem do bazy (`Where`), a nie na liście w pamięci.

## Czy potrafię…?

- [ ] zaprojektować klasę-tabelę dla danych z zadania
- [ ] zapisać w bazie wartość obliczoną
- [ ] posortować rekordy malejąco po dacie
- [ ] połączyć bazę danych z preferencjami
