# Lekcja 5. Układy liniowe: StackLayout

<p class="lekcja-meta">Dział: XAML i układy · 45 min · Efekty: INF.04.6 (2) kryt. 5, 6 · <span class="zakres zakres-p">INF.04</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- ułożyć kontrolki w pionie i w poziomie,
- ustawić marginesy zewnętrzne (`Margin`) i wewnętrzne (`Padding`),
- wyrównać kontrolki (`HorizontalOptions`, `VerticalOptions`),
- zagnieżdżać układy jeden w drugim.

## Wprowadzenie

Strona (`ContentPage`) ma **jedno** dziecko: zwykle jest nim układ (*layout*), który zawiera wiele kontrolek.

| Układ | Działanie |
|---|---|
| `VerticalStackLayout` | elementy jeden pod drugim |
| `HorizontalStackLayout` | elementy obok siebie |
| `Spacing="10"` | odstęp między elementami |

```text
VerticalStackLayout                  HorizontalStackLayout
+----------------+                   +-----+-----+-----+
| element 1      |                   | el1 | el2 | el3 |
+----------------+                   +-----+-----+-----+
| element 2      |
+----------------+
```

### Margin i Padding

| Zapis | Znaczenie |
|---|---|
| `Margin="20"` | 20 ze wszystkich stron |
| `Margin="20,10"` | 20 lewo i prawo, 10 góra i dół |
| `Margin="5,10,15,20"` | lewo, góra, prawo, dół (**inna kolejność niż w CSS!**) |
| `Padding="15"` | odstęp wewnętrzny (między krawędzią układu a zawartością) |

### Wyrównanie

`HorizontalOptions` i `VerticalOptions` przyjmują wartości: `Start`, `Center`, `End`, `Fill` (wypełnij). W `VerticalStackLayout` liczy się wyrównanie w poziomie, w `HorizontalStackLayout` w pionie.

```xml
<VerticalStackLayout Padding="20" Spacing="15">
    <Label Text="Logowanie" FontSize="28" HorizontalOptions="Center" />
    <HorizontalStackLayout Spacing="10" HorizontalOptions="End">
        <Button Text="Anuluj" />
        <Button Text="OK" />
    </HorizontalStackLayout>
</VerticalStackLayout>
```

!!! info "Jednostki"
    Wymiary w MAUI podajesz w jednostkach niezależnych od urządzenia (na Androidzie: *dp*). Dzięki temu przycisk `WidthRequest="200"` wygląda podobnie na telefonach o różnej gęstości pikseli.

!!! warning "Egzamin: elementy nie mogą na siebie nachodzić"
    W arkuszach INF.04 często pojawia się wymaganie: „Zastosowany typ rozkładu: liniowy (Linear / Stack) lub względny, elementy rozkładu nie mogą na siebie nachodzić”. `VerticalStackLayout` spełnia je automatycznie.

## Zadanie główne (25 min)

Utwórz projekt `Profil` i odwzoruj ekran z rysunku 1.

```text
Rysunek 1. Ekran aplikacji

+-----------------------------------+
|          PROFIL UCZNIA            |  <- tło #4527A0, tekst biały, 26, pogrubiony
+-----------------------------------+
|  Imię:        Jan                 |  <- dwa Label obok siebie
|  Nazwisko:    Kowalski            |
|  Klasa:       4TP                 |
+-----------------------------------+
|  [ Edytuj ]   [ Usuń ]            |  <- przyciski obok siebie, do prawej
+-----------------------------------+
|        Ostatnia zmiana: dziś      |  <- kursywa, 14, kolor #757575, na środku
+-----------------------------------+
```

1. Główny układ: `VerticalStackLayout` bez odstępu wewnętrznego, `Spacing="0"`.
2. Nagłówek **PROFIL UCZNIA**: `Label` z tłem `#4527A0`, tekst biały, rozmiar `26`, pogrubiony, `Padding="20"`, tekst wyśrodkowany (`HorizontalTextAlignment="Center"`).
3. Sekcja danych: `VerticalStackLayout` z `Padding="20"` i `Spacing="8"`. Każdy wiersz to `HorizontalStackLayout` z dwiema etykietami. Pierwsza etykieta (opis) ma szerokość `100` i jest pogrubiona.
4. Przyciski **Edytuj** (tło `#FF9800`) i **Usuń** (tło `#D32F2F`), tekst biały, obok siebie, odstęp `10`, wyrównane do prawej, margines `20` z prawej i z dołu.
5. Stopka zgodnie z rysunkiem.
6. Uruchom aplikację w emulatorze i na Windows. Porównaj wygląd.

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Dodaj między danymi a przyciskami poziomą linię oddzielającą: `BoxView` o wysokości `1`, kolorze `#BDBDBD` i marginesie `20,0`. Następnie zmień przyciski tak, aby **razem** wypełniały całą szerokość ekranu po połowie (podpowiedź: tu `HorizontalStackLayout` nie wystarczy, wrócisz do tego przy `Grid`).

## Czy potrafię…?

- [ ] ułożyć elementy w pionie i w poziomie
- [ ] zapisać `Margin` z czterema wartościami we właściwej kolejności
- [ ] odróżnić `Margin` od `Padding`
- [ ] wyrównać przyciski do prawej krawędzi
