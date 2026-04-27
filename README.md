# mPohoda API - Kompletní dokumentace

## Základní informace

**API URL:** `https://api.mpohoda.cz/v1`

**Autentizační server:** `https://ucet.pohoda.cz`

**Aplikace mPohoda:** `https://app.mpohoda.cz`

**Swagger UI:** https://api.mpohoda.cz/swagger/index.html

**Redoc:** https://api.mpohoda.cz/redoc

**OpenAPI specifikace:** https://api.mpohoda.cz/swagger/v1/swagger.json

**Postman kolekce:** [Ke stažení](postman/v1/collection_cz.json)

---

## Obsah dokumentace

1. [Úvod a rychlý start](01-uvod/) - Jak začít s API
2. [Autentizace](02-autentizace/) - Způsoby přihlášení a bezpečnost
3. [Struktura dat](03-struktura-dat/) - Formát odpovědí a chybové kódy
4. [Endpointy](04-endpointy/) - Kompletní popis všech API metod
5. [Průvodci](05-pruvodci/) - Návody krok za krokem
6. [Podpora](06-podpora/) - Changelog a FAQ
7. [SDK](07-sdk/) - Knihovny pro vývojáře
8. [Swagger](swagger/) - OpenAPI specifikace

---

## Doporučení

> Doporučujeme průběžně sledovat [Changelog](06-podpora/changelog.md), kde je historie zapracovaných změn.

> Pro vývojáře je k dispozici také [SDK pro C#](07-sdk/csharp-sdk.md).

---

## Způsoby autentizace

API mPohoda podporuje dva způsoby autentizace:

1. **API klíč** - Jednoduchý přístup pomocí statického klíče
2. **Přístupový token** - Bezpečnější OAuth2 přístup (doporučeno)

> Z hlediska větší bezpečnosti doporučujeme použít přístup pomocí přístupového tokenu.

---

## Základní struktura

### Požadavek

```http
GET https://api.mpohoda.cz/v1/BusinessPartners?pageSize=10&pageNumber=1
Api-Key: váš-api-klíč
```

nebo s tokenem:

```http
GET https://api.mpohoda.cz/v1/BusinessPartners?pageSize=10&pageNumber=1
Authorization: Bearer váš-token
```

### Odpověď

```json
{
  "data": [...],
  "pageSize": 10,
  "pageNumber": 1,
  "totalCount": 150,
  "totalPages": 15
}
```

---

*Dokumentace vytvořena na základě oficiální dokumentace mPohoda API.*
