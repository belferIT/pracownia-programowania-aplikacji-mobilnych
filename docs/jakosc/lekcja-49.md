# Lekcja 49. MVVM z CommunityToolkit.Mvvm

<p class="lekcja-meta">Dział: Jakość, testy i publikacja · 45 min · Efekty: INF.04.3 (8) · <span class="zakres zakres-gw">★ poza egzaminem</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- dodać do projektu pakiet `CommunityToolkit.Mvvm`,
- skrócić ViewModel dzięki atrybutom `[ObservableProperty]` i `[RelayCommand]`,
- zablokować polecenie, gdy nie można go wykonać (`CanExecute`).

## Wprowadzenie

W lekcji 48 każda właściwość miała pole, getter, setter i wywołanie `OnPropertyChanged`. Pakiet **CommunityToolkit.Mvvm** (Microsoft, licencja MIT) generuje ten kod sam podczas kompilacji. Dodajesz go przez **Projekt → Zarządzaj pakietami NuGet → Przeglądaj**.

| Zapis z pakietem | Co powstaje podczas kompilacji |
|---|---|
| `partial class ...VM : ObservableObject` | klasa z gotowym `INotifyPropertyChanged` |
| `[ObservableProperty] private string tytul = "";` | właściwość `Tytul` z powiadomieniem |
| `[NotifyPropertyChangedFor(nameof(Podsumowanie))]` | powiadomienie także o innej właściwości |
| `[RelayCommand] private void Dodaj()` | właściwość `DodajCommand` |
| `[RelayCommand(CanExecute = nameof(MoznaDodac))]` | polecenie aktywne tylko gdy `MoznaDodac` zwraca `true` |
| `[NotifyCanExecuteChangedFor(nameof(DodajCommand))]` | po zmianie pola przycisk sprawdza, czy ma być aktywny |

```csharp
using System.Collections.ObjectModel;
using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;

namespace Zadania;

public partial class ListaViewModel : ObservableObject
{
    [ObservableProperty]
    [NotifyCanExecuteChangedFor(nameof(DodajCommand))]
    private string nowyTytul = "";

    public ObservableCollection<string> Zadania { get; } = new();

    public string Podsumowanie => $"Zadań: {Zadania.Count}";

    private bool MoznaDodac() => !string.IsNullOrWhiteSpace(NowyTytul);

    [RelayCommand(CanExecute = nameof(MoznaDodac))]
    private void Dodaj()
    {
        Zadania.Add(NowyTytul.Trim());
        NowyTytul = "";
        OnPropertyChanged(nameof(Podsumowanie));
    }
}
```

!!! warning "Częste błędy"
    - Klasa musi być `partial`, inaczej generator nie może jej uzupełnić.
    - Pole piszesz małą literą (`nowyTytul`), a w XAML wiążesz **właściwość** wielką literą (`NowyTytul`).
    - Metoda `Dodaj` daje polecenie `DodajCommand`, a metoda `DodajAsync` też daje `DodajCommand` (bez `Async`).

!!! info "Nowszy zapis"
    W nowszych wersjach pakietu możesz pisać `[ObservableProperty] public partial string NowyTytul { get; set; }`. Na Windows kompilator może proponować ten zapis ostrzeżeniem MVVMTK0045. Oba zapisy działają, na lekcji używamy pól.

## Zadanie główne (25 min)

Utwórz projekt `Zadania`, dodaj pakiet `CommunityToolkit.Mvvm` i klasę `ListaViewModel` z przykładu.

```text
+-------------------------------------+
|  Moje zadania                       |
+-------------------------------------+
|  [ nowe zadanie        ] [ DODAJ ]  |  <- DODAJ nieaktywny przy pustym polu
|  Zadań: 3                           |
+-------------------------------------+
|  Kupić mleko                 [ X ]  |
|  Projekt z MAUI              [ X ]  |
|  Trening                     [ X ]  |
+-------------------------------------+
|  [        USUŃ WSZYSTKIE          ] |
+-------------------------------------+
```

1. Ustaw `BindingContext = new ListaViewModel();` i zbuduj widok według rysunku. `Entry` wiąż z `NowyTytul`, przycisk **DODAJ** z `DodajCommand`.
2. Sprawdź, że przycisk **DODAJ** jest szary, gdy pole jest puste lub zawiera same spacje.
3. Dodaj polecenie `Usun(string zadanie)` z atrybutem `[RelayCommand]`. Przycisk **X** w szablonie elementu listy wywołuje je z parametrem `{Binding .}` (cały element).
4. Dodaj polecenie **USUŃ WSZYSTKIE**, aktywne tylko wtedy, gdy lista nie jest pusta. Po każdej zmianie listy wywołaj `UsunWszystkieCommand.NotifyCanExecuteChanged()`.
5. Etykieta **Zadań: N** zmienia się po każdym dodaniu i usunięciu.
6. W pliku `MainPage.xaml.cs` nie ma żadnej metody obsługi zdarzenia.

??? question "Podpowiedź: polecenie z ViewModelu w szablonie elementu"
    Wewnątrz `DataTemplate` kontekstem jest pojedynczy element (tekst zadania), a nie ViewModel. Wskaż ViewModel przez przodka:
    ```xml
    <Button Text="X"
            Command="{Binding Source={RelativeSource AncestorType={x:Type vm:ListaViewModel}},
                              Path=UsunCommand}"
            CommandParameter="{Binding .}" />
    ```

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Zamień `string` na klasę `Zadanie : ObservableObject` z polami `[ObservableProperty]` `tytul` i `wykonane`. Dodaj `CheckBox` przy każdym zadaniu, a podsumowanie zmień na **Wykonano 2 z 5**. Wskazówka: po zmianie `Wykonane` ViewModel musi dowiedzieć się o zmianie, np. przez zdarzenie `PropertyChanged` każdego zadania.

## Czy potrafię…?

- [ ] dodać pakiet NuGet do projektu
- [ ] zamienić ręczną właściwość z powiadomieniem na `[ObservableProperty]`
- [ ] utworzyć polecenie atrybutem `[RelayCommand]`
- [ ] zablokować przycisk przez `CanExecute` i odświeżyć jego stan
