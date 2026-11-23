# Lekcja 36. Baza SQLite, cz. 1: model i dodawanie rekordów

<p class="lekcja-meta">Dział: Dane, sieć i usługi urządzenia · 45 min · Efekty: INF.04.6 (2) kryt. 9, INF.04.3 (6) kryt. 8 · <span class="zakres zakres-p">INF.04</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- dodać do projektu bibliotekę SQLite,
- opisać tabelę klasą C# z atrybutami,
- utworzyć bazę i tabelę, dodać rekordy i odczytać je.

## Wprowadzenie

**SQLite** to baza danych zapisana w jednym pliku na urządzeniu. Nie wymaga serwera. W MAUI używamy pakietu **sqlite-net-pcl**, który mapuje klasy C# na tabele (ORM).

### Instalacja

Zainstaluj z NuGet dwa pakiety (najnowsze stabilne wersje):

- `sqlite-net-pcl`
- `SQLitePCLRaw.bundle_green`

### Model

```csharp
using SQLite;

[Table("ksiazki")]
public class Ksiazka
{
    [PrimaryKey, AutoIncrement]
    public int Id { get; set; }

    [MaxLength(100), NotNull]
    public string Tytul { get; set; } = "";

    public string Autor { get; set; } = "";
    public int Rok { get; set; }
    public bool Przeczytana { get; set; }
}
```

### Klasa obsługująca bazę

```csharp
using SQLite;

public class BazaDanych
{
    private SQLiteAsyncConnection? polaczenie;

    private async Task InicjujAsync()
    {
        if (polaczenie != null) return;
        string sciezka = Path.Combine(FileSystem.AppDataDirectory, "biblioteczka.db3");
        polaczenie = new SQLiteAsyncConnection(sciezka);
        await polaczenie.CreateTableAsync<Ksiazka>();        // tworzy tabelę, jeśli jej nie ma
    }

    public async Task<int> DodajAsync(Ksiazka k)
    {
        await InicjujAsync();
        return await polaczenie!.InsertAsync(k);              // po wstawieniu k.Id ma nadany numer
    }

    public async Task<List<Ksiazka>> PobierzWszystkieAsync()
    {
        await InicjujAsync();
        return await polaczenie!.Table<Ksiazka>().OrderBy(k => k.Tytul).ToListAsync();
    }
}
```

| Atrybut | SQL |
|---|---|
| `[Table("ksiazki")]` | nazwa tabeli |
| `[PrimaryKey, AutoIncrement]` | `INTEGER PRIMARY KEY AUTOINCREMENT` |
| `[MaxLength(100)]` | `varchar(100)` |
| `[NotNull]` | `NOT NULL` |
| `[Ignore]` | właściwość nie trafia do tabeli |

!!! info "Związek z INF.03"
    To ta sama baza i ten sam SQL, który znasz z przedmiotu o bazach danych. sqlite-net-pcl generuje SQL za Ciebie, ale możesz też pisać zapytania: `await polaczenie.QueryAsync<Ksiazka>("SELECT * FROM ksiazki WHERE Rok > ?", 1900);`.

## Zadanie główne (25 min)

Utwórz projekt `Biblioteczka`.

1. Zainstaluj pakiety, dodaj klasy `Ksiazka` i `BazaDanych` z przykładu.
2. W `MainPage` utwórz pole `private readonly BazaDanych baza = new();`.
3. Formularz: **Tytuł**, **Autor**, **Rok wydania** (klawiatura numeryczna), `CheckBox` **Przeczytana**, przycisk **Dodaj**.
4. Po kliknięciu **Dodaj**: sprawdź, czy tytuł nie jest pusty, a rok jest liczbą z zakresu 1450–2030. Jeśli tak, dodaj książkę do bazy, wyczyść formularz i odśwież listę. W przeciwnym razie wyświetl komunikat z błędem.
5. Lista `CollectionView` pod formularzem: tytuł (pogrubiony), autor i rok (**Bolesław Prus, 1890**), znak ✔ przy przeczytanych.
6. Lista wczytuje się w `OnAppearing`.
7. Dodaj 4 książki, zamknij aplikację i uruchom ponownie – dane zostały w bazie.

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Otwórz plik bazy w programie **DB Browser for SQLite**. Na Windows ścieżkę znajdziesz, wypisując `FileSystem.AppDataDirectory`. W emulatorze plik pobierzesz przez **Widok → Inne okna → Device File Explorer** (lub `adb pull`). Sprawdź, jaki SQL utworzył tabelę (zakładka *Database Structure*).

## Czy potrafię…?

- [ ] zainstalować pakiety SQLite w projekcie MAUI
- [ ] opisać tabelę klasą z atrybutami
- [ ] utworzyć połączenie i tabelę tylko raz
- [ ] dodać rekord i odczytać wszystkie rekordy
