# pricelistitems

## `/v1/PriceListItems`

### GET

**Price list items paginated.**

Gets all **Price list items** by specified pagination.

#### Parametry

| Název | Typ | Umístění | Povinné | Popis |
|-------|-----|----------|---------|-------|
| After | string | query | Ne | Key set pagination after specified id. |
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

## `/v1/PriceListItems/AvailableQuantities`

### POST

**Price list item available quantity by ids.**

Retrieves **Price list item available quantities** or information about parent entities by passed ids.

#### Tělo požadavku

- **Content-Type:** `application/json`
- **Schéma:** `ByIdListRequest`

#### Odpovědi

- **200** - Success
- **401** - Unauthorized
- **403** - Forbidden
- **422** - Unprocessable Entity
- **429** - Too Many Requests

---

## `/v1/PriceListItems/SellingPrices`

### POST

**Price list item with selling prices by ids.**

Retrieves **Price list item with selling prices** or information about parent entities by passed ids.

#### Tělo požadavku

- **Content-Type:** `application/json`
- **Schéma:** `ByIdListRequest`

#### Odpovědi

- **200** - Success
- **401** - Unauthorized
- **403** - Forbidden
- **422** - Unprocessable Entity
- **429** - Too Many Requests

---

## `/v1/PriceListItems/{PriceListItemId}/RegistrationNumbers`

### GET

**Registration numbers paginated.**

Gets all **Registration numbers** by specified pagination.

#### Parametry

| Název | Typ | Umístění | Povinné | Popis |
|-------|-----|----------|---------|-------|
| PriceListItemId | string | path | Ano | Price list item id. |
| After | string | query | Ne | Key set pagination after specified id. |
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

## `/v1/PriceListItems/{id}`

### GET

**Gets Price list item by id.**

Retrieves **Price list item** by passed id, that cannot be empty.

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
