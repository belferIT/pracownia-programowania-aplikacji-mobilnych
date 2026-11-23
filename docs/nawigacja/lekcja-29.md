# Lekcja 29. Shell: zakładki i menu wysuwane

<p class="lekcja-meta">Dział: Nawigacja i platformy · 45 min · Efekty: INF.04.6 (2) kryt. 4, 6 · <span class="zakres zakres-p">INF.04</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- zbudować aplikację z dolnymi zakładkami (`TabBar`),
- zbudować aplikację z menu wysuwanym z boku (`Flyout`),
- dodać do menu pozycję wykonującą akcję (`MenuItem`).

## Wprowadzenie

`AppShell.xaml` opisuje **strukturę** aplikacji. Strony w nim nie są tworzone od razu – `DataTemplate` tworzy stronę dopiero przy pierwszym wejściu.

=== "Zakładki (TabBar)"

    ```xml
    <Shell xmlns="http://schemas.microsoft.com/dotnet/2021/maui"
           xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
           xmlns:local="clr-namespace:Kino"
           x:Class="Kino.AppShell">
        <TabBar>
            <ShellContent Title="Repertuar" ContentTemplate="{DataTemplate local:RepertuarPage}" />
            <ShellContent Title="Bilety" ContentTemplate="{DataTemplate local:BiletyPage}" />
            <ShellContent Title="Kontakt" ContentTemplate="{DataTemplate local:KontaktPage}" />
        </TabBar>
    </Shell>
    ```

=== "Menu wysuwane (Flyout)"

    ```xml
    <Shell ... Shell.FlyoutBehavior="Flyout" FlyoutBackgroundColor="#EDE7F6">
        <Shell.FlyoutHeader>
            <Label Text="Kino Kadr" FontSize="28" Padding="20" BackgroundColor="#4527A0"
                   TextColor="White" />
        </Shell.FlyoutHeader>

        <FlyoutItem Title="Repertuar">
            <ShellContent ContentTemplate="{DataTemplate local:RepertuarPage}" />
        </FlyoutItem>
        <FlyoutItem Title="Bilety">
            <ShellContent ContentTemplate="{DataTemplate local:BiletyPage}" />
        </FlyoutItem>

        <MenuItem Text="O aplikacji" Clicked="OnOAplikacjiClicked" />
    </Shell>
    ```

| Element | Znaczenie |
|---|---|
| `TabBar` | dolne zakładki; menu boczne jest wyłączone |
| `FlyoutItem` | pozycja menu bocznego (ikona ☰ w pasku) |
| `Tab` w `FlyoutItem` | zakładki **wewnątrz** pozycji menu |
| `MenuItem` | pozycja menu, która wykonuje akcję zamiast otwierać stronę |
| `Shell.FlyoutHeader`, `Shell.FlyoutFooter` | nagłówek i stopka menu |
| `Icon="ikona.png"` | ikona zakładki lub pozycji menu (z `Resources/Images`) |

!!! info "Egzamin"
    Wśród możliwych zadań INF.04 jest „implementacja aplikacji mobilnej z systemem menu i przechodzeniem do podstron”. `Shell` z `Flyout` lub `TabBar` to najszybszy sposób, aby je wykonać w MAUI.

## Zadanie główne (25 min)

Utwórz projekt `Kino`.

1. Dodaj trzy strony: `RepertuarPage`, `BiletyPage`, `KontaktPage`. Na każdej nagłówek z jej nazwą i krótka treść (repertuar: 3 filmy z godzinami; bilety: tabela cen w `Grid`: normalny 28 zł, ulgowy 22 zł, rodzinny 80 zł; kontakt: adres i telefon).
2. W `AppShell.xaml` zastąp domyślną zawartość dolnymi zakładkami z trzema stronami. Uruchom aplikację.
3. Zmień strukturę na **menu wysuwane**: trzy `FlyoutItem`, nagłówek menu z nazwą **Kino Kadr** (tło `#4527A0`, tekst biały), tło menu `#EDE7F6`.
4. Dodaj `MenuItem` **O aplikacji**, który wyświetla komunikat z nazwą i wersją aplikacji (metoda w `AppShell.xaml.cs`: `await DisplayAlertAsync(...)`).
5. Dodaj w `Shell.FlyoutFooter` etykietę **Autor: Imię Nazwisko**.
6. Kolory paska tytułu ustaw w `Shell`: `Shell.BackgroundColor="#4527A0"`, `Shell.ForegroundColor="White"`, `Shell.TitleColor="White"`.

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Połącz oba sposoby: pozycja menu **Repertuar** ma w środku dwie zakładki (`Tab`): **Dziś** i **Jutro**, każda z osobną stroną. Dodaj ikony zakładek narysowane w Inkscape (SVG, 24×24) – w XAML odwołujesz się do nich z rozszerzeniem `.png`.

## Czy potrafię…?

- [ ] zbudować dolne zakładki w `AppShell.xaml`
- [ ] zbudować menu wysuwane z nagłówkiem i stopką
- [ ] dodać pozycję menu wykonującą akcję
- [ ] ustawić kolory paska tytułu w `Shell`
