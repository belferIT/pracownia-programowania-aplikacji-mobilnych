# Lekcja 22. Lista zakupów. Zadanie w stylu egzaminu

<p class="lekcja-meta">Dział: Kontrolki i wiązanie danych · 45 min · Efekty: INF.04.6 (2) kryt. 6, 7, INF.04.3 (6) kryt. 9 · <span class="zakres zakres-p">INF.04</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- dodawać i usuwać elementy listy w trakcie działania aplikacji,
- oznaczać elementy jako wykonane (wiązanie `CheckBox` z właściwością obiektu),
- wykonać aplikację z listą według opisu w stylu arkusza INF.04.

## Wprowadzenie

```csharp
public class Produkt : INotifyPropertyChanged
{
    private bool kupiony;
    public string Nazwa { get; set; } = "";
    public int Ilosc { get; set; } = 1;   // jeśli zmieniasz ilość po dodaniu, też musi powiadamiać o zmianie!

    public bool Kupiony
    {
        get => kupiony;
        set { kupiony = value; OnPropertyChanged(); }
    }
    // PropertyChanged i OnPropertyChanged jak w lekcji 19
}
```

```csharp
produkty.Add(new Produkt { Nazwa = "Mleko", Ilosc = 2 });   // lista na ekranie od razu się zmienia
produkty.Remove(wybrany);
int doKupienia = produkty.Count(p => !p.Kupiony);          // LINQ: using System.Linq
```

```xml
<DataTemplate x:DataType="local:Produkt">
    <Grid ColumnDefinitions="Auto,*,Auto" Padding="5">
        <CheckBox IsChecked="{Binding Kupiony}" CheckedChanged="OnKupionyZmieniony" />
        <Label Grid.Column="1" Text="{Binding Nazwa}" VerticalOptions="Center" />
        <Label Grid.Column="2" Text="{Binding Ilosc, StringFormat='{0} szt.'}" VerticalOptions="Center" />
    </Grid>
</DataTemplate>
```

!!! info "Projekt struktury danych"
    Zanim zaczniesz pisać, zastanów się, jakie **pola** ma jeden element listy i jakiego są typu. To jest kryterium „projektuje struktury danych dla aplikacji” z podstawy programowej.

## Zadanie główne (25 min)

!!! note "Polecenie (styl arkusza INF.04)"
    Wykonaj aplikację mobilną **Lista zakupów** i uruchom ją w emulatorze. Projekt nazwij `ListaZakupow`.

```text
Rysunek 1. Aplikacja po dodaniu trzech produktów

+---------------------------------------+
|            Lista zakupów              |  <- tło #2E7D32, tekst biały, 24
+---------------------------------------+
| Produkt [______________]  Ilość [-|+] |  <- Entry, Stepper 1–20
| [ DODAJ ]                             |
+---------------------------------------+
| [x] Chleb                     1 szt.  |  <- kupione: tekst przekreślony
| [ ] Mleko                     2 szt.  |
| [ ] Jabłka                    6 szt.  |
+---------------------------------------+
| Do kupienia: 2 z 3                    |
| [ USUŃ KUPIONE ]                      |
+---------------------------------------+
```

**Opis wyglądu i działania aplikacji**

1. Napis **Lista zakupów** na pasku u góry (tło `#2E7D32`, tekst biały, rozmiar `24`).
2. Pole edycyjne `entProdukt` z podpowiedzią **Nazwa produktu**, etykieta **Ilość: N** i `Stepper` (1–20, start 1).
3. Przycisk **DODAJ** dodaje produkt z podaną nazwą i ilością na **koniec** listy, czyści pole i ustawia stepper na 1. Pusta nazwa (lub same spacje) – komunikat **Podaj nazwę produktu**, nic nie jest dodawane.
4. Jeśli produkt o tej samej nazwie (bez względu na wielkość liter) jest już na liście, zamiast dodawać nowy, zwiększa się jego ilość.
5. Lista (`CollectionView`): pole wyboru, nazwa, ilość z dopiskiem **szt.**. Gdy pusta – napis **Lista jest pusta**.
6. Zaznaczenie pola wyboru oznacza produkt jako kupiony.
7. Etykieta **Do kupienia: X z Y** aktualizuje się po każdej zmianie.
8. Przycisk **USUŃ KUPIONE** pyta **Usunąć kupione produkty?** (Tak/Nie) i po potwierdzeniu usuwa z listy wszystkie zaznaczone.

**Założenia**

- klasa `Produkt` z polami: nazwa (tekst), ilość (liczba całkowita), kupiony (logiczne),
- kolekcja `ObservableCollection<Produkt>`, interfejs w XAML, układ bez nachodzenia elementów,
- obsługa zdarzeniami, kod czytelny, znaczące nazwy.

**Testy**

| Akcja | Oczekiwany wynik |
|---|---|
| dodaj „Chleb”, 1 | lista: Chleb 1 szt.; Do kupienia: 1 z 1 |
| dodaj „Mleko”, 2 i „Jabłka”, 6 | Do kupienia: 3 z 3 |
| dodaj „mleko”, 1 | Mleko 3 szt., nadal 3 pozycje |
| zaznacz Chleb | Do kupienia: 2 z 3 |
| dodaj „ ” (spacja) | komunikat Podaj nazwę produktu |
| USUŃ KUPIONE → Tak | zostają Mleko i Jabłka; Do kupienia: 2 z 2 |

??? question "Podpowiedź: usuwanie kilku elementów"
    Nie usuwaj elementów kolekcji w pętli `foreach` po tej samej kolekcji (wyjątek). Najpierw zrób kopię: `foreach (var p in produkty.Where(p => p.Kupiony).ToList()) produkty.Remove(p);`.

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

1. Kupione produkty mają przekreślony szary tekst – użyj `DataTrigger` na `Kupiony` w szablonie (`TextDecorations="Strikethrough"`).
2. Dodaj usuwanie pojedynczego produktu gestem przesunięcia: owiń szablon w `SwipeView` z `SwipeItem` **Usuń** (tło czerwone).

## Czy potrafię…?

- [ ] dodać i usunąć element `ObservableCollection`
- [ ] powiązać `CheckBox` w szablonie z właściwością obiektu
- [ ] policzyć elementy spełniające warunek (LINQ `Count`)
- [ ] bezpiecznie usunąć kilka elementów z kolekcji
