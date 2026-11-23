# Lekcja 25. Powtórka: aplikacja według projektu

<p class="lekcja-meta">Dział: Kontrolki i wiązanie danych · 45 min · Efekty: INF.04.6 (2) kryt. 5, 6, INF.04.3 (6) kryt. 1, 4 · <span class="zakres zakres-p">INF.04</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- przeanalizować wymagania klienta i przełożyć je na listę kontrolek,
- samodzielnie zaprojektować układ ekranu,
- połączyć `Picker`, `Image`, `Stepper`, `CheckBox` i okno dialogowe w jednej aplikacji.

## Wprowadzenie

Przed sprawdzianem ćwiczysz pracę **od wymagań do aplikacji**. Klient nie podaje nazw kontrolek – opisuje, czego potrzebuje. Twoim zadaniem jest dobrać kontrolki.

| Wymaganie klienta | Kontrolka |
|---|---|
| „wybór jednej pozycji z kilku” | `Picker` lub `RadioButton` |
| „tak / nie” | `Switch` lub `CheckBox` |
| „liczba sztuk, zwiększana przyciskami” | `Stepper` |
| „wartość z zakresu, płynnie” | `Slider` |
| „potwierdzenie przed wysłaniem” | `DisplayAlertAsync` z Tak/Nie |
| „zdjęcie produktu zmienia się po wyborze” | `Image` + zdarzenie `SelectedIndexChanged` |

!!! tip "Szkic na kartce"
    Zanim otworzysz Visual Studio, narysuj ekran na kartce (jak rysunki ASCII w zadaniach). Zaznacz nazwy kontrolek (`pckProdukt`, `imgProdukt`…). Oszczędzisz czas na egzaminie.

## Zadanie główne (25 min)

Pobierz i rozpakuj [kawiarnia.zip](../pliki/lekcja-25/kawiarnia.zip){ download }: `kawa.png`, `herbata.png`, `ciasto.png`.

!!! note "Wymagania klienta: kawiarnia „Pod Lipą”"
    „Potrzebujemy prostej aplikacji do zamawiania przy stoliku. Gość wybiera produkt: kawę (12 zł), herbatę (9 zł) albo ciasto (14 zł) – i od razu widzi jego zdjęcie. Ustawia liczbę sztuk (od 1 do 10). Może zaznaczyć, że zamówienie jest na wynos – wtedy doliczamy 1 zł do każdej sztuki za opakowanie. Cena ma się zmieniać na bieżąco. Po kliknięciu przycisku zamówienia aplikacja pyta, czy na pewno zamówić, a po potwierdzeniu pokazuje podziękowanie z kwotą. Kolory: brązowy `#4E342E` i kremowy `#FFF8E1`.”

1. Narysuj szkic ekranu i wpisz nazwy kontrolek. Pokaż szkic nauczycielowi.
2. Utwórz projekt `PodLipa` i wykonaj aplikację zgodnie z wymaganiami.
3. Cena przeliczana przy każdej zmianie produktu, liczby sztuk i pola „na wynos”, format **Do zapłaty: 30,00 zł**.
4. Przed wybraniem produktu obraz jest ukryty, a przycisk zamówienia nieaktywny.
5. Po potwierdzeniu zamówienia: komunikat **Dziękujemy! Zamówienie na kwotę 30,00 zł przyjęte.** i powrót do stanu początkowego.

| Produkt | Sztuk | Na wynos | Do zapłaty |
|---|---|---|---|
| kawa | 1 | nie | 12,00 zł |
| herbata | 3 | tak | 30,00 zł |
| ciasto | 2 | tak | 30,00 zł |
| kawa | 5 | nie | 60,00 zł |

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Pozwól zamówić kilka różnych produktów: przycisk **Dodaj do zamówienia** dodaje pozycję do listy (`CollectionView`) pod formularzem, a suma obejmuje wszystkie pozycje. Przycisk zamówienia wysyła całe zamówienie.

## Czy potrafię…?

- [ ] dobrać kontrolkę do opisu wymagania
- [ ] narysować szkic ekranu z nazwami kontrolek
- [ ] przeliczać wynik przy każdej zmianie danych
- [ ] przywrócić aplikację do stanu początkowego
