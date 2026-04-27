---
name: mpohoda-api-doklady
description: |
  Doklady v mPohoda API - faktury, objednávky, nabídky, výdejky, zálohovky, ODD.
  Použij tento skill při dotazech na vytvoření, čtení, úpravu, mazání, 
  PDF export, ISDOC export, likvidaci, přenos dokladů.
  
  Pokrývá: IssuedInvoices, ReceivedInvoices, IssuedOrders, ReceivedOrders,
  IssuedOffers, IssueSlips, IssuedAdvanceInvoices, IssuedInvoiceCorrectiveTaxDocuments.
---

# mPohoda API - Doklady

## Přehled

Tento skill pokrývá všechny dokladové agendy v mPohoda API.

| Agenda | Popis |
|--------|-------|
| **IssuedInvoices** | Vydané faktury (prodej) |
| **ReceivedInvoices** | Přijaté faktury (nákup) |
| **IssuedOrders** | Vydané objednávky |
| **ReceivedOrders** | Přijaté objednávky |
| **IssuedOffers** | Nabídky |
| **IssueSlips** | Výdejky |
| **IssuedAdvanceInvoices** | Zálohové faktury |
| **IssuedInvoiceCorrectiveTaxDocuments** | Opravné daňové doklady |

---

## Vydané faktury — IssuedInvoices

### Základní operace

| Operace | Endpoint | Metoda |
|---------|----------|--------|
| Seznam | `/v1/IssuedInvoices` | GET |
| Vytvoření | `/v1/IssuedInvoices` | POST |
| Detail | `/v1/IssuedInvoices/{id}` | GET |
| PDF | `/v1/IssuedInvoices/{id}/pdf` | GET |
| ISDOC | `/v1/IssuedInvoices/{id}/isdoc` | GET |
| Zbývá k úhradě | `/v1/IssuedInvoices/{id}/RestToPay` | GET |
| Likvidace | `/v1/IssuedInvoices/Liquidation/{id}` | GET |
| Nezaplacené | `/v1/IssuedInvoices/Unpaid` | GET |
| Plná likvidace | `/v1/IssuedInvoices/{id}/Liquidate/Standalone/Fully` | POST |
| Částečná likvidace | `/v1/IssuedInvoices/{id}/Liquidate/Standalone/Partially` | POST |

### Vytvoření faktury

```json
{
  "Text": "Faktura za zboží",
  "IssueDate": "2024-01-15",
  "DueDate": "2024-01-29",
  "TaxDate": "2024-01-15",
  "PaymentMethodId": "uuid-formy-uhry",
  "BankAccountId": "uuid-uctu",
  "BusinessPartnerAddress": {
    "DocumentAddressWithAddressBookLink": {
      "Id": "uuid-odberatele"
    }
  },
  "Items": [
    {
      "TextItem": {
        "Text": "Polozka 1",
        "Quantity": 1,
        "Unit": "ks",
        "UnitPrice": 1000,
        "UnitPriceType": "WithoutVat",
        "VatRateType": "BasicVatRate"
      }
    },
    {
      "PriceListItem": {
        "PriceListItemId": "uuid-zasoby",
        "Quantity": 5
      }
    }
  ]
}
```

### Likvidace faktury

**Plná likvidace** (celá částka):
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

**Částečná likvidace** (část částky):
```bash
curl -X POST "https://api.mpohoda.cz/v1/IssuedInvoices/{id}/Liquidate/Standalone/Partially" \
  -H "Authorization: Bearer ***" \
  -H "Content-Type: application/json" \
  -d '{
    "LiquidationDate": "2024-01-20",
    "Amount": 5000,
    "CashRegisterId": "uuid-pokladny"
  }'
```

---

## Přijaté faktury — ReceivedInvoices

### Základní operace

| Operace | Endpoint | Metoda |
|---------|----------|--------|
| Seznam | `/v1/ReceivedInvoices` | GET |
| Vytvoření | `/v1/ReceivedInvoices` | POST |
| Detail | `/v1/ReceivedInvoices/{id}` | GET |
| PDF | `/v1/ReceivedInvoices/{id}/pdf` | GET |

---

## Vydané objednávky — IssuedOrders

### Základní operace

| Operace | Endpoint | Metoda |
|---------|----------|--------|
| Seznam | `/v1/IssuedOrders` | GET |
| Vytvoření | `/v1/IssuedOrders` | POST |
| Detail | `/v1/IssuedOrders/{id}` | GET |
| PDF | `/v1/IssuedOrders/{id}/pdf` | GET |
| Stav | `/v1/IssuedOrders/{id}/status` | GET |
| Přenos do přijaté faktury | `/v1/IssuedOrders/{id}/Transfer/ToReceivedInvoice/Fully` | POST |

### Přenos objednávky na fakturu

```bash
curl -X POST "https://api.mpohoda.cz/v1/IssuedOrders/{id}/Transfer/ToReceivedInvoice/Fully" \
  -H "Authorization: Bearer ***" \
  -H "Content-Type: application/json" \
  -d '{}'
```

---

## Přijaté objednávky — ReceivedOrders

### Základní operace

| Operace | Endpoint | Metoda |
|---------|----------|--------|
| Seznam | `/v1/ReceivedOrders` | GET |
| Vytvoření | `/v1/ReceivedOrders` | POST |
| Detail | `/v1/ReceivedOrders/{id}` | GET |
| PDF | `/v1/ReceivedOrders/{id}/pdf` | GET |
| Stav | `/v1/ReceivedOrders/{id}/status` | GET |
| Přenos do vydané faktury | `/v1/ReceivedOrders/{id}/Transfer/ToIssuedInvoice/Fully` | POST |

---

## Nabídky — IssuedOffers

### Základní operace

| Operace | Endpoint | Metoda |
|---------|----------|--------|
| Seznam | `/v1/IssuedOffers` | GET |
| Vytvoření | `/v1/IssuedOffers` | POST |
| Detail | `/v1/IssuedOffers/{id}` | GET |
| PDF | `/v1/IssuedOffers/{id}/pdf` | GET |

---

## Výdejky — IssueSlips

### Základní operace

| Operace | Endpoint | Metoda |
|---------|----------|--------|
| Seznam | `/v1/IssueSlips` | GET |
| Vytvoření | `/v1/IssueSlips` | POST |
| Detail | `/v1/IssueSlips/{id}` | GET |
| PDF | `/v1/IssueSlips/{id}/pdf` | GET |

---

## Zálohové faktury — IssuedAdvanceInvoices

### Základní operace

| Operace | Endpoint | Metoda |
|---------|----------|--------|
| Seznam | `/v1/IssuedAdvanceInvoices` | GET |
| Vytvoření | `/v1/IssuedAdvanceInvoices` | POST |
| Detail | `/v1/IssuedAdvanceInvoices/{id}` | GET |
| PDF | `/v1/IssuedAdvanceInvoices/{id}/pdf` | GET |
| ISDOC | `/v1/IssuedAdvanceInvoices/{id}/isdoc` | GET |
| Zbývá k úhradě | `/v1/IssuedAdvanceInvoices/{id}/RestToPay` | GET |
| Likvidace | `/v1/IssuedAdvanceInvoices/Liquidation/{id}` | GET |
| Nezaplacené | `/v1/IssuedAdvanceInvoices/Unpaid` | GET |
| Plná likvidace | `/v1/IssuedAdvanceInvoices/{id}/Liquidate/Standalone/Fully` | POST |

---

## Opravné daňové doklady — IssuedInvoiceCorrectiveTaxDocuments

### Základní operace

| Operace | Endpoint | Metoda |
|---------|----------|--------|
| Seznam | `/v1/IssuedInvoiceCorrectiveTaxDocuments` | GET |
| Vytvoření | `/v1/IssuedInvoiceCorrectiveTaxDocuments` | POST |
| Detail | `/v1/IssuedInvoiceCorrectiveTaxDocuments/{id}` | GET |
| PDF | `/v1/IssuedInvoiceCorrectiveTaxDocuments/{id}/pdf` | GET |

---

## Společné vlastnosti dokladů

### Položky dokladu

| Typ | Použití | Povinná pole |
|-----|---------|--------------|
| `TextItem` | Textová položka | Text, Quantity, UnitPrice, UnitPriceType, VatRateType |
| `PriceListItem` | Skladová položka | PriceListItemId, Quantity |

### Typy cen

| Hodnota | Popis |
|---------|-------|
| `WithoutVat` | Cena bez DPH |
| `WithVat` | Cena s DPH |

### DPH sazby

| Hodnota | Popis |
|---------|-------|
| `ZeroVatRate` | 0% |
| `BasicVatRate` | Základní (21%) |
| `FirstReducedVatRate` | 1. snížená (15%) |
| `SecondReducedVatRate` | 2. snížená (10%) |

### Stavy objednávek

| Stav | Popis |
|------|-------|
| `New` | Nová |
| `InProgress` | Rozpracovaná |
| `Completed` | Vyřízená |
| `Cancelled` | Stornovaná |

---

## Rychlé odkazy

- [Hlavní skill](../SKILL.md) — Přehled celého API
- [Autentizace](../references/autentizace.md) — Jak se přihlásit
- [Endpointy](../references/endpointy.md) — Kompletní seznam endpointů
- [Průvodci](../references/pruvodci.md) — Návody krok za krokem
- [Adresář](../references/adresar.md) — Odběratelé, ceník
- [SDK](../references/sdk.md) — C# SDK

---

**Synchronizováno s:** api.mpohoda.cz/doc  
**Verze:** 1.0.0
