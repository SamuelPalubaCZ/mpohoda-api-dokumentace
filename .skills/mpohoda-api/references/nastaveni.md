---
name: mpohoda-api-nastaveni
description: |
  Nastavení a číselníky v mPohoda API - DPH sazby, měny, kurzy, střediska,
  činnosti, země, kraje, PSČ, provozovny, banky, typy úhrad.
  Použij tento skill při dotazech na VatRates, Currencies, ExchangeRates,
  Centres, Activities, Countries, Regions, CityPostCodes, Establishments,
  Banks, PaymentMethodTypes.
---

# mPohoda API - Nastavení a číselníky

## Přehled

Tento skill pokrývá nastavovací agendy a číselníky.

| Agenda | Popis |
|--------|-------|
| **VatRates** | DPH sazby |
| **Currencies** | Měny |
| **ExchangeRates** | Kurzy měn |
| **Centres** | Střediska |
| **Activities** | Činnosti |
| **Countries** | Země |
| **Regions** | Kraje |
| **CityPostCodes** | PSČ |
| **Establishments** | Provozovny |
| **Banks** | Banky (číselník) |
| **PaymentMethodTypes** | Typy forem úhrady |

---

## DPH sazby — VatRates

### Základní operace

| Operace | Endpoint | Metoda |
|---------|----------|--------|
| Seznam | `/v1/VatRates` | GET |
| Detail | `/v1/VatRates/{id}` | GET |

### Sazby DPH v ČR (2024)

| Sazba | Hodnota | Použití |
|-------|---------|---------|
| Základní | 21 % | Většina zboží a služeb |
| 1. snížená | 15 % | Potraviny, dětské zboží |
| 2. snížená | 10 % | Léky, knihy |
| Nulová | 0 % | Export, finanční služby |

### Mapování API hodnot

| API hodnota | Sazba |
|-------------|-------|
| `BasicVatRate` | 21 % |
| `FirstReducedVatRate` | 15 % |
| `SecondReducedVatRate` | 10 % |
| `ZeroVatRate` | 0 % |

---

## Měny — Currencies

### Základní operace

| Operace | Endpoint | Metoda |
|---------|----------|--------|
| Seznam | `/v1/Currencies` | GET |
| Detail | `/v1/Currencies/{id}` | GET |

### Hlavní měny

| Kód | Název |
|-----|-------|
| `CZK` | Česká koruna |
| `EUR` | Euro |
| `USD` | Americký dolar |
| `GBP` | Britská libra |

---

## Kurzy — ExchangeRates

### Základní operace

| Operace | Endpoint | Metoda |
|---------|----------|--------|
| Seznam | `/v1/ExchangeRates` | GET |
| Vytvoření | `/v1/ExchangeRates` | POST |
| Detail | `/v1/ExchangeRates/{id}` | GET |

### Vytvoření kurzu

```json
{
  "Date": "2024-01-15",
  "CurrencyId": "uuid-meny",
  "Rate": 24.50,
  "Amount": 1
}
```

---

## Střediska — Centres

### Základní operace

| Operace | Endpoint | Metoda |
|---------|----------|--------|
| Seznam | `/v1/Centres` | GET |
| Vytvoření | `/v1/Centres` | POST |
| Detail | `/v1/Centres/{id}` | GET |

---

## Činnosti — Activities

### Základní operace

| Operace | Endpoint | Metoda |
|---------|----------|--------|
| Seznam | `/v1/Activities` | GET |
| Vytvoření | `/v1/Activities` | POST |
| Detail | `/v1/Activities/{id}` | GET |

---

## Země — Countries

### Základní operace

| Operace | Endpoint | Metoda |
|---------|----------|--------|
| Seznam | `/v1/Countries` | GET |
| Detail | `/v1/Countries/{id}` | GET |

### Hlavní země EU

| Kód | Název |
|-----|-------|
| `CZ` | Česká republika |
| `SK` | Slovensko |
| `DE` | Německo |
| `PL` | Polsko |
| `AT` | Rakousko |

---

## Kraje — Regions

### Základní operace

| Operace | Endpoint | Metoda |
|---------|----------|--------|
| Seznam | `/v1/Regions` | GET |
| Detail | `/v1/Regions/{id}` | GET |

---

## PSČ — CityPostCodes

### Základní operace

| Operace | Endpoint | Metoda |
|---------|----------|--------|
| Seznam | `/v1/CityPostCodes` | GET |
| Detail | `/v1/CityPostCodes/{id}` | GET |

---

## Provozovny — Establishments

### Základní operace

| Operace | Endpoint | Metoda |
|---------|----------|--------|
| Seznam | `/v1/Establishments` | GET |
| Vytvoření | `/v1/Establishments` | POST |
| Detail | `/v1/Establishments/{id}` | GET |

### Vytvoření provozovny

```json
{
  "Name": "Hlavní provozovna",
  "Street": "Hlavní 1",
  "City": "Praha",
  "ZipCode": "11000",
  "CountryId": "uuid-zeme",
  "Phone": "+420123456789",
  "Email": "provozovna@firma.cz"
}
```

---

## Rychlé odkazy

- [Hlavní skill](../SKILL.md) — Přehled celého API
- [Autentizace](../references/autentizace.md) — Jak se přihlásit
- [Endpointy](../references/endpointy.md) — Kompletní seznam endpointů
- [Doklady](../references/doklady.md) — Faktury, objednávky
- [Adresář](../references/adresar.md) — Odběratelé, ceník
- [SDK](../references/sdk.md) — C# SDK

---

**Synchronizováno s:** api.mpohoda.cz/doc  
**Verze:** 1.0.0
