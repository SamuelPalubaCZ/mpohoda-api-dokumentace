---
name: mpohoda-api
description: |
  Kompletní skill pro práci s mPohoda API (api.mpohoda.cz). 
  Použij tento skill VŽDY, když uživatel zmíní mPohoda, Stormware, faktury, 
  objednávky, sklad, ceník, nebo jakoukoliv integraci s účetním systémem mPohoda.
  Skill pokrývá: autentizaci (API klíč/token), všechny 78 endpointů, průvodce 
  vytvořením faktur/objednávek, SDK pro C#, Swagger/OpenAPI specifikaci.
  
  Tento skill je hlavní router — načte se při každém dotazu na mPohoda API 
  a deleguje na specializované pod-skilly podle kontextu.
category: api-integration
version: 1.0.0
author: Samuel Paluba
---

# mPohoda API Skill

## Přehled

Tento skill poskytuje kompletní podporu pro integraci s **mPohoda API** 
(https://api.mpohoda.cz). Dokumentace je synchronizována 1:1 s oficiální 
dokumentací na api.mpohoda.cz/doc.

## Struktura skill systému

```
mpohoda-api/
├── SKILL.md                    ← Tento soubor - hlavní router
├── references/
    ├── autentizace.md          ← API klíč, OAuth2 token, zásady bezpečnosti
    ├── endpointy.md            ← Kompletní seznam všech 78 endpointů
    ├── struktura-dat.md        ← HTTP konvence, kódy chyb, stránkování
    ├── pruvodci.md             ← Návody: faktury, objednávky, Postman, Swagger
    ├── sdk.md                  ← C# SDK, NuGet balíčky, příklady kódu
    ├── exporty.md              ← PDF export, ISDOC export
    ├── pokrocile-operace.md    ← Likvidace, přenosy, stavy, platby, sklad, ceny
    └── doklady.md              ← Vydané/přijaté faktury, objednávky, nabídky, výdejky
└── scripts/
    ├── validate-request.py     ← Validace požadavků na API
    ├── generate-invoice.py     ← Generování JSON pro fakturu
    └── check-endpoint.py       ← Kontrola dostupnosti endpointu
```

## Kdy použít který reference

| Dotaz uživatele | Načíst reference |
|-----------------|------------------|
| "Jak se autentizovat?" | `references/autentizace.md` |
| "Jaký je endpoint pro...?" | `references/endpointy.md` |
| "Jak vytvořit fakturu?" | `references/pruvodci.md` |
| "Jaký je formát odpovědi?" | `references/struktura-dat.md` |
| "Jak použít SDK?" | `references/sdk.md` |
| "PDF export" | `references/exporty.md` |
| "ISDOC export" | `references/exporty.md` |
| "Likvidace, úhrada" | `references/pokrocile-operace.md` |
| "Přenos objednávky" | `references/pokrocile-operace.md` |
| "Stav objednávky" | `references/pokrocile-operace.md` |
| "Dostupné množství" | `references/pokrocile-operace.md` |
| "Prodejní ceny" | `references/pokrocile-operace.md` |
| "Validace požadavku" | `scripts/validate-request.py` |

## Základní URL

| Služba | URL |
|--------|-----|
| API | `https://api.mpohoda.cz/v1` |
| Autentizační server | `https://ucet.pohoda.cz` |
| Swagger UI | `https://api.mpohoda.cz/swagger/index.html` |
| ReDoc | `https://api.mpohoda.cz/redoc` |
| OpenAPI spec | `https://api.mpohoda.cz/swagger/v1/swagger.json` |
| Postman kolekce | `https://api.mpohoda.cz/postman/v1/collection_cz.json` |

## Rychlé odkazy na průvodce

1. [Autentizace](../references/autentizace.md) — API klíč vs token
2. [Endpointy](../references/endpointy.md) — Seznam všech API metod
3. [Průvodci](../references/pruvodci.md) — Jak vytvořit fakturu, objednávku
4. [SDK](../references/sdk.md) — C# NuGet balíčky
5. [Struktura dat](../references/struktura-dat.md) — Formáty, chybové kódy

## Autentizace - základní přehled

API podporuje dva způsoby autentizace:

### 1. API klíč (jednodušší)
```http
Api-Key: váš-api-klíč
```

### 2. OAuth2 token (bezpečnější - doporučeno)
```bash
# Získání tokenu
curl -X POST "https://ucet.pohoda.cz/connect/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=client_credentials" \
  -d "client_id=váše-client-id" \
  -d "client_secret=váš-client-secret" \
  -d "scope=Mph.OpenApi.Access.Cz"
```

```http
Authorization: Bearer získaný-token
```

> **Důležité:** Token má omezenou platnost (expires_in). Po vypršení je nutné získat nový.

## Kompletní seznam všech 87 endpointů

### Doklady (41 endpointů)

#### Vydané faktury — `IssuedInvoices` (10)
| Metoda | Endpoint | Popis |
|--------|----------|-------|
| GET | `/v1/IssuedInvoices` | Seznam vydaných faktur |
| POST | `/v1/IssuedInvoices` | Vytvoření vydané faktury |
| GET | `/v1/IssuedInvoices/{id}` | Detail vydané faktury |
| GET | `/v1/IssuedInvoices/{id}/pdf` | PDF vydané faktury |
| GET | `/v1/IssuedInvoices/{id}/isdoc` | ISDOC vydané faktury |
| GET | `/v1/IssuedInvoices/{id}/RestToPay` | Zbývající částka k úhradě |
| GET | `/v1/IssuedInvoices/Unpaid` | Seznam nezaplacených faktur |
| POST | `/v1/IssuedInvoices/{id}/Liquidate/Standalone/Fully` | Plná likvidace |
| POST | `/v1/IssuedInvoices/{id}/Liquidate/Standalone/Partially` | Částečná likvidace |
| GET | `/v1/IssuedInvoices/Liquidation/{id}` | Detail likvidace |

#### Přijaté faktury — `ReceivedInvoices` (4)
| Metoda | Endpoint | Popis |
|--------|----------|-------|
| GET | `/v1/ReceivedInvoices` | Seznam přijatých faktur |
| POST | `/v1/ReceivedInvoices` | Vytvoření přijaté faktury |
| GET | `/v1/ReceivedInvoices/{id}` | Detail přijaté faktury |
| GET | `/v1/ReceivedInvoices/{id}/pdf` | PDF přijaté faktury |

#### Vydané objednávky — `IssuedOrders` (6)
| Metoda | Endpoint | Popis |
|--------|----------|-------|
| GET | `/v1/IssuedOrders` | Seznam vydaných objednávek |
| POST | `/v1/IssuedOrders` | Vytvoření vydané objednávky |
| GET | `/v1/IssuedOrders/{id}` | Detail vydané objednávky |
| GET | `/v1/IssuedOrders/{id}/pdf` | PDF vydané objednávky |
| GET | `/v1/IssuedOrders/{id}/status` | Stav objednávky |
| POST | `/v1/IssuedOrders/{id}/Transfer/ToReceivedInvoice/Fully` | Přenos do přijaté faktury |

#### Přijaté objednávky — `ReceivedOrders` (6)
| Metoda | Endpoint | Popis |
|--------|----------|-------|
| GET | `/v1/ReceivedOrders` | Seznam přijatých objednávek |
| POST | `/v1/ReceivedOrders` | Vytvoření přijaté objednávky |
| GET | `/v1/ReceivedOrders/{id}` | Detail přijaté objednávky |
| GET | `/v1/ReceivedOrders/{id}/pdf` | PDF přijaté objednávky |
| GET | `/v1/ReceivedOrders/{id}/status` | Stav objednávky |
| POST | `/v1/ReceivedOrders/{id}/Transfer/ToIssuedInvoice/Fully` | Přenos do vydané faktury |

#### Nabídky — `IssuedOffers` (4)
| Metoda | Endpoint | Popis |
|--------|----------|-------|
| GET | `/v1/IssuedOffers` | Seznam nabídek |
| POST | `/v1/IssuedOffers` | Vytvoření nabídky |
| GET | `/v1/IssuedOffers/{id}` | Detail nabídky |
| GET | `/v1/IssuedOffers/{id}/pdf` | PDF nabídky |

#### Výdejky — `IssueSlips` (4)
| Metoda | Endpoint | Popis |
|--------|----------|-------|
| GET | `/v1/IssueSlips` | Seznam výdejek |
| POST | `/v1/IssueSlips` | Vytvoření výdejky |
| GET | `/v1/IssueSlips/{id}` | Detail výdejky |
| GET | `/v1/IssueSlips/{id}/pdf` | PDF výdejky |

#### Zálohové faktury — `IssuedAdvanceInvoices` (9)
| Metoda | Endpoint | Popis |
|--------|----------|-------|
| GET | `/v1/IssuedAdvanceInvoices` | Seznam zálohových faktur |
| POST | `/v1/IssuedAdvanceInvoices` | Vytvoření zálohové faktury |
| GET | `/v1/IssuedAdvanceInvoices/{id}` | Detail zálohové faktury |
| GET | `/v1/IssuedAdvanceInvoices/{id}/pdf` | PDF zálohové faktury |
| GET | `/v1/IssuedAdvanceInvoices/{id}/isdoc` | ISDOC zálohové faktury |
| GET | `/v1/IssuedAdvanceInvoices/{id}/RestToPay` | Zbývající částka |
| GET | `/v1/IssuedAdvanceInvoices/Unpaid` | Nezaplacené zálohovky |
| POST | `/v1/IssuedAdvanceInvoices/{id}/Liquidate/Standalone/Fully` | Plná likvidace |
| GET | `/v1/IssuedAdvanceInvoices/Liquidation/{id}` | Detail likvidace |

#### Opravné daňové doklady — `IssuedInvoiceCorrectiveTaxDocuments` (3)
| Metoda | Endpoint | Popis |
|--------|----------|-------|
| GET | `/v1/IssuedInvoiceCorrectiveTaxDocuments` | Seznam ODD |
| GET | `/v1/IssuedInvoiceCorrectiveTaxDocuments/{id}` | Detail ODD |
| GET | `/v1/IssuedInvoiceCorrectiveTaxDocuments/{id}/pdf` | PDF ODD |

### Adresář a sklad (14 endpointů)

#### Odběratelé/dodavatelé — `BusinessPartners` (3)
| Metoda | Endpoint | Popis |
|--------|----------|-------|
| GET | `/v1/BusinessPartners` | Seznam obchodních partnerů |
| POST | `/v1/BusinessPartners` | Vytvoření obchodního partnera |
| GET | `/v1/BusinessPartners/{id}` | Detail obchodního partnera |

#### Ceníkové položky — `PriceListItems` (5)
| Metoda | Endpoint | Popis |
|--------|----------|-------|
| GET | `/v1/PriceListItems` | Seznam ceníkových položek |
| GET | `/v1/PriceListItems/{id}` | Detail ceníkové položky |
| POST | `/v1/PriceListItems/AvailableQuantities` | Dostupné množství |
| POST | `/v1/PriceListItems/SellingPrices` | Prodejní ceny |
| GET | `/v1/PriceListItems/{id}/RegistrationNumbers` | Registrační čísla |

#### Prodejní ceny — `SellingPrices` (2)
| Metoda | Endpoint | Popis |
|--------|----------|-------|
| GET | `/v1/SellingPrices` | Seznam prodejních cen |
| GET | `/v1/SellingPrices/{id}` | Detail prodejní ceny |

#### Registrační čísla — `RegistrationNumbers` (2)
| Metoda | Endpoint | Popis |
|--------|----------|-------|
| GET | `/v1/RegistrationNumbers` | Seznam registračních čísel |
| GET | `/v1/RegistrationNumbers/{id}` | Detail registračního čísla |

#### Formy úhrady — `PaymentMethods` (3)
| Metoda | Endpoint | Popis |
|--------|----------|-------|
| GET | `/v1/PaymentMethods` | Seznam forem úhrady |
| POST | `/v1/PaymentMethods` | Vytvoření formy úhrady |
| GET | `/v1/PaymentMethods/{id}` | Detail formy úhrady |

#### Typy plateb — `PaymentMethodTypes` (2)
| Metoda | Endpoint | Popis |
|--------|----------|-------|
| GET | `/v1/PaymentMethodTypes` | Seznam typů plateb |
| GET | `/v1/PaymentMethodTypes/{id}` | Detail typu platby |

### Nastavení systému (22 endpointů)

#### DPH sazby — `VatRates` (2)
| Metoda | Endpoint | Popis |
|--------|----------|-------|
| GET | `/v1/VatRates` | Seznam DPH sazeb |
| GET | `/v1/VatRates/{id}` | Detail DPH sazby |

#### Měny — `Currencies` (2)
| Metoda | Endpoint | Popis |
|--------|----------|-------|
| GET | `/v1/Currencies` | Seznam měn |
| GET | `/v1/Currencies/{id}` | Detail měny |

#### Kurzy — `ExchangeRates` (2)
| Metoda | Endpoint | Popis |
|--------|----------|-------|
| GET | `/v1/ExchangeRates` | Seznam kurzových lístků |
| GET | `/v1/ExchangeRates/{id}` | Detail kurzového lístku |

#### Banky — `Banks` (2)
| Metoda | Endpoint | Popis |
|--------|----------|-------|
| GET | `/v1/Banks` | Seznam bank |
| GET | `/v1/Banks/{id}` | Detail banky |

#### Bankovní účty — `BankAccounts` (2)
| Metoda | Endpoint | Popis |
|--------|----------|-------|
| GET | `/v1/BankAccounts` | Seznam bankovních účtů |
| GET | `/v1/BankAccounts/{id}` | Detail bankovního účtu |

#### Pokladny — `CashRegisters` (2)
| Metoda | Endpoint | Popis |
|--------|----------|-------|
| GET | `/v1/CashRegisters` | Seznam pokladen |
| GET | `/v1/CashRegisters/{id}` | Detail pokladny |

#### Střediska — `Centres` (2)
| Metoda | Endpoint | Popis |
|--------|----------|-------|
| GET | `/v1/Centres` | Seznam středisek |
| GET | `/v1/Centres/{id}` | Detail střediska |

#### Činnosti — `Activities` (2)
| Metoda | Endpoint | Popis |
|--------|----------|-------|
| GET | `/v1/Activities` | Seznam činností |
| GET | `/v1/Activities/{id}` | Detail činnosti |

#### Země — `Countries` (2)
| Metoda | Endpoint | Popis |
|--------|----------|-------|
| GET | `/v1/Countries` | Seznam zemí |
| GET | `/v1/Countries/{id}` | Detail země |

#### Kraje — `Regions` (2)
| Metoda | Endpoint | Popis |
|--------|----------|-------|
| GET | `/v1/Regions` | Seznam krajů |
| GET | `/v1/Regions/{id}` | Detail kraje |

#### PSČ — `CityPostCodes` (2)
| Metoda | Endpoint | Popis |
|--------|----------|-------|
| GET | `/v1/CityPostCodes` | Seznam PSČ |
| GET | `/v1/CityPostCodes/{id}` | Detail PSČ |

#### Provozovny — `Establishments` (2)
| Metoda | Endpoint | Popis |
|--------|----------|-------|
| GET | `/v1/Establishments` | Seznam provozoven |
| GET | `/v1/Establishments/{id}` | Detail provozovny |

## Souhrn endpointů podle kategorie

| Kategorie | Endpointů | Entity |
|-----------|-----------|--------|
| **Doklady** | 41 | 8 entit |
| **Adresář a sklad** | 14 | 6 entit |
| **Nastavení systému** | 22 | 11 entit |
| **CELKEM** | **87** | **25 entit** |

## Práce s tímto skillem

### Krok 1: Identifikace záměru
Urči, co uživatel chce:
- Vytvořit/číst/aktualizovat/smazat záznam?
- Jaký typ záznamu (faktura, objednávka, odběratel)?
- Jakou autentizaci používá?

### Krok 2: Načtení reference
Na základě záměru načti příslušný reference soubor:
```
Pro faktury → references/pruvodci.md (sekce Vydané faktury)
Pro endpointy → references/endpointy.md (vyhledej konkrétní endpoint)
Pro autentizaci → references/autentizace.md
```

### Krok 3: Sestavení požadavku
Použij informace z reference k sestavení:
- HTTP metoda (GET/POST/PUT/DELETE)
- URL endpointu
- Hlavičky (autentizace)
- Tělo požadavku (JSON)

### Krok 4: Validace
Použij script `scripts/validate-request.py` pro kontrolu struktury požadavku.

### Krok 5: Zpracování odpovědi
Odpověď obsahuje standardní strukturu:
```json
{
  "Data": { ... },
  "Errors": [ ... ],
  "Warnings": [ ... ]
}
```

## Příklady použití

### Vytvoření faktury
```bash
curl -X POST "https://api.mpohoda.cz/v1/IssuedInvoices" \
  -H "Authorization: Bearer ***" \
  -H "Content-Type: application/json" \
  -d '{
    "Text": "Faktura za zboží",
    "IssueDate": "2024-01-15",
    "DueDate": "2024-01-29",
    "BusinessPartnerAddress": {
      "DocumentAddressWithAddressBookLink": { "Id": "..." }
    },
    "Items": [{
      "TextItem": {
        "Text": "Polozka 1",
        "Quantity": 1,
        "UnitPrice": 1000,
        "UnitPriceType": "WithoutVat",
        "VatRateType": "BasicVatRate"
      }
    }]
  }'
```

### Stažení seznamu odběratelů
```bash
curl -X GET "https://api.mpohoda.cz/v1/BusinessPartners?pageSize=10&pageNumber=1" \
  -H "Authorization: Bearer ***"
```

## Chybové kódy

| Kód | Význam |
|-----|--------|
| 400 | Bad Request - špatný formát požadavku |
| 401 | Unauthorized - chybí/špatná autentizace |
| 403 | Forbidden - nedostatečná práva |
| 404 | Not Found - záznam nenalezen |
| 422 | Unprocessable Entity - validační chyba |
| 429 | Too Many Requests - rate limit |

## Odkazy

- Oficiální dokumentace: https://api.mpohoda.cz/doc
- Swagger UI: https://api.mpohoda.cz/swagger/index.html
- ReDoc: https://api.mpohoda.cz/redoc
- GitHub tohoto repozitáře: https://github.com/SamuelPalubaCZ/mpohoda-api-dokumentace

---

**Verze:** 1.0.0  
**Synchronizováno s:** api.mpohoda.cz/doc (2026-04-27)  
**Celkem endpointů:** 87  
**Celkem průvodců:** 5
