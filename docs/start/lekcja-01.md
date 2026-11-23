# Lekcja 1. BHP i organizacja pracy. Visual Studio 2026 z .NET MAUI

<p class="lekcja-meta">Dział: Start · 45 min · Efekty: INF.04.1, INF.04.6 (1) · <span class="zakres zakres-p">INF.04</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- wymienić zasady bezpiecznej pracy w pracowni komputerowej,
- sprawdzić, czy Visual Studio ma zainstalowane obciążenie .NET MAUI,
- odczytać wersję Visual Studio, .NET SDK i zainstalowanych obciążeń.

## Wprowadzenie

### Zasady pracy w pracowni

| Zasada | Dlaczego |
|---|---|
| Nie jesz i nie pijesz przy komputerze | Rozlany napój to zwarcie i zniszczony sprzęt |
| Nie dotykasz kabli zasilających i gniazd | Ryzyko porażenia prądem |
| Ekran w odległości 50–70 cm, górna krawędź na wysokości oczu | Mniejsze zmęczenie oczu i karku |
| Co godzinę 5 minut przerwy od ekranu (zasada 20-20-20: co 20 min patrz 20 s na coś odległego o 6 m) | Ochrona wzroku |
| Usterki zgłaszasz nauczycielowi, nie naprawiasz sam | Bezpieczeństwo i gwarancja sprzętu |
| Swoje projekty zapisujesz w folderze `C:\Projekty\Nazwisko_Imie` | Porządek i łatwe oddawanie prac |

### Środowisko pracy

Aplikacje mobilne tworzysz w **.NET MAUI** (*Multi-platform App UI*). Jeden projekt w C# i XAML uruchomisz na Androidzie, iOS, Windows i macOS.

| Element | Do czego służy |
|---|---|
| Visual Studio Community 2026 | środowisko IDE: edytor, kompilator, debugger, projektant |
| obciążenie **.NET MAUI** (*.NET Multi-platform App UI development*) | szablony projektów MAUI, Android SDK, emulator |
| .NET 10 SDK (LTS) | kompilator C# i biblioteki |
| Android Device Manager | tworzenie i uruchamianie emulatorów Androida |

!!! info "Podstawa programowa"
    Na egzaminie INF.04 dobierasz środowisko do zadania. Podstawa wymienia **Visual Studio**, **Android Studio** i **Xcode**. My używamy Visual Studio, bo w nim piszesz też aplikacje konsolowe i desktopowe w C#.

!!! warning "Wirtualizacja"
    Emulator Androida wymaga włączonej wirtualizacji sprzętowej (w BIOS/UEFI) i funkcji Windows **Platforma funkcji hypervisor systemu Windows**. W pracowni jest to już skonfigurowane. W domu możesz to sprawdzić w Menedżerze zadań → Wydajność → Procesor → Wirtualizacja.

## Zadanie główne (25 min)

1. Utwórz folder `C:\Projekty\Nazwisko_Imie` (wpisz swoje dane, bez polskich znaków i spacji).
2. Uruchom **Visual Studio Installer**. Przy Visual Studio Community 2026 kliknij **Modyfikuj** i sprawdź, czy zaznaczone jest obciążenie **.NET Multi-platform App UI development**. Niczego nie zmieniaj, zamknij okno przyciskiem **Zamknij**.
3. Uruchom Visual Studio. Otwórz **Pomoc → Informacje o programie Microsoft Visual Studio** i odczytaj numer wersji.
4. Otwórz **Narzędzia → Wiersz polecenia → Developer PowerShell** i wykonaj polecenia:

    ```powershell
    dotnet --version
    dotnet workload list
    ```

5. Otwórz **Narzędzia → Android → Android Device Manager** i sprawdź, czy jest już utworzony jakiś emulator.
6. W folderze `C:\Projekty\Nazwisko_Imie` utwórz plik `srodowisko.txt` i uzupełnij go według wzoru:

    ```text
    System operacyjny: Windows 11 ...
    Visual Studio: Community 2026, wersja ...
    .NET SDK: ...
    Obciążenia: maui-android ..., maui-windows ...
    Emulator: (nazwa lub "brak")
    ```

7. Ustaw sobie wygodne środowisko: **Narzędzia → Opcje → Środowisko → Ogólne**, motyw jasny lub ciemny. Włącz numery wierszy w edytorze (**Edytor tekstu → Wszystkie języki → Numery wierszy**).

??? question "Podpowiedź: polecenie dotnet nie działa"
    Zamknij okno i otwórz **Developer PowerShell** z menu Visual Studio, a nie zwykły PowerShell. Jeśli dalej nie działa, zgłoś to nauczycielowi.

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Wykonaj polecenie `dotnet --info` i znajdź w wyniku: architekturę procesora (`RID`), ścieżkę instalacji SDK i listę zainstalowanych środowisk uruchomieniowych (*runtimes*). Dopisz je do pliku `srodowisko.txt`.

## Czy potrafię…?

- [ ] wymienić 4 zasady bezpiecznej pracy przy komputerze
- [ ] sprawdzić w Visual Studio Installer, jakie obciążenia są zainstalowane
- [ ] odczytać wersję .NET SDK poleceniem `dotnet --version`
- [ ] wyjaśnić, czym jest .NET MAUI
