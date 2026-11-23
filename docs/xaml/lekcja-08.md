# Lekcja 8. Obrazy w aplikacji

<p class="lekcja-meta">Dział: XAML i układy · 45 min · Efekty: INF.04.6 (2) kryt. 4, 6 · <span class="zakres zakres-p">INF.04</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- dodać obraz do zasobów aplikacji,
- wyświetlić obraz kontrolką `Image` i dobrać sposób skalowania (`Aspect`),
- utworzyć przycisk z obrazkiem (`ImageButton`).

## Wprowadzenie

### Zasoby obrazów

Obrazy kopiujesz do folderu **`Resources/Images`** projektu. Visual Studio automatycznie nadaje im akcję kompilacji **MauiImage** i przygotowuje wersje dla każdej platformy.

!!! warning "Nazwy plików obrazów"
    Nazwa pliku: **małe litery**, cyfry i podkreślnik, zaczyna się od litery. Bez spacji, myślników i polskich znaków. `kot_1.png` – dobrze, `Kot-1.png` – źle (na Androidzie projekt się nie zbuduje).

```xml
<Image Source="gory.jpg"
       Aspect="AspectFill"
       HeightRequest="200"
       HorizontalOptions="Fill" />
```

| `Aspect` | Działanie |
|---|---|
| `AspectFit` | cały obraz widoczny, zachowane proporcje (mogą zostać puste pasy) – domyślne |
| `AspectFill` | wypełnia obszar, zachowuje proporcje, przycina nadmiar |
| `Fill` | rozciąga do obszaru, **zniekształca** proporcje |
| `Center` | bez skalowania, na środku |

!!! info "Obraz na całą szerokość ekranu"
    W arkuszach INF.04 pojawia się wymaganie: „obraz jest rozciągnięty (wypełnia) cały obszar ekranu w poziomie”. Ustaw `HorizontalOptions="Fill"` i odpowiedni `Aspect` (`AspectFill` lub `Fill`, zależnie od treści polecenia), a stronie nie dawaj bocznego `Padding`.

### Zmiana obrazu z C#

```csharp
imgWidok.Source = "morze.jpg";                     // z zasobów
imgWidok.Source = ImageSource.FromFile("las.jpg");  // to samo, zapis pełny
```

### ImageButton

```xml
<ImageButton Source="logo.png" WidthRequest="80" HeightRequest="80"
             CornerRadius="40" Clicked="OnLogoClicked" />
```

## Zadanie główne (25 min)

Pobierz i rozpakuj [obrazy.zip](../pliki/lekcja-08/obrazy.zip){ download }: `gory.jpg`, `morze.jpg`, `las.jpg`, `logo.png`.

Utwórz projekt `Widoki`. Skopiuj obrazy do `Resources/Images` (przeciągnij je do folderu w Eksploratorze rozwiązań).

```text
Rysunek 1. Ekran aplikacji

+-----------------------------------+
| (logo)   Biuro podróży Widok      |  <- logo 60×60, tekst 22, pogrubiony
+-----------------------------------+
|                                   |
|        [ obraz gory.jpg ]         |  <- cała szerokość, wysokość 220
|                                   |
+-----------------------------------+
|  [morze]   [las]   [gory]         |  <- 3 miniatury 100×70, obok siebie
+-----------------------------------+
|  Wybierz kierunek podróży.        |
+-----------------------------------+
```

1. Strona ma tło `#FAFAFA`. Główny układ: `VerticalStackLayout` z `Spacing="10"`, bez bocznego odstępu.
2. Nagłówek: `HorizontalStackLayout` z `Padding="10"` i `Spacing="10"`: obraz `logo.png` 60×60 oraz etykieta **Biuro podróży Widok** (rozmiar `22`, pogrubiona, kolor `#4527A0`, wyśrodkowana w pionie).
3. Duży obraz `gory.jpg` o nazwie `imgWidok`: wypełnia ekran w poziomie, wysokość `220`, `Aspect="AspectFill"`.
4. Trzy kontrolki `ImageButton` (miniatury `morze.jpg`, `las.jpg`, `gory.jpg`) o wymiarach 100×70, `Aspect="AspectFill"`, zaokrąglenie `10`, obok siebie, wyśrodkowane, odstęp `10`.
5. Etykieta **Wybierz kierunek podróży.** z marginesem `10`.
6. Uruchom aplikację. Zmień `Aspect` dużego obrazu na `Fill`, potem na `AspectFit` i zobacz różnicę. Pozostaw `AspectFill`.

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Obsłuż kliknięcia miniatur: po kliknięciu w miniaturę duży obraz zmienia się na wybrany widok, a etykieta pokazuje tekst **Wybrano: morze** (las, góry). Wykorzystaj jedną metodę dla wszystkich trzech przycisków i właściwość `CommandParameter` albo porównanie `sender` z nazwą kontrolki.

## Czy potrafię…?

- [ ] dodać obraz do zasobów i nazwać plik zgodnie z zasadami
- [ ] dobrać wartość `Aspect` do sytuacji
- [ ] rozciągnąć obraz na całą szerokość ekranu
- [ ] zmienić obraz z poziomu C#
