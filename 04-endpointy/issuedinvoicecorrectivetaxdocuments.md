# issuedinvoicecorrectivetaxdocuments

## `/v1/IssuedInvoiceCorrectiveTaxDocuments`

### GET

**Issued invoice corrective tax documents paginated.**

Gets all **Issued invoice corrective tax documents** by specified pagination.

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

## `/v1/IssuedInvoiceCorrectiveTaxDocuments/{id}`

### GET

**Gets Issued invoice corrective tax document by id.**

Retrieves **Issued invoice corrective tax document** by passed id, that cannot be empty.

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

## `/v1/IssuedInvoiceCorrectiveTaxDocuments/{id}/pdf`

### GET

**Issued invoice corrective tax document pdf by id.**

Retrieves **Issued invoice corrective tax document** pdf by id in specified language.

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
