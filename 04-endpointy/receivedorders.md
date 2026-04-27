# ReceivedOrders

## GET /v1/ReceivedOrders

**Received orders paginated.**

Gets all <b>Received orders</b> by specified pagination.

---

## POST /v1/ReceivedOrders

**Creates Received order.**

Creates <b>Received order</b> by passed payload.

---

## GET /v1/ReceivedOrders/{id}

**Gets Received order by id.**

Retrieves <b>Received order</b> by passed id, that cannot be empty.

---

## GET /v1/ReceivedOrders/{id}/pdf

**Received order pdf by id.**

Retrieves <b>Received order</b> pdf by id in specified language.

---

## GET /v1/ReceivedOrders/{id}/status

**Gets Order status enum by id.**

Retrieves <b>Order status enum</b> by passed id, that cannot be empty.

---

## POST /v1/ReceivedOrders/{id}/Transfer/ToIssuedInvoice/Fully

**Full transfer to Issued invoice.**

Fully transfers <b>Received order</b> specified by id to new <b>Issued invoice</b>.

---

