# Lekcja 28. Przekazywanie danych między stronami

<p class="lekcja-meta">Dział: Nawigacja i platformy · 45 min · Efekty: INF.04.6 (2) kryt. 6 · <span class="zakres zakres-p">INF.04</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- przekazać obiekt do nowej strony przez konstruktor,
- wyświetlić szczegóły elementu wybranego z listy,
- zmienić dane na drugiej stronie tak, aby zmiana była widoczna na pierwszej.

## Wprowadzenie

Najprostszy sposób: nowa strona ma **konstruktor z parametrem**.

=== "SzczegolyPage.xaml.cs"

    ```csharp
    public partial class SzczegolyPage : ContentPage
    {
        private readonly Kontakt kontakt;

        public SzczegolyPage(Kontakt kontakt)
        {
            InitializeComponent();
            this.kontakt = kontakt;
            BindingContext = kontakt;      // wiązania na stronie pokażą dane kontaktu
        }
    }
    ```

=== "MainPage.xaml.cs"

    ```csharp
    private async void OnKontaktWybrany(object? sender, SelectionChangedEventArgs e)
    {
        if (e.CurrentSelection.FirstOrDefault() is Kontakt k)
        {
            await Navigation.PushAsync(new SzczegolyPage(k));
            cvKontakty.SelectedItem = null;
        }
    }
    ```

!!! info "Ten sam obiekt na dwóch stronach"
    Do strony szczegółów trafia **referencja** do tego samego obiektu, który jest na liście. Jeśli zmienisz jego właściwość (a klasa ma `INotifyPropertyChanged`), lista na pierwszej stronie odświeży się sama po powrocie.

| Sposób | Kiedy |
|---|---|
| parametr konstruktora | prosta aplikacja, przekazanie obiektu |
| wspólna klasa statyczna / usługa | dane potrzebne na wielu stronach |
| parametry trasy `Shell` (`?id=3`) | nawigacja przez `GoToAsync` (lekcja 30) |

## Zadanie główne (25 min)

Utwórz projekt `Kontakty`.

1. Klasa `Kontakt` z `INotifyPropertyChanged`: `Imie`, `Nazwisko`, `Telefon`, `Ulubiony` (`bool`) oraz właściwość tylko do odczytu `PelneImie` (imię i nazwisko).
2. Strona główna: lista `CollectionView` 5 kontaktów (wymyślone dane). Każdy element: pełne imię (pogrubione) i telefon. Ulubione mają przed imieniem gwiazdkę ★ (wskazówka: `DataTrigger` albo właściwość `Gwiazdka` zwracająca `"★ "` lub `""`).
3. Po wybraniu kontaktu otwiera się `SzczegolyPage` z przekazanym obiektem. Tytuł strony: pełne imię.
4. Strona szczegółów: pola `Entry` powiązane (`Mode=TwoWay`) z imieniem, nazwiskiem i telefonem, `Switch` **Ulubiony**.
5. Po zmianie danych i powrocie na listę widać nowe wartości (bez przeładowywania listy).
6. Na stronie szczegółów przycisk **Usuń kontakt**: pyta o potwierdzenie, usuwa kontakt z kolekcji i wraca na listę. Kolekcję przekaż do strony jako drugi parametr konstruktora.

??? question "Podpowiedź: PelneImie nie odświeża się"
    W seterach `Imie` i `Nazwisko` wywołaj także `OnPropertyChanged(nameof(PelneImie));`.

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Dodaj na stronie szczegółów przycisk **Zadzwoń**, który otwiera aplikację telefonu z numerem: `PhoneDialer.Default.Open(kontakt.Telefon);`. Na Androidzie 11+ trzeba dodać do `AndroidManifest.xml` sekcję `<queries>` z akcją `android.intent.action.DIAL` (sprawdź w dokumentacji „Phone dialer”).

## Czy potrafię…?

- [ ] przekazać obiekt do strony przez konstruktor
- [ ] ustawić `BindingContext` na przekazany obiekt
- [ ] wyjaśnić, dlaczego zmiana jest widoczna na pierwszej stronie
- [ ] usunąć element z kolekcji na innej stronie
