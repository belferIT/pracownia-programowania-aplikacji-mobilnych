---
description: Wprowadź poprawkę w lekcji, sprawdź budowanie strony, zrób commit i push
argument-hint: "Lekcja NN: co poprawić"
---

Wprowadź w repozytorium poprawkę opisaną przez nauczyciela:

$ARGUMENTS

Postępuj tak:

1. Przeczytaj `CLAUDE.md` i plik lekcji, której dotyczy poprawka (`docs/*/lekcja-NN.md`). Lekcje 57–60 są w `docs/powtorka/lekcja-57.md`, 61–64 w `docs/powtorka/lekcja-61.md`.
2. Zmień tylko to, o co prosi nauczyciel. Jeśli poprawka dotyczy pliku startowego, zmień też plik w `docs/pliki/lekcja-NN/`. Archiwum `.zip` rozpakuj do katalogu tymczasowego, popraw i spakuj ponownie z tą samą strukturą folderów.
3. Jeśli poprawka zmienia dane w zadaniu z obliczeniami, przelicz ponownie tabelę z danymi testowymi.
4. Jeśli zmieniasz temat lekcji, zaktualizuj też `docs/rozklad.md` i tytuł w `nav` w `mkdocs.yml`.
5. Uruchom `mkdocs build --strict`. Jeśli są błędy, napraw je.
6. Pokaż krótko, co zmieniłeś (`git diff --stat` i 1–3 zdania opisu).
7. Zrób commit z opisem w formacie `Lekcja NN: krótki opis zmiany` i wykonaj `git push`.

Jeśli opis poprawki jest niejasny albo dotyczy kilku możliwych miejsc, najpierw zapytaj.
