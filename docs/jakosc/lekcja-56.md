# Lekcja 56. Git i GitHub w projekcie MAUI

<p class="lekcja-meta">Dział: Jakość, testy i publikacja · 45 min · Efekty: INF.04.3 (5) · <span class="zakres zakres-gw">★ poza egzaminem</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- utworzyć repozytorium Git dla projektu .NET MAUI z poprawnym plikiem `.gitignore`,
- zapisywać zmiany w commitach z dobrymi opisami,
- przywrócić poprzednią wersję pliku,
- wysłać projekt na GitHub.

## Wprowadzenie

**Git** zapisuje historię zmian w projekcie. Każdy **commit** to migawka plików z opisem. Możesz wrócić do dowolnej wersji, porównać zmiany i pracować w zespole. **GitHub** to serwis, w którym trzymasz kopię repozytorium w internecie.

| Polecenie | Co robi |
|---|---|
| `git init` | tworzy repozytorium w bieżącym folderze |
| `git status` | pokazuje zmienione i nowe pliki |
| `git add .` | dodaje zmiany do następnego commita |
| `git commit -m "opis"` | zapisuje commit |
| `git log --oneline` | historia commitów |
| `git diff` | zmiany, które nie są jeszcze w commicie |
| `git restore plik` | cofa niezapisane zmiany w pliku |
| `git push` | wysyła commity na GitHub |

!!! warning "Czego nie wysyłać do repozytorium"
    Foldery `bin/` i `obj/` (wynik kompilacji, setki MB), `.vs/` (ustawienia Visual Studio), pliki `*.keystore` (klucz z lekcji 55), hasła i klucze API. Plik `.gitignore` z szablonu Visual Studio wyklucza większość z nich. Wygenerujesz go poleceniem `dotnet new gitignore`.

!!! tip "Dobry opis commita"
    Krótko, w trybie rozkazującym, co zmienia commit: **Dodaj przycisk WYCZYŚĆ**, **Popraw zaokrąglenie kwoty na osobę**. Złe opisy: „zmiany”, „asdf”, „działa!!!”.

Visual Studio ma wbudowaną obsługę Gita: menu **Git** i okno **Zmiany Git** (*Git Changes*). Commit robisz tam przyciskiem **Zatwierdź wszystko**, a wysyłasz strzałką **Wypchnij**.

## Zadanie główne (25 min)

Pracujesz na projekcie `Napiwek` albo innym własnym projekcie. Jeśli nie masz konta GitHub, wykonaj kroki 1–6 lokalnie.

1. Otwórz terminal w folderze rozwiązania (**Widok → Terminal**). Przy pierwszym użyciu Gita ustaw swoje dane:
    ```powershell
    git config --global user.name "Imię Nazwisko"
    git config --global user.email "adres@example.com"
    ```
2. Utwórz plik `.gitignore` (`dotnet new gitignore`) i dopisz na końcu wiersz `*.keystore`. Wykonaj `git init`.
3. Sprawdź `git status`. Na liście **nie może** być folderów `bin`, `obj` ani `.vs`. Wykonaj pierwszy commit **Pierwsza wersja aplikacji Napiwek**.
4. Wprowadź w aplikacji trzy małe zmiany (np. kolor paska, nowy przycisk 25%, tekst w **O aplikacji**). Po każdej zmianie zrób osobny commit z dobrym opisem. Użyj raz terminala, a raz okna **Zmiany Git**.
5. Zepsuj celowo plik `MainPage.xaml` (usuń kilka wierszy) i przywróć go poleceniem `git restore MainPage.xaml`.
6. Wyświetl historię `git log --oneline` i zrób zrzut ekranu.
7. Na GitHub utwórz puste repozytorium `napiwek` (bez README). W Visual Studio: **Git → Wypchnij do usługi Git** albo w terminalu polecenia, które pokaże GitHub (`git remote add origin …`, `git push -u origin main`). Sprawdź w przeglądarce, że w repozytorium nie ma folderów `bin` i `obj`.

??? question "Podpowiedź: `bin` i `obj` trafiły do commita"
    Plik `.gitignore` dodano za późno. Usuń foldery z repozytorium (pliki na dysku zostaną):
    ```powershell
    git rm -r --cached bin obj
    git commit -m "Usuń wyniki kompilacji z repozytorium"
    ```

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Utwórz gałąź `tryb-ciemny` (`git switch -c tryb-ciemny`), dodaj w niej obsługę trybu ciemnego (lekcja 33) w dwóch commitach i połącz ją z gałęzią główną (`git switch main`, `git merge tryb-ciemny`). Na GitHub dodaj plik `README.md` z opisem aplikacji i zrzutem ekranu.

## Czy potrafię…?

- [ ] utworzyć repozytorium z plikiem `.gitignore` dla projektu .NET
- [ ] zrobić commit z dobrym opisem w terminalu i w Visual Studio
- [ ] przywrócić plik do ostatniej zapisanej wersji
- [ ] wysłać repozytorium na GitHub
- [ ] wymienić pliki, których nie wysyła się do repozytorium
