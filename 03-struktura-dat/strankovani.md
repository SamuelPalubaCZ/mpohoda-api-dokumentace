# Stránkování

## Parametry stránkování

| Parametr | Typ | Popis |
|----------|-----|-------|
| `PageSize` | integer | Počet položek na stránku (povinné) |
| `PageNumber` | integer | Číslo stránky (povinné) |
| `After` | string | Key set pagination after specified id |
| `ModifiedSince` | date-time | Filtr pro změny od určitého data |

## Příklad

```bash
curl -X GET "https://api.mpohoda.cz/v1/BusinessPartners?pageSize=10&pageNumber=1"   -H "Api-Key: váš-api-klíč"
```
