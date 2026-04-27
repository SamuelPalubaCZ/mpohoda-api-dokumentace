# receivedorders

## `/v1/ReceivedOrders`

### GET

**Received orders paginated.**

Gets all **Received orders** by specified pagination.

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

**Creates Received order.**

Creates **Received order** by passed payload.

#### Tělo požadavku

- **Content-Type:** `application/json`
- **Schéma:** `CreateReceivedOrderDto`

#### Odpovědi

- **201** - Created
- **400** - Bad Request
- **401** - Unauthorized
- **403** - Forbidden
- **404** - Not Found
- **422** - Unprocessable Entity
- **429** - Too Many Requests

---

## `/v1/ReceivedOrders/{id}`

### GET

**Gets Received order by id.**

Retrieves **Received order** by passed id, that cannot be empty.

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

## `/v1/ReceivedOrders/{id}/Transfer/ToIssuedInvoice/Fully`

### POST

**Full transfer to Issued invoice.**

Fully transfers **Received order** specified by id to new **Issued invoice**.

#### Parametry

| Název | Typ | Umístění | Povinné | Popis |
|-------|-----|----------|---------|-------|
| id | string | path | Ano |  |

#### Odpovědi

- **201** - Created
- **400** - Bad Request
- **401** - Unauthorized
- **403** - Forbidden
- **404** - Not Found
- **422** - Unprocessable Entity
- **429** - Too Many Requests

---

## `/v1/ReceivedOrders/{id}/pdf`

### GET

**Received order pdf by id.**

Retrieves **Received order** pdf by id in specified language.

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

## `/v1/ReceivedOrders/{id}/status`

### GET

**Gets Order status enum by id.**

Retrieves **Order status enum** by passed id, that cannot be empty.

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
