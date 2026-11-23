# Instrukcje dla Claude: materiały „Pracownia programowania aplikacji mobilnych”

Repozytorium z materiałami dla uczniów klasy IV technikum (technik programista), przedmiot „Pracownia programowania aplikacji mobilnych”: 64 h, lekcje po 45 min w pracowni. Przedmiot przygotowuje do kwalifikacji INF.04 (aplikacje mobilne w .NET MAUI: C#, XAML, emulator Androida, dane, sieć, testy i dokumentacja). Uczniowie pracują w Visual Studio Community 2026 z obciążeniem .NET MAUI (.NET 10 LTS).

## Źródła
- `docs/rozklad.md`: rozkład materiału (numer lekcji, temat, efekty, zakres P / P+ / ★). Nowe lekcje twórz zgodnie z nim.
- Podstawa programowa 2019 (Dz.U. 2019 poz. 991), technik programista 351406: INF.04.6 (efekty 1–2, kryteria 1–12), wybrane efekty INF.04.3 (6, 8, 9) i INF.04.8 (1–3).
- Informator CKE o egzaminie zawodowym, technik programista (aktualizacja 2022): część praktyczna INF.04 trwa 180 min (aplikacja konsolowa + aplikacja mobilna/desktopowa/webowa + dokumentacja lub testy).

## Zasady tworzenia lekcji
- Szablon: `szablony/lekcja.md`. Plik: `docs/<dział>/lekcja-NR.md` (NR dwucyfrowy), pliki startowe: `docs/pliki/lekcja-NR/`.
- Po dodaniu lekcji dopisz ją do `nav` w `mkdocs.yml`.
- Struktura 45 min: wprowadzenie ok. 10 min, zadanie główne ok. 25 min, podsumowanie i „Czy potrafię…?” ok. 5 min.
- Zadanie główne musi być wykonalne przez przeciętnego ucznia klasy IV w 25 min (pamiętaj, że pierwsze uruchomienie emulatora i kompilacja Androida trwają kilka minut). Zadanie dla chętnych zawsze dodatkowe.
- Treści spoza podstawy oznaczaj `<span class="zakres zakres-gw">★ poza egzaminem</span>`.
- Zadania w stylu egzaminu INF.04: rysunek ekranu aplikacji w ASCII, opis wyglądu i działania, założenia (kolory HEX, układ, nazwy kontrolek), tabela danych testowych, wymagane zrzuty ekranu i komentarz nagłówkowy według wzoru CKE.
- Kod: C# z nazwami po polsku lub angielsku (konsekwentnie w lekcji), interfejs w XAML, obsługa zdarzeń w `.xaml.cs` lub wiązanie danych. Nie używaj przestarzałych `ListView`, `Frame`, `Device.*`, `MessagingCenter`; zamiast nich `CollectionView`, `Border`, `DeviceInfo`/`MainThread`.
- Obliczenia w tabelach danych testowych sprawdzaj, uruchamiając kod (np. ekwiwalent w Pythonie).
- Obrazy, dźwięki i ikony generuj samodzielnie (Python/PIL, ffmpeg), bez zasobów z internetu.
- Język: polski, zwracanie się do ucznia na „ty”, krótkie zdania.
- Składnia MkDocs Material: ramki `!!! info|tip|warning`, zwijane `??? question`, klawisze `++f5++`, zakładki `=== "XAML"` / `=== "C#"`.

## Rozwiązania
Rozwiązań NIE umieszczaj w tym repozytorium (strona jest publiczna). Trafiają do osobnego, prywatnego repozytorium nauczyciela.

## Struktura repozytorium
- `docs/start/` lekcje 1–3, `docs/xaml/` 4–12, `docs/kontrolki/` 13–26, `docs/nawigacja/` 27–33, `docs/dane/` 34–47, `docs/jakosc/` 48–56, `docs/powtorka/` 57–64 (plik `lekcja-57.md` obejmuje lekcje 57–60, `lekcja-61.md` lekcje 61–64).
- Pliki startowe: `docs/pliki/lekcja-NN/`; wieloplikowe zestawy są spakowane w `.zip` (folder główny w archiwum ma nazwę zestawu, np. `galeria/`).
- Dane JSON do lekcji o sieci leżą w `docs/pliki/` i są dostępne pod adresem strony na GitHub Pages (stabilne „API” dla uczniów).

## Praca z poprawkami
- Polecenie `/popraw Lekcja NN: …` wprowadza poprawkę, sprawdza `mkdocs build --strict`, robi commit i push.
- Opis commita: `Lekcja NN: krótki opis zmiany`.
- Publikacja na GitHub Pages dzieje się automatycznie po pushu do `main` (`.github/workflows/deploy.yml`).
