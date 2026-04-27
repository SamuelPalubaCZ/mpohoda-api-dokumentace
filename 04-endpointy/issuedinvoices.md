# IssuedInvoices

## GET /v1/IssuedInvoices

**Issued invoices paginated.**

Gets all <b>Issued invoices</b> by specified pagination.

---

## POST /v1/IssuedInvoices

**Creates Issued invoice.**

Creates <b>Issued invoice</b> by passed payload.

---

## POST /v1/IssuedInvoices/{DocumentId}/Liquidate/Standalone/Fully

**Creates Liquidation.**

Creates <b>Liquidation</b> by passed payload.

---

## POST /v1/IssuedInvoices/{DocumentId}/Liquidate/Standalone/Partially

**Creates Liquidation.**

Creates <b>Liquidation</b> by passed payload.

---

## GET /v1/IssuedInvoices/{id}

**Gets Issued invoice by id.**

Retrieves <b>Issued invoice</b> by passed id, that cannot be empty.

---

## GET /v1/IssuedInvoices/{id}/isdoc

**Issued invoice ISDOC by id.**

Retrieves <b>Issued invoice</b> ISDOC.

---

## GET /v1/IssuedInvoices/{id}/pdf

**Issued invoice pdf by id.**

Retrieves <b>Issued invoice</b> pdf by id in specified language.

---

## GET /v1/IssuedInvoices/{id}/RestToPay

**Gets Document payment status by id.**

Retrieves <b>Document payment status</b> by passed id, that cannot be empty.

---

## GET /v1/IssuedInvoices/Liquidation/{id}

**Gets Liquidation by id.**

Retrieves <b>Liquidation</b> by passed id, that cannot be empty.

---

## GET /v1/IssuedInvoices/Unpaid

**Document payment statuses paginated.**

Gets all <b>Document payment statuses</b> by specified pagination.

---

