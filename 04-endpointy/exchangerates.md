# exchangerates

## `/v1/ExchangeRates`

### GET

**Exchange rate sets paginated.**

Gets all **Exchange rate sets** by specified pagination.

#### Parametry

| Název | Typ | Umístění | Povinné | Popis |
|-------|-----|----------|---------|-------|
| PageSize | integer | query | Ano | Page size. |
| PageNumber | integer | query | Ano | Page number. |
| ModifiedSince | string | query | Ne | Basic filter for modified since. |

#### Odpovědi

- **200** - Success
- **401** - Unauthorized
- **403** - Forbidden
- **422** - Unprocessable Entity
- **429** - Too Many Requests

---

## `/v1/ExchangeRates/{id}`

### GET

**Gets Exchange rate set by id.**

Retrieves **Exchange rate set** by passed id, that cannot be empty.

#### Parametry

| Název | Typ | Umístění | Povinné | Popis |
|-------|-----|----------|---------|-------|
| id | string | path | Ano |  |

#### Odpovědi

- **200** - Success
- **401** - Unauthorized
- **403** - Forbidden
- **404** - Not Found
- **422** - Unprocessable Entity
- **429** - Too Many Requests

---
