# Lekcja 55. Przygotowanie do publikacji: podpisany plik APK/AAB, Google Play

<p class="lekcja-meta">Dział: Jakość, testy i publikacja · 45 min · Efekty: INF.04.6 (2) kryt. 12 · <span class="zakres zakres-p">INF.04</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- odróżnić kompilację **Debug** od **Release**,
- utworzyć klucz do podpisywania aplikacji,
- zbudować podpisany plik APK i zainstalować go w emulatorze,
- wymienić kroki publikacji aplikacji w sklepie Google Play.

## Wprowadzenie

Do tej pory uruchamiałeś aplikację w trybie **Debug**: Visual Studio instaluje ją w emulatorze razem z danymi do debugowania. Aplikacja dla użytkowników powstaje w trybie **Release**: jest mniejsza, szybsza i **podpisana** kluczem autora.

| Plik | Do czego |
|---|---|
| **APK** (*Android Package*) | instalacja bezpośrednio na telefonie lub w emulatorze, testy, dystrybucja poza sklepem |
| **AAB** (*Android App Bundle*) | wysyłka do Google Play; sklep sam przygotowuje z niego APK dla konkretnych telefonów |
| **keystore** (magazyn kluczy) | plik z kluczem prywatnym; każda aktualizacja aplikacji musi być podpisana **tym samym** kluczem |

!!! warning "Klucz to jak hasło do konta bankowego"
    Zgubiony klucz (albo hasło do niego) oznacza, że nie wydasz aktualizacji aplikacji. Wykradziony klucz pozwala podszyć się pod Ciebie. Nie wysyłaj pliku `.keystore` do repozytorium ani nikomu. Zrób kopię zapasową w bezpiecznym miejscu.

**Podpisywanie w Visual Studio:**

1. Na pasku narzędzi wybierz **Release** i urządzenie z Androidem.
2. Prawy przycisk na projekcie → **Publikuj…** (*Publish*). Otworzy się **Menedżer archiwów** i zbuduje archiwum.
3. **Distribute… → Ad Hoc** → **+** (nowa tożsamość podpisywania): alias, hasło, imię i nazwisko, organizacja.
4. **Save As** zapisuje podpisany plik APK.

**To samo z wiersza poleceń** (Terminal w Visual Studio: **Widok → Terminal**):

```powershell
# 1. klucz (jednorazowo); keytool jest częścią JDK instalowanego z Visual Studio
keytool -genkeypair -v -keystore napiwek.keystore -alias napiwek -keyalg RSA -keysize 2048 -validity 10000

# 2. podpisany APK
dotnet publish -f net10.0-android -c Release -p:AndroidPackageFormats=apk `
  -p:AndroidKeyStore=true -p:AndroidSigningKeyStore=napiwek.keystore `
  -p:AndroidSigningKeyAlias=napiwek -p:AndroidSigningKeyPass=HASLO -p:AndroidSigningStorePass=HASLO
```

Gotowy plik znajdziesz w `bin/Release/net10.0-android/publish/` (nazwa kończy się na `-Signed.apk`).

**Publikacja w Google Play** – kroki:

1. Konto dewelopera Google Play (jednorazowa opłata, weryfikacja tożsamości; osoba niepełnoletnia potrzebuje konta rodzica lub opiekuna).
2. Utworzenie aplikacji w **Google Play Console**: nazwa, język, darmowa czy płatna.
3. Karta sklepu: opis krótki i pełny, ikona 512 × 512 px, grafika 1024 × 500 px, zrzuty ekranu z telefonu.
4. **Polityka prywatności** (adres strony WWW) i ankieta o danych użytkownika, klasyfikacja treści (wiek), grupa docelowa.
5. Wysłanie pliku **AAB** na ścieżkę testów (wewnętrzne, zamknięte), a po testach – do produkcji. Nowe konta osobiste muszą najpierw przeprowadzić testy zamknięte z grupą testerów przez określony czas – sprawdź aktualne wymagania w Play Console.
6. Przegląd aplikacji przez Google (od kilku godzin do kilku dni).

!!! info "Uprawnienia i prywatność"
    Każde uprawnienie w `AndroidManifest.xml` (lokalizacja, aparat) musisz uzasadnić w Play Console. Usuń uprawnienia, z których aplikacja nie korzysta.

## Zadanie główne (25 min)

Pracujesz na projekcie `Napiwek` (z ikoną i wersją z lekcji 54) albo innym własnym projekcie.

1. Przełącz konfigurację na **Release** i uruchom aplikację w emulatorze. Porównaj czas startu z trybem **Debug**.
2. Utwórz klucz `napiwek.keystore` (Visual Studio albo `keytool`). Zapisz alias i hasło w bezpiecznym miejscu – **nie** w folderze projektu.
3. Zbuduj podpisany plik APK.
4. Odinstaluj aplikację z emulatora. Przeciągnij plik `.apk` na okno emulatora, aby go zainstalować. Uruchom aplikację z ikony.
5. Sprawdź w emulatorze **Ustawienia → Aplikacje → Napiwek** numer wersji i rozmiar aplikacji.
6. Przygotuj w edytorze tekstu dokument `karta-sklepu`: krótki opis (do 80 znaków), pełny opis (3–5 zdań), lista uprawnień z uzasadnieniem, kategoria aplikacji, dwa zrzuty ekranu.

??? question "Podpowiedź: `keytool` nie jest rozpoznawany"
    `keytool` leży w folderze `bin` pakietu JDK. W Visual Studio sprawdzisz ścieżkę w **Narzędzia → Opcje → Xamarin/.NET MAUI → Ustawienia systemu Android → Lokalizacja Java Development Kit**. Możesz też użyć kreatora podpisywania w Visual Studio.

??? question "Podpowiedź: „App not installed” przy instalacji APK"
    Najczęściej w emulatorze jest już aplikacja o tym samym `ApplicationId` podpisana innym kluczem (np. debugowa wersja). Odinstaluj ją i spróbuj ponownie.

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Zbuduj plik **AAB** (bez parametru `AndroidPackageFormats=apk`) i porównaj jego rozmiar z APK. Dowiedz się, czym jest **Play App Signing** i dlaczego Google przechowuje własny klucz do podpisywania aplikacji wysłanych do sklepu.

## Czy potrafię…?

- [ ] wyjaśnić różnicę między trybem Debug i Release
- [ ] wyjaśnić różnicę między APK i AAB
- [ ] utworzyć klucz i zbudować podpisaną aplikację
- [ ] zainstalować plik APK w emulatorze
- [ ] wymienić kroki publikacji aplikacji w Google Play
