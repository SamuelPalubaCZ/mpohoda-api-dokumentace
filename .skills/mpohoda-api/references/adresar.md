---
name: mpohoda-api-adresar
description: |
  Adresář a sklad v mPohoda API - odběratelé, dodavatelé, ceníkové položky,
  formy úhrady, bankovní účty, pokladny, prodejní ceny, registrační čísla.
  Použij tento skill při dotazech na BusinessPartners, PriceListItems,
  PaymentMethods, BankAccounts, CashRegisters, SellingPrices, RegistrationNumbers.
---

# mPohoda API - Adresář a sklad

## Přehled

Tento skill pokrývá adresářové a skladové agendy.

| Agenda | Popis |
|--------|-------|
| **BusinessPartners** | Odběratelé a dodavatelé |
| **PriceListItems** | Ceníkové položky (skladové zásoby) |
| **PaymentMethods** | Formy úhrady |
| **PaymentMethodTypes** | Typy forem úhrady |
| **BankAccounts** | Bankovní účty |
| **Banks** | Banky (číselník) |
| **CashRegisters** | Pokladny |
| **SellingPrices** | Prodejní ceny |
| **RegistrationNumbers** | Registrační čísla |

---

## Odběratelé/dodavatelé — BusinessPartners

### Základní operace

| Operace | Endpoint | Metoda |
|---------|----------|--------|
| Seznam | `/v1/BusinessPartners` | GET |
| Vytvoření | `/v1/BusinessPartners` | POST |
| Detail | `/v1/BusinessPartners/{id}` | GET |

### Vytvoření odběratele

```json
{
  "Name": "Firma s.r.o.",
  "CompanyId": "12345678",
  "VatId": "CZ12345678",
  "Email": "info@firma.cz",
  "Phone": "+420123456789",
  "Street": "Hlavní 1",
  "City": "Praha",
  "ZipCode": "11000",
  "CountryId": "uuid-zeme",
  "IsCustomer": true,
  "IsSupplier": false
}
```

### Filtr odběratelů

```bash
# Všichni odběratelé
curl -X GET "https://api.mpohoda.cz/v1/BusinessPartners?isCustomer=true" \
  -H "Authorization: Bearer ***"

# Vyhledání podle názvu
curl -X GET "https://api.mpohoda.cz/v1/BusinessPartners?filter=Stormware" \
  -H "Authorization: Bearer ***"
```

---

## Ceníkové položky — PriceListItems

### Základní operace

| Operace | Endpoint | Metoda |
|---------|----------|--------|
| Seznam | `/v1/PriceListItems` | GET |
| Detail | `/v1/PriceListItems/{id}` | GET |
| Dostupné množství | `/v1/PriceListItems/AvailableQuantities` | POST |
| Prodejní ceny | `/v1/PriceListItems/SellingPrices` | POST |
| Registrační čísla | `/v1/PriceListItems/{id}/RegistrationNumbers` | GET |

### Typy položek

| Typ | Popis |
|-----|-------|
| `Card` | Karta (jednoduchá skladová položka) |
| `Set` | Sada (složená z více karet) |
| `Complex` | Komplet (složená položka s vlastními složkami) |

### Vytvoření skladové položky

```json
{
  "Name": "Židle Z220",
  "Code": "Z220",
  "Unit": "ks",
  "Price": 2500,
  "VatRateId": "uuid-dph",
  "Type": "Card",
  "StockItem": {
    "MinStock": 10,
    "MaxStock": 100,
    "Stock": 50
  }
}
```

### Kontrola dostupného množství

```bash
curl -X POST "https://api.mpohoda.cz/v1/PriceListItems/AvailableQuantities" \
  -H "Authorization: Bearer ***" \
  -H "Content-Type: application/json" \
  -d '{
    "Ids": [
      "550e8400-e29b-41d4-a716-446655440000",
      "550e8400-e29b-41d4-a716-446655440001"
    ]
  }'
```

---

## Formy úhrady — PaymentMethods

### Základní operace

| Operace | Endpoint | Metoda |
|---------|----------|--------|
| Seznam | `/v1/PaymentMethods` | GET |
| Vytvoření | `/v1/PaymentMethods` | POST |
| Detail | `/v1/PaymentMethods/{id}` | GET |

### Typy úhrad

| Typ | Popis |
|-----|-------|
| `Cash` | Hotovost |
| `BankTransfer` | Převodem |
| `CashOnDelivery` | Dobírka |
| `Card` | Platební karta |
| `Cheque` | Šek |

---

## Bankovní účty — BankAccounts

### Základní operace

| Operace | Endpoint | Metoda |
|---------|----------|--------|
| Seznam | `/v1/BankAccounts` | GET |
| Vytvoření | `/v1/BankAccounts` | POST |
| Detail | `/v1/BankAccounts/{id}` | GET |

### Vytvoření účtu

```json
{
  "Name": "Účet KB",
  "AccountNumber": "1234567890",
  "BankCode": "0100",
  "Iban": "CZ6501000000123456789012",
  "Swift": "KOMBCZPP",
  "CurrencyId": "uuid-meny"
}
```

---

## Pokladny — CashRegisters

### Základní operace

| Operace | Endpoint | Metoda |
|---------|----------|--------|
| Seznam | `/v1/CashRegisters` | GET |
| Vytvoření | `/v1/CashRegisters` | POST |
| Detail | `/v1/CashRegisters/{id}` | GET |

---

## Prodejní ceny — SellingPrices

### Základní operace

| Operace | Endpoint | Metoda |
|---------|----------|--------|
| Seznam | `/v1/SellingPrices` | GET |
| Vytvoření | `/v1/SellingPrices` | POST |
| Detail | `/v1/SellingPrices/{id}` | GET |

### Ceníkové skupiny

Prodejní ceny se definují v ceníkových skupinách:
- **Základní** (výchozí)
- **Velkoobchod**
- **Maloobchod**
- **Zahraniční**

---

## Registrační čísla — RegistrationNumbers

### Základní operace

| Operace | Endpoint | Metoda |
|---------|----------|--------|
| Seznam | `/v1/RegistrationNumbers` | GET |
| Vytvoření | `/v1/RegistrationNumbers` | POST |
| Detail | `/v1/RegistrationNumbers/{id}` | GET |

---

## Rychlé odkazy

- [Hlavní skill](../SKILL.md) — Přehled celého API
- [Autentizace](../references/autentizace.md) — Jak se přihlásit
- [Endpointy](../references/endpointy.md) — Kompletní seznam endpointů
- [Doklady](../references/doklady.md) — Faktury, objednávky
- [Nastavení](../references/nastaveni.md) — DPH, měny, střediska
- [SDK](../references/sdk.md) — C# SDK

---

**Synchronizováno s:** api.mpohoda.cz/doc  
**Verze:** 1.0.0
