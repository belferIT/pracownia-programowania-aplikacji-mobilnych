# Dział 4. Dane, sieć i usługi urządzenia

14 lekcji o przechowywaniu danych (preferencje, pliki, SQLite), komunikacji z serwerem i funkcjach telefonu: czas, kalendarz, lokalizacja, powiadomienia, czujniki i aparat. Dział kończy się sprawdzianem.

| Lekcje | Temat | Zakres |
|---|---|---|
| 34–35 | `Preferences`, pliki i JSON | <span class="zakres zakres-p">INF.04</span> |
| 36–38 | baza SQLite: model, CRUD, dziennik treningów w stylu egzaminu | <span class="zakres zakres-p">INF.04</span> |
| 39–40 | `HttpClient`: pobieranie i wysyłanie JSON, błędy sieci | <span class="zakres zakres-p">INF.04</span> |
| 41–44 | timer, daty, lokalizacja, powiadomienia | <span class="zakres zakres-p">INF.04</span> |
| 45–46 | czujniki, aparat i galeria | <span class="zakres zakres-gw">★ poza egzaminem</span> |
| 47 | sprawdzian praktyczny | <span class="zakres zakres-p">INF.04</span> |

!!! info "Dane z internetu do ćwiczeń"
    Pliki JSON do lekcji 39 są na tej stronie: [ksiazki.json](../pliki/api/ksiazki.json) i [kursy.json](../pliki/api/kursy.json). Kursy walut są przykładowe, nie rzeczywiste.

!!! warning "Uprawnienia Androida"
    Lokalizacja, aparat, powiadomienia, wibracja i latarka wymagają wpisu w `Platforms/Android/AndroidManifest.xml`. Brak wpisu to najczęstsza przyczyna wyjątku `PermissionException`.
