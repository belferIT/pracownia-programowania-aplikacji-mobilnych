# Lekcja 46. Aparat i galeria zdjęć

<p class="lekcja-meta">Dział: Dane, sieć i usługi urządzenia · 45 min · Efekty: INF.04.6 (2) kryt. 7 · <span class="zakres zakres-gw">★ poza egzaminem</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- zrobić zdjęcie aparatem z poziomu aplikacji,
- wybrać zdjęcia z galerii,
- zapisać zdjęcie w folderze danych aplikacji i wyświetlić je.

## Wprowadzenie

Klasa `MediaPicker` otwiera systemową aplikację aparatu albo galerię i zwraca wybrany plik (`FileResult`).

```csharp
// zdjęcie z aparatu (null, gdy użytkownik anulował)
if (MediaPicker.Default.IsCaptureSupported)
{
    FileResult? zdjecie = await MediaPicker.Default.CapturePhotoAsync();
    if (zdjecie != null)
    {
        string sciezka = await ZapiszKopieAsync(zdjecie);
        imgPodglad.Source = ImageSource.FromFile(sciezka);
    }
}

// wybór z galerii (.NET 10: lista, także dla jednego zdjęcia)
List<FileResult> wybrane = await MediaPicker.Default.PickPhotosAsync(
    new MediaPickerOptions { SelectionLimit = 5, MaximumWidth = 1024 });

private static async Task<string> ZapiszKopieAsync(FileResult plik)
{
    string cel = Path.Combine(FileSystem.AppDataDirectory, plik.FileName);
    using Stream zrodlo = await plik.OpenReadAsync();
    using FileStream docelowy = File.OpenWrite(cel);
    await zrodlo.CopyToAsync(docelowy);
    return cel;
}
```

| Metoda (.NET 10) | Zwraca |
|---|---|
| `CapturePhotoAsync()` | `FileResult?` – zdjęcie z aparatu |
| `PickPhotosAsync(opcje)` | `List<FileResult>` – pusta, gdy anulowano |
| `MediaPickerOptions.SelectionLimit` | maks. liczba zdjęć (na Windows nieobsługiwane) |
| `MaximumWidth`, `CompressionQuality` | zmniejszenie zdjęcia przy wyborze |

!!! info "Starsze wersje"
    W .NET 8–9 wybór jednego zdjęcia to `PickPhotoAsync()`. W .NET 10 dokumentacja zaleca `PickPhotosAsync` także dla jednego zdjęcia.

!!! warning "Uprawnienia Android"
    W `AndroidManifest.xml` dodaj `<uses-permission android:name="android.permission.CAMERA" />` oraz wewnątrz `<manifest>` sekcję, która pozwala znaleźć aplikację aparatu:

    ```xml
    <queries>
        <intent>
            <action android:name="android.media.action.IMAGE_CAPTURE" />
        </intent>
    </queries>
    ```

!!! tip "Aparat w emulatorze"
    Emulator ma wirtualny aparat ze sceną 3D (poruszasz się klawiszami W, A, S, D i myszą z ++alt++). W ustawieniach emulatora (**Extended controls → Camera**) możesz wstawić własny obraz na ścianę sceny.

## Zadanie główne (25 min)

Utwórz projekt `Album`.

1. Dodaj uprawnienia i sekcję `queries` do manifestu.
2. Przyciski **Zrób zdjęcie** i **Wybierz z galerii** (do 5 zdjęć).
3. Każde zdjęcie jest kopiowane do `AppDataDirectory`, a ścieżka dodawana do `ObservableCollection<string>`.
4. Zdjęcia wyświetlaj w `CollectionView` jako siatkę 3 kolumn: `ItemsLayout="VerticalGrid, 3"`, miniatury 110×110, `Aspect="AspectFill"`.
5. Dotknięcie miniatury otwiera stronę z dużym zdjęciem i przyciskiem **Usuń** (usuwa plik `File.Delete` i pozycję z kolekcji).
6. Listę ścieżek zapisuj w `Preferences` (jako jeden tekst z separatorem `|` albo JSON), żeby album przetrwał ponowne uruchomienie.
7. Obsłuż anulowanie wyboru i brak aparatu.

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Dodaj przycisk **Udostępnij** na stronie zdjęcia: `await Share.Default.RequestAsync(new ShareFileRequest { Title = "Moje zdjęcie", File = new ShareFile(sciezka) });`. Dodaj też podpis zdjęcia zapisywany razem ze ścieżką (klasa `Zdjecie` i JSON).

## Czy potrafię…?

- [ ] zrobić zdjęcie aparatem i wybrać zdjęcia z galerii
- [ ] skopiować plik do folderu danych aplikacji
- [ ] wyświetlić zdjęcia w siatce `CollectionView`
- [ ] dodać uprawnienia i sekcję `queries` do manifestu
