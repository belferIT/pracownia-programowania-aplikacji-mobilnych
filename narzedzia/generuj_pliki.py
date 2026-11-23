"""Generuje pliki startowe do lekcji (obrazy, dźwięki, archiwa ZIP).

Uruchomienie z katalogu głównego repozytorium:
    .venv/bin/pip install pillow
    .venv/bin/python narzedzia/generuj_pliki.py

Wszystkie zasoby są rysowane/syntezowane przez ten skrypt, więc nie ma
problemów z licencjami. Dźwięki są syntezowane w Pythonie (moduł wave).
"""
import io
import math
import random
import zipfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
PLIKI = ROOT / "docs" / "pliki"
FONT = "/usr/share/fonts/noto/NotoSans-Bold.ttf"
FONT_R = "/usr/share/fonts/noto/NotoSans-Regular.ttf"
random.seed(4)


def font(size, bold=True):
    return ImageFont.truetype(FONT if bold else FONT_R, size)


def zapisz_zip(nazwa_zip, folder, pliki):
    """pliki: dict nazwa -> bytes. Archiwum ma jeden folder główny."""
    cel = PLIKI / nazwa_zip
    cel.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(cel, "w", zipfile.ZIP_DEFLATED) as z:
        for n, dane in pliki.items():
            z.writestr(f"{folder}/{n}", dane)
    print("zapisano", cel.relative_to(ROOT))


def png(img, fmt="PNG"):
    b = io.BytesIO()
    if fmt == "JPEG":
        img = img.convert("RGB")
        img.save(b, fmt, quality=85)
    else:
        img.save(b, fmt, optimize=True)
    return b.getvalue()


def gradient(w, h, gora, dol):
    img = Image.new("RGB", (w, h))
    d = ImageDraw.Draw(img)
    for y in range(h):
        t = y / (h - 1)
        c = tuple(int(gora[i] + (dol[i] - gora[i]) * t) for i in range(3))
        d.line([(0, y), (w, y)], fill=c)
    return img


def napis(d, xy, tekst, size, fill="white", anchor="mm", bold=True):
    d.text(xy, tekst, font=font(size, bold), fill=fill, anchor=anchor,
           stroke_width=max(1, size // 18), stroke_fill=(0, 0, 0))


# ---------- krajobrazy ----------
def gory(w=800, h=500, podpis=None):
    img = gradient(w, h, (120, 180, 240), (220, 235, 250))
    d = ImageDraw.Draw(img)
    d.ellipse([w * 0.72, h * 0.1, w * 0.86, h * 0.1 + w * 0.14], fill=(255, 220, 90))
    d.polygon([(0, h), (w * 0.3, h * 0.35), (w * 0.6, h)], fill=(90, 100, 120))
    d.polygon([(w * 0.3, h * 0.35), (w * 0.24, h * 0.47), (w * 0.36, h * 0.47)], fill="white")
    d.polygon([(w * 0.35, h), (w * 0.7, h * 0.25), (w, h * 0.8), (w, h)], fill=(70, 80, 100))
    d.polygon([(w * 0.7, h * 0.25), (w * 0.63, h * 0.38), (w * 0.77, h * 0.38)], fill="white")
    d.rectangle([0, h * 0.88, w, h], fill=(60, 140, 70))
    if podpis:
        napis(d, (w / 2, h * 0.12), podpis, h // 9)
    return img


def morze(w=800, h=500, podpis=None):
    img = gradient(w, h, (250, 170, 110), (255, 225, 170))
    d = ImageDraw.Draw(img)
    d.ellipse([w * 0.42, h * 0.35, w * 0.58, h * 0.35 + w * 0.16], fill=(255, 120, 60))
    d.rectangle([0, h * 0.55, w, h], fill=(30, 110, 170))
    for i in range(14):
        y = h * 0.6 + i * h * 0.03
        x = random.randint(0, w)
        d.line([(x, y), (x + 60, y)], fill=(140, 200, 240), width=3)
    d.polygon([(0, h), (0, h * 0.85), (w * 0.4, h)], fill=(240, 210, 150))
    if podpis:
        napis(d, (w / 2, h * 0.12), podpis, h // 9)
    return img


def las(w=800, h=500, podpis=None):
    img = gradient(w, h, (170, 215, 240), (230, 245, 230))
    d = ImageDraw.Draw(img)
    d.rectangle([0, h * 0.8, w, h], fill=(70, 130, 60))
    for i in range(9):
        x = w * (0.05 + i * 0.11)
        s = random.uniform(0.8, 1.2)
        d.rectangle([x - 8, h * 0.7, x + 8, h * 0.85], fill=(100, 70, 40))
        for k in range(3):
            y0 = h * (0.3 + k * 0.13) / s + h * 0.1
            d.polygon([(x, y0), (x - 50 * s + k * 6, y0 + h * 0.2), (x + 50 * s - k * 6, y0 + h * 0.2)],
                      fill=(30 + k * 15, 110 + k * 10, 50))
    if podpis:
        napis(d, (w / 2, h * 0.12), podpis, h // 9)
    return img


def miasto(w=800, h=500, podpis=None):
    img = gradient(w, h, (40, 50, 110), (140, 110, 170))
    d = ImageDraw.Draw(img)
    x = 0
    while x < w:
        bw = random.randint(60, 120)
        bh = random.randint(int(h * 0.25), int(h * 0.7))
        d.rectangle([x, h - bh, x + bw, h], fill=(30, 30, 50))
        for wy in range(h - bh + 15, h - 10, 28):
            for wx in range(x + 10, x + bw - 15, 22):
                if random.random() < 0.55:
                    d.rectangle([wx, wy, wx + 10, wy + 14], fill=(255, 220, 120))
        x += bw + 6
    if podpis:
        napis(d, (w / 2, h * 0.12), podpis, h // 9)
    return img


def logo(rozmiar=400, litera="M", kolor=(69, 39, 160)):
    img = Image.new("RGBA", (rozmiar, rozmiar), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.ellipse([10, 10, rozmiar - 10, rozmiar - 10], fill=kolor + (255,))
    d.ellipse([40, 40, rozmiar - 40, rozmiar - 40], outline=(255, 152, 0, 255), width=14)
    d.text((rozmiar / 2, rozmiar / 2), litera, font=font(int(rozmiar * 0.45)), fill="white", anchor="mm")
    return img


def ikona_produktu(nazwa, kolor, ksztalt, rozmiar=400):
    """Prosta ilustracja produktu na przezroczystym tle."""
    img = Image.new("RGBA", (rozmiar, rozmiar), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    s = rozmiar
    if ksztalt == "kubek":
        d.rounded_rectangle([s * .22, s * .3, s * .68, s * .85], radius=s * .06, fill=kolor)
        d.arc([s * .58, s * .42, s * .85, s * .7], 270, 90, fill=kolor, width=int(s * .06))
        d.ellipse([s * .25, s * .26, s * .65, s * .36], fill=(90, 50, 25))
        for i in range(3):
            x = s * (.32 + i * .12)
            d.arc([x, s * .05, x + s * .08, s * .25], 90, 270, fill=(160, 160, 160), width=6)
    elif ksztalt == "filizanka":
        d.pieslice([s * .18, s * .2, s * .72, s * .8], 0, 180, fill=kolor)
        d.arc([s * .62, s * .5, s * .85, s * .72], 270, 90, fill=kolor, width=int(s * .05))
        d.ellipse([s * .1, s * .78, s * .8, s * .9], fill=(220, 220, 220))
        d.rectangle([s * .44, s * .2, s * .46, s * .5], fill=(240, 240, 240))
        d.rectangle([s * .4, s * .12, s * .5, s * .2], fill=(250, 200, 60))
    elif ksztalt == "ciasto":
        d.polygon([(s * .1, s * .75), (s * .9, s * .75), (s * .9, s * .5), (s * .1, s * .35)], fill=kolor)
        d.polygon([(s * .1, s * .35), (s * .9, s * .5), (s * .9, s * .42), (s * .1, s * .27)], fill=(255, 245, 230))
        d.ellipse([s * .55, s * .2, s * .7, s * .35], fill=(200, 20, 40))
    elif ksztalt == "kwiat":
        d.line([(s * .5, s * .5), (s * .5, s * .95)], fill=(40, 130, 50), width=int(s * .04))
        d.ellipse([s * .5, s * .7, s * .72, s * .8], fill=(60, 160, 70))
        for k in range(8):
            a = k * math.pi / 4
            cx, cy = s * .5 + math.cos(a) * s * .18, s * .35 + math.sin(a) * s * .18
            d.ellipse([cx - s * .12, cy - s * .12, cx + s * .12, cy + s * .12], fill=kolor)
        d.ellipse([s * .4, s * .25, s * .6, s * .45], fill=(250, 200, 40) if kolor != (250, 200, 40) else (110, 60, 20))
    elif ksztalt == "tulipan":
        d.line([(s * .5, s * .5), (s * .5, s * .95)], fill=(40, 130, 50), width=int(s * .04))
        d.ellipse([s * .28, s * .6, s * .5, s * .85], fill=(60, 160, 70))
        d.pieslice([s * .28, s * .05, s * .72, s * .6], 0, 180, fill=kolor)
        d.polygon([(s * .28, s * .33), (s * .36, s * .1), (s * .44, s * .33)], fill=kolor)
        d.polygon([(s * .43, s * .33), (s * .5, s * .06), (s * .57, s * .33)], fill=kolor)
        d.polygon([(s * .56, s * .33), (s * .64, s * .1), (s * .72, s * .33)], fill=kolor)
    elif ksztalt == "rakieta":
        d.ellipse([s * .38, s * .05, s * .62, s * .75], fill=kolor)
        d.polygon([(s * .38, s * .55), (s * .22, s * .8), (s * .4, s * .7)], fill=(200, 40, 40))
        d.polygon([(s * .62, s * .55), (s * .78, s * .8), (s * .6, s * .7)], fill=(200, 40, 40))
        d.ellipse([s * .44, s * .25, s * .56, s * .37], fill=(80, 170, 230), outline="white", width=4)
        d.polygon([(s * .43, s * .74), (s * .57, s * .74), (s * .5, s * .95)], fill=(255, 152, 0))
    elif ksztalt == "rower":
        for cx in (s * .25, s * .75):
            d.ellipse([cx - s * .18, s * .5, cx + s * .18, s * .86], outline=(40, 40, 40), width=int(s * .03))
        d.line([(s * .25, s * .68), (s * .45, s * .45), (s * .7, s * .45), (s * .75, s * .68)], fill=kolor, width=int(s * .035))
        d.line([(s * .45, s * .45), (s * .5, s * .68), (s * .25, s * .68)], fill=kolor, width=int(s * .035))
        d.line([(s * .5, s * .68), (s * .7, s * .45)], fill=kolor, width=int(s * .035))
        d.line([(s * .7, s * .45), (s * .67, s * .32), (s * .6, s * .32)], fill=(40, 40, 40), width=int(s * .03))
        d.line([(s * .42, s * .4), (s * .52, s * .4)], fill=(40, 40, 40), width=int(s * .04))
    d.text((s / 2, s * .97), nazwa, font=font(int(s * .07)), fill=(60, 60, 60), anchor="md")
    return img


def wav(nuty, glosnosc=0.5, rate=22050):
    """Syntezuje dźwięk z listy (częstotliwość Hz, czas s); zwraca bajty WAV."""
    import struct
    import wave
    probki = bytearray()
    for f, czas in nuty:
        n = int(rate * czas)
        for i in range(n):
            obw = min(1.0, i / (rate * 0.005), (n - i) / (rate * 0.05))  # bez trzasków
            v = glosnosc * obw * math.sin(2 * math.pi * f * i / rate) if f else 0
            probki += struct.pack("<h", int(v * 32767))
    b = io.BytesIO()
    with wave.open(b, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(rate)
        w.writeframes(bytes(probki))
    return b.getvalue()


# ================= lekcje =================
def lekcja_08():
    zapisz_zip("lekcja-08/obrazy.zip", "obrazy", {
        "gory.jpg": png(gory(), "JPEG"),
        "morze.jpg": png(morze(), "JPEG"),
        "las.jpg": png(las(), "JPEG"),
        "logo.png": png(logo()),
    })


def lekcja_16():
    rys = [gory, morze, las, miasto]
    pliki = {f"widok{i + 1}.jpg": png(f(podpis=str(i + 1)), "JPEG") for i, f in enumerate(rys)}
    zapisz_zip("lekcja-16/galeria.zip", "galeria", pliki)


def lekcja_23():
    cel = PLIKI / "lekcja-23" / "rakieta.png"
    cel.parent.mkdir(parents=True, exist_ok=True)
    cel.write_bytes(png(ikona_produktu("", (230, 230, 240), "rakieta")))
    print("zapisano", cel.relative_to(ROOT))


def lekcja_24():
    zapisz_zip("lekcja-24/dzwieki.zip", "dzwieki", {
        "dzwonek.wav": wav([(880, 0.25), (660, 0.4)]),
        "klik.wav": wav([(2000, 0.04)], 0.4),
        "fanfara.wav": wav([(523, 0.2), (659, 0.2), (784, 0.2), (1047, 0.6)]),
        "blad.wav": wav([(220, 0.2), (0, 0.05), (180, 0.4)]),
    })


def lekcja_25():
    zapisz_zip("lekcja-25/kawiarnia.zip", "kawiarnia", {
        "kawa.png": png(ikona_produktu("kawa", (120, 70, 40), "kubek")),
        "herbata.png": png(ikona_produktu("herbata", (200, 60, 50), "filizanka")),
        "ciasto.png": png(ikona_produktu("ciasto", (230, 180, 110), "ciasto")),
    })


def lekcja_26():
    zapisz_zip("lekcja-26/kwiaciarnia.zip", "kwiaciarnia", {
        "roza.png": png(ikona_produktu("róża", (200, 20, 50), "kwiat")),
        "tulipan.png": png(ikona_produktu("tulipan", (250, 120, 30), "tulipan")),
        "slonecznik.png": png(ikona_produktu("słonecznik", (250, 200, 40), "kwiat")),
    })


def lekcja_32():
    zapisz_zip("lekcja-32/przewodnik.zip", "przewodnik", {
        "zamek.jpg": png(gory(podpis="Zamek"), "JPEG"),
        "rynek.jpg": png(miasto(podpis="Rynek"), "JPEG"),
        "park.jpg": png(las(podpis="Park"), "JPEG"),
        "port.jpg": png(morze(podpis="Port"), "JPEG"),
    })


def lekcja_47():
    zapisz_zip("lekcja-47/rowery.zip", "rowery", {
        "miejski.png": png(ikona_produktu("miejski", (30, 120, 200), "rower")),
        "gorski.png": png(ikona_produktu("górski", (60, 150, 60), "rower")),
        "elektryczny.png": png(ikona_produktu("elektryczny", (230, 120, 20), "rower")),
    })


def lekcja_57():
    zapisz_zip("lekcja-57/wycieczki.zip", "wycieczki", {
        "gory.jpg": png(gory(podpis="Tatry"), "JPEG"),
        "morze.jpg": png(morze(podpis="Bałtyk"), "JPEG"),
        "las.jpg": png(las(podpis="Bieszczady"), "JPEG"),
        "miasto.jpg": png(miasto(podpis="Kraków"), "JPEG"),
    })




# ---------- dział 5: kod z celowymi błędami (NIE poprawiać!) ----------
DEBUG_XAML = '''<?xml version="1.0" encoding="utf-8" ?>
<ContentPage xmlns="http://schemas.microsoft.com/dotnet/2021/maui"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             x:Class="Debugowanie.MainPage"
             Title="Średnia ocen">

    <VerticalStackLayout Padding="20" Spacing="12">
        <Label Text="Średnia ocen" FontSize="28" FontAttributes="Bold" TextColor="#4527A0" />
        <Label Text="Wpisz oceny oddzielone spacjami, np. 5 4 3 6" />
        <Entry x:Name="entOceny" Placeholder="oceny" />
        <Button x:Name="btnOblicz" Text="Oblicz" BackgroundColor="#FF9800" TextColor="White"
                Clicked="OnObliczClicked" />
        <Label x:Name="lblWynik" FontSize="20" />
    </VerticalStackLayout>

</ContentPage>
'''

DEBUG_CS = '''namespace Debugowanie;

public partial class MainPage : ContentPage
{
    public MainPage()
    {
        InitializeComponent();
    }

    private void OnObliczClicked(object? sender, EventArgs e)
    {
        string[] czesci = entOceny.Text.Split(' ', StringSplitOptions.RemoveEmptyEntries);
        int[] oceny = new int[czesci.Length];

        for (int i = 0; i <= czesci.Length; i++)
        {
            oceny[i] = int.Parse(czesci[i]);
        }

        int suma = 0;
        int najwyzsza = 0;
        foreach (int ocena in oceny)
        {
            if (ocena < 1 && ocena > 6)
            {
                lblWynik.Text = $"Ocena {ocena} jest spoza skali 1–6";
                return;
            }
            suma += ocena;
            if (ocena > najwyzsza)
            {
                najwyzsza = ocena;
            }
        }

        double srednia = suma / oceny.Length;
        string wyroznienie = srednia > 4.75 ? "TAK" : "NIE";

        lblWynik.Text = $"Średnia: {srednia:F2}\\nNajwyższa: {najwyzsza}\\nWyróżnienie: {wyroznienie}";
    }
}
'''

CENNIK_CS = '''namespace Kino.Logika;

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
'''


def lekcja_50():
    zapisz_zip("lekcja-50/debugowanie.zip", "debugowanie", {
        "MainPage.xaml": DEBUG_XAML.encode(),
        "MainPage.xaml.cs": DEBUG_CS.encode(),
    })


def lekcja_51():
    cel = PLIKI / "lekcja-51" / "Cennik.cs"
    cel.parent.mkdir(parents=True, exist_ok=True)
    cel.write_text(CENNIK_CS)
    print("zapisano", cel.relative_to(ROOT))


def lekcja_54():
    tlo = '''<svg xmlns="http://www.w3.org/2000/svg" width="456" height="456" viewBox="0 0 456 456">
  <!-- tło ikony: cały kwadrat, jeden kolor (system sam przytnie do koła lub zaokrąglonego kwadratu) -->
  <rect x="0" y="0" width="456" height="456" fill="#4527A0"/>
</svg>
'''
    przod = '''<svg xmlns="http://www.w3.org/2000/svg" width="456" height="456" viewBox="0 0 456 456">
  <!-- pierwszy plan: rysuj tylko w środkowym obszarze ok. 300×300 (przerywana ramka – usuń ją) -->
  <rect x="78" y="78" width="300" height="300" fill="none" stroke="#FFFFFF" stroke-dasharray="12 8" stroke-width="4"/>
  <circle cx="228" cy="228" r="110" fill="#FF9800"/>
  <text x="228" y="268" font-family="Arial, sans-serif" font-size="120" font-weight="bold"
        text-anchor="middle" fill="#FFFFFF">A</text>
</svg>
'''
    zapisz_zip("lekcja-54/ikona.zip", "ikona", {"appicon.svg": tlo.encode(), "appiconfg.svg": przod.encode()})


if __name__ == "__main__":
    for nazwa, f in sorted(globals().items()):
        if nazwa.startswith("lekcja_") and callable(f):
            f()
