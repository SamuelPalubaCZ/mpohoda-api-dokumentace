# IssuedOrders

## GET /v1/IssuedOrders

**Issued orders paginated.**

Gets all <b>Issued orders</b> by specified pagination.

---

## POST /v1/IssuedOrders

**Creates Issued order.**

Creates <b>Issued order</b> by passed payload.

---

## GET /v1/IssuedOrders/{id}

**Gets Issued order by id.**

Retrieves <b>Issued order</b> by passed id, that cannot be empty.

---

## GET /v1/IssuedOrders/{id}/pdf

**Issued order pdf by id.**

Retrieves <b>Issued order</b> pdf by id in specified language.

---

## GET /v1/IssuedOrders/{id}/status

**Gets Order status enum by id.**

Retrieves <b>Order status enum</b> by passed id, that cannot be empty.

---

## POST /v1/IssuedOrders/{id}/Transfer/ToReceivedInvoice/Fully

**Full transfer to Received invoice.**

Fully transfers <b>Issued order</b> specified by id to new <b>Received invoice</b>.

---

