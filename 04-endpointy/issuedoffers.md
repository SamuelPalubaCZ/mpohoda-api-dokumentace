# issuedoffers

## `/v1/IssuedOffers`

### GET

**Issued offers paginated.**

Gets all **Issued offers** by specified pagination.

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

### POST

**Creates Issued offer.**

Creates **Issued offer** by passed payload.

#### Tělo požadavku

- **Content-Type:** `application/json`
- **Schéma:** `CreateIssuedOfferDto`

#### Odpovědi

- **201** - Created
- **400** - Bad Request
- **401** - Unauthorized
- **403** - Forbidden
- **404** - Not Found
- **422** - Unprocessable Entity
- **429** - Too Many Requests

---

## `/v1/IssuedOffers/{id}`

### GET

**Gets Issued offer by id.**

Retrieves **Issued offer** by passed id, that cannot be empty.

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

## `/v1/IssuedOffers/{id}/pdf`

### GET

**Issued offer pdf by id.**

Retrieves **Issued offer** pdf by id in specified language.

#### Parametry

| Název | Typ | Umístění | Povinné | Popis |
|-------|-----|----------|---------|-------|
| id | string | path | Ano |  |
| Language |  | query | Ano |  |

#### Odpovědi

- **200** - Pdf file
- **204** - No Content
- **401** - Unauthorized
- **403** - Forbidden
- **404** - Not Found
- **422** - Unprocessable Entity
- **429** - Too Many Requests

---
