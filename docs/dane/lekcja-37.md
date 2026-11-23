# Lekcja 37. Baza SQLite, cz. 2: wyszukiwanie, edycja, usuwanie

<p class="lekcja-meta">Dział: Dane, sieć i usługi urządzenia · 45 min · Efekty: INF.04.6 (2) kryt. 9 · <span class="zakres zakres-p">INF.04</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- wyszukać rekordy spełniające warunek,
- zmienić i usunąć rekord,
- przejść z listy do strony edycji rekordu (CRUD).

## Wprowadzenie

**CRUD** to cztery podstawowe operacje na danych:

| Operacja | SQL | sqlite-net-pcl |
|---|---|---|
| **C**reate | `INSERT` | `InsertAsync(obiekt)` |
| **R**ead | `SELECT` | `Table<T>().ToListAsync()`, `GetAsync<T>(id)`, `FindAsync<T>(id)` |
| **U**pdate | `UPDATE` | `UpdateAsync(obiekt)` – po kluczu głównym |
| **D**elete | `DELETE` | `DeleteAsync(obiekt)` lub `DeleteAsync<T>(id)` |

```csharp
public async Task<List<Ksiazka>> SzukajAsync(string fraza)
{
    await InicjujAsync();
    return await polaczenie!.Table<Ksiazka>()
        .Where(k => k.Tytul.Contains(fraza) || k.Autor.Contains(fraza))
        .OrderBy(k => k.Tytul)
        .ToListAsync();
}

public async Task<int> ZapiszAsync(Ksiazka k)
{
    await InicjujAsync();
    return k.Id == 0
        ? await polaczenie!.InsertAsync(k)    // nowa książka
        : await polaczenie!.UpdateAsync(k);   // istniejąca
}

public async Task<int> UsunAsync(Ksiazka k)
{
    await InicjujAsync();
    return await polaczenie!.DeleteAsync(k);
}

public async Task<int> LiczbaPrzeczytanychAsync()
{
    await InicjujAsync();
    return await polaczenie!.Table<Ksiazka>().CountAsync(k => k.Przeczytana);
}
```

!!! info "Jedna baza dla całej aplikacji"
    Jeśli kilka stron korzysta z bazy, utwórz **jeden** obiekt `BazaDanych` i przekazuj go stronom (np. przez konstruktor) albo zrób z niego pole statyczne w klasie `App`. Każde nowe połączenie to strata czasu.

!!! tip "Wzorzec: ta sama strona do dodawania i edycji"
    Strona `KsiazkaPage` przyjmuje obiekt `Ksiazka`. Dla nowej książki przekazujesz `new Ksiazka()` (Id = 0), dla edycji – wybraną z listy. Metoda `ZapiszAsync` sama wybiera `Insert` lub `Update`.

## Zadanie główne (25 min)

Rozbuduj projekt `Biblioteczka` z lekcji 36.

1. Przenieś formularz na nową stronę `KsiazkaPage` (tytuł strony **Nowa książka** albo **Edycja**). Strona przyjmuje w konstruktorze bazę i obiekt `Ksiazka`, pola są z nim powiązane (`BindingContext`, `Mode=TwoWay`).
2. Na stronie głównej: `ToolbarItem` **Dodaj** otwiera `KsiazkaPage` z nową książką.
3. Wybranie książki na liście otwiera `KsiazkaPage` z tą książką do edycji.
4. `KsiazkaPage` ma przyciski **Zapisz** (`ZapiszAsync` + powrót) i **Usuń** (widoczny tylko dla istniejącej książki, z potwierdzeniem).
5. Na stronie głównej `SearchBar` nad listą – wyszukiwanie po tytule i autorze przy każdej zmianie tekstu.
6. Pod listą etykieta **Przeczytane: X z Y**.
7. Dodaj przykładowe dane: *Lalka* (Bolesław Prus, 1890), *Quo vadis* (Henryk Sienkiewicz, 1896), *Solaris* (Stanisław Lem, 1961), *Cyberiada* (Stanisław Lem, 1965). Wyszukaj „Lem” – widać 2 książki.

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Dodaj drugą tabelę `Wypozyczenie` (`Id`, `KsiazkaId`, `Komu`, `DataWypozyczenia`, `Zwrocona`) i na stronie książki listę jej wypożyczeń (zapytanie z warunkiem `KsiazkaId == ksiazka.Id`). To relacja jeden do wielu, znana z baz danych.

## Czy potrafię…?

- [ ] wymienić operacje CRUD i odpowiadające im metody
- [ ] wyszukać rekordy warunkiem `Where`
- [ ] zaktualizować i usunąć rekord
- [ ] użyć jednej strony do dodawania i edycji
