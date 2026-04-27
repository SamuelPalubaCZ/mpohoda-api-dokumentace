# issuedadvanceinvoices

## `/v1/IssuedAdvanceInvoices`

### GET

**Issued advance invoices paginated.**

Gets all **Issued advance invoices** by specified pagination.

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

**Creates Issued advance invoice.**

Creates **Issued advance invoice** by passed payload.

#### Tělo požadavku

- **Content-Type:** `application/json`
- **Schéma:** `CreateIssuedAdvanceInvoiceDto`

#### Odpovědi

- **201** - Created
- **400** - Bad Request
- **401** - Unauthorized
- **403** - Forbidden
- **404** - Not Found
- **422** - Unprocessable Entity
- **429** - Too Many Requests

---

## `/v1/IssuedAdvanceInvoices/Liquidation/{id}`

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

## `/v1/IssuedAdvanceInvoices/Unpaid`

### GET

**Document payment statuses paginated.**

Gets all **Document payment statuses** by specified pagination.

#### Parametry

| Název | Typ | Umístění | Povinné | Popis |
|-------|-----|----------|---------|-------|
| After | string | query | Ne |  |
| PageSize | integer | query | Ano |  |
| PageNumber | integer | query | Ano |  |
| ModifiedSince | string | query | Ne |  |

#### Odpovědi

- **200** - Success
- **401** - Unauthorized
- **403** - Forbidden
- **422** - Unprocessable Entity
- **429** - Too Many Requests

---

## `/v1/IssuedAdvanceInvoices/{DocumentId}/Liquidate/Standalone/Fully`

### POST

**Creates Liquidation.**

Creates **Liquidation** by passed payload.

#### Parametry

| Název | Typ | Umístění | Povinné | Popis |
|-------|-----|----------|---------|-------|
| DocumentId | string | path | Ano | Issued invoice id. |

#### Tělo požadavku

- **Content-Type:** `application/json`
- **Schéma:** `CreateFullIssuedAdvanceInvoiceLiquidationDto`

#### Odpovědi

- **201** - Created
- **400** - Bad Request
- **401** - Unauthorized
- **403** - Forbidden
- **404** - Not Found
- **422** - Unprocessable Entity
- **429** - Too Many Requests

---

## `/v1/IssuedAdvanceInvoices/{id}`

### GET

**Gets Issued advance invoice by id.**

Retrieves **Issued advance invoice** by passed id, that cannot be empty.

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

## `/v1/IssuedAdvanceInvoices/{id}/RestToPay`

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

## `/v1/IssuedAdvanceInvoices/{id}/isdoc`

### GET

**Issued advance invoice ISDOC by id.**

Retrieves **Issued advance invoice** ISDOC.

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

## `/v1/IssuedAdvanceInvoices/{id}/pdf`

### GET

**Advance invoice pdf by id.**

Retrieves **Advance invoice** pdf by id in specified language.

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
