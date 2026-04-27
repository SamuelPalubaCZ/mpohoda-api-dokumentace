---
name: mpohoda-api-pruvodci
description: |
  Návody a průvodci pro mPohoda API - vytvoření faktury, objednávky, 
  Postman, Swagger UI, navázané záznamy. 
  Použij tento skill při dotazech na "jak na to", tutoriály, 
  příklady kódu, Postman, Swagger, vytvoření faktury/objednávky.
---

# mPohoda API - Průvodci

## Rychlý start

### 1. Získání přístupových údajů

Nejdříve potřebujete API klíč nebo OAuth2 klienta:

1. Přihlaste se do [mPohoda](https://app.mpohoda.cz) jako **administrátor**
2. Otevřete agendu **API**
3. Vygenerujte:
   - **API klíč** (jednodušší) nebo
   - **Client ID + Client Secret** (bezpečnější)

### 2. První požadavek

#### S API klíčem:

```bash
curl -X GET "https://api.mpohoda.cz/v1/BusinessPartners?pageSize=10&pageNumber=1" \
  -H "Api-Key: váš-api-klíč"
```

#### S tokenem:

```bash
# 1. Získání tokenu
curl -X POST "https://ucet.pohoda.cz/connect/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=client_credentials" \
  -d "client_id=váše-client-id" \
  -d "client_secret=váš-client-secret" \
  -d "scope=Mph.OpenApi.Access.Cz"

# 2. Použití tokenu
curl -X GET "https://api.mpohoda.cz/v1/BusinessPartners?pageSize=10&pageNumber=1" \
  -H "Authorization: Bearer získaný-token"
```

---

## Průvodce: Postman

### Instalace

1. Stáhněte [Postman](https://www.postman.com/downloads/)
2. Importujte [oficiální kolekci](https://api.mpohoda.cz/postman/v1/collection_cz.json)

### Nastavení autentizace

1. Vytvořte **novou kolekci**
2. Na záložce **Authorization** vyberte:
   - **API Key** → zadejte API klíč do hlavičky `Api-Key`
   - **Bearer Token** → zadejte token
   - **OAuth 2.0** → konfigurace pro automatické získávání tokenu:
     - Access Token URL: `https://ucet.pohoda.cz/connect/token`
     - Client ID: z agendy API
     - Client Secret: z agendy API
     - Scope: `Mph.OpenApi.Access.Cz`

### Odeslání požadavku

1. Vytvořte **nový požadavek** (HTTP)
2. Zvolte metodu (GET/POST)
3. Zadejte URL: `https://api.mpohoda.cz/v1/{endpoint}`
4. Na záložce **Body** → **raw** → **JSON** zadejte data
5. Klikněte **Send**

---

## Průvodce: Swagger UI

1. Otevřete [Swagger UI](https://api.mpohoda.cz/swagger/index.html)
2. Klikněte na **Authorize**
3. Zadejte:
   - **ApiKeyAuth**: váš API klíč, nebo
   - **Oauth2**: Client ID + Client Secret + scope
4. Klikněte **Authorize** → **Close**
5. Najděte požadovaný endpoint
6. Klikněte **Try it out**
7. Vyplňte parametry a klikněte **Execute**

---

## Průvodce: Navázané záznamy

### Co je navázaný záznam?

Navázaným záznamem je např. forma úhrady, bankovní účet, zásoba nebo odběratel. 
Každý má unikátní **ID**, které musíte znát při vytváření dokladu.

### Získání ID odběratele

```bash
curl -X GET "https://api.mpohoda.cz/v1/BusinessPartners?pageSize=100" \
  -H "Authorization: Bearer ***"
```

V odpovědi najděte:
```json
{
  "Data": {
    "Items": [
      {
        "Id": "9423064b-5842-450d-9d31-cca121b8e034",
        "Name": "STORMWARE s.r.o.",
        "...": "..."
      }
    ]
  }
}
```

### Získání ID formy úhrady

```bash
curl -X GET "https://api.mpohoda.cz/v1/PaymentMethods" \
  -H "Authorization: Bearer ***"
```

### Získání ID bankovního účtu

```bash
curl -X GET "https://api.mpohoda.cz/v1/BankAccounts" \
  -H "Authorization: Bearer ***"
```

---

## Průvodce: Vytvoření faktury

### Použitý endpoint

```http
POST https://api.mpohoda.cz/v1/IssuedInvoices
```

### Příklad: Faktura s textovými položkami

```bash
curl -X POST "https://api.mpohoda.cz/v1/IssuedInvoices" \
  -H "Authorization: Bearer ***" \
  -H "Content-Type: application/json" \
  -d '{
    "Text": "Fakturujeme Vám zboží dle objednávky:",
    "IssueDate": "2024-01-15",
    "DueDate": "2024-01-29",
    "TaxDate": "2024-01-15",
    "PaymentMethodId": "e9001046-a210-49fe-bb5d-ee463b88ca9d",
    "BankAccountId": "b61898b3-3ed1-4cb5-b099-475ea32d79fe",
    "BusinessPartnerAddress": {
      "DocumentAddressWithAddressBookLink": {
        "Id": "9423064b-5842-450d-9d31-cca121b8e034"
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
        "TextItem": {
          "Text": "Polozka 2",
          "Quantity": 2,
          "Unit": "hod",
          "UnitPrice": 500,
          "UnitPriceType": "WithVat",
          "VatRateType": "FirstReducedVatRate"
        }
      }
    ]
  }'
```

### Příklad: Faktura se skladovými položkami

```json
{
  "Text": "Faktura za zboží",
  "IssueDate": "2024-01-15",
  "BusinessPartnerAddress": {
    "DocumentAddressWithAddressBookLink": {
      "Id": "9423064b-5842-450d-9d31-cca121b8e034"
    }
  },
  "Items": [
    {
      "PriceListItem": {
        "PriceListItemId": "5bed760c-ac9d-451c-bb2d-96c353319d01",
        "Quantity": 4
      }
    }
  ]
}
```

> **Tip:** U skladových položek stačí zadat `PriceListItemId` a `Quantity` — 
> cena a DPH se načtou automaticky z ceníku.

### Typy položek

| Typ | Popis | Povinná pole |
|-----|-------|--------------|
| `TextItem` | Textová položka | `Text`, `Quantity`, `UnitPrice`, `UnitPriceType`, `VatRateType` |
| `PriceListItem` | Skladová položka | `PriceListItemId`, `Quantity` |

### Typy cen

| Hodnota | Popis |
|---------|-------|
| `WithoutVat` | Cena bez DPH |
| `WithVat` | Cena s DPH |

### Typy DPH sazeb

| Hodnota | Popis |
|---------|-------|
| `ZeroVatRate` | 0% DPH |
| `BasicVatRate` | Základní sazba (21%) |
| `FirstReducedVatRate` | 1. snížená sazba (15%) |
| `SecondReducedVatRate` | 2. snížená sazba (10%) |

---

## Průvodce: Vytvoření faktury z objednávky

### Použitý endpoint

```http
POST https://api.mpohoda.cz/v1/ReceivedOrders/{id}/Transfer/ToIssuedInvoice/Fully
```

### Podmínky

- Objednávka musí mít stav **Nevyřízená**
- Přenos je vždy **kompletní** (všechny položky)
- Částečný přenos není podporován

### Příklad

```bash
curl -X POST "https://api.mpohoda.cz/v1/ReceivedOrders/550e8400-e29b-41d4-a716-446655440000/Transfer/ToIssuedInvoice/Fully" \
  -H "Authorization: Bearer ***" \
  -H "Content-Type: application/json" \
  -d '{}'
```

> **Poznámka:** Tělo požadavku je prázdné `{}` — vše se přenese z objednávky.

---

## Průvodce: Stažení PDF

```bash
curl -X GET "https://api.mpohoda.cz/v1/IssuedInvoices/550e8400-e29b-41d4-a716-446655440000/pdf" \
  -H "Authorization: Bearer ***" \
  --output faktura.pdf
```

---

## Rychlé odkazy

- [Hlavní skill](../SKILL.md) — Přehled celého API
- [Autentizace](../references/autentizace.md) — Jak se přihlásit
- [Endpointy](../references/endpointy.md) — Seznam všech API metod
- [SDK](../references/sdk.md) — C# SDK
- [Struktura dat](../references/struktura-dat.md) — Formáty, chybové kódy

---

**Synchronizováno s:** api.mpohoda.cz/doc/guides  
**Verze:** 1.0.0
