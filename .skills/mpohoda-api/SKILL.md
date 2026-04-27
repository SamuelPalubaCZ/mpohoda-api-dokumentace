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

## Hlavní entity (endpointy)

### Doklady
- **IssuedInvoices** — Vydané faktury (včetně PDF, ISDOC, likvidace, úhrady)
- **ReceivedInvoices** — Přijaté faktury
- **IssuedOrders** — Vydané objednávky (včetně přenosu do přijaté faktury)
- **ReceivedOrders** — Přijaté objednávky (včetně přenosu do vydané faktury)
- **IssuedOffers** — Nabídky
- **IssueSlips** — Výdejky
- **IssuedAdvanceInvoices** — Zálohové faktury
- **IssuedInvoiceCorrectiveTaxDocuments** — Opravné daňové doklady

### Adresář
- **BusinessPartners** — Odběratelé/dodavatelé
- **PriceListItems** — Ceníkové položky (skladové zásoby)
- **PaymentMethods** — Formy úhrady
- **BankAccounts** — Bankovní účty
- **CashRegisters** — Pokladny

### Nastavení
- **VatRates** — DPH sazby
- **Currencies** — Měny
- **ExchangeRates** — Kurzy
- **Centres** — Střediska
- **Activities** — Činnosti
- **Countries** — Země
- **Regions** — Kraje
- **Establishments** — Provozovny

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
**Celkem endpointů:** 78  
**Celkem průvodců:** 5
