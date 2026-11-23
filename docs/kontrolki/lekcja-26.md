# Lekcja 26. Sprawdzian praktyczny: aplikacja mobilna

<p class="lekcja-meta">Dział: Kontrolki i wiązanie danych · 45 min · Efekty: INF.04.6 (2) kryt. 5, 6, 11, INF.04.8 (2) · <span class="zakres zakres-p">INF.04</span></p>

## Zasady

- Czas: **40 minut** na pracę, 5 minut na przygotowanie i oddanie.
- Możesz korzystać z [dokumentacji .NET MAUI](https://learn.microsoft.com/pl-pl/dotnet/maui/). Nie możesz korzystać z narzędzi AI, materiałów z lekcji ani pomocy innych osób.
- Zadanie jest zbudowane jak część II (aplikacja mobilna) egzaminu INF.04.
- Oddajesz folder `Nazwisko_Imie` z podfolderami `mobilna` (cały projekt) i `dokumentacja` (zrzut `mobilna.jpg`) w miejscu wskazanym przez nauczyciela.

## Materiały

Pobierz i rozpakuj [kwiaciarnia.zip](../pliki/lekcja-26/kwiaciarnia.zip){ download }: `roza.png`, `tulipan.png`, `slonecznik.png`.

## Zadanie

!!! note "Polecenie"
    Wykonaj aplikację mobilną kwiaciarni **Bukiet** i uruchom ją w emulatorze. Projekt nazwij `Bukiet`. Obrazy umieść w zasobach aplikacji.

```text
Rysunek 1. Aplikacja po wybraniu kwiatu

+---------------------------------------+
|           Kwiaciarnia Bukiet          |  <- kolor 1, tekst biały, 26
+---------------------------------------+
|  Kwiat:  [ róża – 8 zł          v ]   |  <- Picker
|                                       |
|            [ obraz roza.png ]         |  <- wysokość 180
|                                       |
|  Liczba sztuk: 5            [ - | + ] |  <- Stepper
|  Ozdobne opakowanie (+10 zł)   [==o]  |  <- Switch
|  Dostawa:                             |
|   (o) odbiór osobisty                 |  <- RadioButton
|   ( ) kurier (+15 zł)                 |
|                                       |
|  [               OBLICZ             ] |  <- kolor 2
|  Do zapłaty: 40,00 zł                 |  <- 22, pogrubiony
|                                       |
|  Autor: Imię Nazwisko                 |
+---------------------------------------+
```

### Wygląd

Kolory dla grupy A i B podaje tabela. Swoją grupę poda nauczyciel.

| Element | Grupa A | Grupa B |
|---|---|---|
| kolor 1 (pasek z nazwą) | `#AD1457` | `#2E7D32` |
| kolor 2 (przycisk) | `#F8BBD0` | `#C8E6C9` |
| kolor 3 (tło strony) | `#FCE4EC` | `#F1F8E9` |

1. Interfejs w XAML, układ liniowy lub siatka, elementy nie nachodzą na siebie.
2. Pasek z napisem **Kwiaciarnia Bukiet** na całą szerokość: tło kolor 1, tekst biały, rozmiar `26`, wyśrodkowany.
3. Tło strony: kolor 3. Przycisk **OBLICZ**: tło kolor 2, tekst czarny, pogrubiony, szerokość ekranu z marginesem `20`.
4. `Picker` z pozycjami: **róża – 8 zł**, **tulipan – 5 zł**, **słonecznik – 7 zł**. Na starcie nic nie jest wybrane.
5. Obraz kwiatu (wysokość `180`) widoczny dopiero po wybraniu kwiatu i zmieniający się zgodnie z wyborem.
6. `Stepper` od 1 do 50 (start 1) z etykietą **Liczba sztuk: N** aktualizowaną na bieżąco.
7. `Switch` z opisem **Ozdobne opakowanie (+10 zł)**, dwa `RadioButton` w jednej grupie: **odbiór osobisty** (zaznaczony) i **kurier (+15 zł)**.
8. Na dole napis **Autor:** z Twoim imieniem i nazwiskiem.

### Działanie

Po kliknięciu **OBLICZ**:

1. Jeśli nie wybrano kwiatu – w etykiecie wyniku napis **Wybierz kwiat**.
2. Koszt kwiatów = cena kwiatu × liczba sztuk. Przy **20 sztukach i więcej** rabat **10%** na kwiaty.
3. Doliczane są: opakowanie 10 zł (jeśli włączone) i kurier 15 zł (jeśli wybrany). Na dodatki rabat nie obowiązuje.
4. Wynik: **Do zapłaty: X zł**, X z dwoma miejscami po przecinku.

| Kwiat | Sztuk | Opakowanie | Dostawa | Do zapłaty |
|---|---|---|---|---|
| róża | 1 | nie | odbiór | 8,00 zł |
| tulipan | 10 | tak | odbiór | 60,00 zł |
| róża | 20 | nie | kurier | 159,00 zł |
| słonecznik | 25 | tak | kurier | 182,50 zł |
| tulipan | 19 | nie | kurier | 110,00 zł |
| (brak) | – | – | – | Wybierz kwiat |

### Dokumentacja

Zrzut ekranu `mobilna.jpg`: cały ekran z widocznym paskiem zadań, emulator z wynikiem dla danych z czwartego wiersza tabeli i Visual Studio z projektem pod spodem.

## Kryteria oceny (30 pkt)

| Kryterium | Punkty |
|---|---|
| Projekt kompiluje się i uruchamia w emulatorze, zrzut ekranu zgodny z wymaganiami | 3 |
| Interfejs w XAML, elementy w kolejności z rysunku, bez nachodzenia | 3 |
| Kolory i formatowanie paska, tła i przycisku zgodnie z grupą | 3 |
| `Picker` z trzema pozycjami, obraz ukryty na starcie i zmieniany po wyborze | 4 |
| `Stepper` z zakresem 1–50 i etykietą aktualizowaną na bieżąco | 3 |
| `Switch` i `RadioButton` w jednej grupie, poprawne stany początkowe | 2 |
| Obliczenia: cena × sztuki, rabat od 20 sztuk tylko na kwiaty | 5 |
| Dodatki: opakowanie i kurier | 2 |
| Komunikat **Wybierz kwiat**, format wyniku z dwoma miejscami | 2 |
| Kod czytelny: wcięcia, znaczące nazwy kontrolek i metod, podpis autora | 3 |

Progi ocen ustala nauczyciel zgodnie z WSO.
