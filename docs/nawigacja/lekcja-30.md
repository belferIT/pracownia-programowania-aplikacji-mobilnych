# Lekcja 30. Trasy, parametry i menu na pasku narzędzi

<p class="lekcja-meta">Dział: Nawigacja i platformy · 45 min · Efekty: INF.04.6 (2) kryt. 4, 6 · <span class="zakres zakres-p">INF.04</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- zarejestrować trasę i przejść do strony metodą `Shell.Current.GoToAsync`,
- przekazać parametr w adresie trasy i odebrać go (`QueryProperty`),
- dodać przyciski do paska narzędzi strony (`ToolbarItem`).

## Wprowadzenie

### Trasy

Strony, których nie ma w `AppShell.xaml` (np. szczegóły), rejestrujesz w konstruktorze `AppShell`:

```csharp
public AppShell()
{
    InitializeComponent();
    Routing.RegisterRoute(nameof(FilmPage), typeof(FilmPage));
}
```

```csharp
await Shell.Current.GoToAsync($"{nameof(FilmPage)}?id={film.Id}");  // przejdź z parametrem
await Shell.Current.GoToAsync("..");                                  // wróć
```

### Odbiór parametru

```csharp
[QueryProperty(nameof(FilmId), "id")]
public partial class FilmPage : ContentPage
{
    public int FilmId
    {
        set
        {
            Film? film = DaneKina.Filmy.FirstOrDefault(f => f.Id == value);
            BindingContext = film;
        }
    }

    public FilmPage()
    {
        InitializeComponent();
    }
}
```

!!! info "Obiekt zamiast tekstu"
    Parametry w adresie to tekst. Obiekt przekażesz słownikiem: `await Shell.Current.GoToAsync(nameof(FilmPage), new Dictionary<string, object> { ["film"] = film });` i odbierzesz `[QueryProperty(nameof(Film), "film")]` z właściwością typu `Film`.

### Pasek narzędzi

```xml
<ContentPage.ToolbarItems>
    <ToolbarItem Text="Szukaj" Order="Primary" Clicked="OnSzukajClicked" />
    <ToolbarItem Text="Ustawienia" Order="Secondary" Clicked="OnUstawieniaClicked" />
</ContentPage.ToolbarItems>
```

`Primary` – przycisk widoczny na pasku, `Secondary` – pozycja w menu „trzech kropek” (⋮) na Androidzie.

## Zadanie główne (25 min)

Rozbuduj projekt `Kino` z lekcji 29.

1. Dodaj klasę `Film` (`Id`, `Tytul`, `Gatunek`, `CzasTrwania` w minutach, `Opis`) i statyczną klasę `DaneKina` z listą `Filmy` (4 filmy, wymyślone tytuły).
2. Na `RepertuarPage` wyświetl filmy w `CollectionView` (tytuł, gatunek, czas **N min**).
3. Dodaj stronę `FilmPage` i zarejestruj trasę w `AppShell`.
4. Po wybraniu filmu przejdź do `FilmPage` z parametrem `id`. Strona pokazuje wszystkie dane filmu i czas w formacie **1 h 52 min** (`czas / 60` i `czas % 60`).
5. Na `FilmPage` przycisk **Kup bilet** przechodzi na zakładkę biletów: `await Shell.Current.GoToAsync("//Bilety");` (nadaj `FlyoutItem` atrybut `Route="Bilety"`).
6. Na `RepertuarPage` dodaj na pasku:
    - `ToolbarItem` **A–Z** (Primary): sortuje filmy alfabetycznie,
    - `ToolbarItem` **Najkrótsze** (Secondary): sortuje według czasu trwania.

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Zamiast `QueryProperty` użyj interfejsu `IQueryAttributable` i metody `ApplyQueryAttributes(IDictionary<string, object> query)`. Przekaż dwa parametry: `id` i `sala`, i wyświetl oba.

## Czy potrafię…?

- [ ] zarejestrować trasę strony
- [ ] przejść do strony z parametrem i wrócić (`".."`)
- [ ] odebrać parametr przez `QueryProperty`
- [ ] dodać przyciski `Primary` i `Secondary` na pasku narzędzi
