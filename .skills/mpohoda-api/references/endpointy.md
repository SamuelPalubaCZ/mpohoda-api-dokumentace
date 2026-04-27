---
name: mpohoda-api-endpointy
description: |
  Kompletní seznam všech 78 mPohoda API endpointů. 
  Použij tento skill při dotazech na konkrétní API metody, 
  URL endpointů, HTTP metody (GET/POST/PUT/DELETE), parametry, 
  odpovědi nebo při potřebě najít správný endpoint pro operaci.
---

# mPohoda API - Endpointy

## Přehled

Celkem **78 endpointů** pokrývajících všechny agendy mPohoda.

Base URL: `https://api.mpohoda.cz/v1`

---

## Doklady (Documents)

### Vydané faktury — IssuedInvoices

| Endpoint | Metoda | Popis |
|----------|--------|-------|
| `/v1/IssuedInvoices` | GET | Seznam vydaných faktur (stránkovaně) |
| `/v1/IssuedInvoices` | POST | Vytvoření vydané faktury |
| `/v1/IssuedInvoices/{id}` | GET | Detail faktury podle ID |
| `/v1/IssuedInvoices/{id}/pdf` | GET | Stažení PDF faktury |
| `/v1/IssuedInvoices/{id}/isdoc` | GET | Stažení ISDOC faktury |
| `/v1/IssuedInvoices/{id}/RestToPay` | GET | Zbývající částka k úhradě |
| `/v1/IssuedInvoices/Liquidation/{id}` | GET | Detail likvidace |
| `/v1/IssuedInvoices/Unpaid` | GET | Seznam nezaplacených faktur |
| `/v1/IssuedInvoices/{DocumentId}/Liquidate/Standalone/Fully` | POST | Plná likvidace faktury |
| `/v1/IssuedInvoices/{DocumentId}/Liquidate/Standalone/Partially` | POST | Částečná likvidace faktury |

### Přijaté faktury — ReceivedInvoices

| Endpoint | Metoda | Popis |
|----------|--------|-------|
| `/v1/ReceivedInvoices` | GET | Seznam přijatých faktur |
| `/v1/ReceivedInvoices` | POST | Vytvoření přijaté faktury |
| `/v1/ReceivedInvoices/{id}` | GET | Detail přijaté faktury |
| `/v1/ReceivedInvoices/{id}/pdf` | GET | Stažení PDF |

### Vydané objednávky — IssuedOrders

| Endpoint | Metoda | Popis |
|----------|--------|-------|
| `/v1/IssuedOrders` | GET | Seznam vydaných objednávek |
| `/v1/IssuedOrders` | POST | Vytvoření vydané objednávky |
| `/v1/IssuedOrders/{id}` | GET | Detail objednávky |
| `/v1/IssuedOrders/{id}/Transfer/ToReceivedInvoice/Fully` | POST | Přenos do přijaté faktury |
| `/v1/IssuedOrders/{id}/pdf` | GET | Stažení PDF |
| `/v1/IssuedOrders/{id}/status` | GET | Stav objednávky |

### Přijaté objednávky — ReceivedOrders

| Endpoint | Metoda | Popis |
|----------|--------|-------|
| `/v1/ReceivedOrders` | GET | Seznam přijatých objednávek |
| `/v1/ReceivedOrders` | POST | Vytvoření přijaté objednávky |
| `/v1/ReceivedOrders/{id}` | GET | Detail objednávky |
| `/v1/ReceivedOrders/{id}/Transfer/ToIssuedInvoice/Fully` | POST | Přenos do vydané faktury |
| `/v1/ReceivedOrders/{id}/pdf` | GET | Stažení PDF |
| `/v1/ReceivedOrders/{id}/status` | GET | Stav objednávky |

### Nabídky — IssuedOffers

| Endpoint | Metoda | Popis |
|----------|--------|-------|
| `/v1/IssuedOffers` | GET | Seznam nabídek |
| `/v1/IssuedOffers` | POST | Vytvoření nabídky |
| `/v1/IssuedOffers/{id}` | GET | Detail nabídky |
| `/v1/IssuedOffers/{id}/pdf` | GET | Stažení PDF |

### Výdejky — IssueSlips

| Endpoint | Metoda | Popis |
|----------|--------|-------|
| `/v1/IssueSlips` | GET | Seznam výdejek |
| `/v1/IssueSlips` | POST | Vytvoření výdejky |
| `/v1/IssueSlips/{id}` | GET | Detail výdejky |
| `/v1/IssueSlips/{id}/pdf` | GET | Stažení PDF |

### Zálohové faktury — IssuedAdvanceInvoices

| Endpoint | Metoda | Popis |
|----------|--------|-------|
| `/v1/IssuedAdvanceInvoices` | GET | Seznam zálohových faktur |
| `/v1/IssuedAdvanceInvoices` | POST | Vytvoření zálohové faktury |
| `/v1/IssuedAdvanceInvoices/{id}` | GET | Detail zálohové faktury |
| `/v1/IssuedAdvanceInvoices/{id}/RestToPay` | GET | Zbývající částka |
| `/v1/IssuedAdvanceInvoices/{id}/isdoc` | GET | Stažení ISDOC |
| `/v1/IssuedAdvanceInvoices/{id}/pdf` | GET | Stažení PDF |
| `/v1/IssuedAdvanceInvoices/Liquidation/{id}` | GET | Detail likvidace |
| `/v1/IssuedAdvanceInvoices/Unpaid` | GET | Nezaplacené zálohovky |
| `/v1/IssuedAdvanceInvoices/{DocumentId}/Liquidate/Standalone/Fully` | POST | Plná likvidace |

### Opravné daňové doklady — IssuedInvoiceCorrectiveTaxDocuments

| Endpoint | Metoda | Popis |
|----------|--------|-------|
| `/v1/IssuedInvoiceCorrectiveTaxDocuments` | GET | Seznam ODD |
| `/v1/IssuedInvoiceCorrectiveTaxDocuments` | POST | Vytvoření ODD |
| `/v1/IssuedInvoiceCorrectiveTaxDocuments/{id}` | GET | Detail ODD |
| `/v1/IssuedInvoiceCorrectiveTaxDocuments/{id}/pdf` | GET | Stažení PDF |

---

## Adresář (Directory)

### Odběratelé/dodavatelé — BusinessPartners

| Endpoint | Metoda | Popis |
|----------|--------|-------|
| `/v1/BusinessPartners` | GET | Seznam obchodních partnerů |
| `/v1/BusinessPartners` | POST | Vytvoření partnera |
| `/v1/BusinessPartners/{id}` | GET | Detail partnera |

### Ceníkové položky — PriceListItems

| Endpoint | Metoda | Popis |
|----------|--------|-------|
| `/v1/PriceListItems` | GET | Seznam ceníkových položek |
| `/v1/PriceListItems` | POST | Vytvoření položky |
| `/v1/PriceListItems/{id}` | GET | Detail položky |
| `/v1/PriceListItems/AvailableQuantities` | GET | Dostupné množství |
| `/v1/PriceListItems/SellingPrices` | GET | Prodejní ceny |
| `/v1/PriceListItems/{PriceListItemId}/RegistrationNumbers` | GET | Registrační čísla |

### Formy úhrady — PaymentMethods

| Endpoint | Metoda | Popis |
|----------|--------|-------|
| `/v1/PaymentMethods` | GET | Seznam forem úhrady |
| `/v1/PaymentMethods` | POST | Vytvoření formy úhrady |
| `/v1/PaymentMethods/{id}` | GET | Detail formy úhrady |

### Typy forem úhrady — PaymentMethodTypes

| Endpoint | Metoda | Popis |
|----------|--------|-------|
| `/v1/PaymentMethodTypes` | GET | Seznam typů úhrad |
| `/v1/PaymentMethodTypes/{id}` | GET | Detail typu úhrady |

### Bankovní účty — BankAccounts

| Endpoint | Metoda | Popis |
|----------|--------|-------|
| `/v1/BankAccounts` | GET | Seznam bankovních účtů |
| `/v1/BankAccounts` | POST | Vytvoření účtu |
| `/v1/BankAccounts/{id}` | GET | Detail účtu |

### Banky — Banks

| Endpoint | Metoda | Popis |
|----------|--------|-------|
| `/v1/Banks` | GET | Seznam bank |
| `/v1/Banks/{id}` | GET | Detail banky |

### Pokladny — CashRegisters

| Endpoint | Metoda | Popis |
|----------|--------|-------|
| `/v1/CashRegisters` | GET | Seznam pokladen |
| `/v1/CashRegisters` | POST | Vytvoření pokladny |
| `/v1/CashRegisters/{id}` | GET | Detail pokladny |

### Prodejní ceny — SellingPrices

| Endpoint | Metoda | Popis |
|----------|--------|-------|
| `/v1/SellingPrices` | GET | Seznam prodejních cen |
| `/v1/SellingPrices` | POST | Vytvoření prodejní ceny |
| `/v1/SellingPrices/{id}` | GET | Detail prodejní ceny |

### Registrační čísla — RegistrationNumbers

| Endpoint | Metoda | Popis |
|----------|--------|-------|
| `/v1/RegistrationNumbers` | GET | Seznam registračních čísel |
| `/v1/RegistrationNumbers` | POST | Vytvoření registračního čísla |
| `/v1/RegistrationNumbers/{id}` | GET | Detail registračního čísla |

---

## Nastavení (Settings)

### DPH sazby — VatRates

| Endpoint | Metoda | Popis |
|----------|--------|-------|
| `/v1/VatRates` | GET | Seznam DPH sazeb |
| `/v1/VatRates/{id}` | GET | Detail sazby |

### Měny — Currencies

| Endpoint | Metoda | Popis |
|----------|--------|-------|
| `/v1/Currencies` | GET | Seznam měn |
| `/v1/Currencies/{id}` | GET | Detail měny |

### Kurzy — ExchangeRates

| Endpoint | Metoda | Popis |
|----------|--------|-------|
| `/v1/ExchangeRates` | GET | Seznam kurzů |
| `/v1/ExchangeRates` | POST | Vytvoření kurzu |
| `/v1/ExchangeRates/{id}` | GET | Detail kurzu |

### Střediska — Centres

| Endpoint | Metoda | Popis |
|----------|--------|-------|
| `/v1/Centres` | GET | Seznam středisek |
| `/v1/Centres` | POST | Vytvoření střediska |
| `/v1/Centres/{id}` | GET | Detail střediska |

### Činnosti — Activities

| Endpoint | Metoda | Popis |
|----------|--------|-------|
| `/v1/Activities` | GET | Seznam činností |
| `/v1/Activities` | POST | Vytvoření činnosti |
| `/v1/Activities/{id}` | GET | Detail činnosti |

### Země — Countries

| Endpoint | Metoda | Popis |
|----------|--------|-------|
| `/v1/Countries` | GET | Seznam zemí |
| `/v1/Countries/{id}` | GET | Detail země |

### Kraje — Regions

| Endpoint | Metoda | Popis |
|----------|--------|-------|
| `/v1/Regions` | GET | Seznam krajů |
| `/v1/Regions/{id}` | GET | Detail kraje |

### PSČ — CityPostCodes

| Endpoint | Metoda | Popis |
|----------|--------|-------|
| `/v1/CityPostCodes` | GET | Seznam PSČ |
| `/v1/CityPostCodes/{id}` | GET | Detail PSČ |

### Provozovny — Establishments

| Endpoint | Metoda | Popis |
|----------|--------|-------|
| `/v1/Establishments` | GET | Seznam provozoven |
| `/v1/Establishments` | POST | Vytvoření provozovny |
| `/v1/Establishments/{id}` | GET | Detail provozovny |

---

## Struktura odpovědi

Všechny endpointy vrací odpověď ve standardním formátu:

```json
{
  "Data": {
    "Items": [ ... ],
    "TotalCount": 100,
    "PageNumber": 1,
    "PageSize": 10
  },
  "Errors": [],
  "Warnings": []
}
```

### Chybové odpovědi

```json
{
  "Errors": [
    {
      "Code": "ErrorCode",
      "Message": "Popis chyby",
      "Detail": "Detailní informace"
    }
  ]
}
```

---

## Stránkování

GET endpointy podporují stránkování pomocí query parametrů:

| Parametr | Typ | Výchozí | Popis |
|----------|-----|---------|-------|
| `pageNumber` | int | 1 | Číslo stránky |
| `pageSize` | int | 10 | Velikost stránky (max 100) |

Příklad:
```
GET /v1/IssuedInvoices?pageNumber=2&pageSize=50
```

---

## Rychlé odkazy

- [Hlavní skill](../SKILL.md) — Přehled celého API
- [Autentizace](../references/autentizace.md) — Jak se přihlásit
- [Průvodci](../references/pruvodci.md) — Návody krok za krokem
- [SDK](../references/sdk.md) — C# SDK pro práci s endpointy
- [Struktura dat](../references/struktura-dat.md) — Formáty, chybové kódy

---

**Synchronizováno s:** api.mpohoda.cz/swagger/v1/swagger.json  
**Verze:** 1.0.0  
**Celkem endpointů:** 78
