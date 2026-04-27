---
name: mpohoda-api-exporty
description: |
  Exporty a tiskové sestavy v mPohoda API - PDF, ISDOC.
  Použij tento skill při dotazech na generování PDF faktur, ISDOC export,
  tiskové sestavy, stažení dokladů jako PDF.
  
  Pokrývá: IssuedInvoices, ReceivedInvoices, IssuedOrders, ReceivedOrders,
  IssuedOffers, IssueSlips, IssuedAdvanceInvoices, IssuedInvoiceCorrectiveTaxDocuments.
---

# mPohoda API - Exporty (PDF, ISDOC)

## Přehled

Tento skill pokrývá exportní operace pro všechny doklady.

| Formát | Popis | Content-Type |
|--------|-------|--------------|
| **PDF** | Tisková sestava dokladu | `application/pdf` |
| **ISDOC** | Elektronický daňový doklad | `application/xml` |

---

## PDF Export

### Podporované doklady

| Doklad | Endpoint |
|--------|----------|
| Vydaná faktura | `GET /v1/IssuedInvoices/{id}/pdf` |
| Přijatá faktura | `GET /v1/ReceivedInvoices/{id}/pdf` |
| Vydaná objednávka | `GET /v1/IssuedOrders/{id}/pdf` |
| Přijatá objednávka | `GET /v1/ReceivedOrders/{id}/pdf` |
| Nabídka | `GET /v1/IssuedOffers/{id}/pdf` |
| Výdejka | `GET /v1/IssueSlips/{id}/pdf` |
| Zálohová faktura | `GET /v1/IssuedAdvanceInvoices/{id}/pdf` |
| ODD | `GET /v1/IssuedInvoiceCorrectiveTaxDocuments/{id}/pdf` |

### Stažení PDF faktury

```bash
# Stažení do souboru
curl -X GET "https://api.mpohoda.cz/v1/IssuedInvoices/550e8400-e29b-41d4-a716-446655440000/pdf" \
  -H "Authorization: Bearer ***" \
  --output faktura.pdf

# Stažení s určením jazyka
curl -X GET "https://api.mpohoda.cz/v1/IssuedInvoices/550e8400-e29b-41d4-a716-446655440000/pdf?language=Cz" \
  -H "Authorization: Bearer ***" \
  --output faktura.pdf
```

### Jazykové varianty

| Kód | Jazyk |
|-----|-------|
| `Cz` | Čeština |
| `Sk` | Slovenština |
| `En` | Angličtina |
| `De` | Němčina |

### Odpověď

- **200 OK** — PDF soubor v těle odpovědi
- **204 No Content** — Doklad nemá PDF (např. ještě nebyl vytištěn)
- **404 Not Found** — Doklad neexistuje

---

## ISDOC Export

### Podporované doklady

| Doklad | Endpoint |
|--------|----------|
| Vydaná faktura | `GET /v1/IssuedInvoices/{id}/isdoc` |
| Zálohová faktura | `GET /v1/IssuedAdvanceInvoices/{id}/isdoc` |

### Stažení ISDOC

```bash
curl -X GET "https://api.mpohoda.cz/v1/IssuedInvoices/550e8400-e29b-41d4-a716-446655440000/isdoc" \
  -H "Authorization: Bearer ***" \
  --output faktura.isdoc.xml
```

### Co je ISDOC?

ISDOC je český standard pro elektronickou fakturaci:
- XML formát s elektronickým podpisem
- Umožňuje automatické zpracování v účetních systémech
- Podporuje EDI (Electronic Data Interchange)

---

## Hromadný export

### Hromadné stažení PDF

```python
#!/usr/bin/env python3
"""Hromadné stažení PDF faktur"""

import requests
import os

API_KEY = "váš-api-klíč"
BASE_URL = "https://api.mpohoda.cz/v1"

# Seznam ID faktur k exportu
invoice_ids = [
    "550e8400-e29b-41d4-a716-446655440000",
    "550e8400-e29b-41d4-a716-446655440001",
    "550e8400-e29b-41d4-a716-446655440002"
]

# Vytvoření adresáře
os.makedirs("pdf_export", exist_ok=True)

# Stažení jednotlivých PDF
for invoice_id in invoice_ids:
    url = f"{BASE_URL}/IssuedInvoices/{invoice_id}/pdf"
    headers = {"Api-Key": API_KEY}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        filename = f"pdf_export/faktura_{invoice_id}.pdf"
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"✅ Staženo: {filename}")
    else:
        print(f"❌ Chyba {response.status_code}: {invoice_id}")
```

---

## Rychlé odkazy

- [Hlavní skill](../SKILL.md) — Přehled celého API
- [Autentizace](../references/autentizace.md) — Jak se přihlásit
- [Doklady](../references/doklady.md) — Faktury, objednávky
- [SDK](../references/sdk.md) — C# SDK (podpora PDF exportu)

---

**Synchronizováno s:** api.mpohoda.cz/doc  
**Verze:** 1.0.0
