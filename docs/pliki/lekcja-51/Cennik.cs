namespace Kino.Logika;

/// <summary>
/// Oblicza cenę biletu do kina „Kadr”.
/// </summary>
public static class Cennik
{
    public const decimal Normalny = 30m;
    public const decimal Dzieciecy = 18m;    // do 12 lat włącznie
    public const decimal Uczniowski = 22m;   // od 13 do 25 lat włącznie
    public const decimal Senioralny = 20m;   // od 65 lat
    public const decimal RabatWtorek = 5m;   // „tani wtorek”: 5 zł mniej za każdy bilet
    public const decimal RabatKarta = 0.10m; // karta stałego klienta: 10% od ceny po innych rabatach

    public static decimal CenaBiletu(int wiek, DayOfWeek dzien, bool karta)
    {
        if (wiek < 0 || wiek > 120)
        {
            throw new ArgumentOutOfRangeException(nameof(wiek), "Wiek musi być z zakresu 0–120");
        }

        decimal cena;
        if (wiek <= 12)
        {
            cena = Dzieciecy;
        }
        else if (wiek < 25)
        {
            cena = Uczniowski;
        }
        else if (wiek > 65)
        {
            cena = Senioralny;
        }
        else
        {
            cena = Normalny;
        }

        if (dzien == DayOfWeek.Tuesday)
        {
            cena -= RabatWtorek;
        }

        if (karta)
        {
            cena -= cena * RabatKarta;
        }

        return Math.Round(cena, 2);
    }
}
