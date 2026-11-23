# Lekcja 40. Wysyłanie danych i obsługa błędów sieci

<p class="lekcja-meta">Dział: Dane, sieć i usługi urządzenia · 45 min · Efekty: INF.04.6 (2) kryt. 8 · <span class="zakres zakres-p">INF.04</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- wysłać dane do serwera metodą POST w formacie JSON,
- odczytać kod odpowiedzi HTTP,
- sprawdzić dostęp do internetu przed wysłaniem żądania,
- ustawić limit czasu żądania.

## Wprowadzenie

| Metoda HTTP | Działanie | `HttpClient` |
|---|---|---|
| `GET` | pobranie danych | `GetFromJsonAsync<T>` |
| `POST` | utworzenie nowego zasobu | `PostAsJsonAsync(adres, obiekt)` |
| `PUT` | zmiana zasobu | `PutAsJsonAsync(adres, obiekt)` |
| `DELETE` | usunięcie zasobu | `DeleteAsync(adres)` |

| Kod odpowiedzi | Znaczenie |
|---|---|
| `200 OK` | sukces |
| `201 Created` | utworzono zasób (typowa odpowiedź na POST) |
| `400 Bad Request` | błędne dane |
| `404 Not Found` | nie ma takiego adresu |
| `500 Internal Server Error` | błąd serwera |

Do ćwiczeń użyjemy publicznego testowego API **JSONPlaceholder**: przyjmuje POST na adres `https://jsonplaceholder.typicode.com/posts`, odpowiada kodem `201` i zwraca wysłany obiekt z nadanym `id` (danych nie zapisuje naprawdę).

```csharp
public class Wpis
{
    [JsonPropertyName("id")] public int Id { get; set; }
    [JsonPropertyName("title")] public string Tytul { get; set; } = "";
    [JsonPropertyName("body")] public string Tresc { get; set; } = "";
    [JsonPropertyName("userId")] public int UzytkownikId { get; set; }
}

private static readonly HttpClient klient = new() { Timeout = TimeSpan.FromSeconds(10) };

private async void OnWyslijClicked(object? sender, EventArgs e)
{
    if (Connectivity.Current.NetworkAccess != NetworkAccess.Internet)
    {
        await DisplayAlertAsync("Brak sieci", "Połącz się z internetem", "OK");
        return;
    }

    var wpis = new Wpis { Tytul = entTytul.Text, Tresc = edtTresc.Text, UzytkownikId = 1 };
    try
    {
        HttpResponseMessage odp = await klient.PostAsJsonAsync("https://jsonplaceholder.typicode.com/posts", wpis);
        if (odp.IsSuccessStatusCode)
        {
            Wpis? zapisany = await odp.Content.ReadFromJsonAsync<Wpis>();
            lblWynik.Text = $"Wysłano. Kod {(int)odp.StatusCode}, nadane id: {zapisany?.Id}";
        }
        else
        {
            lblWynik.Text = $"Serwer zwrócił błąd {(int)odp.StatusCode}";
        }
    }
    catch (TaskCanceledException)
    {
        lblWynik.Text = "Przekroczono czas oczekiwania";
    }
    catch (HttpRequestException ex)
    {
        lblWynik.Text = $"Błąd połączenia: {ex.Message}";
    }
}
```

!!! warning "Nie zamrażaj interfejsu"
    Nigdy nie wywołuj `.Result` ani `.Wait()` na operacji sieciowej. Zamrozi to aplikację (a Android może ją zamknąć). Zawsze `await`.

## Zadanie główne (25 min)

Utwórz projekt `Zgloszenie` – formularz zgłoszenia usterki w pracowni.

1. Formularz: `Picker` **Sala** (12, 14, 21), `Picker` **Rodzaj usterki** (komputer, monitor, drukarka, sieć), `Editor` **Opis**, przycisk **Wyślij zgłoszenie**, `ActivityIndicator`, etykieta `lblWynik`.
2. Klasa `Wpis` jak w przykładzie. Tytuł: **Sala 14 – drukarka**, treść: opis z pola.
3. Przed wysłaniem sprawdź: wybrano salę i rodzaj, opis ma co najmniej 10 znaków. W przeciwnym razie komunikat i brak wysyłania.
4. Sprawdź dostęp do internetu (`Connectivity`).
5. Wyślij dane metodą POST. Po sukcesie: **Zgłoszenie przyjęte. Numer: 101** (numer = `id` z odpowiedzi), wyczyść formularz.
6. Obsłuż błędy: brak sieci, przekroczenie czasu, błąd HTTP. Sprawdź tryb samolotowy w emulatorze.
7. W trakcie wysyłania przycisk jest nieaktywny, a `ActivityIndicator` się kręci.

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Zapisuj zgłoszenia wysłane bez internetu w pliku JSON (lekcja 35) jako „oczekujące”. Gdy wróci połączenie (zdarzenie `Connectivity.Current.ConnectivityChanged`), wyślij je automatycznie i pokaż komunikat **Wysłano N oczekujących zgłoszeń**.

## Czy potrafię…?

- [ ] wysłać obiekt jako JSON metodą POST
- [ ] odczytać kod odpowiedzi i treść odpowiedzi
- [ ] sprawdzić dostęp do internetu
- [ ] obsłużyć przekroczenie czasu i błąd połączenia
