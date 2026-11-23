# Lekcja 13. Przełączniki: Switch, CheckBox, RadioButton

<p class="lekcja-meta">Dział: Kontrolki i wiązanie danych · 45 min · Efekty: INF.04.6 (2) kryt. 4, 6 · <span class="zakres zakres-p">INF.04</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- użyć przełącznika `Switch`, pola wyboru `CheckBox` i przycisków opcji `RadioButton`,
- odczytać ich stan w C# i reagować na jego zmianę,
- pogrupować przyciski opcji tak, aby wybrać tylko jeden.

## Wprowadzenie

| Kontrolka | Stan | Zdarzenie | Typowe użycie |
|---|---|---|---|
| `Switch` | `IsToggled` (`bool`) | `Toggled` → `e.Value` | włącz / wyłącz (tryb ciemny, powiadomienia) |
| `CheckBox` | `IsChecked` (`bool`) | `CheckedChanged` → `e.Value` | dodatki, zgody; można zaznaczyć wiele |
| `RadioButton` | `IsChecked` (`bool`) | `CheckedChanged` → `e.Value` | jeden wybór z grupy (`GroupName`) |

```xml
<HorizontalStackLayout Spacing="10">
    <Label Text="Tło niebieskie?" VerticalOptions="Center" />
    <Switch x:Name="swTlo" Toggled="OnTloToggled" OnColor="#90CAF9" ThumbColor="#1565C0" />
</HorizontalStackLayout>

<HorizontalStackLayout>
    <CheckBox x:Name="chkSyrop" Color="#4527A0" CheckedChanged="OnZmiana" />
    <Label Text="Syrop (+2 zł)" VerticalOptions="Center" />
</HorizontalStackLayout>

<RadioButton x:Name="rbMala" GroupName="rozmiar" Content="mała (8 zł)" IsChecked="True"
             CheckedChanged="OnZmiana" />
<RadioButton x:Name="rbSrednia" GroupName="rozmiar" Content="średnia (10 zł)"
             CheckedChanged="OnZmiana" />
```

```csharp
private void OnTloToggled(object? sender, ToggledEventArgs e)
{
    BackgroundColor = e.Value ? Color.FromArgb("#1565C0") : Color.FromArgb("#2E7D32");
}
```

!!! info "CheckBox nie ma tekstu"
    `CheckBox` to sam kwadracik. Opis dodajesz osobną etykietą obok (w `HorizontalStackLayout`). `RadioButton` ma własny tekst we właściwości `Content`.

!!! warning "RadioButton.CheckedChanged wywołuje się dwa razy"
    Zmiana wyboru w grupie wywołuje zdarzenie dla przycisku **odznaczanego** i **zaznaczanego**. Jeśli przeliczasz wynik od nowa na podstawie stanu wszystkich kontrolek, to nie przeszkadza.

## Zadanie główne (25 min)

Utwórz projekt `Kawiarenka`: zamówienie kawy z automatycznym przeliczaniem ceny.

1. Nagłówek **Twoja kawa**, rozmiar `26`, kolor `#4E342E`.
2. Etykieta **Rozmiar:** i trzy `RadioButton` w grupie `rozmiar`: **mała – 8 zł** (zaznaczona), **średnia – 10 zł**, **duża – 12 zł**.
3. Etykieta **Dodatki:** i dwa `CheckBox` z opisami: **syrop (+2 zł)**, **bita śmietana (+3 zł)**.
4. `Switch` z opisem **Na wynos (+1 zł za kubek)**.
5. Etykieta `lblCena` z tekstem **Do zapłaty: 8 zł**, rozmiar `22`, pogrubiona, kolor `#E65100`.
6. Każda zmiana dowolnej kontrolki wywołuje **jedną** metodę `PrzeliczCene()`, która sprawdza stan wszystkich kontrolek i aktualizuje `lblCena`.
7. Gdy włączone jest **Na wynos**, tło strony zmienia się na `#FFF3E0`, a po wyłączeniu wraca do białego.

| Rozmiar | Syrop | Śmietana | Na wynos | Do zapłaty |
|---|---|---|---|---|
| mała | nie | nie | nie | 8 zł |
| średnia | tak | nie | tak | 13 zł |
| duża | tak | tak | tak | 18 zł |
| mała | nie | tak | nie | 11 zł |

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Kliknięcie etykiety obok `CheckBox` też powinno go zaznaczać. Dodaj do etykiet `TapGestureRecognizer`:

```xml
<Label Text="syrop (+2 zł)">
    <Label.GestureRecognizers>
        <TapGestureRecognizer Tapped="OnSyropTapped" />
    </Label.GestureRecognizers>
</Label>
```

W metodzie odwróć stan: `chkSyrop.IsChecked = !chkSyrop.IsChecked;`.

## Czy potrafię…?

- [ ] odczytać stan `Switch`, `CheckBox` i `RadioButton`
- [ ] pogrupować przyciski opcji
- [ ] podłączyć jedną metodę do zdarzeń wielu kontrolek
- [ ] zmienić kolor tła strony z kodu
