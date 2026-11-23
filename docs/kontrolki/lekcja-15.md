# Lekcja 15. Picker, DatePicker i TimePicker

<p class="lekcja-meta">Dział: Kontrolki i wiązanie danych · 45 min · Efekty: INF.04.6 (2) kryt. 6, 7 · <span class="zakres zakres-p">INF.04</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- utworzyć listę wyboru `Picker` i odczytać wybraną pozycję,
- pobrać datę i godzinę od użytkownika,
- ograniczyć zakres dat i sprawdzić poprawność godziny.

## Wprowadzenie

### Picker (lista rozwijana, *spinner*)

```xml
<Picker x:Name="pckSala" Title="Wybierz salę" SelectedIndexChanged="OnSalaWybrana">
    <Picker.Items>
        <x:String>Sala główna</x:String>
        <x:String>Ogródek</x:String>
        <x:String>Antresola</x:String>
    </Picker.Items>
</Picker>
```

```csharp
if (pckSala.SelectedIndex == -1)          // nic nie wybrano
{
    lblInfo.Text = "Wybierz salę";
    return;
}
string sala = pckSala.SelectedItem.ToString()!;
```

Listę możesz też wypełnić w C#: `pckSala.ItemsSource = new List<string> { "A", "B" };`.

### DatePicker i TimePicker

```xml
<DatePicker x:Name="dpData" Format="dd.MM.yyyy" DateSelected="OnDataWybrana" />
<TimePicker x:Name="tpGodzina" Format="HH:mm" Time="18:00" TimeSelected="OnGodzinaWybrana" />
```

```csharp
public MainPage()
{
    InitializeComponent();
    dpData.MinimumDate = DateTime.Today;
    dpData.MaximumDate = DateTime.Today.AddDays(30);
}

// w .NET 10 Date i Time mogą mieć wartość null (nic nie wybrano)
DateTime data = dpData.Date ?? DateTime.Today;
TimeSpan godzina = tpGodzina.Time ?? TimeSpan.Zero;
```

| Format | Wynik |
|---|---|
| `dd.MM.yyyy` | 05.03.2027 |
| `dddd, d MMMM` | piątek, 5 marca (język systemu) |
| `HH:mm` | 18:30 (zegar 24-godzinny) |

!!! info "Porównywanie godzin"
    `TimeSpan` porównujesz zwykłymi operatorami: `godzina >= new TimeSpan(12, 0, 0)`. Liczbę dni między datami da odejmowanie: `(data - DateTime.Today).Days`.

## Zadanie główne (25 min)

Utwórz projekt `RezerwacjaStolika`.

1. Nagłówek **Rezerwacja stolika**, tło `#4527A0`, tekst biały.
2. `Picker` `pckSala` z salami: **Sala główna**, **Ogródek**, **Antresola**.
3. `Picker` `pckOsoby` z liczbą osób od 1 do 8, wypełniony w konstruktorze pętlą `for`.
4. `DatePicker` `dpData`: format `dd.MM.yyyy`, najwcześniej dziś, najpóźniej za 30 dni.
5. `TimePicker` `tpGodzina`: format `HH:mm`, domyślnie `18:00`.
6. Przycisk **Zarezerwuj** i etykieta `lblPotwierdzenie`.
7. Po kliknięciu przycisku sprawdź:
    1. czy wybrano salę i liczbę osób – jeśli nie: **Wybierz salę i liczbę osób**,
    2. czy godzina jest w przedziale 12:00–21:00 – jeśli nie: **Rezerwacje przyjmujemy od 12:00 do 21:00**,
    3. czy w **Ogródku** rezerwacja jest dla maksymalnie 4 osób – jeśli nie: **W ogródku są stoliki do 4 osób**.
8. Jeśli wszystko się zgadza, wypisz: **Rezerwacja: Sala główna, 4 os., 12.12.2026, godz. 18:00. Do wizyty zostało N dni.**

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Zablokuj rezerwacje w poniedziałki (`data.DayOfWeek == DayOfWeek.Monday`) z komunikatem **W poniedziałki restauracja jest nieczynna**. Dodaj też informację o dniu tygodnia w potwierdzeniu, np. **(sobota)** – użyj `data.ToString("dddd")`.

## Czy potrafię…?

- [ ] wypełnić `Picker` w XAML i w C#
- [ ] sprawdzić, czy użytkownik coś wybrał (`SelectedIndex`)
- [ ] ograniczyć zakres dat w `DatePicker`
- [ ] porównać godzinę z przedziałem
