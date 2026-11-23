# Lekcja 32. Przewodnik po mieście. Zadanie w stylu egzaminu

<p class="lekcja-meta">Dział: Nawigacja i platformy · 45 min · Efekty: INF.04.6 (2) kryt. 5, 6, 10 · <span class="zakres zakres-p">INF.04</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- wykonać aplikację z menu i podstronami według opisu w stylu arkusza INF.04,
- połączyć `Shell`, listę, nawigację z parametrem i obrazy z zasobów.

## Wprowadzenie

!!! tip "Plan na 25 minut"
    | Minuty | Krok |
    |---|---|
    | 0–3 | utworzenie projektu, skopiowanie obrazów, dodanie pustych stron |
    | 3–8 | `AppShell.xaml`: menu i kolory, uruchomienie |
    | 8–15 | klasa danych i lista na stronie **Atrakcje** |
    | 15–21 | strona szczegółów i przekazanie danych |
    | 21–25 | strona **O mieście**, sprawdzenie, zrzut ekranu |

## Zadanie główne (25 min)

Pobierz i rozpakuj [przewodnik.zip](../pliki/lekcja-32/przewodnik.zip){ download }: `zamek.jpg`, `rynek.jpg`, `park.jpg`, `port.jpg`.

!!! note "Polecenie (styl arkusza INF.04)"
    Wykonaj aplikację mobilną **Przewodnik** z systemem menu i przechodzeniem do podstron. Projekt nazwij `Przewodnik`. Uruchom aplikację w emulatorze i wykonaj zrzut ekranu `mobilna.jpg` ze stroną szczegółów atrakcji **Port**.

```text
Rysunek 1. Menu                       Rysunek 2. Atrakcje             Rysunek 3. Szczegóły

+-------------------------+          +--------------------------+     +--------------------------+
|  PRZEWODNIK             |          | ☰  Atrakcje              |     | ←  Port                  |
|  Odkryj nasze miasto    |          +--------------------------+     +--------------------------+
+-------------------------+          | Zamek            1,2 km  |     | [ obraz port.jpg ]       |
|  Atrakcje               |          | Rynek            0,0 km  |     |                          |
|  O mieście              |          | Park             0,8 km  |     | Bilet: 15 zł             |
|  Ustawienia             |          | Port             2,5 km  |     | Odległość: 2,5 km        |
+-------------------------+          +--------------------------+     | Opis ...                 |
|  Autor: Imię Nazwisko   |                                           | [ Odwiedzone   [==o] ]   |
+-------------------------+                                           +--------------------------+
```

**Opis wyglądu i działania aplikacji**

1. Aplikacja ma menu wysuwane z pozycjami **Atrakcje**, **O mieście**, **Ustawienia**. Nagłówek menu: napis **PRZEWODNIK** (rozmiar `28`, pogrubiony) i pod nim **Odkryj nasze miasto**, tło `#00695C`, tekst biały. Stopka menu: **Autor:** i Twoje imię i nazwisko.
2. Pasek tytułu: tło `#00695C`, tekst biały.
3. **Atrakcje**: lista czterech atrakcji z nazwą (pogrubioną) i odległością od rynku po prawej stronie, w formacie **1,2 km**. Dane:

    | Nazwa | Obraz | Bilet | Odległość od rynku |
    |---|---|---|---|
    | Zamek | zamek.jpg | 20 zł | 1,2 km |
    | Rynek | rynek.jpg | bezpłatnie | 0,0 km |
    | Park | park.jpg | bezpłatnie | 0,8 km |
    | Port | port.jpg | 15 zł | 2,5 km |

4. Dotknięcie atrakcji otwiera stronę szczegółów z tytułem równym nazwie atrakcji, obrazem na całą szerokość ekranu (wysokość `220`), ceną biletu (**Bilet: 15 zł** albo **Wstęp bezpłatny**, gdy cena wynosi 0), odległością i opisem (2–3 zdania, wymyślone).
5. Na stronie szczegółów jest przełącznik **Odwiedzone**. Po powrocie na listę odwiedzone atrakcje mają przy nazwie znak ✔.
6. **O mieście**: nagłówek, akapit tekstu (wymyślone miasto) i liczba odwiedzonych atrakcji: **Odwiedzono 2 z 4 atrakcji** (aktualna przy każdym wejściu na stronę – metoda `OnAppearing`).
7. **Ustawienia**: `Stepper` rozmiaru czcionki opisu (12–24, start 16) – zmiana jest widoczna na stronach szczegółów (wspólna klasa statyczna `Ustawienia`).

**Założenia aplikacji**

- obrazy w zasobach aplikacji, interfejs w XAML, układ bez nachodzenia elementów,
- dane atrakcji w klasie `Atrakcja` (nazwa, obraz, cena biletu – liczba całkowita, odległość – liczba rzeczywista, opis, odwiedzone),
- nawigacja: `Shell` z `FlyoutItem` oraz `PushAsync` albo `GoToAsync` dla szczegółów,
- kod czytelny, znaczące nazwy.

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Dodaj na stronie **Atrakcje** `ToolbarItem` **Najbliżej**, który sortuje listę rosnąco według odległości, oraz `ToolbarItem` **Nieodwiedzone**, który pokazuje tylko nieodwiedzone atrakcje.

## Czy potrafię…?

- [ ] zaplanować pracę nad aplikacją z kilkoma stronami
- [ ] zbudować menu wysuwane z nagłówkiem i stopką
- [ ] przekazać dane do strony szczegółów i odświeżyć listę po powrocie
- [ ] użyć `OnAppearing` do odświeżenia danych na stronie
