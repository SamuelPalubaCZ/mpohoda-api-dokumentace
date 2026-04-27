# issuedinvoices

## `/v1/IssuedInvoices`

### GET

**Issued invoices paginated.**

Gets all **Issued invoices** by specified pagination.

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

**Creates Issued invoice.**

Creates **Issued invoice** by passed payload.

#### Tělo požadavku

- **Content-Type:** `application/json`
- **Schéma:** `CreateIssuedInvoiceDto`

#### Odpovědi

- **201** - Created
- **400** - Bad Request
- **401** - Unauthorized
- **403** - Forbidden
- **404** - Not Found
- **422** - Unprocessable Entity
- **429** - Too Many Requests

---

## `/v1/IssuedInvoices/Liquidation/{id}`

### GET

**Gets Liquidation by id.**

Retrieves **Liquidation** by passed id, that cannot be empty.

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

## `/v1/IssuedInvoices/Unpaid`

### GET

**Document payment statuses paginated.**

Gets all **Document payment statuses** by specified pagination.

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

## `/v1/IssuedInvoices/{DocumentId}/Liquidate/Standalone/Fully`

### POST

**Creates Liquidation.**

Creates **Liquidation** by passed payload.

#### Parametry

| Název | Typ | Umístění | Povinné | Popis |
|-------|-----|----------|---------|-------|
| DocumentId | string | path | Ano | Issued invoice id. |

#### Tělo požadavku

- **Content-Type:** `application/json`
- **Schéma:** `CreateFullIssuedInvoiceLiquidationDto`

#### Odpovědi

- **201** - Created
- **400** - Bad Request
- **401** - Unauthorized
- **403** - Forbidden
- **404** - Not Found
- **422** - Unprocessable Entity
- **429** - Too Many Requests

---

## `/v1/IssuedInvoices/{DocumentId}/Liquidate/Standalone/Partially`

### POST

**Creates Liquidation.**

Creates **Liquidation** by passed payload.

#### Parametry

| Název | Typ | Umístění | Povinné | Popis |
|-------|-----|----------|---------|-------|
| DocumentId | string | path | Ano | Issued invoice id. |

#### Tělo požadavku

- **Content-Type:** `application/json`
- **Schéma:** `CreatePartialIssuedInvoiceLiquidationDto`

#### Odpovědi

- **201** - Created
- **400** - Bad Request
- **401** - Unauthorized
- **403** - Forbidden
- **404** - Not Found
- **422** - Unprocessable Entity
- **429** - Too Many Requests

---

## `/v1/IssuedInvoices/{id}`

### GET

**Gets Issued invoice by id.**

Retrieves **Issued invoice** by passed id, that cannot be empty.

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

## `/v1/IssuedInvoices/{id}/RestToPay`

### GET

**Gets Document payment status by id.**

Retrieves **Document payment status** by passed id, that cannot be empty.

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

## `/v1/IssuedInvoices/{id}/isdoc`

### GET

**Issued invoice ISDOC by id.**

Retrieves **Issued invoice** ISDOC.

#### Parametry

| Název | Typ | Umístění | Povinné | Popis |
|-------|-----|----------|---------|-------|
| id | string | path | Ano |  |

#### Odpovědi

- **200** - Pdf file
- **204** - No Content
- **401** - Unauthorized
- **403** - Forbidden
- **404** - Not Found
- **422** - Unprocessable Entity
- **429** - Too Many Requests

---

## `/v1/IssuedInvoices/{id}/pdf`

### GET

**Issued invoice pdf by id.**

Retrieves **Issued invoice** pdf by id in specified language.

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
