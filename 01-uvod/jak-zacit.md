# Jak začít

## Přehled

API mPohoda podporuje dva způsoby autentizace:

- **API klíč** - Jednoduchý statický klíč
- **Přístupový token** - OAuth2 token (doporučeno)

> Z hlediska větší bezpečnosti doporučujeme použít přístup pomocí přístupového tokenu.

## Základní URL

```
https://api.mpohoda.cz/v1
```

## První požadavek

### S API klíčem:

```bash
curl -X GET "https://api.mpohoda.cz/v1/BusinessPartners?pageSize=10&pageNumber=1"   -H "Api-Key: váš-api-klíč"
```

### S tokenem:

```bash
curl -X GET "https://api.mpohoda.cz/v1/BusinessPartners?pageSize=10&pageNumber=1"   -H "Authorization: Bearer váš-token"
```

## Nástroje pro testování

- [Swagger UI](https://api.mpohoda.cz/swagger/index.html)
- [Postman](https://www.postman.com/downloads/) - [kolekce ke stažení](https://api.mpohoda.cz/postman/v1/collection_cz.json)

> Pro vývojáře je k dispozici také SDK pro C#.
