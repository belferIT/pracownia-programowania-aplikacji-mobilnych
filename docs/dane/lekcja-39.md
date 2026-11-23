# Lekcja 39. Dane z internetu: HttpClient i JSON

<p class="lekcja-meta">Dział: Dane, sieć i usługi urządzenia · 45 min · Efekty: INF.04.6 (2) kryt. 8, INF.04.3 (6) kryt. 7 · <span class="zakres zakres-p">INF.04</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- wyjaśnić, jak działa aplikacja w architekturze klient–serwer,
- pobrać dane JSON z serwera klasą `HttpClient`,
- zamienić odpowiedź na listę obiektów i wyświetlić ją.

## Wprowadzenie

Aplikacja mobilna (klient) wysyła żądanie HTTP do serwera (API). Serwer odpowiada danymi, najczęściej w formacie JSON.

```text
+-----------------+   GET /pliki/api/ksiazki.json    +------------------+
|   aplikacja     | -------------------------------> |     serwer       |
|   (klient)      | <------------------------------- |   (GitHub Pages) |
+-----------------+   200 OK + JSON                  +------------------+
```

Dla tej lekcji przygotowaliśmy dane na stronie kursu (zawsze dostępne):

- [ksiazki.json](../pliki/api/ksiazki.json) – 12 książek: `id`, `tytul`, `autor`, `rok`, `gatunek`, `ocena`,
- [kursy.json](../pliki/api/kursy.json) – przykładowe kursy walut.

Pełny adres: `https://belferit.github.io/pracownia-programowania-aplikacji-mobilnych/pliki/api/ksiazki.json`

```csharp
using System.Net.Http.Json;
using System.Text.Json.Serialization;

public class KsiazkaApi
{
    [JsonPropertyName("tytul")] public string Tytul { get; set; } = "";
    [JsonPropertyName("autor")] public string Autor { get; set; } = "";
    [JsonPropertyName("rok")] public int Rok { get; set; }
    [JsonPropertyName("ocena")] public double Ocena { get; set; }
}

public partial class MainPage : ContentPage
{
    private static readonly HttpClient klient = new();   // jeden obiekt na całą aplikację
    private const string Adres =
        "https://belferit.github.io/pracownia-programowania-aplikacji-mobilnych/pliki/api/ksiazki.json";

    private async void OnPobierzClicked(object? sender, EventArgs e)
    {
        aiLadowanie.IsRunning = true;
        try
        {
            List<KsiazkaApi>? ksiazki = await klient.GetFromJsonAsync<List<KsiazkaApi>>(Adres);
            cvKsiazki.ItemsSource = ksiazki;
        }
        catch (HttpRequestException ex)
        {
            await DisplayAlertAsync("Błąd sieci", ex.Message, "OK");
        }
        finally
        {
            aiLadowanie.IsRunning = false;
        }
    }
}
```

| Element | Znaczenie |
|---|---|
| `GetFromJsonAsync<T>(adres)` | pobiera i od razu deserializuje JSON |
| `GetStringAsync(adres)` | pobiera surowy tekst |
| `[JsonPropertyName("tytul")]` | nazwa pola w JSON różni się od nazwy właściwości C# |
| `ActivityIndicator` (`IsRunning`) | „kręciołek” w trakcie ładowania |

!!! info "Uprawnienie INTERNET"
    Aplikacja na Androidzie potrzebuje uprawnienia `android.permission.INTERNET`. Szablon MAUI dodaje je w `Platforms/Android/AndroidManifest.xml` razem z `ACCESS_NETWORK_STATE`. Sprawdź, czy tam są.

!!! warning "Tylko HTTPS"
    Android domyślnie blokuje połączenia `http://` (bez szyfrowania). Używaj adresów `https://`.

## Zadanie główne (25 min)

Utwórz projekt `KsiazkiOnline`.

1. Klasa `KsiazkaApi` ze wszystkimi polami z pliku `ksiazki.json` (także `id` i `gatunek`).
2. Strona: przycisk **Pobierz książki**, `ActivityIndicator`, etykieta `lblInfo` i lista `CollectionView` (tytuł pogrubiony, autor i rok, ocena po prawej z gwiazdką: **4,6 ★**).
3. Po pobraniu `lblInfo` pokazuje: **Pobrano 12 książek, średnia ocena: 4,40** (oblicz LINQ `Average`).
4. Dodaj `Picker` **Gatunek** wypełniany po pobraniu danych listą gatunków bez powtórzeń (`Select(k => k.Gatunek).Distinct().OrderBy(g => g)`) i pozycją **wszystkie**. Wybór filtruje listę.
5. Wyłącz internet w emulatorze (tryb samolotowy) i kliknij przycisk. Aplikacja wyświetla komunikat zamiast się zamykać.

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Wykonaj przelicznik walut na danych z [kursy.json](../pliki/api/kursy.json): `Picker` z walutami pobranymi z pliku, pole kwoty w złotych, wynik w wybranej walucie z dwoma miejscami po przecinku (100 zł → 23,53 EUR). Plik ma inną budowę: obiekt z tablicą `kursy` w środku – przygotuj dwie klasy.

## Czy potrafię…?

- [ ] opisać komunikację klient–serwer
- [ ] pobrać JSON z adresu i zamienić go na listę obiektów
- [ ] dopasować nazwy pól JSON do właściwości C#
- [ ] obsłużyć brak połączenia z internetem
