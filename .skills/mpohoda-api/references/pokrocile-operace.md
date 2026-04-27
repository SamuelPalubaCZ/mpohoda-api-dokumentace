---
name: mpohoda-api-pokrocile-operace
description: |
  Pokročilé operace v mPohoda API - likvidace, přenosy dokladů, stavy objednávek,
  platby a úhrady, skladové operace, cenové operace.
  Použij tento skill při dotazech na Liquidate, Transfer, RestToPay, Unpaid,
  status objednávek, dostupné množství, prodejní ceny.
---

# mPohoda API - Pokročilé operace

## Přehled

Tento skill pokrývá pokročilé business operace v mPohoda API.

| Operace | Popis |
|---------|-------|
| **Likvidace** | Úhrada faktury (plná/částečná) |
| **Přenos** | Převod objednávky na fakturu |
| **Platby** | Kontrola úhrad a nezaplacených dokladů |
| **Stavy** | Kontrola stavu objednávek |
| **Sklad** | Dostupné množství, registrační čísla |
| **Ceny** | Prodejní ceny, cenové skupiny |

---

## Likvidace (úhrada faktur)

### Plná likvidace

Úhrada celé částky faktury najednou.

**Vydaná faktura:**
```bash
curl -X POST "https://api.mpohoda.cz/v1/IssuedInvoices/{id}/Liquidate/Standalone/Fully" \
  -H "Authorization: Bearer ***" \
  -H "Content-Type: application/json" \
  -d '{
    "LiquidationDate": "2024-01-20",
    "CashRegisterId": "uuid-pokladny",
    "BankAccountId": "uuid-uctu"
  }'
```

**Zálohová faktura:**
```bash
curl -X POST "https://api.mpohoda.cz/v1/IssuedAdvanceInvoices/{id}/Liquidate/Standalone/Fully" \
  -H "Authorization: Bearer ***" \
  -H "Content-Type: application/json" \
  -d '{
    "LiquidationDate": "2024-01-20",
    "CashRegisterId": "uuid-pokladny"
  }'
```

### Částečná likvidace

Úhrada pouze části částky faktury.

**Vydaná faktura:**
```bash
curl -X POST "https://api.mpohoda.cz/v1/IssuedInvoices/{id}/Liquidate/Standalone/Partially" \
  -H "Authorization: Bearer ***" \
  -H "Content-Type: application/json" \
  -d '{
    "LiquidationDate": "2024-01-20",
    "Amount": 5000.00,
    "CashRegisterId": "uuid-pokladny",
    "BankAccountId": "uuid-uctu"
  }'
```

### Parametry likvidace

| Parametr | Typ | Popis |
|----------|-----|-------|
| `LiquidationDate` | string (datum) | Datum úhrady |
| `Amount` | number | Částka (pouze pro částečnou likvidaci) |
| `CashRegisterId` | string (UUID) | ID pokladny (pro hotovostní úhradu) |
| `BankAccountId` | string (UUID) | ID bankovního účtu (pro bezhotovostní úhradu) |

> **Pravidlo:** Zadejte buď `CashRegisterId` NEBO `BankAccountId`, ne obojí.

### Kontrola likvidace

```bash
# Detail likvidace
curl -X GET "https://api.mpohoda.cz/v1/IssuedInvoices/Liquidation/{id}" \
  -H "Authorization: Bearer ***"
```

---

## Přenosy dokladů

### Přijatá objednávka → Vydaná faktura

Nejčastější přenos — z objednávky zákazníka vytvoříte fakturu.

```bash
curl -X POST "https://api.mpohoda.cz/v1/ReceivedOrders/{id}/Transfer/ToIssuedInvoice/Fully" \
  -H "Authorization: Bearer ***" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Vydaná objednávka → Přijatá faktura

```bash
curl -X POST "https://api.mpohoda.cz/v1/IssuedOrders/{id}/Transfer/ToReceivedInvoice/Fully" \
  -H "Authorization: Bearer ***" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Podmínky přenosu

- Objednávka musí mít stav **Nevyřízená** (`New`)
- Přenos je vždy **kompletní** (všechny položky)
- Částečný přenos není podporován
- Tělo požadavku je prázdné `{}`

### Odpověď přenosu

```json
{
  "Data": {
    "Id": "uuid-nove-faktury",
    "DocumentNumber": "VF20240001",
    "...": "..."
  },
  "Errors": [],
  "Warnings": []
}
```

---

## Platby a úhrady

### Zbývající částka k úhradě

```bash
# Vydaná faktura
curl -X GET "https://api.mpohoda.cz/v1/IssuedInvoices/{id}/RestToPay" \
  -H "Authorization: Bearer ***"

# Zálohová faktura
curl -X GET "https://api.mpohoda.cz/v1/IssuedAdvanceInvoices/{id}/RestToPay" \
  -H "Authorization: Bearer ***"
```

### Odpověď

```json
{
  "Data": {
    "RestToPay": 12500.50,
    "Currency": "CZK",
    "TotalAmount": 15000.00,
    "PaidAmount": 2499.50
  }
}
```

### Seznam nezaplacených dokladů

```bash
# Nezaplacené vydané faktury
curl -X GET "https://api.mpohoda.cz/v1/IssuedInvoices/Unpaid?pageSize=50" \
  -H "Authorization: Bearer ***"

# Nezaplacené zálohovky
curl -X GET "https://api.mpohoda.cz/v1/IssuedAdvanceInvoices/Unpaid?pageSize=50" \
  -H "Authorization: Bearer ***"
```

---

## Stavy objednávek

### Kontrola stavu

```bash
# Vydaná objednávka
curl -X GET "https://api.mpohoda.cz/v1/IssuedOrders/{id}/status" \
  -H "Authorization: Bearer ***"

# Přijatá objednávka
curl -X GET "https://api.mpohoda.cz/v1/ReceivedOrders/{id}/status" \
  -H "Authorization: Bearer ***"
```

### Odpověď

```json
{
  "Data": {
    "Status": "New",
    "StatusText": "Nevyřízená"
  }
}
```

### Stavy objednávek

| Stav | Popis | Přenos možný? |
|------|-------|---------------|
| `New` | Nevyřízená | ✅ Ano |
| `InProgress` | Rozpracovaná | ❌ Ne |
| `Completed` | Vyřízená | ❌ Ne |
| `Cancelled` | Stornovaná | ❌ Ne |

---

## Skladové operace

### Dostupné množství

Kontrola skladových zásob pro více položek najednou.

```bash
curl -X POST "https://api.mpohoda.cz/v1/PriceListItems/AvailableQuantities" \
  -H "Authorization: Bearer ***" \
  -H "Content-Type: application/json" \
  -d '{
    "Ids": [
      "550e8400-e29b-41d4-a716-446655440000",
      "550e8400-e29b-41d4-a716-446655440001",
      "550e8400-e29b-41d4-a716-446655440002"
    ]
  }'
```

### Odpověď

```json
{
  "Data": {
    "Items": [
      {
        "PriceListItemId": "550e8400-e29b-41d4-a716-446655440000",
        "AvailableQuantity": 150.5,
        "Unit": "ks"
      },
      {
        "PriceListItemId": "550e8400-e29b-41d4-a716-446655440001",
        "AvailableQuantity": 0,
        "Unit": "ks"
      }
    ]
  }
}
```

### Registrační čísla položky

```bash
curl -X GET "https://api.mpohoda.cz/v1/PriceListItems/{id}/RegistrationNumbers" \
  -H "Authorization: Bearer ***"
```

---

## Cenové operace

### Prodejní ceny položek

Získání prodejních cen pro konkrétní položky a cenovou skupinu.

```bash
curl -X POST "https://api.mpohoda.cz/v1/PriceListItems/SellingPrices" \
  -H "Authorization: Bearer ***" \
  -H "Content-Type: application/json" \
  -d '{
    "Ids": [
      "550e8400-e29b-41d4-a716-446655440000",
      "550e8400-e29b-41d4-a716-446655440001"
    ],
    "SellingPriceCode": "Maloobchod"
  }'
```

### Odpověď

```json
{
  "Data": {
    "Items": [
      {
        "PriceListItemId": "550e8400-e29b-41d4-a716-446655440000",
        "Price": 2999.00,
        "PriceWithVat": 3628.79,
        "Currency": "CZK"
      }
    ]
  }
}
```

### Cenové skupiny

| Kód | Popis |
|-----|-------|
| `Zakladni` | Základní ceník |
| `Velkoobchod` | Velkoobchodní ceny |
| `Maloobchod` | Maloobchodní ceny |
| `Zahranicni` | Zahraniční ceny |

---

## Rychlé odkazy

- [Hlavní skill](../SKILL.md) — Přehled celého API
- [Autentizace](../references/autentizace.md) — Jak se přihlásit
- [Doklady](../references/doklady.md) — Faktury, objednávky
- [Adresář](../references/adresar.md) — Odběratelé, ceník
- [Exporty](../references/exporty.md) — PDF, ISDOC
- [SDK](../references/sdk.md) — C# SDK

---

**Synchronizováno s:** api.mpohoda.cz/doc  
**Verze:** 1.0.0
