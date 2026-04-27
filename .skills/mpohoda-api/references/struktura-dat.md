---
name: mpohoda-api-struktura-dat
description: |
  Struktura dat, HTTP konvence, kódy chyb a varování, stránkování 
  pro mPohoda API. Použij tento skill při dotazech na formát odpovědi, 
  HTTP hlavičky, chybové kódy, stránkování, JSON strukturu.
---

# mPohoda API - Struktura dat

## HTTP konvence

### Hlavičky požadavku

Všechny požadavky musí obsahovat:

| Hlavička | Hodnota | Popis |
|----------|---------|-------|
| `Content-Type` | `application/json` | Pro POST/PUT požadavky |
| `Api-Key` | `váš-api-klíč` | Autentizace API klíčem |
| `Authorization` | `Bearer váš-token` | Autentizace tokenem |

### HTTP metody

| Metoda | Použití |
|--------|---------|
| `GET` | Čtení dat (seznam, detail) |
| `POST` | Vytvoření nového záznamu |
| `PUT` | Aktualizace existujícího záznamu |
| `DELETE` | Smazání záznamu |

### URL formát

```
https://api.mpohoda.cz/v1/{Endpoint}[/{id}][/{akce}]
```

Příklady:
- `GET /v1/IssuedInvoices` — seznam faktur
- `GET /v1/IssuedInvoices/123` — detail faktury 123
- `POST /v1/IssuedInvoices` — vytvoření faktury
- `GET /v1/IssuedInvoices/123/pdf` — PDF faktury

---

## Struktura odpovědi

### Úspěšná odpověď (200 OK)

```json
{
  "Data": {
    "Items": [
      {
        "Id": "550e8400-e29b-41d4-a716-446655440000",
        "LastUpdate": "2024-01-15T10:30:00Z",
        "...": "..."
      }
    ],
    "TotalCount": 150,
    "PageNumber": 1,
    "PageSize": 10
  },
  "Errors": [],
  "Warnings": []
}
```

### Prázdná odpověď (204 No Content)

Některé operace vrací `204 No Content` (např. generování PDF když není k dispozici).

### Chybová odpověď (400 Bad Request)

```json
{
  "Data": null,
  "Errors": [
    {
      "Code": "ValidationError",
      "Message": "Pole 'IssueDate' je povinné.",
      "Detail": "..."
    }
  ],
  "Warnings": []
}
```

---

## Kódy chyb

### HTTP status kódy

| Kód | Význam | Kdy nastane |
|-----|--------|-------------|
| `200` | OK | Úspěšné zpracování GET požadavku |
| `201` | Created | Úspěšné vytvoření záznamu (POST) |
| `204` | No Content | Operace úspěšná, ale bez návratových dat |
| `400` | Bad Request | Špatný formát požadavku, validační chyba |
| `401` | Unauthorized | Chybí nebo je neplatná autentizace |
| `403` | Forbidden | Nedostatečná práva pro operaci |
| `404` | Not Found | Požadovaný záznam neexistuje |
| `422` | Unprocessable Entity | Validace selhala (např. chybí povinné pole) |
| `429` | Too Many Requests | Překročen rate limit |

### Interní chybové kódy

| Kód | Popis |
|-----|-------|
| `ValidationError` | Pole neprošlo validací |
| `NotFound` | Záznam nenalezen |
| `AlreadyExists` | Záznam již existuje |
| `Unauthorized` | Neplatné přístupové údaje |
| `Forbidden` | Nedostatečná práva |

---

## Kódy varování

Varování nezastaví zpracování, ale upozorní na potenciální problém:

```json
{
  "Warnings": [
    {
      "Code": "WarningCode",
      "Message": "Upozornění na možný problém"
    }
  ]
}
```

---

## Stránkování

GET endpointy podporují stránkování:

| Parametr | Typ | Výchozí | Popis |
|----------|-----|---------|-------|
| `pageNumber` | integer | 1 | Číslo stránky (od 1) |
| `pageSize` | integer | 10 | Počet položek na stránku (max 100) |

### Příklad

```bash
curl -X GET "https://api.mpohoda.cz/v1/IssuedInvoices?pageNumber=2&pageSize=50" \
  -H "Authorization: Bearer ***"
```

### Odpověď s stránkováním

```json
{
  "Data": {
    "Items": [ ... ],
    "TotalCount": 150,
    "PageNumber": 2,
    "PageSize": 50
  }
}
```

---

## Formáty dat

### Datum a čas

Všechny datumy jsou ve formátu **ISO 8601**:

```json
"IssueDate": "2024-01-15T10:30:00Z"
```

Nebo pouze datum:

```json
"IssueDate": "2024-01-15"
```

### Čísla

- Ceny: desetinná čísla (např. `1000.50`)
- Množství: desetinná čísla (např. `2.5`)
- ID: UUID formát (např. `550e8400-e29b-41d4-a716-446655440000`)

### Měna

Ceny jsou vždy v **měně firmy** (výchozí CZK). Pro jinou měnu použijte `CurrencyId`.

---

## Rychlé odkazy

- [Hlavní skill](../SKILL.md) — Přehled celého API
- [Autentizace](../references/autentizace.md) — Jak se přihlásit
- [Endpointy](../references/endpointy.md) — Seznam všech API metod
- [Průvodci](../references/pruvodci.md) — Návody krok za krokem
- [SDK](../references/sdk.md) — C# SDK

---

**Synchronizováno s:** api.mpohoda.cz/doc  
**Verze:** 1.0.0
