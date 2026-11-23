# Lekcja 20. Konwertery wartości i wyzwalacze

<p class="lekcja-meta">Dział: Kontrolki i wiązanie danych · 45 min · Efekty: INF.04.6 (2) kryt. 5 · <span class="zakres zakres-p">INF.04</span> <span class="zakres zakres-gw">P+</span></p>

## Cel lekcji

Po tej lekcji potrafisz:

- napisać konwerter, który zamienia wartość wiązania na inny typ (np. liczbę na kolor),
- zmienić wygląd kontrolki wyzwalaczem (`DataTrigger`) bez kodu C#.

## Wprowadzenie

### Konwerter

Konwerter to klasa z interfejsem `IValueConverter`. Metoda `Convert` zamienia wartość źródła na wartość dla celu.

```csharp
using System.Globalization;

public class BmiNaKolorConverter : IValueConverter
{
    public object? Convert(object? value, Type targetType, object? parameter, CultureInfo culture)
    {
        double bmi = (double)value!;
        if (bmi < 18.5) return Colors.SteelBlue;
        if (bmi < 25) return Colors.SeaGreen;
        if (bmi < 30) return Colors.Orange;
        return Colors.Red;
    }

    public object? ConvertBack(object? value, Type targetType, object? parameter, CultureInfo culture)
        => throw new NotImplementedException();
}
```

```xml
<ContentPage.Resources>
    <local:BmiNaKolorConverter x:Key="BmiNaKolor" />
</ContentPage.Resources>

<Label Text="{Binding Bmi, StringFormat='{0:F2}'}"
       TextColor="{Binding Bmi, Converter={StaticResource BmiNaKolor}}" />
```

### Wyzwalacz danych

```xml
<Entry x:Name="entKod" Placeholder="Kod (4 cyfry)" Keyboard="Numeric" />

<Button Text="Wyślij" IsEnabled="False">
    <Button.Triggers>
        <DataTrigger TargetType="Button"
                     Binding="{Binding Source={x:Reference entKod}, Path=Text.Length}"
                     Value="4">
            <Setter Property="IsEnabled" Value="True" />
            <Setter Property="BackgroundColor" Value="#FF9800" />
        </DataTrigger>
    </Button.Triggers>
</Button>
```

| Rodzaj wyzwalacza | Kiedy działa |
|---|---|
| `Trigger` | gdy **własna** właściwość kontrolki ma wartość (np. `IsFocused` = `True`) |
| `DataTrigger` | gdy wiązanie ma wartość (np. długość tekstu innego pola = 4) |
| `MultiTrigger` | gdy spełnionych jest kilka warunków naraz |

!!! tip "Gotowe konwertery"
    Pakiet **CommunityToolkit.Maui** zawiera wiele gotowych konwerterów, np. `InvertedBoolConverter`, `IsStringNullOrEmptyConverter`, `IntToBoolConverter`. Warto je znać, ale na lekcji piszesz własny.

## Zadanie główne (25 min)

Rozbuduj projekt `Bmi` z lekcji 19.

1. Dodaj klasę `BmiNaKolorConverter` z przykładu. Zarejestruj ją w zasobach strony.
2. Kolor tekstu etykiety z BMI i etykiety z kategorią ustaw przez wiązanie z konwerterem.
3. Napisz drugi konwerter `BmiNaPostepConverter`, który zamienia BMI na wartość 0–1 dla `ProgressBar`: `(bmi - 15) / 25`, ograniczoną do przedziału 0–1 (`Math.Clamp`). Dodaj pasek postępu pod BMI.
4. Dodaj `Entry` **Imię** i przycisk **Zapisz wynik**, który jest aktywny tylko wtedy, gdy imię ma co najmniej 1 znak. Użyj `DataTrigger` (podpowiedź: `Value="0"` i ustaw `IsEnabled` na `False`, a domyślnie przycisk jest aktywny).
5. Dodaj do pola **Imię** `Trigger`: gdy pole ma fokus (`IsFocused` = `True`), jego tło zmienia się na `#FFF3E0`.

## Zadanie dla chętnych <span class="zakres zakres-gw">★ poza egzaminem</span>

Napisz konwerter z parametrem: `ProgPrzekroczonyConverter`, który zwraca `true`, gdy wartość jest większa niż `ConverterParameter`. Użyj go, aby pokazać ikonę ostrzeżenia (⚠) tylko dla BMI większego niż 30: `IsVisible="{Binding Bmi, Converter={StaticResource Prog}, ConverterParameter=30}"`. Pamiętaj, że parametr przychodzi jako tekst.

## Czy potrafię…?

- [ ] napisać klasę z interfejsem `IValueConverter`
- [ ] zarejestrować konwerter w zasobach i użyć go w wiązaniu
- [ ] zmienić wygląd kontrolki wyzwalaczem `DataTrigger`
- [ ] odróżnić `Trigger` od `DataTrigger`
