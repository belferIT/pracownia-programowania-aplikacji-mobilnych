# Lekcja 35. Pliki i JSON

<p class="lekcja-meta">Dział: Dane, sieć i usługi urządzenia · 45 min · Efekty: INF.04.6 (2) kryt. 3 · <span class="zakres zakres-p">INF.04</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- wskazać folder, w którym aplikacja może zapisywać pliki,
- zapisać i odczytać plik tekstowy,
- zamienić listę obiektów na JSON i z powrotem (serializacja).

## Wprowadzenie

### Foldery aplikacji

| Właściwość | Zawartość |
|---|---|
| `FileSystem.AppDataDirectory` | trwałe dane aplikacji (usuwane razem z aplikacją) |
| `FileSystem.CacheDirectory` | dane tymczasowe; system może je usunąć |
| `FileSystem.OpenAppPackageFileAsync("plik")` | odczyt pliku dołączonego do aplikacji (`Resources/Raw`) |

```csharp
string sciezka = Path.Combine(FileSystem.AppDataDirectory, "notatki.json");

await File.WriteAllTextAsync(sciezka, tekst);
if (File.Exists(sciezka))
{
    string tekst = await File.ReadAllTextAsync(sciezka);
}
```

### JSON

JSON to tekstowy format danych. Biblioteka `System.Text.Json` zamienia obiekty C# na JSON (**serializacja**) i odwrotnie (**deserializacja**).

```csharp
using System.Text.Json;

public class Notatka
{
    public string Tytul { get; set; } = "";
    public string Tresc { get; set; } = "";
    public DateTime Data { get; set; }
}

var opcje = new JsonSerializerOptions { WriteIndented = true };
string json = JsonSerializer.Serialize(notatki, opcje);          // List<Notatka> → tekst

List<Notatka> wczytane = JsonSerializer.Deserialize<List<Notatka>>(json) ?? new();
```

```json
[
  {
    "Tytul": "Zakupy",
    "Tresc": "mleko, chleb",
    "Data": "2026-11-23T08:15:00"
  }
]
```

!!! warning "Uszkodzony plik"
    Jeśli plik ma błędny JSON, `Deserialize` wyrzuci `JsonException`. Odczyt umieść w `try`/`catch` i w razie błędu zacznij od pustej listy.

!!! tip "Gdzie jest plik?"
    Wypisz ścieżkę w etykiecie lub w oknie Output (`System.Diagnostics.Debug.WriteLine(sciezka);`). Na Windows możesz otworzyć plik w Notatniku i zobaczyć JSON.

## Zadanie główne (25 min)

Utwórz projekt `Notatnik`.

1. Klasa `Notatka` jak w przykładzie.
2. Strona: pole **Tytuł** (`Entry`), pole **Treść** (`Editor`, wysokość `120`), przycisk **Dodaj**, lista notatek (`CollectionView`: tytuł pogrubiony, data w formacie `dd.MM.yyyy HH:mm`, treść szarym kolorem, maksymalnie 2 wiersze: `MaxLines="2"`).
3. Dane w `ObservableCollection<Notatka>`. Po każdym dodaniu lub usunięciu notatki zapisz całą kolekcję do pliku `notatki.json` w `AppDataDirectory` (metoda `ZapiszAsync`).
4. W `OnAppearing` wczytaj notatki z pliku (metoda `WczytajAsync`). Brak pliku lub błąd odczytu – pusta lista.
5. Wybranie notatki pyta **Usunąć notatkę „Tytuł”?** i po potwierdzeniu ją usuwa.
6. Nie można dodać notatki bez tytułu.
7. Na dole etykieta ze ścieżką pliku (rozmiar `10`).
8. Sprawdź: dodaj 3 notatki, zamknij aplikację, uruchom ponownie – notatki są na liście.

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Dodaj przycisk **Eksportuj**, który udostępnia plik JSON innej aplikacji (np. poczcie) przez `await Share.Default.RequestAsync(new ShareFileRequest { Title = "Notatki", File = new ShareFile(sciezka) });`.

## Czy potrafię…?

- [ ] utworzyć ścieżkę pliku w folderze danych aplikacji
- [ ] zapisać i odczytać plik tekstowy asynchronicznie
- [ ] zserializować listę obiektów do JSON i wczytać ją z powrotem
- [ ] obsłużyć brak pliku i błędny JSON
