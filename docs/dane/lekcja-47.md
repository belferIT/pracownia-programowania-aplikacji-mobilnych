# Lekcja 47. Sprawdzian praktyczny: aplikacja z danymi

<p class="lekcja-meta">Dział: Dane, sieć i usługi urządzenia · 45 min · Efekty: INF.04.6 (2) kryt. 3, 6, 9, INF.04.8 (2) · <span class="zakres zakres-p">INF.04</span></p>

## Zasady

- Czas: **40 minut** na pracę, 5 minut na przygotowanie i oddanie.
- Możesz korzystać z [dokumentacji .NET MAUI](https://learn.microsoft.com/pl-pl/dotnet/maui/) i strony pakietu [sqlite-net](https://github.com/praeclarum/sqlite-net). Nie możesz korzystać z narzędzi AI, materiałów z lekcji ani pomocy innych osób.
- Oddajesz folder `Nazwisko_Imie` z podfolderami `mobilna` (cały projekt) i `dokumentacja` (zrzut `mobilna.jpg`).

## Materiały

Pobierz i rozpakuj [rowery.zip](../pliki/lekcja-47/rowery.zip){ download }: `miejski.png`, `gorski.png`, `elektryczny.png`.

## Zadanie

!!! note "Polecenie"
    Wykonaj aplikację mobilną wypożyczalni rowerów **Dwa Kółka**, zapisującą wypożyczenia w bazie SQLite. Projekt nazwij `DwaKolka`. Uruchom aplikację w emulatorze.

```text
Rysunek 1. Aplikacja po dodaniu dwóch wypożyczeń

+---------------------------------------+
|  Dwa Kółka                            |  <- kolor 1, tekst biały
+---------------------------------------+
|  Klient:  [ Jan Kowalski        ]     |
|  Rower:   [ górski – 15 zł/h  v ]     |
|           [ obraz gorski.png ]        |  <- wysokość 120
|  Liczba godzin: 3           [ - | + ] |
|  Kask (+5 zł)                 [==o]   |
|  Koszt: 50,00 zł                      |  <- liczony na bieżąco
|  [            WYPOŻYCZ              ] |  <- kolor 2
+---------------------------------------+
|  Jan Kowalski  górski  3 h   50,00 zł |
|  Anna Nowak    miejski 1 h   10,00 zł |
+---------------------------------------+
|  Przychód: 60,00 zł                   |
+---------------------------------------+
```

| Element | Grupa A | Grupa B |
|---|---|---|
| kolor 1 (pasek) | `#283593` | `#4E342E` |
| kolor 2 (przycisk) | `#FFB300` | `#26A69A` |

### Wygląd i działanie

1. Interfejs w XAML, układ bez nachodzenia elementów. Pasek **Dwa Kółka** (tło kolor 1, tekst biały, rozmiar `24`).
2. Pole **Klient**. Po wypożyczeniu nazwa klienta zostaje zapamiętana w preferencjach i wpisuje się automatycznie przy następnym uruchomieniu aplikacji.
3. `Picker` z rowerami: **miejski – 10 zł/h**, **górski – 15 zł/h**, **elektryczny – 25 zł/h**. Po wyborze widoczny jest obraz roweru (przed wyborem – ukryty).
4. `Stepper` 1–12 godzin (start 1) z etykietą **Liczba godzin: N**, `Switch` **Kask (+5 zł)**.
5. Koszt przeliczany na bieżąco przy każdej zmianie: cena × godziny; od **4 godzin** rabat **20%** na rower; kask 5 zł bez rabatu. Format: **Koszt: 50,00 zł**.
6. Przycisk **WYPOŻYCZ** (tło kolor 2): gdy brak klienta lub roweru – komunikat **Uzupełnij dane wypożyczenia**. W przeciwnym razie zapisuje wypożyczenie w bazie (klient, rower, godziny, kask, koszt, data i godzina) i odświeża listę.
7. Lista wypożyczeń z bazy (najnowsze na górze): klient, rower, godziny, koszt. Pod listą **Przychód: X zł** – suma kosztów wszystkich wypożyczeń.
8. Dotknięcie wypożyczenia pyta **Usunąć wypożyczenie?** i po potwierdzeniu usuwa je z bazy.

| Rower | Godziny | Kask | Koszt |
|---|---|---|---|
| miejski | 1 | nie | 10,00 zł |
| górski | 3 | tak | 50,00 zł |
| elektryczny | 4 | nie | 80,00 zł |
| miejski | 6 | tak | 53,00 zł |
| elektryczny | 2 | tak | 55,00 zł |

### Dokumentacja

Zrzut `mobilna.jpg` (cały ekran, pasek zadań, emulator i Visual Studio) po dodaniu wypożyczeń z dwóch pierwszych wierszy tabeli.

## Kryteria oceny (30 pkt)

| Kryterium | Punkty |
|---|---|
| Projekt kompiluje się i uruchamia, zrzut ekranu zgodny z wymaganiami | 3 |
| Interfejs w XAML zgodny z rysunkiem, kolory grupy | 3 |
| `Picker` z obrazem ukrytym na starcie i zmienianym po wyborze | 3 |
| `Stepper`, `Switch`, koszt przeliczany na bieżąco | 3 |
| Obliczenia: cena × godziny, rabat 20% od 4 h tylko na rower, kask | 4 |
| Klasa-tabela z kluczem głównym, utworzenie bazy w folderze danych aplikacji | 4 |
| Zapis wypożyczenia w bazie i lista z bazy posortowana od najnowszych | 4 |
| Suma przychodu i usuwanie z potwierdzeniem | 3 |
| Zapamiętanie klienta w preferencjach | 1 |
| Walidacja danych, kod czytelny, znaczące nazwy | 2 |

Progi ocen ustala nauczyciel zgodnie z WSO.
