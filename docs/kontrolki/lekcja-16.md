# Lekcja 16. Galeria obrazów. Zadanie w stylu egzaminu

<p class="lekcja-meta">Dział: Kontrolki i wiązanie danych · 45 min · Efekty: INF.04.6 (2) kryt. 5, 6, 11 · <span class="zakres zakres-p">INF.04</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- wykonać galerię obrazów przewijanych „w kółko” (karuzela),
- przechowywać obrazy w zasobach i wybierać je z tablicy,
- połączyć przyciski, pole edycyjne i przełącznik w jednej aplikacji.

## Wprowadzenie

Karuzela to przechodzenie po obrazach tak, że po ostatnim jest pierwszy, a przed pierwszym – ostatni. Wygodnie użyć tablicy nazw plików i indeksu z operatorem reszty z dzielenia `%`.

```csharp
private readonly string[] obrazy = { "widok1.jpg", "widok2.jpg", "widok3.jpg", "widok4.jpg" };
private int indeks = 0;

private void Nastepny()
{
    indeks = (indeks + 1) % obrazy.Length;              // 3 → 0
    imgGaleria.Source = obrazy[indeks];
}

private void Poprzedni()
{
    indeks = (indeks - 1 + obrazy.Length) % obrazy.Length;  // 0 → 3
    imgGaleria.Source = obrazy[indeks];
}
```

| `indeks` | Następny | Poprzedni |
|---|---|---|
| 0 (widok1) | 1 (widok2) | 3 (widok4) |
| 3 (widok4) | 0 (widok1) | 2 (widok3) |

!!! tip "Gotowa kontrolka"
    MAUI ma też `CarouselView` (przewijanie palcem). Na egzaminie polecenie zwykle opisuje przyciski, więc zrób dokładnie to, co jest w poleceniu.

## Zadanie główne (25 min)

Pobierz i rozpakuj [galeria.zip](../pliki/lekcja-16/galeria.zip){ download }: `widok1.jpg` … `widok4.jpg`.

!!! note "Polecenie (styl arkusza INF.04)"
    Wykonaj aplikację mobilną za pomocą środowiska programistycznego dostępnego na stanowisku i uruchom ją w emulatorze systemu mobilnego. Projekt nazwij `Galeria`. Wykorzystaj obrazy z archiwum `galeria.zip`.

```text
Rysunek 1. Stan początkowy aplikacji

+---------------------------------------+
|              Galeria                  |  <- większa czcionka, tło #4527A0
+---------------------------------------+
|                                       |
|          [ obraz widok1.jpg ]         |  <- na całą szerokość ekranu
|                                       |
+---------------------------------------+
| [ POPRZEDNI ]           [ NASTĘPNY ]  |  <- przy lewej i prawej krawędzi
|                                       |
| Który obraz wyświetlić?  [_______]    |
| Tryb ciemny?             [ switch ]   |
|                                       |
| Autor: Imię Nazwisko                  |
+---------------------------------------+
```

**Opis wyglądu i działania aplikacji**

- Napis **Galeria**, wizualnie większy od pozostałych.
- Poniżej obszar do przeglądania zdjęć z domyślnie załadowanym obrazem `widok1.jpg`. Kolejność wyświetlania: widok1, widok2, widok3, widok4, widok1 (karuzela).
- Poniżej przycisk **POPRZEDNI**, który zmienia obraz na poprzedni, np. 1 na 4, 4 na 3.
- Obok przycisk **NASTĘPNY**, który zmienia obraz na następny, np. 1 na 2, 4 na 1.
- Poniżej pole edycyjne poprzedzone napisem **Który obraz wyświetlić?**. Wpisanie liczby 1–4 wyświetla odpowiedni obraz. Wpisanie innego znaku lub liczby jest ignorowane – aplikacja nie wywołuje błędu.
- Poniżej przełącznik poprzedzony napisem **Tryb ciemny?**. Włączenie zmienia tło aplikacji na `#212121`, a kolor wszystkich napisów na biały. Wyłączenie przywraca tło `#EDE7F6` i napisy czarne.
- Na dole napis **Autor:** i Twoje imię i nazwisko.

**Założenia aplikacji**

- obrazy przechowywane w zasobach aplikacji,
- interfejs zapisany w języku XAML,
- układ liniowy (Stack) lub siatka (Grid), elementy nie nachodzą na siebie,
- kolory tła: `#4527A0` (pasek z napisem Galeria, tekst biały), `#EDE7F6` (tło aplikacji), `#FF9800` (przyciski),
- obraz wypełnia cały obszar ekranu w poziomie,
- przyciski są umieszczone poziomo obok siebie i przylegają do lewej i prawej krawędzi ekranu,
- do pola edycyjnego można wpisać jedynie liczby,
- działanie kontrolek obsłużone za pomocą zdarzeń, kod czytelny, nazwy znaczące.

**Testy**

| Akcja (od stanu początkowego) | Wyświetlany obraz |
|---|---|
| NASTĘPNY | widok2 |
| POPRZEDNI | widok4 |
| NASTĘPNY × 4 | widok1 |
| wpisanie `3` | widok3 |
| wpisanie `7` albo `a` | bez zmiany, brak błędu |

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Gdy w polu jest wpisany numer, a użytkownik kliknie NASTĘPNY lub POPRZEDNI, pole powinno pokazywać numer bieżącego obrazu. Dodaj też obsługę przesunięcia palcem po obrazie (`SwipeGestureRecognizer` z `Direction="Left"` i `Direction="Right"`).

## Czy potrafię…?

- [ ] przechodzić po tablicy „w kółko” operatorem `%`
- [ ] przyleić przyciski do lewej i prawej krawędzi ekranu
- [ ] zignorować błędne dane w polu bez awarii aplikacji
- [ ] zmienić kolor tła i napisów przełącznikiem
