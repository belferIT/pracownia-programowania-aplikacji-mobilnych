# Lekcja 53. Dokumentacja: komentarze nagłówkowe i instrukcja użytkownika

<p class="lekcja-meta">Dział: Jakość, testy i publikacja · 45 min · Efekty: INF.04.8 (2) kryt. 1, 2, 4 · <span class="zakres zakres-p">INF.04</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- napisać komentarz nagłówkowy funkcji według wzoru z arkusza INF.04,
- udokumentować klasę: jej przeznaczenie, pola i metody,
- napisać krótką instrukcję użytkownika ze zrzutami ekranu.

## Wprowadzenie

Na egzaminie INF.04 dokumentacja to osobne punkty w kryteriach oceny. Zwykle musisz:

1. wstawić **komentarz nagłówkowy** przed wskazaną funkcją lub klasą, dokładnie według wzoru z arkusza,
2. wykonać **zrzuty ekranu** działających aplikacji (cały ekran, z nazwami plików z polecenia),
3. czasem: opisać testy lub środowisko (system, IDE, wersja .NET).

Wzór komentarza w arkuszach CKE wygląda tak:

```csharp
/********************************************************
 * nazwa funkcji: <tu wstaw nazwę funkcji>
 * opis funkcji: <tu wstaw opis działania funkcji>
 * parametry: <tu wstaw nazwę parametru> - <tu wstaw opis parametru>
 * zwracany typ i opis: <tu wstaw typ zwracany oraz opis>
 * autor: <tu wstaw numer zdającego>
 ********************************************************/
```

Przykład wypełnienia:

```csharp
/********************************************************
 * nazwa funkcji: CenaBiletu
 * opis funkcji: oblicza cenę biletu do kina na podstawie wieku widza,
 *               dnia tygodnia i karty stałego klienta
 * parametry: wiek - wiek widza w latach, od 0 do 120
 *            dzien - dzień tygodnia seansu (we wtorek rabat 5 zł)
 *            karta - true, gdy widz ma kartę stałego klienta (rabat 10%)
 * zwracany typ i opis: decimal - cena biletu w złotych, zaokrąglona do groszy
 * autor: 01234567890
 ********************************************************/
public static decimal CenaBiletu(int wiek, DayOfWeek dzien, bool karta)
```

!!! warning "Wzór z arkusza jest najważniejszy"
    Wzór może się różnić w kolejnych arkuszach, np. w polu **autor** (PESEL albo numer zdającego) lub w opisie klasy zamiast funkcji. Zawsze przepisz układ z arkusza, który masz przed sobą. Za brak jednego pola tracisz punkt.

!!! tip "Dobry opis"
    - Opis mówi, **co** robi funkcja, a nie powtarza kod („dodaje 5 do zmiennej”).
    - Przy parametrach podaj jednostki i dopuszczalny zakres.
    - Gdy funkcja nic nie zwraca: `zwracany typ i opis: void - brak, wynik wyświetlany jest w etykiecie lblWynik`.

!!! info "Komentarze XML <span class="zakres zakres-gw">★ poza egzaminem</span>"
    W pracy częściej używa się komentarzy `///`. Wpisz `///` nad metodą, a Visual Studio wstawi szablon `<summary>`, `<param>`, `<returns>`. Treść pojawia się potem w podpowiedziach IntelliSense.

**Instrukcja użytkownika** to krótki dokument dla osoby, która nie zna kodu. Zawiera: przeznaczenie aplikacji, wymagania (system), opis ekranu ze zrzutem, kroki typowych czynności, komunikaty błędów i co wtedy zrobić.

## Zadanie główne (25 min)

**Część 1 (12 min).** Skopiuj kod do pliku `Statystyka.cs` i wstaw komentarz nagłówkowy według wzoru CKE przed każdą z trzech metod. Przed klasą wstaw komentarz z polami **nazwa klasy**, **opis klasy**, **pola**, **metody**, **autor**.

```csharp
public class Statystyka
{
    private readonly List<int> wyniki = new();

    public void Dodaj(int punkty)
    {
        if (punkty < 0 || punkty > 100)
            throw new ArgumentOutOfRangeException(nameof(punkty));
        wyniki.Add(punkty);
    }

    public double Srednia()
    {
        return wyniki.Count == 0 ? 0 : wyniki.Average();
    }

    public int LiczbaZdanych(int prog)
    {
        int licznik = 0;
        foreach (int w in wyniki)
            if (w >= prog) licznik++;
        return licznik;
    }
}
```

**Część 2 (13 min).** Napisz instrukcję użytkownika aplikacji **Napiwek** z lekcji 48 (albo innej Twojej aplikacji) w edytorze tekstu. Plik `instrukcja`:

1. Tytuł, przeznaczenie aplikacji (1–2 zdania), wymagania (Android od wersji…, Windows 10/11).
2. Zrzut ekranu z podpisem **Rysunek 1. Ekran główny** i opisem każdego elementu (numerki na zrzucie lub lista).
3. Kroki: **Jak podzielić rachunek** (numerowana lista, co najmniej 4 kroki).
4. Tabela **Komunikaty i problemy**: co widzi użytkownik, co oznacza, co zrobić (co najmniej 2 wiersze).
5. Stopka: wersja aplikacji, data, autor.

??? question "Podpowiedź: zrzut ekranu jak na egzaminie"
    ++win+shift+s++ wycina fragment ekranu, ++print-screen++ kopiuje cały ekran. Na egzaminie zwykle wymagany jest zrzut **całego** ekranu z widocznym emulatorem i paskiem zadań. Zapisz go w formacie z polecenia (najczęściej JPEG lub PNG).

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Dodaj w projekcie `Kino.Logika` z lekcji 51 komentarze XML `///` do klasy `Cennik` i jej metody. We właściwościach projektu włącz **Kompilacja → Dane wyjściowe → Plik dokumentacji**. Zbuduj projekt i znajdź wygenerowany plik `Kino.Logika.xml`.

## Czy potrafię…?

- [ ] napisać komentarz nagłówkowy funkcji według wzoru CKE
- [ ] opisać parametry z zakresem wartości i typ zwracany
- [ ] udokumentować klasę: pola i metody
- [ ] przygotować instrukcję użytkownika ze zrzutem ekranu
